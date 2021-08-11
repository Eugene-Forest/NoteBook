=====================
redis 的简单配置
=====================


redis没有实现访问控制这个功能，但是它提供了一个轻量级的认证方式，可以编辑redis.conf配置来启用认证。

.. code-block:: redis

   127.0.0.1:6379> config get requirepass
   1) "requirepass"
   2) ""

不重启Redis设置密码
===========================


.. code-block:: redis

   127.0.0.1:6379> config set requirepass e1f2677d7f87a5f2101a85f0908e6ff0
   OK
   127.0.0.1:6379> config get requirepass
   (error) NOAUTH Authentication required.
   127.0.0.1:6379> auth e1f2677d7f87a5f2101a85f0908e6ff0
   OK
   127.0.0.1:6379> config get requirepass
   1) "requirepass"
   2) "e1f2677d7f87a5f2101a85f0908e6ff0"

 在配置文件中配置requirepass的密码（当redis重启时密码依然有效）。 但是如果配置文件中没添加密码，那么redis重启后，密码失效（如上文只通过终端窗口执行配置，那么重启 redis 之后配置失效）。