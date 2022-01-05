-- 函数的简单应用
delimiter $$
create function get_dept_name(dept_no char(4))
    returns varchar(40)
    deterministic
begin
    declare d_name varchar(40);
    select dept_name into d_name
    from departments as A
    where A.dept_no=dept_no;
    return d_name;
end $$
delimiter ;

-- 查询中使用函数
select emp_no, get_dept_name(dept_no) as dept_name, from_date, to_date 
from dept_emp
order by emp_no limit 2;

-- 创建格式化字段的函数
delimiter $$
create function format_date(origin_date date)
    returns varchar(60)
    deterministic
begin
    return date_format(origin_date ,'%Y 年 %m 月 %d 日');
end $$
delimiter ;

-- 使用自定义函数的查询
select emp_no, get_dept_name(dept_no) as dept_name,
    format_date(from_date) as from_date,
    format_date(to_date) as to_date
from dept_emp
order by emp_no limit 2;

-- 直接使用系统的格式化函数的查询
select emp_no, get_dept_name(dept_no) as dept_name,
    date_format(from_date ,'%Y 年 %m 月 %d 日') as from_date,
    date_format(to_date ,'%Y 年 %m 月 %d 日') as to_date
from dept_emp
order by emp_no limit 2;