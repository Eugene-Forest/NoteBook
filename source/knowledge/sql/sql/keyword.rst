===============================
sql 中的常用关键字
===============================

DISTINCT / distinct
============================

关键词 DISTINCT 用于返回唯一不同的值。


.. code-block:: sql

   -- the sampling code
   SELECT DISTINCT vend_id,prod_price FROM products;
   SELECT vend_id,prod_price FROM products;

.. code-block:: sql

   --the output of the first line of sampling code
   vend_id	prod_price
   BRS01     	5.99
   BRS01     	8.99
   BRS01     	11.99
   DLL01     	3.49
   DLL01     	4.99
   FNG01     	9.49
   --the output of the second line of sampling code
   vend_id	prod_price
   DLL01     	3.49
   DLL01     	3.49
   DLL01     	3.49
   BRS01     	5.99
   BRS01     	8.99
   BRS01     	11.99
   DLL01     	4.99
   FNG01     	9.49
   FNG01     	9.49


.. attention:: 

   不能部分使用 DISTINCT, DISTINCT 关键字作用于所有的列而不仅仅是紧跟在其后的一列。【比较上文的结果可知】

----

limit 和 top 以及其他限制结果的关键字
=======================================

需要清楚的是，限制结果的关键字在不同的数据库中有所不同，比如在 SQL Server 中为 ``select top 5 * from table_name;`` , 在 MySQL、MariaDB、PostgreSQL、SQLite 中为 ``select * from table_name limit 5;`` ，在 DB2 中为 ``SELECT * FROM table_name FETCH FIRST 5 ROWS ONLY;`` ,在 Oracle 为 ``select * from table_name where ROWNUM <= 5;``






