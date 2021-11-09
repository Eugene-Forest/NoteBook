===================================
游标 （Cursor）
===================================


.. literalinclude:: ../result-file/show_description_all_tables.sql
    :language: sql

.. tip:: 

    在MySQL的存储过程中判断是否使用游标时考虑的情形:
    
    1. 是否需要遍历某个结果集（并同时执行一些操作）

        * 如果是则进行下一步，否则不需要使用游标

    2. 判断被遍历的结果是否是一次性的（即该结果集预计在整个存储过程中都不会变化）

        * 如果是则不需要建立临时表以用来存储结果集，直接将该结果集使用于游标定义中。如： ``DECLARE name_cursor CURSOR FOR SELECT table_name FROM information_schema.TABLES``
        * 否则，需要定义一个临时表用以存储数据。

    3. 需要注意定义游标相关变量的顺序

        * 首先，需要定义游标的结束判断的变量，如 ： ``DECLARE done boolean DEFAULT TRUE;``
        * 其次，需要定义游标，如： ``DECLARE name_cursor CURSOR FOR SELECT table_name FROM information_schema.TABLES``
        * 最后，需要定义游标的结束时触发的行为，如 ： ``DECLARE CONTINUE HANDLER FOR NOT FOUND SET done=FALSE;``

    4. 遍历循环体：

        .. code-block:: mysql

            -- ...
            DECLARE v_name ...;
            DECLARE v_name2 ...;
            DECLARE done boolean DEFAULT TRUE;
            -- ...
            DECLARE cursor_name CURSOR FOR ...;
            DECLARE CONTINUE HANDLER FOR NOT FOUND SET done=FALSE;
            -- ...

            -- 遍历查询所有
            OPEN cursor_name;
            FETCH cursor_name INTO v_name,v_name2,...;
            WHILE done DO
                -- ...deal something...
                FETCH cursor_name INTO v_name,v_name2,...;
            END WHILE;
            CLOSE cursor_name;
            -- ...
