# 集合 [^id4]

在实现方法时，选择不同的数据结构会导致其实现风格以及性能存在着很大差异。需要快速地搜索成千上万个（甚至上百万）有序的数据项吗？ 需要快速地在有序的序列中间插人元素或删除元素吗？ 需要建立键与值之间的关联吗？这些要求数组肯定是没有办法做到的，因为数组的缺点是一旦声明之后，长度就不可变了；同时，声明数组时的数据类型也决定了该数组存储的数据的类型；而且，数组存储的数据是有序的、可重复的，特点单一。但是集合提高了数据存储的灵活性，Java 集合不仅可以用来存储不同类型不同数量的对象，还可以保存具有映射关系的数据。

```{eval-rst}
.. csv-table:: Java 库中的具体集合(未包含线程安全集合)
    :file: ../example_java/basic/gather/gather-frame.csv
    :header-rows: 1
    :align: center
```

:::{figure} ../img/core_tech/base/gather-frame.png
:alt: 集合框架中的类

集合框架中的类
:::

我们在不处理大量或复杂数据的情况下使用较多的类应当是 ArrayList 和 HashMap 两个。

Java 集合， 也叫作容器，主要是由两大接口派生而来：一个是 Collection接口，主要用于存放单一元素；另一个是 Map 接口，主要用于存放键值对。

对于Collection 接口，下面又有三个主要的子接口：List、Set 和 Queue。

:::{figure} ../img/core_tech/base/java-collection-hierarchy.png
:alt: Java 集合

Java 集合 [^id5]
:::

List
: - `ArrayList` ： Object\[\] 数组
  - `Vector` ：Object\[\] 数组
  - `LinkedList` ： 双向链表(JDK1.6 之前为循环链表，JDK1.7 取消了循环)

Set
: - `HashSet` (无序，唯一): 基于 `HashMap` 实现的，底层采用 `HashMap` 来保存元素
  - `LinkedHashSet` : `LinkedHashSet` 是 `HashSet` 的子类，并且其内部是通过 `LinkedHashMap` 来实现的。有点类似于我们之前说的 `LinkedHashMap` 其内部是基于 `HashMap` 实现一样，不过还是有一点点区别的
  - `TreeSet` (有序，唯一): 红黑树(自平衡的排序二叉树)

Queue
: - `PriorityQueue` : Object\[\] 数组来实现二叉堆
  - `ArrayQueue` : Object\[\] 数组 + 双指针

Map
: - `HashMap` ： JDK1.8 之前 `HashMap` 由数组+链表组成的，数组是 `HashMap` 的主体，链表则是主要为了解决哈希冲突而存在的（“拉链法”解决冲突）。JDK1.8 以后在解决哈希冲突时有了较大的变化，当链表长度大于阈值（默认为 8）（将链表转换成红黑树前会判断，如果当前数组的长度小于 64，那么会选择先进行数组扩容，而不是转换为红黑树）时，将链表转化为红黑树，以减少搜索时间
  - `LinkedHashMap` ： `LinkedHashMap` 继承自 `HashMap` ，所以它的底层仍然是基于拉链式散列结构即由数组和链表或红黑树组成。另外， `LinkedHashMap` 在上面结构的基础上，增加了一条双向链表，使得上面的结构可以保持键值对的插入顺序。同时通过对链表进行相应的操作，实现了访问顺序相关逻辑。详细可以查看：《LinkedHashMap 源码详细分析（JDK1.8）》  (opens new window)
  - `Hashtable` ： 数组+链表组成的，数组是 `Hashtable` 的主体，链表则是主要为了解决哈希冲突而存在的
  - `TreeMap` ： 红黑树（自平衡的排序二叉树）

## List, Set, Queue, Map 四者的区别

> - **List** (对付顺序的好帮手): 存储的元素是有序的、可重复的。
> - **Set** (注重独一无二的性质): 存储的元素是无序的、不可重复的。
> - **Queue** (实现排队功能的叫号机): 按特定的排队规则来确定先后顺序，存储的元素是有序的、可重复的。
> - **Map** (用 key 来搜索的专家): 使用键值对（key-value）存储，类似于数学上的函数 y=f(x)，"x" 代表 key，"y" 代表 value，key 是无序的、不可重复的，value 是无序的、可重复的，每个键最多映射到一个值。

## Collection 子接口之 List

<!-- //todo java集合笔记未完待续 -->

[^id4]: 考虑到讲到 Java 集合框架就不可避免地要涉及数据结构，所以在本章节中就不对 Java 集合进行详细讲解。同时本文章参考 JavaGuide {ref}`容器 <https://javaguide.cn/home/>`

[^id5]: 图中只列举了主要的继承派生关系，并没有列举所有关系。比方省略了AbstractList, NavigableSet等抽象类以及其他的一些辅助类。
