delimiter $$
CREATE PROCEDURE show_db_table_clo(
	-- 表名
	IN t_name VARCHAR(255),
	-- 查询页码
	IN current INT,
	-- 页大小
	IN size INT,
	-- 总条数
	OUT record_total INT
)
BEGIN
	DECLARE offset_size INT DEFAULT 0;
	SET offset_size=(current-1)*size;
	SELECT SQL_CALC_FOUND_ROWS * FROM information_schema.COLUMNS WHERE table_schema=t_name LIMIT offset_size,size;
	SET record_total=FOUND_ROWS();
END$$
delimiter ;

-- 查询
SET @table_name='employees';
SET @current=1;
SET @size=5;
CALL show_db_table_clo(@table_name,@current,@size,@total);

SELECT @total;