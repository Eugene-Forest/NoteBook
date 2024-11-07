# Navicat Premium 实用技巧

## Navicat 中怎么查看数据库密码

有时候，我们在连接 Navicat 中创建了一个数据库连接并成功连接后忘记了密码，这个时候我们可以通过以下方法来通过 Navicat 现有的数据库连接配置来获取其密码。

- 第一步: 点击 Navicat 菜单栏 {menuselection}`文件-->导出连接..` ，导出数据库连接配置，导出连接获取到 `connections.ncx` 文件

```{figure} ./navicat-connect-config-output.png
:align: center
:alt: navicat-connect-config-output.png

导出数据库连接配置(勾选导出密码)
```

```{literalinclude} ./connections.ncx
:language: xml
:caption: 导出的 connections.ncx 文件示例
```

- 第二步：找到加密密码，然后添加到 PHP 程序中运行破解

在导出的 `connections.ncx` 文件中找到 `Password` ，然后复制到下面 PHP 代码中。（ 在 `decode=navicatPassword->decrypt('复制出来的密码');` ）

```{literalinclude} ./navicat-decode-password.php
:language: php
:caption: 解码程序
```

如果自己没有运行 PHP 的环境，那么可以直接到网上找在线运行程序的网站，例如 [https://tool.lu/coderunner](https://tool.lu/coderunner) ，或者直接 [百度-代码在线运行](https://www.baidu.com/s?tn=88093251_47_hao_pg&ie=utf-8&wd=%E4%BB%A3%E7%A0%81%E5%9C%A8%E7%BA%BF%E8%BF%90%E8%A1%8C)

## Linux Mysql8.0+数据库密码重置办法

前提：mysql 部署在在自己的 Linux 服务器。

- 关闭 mysql 服务
  - `systemctl stop mysqld`
- 找到 my.cnf mysql的配置文件
  - `find / -name my.cnf`
- 到达配置文件目录，进入编辑模式 `vim my.cnf`
- 在文件末尾加入 *skip-grant-tables*

```txt
datadir=/var/lib/mysql
socket=/var/lib/mysql/mysql.sock

log-error=/var/log/mysqld.log
pid-file=/var/run/mysqld/mysqld.pid
skip-grant-tables
```

- 重新开启 mysql 服务
  - `systemctl start mysqld`
- 进入 mysql ,不用输入密码直接回车进入。
  - `mysql -u root -p`, 回车进入，然后不输入密码再回车，即可进入 mysql。
- `use mysql;` , 然后执行命令清空指定用户的密码 `update user set authentication_string="" where user = "root";`
- 退出 mysql , 然后重新编辑 **my.cnf** 文件，将 `skip-grant-tables` 注释或删除掉。
- 重启 mysql , `systemctl restart mysqld`;
- 进入 mysql ,不用输入密码直接回车进入。
  - `mysql -u root -p`, 回车进入，然后不输入密码再回车，即可进入 mysql。
- 重置指定用户密码，`alter user 'root'@'localhost' identified by 'NewPassword';`
