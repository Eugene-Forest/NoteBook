======================================
泛型程序设计（Generic programming) 
======================================

**泛型程序设计 （Generic programming) 意味着编写的代码可以被很多不同类型的对象所重用。** 例如， 我们并不希望为聚集 String 和 File 对象分别设计不同的类。实际上，也不需要这样做，因为一个 ArrayList 类可以聚集任何类型的对象。

泛型 [#]_ 的本质是参数化类型，也就是说所操作的数据类型被指定为一个参数。在表面上看来， 泛型很像 C++ 中的模板。 **使用泛型机制编写的程序代码要比那些杂乱地使用 Object 变量，然后再进行强制类型转换的代码具有更好的安全性和可读性。**

泛型类
===========

一个泛型类（ generic class) 就是具有一个或多个类型变量的类。


.. literalinclude:: ../example_java/basic/genericity/Pair.java
   :language: Java
   :linenos:
   :lines: 3-


.. tip:: 

   **类型变量** 使用大写形式，且比较短， 这是很常见的。在 Java 库中:
   
   * 使用变量 E 表示集合的元素类型， 
   * K 和 V 分别表示表的关键字与值的类型。
   * T ( 需要时还可以用临近的字母 U 和 S) 表示“ 任意类型”。

   *类型变量 ，用尖括号 ( < >) 括起来*

.. warning:: 

   区分概念：泛型类 和 类型变量 。 

   例如： 假设 T 类型变量， 那么 Pair<T> 是泛型类。

泛型方法
==============

下面这个方法是在普通类中定义的。

.. literalinclude:: ../example_java/basic/genericity/ArrayAlg.java
   :language: Java
   :linenos:
   :lines: 3-8,22-24,31-32



* 泛型方法可以定义在普通类中，也可以定义在泛型类中。
* 类型变量放在修饰符（这里是 public static) 的后面，返回类型的前面。
* 当调用一个泛型方法时，在方法名前的尖括号中放人具体的类型： ``String middle = ArrayAlg.<String>getMiddle("private", "Q", "Public");`` 在这种情况（实际也是大多数情况）下，方法调用中可以省略 <String> 类型参数。


类型变量的限定
====================

有时，类或方法需要对类型变量加以约束。


.. code-block:: java
   :linenos:

    public static <T> T min(T[] a) {
        if (a == null || a.length == 0) {
            return null;
        }
        T smallest = a[0];
        for (int i = 1; i < a.length; i++) {
            if (smallest.compareTo(a[i]) > 0) {
                smallest = a[i];
            }
        }
        return smallest;
    }


这段代码有一个问题。 变量 smallest 类型为 T, 这意味着它可以是任何一个类的对象。怎么才能确信 T 所属的类有 compareTo 方法呢？

解决这个问题的方案是将 T 限制为实现了 Comparable 接口（只含一个方法 compareTo 的标准接口）的类。可以通过对类型变量 T 设置限定（bound) 实现这一点: ``public static <T extends Comparable> T a) ...``

.. literalinclude:: ../example_java/basic/genericity/ArrayAlg.java
   :language: Java
   :linenos:
   :lines: 3-4,9-22,26-32

**一个类型变量或通配符可以有多个限定**， 例如： ``< T extends Comparable & Serializable>``

.. warning:: 

   在 C++ 中不能对模板参数的类型加以限制。如果程序员用一个不适当的类型实例化一个模板，将会在模板代码中报告一个（通常是含糊不清的）错误消息。


泛型代码和虚拟机
======================


虚拟机没有泛型类型对象—所有对象都属于普通类。


类型擦除
---------


无论何时定义一个泛型类型， 都自动提供了一个相应的原始类型 （ raw type )。原始类型的名字就是删去类型参数后的泛型类型名。擦除（ erased) 类型变量, 并替换为限定类型（无限定的变量用 Object）。

例如， Pair<T> 的原始类型如下所示: (因为 T 是一个无限定的变量， 所以直接用 Object 替换。)

