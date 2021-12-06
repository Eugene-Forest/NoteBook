=================================
继承
=================================

关键字 extends 表明正在构造的新类派生于一个已存在的类。 已存在的类称为超类( super class)、 基类（ base class) 或父类（parent class); 新类称为子类（subclass、) 派生类( derived class) 或孩子类（child class)。 超类和子类是 Java 程序员最常用的两个术语。

前缀“ 超” 和“ 子” 来源于计算机科学和数学理论中的集合语言的术语。所有雇员组成的集合包含所有经理组成的集合。可以这样说， 雇员集合是经理集合的超集， 也可以说，经理集合是雇员集合的子集。

**一个子类只能继承一个超类，而一个子类可以实现多个接口。**

|75|

继承设计的技巧
======================================


1. 将公共操作和域放在超类

   * 这就是为什么将姓名域放在 Person类中，而没有将它放在 Employee 和 Student 类中的原因

2. 不要使用受保护的域

   * protected 机制并不能够带来更好的保护，某个类的子类和或与其同一个包中的所有类都可以访问它 proteced 域，这样会破坏类的封装性。

3. 使用继承实现 “is-a” 关系

   * 教师和人属于 is-a 关系，所以 Teacher 可以继承 Person ; 而学生和教师不属于 is-a 关系，所以不可继承。

4. 除非所有继承的方法都有意义，否则不要使用继承

   * 并非所有类都适合作为超类被继承，假如继承一个类会使得其子类封装性出现问题，那么就不要使用该类作为其“子类”的超类。

5. 在覆盖方法时，不要改变预期的行为

   * 关键在于， 在覆盖/重写子类中的方法时，不要偏离最初的设计想法

6. 使用多态， 而非类型信息

    .. code-block:: java
        
        if (x is of type 1)
            action1();
        else if (x is of type 2)
            action2();
        /*
        * 对于以上这种情况都应当考虑使用多态。最终简化为 x.action()，
        * 以便使用多态性提供的动态分派机制执行相应的动作。
        */

7. 不要过多地使用 反射

   * 反射机制使得人们可以通过在运行时查看域和方法， 让人们编写出更具有通用性的程序。这种功能对于编写系统程序来说极其实用，但是通常不适于编写应用程序。反射是很脆弱的，即编译器很难帮助人们发现程序中的错误， 因此只有在运行时才发现错误并导致异常。




|50|

instanceof 关键字 [#]_
===========================

严格来说 ``instanceof`` 是 Java 中的一个双目运算符，由于它是由字母组成的，所以也是 Java 的保留关键字。在 Java 中可以使用 ``instanceof`` 关键字判断一个对象是否为一个类（或接口、抽象类、父类）的实例。语法格式如下所示:

``boolean result = obj instanceof Class``

其中，obj 是一个对象，Class 表示一个类或接口。obj 是 class 类（或接口）的实例或者子类实例时，结果 result 返回 true，否则返回 false。

Java instanceof 关键字的几种用法：

* 声明一个 class 类的对象，判断 obj 是否为 class 类的实例对象

.. code-block:: java

    Integer integer = new Integer(1);
    System.out.println(integer instanceof  Integer);    // true

* 声明一个 class 接口实现类的对象 obj，判断 obj 是否为 class 接口实现类的实例对象

.. code-block:: java

    ArrayList arrayList = new ArrayList();
    System.out.println(arrayList instanceof List);    // true


* obj 是 class 类的直接或间接子类

.. code-block:: java

    Integer integer = new Integer(1);
    System.out.println(integer instanceof Number);    // true
    System.out.println(integer instanceof Object);    // true


.. warning:: 

    对于 ``obj instanceof class`` :
    
    obj 的类型必须是引用类型或空类型，否则会编译错误。class 只能是类或者接口，当其为 null 时，会发生编译错误。

|30|

三目运算
---------------

instanceof 也经常和三目（条件）运算符一起使用，代码如下：

``A instanceof B ? A : C``

.. code-block:: java

    public class Test {
        public Object animalCall(Animal a) {
            String tip = "这个动物不是牛！";
            // 判断参数a是不是Cow的对象
            return a instanceof Cow ? (Cow) a : tip;
        }

        public static void main(String[] args) {
            Sheep sh = new Sheep();
            Test test = new Test();
            System.out.println(test.animalCall(sh));
        }
    }

    class Animal {

    }

    class Cow extends Animal {

    }

    class Sheep extends Animal {

    }



|50|

Object： 所有类的超类
===========================

Object 类是 Java 中所有类的始祖， 在 Java 中每个类都是由它扩展而来的。但是并不需要这样写：

.. code-block:: java

    public class Employee extends Object


如果没有明确地指出超类，Object 就被认为是这个类的超类。故而可以使用 Object 类型的变量引用任何类型的对象：

.. code-block:: java

    Object obj = new Employee(Harry Hacker", 35000);


由于在 Java中，每个类都是由 Object 类扩展而来的，所以， 熟悉这个类提供的所有服务十分重要。


在 Java 中，只有基本类型(primitive types) 不是对象， 例如，数值、 字符和布尔类型的值都不是对象。所有的数组类型，不管是对象数组还是基本类型的数组都扩展了 Object 类。

|30|

equal() 
---------------

Object 类中的 equals 方法用于检测一个对象是否等于另外一个对象。在 Object 类中，这个方法将判断两个对象是否具有相同的引用。如果两个对象具有相同的引用， 它们一定是相等的。然而，对于多数类来说， 这种判断并没有什么意义。

例如， 如果两个雇员对象的 ID 一样， 就认为它们是相等的（利用下面这个示例演示 equals 方法的实现机制）:

.. sidebar:: 编写一个完美的 equals 方法的建议

    1) 显式参数命名为 otherObject, 稍后需要将它转换成另一个叫做 other 的变量
    2) 检测 this 与 otherObject 是否引用同一个对象
    3) 检测 otherObject 是否为 null, 如果为 null, 返回 false。
    4) \* 比较 this 与 otherObject 是否属于同一个类。如果 equals 的语义在每个子类中有所改变，就使用 getClass 检测 ；如果所有的子类都拥有统一的语义，就使用 instanceof 检测；
    5) 将 otherObject 转换为相应的类类型变量
    6) 现在开始对所有需要比较的域进行比较了。使用 == 比较基本类型域，使用 equals 比较对象域。如果所有的域都匹配， 就返回 true; 否则返回 false


