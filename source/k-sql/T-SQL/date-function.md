# T-SQL 日期函数

以下是MS SQL Server中的日期函数列表。

- `GETDATE()` 它将返回当前日期和时间。
- `DATEPART(datepart, datecolumnname)` 它将返回日期或时间的一部分。
- `DATEADD(datepart, number, datecolumnname)` 它将通过加或减日期和时间间隔显示日期和时间。
- `DATEDIFF(datepart, startdate, enddate)` 它将显示两个日期之间的日期和时间。
- `CONVERT(datatype, expression, style)` 它将以不同的格式显示日期和时间。
 
## GETDATE() / getDate() / getdate()

:::{note}

SQL 的关键字和函数名不区分大小写。所以，下文的函数名的写法将使用驼峰写法。
:::

它将返回当前日期和时间。

```sql
select getdate() as now_time
```
 
## datePart(datepart, datecolumnname)

它将返回日期或时间的一部分。

```sql
select DATEPART(YEAR,GETDATE()) as now_year
```

| datepart | 缩写            |
| -------- | --------------- |
| 年       | yy, yyyy , year |
| 季度     | qq, q           |
| 月       | mm, m , month   |
| 年中的日 | dy, y           |
| 日       | dd, d           |
| 周       | wk, ww          |
| 星期     | dw, w           |
| 小时     | hh              |
| 分钟     | mi, n           |
| 秒       | ss, s           |
| 毫秒     | ms              |
| 微妙     | mcs             |
| 纳秒     | ns              |

:::{attention}
该篇章的所有 datepart 参数都是参考上表。
:::
 
## dateAdd(datepart, number, datecolumnname)

它将通过加(number为正)或减(number为负)日期和时间间隔显示日期和时间。

```sql
SELECT DATEADD(DAY,10,GETDATE()) AS ten_day_later_datetime
SELECT DATEADD(DAY,-10,GETDATE()) AS ten_day_before_datetime
```
 
## DATEDIFF(datepart, startdate, enddate)

返回两个日期之间的时间。  (enddate-startdate的结果并转换为以datepart为单位的数值)

```sql
SELECT DATEDIFF(DAY,(SELECT DATEADD(DAY,10,GETDATE()) AS ten_day_later_datetime),GETDATE()) as diff_time
-- result is -10
```
 
## CONVERT(datatype, expression, style)

CONVERT() 函数是把日期转换为新数据类型的通用函数。

CONVERT() 函数可以用不同的格式显示日期/时间数据。

| Style ID     | Style 格式                            |
| ------------ | ------------------------------------- |
| 100 或者 0   | mon dd yyyy hh:miAM （或者 PM）       |
| 101          | mm/dd/yy                              |
| 102          | yy.mm.dd                              |
| 103          | dd/mm/yy                              |
| 104          | dd.mm.yy                              |
| 105          | dd-mm-yy                              |
| 106          | dd mon yy                             |
| 107          | Mon dd, yy                            |
| 108          | hh:mm:ss                              |
| 109  或者 9  | mon dd yyyy hh:mi:ss:mmmAM（或者 PM） |
| 110          | mm-dd-yy                              |
| 111          | yy/mm/dd                              |
| 112          | yymmdd                                |
| 113  或者 13 | dd mon yyyy hh:mm:ss:mmm(24h)         |
| 114          | hh:mi:ss:mmm(24h)                     |
| 120  或者 20 | yyyy-mm-dd hh:mi:ss(24h)              |
| 121  或者 21 | yyyy-mm-dd hh:mi:ss.mmm(24h)          |
| 126          | yyyy-mm-ddThh:mm:ss.mmm（没有空格）   |
| 130          | dd mon yyyy hh:mi:ss:mmmAM            |
| 131          | dd/mm/yy hh:mi:ss:mmmAM               |

```sql
select CONVERT(varchar(255),getdate(),110) as format_date
```
