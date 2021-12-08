============================
基本数据类型及其封装类
============================

.. _java-basic-datatype-and-class:

Java语言提供了八种基本类型。六种数字类型（四个整数型，两个浮点型），一种字符类型，还有一种布尔型。

在 Java 中，每个基本数据类型都有其对应的封装类。在此篇章中，将学习 Java 的基本数据类型和它们对应的分装类。

+------------+---------+------+----------------+-------+---------+--------+------------+------------+------+
| 简单类型   | boolean | byte | char           | short | int     | long   | float      | double     | void |
+------------+---------+------+----------------+-------+---------+--------+------------+------------+------+
| 二进制位数 | 1       | 8    | 16             | 16    | 32      | 64     | 32         | 64         | --   |
+------------+---------+------+----------------+-------+---------+--------+------------+------------+------+
| 封装器类   | Boolean | Byte | Character      | Short | Integer | Long   | Float      | Double     | Void |
+------------+---------+------+----------------+-------+---------+--------+------------+------------+------+
| 类中默认值 | false   | 0    | ' ' (ASCII为0) | 0     | 0       | 0 (0L) | 0.0 (0.0f) | 0.0 (0.0d) | --   |
+------------+---------+------+----------------+-------+---------+--------+------------+------------+------+

对于 Java 数据类型的详细讲解 :ref:`点击前往笔记 <java-basic-datatypes>` ；表中的默认值为在类中定义使用时的默认值。

.. code-block:: java
   :caption: Java 基本类型在类中默认值 的测试类

   public class BaseTest {
      private boolean aBoolean;
      private byte aByte;
      private char aChar;
      private int anInt;
      private short aShort;
      private long aLong;
      private float aFloat;
      private double aDouble;

      @Override
      public String toString() {
         return "BaseTest{" +
                  "aBoolean=" + aBoolean +
                  ", aByte=" + aByte +
                  ", aChar=" + aChar +
                  ", anInt=" + anInt +
                  ", aShort=" + aShort +
                  ", aLong=" + aLong +
                  ", aFloat=" + aFloat +
                  ", aDouble=" + aDouble +
                  '}';
      }

      // Getters and Setters
   
      public static void main(String[] args) {
         BaseTest baseTest=new BaseTest();
         System.out.println(baseTest);
         System.out.println((int)baseTest.getaChar());
      }
   }


|75|

boolean and Boolean
========================

boolean
----------------

boolean数据类型表示一位的信息，只有两个取值：true 和 false。 

|30|

Boolean类
--------------

Boolean 将对象中的基元类型boolean的值进行包装。 类型为 Boolean 的对象包含一个单一字段，其类型为 boolean 。 此外，该类还提供了许多将 boolean 转换为 String 和 String 转换为 boolean ，以及在处理 boolean 时有用的其他常量和方法。

首先来看看定义：

.. code-block:: java
   :caption: Boolean类定义

   public final class Boolean 
      extends Object 
      implements Serializable, Comparable<Boolean>

可以看到，Boolean 实现了序列化和比较接口，说明一个 Boolean 对象是可以序列化的；是可以比较大小的；另外，注意 final 修饰符，Boolean 不可被继承。


构造函数：
   * Boolean(boolean value) :
      分配一个 Boolean对象，代表 value参数。
      
      **很少使用这个构造函数。 除非需要新的实例，静态工厂valueOf(boolean)通常是一个更好的选择。 它可能产生明显更好的空间和时间性能。**

   * public static Boolean valueOf(boolean b) :
      返回一个Boolean指定的boolean值的Boolean实例。 
      
      如果指定的boolean值为true ，此方法返回Boolean.TRUE ; 
      如果是false ，此方法返回Boolean.FALSE 。
      如果不需要新的Boolean实例，则该方法通常优先于构造函数Boolean(boolean)使用 ，因为该方法可能会产生明显更好的空间和时间性能。 

   * Boolean(String s):
      如果字符串参数不为空并且等于(忽略大小写)字符串"true"，则分配一个 Boolean 对象，表示值为 true ，否则返回 false。

   * public static Boolean valueOf(String s):
      返回一个布尔值，其值由指定的字符串表示。如果字符串参数不为空并且等于(忽略大小写)字符串"true"，则返回的布尔值表示为真值。否则，返回一个假值，包括null参数。 例子： 
      
      new Boolean("True")生成一个Boolean对象，代表true 。 
      new Boolean("yes")生成一个Boolean对象，代表false 。 


Boolean 类的其他几个比较重要的方法：
   * boolean Boolean.parseBoolean(String string)
      将字符串参数解析为布尔值。返回的布尔值表示，如果字符串参数不为空，并且与字符串"true"相等(忽略大小写)，则为true。否则，返回一个假值，包括null参数。

   * boolean Boolean.getBoolean(String name)
      当且仅当由参数命名的系统属性存在且等于(忽略大小写)字符串"true"时返回true。(系统属性可以通过system类定义的方法getProperty来访问。如果没有指定名称的属性，或者指定的名称为空或空，则返回false。)

   * String Boolean.toString(Boolean boolean)
      返回一个表示指定布尔值的String对象。如果指定的布尔值为true，则返回字符串"true"，否则返回字符串"false"。

.. code-block:: Java
   :caption: 示例代码

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

.. code-block:: guess
   :caption: 运行结果

   信息: aBoolean is true and aBoolean2 is true; aBoolean3 is false



|50|


byte and Byte
==================


byte
--------------

byte 数据类型是8位（1*8bit）、有符号的，以二进制补码表示的整数；取值范围：-128~127 。

|30|

Byte类
---------


