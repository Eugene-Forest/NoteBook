========================
配置yum源
========================

.. _config-ali-yum:


配置阿里yum源
----------------

前提条件：备份好原来的repo文件+保持网络通畅（linux虚拟机打开网络连接）


------
备份
------

.. code-block:: shell

   mv /etc/yum.repos.d/CentOS-Base.repo /etc/yum.repos.d/CentOS-Base.repo.backup

-------------------------------------------------
下载新的CentOS-Base.repo 到/etc/yum.repos.d/
-------------------------------------------------

.. code-block:: shell

   # CentOS 5

   wget -O /etc/yum.repos.d/CentOS-Base.repo http://mirrors.aliyun.com/repo/Centos-5.repo

   或者

   curl -o /etc/yum.repos.d/CentOS-Base.repo http://mirrors.aliyun.com/repo/Centos-5.repo

   # CentOS 6

   wget -O /etc/yum.repos.d/CentOS-Base.repo http://mirrors.aliyun.com/repo/Centos-6.repo

   或者

   curl -o /etc/yum.repos.d/CentOS-Base.repo http://mirrors.aliyun.com/repo/Centos-6.repo

   # CentOS 7

   wget -O /etc/yum.repos.d/CentOS-Base.repo http://mirrors.aliyun.com/repo/Centos-7.repo

   或者

   curl -o /etc/yum.repos.d/CentOS-Base.repo http://mirrors.aliyun.com/repo/Centos-7.repo


---------------------------------------
删除本地yum缓存并更新
---------------------------------------

运行 ``yum clean all`` 清空缓存，然后运行 ``yum makecache`` 生成缓存。