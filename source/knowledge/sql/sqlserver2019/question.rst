================================
window mssql 问题集
================================


通过端口1433连接到主机127.0.0.1的 TCP/IP 连接失败，错误:“connect timed out”的解决方法
================================================================================================


完整报错：通过端口1433 连接到主机127.0.0.1 的TCP/IP 连接失败。错误:“connect timed out。请验证连接属性，并检查 SQL Server 的实例正在主机上运行，且在此端口接受 TCP/IP 连接，还要确保防火墙没有阻止到此端口的 TCP 连接。


**可能原因： sql server 的网络配置中的 TCP/IP 协议没有启用。**

解决方法： 

*打开SQLServer 配置管理器------->SQLServer for MSQLSERVER------->TCP/IP------->如果没有启动，则启动*


.. image:: ../../img/sqlserver/sqlserver-tcp-config.png
   :alt: sqlserver-tcp-config