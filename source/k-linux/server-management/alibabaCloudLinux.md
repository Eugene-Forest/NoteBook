# Alibaba Cloud Linux 3/2

> 由于阿里云的服务器的 yum 源没有了可以直接安装 Mysql 等常用的软件的功能，所以此章节主要用来记录在阿里云服务器中使用安装包安装软件方式。

## 在Linux实例中安装MySQL数据库

> 参考原文： [在Linux实例中安装MySQL数据库](https://help.aliyun.com/zh/ecs/use-cases/manually-deploy-mysql-on-an-ecs-instance-that-runs-centos)

手动部署MySQL时，已有ECS实例必须满足以下条件：

* 实例已分配公网IP地址或绑定弹性公网IP（EIP）。

* 操作系统：CentOS 7.x、Alibaba Cloud Linux 2、Alibaba Cloud Linux 3。

* 实例安全组的入方向规则已放行22、80、443、3306端口。具体操作，请参见添加安全组规则。

### 安装MySQL

1. 安装 mysql 前，需要获取安装包链接， [Mysql Rpm](https://repo.mysql.com/); 运行以下命令，更新YUM源。

``` bash
sudo rpm -Uvh https://repo.mysql.com/mysql80-community-release-el7-7.noarch.rpm
```

2. （可选）当操作系统为Alibaba Cloud Linux 3时，请执行如下命令，安装MySQL所需的库文件。

``` bash
sudo rpm -Uvh https://mirrors.aliyun.com/alinux/3/updates/x86_64/Packages/compat-openssl10-1.0.2o-4.0.1.al8.x86_64.rpm
```

3. 运行以下命令，安装MySQL。

> `--enablerepo=mysql80-community` 换成自己实际的版本

```bash
sudo yum -y install mysql-community-server --enablerepo=mysql80-community --nogpgcheck
```

4. 查看版本号

```bash
mysql -V
```

```text
mysql Ver 8.0.33 for Linux on x86_64 (MySQL Community Server - GPL)
```

#### 异常解决

* 出现 libaio 软件缺失，需要安装 [libaio Rpm](https://pkgs.org/search/?q=Libaio)

``` bash
sudo rpm -Uvh https://mirror.stream.centos.org/9-stream/BaseOS/x86_64/os/Packages/libaio-0.3.111-13.el9.i686.rpm
```

* 出现报错： GPG check FAILED

  * 确保 安装 mysql 的命令带有 `--nogpgcheck`

### 配置 Mysql

1. 运行以下命令，启动并设置开机自启动MySQL服务。

```
sudo systemctl start mysqld
sudo systemctl enable mysqld
```

> `systemctl status mysqld` 可以查看 mysql 的运行状态。状态为 Active 即可。

3. 运行以下命令，获取并记录root用户的初始密码。

```
sudo grep 'temporary password' /var/log/mysqld.log
```

5. 初始化 Mysql root 用户配置，对MySQL进行安全性配置。

```
sudo mysql_secure_installation
```

* 根据提示信息，重置MySQL数据库root用户的密码。

```
Enter password for user root: #输入已获取的root用户初始密码

The existing password for the user account root has expired. Please set a new password.

New password: #输入新的MySQL密码

Re-enter new password: #重复输入新的MySQL密码
The 'validate_password' component is installed on the server.
The subsequent steps will run with the existing configuration
of the component.
Using existing password for root.
Change the password for root ? ((Press y|Y for Yes, any other key for No) :Y #输入Y选择更新MySQL密码。您也可以输入N不再更新MySQL密码。

New password: #输入新的MySQL密码

Re-enter new password: #重复输入新的MySQL密码

Estimated strength of the password: 100
Do you wish to continue with the password provided?(Press y|Y for Yes, any other key for No) :Y #输入Y确认使用已设置的密码。
```

* 根据提示信息，删除匿名用户。

```
By default, a MySQL installation has an anonymous user,
allowing anyone to log into MySQL without having to have
a user account created for them. This is intended only for
testing, and to make the installation go a bit smoother.
You should remove them before moving into a production
environment.

Remove anonymous users? (Press y|Y for Yes, any other key for No) :Y #输入Y删除MySQL默认的匿名用户。
Success.
```

* 禁止root账号远程登录。

```
Normally, root should only be allowed to connect from
'localhost'. This ensures that someone cannot guess at
the root password from the network.

Disallow root login remotely? (Press y|Y for Yes, any other key for No) :Y #输入Y禁止root远程登录。
Success.
```

* 删除test库以及对test库的访问权限。

```
By default, MySQL comes with a database named 'test' that
anyone can access. This is also intended only for testing,
and should be removed before moving into a production
environment.


Remove test database and access to it? (Press y|Y for Yes, any other key for No) :Y #输入Y删除test库以及对test库的访问权限。
 - Dropping test database...
Success.

 - Removing privileges on test database...
Success.
```

* 重新加载授权表。

```
Reloading the privilege tables will ensure that all changes
made so far will take effect immediately.

Reload privilege tables now? (Press y|Y for Yes, any other key for No) :Y #输入Y重新加载授权表。
Success.

All done!
```

#### 配置远程用户

```
#创建数据库用户dmsTest,并授予远程连接权限。
create user 'dmsTest'@'%' identified by 'Ecs@123****'; 
#为dmsTest用户授权数据库所有权限。
grant all privileges on *.* to 'dmsTest'@'%'; 
#刷新权限。
flush privileges; 
```
