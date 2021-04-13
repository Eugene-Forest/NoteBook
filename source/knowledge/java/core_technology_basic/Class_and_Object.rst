================
类与对象
================

.. tip:: 

   一个对象变量并没有实际包含一个对象，而仅仅是引用一个对象。在 Java 中，任何对象变量的值都是存储在另一个地方的一个对象的引用。通过 new 操作符返回的值也是一个引用。

构造器总是伴随着 new 操作符的执行被调用，而不能对一个已经存在的对象调用构造器来达到重新设置实例域的目的。

构造器是与类同名的没有返回值的方法，每个类可以有一个或者多个构造器，构造器可以有零个、一个或者多个参数。

.. code-block:: java

   class Something {

      private String message = null;
      ...

      Something(){}

      Something(String message){
         this.message = message;
      }

      ...

   }

封装
======

一般来说，对于一个类的私有变量，在该类的外部是不能直接访问的，只能通过该类提供的域访问器（即setter adn getter）或者其他公共方法来对私有变量进行操作。

封装的最简单的实现方法：

* 将类的数据域设置为私有 （必不可少）
* 公有的域访问器方法
* 公有的域更改器方法

.. note:: 

   需要注意的是，对于公有的域访问器方法和公有的域更改器方法，不要编写返回引用可变对象的访问器/更改器方法。如果需要返回一个可变对象的引用， 应该首先对它进行克隆（clone )。对象 clone 是指存放在另一个位置上的对象副本。

   .. code-block:: java

      class Something{
         ...
         public Date getDate(){
            return (Date) date.clone();
         }
         ...
      }

基于类的访问权限
==================

由前面可知，方法可以访问所调用对象的私有数据。**一个方法可以访问所属类的所有对象的私有数据。**

.. code-block:: java

      public class Something {
         
         private String message=null;

         public String getMessage() {
            return message;
         }

         public void setMessage(String message) {
            this.message = message;
         }
         
         public void setOtherObjectMessage(Something other) {
         //该方法中，other对象直接使用私有字段而通过方法
            other.message="Be setting by other object";
         }

         public Something(String message) {
            this.message = message;
         }

      }



.. code-block:: java

   public class TestMain {
      
      public static void main(String[] args) {
         Something eugene=new Something("eugene");
         Something forest=new Something("forest");
         System.out.println(eugene.getMessage());
         System.out.println(forest.getMessage());
         eugene.setOtherObjectMessage(forest);
         System.out.println(eugene.getMessage());
         System.out.println(forest.getMessage());
      }

   }


.. code-block:: word

   eugene
   forest
   eugene
   Be setting by other object


静态域和静态方法
==================

如果将域定义为 static, 每个类中只有一个这样的域。而每一个对象对于所有的实例域却都有自己的一份拷贝。

类的静态域又称为 **类域**。当类没有实例化时，不存在对象域，但是却存在类域。所有该类的实例化对象都共享一个类域，而其对象域是相互独立的。

静态方法是不能对对象实时操作的方法，（可以认为静态方法是没有隐式参数this的方法）。静态方法不能访问对象域，而只能访问静态域。普通方法则对象域、静态域都可以访问。

方法参数
===========

很多程序设计语言（特别是， C++ 和 Pascal) 提供了两种参数传递的方式：值调用和引用调用。有些程序员认为 Java 程序设计语言对对象采用的是引用调用，实际上， 这种理解是不对的。

.. code-block:: java

   public class SwapMain {
      
      /**
      * 预期是互换参数的引用对象
      * @param before
      * @param after
      */
      public static void swap(Something before,Something after) {
         Something temp=before;
         before=after;
         after=temp;
         System.out.println(before.getMessage());
         System.out.println(after.getMessage());
      }
      
      public static void main(String[] args) {
         Something eugene=new Something("eugene");
         Something forest=new Something("forest");
         System.out.println(eugene.getMessage());
         System.out.println(forest.getMessage());
         swap(eugene, forest);
         System.out.println(eugene.getMessage());
         System.out.println(forest.getMessage());
      }
   }

.. code-block:: word

   eugene
   forest
   forest
   eugene
   eugene
   forest

通过以上实例，我们发现传入swap方法的两个对象参数都是拷贝引用。

.. note:: 

   C++ 有 值调用 和 引用调用。引用参数标有 & 符号。``void swap(Something& x, Something& y)`` 方法可实现修改。

类设计技巧
===========

#. 一定要保证数据私有
#. 一定要对数据初始化
#. 不要再类中使用过多的基本类型 \*
#. 不是所有的域都需要独立的域访问器和域更改器
#. 将职能过多的类进行分解
#. 类名和方法名要能体现它们的职责
#. 优先使用不可变的类 \*


对于第三点，**不要再类中使用过多的基本类型**，例子如下：

假设一个描述个人信息的类中包含以下用来表示地址字段：

.. code-block:: java

   private String street;
   private String city;
   private String state;
   private String zip;

那么显然自定义包含这四个字段的一个地址类来代替它们会明了地多。

.. tip:: 

   **优先使用不可变的类**,在设计类时，最好考虑该类是否可变（即判断类的字段初始化后有没有必要再次变化），如果一个类被设计为 immutable 。那么说明该类是线程安全类。线程安全的类可以省去许多麻烦，而且在某些情况下可以提高程序运行效率。
