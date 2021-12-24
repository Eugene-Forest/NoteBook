# 存储过程、函数

:::{sidebar} 测试库
在笔者编写笔记的过程中，使用的测试库和测试表源于 MySQL 的 test_db 以及 书籍 SQL in 10 Minutes 的测试表，其测试库和表的下载前往测试库安装笔记:

- {ref}`MySQL 测试库/表 安装笔记 <mssql_test_db_installer>`
- {ref}`SQL Server 测试库/表 安装笔记 <mysql_test_db_installer>`
:::

存储过程和存储函数类似于面向对象程序设计语言中的方法，可以简化代码，提高代码的重用性。

## MySQL 存储过程与存储函数

MySQL中提供存储过程与存储函数机制，我们姑且将存储过程和存储函数合称为存储程序。与一般的SQL语句需要先编译然后立即执行不同，存储程序是一组为了完成特定功能的SQL语句集，经编译后存储在数据库中，当用户通过指定存储程序的名字并给定参数（如果该存储程序带有参数）来调用才会执行。

存储程序就是一条或者多条SQL语句和控制语句的集合，我们可以将其看作MySQL的批处理文件，当然，其作用不仅限于批处理。当想要在不同的应用程序或平台上执行相同的功能一段程序或者封装特定功能时，存储程序是非常有用的。数据库中的存储程序可以看做是面向对编程中面向对象方法，它允许控制数据的访问方式。



### MySQL 存储过程

:::{note}

由于语法原因，一般我们通过查询或命令行来创建 MySQL 存储过程需要将 SQL 结束符号变为非 `;` 字符。（即 `delimiter $$`）
:::

```{literalinclude} ../result-file/show_description_all_tables.sql
:language: mysql
```

:::{attention}
在 MySQL 中一般的SQL语句需要先编译然后立即执行，所以在存储过程中如果需要使用拼接SQL语句时需要先预处理在执行并且最终要释放资源。
:::



### MySQL 存储函数 [^id17]

存储的函数是返回单个值的特殊类型的存储程序。您使用存储的函数来封装在SQL语句或存储的程序中可重用的常用公式或业务规则。

与存储过程不同，您可以在SQL语句中使用存储的函数，也可以在表达式中使用。 这有助于提高程序代码的可读性和可维护性。

```mysql
CREATE FUNCTION function_name(param1,param2,…)
    RETURNS datatype
    [NOT] DETERMINISTIC
statements
```

1. 首先，在 `CREATE FUNCTION` 子句之后指定存储函数的名称。
2. 其次，列出括号内存储函数的所有参数。 默认情况下，所有参数均为 `IN` 参数。不能为参数指定 `IN` ， `OUT` 或 `INOUT` 修饰符。
3. 第三，必须在 `RETURNS` 语句中指定返回值的数据类型。它可以是任何有效的 **MySQL 数据类型**。
4. 第四，对于相同的输入参数，如果存储的函数返回相同的结果，这样则被认为是确定性的，否则存储的函数不是确定性的。必须决定一个存储函数是否是确定性的。 如果您声明不正确，则存储的函数可能会产生意想不到的结果，或者不使用可用的优化，从而降低性能。
5. 第五，将代码写入存储函数的主体中。 它可以是单个语句或复合语句。 在主体部分中，必须至少指定一个 `RETURN` 语句。 `RETURN` 语句用于返回一个值给调用者。 每当到达 `RETURN` 语句时，存储的函数的执行将立即终止。

```{literalinclude} ../result-file/mysql_function_ex.sql
:language: mysql
:lines: 1-19
```

```{eval-rst}
.. csv-table:: 查询的运行结果
    :header-rows: 1
    :stub-columns: 1
    :file: ../result-file/get_dept_name.csv
```

:::{note}

通过该方法可以实现与表连接的相同的效果。（以上示例代码的运行结果同样可以 employees 表和 departments 表连接生成）

```mysql
select emp_no,dept_name,from_date,to_date
from dept_emp as A
left join departments as B
on A.dept_no = B.dept_no
order by emp_no limit 2;
```

**一般来说，使用在查询中使用函数可以降低 SQl 语句的复杂度（例如可以将较为复杂的多表连接通过存储函数来简化），但是需要注意的是这种优势往往需要牺牲运行效率/速度来实现。**
:::

:::{important}
存储函数较为重要的应用领域是简化 select 查询，使得代码更易读懂。

例如

```{literalinclude} ../result-file/mysql_function_ex.sql
:language: mysql
:lines: 20-
```

