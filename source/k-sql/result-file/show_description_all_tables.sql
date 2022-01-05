delimiter $$
CREATE PROCEDURE `show_description_all_tables`()
BEGIN
    DECLARE t_name VARCHAR(255) DEFAULT '';
    DECLARE done boolean DEFAULT TRUE;
        -- 定义游标
    DECLARE name_cursor CURSOR FOR
        SELECT table_name FROM information_schema.TABLES 
        WHERE table_schema='employees' AND table_type='base table';
    -- 定义结束条件
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET done=FALSE;
    -- 遍历查询所有
    OPEN name_cursor;
    -- 获取下一个表名
    FETCH name_cursor INTO t_name;
    WHILE done DO
        -- 获取创建信息
        SET @sql=CONCAT('show create table ',t_name,';');
        -- 预处理
        PREPARE order_sql FROM @sql;
        -- 执行
        EXECUTE order_sql;
        -- 获取下一个表名
        FETCH name_cursor INTO t_name;
    END WHILE;
    -- 释放资源
    DEALLOCATE PREPARE order_sql;
    CLOSE name_cursor;
    DROP TABLE table_result;
END$$
delimiter ;