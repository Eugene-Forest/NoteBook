# java 数据类型操作的原子性

Java编程规范定义了一些原子操作。如，char、int等 **基本类型的赋值和引用操作都是原子的**。另外。**对象的引用类型的赋值和引用操作都是原子的**。

同时，Java编程规范定义 **long、double的赋值和引用操作都不是原子的**。

数据类型是否是原子性在多线程中会有很大影响。

如：假设存在一个int类型的字段n，某个线程执行了以下赋值操作。

```java
n=123;
```

并且，相继有另外一个线程执行了下方的赋值操作。

```java
n=456;
```

那么，一般来说n的值不是123就是456 [^id2]。由于这些操作本身就是原子的，所以就算不加上 synchronized，这些操作也不会出错。但是，对于long、double类型的数据执行以上步骤，其得出的结果是不可预测的。

总结如下：

- 基本类型、引用类型的赋值和引用是原子操作
- 但是long、double的赋值和引用是非原子操作
- long或double在线程间共享时，需要将其放入synchronized中操作，或者声明为volatile。
 
[^id2]: 如果这个字段既不是volatile，也没有加上synchronized进行同步，那么其他线程有可能不会立即看到赋值结果。这种情况不是原子性的问题，而是其他线程能否看见的问题，即可见性问题。可见性问题参见java内存模型。
