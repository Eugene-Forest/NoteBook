-- 标值函数
create function get_grade_of_price(@price int = -1)
returns int with schemabinding
begin
    declare @grade int =0;
    if @grade >0
        if @price >0  and @price <10
            set @grade = 1;
        else
            set @grade = 2;
    else
        set @grade=-1;
    return @grade;
end

begin
	declare @price int = 0
	declare @result int
	exec
		@result = get_grade_of_price @price
	select @result as result
end
go

/* 运行结果:
 result = -1
 */

-- 表值函数创建方法一

-- 获取子单据中单价最小为10的订单
create function get_with_least_item_price(@price int=0)
returns table -- with schemabinding
as
return (
    select order_num, order_item, prod_id, quantity, item_price from OrderItems
    where item_price >= @price) ;
go

begin
	declare @price int = 10
	select * from get_with_least_item_price(@price)
end
go

-- 表值函数创建方法二
-- 获取子单据中单价最大为10的订单
create function get_with_maximum_item_price(@price int=0)
returns @resutl_table table (
    order_num  int           not null,
    order_item int           not null,
    prod_id    char(10)      not null,
    quantity   int           not null,
    item_price decimal(8, 2) not null
    ) -- with schemabinding
begin
    insert @resutl_table
    select order_num, order_item, prod_id, quantity, item_price from OrderItems
    where item_price <= @price;
    return ;
end
go

begin
	declare @price int = 10
	select * from get_with_maximum_item_price(@price)
end
go