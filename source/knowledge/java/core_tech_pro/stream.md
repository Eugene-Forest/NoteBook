# Java 8 Stream [^id8]

Java 8 API 添加了一个新的抽象称为 流Stream，可以让你以一种声明的方式处理数据。

Stream 使用一种类似用 SQL 语句从数据库查询数据的直观方式来提供一种对 Java 集合运算和表达的高阶抽象。

Stream API 可以极大提高 Java 程序员的生产力，让程序员写出高效率、干净、简洁的代码。

这种风格将要处理的 **元素集合看作一种流** ， 流在管道中传输（ *即数据在管道中传输* ）， 并且可以在管道的节点上进行处理， 比如筛选， 排序，聚合等。

元素流在管道中经过中间操作（intermediate operation）的处理，最后由最终操作(terminal operation)得到前面处理的结果。

```guess
+--------------------+       +------+   +------+   +---+   +-------+
| stream of elements +-----> |filter+-> |sorted+-> |map+-> |collect|
+--------------------+       +------+   +------+   +---+   +-------+
```

转化为可供参考的代码如下所示：

```Java
List<Integer> transactionsIds =
widgets.stream()
            .filter(b -> b.getColor() == RED)
            .sorted((x,y) -> x.getWeight() - y.getWeight())
            .mapToInt(Widget::getWeight)
            .sum();
```

(java-stream)=

## 什么是 stream ?

Stream（流） **是一个来自数据源的元素队列** 并支持聚合操作。

**数据源** 流的来源。 可以是集合，数组，I/O channel， 产生器generator 等

**聚合操作** 类似SQL语句一样的操作， 比如filter, map, reduce, find, match, sorted等。

和以前的 Collection 操作不同， Stream 操作还有两个基础的特征：

1. Pipelining: 中间操作都会返回流对象本身。 这样多个操作可以串联成一个管道， 如同流式风格（fluent style）。 这样做可以对操作进行优化， 比如延迟执行(laziness)和短路( short-circuiting)。
2. 内部迭代： 以前对集合遍历都是通过Iterator或者For-Each的方式, 显式的在集合外部进行迭代， 这叫做外部迭代。 Stream提供了内部迭代的方式， 通过访问者模式(Visitor)实现。

## 生成流

在 Java 8 中, 集合接口有两个方法来生成流：

1. **stream()** − 为集合创建 *串行流*。
2. **parallelStream()** − 为集合创建 *并行流*。

## 聚合操作

可根据操作方法的返回结果将其分为两类：将返回流的操作方法称为中间操作，其他称为终止操作。

### 中间操作

多个中间操作可以连接起来形成一个流水线，除非流水线上触发终止操作，否则中间操作不会执行任何的处理！而在终止操作时一次性全部处理，称为“惰性求值”

| 方法                      | 描述                                     |
| ----------------------- | -------------------------------------- |
| filter(Predicate p)     | 接收 Lambda ， 从流中排除某些元素。                 |
| distinct()              | 筛选，通过流所生成元素的 hashCode() 和 equals() 去   |
| limit(long maxSize)     | 截断流，使其元素不超过给定数量。                       |
| map(Function f)         | 接收一个函数作为参数，该函数会被应用到每个元素上，并将其映射成一个新的元素。 |
| flatMap(Function f)     | 接收一个函数作为参数，将流中的每个值都换成另一个流，然后把所有流连接成一个流 |
| sorted(Comparator comp) | 产生一个新流，其中按比较器顺序排序                      |
| sorted()                | 产生一个新流，其中按自然顺序排序                       |

#### filter

filter 方法用于通过设置的条件过滤出元素。

```{literalinclude} ../example_java/extend/stream/DStreamFilter.java
:language: Java
:linenos: true
```

#### limit

返回由此流的元素组成的流，截短长度不能超过 maxSize 。

```{literalinclude} ../example_java/extend/stream/DStream.java
:language: Java
:linenos: true
```

#### distinct

返回由该流的不同元素（根据 Object.equals(Object) ）组成的流。

```{literalinclude} ../example_java/extend/stream/DStreamDistinct.java
:language: Java
:linenos: true
```

#### map

返回由给定函数应用于此流的元素的结果组成的流。

map 方法用于映射每个元素到对应的结果，以下代码片段使用 map 输出了元素对应的平方数：

```{literalinclude} ../example_java/extend/stream/DStreamMap.java
:language: Java
:linenos: true
```

```guess
9
4
49
25
```

#### sorted

sorted 方法用于对流进行排序

```{literalinclude} ../example_java/extend/stream/DStreamSorted.java
:language: Java
:linenos: true
```

```guess
4
9
25
49
```

### 终止操作

终端操作会从流的流水线生成结果。其结果可以是任何不是流的值，例如：List、Integer，甚至是void 。

| 方法                   | 描述                                               |
| -------------------- | ------------------------------------------------ |
| forEach(Consumer c)  | 内部迭代                                             |
| collect(Collector c) | 将流转换为其他形式。接收一个 Collector接口的实现，用于给Stream中元素做汇总的方法 |
| max(Comparator c)    | 返回流中最大值                                          |
| min(Comparator c)    | 返回流中最小值                                          |
| count()              | 返回流中元素总数                                         |

#### forEach

Stream 提供了新的方法 'forEach' 来迭代流中的每个数据。

```{literalinclude} ../example_java/extend/stream/DStream.java
:language: Java
:linenos: true
```

输出结果不确定，但是其结果一定是10个整数随机数。

#### 并行（parallel）程序

parallelStream 是流并行处理程序的代替方法。

```{literalinclude} ../example_java/extend/stream/DStreamParallel.java
:language: Java
:linenos: true
```

:::{attention}
运行后我们可知道， parallelStream 是不适合排序处理的，但是，他的运行速度比串行处理快。
:::

#### Collectors

Collectors 类实现了很多归约操作，例如将流转换成集合和聚合元素。Collectors 可用于返回列表或字符串；

```{literalinclude} ../example_java/extend/stream/DStreamCollectors.java
:language: Java
:linenos: true
```

```guess
筛选列表: [abc, bc, efg, abcd, jkl]
合并字符串: abc, bc, efg, abcd, jkl
```

#### 统计

一些产生统计结果的收集器也非常有用。它们主要用于int、double、long等基本类型上，它们可以用来产生类似如下的统计结果。

```{literalinclude} ../example_java/extend/stream/DStreamStatistics.java
:language: Java
:linenos: true
```

```guess
列表中最大的数 : 7
列表中最小的数 : 2
所有数之和 : 25
平均数 : 3.5714285714285716
```

#### count

返回此流中的元素数。

```{literalinclude} ../example_java/extend/stream/DStreamFilter.java
:language: Java
:linenos: true
```

#### 比较

`max(Comparator<? super T> comparator)`
根据提供的 Comparator返回此流的最大元素。

`Optional<T> min(Comparator<? super T> comparator)`
根据提供的 Comparator返回此流的最小元素。

#### 匹配 match

`allMatch(Predicate<? super T> predicate)`
返回此流的所有元素是否与提供的谓词匹配。

`boolean anyMatch(Predicate<? super T> predicate)`
返回此流的任何元素是否与提供的谓词匹配。

`noneMatch(Predicate<? super T> predicate)`
返回此流的元素是否与提供的谓词匹配。

______________________________________________________________________

[^id8]: 本文摘自菜鸟教程（<https://www.runoob.com/java/java8-streams.html>）
