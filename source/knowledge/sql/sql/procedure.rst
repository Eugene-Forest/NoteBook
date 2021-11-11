===============================
存储过程、函数
===============================

存储过程和存储函数类似于面向对象程序设计语言中的方法，可以简化代码，提高代码的重用性。


SQL Server 存储过程与存储函数
================================

SQL Server中的存储过程是使用T-SQL编写的代码段。它的目的在于能够方便的从系统表中查询信息，或者完成与更新数据库表相关的管理任务和其他的系统管理任务.T-SQL语句是SQL Server数据库与应用程序之间的编程接口。在很多情况下，一些代码会被开发者重复编写多次，如果每次都编写相同功能的代码，不但繁琐，而且容易出错，而且由于SQL Server逐条的执行语句会降低系统的运行效率。

简而言之，存储过程就是SQL Server为了实现特定任务，而将一些需要多次调用的固定操作语句编写成程序段，这些程序段存储在服务器上，有数据库服务器通过程序来调用。

.. //todo 添加详细的官方说明，比较


SQL Server 存储过程
============================

.. code-block:: sql

   Create procedure <procedure_Name> 
   As 
   Begin 
   <SQL Statement> 
   End 
   Go

样例
--------------------------

.. literalinclude:: ../result-file/drop_all_tables.sql
    :language: sql
    

.. attention:: 

    SQL Server 有许多定义好的变量，如 @@FETCH_STATUS 是在游标遍历时判断是否获取下一个数据的状态变量。



MySQL 存储过程与存储函数
===============================

MySQL中提供存储过程与存储函数机制，我们姑且将存储过程和存储函数合称为存储程序。与一般的SQL语句需要先编译然后立即执行不同，存储程序是一组为了完成特定功能的SQL语句集，经编译后存储在数据库中，当用户通过指定存储程序的名字并给定参数（如果该存储程序带有参数）来调用才会执行。

存储程序就是一条或者多条SQL语句和控制语句的集合，我们可以将其看作MySQL的批处理文件，当然，其作用不仅限于批处理。当想要在不同的应用程序或平台上执行相同的功能一段程序或者封装特定功能时，存储程序是非常有用的。数据库中的存储程序可以看做是面向对编程中面向对象方法，它允许控制数据的访问方式。

两者比较 [#]_
---------------


存储函数与存储过程有如下区别：

　　1) 存储函数的限制比较多,例如不能用临时表,只能用表变量,而存储过程的限制较少，存储过程的实现功能要复杂些,而函数的实现功能针对性比较强。

　　2) 返回值不同。存储函数必须有返回值,且仅返回一个结果值；存储过程可以没有返回值,但是能返回结果集(out,inout)。

　　3) 调用时的不同。存储函数嵌入在SQL中使用,可以在select 存储函数名(变量值)；存储过程通过call语句调用 call 存储过程名。

　　4) 参数的不同。存储函数的参数类型类似于IN参数，没有类似于OUT和INOUT的参数。存储过程的参数类型有三种，IN、OUT和INOUT：

　　　　a. in：数据只是从外部传入内部使用(值传递),可以是数值也可以是变量

　　　　b. out：只允许过程内部使用(不用外部数据),给外部使用的(引用传递:外部的数据会被先清空才会进入到内部),只能是变量

　　　　c. inout：外部可以在内部使用,内部修改的也可以给外部使用,典型的引用 传递,只能传递变量。

总的来说，存储过程和函数的区别在于函数必须有返回值，而存储过程没有，存储过程的参数可以使用 **IN、OUT、INOUT** 类型，而函数的参数只能是 **“IN”** 类型的。如果有函数从其他类型的数据库迁移到 MySQL，那么就可能因此需要将函数改造成存储过程。

.. important:: 

    在对存储过程或函数进行操作时，需要首先确认用户是否具有相应的权限。例如，创建存储过程或者函数需要 ``CREATE ROUTINE`` 权限，修改或者删除存储过程或者函数需要 ``ALTER ROUTINE`` 权限，执行存储过程或者函数需要 ``EXECUTE`` 权限。

    *在实际项目使用时，一定要确定项目配置中的MySQL用户拥有执行存储过程的权限。*



MySQL 存储过程
================================

.. note:: 
    由于语法原因，一般我们通过查询或命令行来创建 MySQL 存储过程需要将 SQL 结束符号变为非 ``;`` 字符。（即 ``delimiter $$``）


样例
--------------

.. literalinclude:: ../result-file/show_description_all_tables.sql
    :language: mysql

.. attention:: 

    在 MySQL 中一般的SQL语句需要先编译然后立即执行，所以在存储过程中如果需要使用拼接SQL语句时需要先预处理在执行并且最终要释放资源。



MySQL 存储函数
===========================

存储的函数是返回单个值的特殊类型的存储程序。您使用存储的函数来封装在SQL语句或存储的程序中可重用的常用公式或业务规则。

与存储过程不同，您可以在SQL语句中使用存储的函数，也可以在表达式中使用。 这有助于提高程序代码的可读性和可维护性。

.. code-block:: mysql

    CREATE FUNCTION function_name(param1,param2,…)
        RETURNS datatype
        [NOT] DETERMINISTIC
    statements


1) 首先，在 ``CREATE FUNCTION`` 子句之后指定存储函数的名称。
2) 其次，列出括号内存储函数的所有参数。 默认情况下，所有参数均为 ``IN`` 参数。不能为参数指定 ``IN`` ， ``OUT`` 或 ``INOUT`` 修饰符。
3) 第三，必须在 ``RETURNS`` 语句中指定返回值的数据类型。它可以是任何有效的 **MySQL 数据类型**。
4) 第四，对于相同的输入参数，如果存储的函数返回相同的结果，这样则被认为是确定性的，否则存储的函数不是确定性的。必须决定一个存储函数是否是确定性的。 如果您声明不正确，则存储的函数可能会产生意想不到的结果，或者不使用可用的优化，从而降低性能。
5) 第五，将代码写入存储函数的主体中。 它可以是单个语句或复合语句。 在主体部分中，必须至少指定一个 ``RETURN`` 语句。 ``RETURN`` 语句用于返回一个值给调用者。 每当到达 ``RETURN`` 语句时，存储的函数的执行将立即终止。


.. code-block:: mysql

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

.. csv-table:: 查询的运行结果
    :header-rows: 1
    :stub-columns: 1
    :file: ../result-file/get_dept_name.csv

.. note:: 

    通过该方法可以实现与表连接的相同的效果。（以上示例代码的运行结果同样可以 employees 表和 departments 表连接生成）

    .. code-block:: mysql

        select emp_no,dept_name,from_date,to_date
        from dept_emp as A
        left join departments as B
        on A.dept_no = B.dept_no
        order by emp_no limit 2;

    **一般来说，使用在查询中使用函数可以降低 SQl 语句的复杂度（例如可以将较为复杂的多表连接通过存储函数来简化），但是需要注意的是这种优势往往需要牺牲运行效率/速度来实现。**

.. important:: 

    存储函数较为重要的应用领域是简化 select 查询。

    例如 

    .. code-block:: mysql

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

    .. csv-table:: 查询的运行结果
        :header-rows: 1
        :stub-columns: 1
        :file: ../result-file/format_function.csv



----


.. [#] 引用自 MySQL数据库之存储过程与存储函数 https://www.cnblogs.com/chenhuabin/p/10142190.html
.. [#] 易百教程——MySQL存储函数,原文链接：https://www.yiibai.com/mysql/stored-function.html