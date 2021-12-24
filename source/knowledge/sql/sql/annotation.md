# 注释

一般来说，通用的行注释为 `--` , 另外还有一些数据库支持 `#` 的行注释。

多行注释为 `/*  ...  */` ; 这种注释方法常用于将代码注释以调试和测试。

```sql
-- the sampling code
/*
SELECT DISTINCT vend_id,prod_price FROM products;*/
SELECT vend_id,prod_price FROM products; -- the sampling code
```
