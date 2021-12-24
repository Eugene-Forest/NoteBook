# 游标 （Cursor）

只进游标是 ODBC 中的默认游标类型。

不同的游标具有不同的特征。 最常见的游标类型（称为只进游标）只能通过结果集向前移动。 若要返回到上一行，应用程序必须关闭并重新打开游标，然后从结果集的开头读取行，直到到达所需的行。 只进游标提供了一种快速机制，用于通过结果集进行单一传递。

% 仅向前游标对于基于屏幕的应用程序不太有用，在这种情况下，用户可以在数据中向后和向前滚动。更好的解决方案是使用可滚动的游标 ，它提供对结果集的随机访问。 此类应用程序还可通过使用所谓的块游标一次提取多行 数据来提高性能。

还有一种叫 **可滚动的游标** ，它提供对结果集的随机访问。 此类应用程序还可通过使用所谓的块游标一次提取多行数据来提高性能。

% //todo 添加 可滚动的游标 笔记记录

:::{note}
文章中只提及（只进）游标的基本使用。
:::

## MySQL 中的 游标

MySQL游标只能用于存储过程（和函数）。

```{literalinclude} ../result-file/show_description_all_tables.sql
:language: mysql
```

:::{tip}
在MySQL的存储过程中判断是否使用游标时考虑的情形:

1. 是否需要遍历某个结果集（并同时执行一些操作）

   > - 如果是则进行下一步，否则不需要使用游标

2. 判断被遍历的结果是否是一次性的（即该结果集预计在整个存储过程中都不会变化）

   > - 如果是则不需要建立临时表以用来存储结果集，直接将该结果集使用于游标定义中。如： `DECLARE name_cursor CURSOR FOR SELECT table_name FROM information_schema.TABLES`
   > - 否则，需要定义一个临时表用以存储数据。

3. 需要注意定义游标相关变量的顺序

   > - 首先，需要定义游标的结束判断的变量，如 ： `DECLARE done boolean DEFAULT TRUE;`
   > - 其次，需要定义游标，如： `DECLARE name_cursor CURSOR FOR SELECT table_name FROM information_schema.TABLES`
   > - 最后，需要定义游标的结束时触发的行为，如 ： `DECLARE CONTINUE HANDLER FOR NOT FOUND SET done=FALSE;`

4. 遍历循环体：

   > ```mysql
   > -- ...
   > DECLARE v_name ...;
   > DECLARE v_name2 ...;
   > DECLARE done boolean DEFAULT TRUE;
   > -- ...
   > DECLARE cursor_name CURSOR FOR ...;
   > DECLARE CONTINUE HANDLER FOR NOT FOUND SET done=FALSE;
   > -- ...
   >
   > -- 遍历查询所有
   > OPEN cursor_name;
   > FETCH cursor_name INTO v_name,v_name2,...;
   > WHILE done DO
   >     -- ...deal something...
   >     FETCH cursor_name INTO v_name,v_name2,...;
   > END WHILE;
   > CLOSE cursor_name;
   > -- ...
   > ```
:::



## SQL Server 中的 游标

SQL Server 中游标的基本使用相较于 MySQL 来说比较简单。

```{literalinclude} ../result-file/drop_all_tables.sql
:language: mysql
:linenos: true
```

:::{note}
[更多关于游标](https://docs.microsoft.com/zh-cn/sql/relational-databases/cursors?view=sql-server-ver15)
:::
