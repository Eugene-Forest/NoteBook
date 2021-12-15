=======================
视图
=======================

.. sidebar:: 测试库

    在笔者编写笔记的过程中，使用的测试库和测试表源于 MySQL 的 test_db 以及 书籍 SQL in 10 Minutes 的测试表，其测试库和表的下载前往测试库安装笔记:

    * :ref:`MySQL 测试库/表 安装笔记 <mssql_test_db_installer>` 
    * :ref:`SQL Server 测试库/表 安装笔记 <mysql_test_db_installer>` 

视图是一个虚拟表，其内容由查询定义。 同表一样，视图包含一系列带有名称的列和行数据。 视图在数据库中并不是以数据值存储集形式存在（但是除了 SQL Server 中的索引视图）。 行和列数据来自由定义视图的查询所引用的表，并且在引用视图时动态生成。

数据库视图是动态的，因为它与物理模式无关。数据库系统将数据库视图存储为具有连接的 SQL SELECT 语句。当表的数据发生变化时，视图也反映了这些数据的变化。同时，数据库视图可以启用计算列——数据库表不应该具有计算列，但数据库视图可以这样。

【所谓计算列是通过已有的两个或多个列的值集算出来的统计列，例如若一张子订单表中有顾客购买的产品数和产品单价，那么可以在视图中新建一个用于计算订单总价的total列，但是这对于需要存在数据库中的基础表来说显得臃肿多余；这是因为基础表的主要目的是更好的将数据存在数据库中，而视图的目的多为将数据库中的数据显示的更加友好】

**视图通常用来集中、简化和自定义每个用户对数据库的不同认识。** 

**视图可用作安全机制**，方法是允许用户通过视图访问数据，而不授予用户直接访问视图基础表的权限。

**--缺点--**

1. **性能**：从数据库视图查询数据可能会很慢，特别是如果视图是基于其他视图创建的。
2. **表依赖关系**：将根据数据库的基础表创建一个视图。每当更改与其相关联的表的结构时，都必须更改视图。



|75|

MySQL 中的视图 [#]_
==========================

MySQL 允许基于其他视图创建视图。在视图定义的 SELECT 语句中，可以引用另一个视图。

.. code-block:: mysql

    CREATE 
    [ALGORITHM = {MERGE  | TEMPTABLE | UNDEFINED}]
    VIEW [database_name].[view_name] 
    AS
    [SELECT  statement]

算法属性
----------------------

算法属性允许您控制 MySQL 在创建视图时使用的机制， MySQL 提供了三种算法： ``MERGE`` ， ``TEMPTABLE`` 和 ``UNDEFINED``。

* 使用 ``MERGE`` 算法，MySQL 首先将输入查询与定义视图的 SELECT 语句组合成单个查询。 然后MySQL执行组合查询返回结果集。 如果 SELECT 语句包含集合函数(如 ``MIN，MAX，SUM，COUNT，AVG`` 等)或 ``DISTINCT，GROUP BY，HAVING，LIMIT，UNION，UNION ALL`` ，子查询，则不允许使用 ``MERGE`` 算法。 如果SELECT语句无引用表，则也不允许使用 ``MERGE`` 算法。 如果不允许 ``MERGE`` 算法，MySQL将算法更改为 ``UNDEFINED`` 。请注意，将视图定义中的输入查询和查询组合成一个查询称为视图分辨率。

* 使用 ``TEMPTABLE`` 算法，MySQL 首先根据定义视图的 SELECT 语句 **创建一个临时表**，然后针对该临时表执行输入查询。因为 MySQL 必须创建临时表来存储结果集并将数据从基表移动到临时表，所以 ``TEMPTABLE`` 算法的效率比 ``MERGE`` 算法效率低。 另外，使用 ``TEMPTABLE`` 算法的视图是 **不可更新的**。

* 当您创建视图而不指定显式算法时， ``UNDEFINED`` 是默认算法。 ``UNDEFINED`` 算法使 MySQL 可以选择使用 ``MERGE`` 或 ``TEMPTABLE`` 算法。MySQL 优先使用 ``MERGE`` 算法,然后才进行 ``TEMPTABLE`` 算法，因为 ``MERGE`` 算法效率更高。

|30|

MySQL 中的可更新视图
-------------------------------

要创建可更新视图，定义视图的 SELECT 语句不能包含以下任何元素：

聚合函数，如：

* ``MIN，MAX，SUM，AVG，COUNT`` 等。
* ``DISTINCT`` 子句
* ``GROUP BY`` 子句
* ``HAVING`` 子句
* ``UNION`` 或 ``UNION ALL`` 子句
* 左连接或外连接。
* SELECT 子句中的子查询或引用该表的 WHERE 子句中的子查询出现在 FROM 子句中。
* 引用 FROM 子句中的不可更新视图
* 仅引用文字值
* 对基表的任何列的多次引用

.. code-block:: mysql

    create view order_infos
    as
    select Orders.order_num, order_date, quantity, item_price
    from
        Orders left join OrderItems OI
        on Orders.order_num = OI.order_num;

    update order_infos set quantity=10 where item_price=10.99;

    -- [2021-11-16 08:42:53] [HY000][1288] The target table order_infos of the UPDATE is not updatable





|50|


SQL Server 中的视图 [#]_
=============================

.. note:: 

    `点击前往 SQL 文档的视图部分文档查看更多类型的视图 <https://docs.microsoft.com/zh-cn/sql/relational-databases/views/views?view=sql-server-ver15#types-of-views>`_ 

|30|

SQL Server 中的可更新视图
---------------------------------

只要满足下列条件，即可通过视图修改基础基表的数据：

* 任何修改（包括 ``UPDATE``、 ``INSERT`` 和 ``DELETE`` 语句）都只能引用一个基表的列。

* 视图中被修改的列必须直接引用表列中的基础数据。 不能通过任何其他方式对这些列进行派生，如通过以下方式：

    * 聚合函数： ``AVG、COUNT、SUM、MIN、MAX、GROUPING、STDEV、STDEVP、VAR`` 和 ``VARP``。

    * 计算。 不能从使用其他列的表达式中计算该列。 使用集合运算符 ``UNION、UNION ALL、CROSSJOIN、EXCEPT`` 和 ``INTERSECT`` 形成的列将计入计算结果，且不可更新。

* 被修改的列不受 ``GROUP BY、HAVING 或 DISTINCT`` 子句的影响。

* TOP 在视图的 ``select_statement`` 中的任何位置都不会与 ``WITH CHECK OPTION`` 子句一起使用。


.. code-block:: mysql
    :linenos:

    -- 在 SQL Server 中，视图中使用了左/右连接也同样是可更新视图
    create view order_infos
    as
    select Orders.order_num, order_date, quantity, item_price
    from
        Orders left join OrderItems OI
        on Orders.order_num = OI.order_num

    select * from order_infos where item_price=10.99

    -- 更新语句成功执行，且基本表中的数据也被更新
    update order_infos set quantity=10 where item_price=10.99





----

.. [#] 原文出自【易百教程】，MySQL视图——原文链接 https://www.yiibai.com/mysql/views.html
.. [#] 原文出自【microsoft SQL 文档】，视图——原文链接 https://docs.microsoft.com/zh-cn/sql/relational-databases/views/views?view=sql-server-ver15






