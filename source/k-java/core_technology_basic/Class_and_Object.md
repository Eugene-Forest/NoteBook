# 类与对象

:::{tip}
一个对象变量并没有实际包含一个对象，而仅仅是引用一个对象。在 Java 中，任何对象变量的值都是存储在另一个地方的一个对象的引用。通过 new 操作符返回的值也是一个引用。
:::

构造器总是伴随着 new 操作符的执行被调用，而不能对一个已经存在的对象调用构造器来达到重新设置实例域的目的。

构造器是与类同名的没有返回值的方法，每个类可以有一个或者多个构造器，构造器可以有零个、一个或者多个参数。

```java
class Something {

   private String message = null;
   ...

   Something(){}

   Something(String message){
      this.message = message;
   }

   ...

}
```

## 封装

一般来说，对于一个类的私有变量，在该类的外部是不能直接访问的，只能通过该类提供的域访问器（即setter adn getter）或者其他公共方法来对私有变量进行操作。

封装的最简单的实现方法：

- 将类的数据域设置为私有 （必不可少）
- 公有的域访问器方法
- 公有的域更改器方法

:::{note}

需要注意的是，对于公有的域访问器方法和公有的域更改器方法，不要编写返回引用可变对象的访问器/更改器方法。如果需要返回一个可变对象的引用， 应该首先对它进行克隆（clone )。对象 clone 是指存放在另一个位置上的对象副本。

```java
class Something{
   ...
   public Date getDate(){
      return (Date) date.clone();
   }
   ...
}
```

:::

## 基于类的访问权限

由前面可知，方法可以访问所调用对象的私有数据。 **一个方法可以访问所属类的所有对象的私有数据。**

```java
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
```

```java
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
```

```guess
eugene
forest
eugene
Be setting by other object
```

**在JAVA中有四种访问控制权限，分别为：private, default, protected, public**。

* 如果一个成员方法或变量名前没有使用任何访问控制符，就为default。默认的访问控制成员可以被这个包中的其它类访问


|                                                   | private | default | protected | public |
| :-----------------------------------------------: | :-----: | :-----: | :-------: | :----: |
|                只用本类内部可访问                 |    √    |    √    |     √     |   √    |
| 同一包中的类（包括子类，以及以以[对象.成员]访问） |         |    √    |     √     |   √    |
|                其它包中的子类内部                 |         |         |     √     |   √    |
|    其它包中的类（[对象.成员]访问， 不是子类）     |         |         |           |   √    |


```{note}

需要注意的是，对于 Java 类，访问权限只有同包内使用（无访问权限修饰符）或其他包中的类可使用（public）两种情况。

```


## 静态域和静态方法

如果将域定义为 static, 每个类中只有一个这样的域。而每一个对象对于所有的实例域却都有自己的一份拷贝。

类的静态域又称为 **类域**。当类没有实例化时，不存在对象域，但是却存在类域。所有该类的实例化对象都共享一个类域，而其对象域是相互独立的。

静态方法是不能对对象实时操作的方法，（可以认为静态方法是没有隐式参数this的方法）。静态方法不能访问对象域，而只能访问静态域。普通方法则对象域、静态域都可以访问。

## 方法参数

很多程序设计语言（特别是， C++ 和 Pascal) 提供了两种参数传递的方式：值调用和引用调用。有些程序员认为 Java 程序设计语言对对象采用的是引用调用，实际上， 这种理解是不对的。

```java
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
```

```guess
eugene
forest
forest
eugene
eugene
forest
```

通过以上实例，我们发现传入swap方法的两个对象参数都是拷贝引用。

:::{note}

C++ 有 值调用 和 引用调用。引用参数标有 & 符号。`void swap(Something& x, Something& y)` 方法可实现修改。
:::

## 类设计技巧

1. 一定要保证数据私有
2. 一定要对数据初始化
3. 不要再类中使用过多的基本类型 \*
4. 不是所有的域都需要独立的域访问器和域更改器
5. 将职能过多的类进行分解
6. 类名和方法名要能体现它们的职责
7. 优先使用不可变的类 \*

对于第三点， **不要再类中使用过多的基本类型**，例子如下：

假设一个描述个人信息的类中包含以下用来表示地址字段：

```java
private String street;
private String city;
private String state;
private String zip;
```

那么显然自定义包含这四个字段的一个地址类来代替它们会明了地多。

:::{tip}
**优先使用不可变的类**,在设计类时，最好考虑该类是否可变（即判断类的字段初始化后有没有必要再次变化），如果一个类被设计为 immutable 。那么说明该类是线程安全类。线程安全的类可以省去许多麻烦，而且在某些情况下可以提高程序运行效率。
:::

(abstract-class)=

## 抽象类 [^id11]

抽象类除了不能实例化对象之外，类的其它功能依然存在，成员变量、成员方法和构造方法的访问方式和普通类一样。

由于抽象类不能实例化对象，所以抽象类必须被继承，才能被使用。

在 Java 中抽象类表示的是一种继承关系，一个类只能继承一个抽象类，而一个类却可以实现多个接口。

*如果你想设计这样一个类，该类包含一个特别的成员方法，该方法的具体实现由它的子类确定，那么你可以在父类中声明该方法为抽象方法。*

Abstract 关键字同样可以用来声明抽象方法，抽象方法只包含一个方法名，而没有方法体。

```{code-block} java
:caption: "抽象类和抽象方法"

public abstract class Employee
{
   private String name;
   private String address;
   private int number;

   public abstract double computePay();

   //其余代码
}
```

:::{note}

声明抽象方法会造成以下两个结果：

- 如果一个类包含抽象方法，那么该类必须是抽象类。
- 任何子类必须重写父类的抽象方法，或者声明自身为抽象类。
:::

:::{tip}

1. 抽象类不能被实例化(初学者很容易犯的错)，如果被实例化，就会报错，编译无法通过。
2. 抽象类中不一定包含抽象方法，但是有抽象方法的类必定是抽象类。
3. 抽象类中的抽象方法只是声明，不包含方法体，就是不给出方法的具体实现也就是方法的具体功能。
4. 构造方法，类方法（用 static 修饰的方法）不能声明为抽象方法。
5. 抽象类的子类必须给出抽象类中的抽象方法的具体实现，除非该子类也是抽象类。
:::

## 内部类 [^id12]

内部类（ inner class ) 机制。理论上讲，内部类有些复杂， 内部类定义在另外一个类的内部， 其中的方法可以访问包含它们的外部类的域。内部类技术主要用于设计具有相互协作关系的类集合。

Java 一个类中可以嵌套另外一个类，语法格式如下：

```{code-block} java
:caption: inner class

class OuterClass {   // 外部类
   // ...
   class NestedClass { // 嵌套类，或称为内部类
      // ...
   }
}
```

:::{warning}
因为笔者暂时未使用到内部类（使用到的基本上是匿名内部类），所以暂时将内部类的笔记记录搁置。如果想要查看相关笔记，可以 [点击前往笔者推荐的博客文章—— Java内部类详解](https://www.cnblogs.com/dolphin0520/p/3811445.html)
:::

[^id11]: 文章引用自菜鸟教程——抽象类； [抽象类](https://www.runoob.com/java/java-abstraction.html)

[^id12]: 文章引用博客园——Java内部类详解； [Java内部类详解](https://www.cnblogs.com/dolphin0520/p/3811445.html)
