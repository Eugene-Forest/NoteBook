==========================
 软件及其服务管理篇
==========================


.. note:: 
   本篇主要记录在centos7中的软件管理。且这些软件都是通过 :ref:`阿里yum源 <config-ali-yum>`  安装的。

#. 软件管理

   #. 更新本地yum源 ``yum makecache`` 
   #. 搜索软件 ``yum search SOFTWARE-NAME``
   #. 安装软件 ``yum install SOFTWARE-NAME``
   #. 卸载软件 ``yum remove SOFTWARE-NAME``

#. 服务管理

   #. 开启服务/启动软件 ``systemctl start SOFTWARE-NAME/Server-Name``
   #. 查看软件/服务运行状态 ``systemctl status SOFTWARE-NAME/Server-Name``
   #. 停止软件/服务运行 ``systemctl stop SOFTWARE-NAME/Server-Name``
   #. 软件/服务开机自启动 ``systemctl enable SOFTWARE-NAME/Server-Name``

#. 软件信息查看

   #. 查看是否已安装及其安装版本 ``yum list installed | grep SOFTWARE-NAME``
   #. 查看软件安装位置及其相关文件路径 ``whereis SOFTWARE-NAME``







