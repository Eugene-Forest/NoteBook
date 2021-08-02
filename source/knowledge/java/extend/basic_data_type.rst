============================
基本数据类型及其封装类
============================

.. _java-basic-datatype-and-class:

Java语言提供了八种基本类型。六种数字类型（四个整数型，两个浮点型），一种字符类型，还有一种布尔型。

在 Java 中，每个基本数据类型都有其对应的封装类。在此篇章中，将学习 Java 的基本数据类型和它们对应的分装类。

对于 Java 数据类型的详细讲解 :ref:`点击前往笔记 <java-basic-datatypes>` .

boolean and Boolean
========================

boolean
----------------

boolean数据类型表示一位的信息，只有两个取值：true 和 false。 

Boolean类
--------------

Boolean 将对象中的基元类型boolean的值进行包装。 类型为 Boolean 的对象包含一个单一字段，其类型为 boolean 。 此外，该类还提供了许多将 boolean 转换为 String 和 String 转换为 boolean ，以及在处理 boolean 时有用的其他常量和方法。

首先来看看定义：

.. code-block:: java

   public final class Boolean 
      extends Object 
      implements Serializable, Comparable<Boolean>

可以看到，Boolean 实现了序列化和比较接口，说明一个 Boolean 对象是可以序列化的；是可以比较大小的；另外，注意 final 修饰符，Boolean 不可被继承。


构造函数：

   ``Boolean(boolean value)`` :
   分配一个 Boolean对象，代表 value参数。
   
   **很少使用这个构造函数。 除非需要新的实例，静态工厂valueOf(boolean)通常是一个更好的选择。 它可能产生明显更好的空间和时间性能。**

   ``public static Boolean valueOf(boolean b)``:
   返回一个Boolean指定的boolean值的Boolean实例。 
   
   如果指定的boolean值为true ，此方法返回Boolean.TRUE ; 
   如果是false ，此方法返回Boolean.FALSE 。
   如果不需要新的Boolean实例，则该方法通常优先于构造函数Boolean(boolean)使用 ，因为该方法可能会产生明显更好的空间和时间性能。 


   ``Boolean(String s)``:
   如果字符串参数不为空并且等于(忽略大小写)字符串"true"，则分配一个 Boolean 对象，表示值为 true ，否则返回 false。

   ``public static Boolean valueOf(String s)``:
   返回一个布尔值，其值由指定的字符串表示。如果字符串参数不为空并且等于(忽略大小写)字符串"true"，则返回的布尔值表示为真值。否则，返回一个假值，包括null参数。 例子： 
   
   new Boolean("True")生成一个Boolean对象，代表true 。 
   new Boolean("yes")生成一个Boolean对象，代表false 。 

示例代码：

.. code-block:: Java

   import java.util.logging.Logger;

   public class Main {
      public static void main(String[] args) {
         Logger logger = Logger.getLogger(Main.class.getName());
         Boolean aBoolean = Boolean.valueOf("true");
         Boolean aBoolean2 = Boolean.valueOf("True");
         Boolean aBoolean3 = Boolean.valueOf("other true");

         logger.info("aBoolean is " + aBoolean.toString() + " and aBoolean2 is " + aBoolean2.toString()
                  + "; aBoolean3 is " + aBoolean3.toString());
      }
   }

运行结果：

.. code-block:: word

   信息: aBoolean is true and aBoolean2 is true; aBoolean3 is false


.. attention:: 


   Boolean 类的其他几个比较重要的方法：

   ``boolean Boolean.parseBoolean(String string)``
   将字符串参数解析为布尔值。返回的布尔值表示，如果字符串参数不为空，并且与字符串"true"相等(忽略大小写)，则为true。否则，返回一个假值，包括null参数。

   ``boolean Boolean.getBoolean(String name)``
   当且仅当由参数命名的系统属性存在且等于(忽略大小写)字符串"true"时返回true。(系统属性可以通过system类定义的方法getProperty来访问。如果没有指定名称的属性，或者指定的名称为空或空，则返回false。)

   ``String Boolean.toString(Boolean boolean)``
   返回一个表示指定布尔值的String对象。如果指定的布尔值为true，则返回字符串"true"，否则返回字符串"false"。


----


byte and Byte
==================


byte
--------------

byte 数据类型是8位、有符号的，以二进制补码表示的整数；取值范围：-128~127 。

Byte类
---------


Byte类在一个对象中包含一个基本类型byte的值。 类型为Byte的对象包含一个单一字段，其类型为byte 。 此外，该类还提供了一些将byte转换为String和String转换为byte ，以及在处理byte时有用的其他常量和方法。


.. code-block:: java

   public final class Byte
      extends Number
      implements Comparable<Byte>