=======================
分页问题 
=======================

.. warning:: 

    一般来说，对于简单分页查询可以直接使用 mybatis-plus 分页插件或者是在 mybatis 中编写 xml 文件查询返回多结果。详情前往 :ref:` 业务实现之分页查询 <business_paging>` 。

    在此篇章中讲述的分页都是基于存储过程中实现的，也就是 *记录总数的获取是通过 OUT 参数来接收 total 的*。



.. note:: 

    在分页时，我们常常需要保证运行速度，所以需要减少查询次数同时优化查询索引。

    我们在使用分页时，常常会碰到以下问题：

        1. 记录总数的获取
        2. 记录总数的计算
        3. 分页偏移量较大时，如何优化偏移
    
在实际业务中，最常使用的查询之一就是分页查询。

分页查询一般来说有两个重要数据，一个是数据列表，一个是数据总条数。

在 MySQL 一般的分页查询的实现方式是通过 ``limit`` 和 ``count(*)`` （或者 ``SQL_CALC_FOUND_ROWS``） 来实现的，这种方法缺点在于耗时的总条数查询无法避免。

    

MySQL 中的分页
=====================

* 记录总数的获取：通过 OUT 参数接收 total
* 记录总数的计算：使用 ``SQL_CALC_FOUND_ROWS`` 来计算记录总条数
* 优化偏移：子查询（适用于有一定顺序的数据，如主键是递增的，那么可以根据主键来唯一的确认一个位置，而这个位置就是分页偏移之后的数据的开始位置）

.. attention:: 

    需要注意的是，使用 *count(*)* 来计算数据条数 比 *count(col_name)* 来的要好，是因为 *count(*)* 与 *count(col_name)* 相比可以避免 *col_name* 为 *NULL* 时而漏掉此条数据；同时，如果当查询 *count(*)* 时没有 *where* 语句和其他子查询的限制的情况下，那么其可以直接通过引擎获取表的总数据条数（如： ``select count(*) from table_name;``）而不需要计算。
    
    优化偏移的实现 [#]_ ：即在满足一定条件的情况下， ``select col_name(s) from table_name where id > 1115 limit 10`` 的执行速度要快于 ``select col_name(s) from table_name limit 1115,10`` ，当然其他关联操作也可以实现相同目的；优化偏移的实现其实就是使用索引来替换可以不用进行全扫描进行定位。

分页实例 
-----------------------


定义代码

.. literalinclude:: ../result-file/show_db_table_clo.sql
    :language: MySQL
    :lines: 1-19

.. raw:: html

    <hr width='50%'>

查询代码

.. literalinclude:: ../result-file/show_db_table_clo.sql
    :language: MySQL
    :lines: 19-

.. raw:: html

    <hr width='50%'>

.. csv-table:: 查询结果
   :file: ../result-file/show_db_table_clo.csv
   :header-rows: 1

.. important:: 

    在此存储过程中使用 ``SQL_CALC_FOUND_ROWS`` 来计算记录总条数。

    理想情况下，如果在存储过程中需要对数据进行分页，那么先考虑是否可以用 ``SQL_CALC_FOUND_ROWS`` 来计算满足条件的数据总数，以及是否可用子查询来快速偏移来节省偏移时间。只有在别无选择的情况下才使用 ``count(*)`` 来计算数据总数，以及使用 ``limit offset,size`` 进行数据分页(当预计该业务未来产生的符合要求的数据很少时，可以直接使用 limit 偏移)


.. attention:: 

    关于 ``SQL_CALC_FOUND_ROWS`` 提示（hint）， 在使用此提示时，我们要明白此提示可能会产生较大的代价（需要扫描所有满足条件的行）。


备选分页方案
=====================

分页查询还有另一种实现方式，不同于一般的分页查询，它不用知道数据总条数，只需要知道是否有下一页数据即可，这种分页方式可以减少查询时间，而且适用性更强。只不过这种实现方式需要业务需求方能接受，因为它没有办法直观地知道数据有多少，在此作为一个备用方案。

**实现思路：如果每页大小为10条数据，那么我们在实际分页时返回11条，然后再（后端）业务逻辑中判断是否存在第11条数据，若存在则有下一页，否则没有下一页。同时用偏移量来判断是否存在上一页。**

如果将分页逻辑封装再实体对象中，那么该实体将类似与下文所示：

.. code-block:: java

    @Data
    public class IPage<T> {

        /**
        * 数据集
        */
        List<T> records;

        Boolean hasNext;

        Boolean hasLast;

        /**
        * 页大小
        */
        Integer size;

        /**
        * 偏移量
        */
        Integer offset;

    }


----


.. [#] 参考 高性能的 MySQL 一书的 第六章查询性能优化