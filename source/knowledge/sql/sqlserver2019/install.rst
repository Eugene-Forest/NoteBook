===============================
sql server 的安装
===============================

在 windows 中安装
==================

.. attention:: 

   详情请前往官网： `下载免费的专用版本 <https://www.microsoft.com/zh-cn/sql-server/sql-server-downloads#>`_ 

在 windows 中安装较为简单，只需要下载安装包即可。

唯一要提及的是，需要选择版本类型，这个根据实际需求来选择。

* Developer 版 : SQL Server 2019 Developer 是一个全功能免费版本，许可在非生产环境下用作开发和测试数据库。
* Express 版本 : SQL Server 2019 Express 是 SQL Server 的一个免费版本，非常适合用于桌面、Web 和小型服务器应用程序的开发和生产。
* 其他付费版本



在 linux -- centos 7.x 中安装
====================================

.. attention:: 

   详情请前往官网 `快速入门：在 Red Hat 上安装 SQL Server 并创建数据库 <https://docs.microsoft.com/zh-cn/sql/linux/quickstart-install-connect-red-hat?view=sql-server-ver15>`_ 

   如果运行内存不大于2G，请不要使用官网在线安装。

* 添加源： ``sudo curl -o /etc/yum.repos.d/mssql-server.repo https://packages.microsoft.com/config/rhel/7/mssql-server-2019.repo``
* 安装： ``sudo yum install -y mssql-server``
* 运行： ``sudo /opt/mssql/bin/mssql-conf setup``
* 通过 systemctl 命令控制软件启动情况
* 如需远程登录，请开启防火墙的 1433 端口


Linux 下安装sql server 时 2G内存限制的解决方案
======================================================

**通过官方指南安装 sql server ， 可能会出现2G内存限制问题而导致 sql server 无法运行。**

笔者的实际服务器基本配置：

* CentOS Linux release 7.8.2003 (Core)
* 运行内存 2G
* 云盘/系统盘 40G


在阿里云学生机中安装 sql server 2017
--------------------------------------------

需要注意的是：不能使用最新版本！！！  不能在线下载！！！

离线下载路径： ``wget   https://packages.microsoft.com/rhel/7/mssql-server-2017/mssql-server-14.0.3030.27-1.x86_64.rpm`` 

-------------------------
添加MSSQL的中文支持
-------------------------

.. code-block:: shell

   export MSSQL_COLLATION='Chinese_PRC_CI_AS'
   export MSSQL_LCID='2052'
   # 这里的两句export增加的环境变量，是为了添加MSSQL的中文支持，否则安装好后再去添加会十分困难。


下载完之后，进入下载目录后 执行 ``yum install mssql-server-14.0.3030.27-1.x86_64.rpm`` 

-------------------
修改内存限制
-------------------

.. code-block:: shell

   cd /opt/mssql/bin/ # 进入目录 
   mv sqlservr sqlservr.bak # 保存备份文件 
   python # 使用python修改内存限制代码
   >>> oldfile = open("sqlservr.bak", "rb").read()
   >>> newfile = oldfile.replace("\x00\x94\x35\x77", "\x00\x80\x84\x1e")
   >>> open("sqlservr", "wb").write(newfile)
   >>>exit()


----------------
安装配置
----------------

进行 sql server 安装配置 

.. code-block:: shell

   export MSSQL_COLLATION='Chinese_PRC_CI_AS'
   export MSSQL_LCID='2052'
   sudo /opt/mssql/bin/mssql-conf setup

   #  然后选择版本(免费的推荐选择Developer)设置密码即可。学习使用推荐使用开发者版本。
   Choose an edition of SQL Server:
      1) Evaluation (free, no production use rights, 180-day limit)
      2) Developer (free, no production use rights)
      3) Express (free)
      4) Web (PAID)
      5) Standard (PAID)
      6) Enterprise (PAID) - CPU Core utilization restricted to 20 physical/40 hyperthreaded
      7) Enterprise Core (PAID) - CPU Core utilization up to Operating System Maximum
      8) I bought a license through a retail sales channel and have a product key to enter.
   
   ......

.. note:: 

   如果遇到： ``/bin/bash: /opt/mssql/bin/sqlservr: 权限不够`` ，执行 ： ``chmod 777 sqlservr`` 后再开启服务 ``systemctl start mssql-server`` 



卸载 sql server 
--------------------

.. code-block:: shell

   sudo yum remove mssql-server

   # 删除包不会删除生成的数据库文件。 如果你想要删除的数据库文件，使用以下命令：
   sudo rm -rf /var/opt/mssql/


.. attention:: 
   
   需要注意的是，通过以上命令卸载 mssql 后，最好重启一次 linux , 因为一些配置还存在：比如 还能执行 systemctl status mssql-server 。


重置系统管理 (SA) 密码
-----------------------

.. code-block:: shell

   sudo systemctl stop mssql-server
   export MSSQL_COLLATION='Chinese_PRC_CI_AS'
   export MSSQL_LCID='2052'
   sudo /opt/mssql/bin/mssql-conf setup

----

参考文章：

* `SQL Server 2017 Linux安装说明以及避坑指南 <https://www.jianshu.com/p/6acb714e37be>`_ 
* `Linux 下安装sql server 时 2G内存限制的最新（2019-08-15） 解决方案 <https://www.cnblogs.com/xtdhb/p/11357702.html>`_ 
* `卸载 SQL Server <https://blog.csdn.net/cangyuemis/article/details/92830712>`_ 
