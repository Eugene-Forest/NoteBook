ALTER PROCEDURE drop_all_tables
AS
BEGIN
    -- 创建表名游标，通过游标来循环遍历
    DECLARE tablesCursor CURSOR FOR 
        SELECT name
    FROM sys.tables
    DECLARE @tableName VARCHAR(255)
    BEGIN
        -- 打开游标
        OPEN tablesCursor
        --将游标向下移1行，获取的数据放入之前定义的变量@tableName
        FETCH NEXT FROM tablesCursor INTO @tableName
        --判断是否成功获取数据
        WHILE @@FETCH_STATUS = 0
        BEGIN
            exec('drop '+@tableName)
            PRINT @tableName
            --将游标向下移1行，获取的数据放入之前定义的变量@tableName
            FETCH NEXT FROM tablesCursor INTO @tableName
        END
        CLOSE tablesCursor
    END
END