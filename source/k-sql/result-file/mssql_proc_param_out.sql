create procedure c_page_employees
    @total int output,
    @current int = 1,
    @size int = 10
as
begin
    declare @offset_size int
    set @offset_size=(@current-1)*@size
    print @offset_size
    -- 实际业务使用时要显示指定查询的列名
    select top(@size) * from employees
    where emp_no > (
        select top 1 (emp_no+@offset_size) from employees order by emp_no
        )
    order by emp_no
    select @total = count(*)  from employees
    -- return 返回的值一般作为存储过程运行状态的参考，
    -- 不同于 select 查询直接返回给客户端的结果（集）
    -- return(0)
end
go

-- 执行存储过程
declare @total int =-1
declare @result int =-1
-- 需要注意的是 执行过程时，调用程序也必须使用 OUTPUT 关键字
exec @result=c_page_employees @total output
print 'total is '+cast(@total as varchar)
print 'result is '+cast(@result as varchar)

/* 控制台输出
[2021-11-12 11:32:29] [S0001] 0
[2021-11-12 11:32:29] [S0001] total is 300024
[2021-11-12 11:32:29] [S0001] result is 0
*/