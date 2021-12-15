=======================
存储数据
=======================

python 中有两个使用比较广的连接数据库的库:

* PyMysql
* mysql-connector-python (官方)

在这里，将使用官方推荐的 mysql-connector-python，需要注意的是，该库并不是对所有 python 版本都支持。

这两个库在使用上大同小异，所有接下来专门针对 mysql-connector-python 库的使用进行说明。


mysql-connector-python code example [#]_
--------------------------------------------

**The following example shows how to connect to the MySQL server:**

.. code-block:: python

   import mysql.connector

   cnx = mysql.connector.connect(user='scott', password='password',
                                 host='127.0.0.1',
                                 database='employees')
   cnx.close()


**To handle connection errors, use the try statement and catch all errors using the errors.** Error exception:

.. code-block:: python

   import mysql.connector
   from mysql.connector import errorcode

   try:
      cnx = mysql.connector.connect(user='scott',
                                    database='employ')
   except mysql.connector.Error as err:
      if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
         print("Something is wrong with your user name or password")
      elif err.errno == errorcode.ER_BAD_DB_ERROR:
         print("Database does not exist")
      else:
         print(err)
   else:
      cnx.close()

插入记录
----------

我们首先打开与MySQL服务器的连接，并将连接对象存储 在变量中cnx。然后 ，我们使用连接的 方法创建一个新的游标，默认情况下为 MySQLCursor对象 cursor()。

我们可以通过调用数据库函数来进行明天的计算，但是为清楚起见，我们使用Python在该 datetime模块中进行了计算。

这两个INSERT语句都存储在名为add_employee和 的变量中add_salary。请注意，第二条 INSERT语句使用扩展的Python格式代码。

新员工的信息存储在元组中 data_employee。执行插入新雇员的查询，并且我们使用游标对象的属性检索该emp_no列（一个 AUTO_INCREMENT列） 的新插入值lastrowid。

接下来，我们使用emp_no保存数据的字典中的变量为新员工插入新薪水 。execute()如果发生错误，此字典将传递给游标对象的 方法。

**由于默认情况下Connector / Python关闭 自动提交，并且MySQL 5.5及更高版本InnoDB默认使用事务表，因此有必要使用连接commit()方法来提交更改。您也可以 使用该 方法回滚rollback()。**

.. code-block:: python

   from __future__ import print_function
   from datetime import date, datetime, timedelta
   import mysql.connector

   cnx = mysql.connector.connect(user='scott', database='employees')
   cursor = cnx.cursor()

   tomorrow = datetime.now().date() + timedelta(days=1)

   add_employee = ("INSERT INTO employees "
                  "(first_name, last_name, hire_date, gender, birth_date) "
                  "VALUES (%s, %s, %s, %s, %s)")
   add_salary = ("INSERT INTO salaries "
               "(emp_no, salary, from_date, to_date) "
               "VALUES (%(emp_no)s, %(salary)s, %(from_date)s, %(to_date)s)")

   data_employee = ('Geert', 'Vanderkelen', tomorrow, 'M', date(1977, 6, 14))

   # Insert new employee
   cursor.execute(add_employee, data_employee)
   emp_no = cursor.lastrowid

   # Insert salary information
   data_salary = {
   'emp_no': emp_no,
   'salary': 50000,
   'from_date': tomorrow,
   'to_date': date(9999, 1, 1),
   }
   cursor.execute(add_salary, data_salary)

   # Make sure data is committed to the database
   cnx.commit()

   cursor.close()
   cnx.close()

----

.. [#] 该章节引用 mysql-connector-python 文档，链接为 https://dev.mysql.com/doc/connector-python/en/connector-python-example-connecting.html
