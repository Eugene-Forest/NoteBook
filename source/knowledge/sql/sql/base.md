# 数据库和表的基本操作

## 查看数据库系统的所有数据库

:::{note}
对于 SQL Server 来说，获取一些基本信息常常需要使用系统定义的存储过程。
:::

### SQL Server 下查看数据库系统的所有数据库

查看数据库(系统)的所有数据库有以下方法：

- 通过存储过程 `sp_databases` （注意：该存储过程是系统级的，在任意数据库都可以使用且效果一样）
- 通过查询 `sys.databases`

#### sp_databases

```sql
-- 系统存储过程 : sp_databases
ALTER procedure [sys].[sp_databases]
as
   set nocount on

   select
      DATABASE_NAME   = db_name(s_mf.database_id),
      DATABASE_SIZE   = convert(int,
                                    case -- more than 2TB(maxint) worth of pages (by 8K each) can not fit an int...
                                    when sum(convert(bigint,s_mf.size)) >= 268435456
                                    then null
                                    else sum(convert(bigint,s_mf.size))*8 -- Convert from 8192 byte pages to Kb
                                    end),
      REMARKS         = convert(varchar(254),null)
   from
      sys.master_files s_mf
   where
      s_mf.state = 0 and -- ONLINE
      has_dbaccess(db_name(s_mf.database_id)) = 1 -- Only look at databases to which we have access
   group by s_mf.database_id
   order by 1
GO
```

```{eval-rst}
.. csv-table:: sp_databases 运行结果
   :file: ../result-file/sp_databases.csv
   :header-rows: 1
   :align: center
```

#### 查询 sys.databases

通过执行查询命令 `SELECT name AS database_name,database_id,collation_name FROM sys.databases` 来查看所有数据库。

```{eval-rst}
.. csv-table::  查询 sys.databases 的运行结果
   :file: ../result-file/sys.databases.csv
   :header-rows: 1
   :align: center

```

### MySQL 下查看数据库系统的所有数据库

MySQL 下的查看方法为： `show databases`

```mysql
mysql> show databases;
+---------------------+
| Database            |
+---------------------+
| information_schema  |
| ...                 |
| yggl                |
+---------------------+
20 rows in set (0.00 sec)
```

```{raw} html
<hr width='50%'>
```

## 使用数据库系统中的某个数据库

使用 `use` 关键字使用或更换使用的数据库，这个是 sql 通用的命令关键字。

命令形如 `use target_database`

```{raw} html
<hr width='50%'>
```

:::{note}
这个方法通用于 SQL Server 和 MySQL 。
:::

## 查看数据库的全部表

### SQL Server 下查看数据库的全部表

有以下方法

- 通过存储过程 `sp_tables` （注意：该存储过程是系统级的）
- 通过查询 `sys.tables`

:::{note}
由于 sp_tables 的实现代码长且复杂，同时如果不带参数地执行该存储过程，那么其结果将包含该库的所有表（一般来说我们只需要看 dbo 部分的表）。同时为节省篇幅，所以不将其展示。{download}`sp_tables 存储过程 <../result-file/sp_tables.sql>` [^id11]
:::

#### 使用带有参数的 sp_tables

不带有参数的 sp_tables 运行产生的结果比较不具备可用性且没有目的性。

让我们通过定义看看 sp_tables 的参数有哪些：

```sql
stored procedure learning_sql_server.sys.sp_tables
   @table_name nvarchar(384) = null, @table_owner nvarchar(384) = null,
   @table_qualifier sysname = null, @table_type varchar(100) = null,
   @fUsePattern bit = 1
```

sp_tables 的参数:

- `table_name` : 表名
- `table_owner` : 表的所有者;（一般查询的都为 dbo ,还有 sys 和 INFORMATION_SCHEMA）
- `table_qualifier` : 对象限定符； **对象限定符的数据库名称部分必须是当前数据库的名称** ，一般 null 。
- `table_type` : 表的类型，有 `TABLE` 和 `VIEW` 以及 `SYSTEM TABLE`

:::{attention}
`sp_tables null,null,null,null` 是等同于 `sp_tables` 的。
:::

```sql
-- 执行存储过程
sp_tables NULL,dbo,NULL,"'TABLE'"
GO
```

```{eval-rst}
.. csv-table::  执行带参数的 sp_tables 的运行结果
   :file: ../result-file/sp_tables.csv
   :header-rows: 1
   :align: center
```

#### 查询 sys.tables

```sql
-- 执行查询
SELECT name,type,type_desc FROM sys.tables
GO
```

```{eval-rst}
.. csv-table::  查询 sys.tables 的运行结果
   :file: ../result-file/sys.tables.csv
   :header-rows: 1
   :align: center
```

```{raw} html
<hr width='50%'>
```

### MySQL 下查看数据库的全部表

- use target_database;
- show tables;

```mysql
mysql> use employees;
Database changed
mysql> show tables;
+----------------------+
| Tables_in_employees  |
+----------------------+
| current_dept_emp     |
| departments          |
| dept_emp             |
| dept_emp_latest_date |
| dept_manager         |
| employees            |
| salaries             |
| titles               |
+----------------------+
8 rows in set (0.00 sec)
```

## 查看表结构

### SQL Server 下查看表结构

让我们通过定义看看 sp_tables 的参数有哪些：

```sql
stored procedure learning_sql_server.sys.sp_columns
     @table_name nvarchar(384), @table_owner nvarchar(384) = null,
     @table_qualifier sysname = null, @column_name nvarchar(384) = null,
     @ODBCVer int = 2
```

sp_tables 的参数有:

- `table_name` : 表名
- `table_owner` : 表的所有者;（一般查询的都为 dbo ,还有 sys 和 INFORMATION_SCHEMA）
- `table_qualifier` : 对象限定符； **对象限定符的数据库名称部分必须是当前数据库的名称** ，一般 null 。
- `column_name` : 指定列名（只能一列）

```sql
-- 查看表结构
sp_columns books
GO
-- 查看表的某列的结构
sp_columns books,dbo,NULL,"book_id"
GO
```

### MySQL　下查看表结构

`show create table table_name;`

```mysql
mysql> show create table departments;
+-------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Table       | Create Table                                                                                                                                                                                            |
+-------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| departments | CREATE TABLE `departments` (
`dept_no` char(4) NOT NULL,
`dept_name` varchar(40) NOT NULL,
PRIMARY KEY (`dept_no`),
UNIQUE KEY `dept_name` (`dept_name`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 |
+-------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
1 row in set (0.00 sec)
```

:::{note}
`show create database database_name;`
:::

______________________________________________________________________

[^id11]: 所有的系统级存储过程都可以在 SQL Server  的系统数据库的系统存储过程中找到。
