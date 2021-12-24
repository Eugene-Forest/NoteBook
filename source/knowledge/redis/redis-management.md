# Redis 管理

## CentOS 7 下的 Redis

### yum 安装

1. 查看需要安装的相关软件 `yum list redis`
2. 安装 `yum install redis -y`
3. 查看安装了的软件 `yum list installed | grep redis`

```bash
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
```

### 运行初始化

```shell
# 运行命令
$ systemctl start redis
# 开机自启动命令
$ systemctl enable redis
```

### 查看redis进程信息

查看redis进程信息 `ps -ef | grep redis`

```shell
[root@eugene-forest ~]# ps -ef | grep redis
redis      884     1  0 Mar22 ?        00:12:26 /usr/bin/redis-server *:6379
root     15861 15829  0 16:56 pts/1    00:00:00 grep --color=auto redis
```

:::{note}

由查看进程信息我们就知道，redis有服务端和客户端之分。而且redis server是通过服务器的6379来提供服务的。所以如果想要在本地之外访问redis服务就需要通过防火墙把6379端口打开。
:::

### 登录redis客户端

添加redis-client登录密码：

1. 执行 `whereis redis` 找到redis的conf文件
2. 通过vim打开配置文件 `vim /etc/redis.conf`
3. 在文件中搜索字符 **requirepass** 并添加一行配置 *requirepass password*, 然后保存即可。

修改完成后登录：

```shell
[root@eugene-forest ~]# redis-cli
127.0.0.1:6379> auth password
OK
```

```{raw} html
<hr width=400 size=10>
```

## Windows 下的 Redis [^id5]

下载地址: [redis for windows](https://github.com/tporadowski/redis/releases)

```{image} ../../img/redis/github-redis.png
:alt: redis for windows
```

```guess
# 打开一个 cmd 窗口 使用 cd 命令切换目录到 C:\<path-to-redis> 运行：
redis-server.exe <redis.windows.conf>
```

:::{note}

如果只是运行 redis-server.exe 而没有后面的 conf 文件名参数，那么配置文件的变动就不会生效（无密码和其他配置）。
:::

```{raw} html
<hr width=400 size=10>
```

[^id5]: 参考菜鸟教程——Redis安装 <https://www.runoob.com/redis/redis-install.html>
