# 关于 MySQL 测试库的下载和安装

(mysql-test-db-installer)=

## 下载 test_db 库

首先，前往 GitHub 仓库下载 [datacharmer/test_db](https://github.com/datacharmer/test_db)  项目 。

```{image} ../../img/sql/mysql_test_db.png
:alt: test_db installer
```

:::{note}

如果无法连接 Github 可在 Gitee 中搜索 test_db 查看相关项目，有许多 fork test_db 的项目。如 [xudayjt/test_db](https://gitee.com/xudayjt/test_db?_from=gitee_search)
:::

## 安装 employees 库

下载完目标项目后，我们要通过命令行来安装测试仓库。

:::{attention}
直接参考项目的 README.MD 文件即可，在此只需要注意命令的运行格式以及文件位置。
:::

:::{important}
**为防止在将来会使用到中文字符，最好在创建数据库的时候就指定编码格式，以免再将来使用时要大量修改已有的表和表的字段的编码。**

由于该数据库在创建时没有指定编码格式，所以可能会受到数据库管理系统的默认编码格式的影响变成拉丁格式的编码，解决的方法时将 `employees.sql` 文件中的每个创建语句都指定编码格式 （ `utf8mb4` ）;

{download}`指定utf8mb4编码的 employees.sql <./result-file/employees.sql>`

```mysql
-- 参考指定编码的语句格式
CREATE DATABASE IF NOT EXISTS employees character set utf8mb4;

CREATE TABLE employees (
    emp_no      INT             NOT NULL,
    birth_date  DATE            NOT NULL,
    first_name  VARCHAR(14)     NOT NULL,
    last_name   VARCHAR(16)     NOT NULL,
    gender      ENUM ('M','F')  NOT NULL,
    hire_date   DATE            NOT NULL,
    PRIMARY KEY (emp_no)
) character set utf8mb4;
```
:::

如在 Linux 下安装：

```bash
# 安装
[root@eugene-forest test_db]$ mysql -t -u root -p < employees.sql
Enter password:

+-----------------------------+
| INFO                        |
+-----------------------------+
| CREATING DATABASE STRUCTURE |
+-----------------------------+
+------------------------+
| INFO                   |
+------------------------+
| storage engine: InnoDB |
+------------------------+
+---------------------+
| INFO                |
+---------------------+
| LOADING departments |
+---------------------+
+-------------------+
| INFO              |
+-------------------+
| LOADING employees |
+-------------------+
+------------------+
| INFO             |
+------------------+
| LOADING dept_emp |
+------------------+
+----------------------+
| INFO                 |
+----------------------+
| LOADING dept_manager |
+----------------------+
+----------------+
| INFO           |
+----------------+
| LOADING titles |
+----------------+
+------------------+
| INFO             |
+------------------+
| LOADING salaries |
+------------------+

# （回车/enter）

+---------------------+
| data_load_time_diff |
+---------------------+
| 00:00:28            |
+---------------------+
```

### 测试 [^id3]

```bash
# 测试
[root@eugene-forest test_db]$ mysql -t -u root -p < test_employees_md5.sql
Enter password:

+----------------------+
| INFO                 |
+----------------------+
| TESTING INSTALLATION |
+----------------------+
+--------------+------------------+------------------------------------------+
| table_name   | expected_records | expected_crc                             |
+--------------+------------------+------------------------------------------+
| departments  |                9 | 4b315afa0e35ca6649df897b958345bcb3d2b764 |
| dept_emp     |           331603 | d95ab9fe07df0865f592574b3b33b9c741d9fd1b |
| dept_manager |               24 | 9687a7d6f93ca8847388a42a6d8d93982a841c6c |
| employees    |           300024 | 4d4aa689914d8fd41db7e45c2168e7dcb9697359 |
| salaries     |          2844047 | b5a1785c27d75e33a4173aaa22ccf41ebd7d4a9f |
| titles       |           443308 | d12d5f746b88f07e69b9e36675b6067abb01b60e |
+--------------+------------------+------------------------------------------+
ERROR 1271 (HY000) at line 60: Illegal mix of collations for operation 'concat_ws'
```
 
[^id3]: 2021年11月10日测试未成功。 ERROR 1271 (HY000) at line 60: Illegal mix of collations for operation 'concat_ws' 。

## 安装 SQL in 10 Minutes 的测试库

[官网下载 SQL in 10 Minutes 的测试库](https://forta.com/books/0135182794/)

{download}`SQL in 10 Minutes 的测试库 <./result-file/TYSQL5_MySQL.zip>`

包结构

- create.txt
- populate.txt
- README.pdf

先运行 `create.txt` 中的 SQL 语句 , 再运行 `populate.txt` 中的 SQL 语句。