.. literalinclude:: ../example_java/basic/inherit/EmployeeTemp.java
    :language: java

对于如何实现 ``equals`` ，可以从两个截然不同的情况看一下这个问题：

* 如果子类能够拥有自己的相等概念， 则对称性需求将强制采用 getClass 进行检测 【因为要确定比较双方是否为同一个类】
* 如果由超类决定相等的概念，那么就可以使用 ``instanceof`` 进行检测， 这样可以在不同子类的对象之间进行相等的比较。【因为需要判断比较对象是否属于超类的实例或其子类对象】

.. attention:: 

    Java 语言规范要求 ``equals`` 方法具有下面的特性:
    
    * 自反性：对于任何非空引用 x, ``x.equals(x)`` 应该返回 true
    * 对称性: 对于任何引用 x 和 y, 当且仅当 ``y.equals(x)`` 返回 true , ``x.equals(y)`` 也应该返回 true
    * 传递性： 对于任何引用 x、 y 和 z, 如果 ``x.equals(y)`` 返回 true， ``y.equals(z)`` 返回 true, ``x.equals(z)`` 也应该返回 true
    * 一致性： 如果 x 和 y 引用的对象没有发生变化，反复调用 ``x.equals(y)`` 应该返回同样的结果
    * 对于任意非空引用 x, ``x.equals(null)`` 应该返回 false

|15|

有特殊要求的对象比较：

Employee 作为基类，Manager 继承 Employee；Staff 类比较时使用 Employee 。（需要注意的是，Staff 类的 equals 实现是不符合 Java 语言规范的） 

以下为类源码：

* :download:`Employee.java <../example_java/basic/inherit/Employee.java>` 
* :download:`Manager.java <../example_java/basic/inherit/Manager.java>`
* :download:`Staff.java <../example_java/basic/inherit/Staff.java>` 

.. literalinclude:: ../example_java/basic/inherit/Main.java
    :language: java

|30|

hashCode 方法
---------------------


散列码（ hash code ） 是由对象导出的一个整型值。散列码是没有规律的。如果 x 和 y 是两个不同的对象， x.hashCode( ) 与 y.hashCode( ) 基本上不会相同。

由于 hashCode方法定义在 Object 类中， 因此每个对象都有一个默认的散列码，其值为对象的存储地址。

Equals 与 hashCode 的定义必须一致：如果 x.equals(y) 返回 true, 那么 x.hashCode( ) 就必须与 y.hashCode( ) 具有相同的值。

.. code-block:: java

    //hashCode 实现样例
    @Override
    public int hashCode() {
        return Objects.hash(id, name, salary, hireDay);
    }

|30|

toString()
------------------------

在 Object 中还有一个重要的方法， 就是 ``toString`` 方法， 它用于返回表示对象值的字符串。


绝大多数（但不是全部）的 toString方法都遵循这样的格式：类的名字，随后是一对括号括起来的域值。下面是 Employee 类中的 toString 方法的实现：

.. code-block:: java

    @Override
    public String toString() {
        return "Staff{" +
                "id='" + id + '\'' +
                ", name='" + name + '\'' +
                ", salary=" + salary +
                ", hireDay=" + hireDay +
                '}';
    }

Object 类定义了 toString 方法， 用来打印输出对象所属的类名和散列码（hashCode）。例如， 调用 ``System.out.println(System.out);`` 将输出内容 *java.io.PrintStream@74a14482*，之所以得到这样的结果是因为 PrintStream 类的设计者没有覆盖 toString 方法。





----

.. [#] Java instanceof 关键字详解 : http://c.biancheng.net/view/6346.html