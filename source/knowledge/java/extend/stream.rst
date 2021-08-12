=====================
Java 8 Stream [#]_
=====================

Java 8 API 添加了一个新的抽象称为 流Stream，可以让你以一种声明的方式处理数据。

Stream 使用一种类似用 SQL 语句从数据库查询数据的直观方式来提供一种对 Java 集合运算和表达的高阶抽象。

Stream API 可以极大提高 Java 程序员的生产力，让程序员写出高效率、干净、简洁的代码。

这种风格将要处理的 **元素集合看作一种流** ， 流在管道中传输（ *即数据在管道中传输* ）， 并且可以在管道的节点上进行处理， 比如筛选， 排序，聚合等。

元素流在管道中经过中间操作（intermediate operation）的处理，最后由最终操作(terminal operation)得到前面处理的结果。


.. code-block:: word

   +--------------------+       +------+   +------+   +---+   +-------+
   | stream of elements +-----> |filter+-> |sorted+-> |map+-> |collect|
   +--------------------+       +------+   +------+   +---+   +-------+

转化为可供参考的代码如下所示：

.. code-block:: Java

   List<Integer> transactionsIds = 
   widgets.stream()
               .filter(b -> b.getColor() == RED)
               .sorted((x,y) -> x.getWeight() - y.getWeight())
               .mapToInt(Widget::getWeight)
               .sum();

.. _java-stream:


什么是 stream ?
=====================

Stream（流） **是一个来自数据源的元素队列** 并支持聚合操作。

**数据源** 流的来源。 可以是集合，数组，I/O channel， 产生器generator 等

**聚合操作** 类似SQL语句一样的操作， 比如filter, map, reduce, find, match, sorted等。


和以前的 Collection 操作不同， Stream 操作还有两个基础的特征：

1) Pipelining: 中间操作都会返回流对象本身。 这样多个操作可以串联成一个管道， 如同流式风格（fluent style）。 这样做可以对操作进行优化， 比如延迟执行(laziness)和短路( short-circuiting)。

2) 内部迭代： 以前对集合遍历都是通过Iterator或者For-Each的方式, 显式的在集合外部进行迭代， 这叫做外部迭代。 Stream提供了内部迭代的方式， 通过访问者模式(Visitor)实现。



生成流
========

在 Java 8 中, 集合接口有两个方法来生成流：

1) **stream()** − 为集合创建 *串行流*。

2) **parallelStream()** − 为集合创建 *并行流*。


聚合操作
===========

------------
中间操作
------------


多个中间操作可以连接起来形成一个流水线，除非流水线上触发终止操作，否则中间操作不会执行任何的处理！而在终止操作时一次性全部处理，称为“惰性求值”


+
|方法|	描述|
+=
|filter(Predicate p)	|接收 Lambda ， 从流中排除某些元素。|
-+
|distinct()|	筛选，通过流所生成元素的 hashCode() 和 equals() 去|
-+
|limit(long maxSize)	|截断流，使其元素不超过给定数量。|
-+
|map(Function f)|	接收一个函数作为参数，该函数会被应用到每个元素上，并将其映射成一个新的元素。|
-+
|flatMap(Function f)|	接收一个函数作为参数，将流中的每个值都换成另一个流，然后把所有流连接成一个流|
-+
|sorted(Comparator comp)	|产生一个新流，其中按比较器顺序排序|
-+
|sorted()|	产生一个新流，其中按自然顺序排序|
+


filter
---------


.. literalinclude:: ../example_java/extend/stream/DStreamFilter.java
   :language: Java
   :linenos:


limit
-------------

.. literalinclude:: ../example_java/extend/stream/DStream.java
   :language: Java
   :linenos:


----------
终止操作
----------

终端操作会从流的流水线生成结果。其结果可以是任何不是流的值，例如：List、Integer，甚至是void 。


+
|方法|	描述|
+=
|forEach(Consumer c)|	内部迭代|
-+
|collect(Collector c)|	将流转换为其他形式。接收一个 Collector接口的实现，用于给Stream中元素做汇总的方法|
-+
|max(Comparator c)	|返回流中最大值|
-+
|min(Comparator c)|	返回流中最小值|
-+
|count()|	返回流中元素总数|
+

forEach
-----------

.. literalinclude:: ../example_java/extend/stream/DStream.java
   :language: Java
   :linenos:

输出结果不确定，但是其结果一定是10个整数随机数。


map
--------------



sorted
------------


并行（parallel）程序
-----------------------



Collectors
---------------



统计
------------

----


.. [#] 本文摘自菜鸟教程（https://www.runoob.com/java/java8-streams.html）