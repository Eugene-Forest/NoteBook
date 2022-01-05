# null 函数

微软的 ISNULL() 函数用于规定如何处理 NULL 值。

NVL() , IFNULL() 和 COALESCE() 函数可以达到相同的结果。

## sql server

`isnull(expression,default_result)`

如果 expression 的结果为 null ， 那么isnull()函数将会返回 default_result。否则返回expression 的结果。

## Oracle

Oracle 没有 ISNULL() 函数。不过，我们可以使用 NVL() 函数达到相同的结果：

`NVL(expression,default_result)`

## MySQL

MySQL可以使用 COALESCE() 函数。

`COALESCE(expression,default_result)`

同时还有 IFNULL(expression,default_result)
