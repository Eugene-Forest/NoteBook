======================
Linux 下的 Redis 
======================

yum安装
===========

#. 查看需要安装的相关软件 ``yum list redis``
#. 安装 ``yum install redis -y``
#. 查看安装了的软件 ``yum list installed | grep redis``

.. code-block:: bash

   [root@eugene-forest ~]# yum list redis
   Loaded plugins: fastestmirror
   Loading mirror speeds from cached hostfile
   * centos-sclo-rh: mirrors.tuna.tsinghua.edu.cn
   * centos-sclo-sclo: mirrors.tuna.tsinghua.edu.cn
   * webtatic: uk.repo.webtatic.com
   Available Packages
   redis.x86_64                   3.2.12-2.el7                   epel

   # 安装
   [root@eugene-forest ~]# yum install redis -y

   # 查看安装了的软件
   [root@eugene-forest ~]# yum list installed | grep redis


运行初始化
============

.. code-block:: shell

   # 运行命令
   $ systemctl start redis
   # 开机自启动命令
   $ systemctl enable redis


查看redis进程信息
==================

查看redis进程信息 ``ps -ef | grep redis``

.. code-block:: shell

   [root@eugene-forest ~]# ps -ef | grep redis
   redis      884     1  0 Mar22 ?        00:12:26 /usr/bin/redis-server *:6379
   root     15861 15829  0 16:56 pts/1    00:00:00 grep --color=auto redis

登录redis客户端
===============

由查看进程信息我们就知道，redis有服务端和客户端之分。

添加redis-client登录密码：

#. 执行 ``whereis redis`` 找到redis的conf文件
#. 通过vim打开配置文件 ``vim /etc/redis.conf``
#. 在文件中搜索字符 **requirepass** 并添加一行配置 *requirepass password*, 然后保存即可。

修改完成后登录：

.. code-block:: shell

   [root@eugene-forest ~]# redis-cli
   127.0.0.1:6379> auth password
   OK