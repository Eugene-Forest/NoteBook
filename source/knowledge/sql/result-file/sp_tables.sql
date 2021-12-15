-- 这是 sp_tables 存储过程的实现
ALTER procedure [sys].[sp_tables]
(
    @table_name         nvarchar(384)   = null,
    @table_owner        nvarchar(384)   = null,
    @table_qualifier    sysname = null,
    @table_type         varchar(100) = null,
    @fUsePattern        bit = 1 -- To allow users to explicitly disable all pattern matching.
)
as
    declare @type1      varchar(3)
    declare @qual_name  nvarchar(517) -- [schema].[table]
    declare @table_id   int

    if @table_qualifier = '%' and @table_owner = '' and @table_name = ''
    begin
        -- Debug output, do not remove it.
        -- print 'Special feature #1:  enumerate databases when owner and name are blank but qualifier is explicitly "%".'
        select
            TABLE_QUALIFIER = convert(sysname,d.name),
            TABLE_OWNER     = convert(sysname,null),
            TABLE_NAME      = convert(sysname,null),
            TABLE_TYPE      = convert(varchar(32),null),
            REMARKS         = convert(varchar(254),null)    -- Remarks are NULL.
        from
            sys.databases d
        where
            d.name <> 'model' -- eliminate MODEL database
        order by 1
        return
    end

    if @table_qualifier = '' and @table_owner = '%' and @table_name = ''
    begin
        -- Debug output, do not remove it.
        -- print 'Special feature #2:  enumerate owners when qualifier and name are blank but owner is explicitly "%".
        select distinct
            TABLE_QUALIFIER = convert(sysname,null),
            TABLE_OWNER     = convert(sysname,schema_name(o.schema_id)),
            TABLE_NAME      = convert(sysname,null),
            TABLE_TYPE      = convert(varchar(32),null),
            REMARKS         = convert(varchar(254),null)    -- Remarks are NULL.
        from
            sys.all_objects o
        where
            o.type in ('S','U','V')  -- limit columns to tables and views only
        order by 2
        return
    end

    if @table_qualifier = '' and @table_owner = '' and @table_name = '' and @table_type = '%'
    begin
        -- Debug output, do not remove it.
        -- print 'Special feature #3:  enumerate table types when qualifier, owner and name are blank but table type is explicitly "%".'
        select
            TABLE_QUALIFIER = convert(sysname,null),
            TABLE_OWNER     = convert(sysname,null),
            TABLE_NAME      = convert(sysname,null),
            TABLE_TYPE      = convert(varchar(32),
                                        rtrim(substring('SYSTEM TABLETABLE       VIEW',(c.column_id-1)*12+1,12))),
            REMARKS         = convert(varchar(254),null)    -- Remarks are NULL.
        from
            sys.all_objects o,
            sys.all_columns c
        where
            o.object_id = c.object_id and o.object_id = object_id('sysusers') and
            c.column_id <= 3 -- ISSUE - what is this for ???
        return
    end

    --
    -- End of special features - do normal processing.
    --

    if @table_qualifier is not null
    begin
        if db_name() <> @table_qualifier
        begin
            if @table_qualifier = ''
            begin  -- If empty qualifier supplied, force an empty result set.
                select @table_name = ''
                select @table_owner = ''
            end
            else
            begin   -- If qualifier doesn't match current database.
                raiserror (15250, -1,-1)
                return
            end
        end
    end
    select @table_qualifier = null -- it's not needed anymore

    if @table_type is null
    begin   -- Select all ODBC supported table types.
        select @type1 = 'SUV'
    end
    else
    begin
        -- TableType is case sensitive if CS server.
        if (charindex('''SYSTEM TABLE''',@table_type) <> 0)
            select @type1 = 'S' -- Add System Tables.
        else
            select @type1 = ''
        if (charindex('''TABLE''',@table_type) <> 0)
            select @type1 = @type1 + 'U' -- Add User Tables.
        if (charindex('''VIEW''',@table_type) <> 0)
            select @type1 = @type1 + 'V' -- Add Views.
    end

    if @table_name is not null
    begin
        if (@table_owner is null) and (charindex('%', @table_name) = 0)
        begin   -- If owner not specified and table contains wildchar.
            if exists
            (
                select
                        *
                from
                        sys.all_objects o
                where
                        o.schema_id = schema_id() and
                        o.object_id = object_id(@table_name) and
                        o.type in ('U','V','S')
            )
            begin   -- Override supplied owner w/owner of table.
                select @table_owner = schema_name()
            end
        end
    end

    select @qual_name = isnull(quotename(@table_owner), '') + '.' + quotename(@table_name)
    select @table_id = object_id(@qual_name)

    if (@fUsePattern = 1) -- Does the user want it?
    begin
        if ((isnull(charindex('%', @table_name),0) = 0) and
            (isnull(charindex('_', @table_name),0) = 0) and
            (isnull(charindex('%', @table_owner),0) = 0) and
            (isnull(charindex('_', @table_owner),0) = 0) and
            (@table_id is not null))
        begin
            select @fUsePattern = 0 -- not a single wild char, so go the fast way.
        end
    end

    if @fUsePattern = 0
    begin
        /* -- Debug output, do not remove it.
        print '*************'
        print 'There is NO pattern matching.'
        print @fUsePattern
        print isnull(@table_name, '@table_name = null')
        print isnull(@table_owner, '@table_owner = null')
        print isnull(@table_type, '@table_type = null')
        print isnull(@type1, '@type1 = null')
        print '*************'
        */
        select
            TABLE_QUALIFIER = convert(sysname,db_name()),
            TABLE_OWNER     = convert(sysname,schema_name(o.schema_id)),
            TABLE_NAME      = convert(sysname,o.name),
            TABLE_TYPE      = convert(varchar(32),
                                        rtrim(substring('SYSTEM TABLE            TABLE       VIEW       ',
                                        (ascii(o.type)-83)*12+1,12))  -- 'S'=0,'U'=2,'V'=3
                                     ),
            REMARKS = convert(varchar(254),null)    -- Remarks are NULL.

        from
            sys.all_objects o

        where
            o.object_id = @table_id and
            (o.type in ('U','V') or 
                (o.type in ('S') and has_perms_by_name(@qual_name, 'object', 'select') = 1)) and
            charindex(substring(o.type,1,1),@type1) <> 0 -- Only desired types.
        order by 4, 1, 2, 3
    end
    else
    begin
        /* -- Debug output, do not remove it.
        print '*************'
        print 'THERE IS pattern matching!'
        print @fUsePattern
        print isnull(@table_name, '@table_name = null')
        print isnull(@table_owner, '@table_owner = null')
        print isnull(@table_type, '@table_type = null')
        print isnull(@type1, '@type1 = null')
        print '*************'
        */
        select
            TABLE_QUALIFIER = convert(sysname,db_name()),
            TABLE_OWNER     = convert(sysname,schema_name(o.schema_id)),
            TABLE_NAME      = convert(sysname,o.name),
            TABLE_TYPE      = convert(varchar(32),
                                        rtrim(substring('SYSTEM TABLE            TABLE       VIEW       ',
                                              (ascii(o.type)-83)*12+1,
                                              12))  -- 'S'=0,'U'=2,'V'=3
                                     ),
            REMARKS = convert(varchar(254),null)    -- Remarks are NULL.

        from
            sys.all_objects o

        where
            (o.type in ('U','V') or 
                (o.type in ('S') and has_perms_by_name(quotename(schema_name(o.schema_id)) + '.' + quotename(o.name), 'object', 'select') = 1)) and
            charindex(substring(o.type,1,1),@type1) <> 0 and -- Only desired types.
            (@table_name  is NULL or o.name like @table_name) and
            (@table_owner is NULL or schema_name(o.schema_id) like @table_owner)
        order by 4, 1, 2, 3
    end
GO