.. code-block:: java

   public class Pair {
      private Object first;
      private Object second;

      public Pair() {
         first = null;
         second = null;
      }

      public Pair(Object first, Object second) {
         this.first = first;
         this.second = second;
      }

      public Object getFirst() {
         return first;
      }

      public Object getSecond() {
         return second;
      }

      public void setFirst(Object newValue) {
         first = newValue;
      }

      public void setSecond(Object newValue) {
         second = newValue;
      }
   }

.. warning:: 

   就这点而言， Java 泛型与 C++ 模板有很大的区别。C++ 中每个模板的实例化产生不同的类型，这一现象称为“ 模板代码膨账”。Java 不存在这个问题的困扰。


泛型的约束和局限性
======================

用 Java 泛型时需要考虑的一些限制。其中大多数限制都是由类型擦除引起的。


* 不能用基本类型实例化类型参数
   * 因此， 没有 Pair<double>, 只有 Pair<Double>。 当然, 其原因是类型擦除。擦除之后， Pair 类含有 Object 类型的域， 而 Object 不能存储 double。
* 运行时类型查询只适用于原始类型
   * 所有的类型查询只产生原始类型。 ``if (a instanceof Pair<T>) // Error``
* 不能创建参数化类型的数组
   * ``Pair<String>[] table = new Pair<String>[10]; // Error``
* 不能实例化类型变量
   * 不能使用像 new T(...，) new T[...] 或 T.class 这样的表达式中的类型变量。
* Varargs 警告 
   * Java 不支持泛型类型的数组
* 泛型类的静态上下文中类型变量无效
   * 不能在静态域或方法中引用类型变量。 ``private static T singlelnstance; // Error``
* 不能抛出或捕获泛型类的实例
   * 既不能抛出也不能捕获泛型类对象。实际上， 甚至泛型类扩展 Throwable 都是不合法的。 ``public class Problem<T> extends Exception { /* . . . */ } // Error can't extend Throwable``
   * catch 子句中不能使用类型变量。 ``catch (T e) // Error can 't catch type variable``
   * 不过， 在异常规范中使用类型变量是允许的。 ``public static <T extends Throwable〉void doWork(T t) throws T``
* 注意擦除后的冲突
   * 将 equals 方法添加到 Pair 类，考虑一个 Pair<String>。从概念上讲， 它有两个 equals 方法: ``boolean equals(String) // defined in Pai r<T>`` 以及 ``boolean equals(Object) // inherited from Object`` 。但是，方法擦除 ``boolean equals(String)`` 后就是 ``boolean equals(Object)`` ，与 Object.equals 方法发生冲突。当然，补救的办法是重新命名引发错误的方法。

.. note:: 

   .. code-block:: java

   Pair<String> stringPair = . .
   Pair<Employee〉employeePair = . .
   if (stringPair.getClass() == employeePair.getClass()) // they are equal
   //其比较的结果是 true, 这是因为两次调用 getClass 都将返回 Pair.class





继承规则
==============

考虑一个类和一个子类， 如 Employee 和 Manager (Manager 是 Employee 的子类)。 Pair<Manager> 是 Pair<Employee> 的一个子类吗？ 

答案是 “否”。


类型通配符
===========

通配符限定与类型变量限定。

:download:`Staff.java <../example_java/basic/genericity/Staff.java>` 

:download:`Manager.java <../example_java/basic/genericity/Manager.java>` 

.. literalinclude:: ../example_java/basic/genericity/ExtendsTest.java
   :language: Java
   :linenos:


超类型限定 
-------------

通配符限定与类型变量限定十分类似，但是，还有一个附加的能力，即可以指定一个超类型限定 （super type bound)

``? super Manager``  这个通配符限制为 Manager 的所有超类型。


----


.. [#] Java 泛型（generics）是 JDK 5 中引入的一个新特性, 泛型提供了编译时类型安全检测机制，该机制允许程序员在编译时检测到非法的类型。


