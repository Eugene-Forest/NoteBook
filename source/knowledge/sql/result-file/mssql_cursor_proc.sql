-- 使用 cursor 数据类型指定输出参数 @my_cursor 的过程。 然后在批处理中调用该过程。

-- 获取计算订单总价格
create procedure get_orderitem_cursor
    @my_cursor cursor varying output
as
begin
    set @my_cursor = cursor
    forward_only static for
        select a.order_num,sum(a.item_total_price) as total_price  from (
            select order_num,(quantity*item_price) as item_total_price
            from OrderItems
            ) as A group by a.order_num;
    open @my_cursor;
end
go

CREATE procedure get_order_price
as
begin
    declare @exec_cursor cursor;
    declare @order_no int;
    declare @order_total_price decimal(8,2);
    execute get_orderitem_cursor @my_cursor = @exec_cursor OUTPUT;
    while (@@fetch_status=0)
    begin
        fetch next from @exec_cursor into @order_no,@order_total_price;
        print N'订单<' +cast(isnull(@order_no,0) as varchar)+ N'>的总价为 ' +cast(isnull(@order_total_price,0) as varchar);
    end
    close @exec_cursor;
    deallocate @exec_cursor;
end
go


begin
	declare @result int
	exec
		@result = get_order_price
	select @result as result
end
go


/* 控制台打印

[2021-11-15 08:48:38] [S0001] 订单<20005>的总价为 1648.00
[2021-11-15 08:48:38] [S0001] 订单<20006>的总价为 329.60
[2021-11-15 08:48:38] [S0001] 订单<20007>的总价为 1696.00
[2021-11-15 08:48:38] [S0001] 订单<20008>的总价为 189.60
[2021-11-15 08:48:38] [S0001] 订单<20009>的总价为 1867.50
[2021-11-15 08:48:38] [S0001] 订单<20009>的总价为 1867.50
[2021-11-15 08:48:38] 在 219 ms (execution: 27 ms, fetching: 192 ms) 内检索到从 1 开始的 1 行

*/

-- 运行结果 ： @result = 0 , 存储过程成功执行。