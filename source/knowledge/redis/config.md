# Redis 配置 [^id3]

Redis 的配置文件位于 Redis 安装目录下，文件名为 redis.conf(Windows下名为 redis.windows.conf)。

## 关于 redis server 的密码

redis没有实现访问控制这个功能，但是它提供了一个轻量级的认证方式，可以编辑redis.conf配置来启用认证。

```guess
127.0.0.1:6379> config get requirepass
1) "requirepass"
2) ""
```

## 不重启Redis设置密码

在配置文件中配置 requirepass 的密码（当 redis-server 重启时密码依然有效）。 但是如果配置文件中没添加密码，那么 redis-server 重启后，密码失效（如下文只通过终端窗口执行配置，那么重启 redis-server 之后配置失效）。

```guess
127.0.0.1:6379> config set requirepass e1f2677d7f87a5f2101a85f0908e6ff0
OK
127.0.0.1:6379> config get requirepass
(error) NOAUTH Authentication required.
127.0.0.1:6379> auth e1f2677d7f87a5f2101a85f0908e6ff0
OK
127.0.0.1:6379> config get requirepass
1) "requirepass"
2) "e1f2677d7f87a5f2101a85f0908e6ff0"
```

## CONFIG 命令

你可以通过 CONFIG 命令查看或设置配置项。

```guess
127.0.0.1:6379> CONFIG GET *
```

:::{note}
具体的配置名和配置效果有哪些请前往 [菜鸟教程—— Redis 配置](https://www.runoob.com/redis/redis-conf.html) 查看。
:::

```{raw} html
<hr width=400 size=10>
```

[^id3]: 参考菜鸟教程—— Redis 配置 <https://www.runoob.com/redis/redis-conf.html>
