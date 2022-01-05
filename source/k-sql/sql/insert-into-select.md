# INSERT INTO SELECT

通过 SQL，您可以从一个表复制信息到另一个表。

INSERT INTO SELECT 语句从一个表复制数据，然后把数据插入到一个已存在的表中。目标表中任何已存在的行都不会受影响。
 
我们可以从一个表中复制所有的列插入到另一个已存在的表中：

```sql
INSERT INTO table2
SELECT * FROM table1;
```

或者我们可以只复制希望的列插入到另一个已存在的表中：

```sql
INSERT INTO table2
(column_name(s))
SELECT column_name(s)
FROM table1;
```

## 拓展： SELECT INTO

SELECT INTO 语句从一个表复制数据，然后把数据插入到另一个新表中。

:::{attention}
MySQL 数据库不支持 SELECT ... INTO 语句，但支持 INSERT INTO ... SELECT 。

当然你可以使用以下语句来拷贝表结构及数据：

```sql
CREATE TABLE 新表
AS
SELECT * FROM 旧表
```
:::

我们可以复制所有的列插入到新表中：

```sql
SELECT *
INTO newtable [IN externaldb]
FROM table1;
```

或者只复制希望的列插入到新表中：

```sql
SELECT column_name(s)
INTO newtable [IN externaldb]
FROM table1;
```

:::{note}

新表将会使用 SELECT 语句中定义的列名称和类型进行创建。您可以使用 AS 子句来应用新名称。
:::

## 比较 SELECT INTO 和 INSERT INTO SELECT

select into from 和 insert into select 都是用来复制表

**两者的主要区别为： select into from 要求目标表不存在，因为在插入时会自动创建；insert into select from 要求目标表存在。**
