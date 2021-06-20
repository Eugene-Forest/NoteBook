======================
 防火墙 管理篇
======================


.. note:: 
   在本篇中，记录的使用firewall防火墙的使用记录。在笔者使用的centos7中安装的防火墙都是firewall，所以此篇章的操作以firewall为基础进行。


对于防火墙，现阶段使用较多的是开启和移除端口。同时，一般的软件控制命令是无法命令防火墙的（比如systemctl命令）。

对服务器端口的控制
====================

#. 对服务器端口的控制

   #. 查看已经开放的端口 ``firewall-cmd --zone=public --list-ports``
   #. 添加开放6379端口 ``firewall-cmd --zone=public --add-port=6379/tcp --permanent``
   #. 从开放端口中移除6379端口 ``firewall-cmd --permanent --remove-port=6379/tcp``
   #. 重载防火墙配置 ``firewall-cmd --reload``
