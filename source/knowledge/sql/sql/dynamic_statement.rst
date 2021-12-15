===============================
动态或拼接语句
===============================


.. literalinclude:: ../result-file/show_description_all_tables.sql
    :language: sql

.. attention:: 

    在 MySQL 中一般的SQL语句需要先编译然后立即执行，所以在存储过程中如果需要使用拼接SQL语句时需要先预处理在执行并且最终要释放资源。