```{eval-rst}
.. csv-table:: 查询的运行结果
    :header-rows: 1
    :stub-columns: 1
    :file: ../result-file/format_function.csv
```
:::



### 两者比较 [^id18]

存储函数与存储过程有如下区别：

1. **存储函数的限制比较多**,例如不能用临时表,只能用表变量, **而存储过程的限制较少**，存储过程的实现功能要复杂些,而函数的实现功能针对性比较强。
2. **返回值不同。** 存储函数必须有返回值,且仅返回一个结果值；存储过程可以没有返回值,但是能返回结果集(out,inout)。
3. **调用时的不同。** 存储函数嵌入在SQL中使用,可以在 select 存储函数名(变量值)；存储过程通过call语句调用 call 存储过程名。
4. **参数的不同。** 存储函数的参数类型类似于IN参数，没有类似于OUT和INOUT的参数。存储过程的参数类型有三种，IN、OUT和INOUT：

> 1. in：数据只是从外部传入内部使用(值传递),可以是数值也可以是变量
> 2. out：只允许过程内部使用(不用外部数据),给外部使用的(引用传递:外部的数据会被先清空才会进入到内部),只能是变量。
> 3. inout：外部可以在内部使用,内部修改的也可以给外部使用,典型的引用 传递,只能传递变量。

总的来说，存储过程和函数的区别在于函数必须有返回值，而存储过程没有，存储过程的参数可以使用 **IN、OUT、INOUT** 类型，而函数的参数只能是 **“IN”** 类型的。如果有函数从其他类型的数据库迁移到 MySQL，那么就可能因此需要将函数改造成存储过程。

:::{important}
在对存储过程或函数进行操作时，需要首先确认用户是否具有相应的权限。例如，创建存储过程或者函数需要 `CREATE ROUTINE` 权限，修改或者删除存储过程或者函数需要 `ALTER ROUTINE` 权限，执行存储过程或者函数需要 `EXECUTE` 权限。

*在实际项目使用时，一定要确定项目配置中的MySQL用户拥有执行存储过程的权限。*
:::

## SQL Server 存储过程与存储函数



### SQL Server 存储过程 [^id19]

SQL Server 中的存储过程是由一个或多个 Transact-SQL 语句或对 Microsoft .NET Framework 公共语言运行时 (CLR) 方法的引用所构成的一个组。 过程与其他编程语言中的构造相似，这是因为它们都可以：

- 接受输入参数并以输出参数的格式向调用程序返回多个值。
- 包含用于在数据库中执行操作的编程语句。 这包括调用其他过程。
- 向调用程序返回状态值，以指明成功或失败（以及失败的原因）。

简而言之，存储过程就是SQL Server为了实现特定任务，而将一些需要多次调用的固定操作语句编写成程序段，这些程序段存储在服务器上，有数据库服务器通过程序来调用。

```{literalinclude} ../result-file/drop_all_tables.sql
:language: sql
```

:::{attention}
SQL Server 有许多定义好的全局变量，如 @@FETCH_STATUS 是在游标遍历时判断是否获取下一个数据的状态变量。
:::

#### 存储过程的类型

