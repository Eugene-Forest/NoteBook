===========================
java 虚拟机环境安装
===========================


.. note:: 
   以下Java版本为1.8.0。


检查本机是否安装java
------------------------

.. code-block:: shell

   yum list installed | grep java


通过阿里yum源安装
----------------------

.. code-block:: shell

   yum install java-1.8.0-openjdk* -y

运行version命令查看是否安装
-----------------------------

.. code-block:: shell

   [root@eugene-forest ~]# java -version
   openjdk version "1.8.0_282"
   OpenJDK Runtime Environment (build 1.8.0_282-b08)
   OpenJDK 64-Bit Server VM (build 25.282-b08, mixed mode)
   [root@eugene-forest ~]# javac -version
   javac 1.8.0_282
   [root@eugene-forest ~]# 

yum安装之后的java路径/usr/lib/jvm
-------------------------------------

.. code-block:: shell

   [root@eugene-forest ~]# whereis jvm
   jvm: /usr/lib/jvm /etc/jvm /usr/share/jvm
   [root@eugene-forest ~]# cd /usr/lib/jvm
   [root@eugene-forest jvm]# ls
   java
   java-1.8.0
   java-1.8.0-openjdk
   java-1.8.0-openjdk-1.8.0.282.b08-1.el7_9.x86_64
   java-openjdk
   jre
   jre-1.8.0
   jre-1.8.0-openjdk
   jre-1.8.0-openjdk-1.8.0.282.b08-1.el7_9.x86_64
   jre-openjdk

jvm目录下的文件夹看似多，实际指向的都是同一文件夹，比如java\*的文件夹指向的实际文件夹是相同的，jre\*的文件夹指向的实际文件夹也是相同的。



关于运行java文件出现 ``Error: Could not find or load main class ..``
------------------------------------------------------------------------

.. note:: 
   情况限定于java文件以及.class文件均在同一目录下。


------------------------
CLASSPATH设置问题
------------------------

linux下 java1.8.0的配置是可以省略的。


------------------------------------------
判断java文件的头部是否包含 package 语句
------------------------------------------

删除package语句。