Byte类在一个对象中包含一个基本类型byte的值。 类型为Byte的对象包含一个单一字段，其类型为byte 。 此外，该类还提供了一些将byte转换为String和String转换为byte ，以及在处理byte时有用的其他常量和方法。

Byte 类的定义：

.. code-block:: java
   :caption: Byte类定义

   public final class Byte
      extends Number
      implements Comparable<Byte>

构造方法：
   * Byte(byte value) 
      构造一个新分配的 Byte对象，该对象表示指定的 byte值。 
    
   * Byte(String s)  
      **Deprecated** 构造一个新分配 Byte对象，表示 byte由指示值 String参数。  

      *使用 Byte.parseByte(String) 将字符串转换为字节原语，或使用 Byte.valueOf(String) 将字符串转换为byte对象。*

.. important:: 

   需要注意的是，通过 Byte 对象将字符串转化为 byte 类型的方法，其允许的字符串被限定为 -128~127

|50|

char and Character
====================


char
--------------

char 类型原本用于表示单个字符。不过，现在情况已经有所变化。 如今，有些 Unicode 字符可以用一个 char 值描述，另外一些 Unicode 字符则需要两个 char 值。这点在 :ref:` Java 中 char 和 String 的细节和使用注意 <not-using-char>` 中有说明。

|30|

Character
----------------

.. code-block:: java
   :caption: Character 类定义

   public final class Character
      extends Object
      implements Serializable, Comparable<Character>

.. note:: 

   因为笔者从未直接使用过 Character 类所以暂时不详细记录对象。

|50|

int and Integer
==================

int
----------

int数据类型是32位有符号Java原语数据类型。

int数据类型的变量需要32位(4*8bit)内存。

其有效范围为-2,147,483,648至2,147,483,647（-231至231 - 1）。

|30|

Integer
------------

Integer类的一个对象中包含一个基本类型int的值。 类型为Integer的对象包含一个单一字段，其类型为int 。 此外，该类还提供了一些将int转换为String和String转换为int ，以及在处理int时有用的其他常量和方法。


.. code-block:: java
   :caption: Integer 类定义

   public final class Integer
      extends Number
      implements Comparable<Integer>

构造方法：
   * Integer(int value) 
      构造一个新分配的 Integer对象，该对象表示指定的 int值。  

   * Integer(String s) 
      构造一个新分配 Integer对象，表示 int由指示值 String参数。  

比较重要的方法：
   * static int compare(int x, int y) 
      比较两个 int数字值。  

   * int compareTo(Integer anotherInteger) 
      数字比较两个 Integer对象。  
      
   * static int compareUnsigned(int x, int y) 
      比较两个 int值，以数值方式将值视为无符号。  


|50|

short and Short
==================

short
--------

short 数据类型是 16 位 （2*8bit）、有符号的以二进制补码表示的整数。最小值是 -32768（-2^15）；最大值是 32767（2^15 - 1）；

Short
------------

Short类在一个对象中包含一个基本类型short的值。 类型为Short的对象包含一个类型为short的单个字段。 

.. code-block:: java
   :caption: Short 类的定义

   public final class Short
      extends Number
      implements Comparable<Short>

构造函数
   * Short(short value) 
      构造一个新分配的 Short对象，表示指定的 short值。  

   * Short(String s) 
      构造一个新分配 Short对象，表示 short由指示值 String参数。  

.. note:: 
   
   由于 Short 类实现了 Comparable<Short> 接口，所以该类中有 compareTo 方法，同理其他封装类如果实现了 Comparable 接口，那么也有 compareTo 方法，同时，这些类通常有对应的基础类型的静态的比较方法。

|50|

long and Long
================

long
---------

long 数据类型是 64 位、有符号的以二进制补码表示的整数；

最小值是 -9,223,372,036,854,775,808（-2^63）；
最大值是 9,223,372,036,854,775,807（2^63 -1）；

|30|

Long
-----------

Long类在一个对象中包含一个基本类型long的值。 类型为Long的对象包含一个单一字段，其类型为long。 

.. code-block:: java
   :caption: Long 类的定义

   public final class Long
      extends Number
      implements Comparable<Long>

构造函数
   * Long(long value) 
      构造一个新分配的 Long 对象，代表指定的 long 参数。  
   
   * Long(String s) 
      构造一个新分配 Long 对象，表示 long 由指示值 String 参数。 


|50|


float and Float
================

float
----------

float 数据类型是单精度、32位、符合IEEE 754标准的浮点数；
float 在储存大型浮点数组的时候可节省内存空间；

|30|

Float
-----------

Float类在一个对象中包含一个基本类型float的值。 类型为Float的对象包含一个单一字段，其类型为float 。 

.. code-block:: java
   :caption: Float 类的定义

   public final class Float
      extends Number
      implements Comparable<Float>


构造函数
   * Float(double value) 
      构造一个新分配 Float对象，它表示转换为类型参数 float 。  

   * Float(float value) 
      构造一个新分配的 Float对象，该对象表示基元 float参数。  

   * Float(String s) 
      构造一个新分配 Float对象，它表示类型的浮点值 float用字符串表示。  


|50|

double and Double
=======================

double
------------

double 数据类型是双精度、64 位、符合 IEEE 754 标准的浮点数；

浮点数的默认类型为 double 类型；

Double
--------------

Double 类在一个对象中包含一个基本类型double的值。 类型为 Double 的对象包含一个单一字段，其类型为 double 。

.. code-block:: java
   :caption: Double 类的定义

   public final class Double
      extends Number
      implements Comparable<Double>


构造函数
   * Double(double value) 
      构造一个新分配的 Double对象，表示原始 double参数。  
   * Double(String s) 
      构造一个新分配 Double对象，它表示类型的浮点值 double用字符串表示。  