- **用户定义** : 用户定义的过程可在用户定义的数据库中创建，或者在除了 Resource 数据库之外的所有系统数据库中创建。 该过程可在 Transact-SQL 中开发，或者作为对 Microsoft .NET Framework 公共语言运行时 (CLR) 方法的引用开发。
- **临时** : 临时过程是用户定义过程的一种形式。 临时过程与永久过程相似，只是临时过程存储于 tempdb 中。 临时过程有两种类型：本地过程和全局过程。 它们在名称、可见性以及可用性上有区别。 本地临时过程的名称以单个数字符号 (#) 开头；它们仅对当前的用户连接是可见的；当用户关闭连接时被删除。 全局临时过程的名称以两个数字符号 (##) 开头，创建后对任何用户都是可见的，并且在使用该过程的最后一个会话结束时被删除。
- **系统** : 系统过程是 SQL Server随附的。 它们物理上存储在内部隐藏的 Resource 数据库中，但逻辑上出现在每个系统定义数据库和用户定义数据库的 sys 架构中。 此外， msdb 数据库还在 dbo 架构中包含用于计划警报和作业的系统存储过程。 因为系统过程以前缀 `sp_` 开头，所以，我们建议你在命名用户定义过程时不要使用此前缀。 同时，SQL Server 支持在 SQL Server 和外部程序之间提供一个接口以实现各种维护活动的系统过程。 这些扩展过程使用 `xp_` 前缀。
- **扩展的用户定义** : 扩展过程允许你使用编程语言（例如 C）创建外部例程。这些过程是指 SQL Server 的实例可以动态加载和运行的 DLL。 *SQL Server的未来版本中将删除扩展存储过程*。

:::{note}

Transact-SQL 用户定义函数中可以使用部分 具有不确定性的（系统）内置函数 ，[点击前往官网查看哪些（系统）内置函数可以在用户定义函数使用](https://docs.microsoft.com/zh-cn/sql/relational-databases/user-defined-functions/user-defined-functions?view=sql-server-ver15#valid-statements-in-a-function) 。
:::

#### 参数

通过指定过程参数，调用程序可以将值传递给过程的主体。 在执行过程期间，这些值可以用于各种目的。 如果将参数标记为 OUTPUT 参数，则过程参数还可以将值返回给调用程序。

一个过程最多可以有 2100 个参数，每个参数都有名称、数据类型和方向。 还可以为参数指定默认值（可选）。

##### 参数的默认值

如果在声明参数时指定了默认值，则参数被视为可选的。 在过程调用中不需要为可选参数提供值。

在以下情况下使用参数的默认值：

- 在过程调用中未指定参数值。
- 在过程调用中将 DEFAULT 关键字指定为值。

如果没有合适的值可以指定为参数的默认值，则指定 NULL 为默认值。 如果在未提供参数值的情况下执行过程，最好让过程返回自定义的消息。

```mysql
CREATE PROCEDURE Sales.uspGetSalesYTD
@SalesPerson nvarchar(50) = NULL  -- NULL default value
AS
BEGIN
    -- Validate the @SalesPerson parameter.
    IF @SalesPerson IS NULL
    BEGIN
        PRINT 'ERROR: You must specify the last name of the sales person.'
        RETURN(500)
    END
    RETURN(0)
END
GO
```

##### 指定参数方向

参数的方向可以为输入（表明将值传递给过程的主体），也可以为输出（表明过程将值返回给调用程序）。 默认为输入参数。

若要指定输出参数，必须在 CREATE PROCEDURE 语句的参数定义中指定 OUTPUT 关键字。 当过程退出时，它向调用程序返回输出参数的当前值。 **执行过程时，调用程序也必须使用 OUTPUT 关键字**，才能将该参数值保存到可以在调用程序中使用的变量中。

```{literalinclude} ../result-file/mssql_proc_param_out.sql
:language: mysql
```

:::{note}

过程可以返回一个整数值（称为“返回代码”），以指示过程的执行状态。 使用 RETURN 语句指定过程的返回代码。 默认情况下，成功执行存储过程会返回整数0。而其他情况返回的数据可以通过逻辑判断语句和 return 语句来自定义。
:::

#### 在 OUTPUT 参数中使用 cursor 数据类型

在 SQL Server 中有将游标作为输出参数的存储过程。同时，Transact-SQL 过程只能将 cursor 数据类型用于 OUTPUT 参数。 如果为某个参数指定了 cursor 数据类型，在过程定义中必须为该参数指定 VARYING 和 OUTPUT 关键字。 可以将参数指定为仅限 OUTPUT，但是如果在参数声明中指定了 VARYING 关键字，则数据类型必须为 cursor 并且也必须指定 OUTPUT 关键字。

在执行过程时，以下规则适用于 cursor 输出参数：

- 对于只进游标，游标的结果集中返回的行只是那些过程执行结束时处于或超出游标位置的行，例如：

  - 在过程中的名为 RS 的 100 行结果集上打开一个非滚动游标。
  - 过程提取结果集 RS 的头 5 行。
  - 过程返回到其调用者。
  - 返回到调用者的结果集 RS 由 RS 的第 6 到 100 行组成，调用者中的游标处于 RS 的第一行之前。

- 对于只进游标，如果过程退出时游标位于第一行的前面，则整个结果集将返回给调用批处理、过程或触发器。 返回时，游标将位于第一行的前面。

- 对于只进游标，如果过程退出时游标的位置超出最后一行的结尾，则为调用批处理、过程或触发器返回空结果集。【空结果集与空值不同】

- 对于可滚动游标，在过程退出时，结果集中的所有行均会返回给调用批处理、过程或触发器。 返回时，游标保留在过程中最后一次执行提取时的位置。

- 对于任意类型的游标，如果游标关闭，则将 Null 值传递回调用批处理、过程或触发器。 如果将游标指派给一个参数，但该游标从未打开过，也会出现这种情况。

:::{note}

关闭状态只有在返回时才有影响。 例如，可以在过程中关闭游标，稍后再打开游标，然后将该游标的结果集返回给调用批处理、过程或触发器。
:::

```{literalinclude} ../result-file/mssql_cursor_proc.sql
:language: mysql
```

:::{important}
*cursor 数据类型不能通过数据库 API（例如 OLE DB、ODBC、ADO 和 DB-Library）绑定到应用程序变量上。* (即在 OUTPUT 参数中使用 cursor 数据类型存储过程不能作为对数据库外的接口程序，如 Spring Boot 项目中的不能成功调用 OUTPUT 参数中使用 cursor 作为数据类型的存储过程 ) 因为必须先绑定 OUTPUT 参数，应用程序才可以执行过程，所以 **带有 cursor OUTPUT 参数的过程不能通过数据库 API 调用。** 只有将 `Transact-SQL` cursor OUTPUT 变量分配给 局部 `Transact-SQL` cursor 变量时，才可以通过 **批处理、过程或触发器** 调用这些过程。

cursor OUTPUT 参数的过程对游标的操作会影响到返回后的 cursor 参数，因为在这个过程中以及返回后的游标参数都是没有关闭的。

更多相关信息 [点击前往官网查看](https://docs.microsoft.com/zh-cn/sql/relational-databases/stored-procedures/return-data-from-a-stored-procedure?view=sql-server-ver15#returning-data-using-an-output-parameter)  。
:::



### SQL Server 用户定义函数 (UDF) [^id20]

与编程语言中的函数类似，SQL Server 用户定义函数是接受参数、执行操作（例如复杂计算）并将操作结果以值的形式返回的例程。 **返回值可以是单个标量值或结果集。**

#### 函数类型

- 标量函数 : 用户定义标量函数返回在 RETURNS 子句中定义的类型的单个数据值。 对于内联标量函数，返回的标量值是单个语句的结果。 对于多语句标量函数，函数体可以包含一系列返回单个值的 Transact-SQL 语句。 返回类型可以是除 text、 ntext、 image、 cursor 和 timestamp 外的任何数据类型。
- 表值函数 : 用户定义的表值函数返回 table 数据类型。 对于内联表值函数，没有函数主体；表是单个 SELECT 语句的结果集。
- 系统函数 : SQL Server 提供了许多系统函数，可用于执行各种操作。 这些函数不能修改。

#### 函数准则和有效语句

`BEGIN...END` 块中的语句不能有任何副作用。 函数副作用是指对具有函数外作用域（例如数据库表的修改）的资源状态的任何永久性更改。 函数中的语句唯一能做的更改是对函数上的局部对象（如局部游标或局部变量）的更改。 **不能在函数中执行的操作包括：对数据库表的修改，对不在函数上的局部游标进行操作，发送电子邮件，尝试修改目录，以及生成返回至用户的结果集。**

函数中的有效语句的类型包括：

- `DECLARE` 语句，该语句可用于定义函数局部的数据变量和游标。
- 为函数局部对象的赋值，如使用 `SET` 为标量和表局部变量赋值。
- 游标操作，该操作引用在函数中声明、打开、关闭和释放的局部游标。 不允许使用 `FETCH` 语句将数据返回到客户端。 仅允许使用 `FETCH` 语句通过 `INTO` 子句给局部变量赋值。
- `TRY...CATCH` 语句 **以外** 的控制流语句。
- `SELECT` 语句，该语句包含具有为函数的局部变量赋值的表达式的选择列表。
- `UPDATE`、 `INSERT` 和 `DELETE` 语句，这些语句修改函数的局部表变量。
- `EXECUTE` 语句，该语句调用扩展存储过程。（扩展存储过程在未来版本中将会抛弃）

:::{note}

其他局限和限制：

01. 用户定义函数 **不能用于执行修改数据库状态的操作**。

02. 用户定义函数不能包含将表作为其目标的 `OUTPUT INTO` 子句。

03. 用户定义函数 **不能返回多个结果集**。 如果您需要返回多个结果集，请使用存储过程。

04. 在用户定义函数中， **错误处理受限制**。 UDF 不支持 `TRY...CATCH`、 `@ERROR` 或 `RAISERROR`。

05. 用户定义函数 **不能调用存储过程**，但是可调用扩展存储过程(但是扩展存储过程的使用并不被官方所建议，同时它也将在未来版本中抛弃)。

06. 用户定义函数 **不能使用动态 SQL 或临时表**。 **但是允许表变量**。

07. 在用户定义函数中 **不允许 SET 语句**。（此 SET 语句并不是赋值临时变量的 SET 语句,  [更多详情点击前往官网](https://docs.microsoft.com/zh-cn/sql/t-sql/statements/set-statements-transact-sql?view=sql-server-ver15) ）

08. 不允许使用 `FOR XML` 子句。

09. 用户定义函数可以嵌套；也就是说，用户定义函数可相互调用。 被调用函数开始执行时，嵌套级别将增加；被调用函数执行结束后，嵌套级别将减少。 用户定义函数的嵌套级别最多可达 32 级。 如果超出最大嵌套级别数，整个调用函数链将失败。 从 `Transact-SQL` 用户定义函数对托管代码的任何引用都将根据 32 级嵌套限制计入一个级别。 从托管代码内部调用的方法不根据此限制进行计数。

10. 下列 Service Broker 语句不能包含在 `Transact-SQL` 用户定义函数的定义中：

    - `BEGIN DIALOG CONVERSATION`
    - `END CONVERSATION`
    - `GET CONVERSATION GROUP`
    - `MOVE CONVERSATION`
    - `RECEIVE`
    - `SEND`
:::

#### 指定参数

用户定义函数采用零个或多个输入参数并返回标量值或表。 一个函数最多可以有 1024 个输入参数。 如果函数的参数有默认值，则调用该函数时必须指定 DEFAULT 关键字，才能获取默认值。 此行为与在用户定义存储过程中具有默认值的参数不同，在后一种情况下，忽略参数同样意味着使用默认值。 **用户定义函数不支持输出参数**。



#### 创建 UDF

**如果用户定义函数 (UDF) 不是使用 SCHEMABINDING 子句创建的，则对基础对象进行的任何更改可能会影响函数定义并在调用函数时可能导致意外结果。** 我们建议您实现以下方法之一，以便确保函数不会由于对于其基础对象的更改而过期：

> 1. 创建 UDF 时指定 `WITH SCHEMABINDING` 子句。 这确保除非也修改了函数，否则无法修改在函数定义中引用的对象。
> 2. 在修改在 UDF 定义中指定的任何对象后执行 [sp_refreshsqlmodule](https://docs.microsoft.com/zh-cn/sql/relational-databases/system-stored-procedures/sp-refreshsqlmodule-transact-sql?view=sql-server-ver15)  存储过程。

如果要创建不访问数据的 UDF，请指定 `SCHEMABINDING` 选项。 这将阻止查询优化器为涉及这些 UDF 的查询计划生成不必要的 `spool` 运算符。

可以在 `FROM` 子句中加入 `MSTVF`，但是会降低性能。 SQL Server 无法对可以加入 MSTVF 的某些语句使用所有优化技术，导致生成的查询计划不佳。 **若要获得最佳的性能，尽可能在基表之间使用联接而不是函数。**

```{literalinclude} ../result-file/mssql_function.sql
:language: mysql
```

:::{warning}
在视图和UDF中一般建议指定 `SCHEMABINDING` 选项， 因为其可以避免在修改基表时导致引用此基表的函数或视图出现意想不到的错误；同时，对于不访问数据的 UDF 来说， 指定 `SCHEMABINDING` 选项可以提升其性能。

所以如果在创建视图和函数需要指定 `SCHEMABINDING` 选项，那么需要确定基表的设计是否已经十分完善，如果仍然需要变动基表，那么就不建议在创建涉及这个基表的视图或函数时指定 `SCHEMABINDING` 选项，或者说不要创建涉及这个基表的视图或函数。
:::
 
[^id17]: 易百教程——MySQL存储函数,原文链接：<https://www.yiibai.com/mysql/stored-function.html>

[^id18]: 引用自 MySQL数据库之存储过程与存储函数 <https://www.cnblogs.com/chenhuabin/p/10142190.html>

[^id19]: 参考 SQL Server 文档： 用户定义函数 <https://docs.microsoft.com/zh-cn/sql/relational-databases/user-defined-functions/user-defined-functions?view=sql-server-ver15>

[^id20]: 参考 SQL Server 文档： 存储过程（数据库引擎） <https://docs.microsoft.com/zh-cn/sql/relational-databases/stored-procedures/stored-procedures-database-engine?view=sql-server-ver15>
