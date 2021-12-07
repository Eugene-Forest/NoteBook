==========================
函数传值与深拷贝、浅拷贝
==========================



我们在对象与对象直接协作时，一个对象常需要获得另一个对象的私有成员变量。那么另外的那个对象就需要定义一个 Getter 函数，但是需要注意的是，对于返回成员对象和数组类型的 Getter 函数，我们通常是不能也不建议直接返回成员变量的，因为这样会破坏类对象的封装性。

首先，我们需要了解在Java中哪些数据类型在函数传值的过程中是传递对象地址。

|75|

Java中的“传值”和“传引用”问题
=====================================

对于Java 函数中的参数究竟是“传值”还是“传引用”，有以下两点定论：

* 在Java中，当 :ref:`基本类型 <java-basic-datatype-and-class>`  作为参数传入方法时，无论该参数在方法内怎样被改变，外部的变量原型总是不变的，这就叫做“值传递”，即方法操作的是参数变量（也就是原型变量的一个值的拷贝）改变的也只是原型变量的一个拷贝而已，而非变量本身。所以变量原型并不会随之改变。

* 当方法传入的参数为非基本类型时（也就是说是一个对象类型的变量）， 方法里面改变参数变量的同时变量原型也会随之改变。这种特性就叫做“引用传递”，也叫做传址，即方法操作参数变量时是拷贝了变量的引用。



.. literalinclude:: ../example_java/extend/ValueMain.java
    :language: java
    :caption: String 字符串对象和基本类型的“值传递”
    :linenos: 

有人看到上面代码运行结果可能会有疑问，String 字符串对象为什么也可以实现 “值传递” ？其实这和 Java String 类的实现方式有关， 点击查看 :ref:`String 的定义 <realize-string>` 或通过 JDK 文档查看 String 的定义，我们会发现 String 类对象的值是存储在 char 类型数组中的，而且这个数组和类是由 final 修饰的，也就是说， *字符串一旦定义则不可变。*


|50|

通过实现 Cloneable 接口进行拷贝 [#]_
========================================


简单来说，在Java中，拷贝就是创建一个和已知对象一模一样的对象，而拷贝有深拷贝和浅拷贝之分。

Java 将内存空间分为堆和栈。基本类型直接在栈中存储数值，而引用类型是将引用放在栈中，实际存储的值是放在堆中，通过栈中的引用指向堆中存放的数据。

.. figure:: ../../../img/java/extend/clone.png
    
    clone


|30|

浅拷贝
-------------------

浅拷贝
    创建一个新对象，然后将当前对象的非静态字段复制到该新对象，如果字段是值类型（即是 Java 基本类型或 String 类型的）的，那么对该字段执行复制；如果该字段是引用类型的话，则复制引用但不复制引用的对象，原始对象及其副本引用同一个对象。

.. note:: 

    浅拷贝之所以称之为浅拷贝，那便是他不能彻底拷贝一个对象。通过浅拷贝获得的拷贝对象的存储仍然与源对象的存储有交叉。参考下文中的 :ref:`浅拷贝示例 <java-extend-shallow-copy-example>` 。



.. code-block:: java
    :caption: 拷贝示例类 Department
    :name: java-extend-department
    :linenos: 


    public class implements Cloneable{

        private int id;
        private String name;
    
        public Department(int id, String name)
        {
            this.id = id;
            this.name = name;
        }

        @Override
        protected Object clone() throws CloneNotSupportedException {
            return super.clone();
        }

        @Override
        public String toString() {
            return "Department{" +
                    "id=" + id +
                    ", name='" + name + '\'' +
                    '}';
        }
    
        //Getters and Setters
    }

.. code-block:: java
    :caption: 拷贝示例类 Employee 
    :name: java-extend-employee
    :linenos: 

    public class Employee implements Cloneable{
    
        private int empoyeeId;
        private String employeeName;
        private Department department;
    
        public Employee(int id, String name, Department dept)
        {
            this.empoyeeId = id;
            this.employeeName = name;
            this.department = dept;
        }
        @Override
        protected Object clone() throws CloneNotSupportedException {
            return super.clone();
        }
        
        //Getters and Setters
    }


.. code-block:: java
    :caption: 浅拷贝示例
    :name: java-extend-shallow-copy-example
    :linenos: 

    public static void main(String[] args) throws CloneNotSupportedException {
        Department hr = new Department(1, "Human Resource");

        Employee original = new Employee(1, "Admin", hr);
        Employee cloned = (Employee) original.clone();

        //Let change the department name in cloned object and we will verify in original object
        cloned.getDepartment().setName("Finance");

        System.out.println(original.getDepartment().getName()); //Finance
        System.out.println(cloned.getDepartment().getName());  //Finance
    }

需要注意的是，一些对象（该对象的属性都是基本类型或String）的浅拷贝的表现类似于深拷贝。

.. code-block:: java
    :caption: 浅拷贝示例2
    :linenos: 

    public static void main(String[] args) throws CloneNotSupportedException {
        Department hr = new Department(1, "Human Resource");
        Department department= (Department) hr.clone();

        department.setId(1244);
        department.setName("1244");

        System.out.println(hr); //Department{id=1, name='Human Resource'}
        System.out.println(department); //Department{id=1244, name='1244'}
    }

|30|

深拷贝
-----------------

深拷贝
    创建一个新对象，然后将当前对象的非静态字段复制到该新对象，无论该字段是值类型的还是引用类型，都复制独立的一份。当你修改其中一个对象的任何内容时，都不会影响另一个对象的内容。

深拷贝示例依旧使用拷贝示例类 :ref:`Employee <java-extend-employee>`  和 :ref:`Department <java-extend-department>` ；唯一区别在于 Employee 类的 clone 方法需要重写成以下形式：

.. code-block:: java
    :caption: 拷贝示例类 Employee 类的 clone 方法重写
    :linenos: 

    @Override
    protected Object clone() throws CloneNotSupportedException {
        Employee cloned = (Employee)super.clone();
        cloned.setDepartment((Department)cloned.getDepartment().clone());
        return cloned;
    }


.. code-block:: java
    :caption: 深拷贝示例
    :linenos: 

    public static void main(String[] args) throws CloneNotSupportedException {
        Department hr = new Department(1, "Human Resource");
        Department department= (Department) hr.clone();

        department.setId(1244);
        department.setName("1244");

        System.out.println(hr); //Department{id=1, name='Human Resource'}
        System.out.println(department); //Department{id=1244, name='1244'}
    }

.. code-block:: java
    :caption: 深拷贝示例2（同浅拷贝示例）
    :name: java-extend-shallow-copy-example
    :linenos: 

    public static void main(String[] args) throws CloneNotSupportedException {
        Department hr = new Department(1, "Human Resource");

        Employee original = new Employee(1, "Admin", hr);
        Employee cloned = (Employee) original.clone();

        //Let change the department name in cloned object and we will verify in original object
        cloned.getDepartment().setName("Finance");

        System.out.println(original.getDepartment().getName()); //Human Resource
        System.out.println(cloned.getDepartment().getName());  //Finance
    }

这种做法有个弊端，这里我们 Employee 类只有一个 Department 引用类型，而 Department 类没有，所以我们只用重写 Department 类的 clone 方法，但是如果 Department 类也存在一个引用类型，那么我们也要重写其 clone 方法，这样下去，有多少个引用类型，我们就要重写多少次，如果存在很多引用类型，那么代码量显然会很大，所以这种方法不太合适对已有代码进行修改。


|50|

通过实现 Serializable 接口进行深拷贝 
========================================

序列化是将对象写到流中便于传输，而反序列化则是把对象从流中读取出来。这里写到流中的对象则是原始对象的一个拷贝，因为原始对象还存在 JVM 中，所以我们可以利用对象的序列化产生克隆对象，然后通过反序列化获取这个对象。

通过实现 Serializable 接口进行拷贝 ，即通过序列化实现拷贝，通过序列化实现的拷贝一定是深拷贝。因为序列化产生的是两个完全独立的对象，所有无论嵌套多少个引用类型，序列化都是能实现深拷贝的。

实现序列化的方法
  1. 实现Serializable接口
       * 该接口是一个可序列化的标志，并没有包含实际的属性和方法。
       * 如果不在该方法中添加readObject()和writeObject()方法，则采取默认的序列化机制。如果添加了这两个方法之后还想利用Java默认的序列化机制，则在这两个方法中分别调用defaultReadObject()和defaultWriteObject()两个方法。
       * 为了保证安全性，可以使用transient关键字进行修饰不必序列化的属性。因为在反序列化时，private修饰的属性也能被查看到。

  2. 实现ExternalSerializeable方法
       * 自己对要序列化的内容进行控制，控制哪些属性能被序列化，哪些不能被序列化。


.. code-block:: java
    :caption: 实现序列化接口的 Department 类
    :linenos: 

    public class Department implements Serializable
    {
        private int id;
        private String name;

        public Department(int id, String name)
        {
            this.id = id;
            this.name = name;
        }

        //Getters and Setters and toString
    }

.. code-block:: java
    :caption: 实现序列化接口的 Employee 类
    :linenos: 

    public class Employee implements Serializable {

        private int empoyeeId;
        private String employeeName;
        private Department department;

        public Employee(int id, String name, Department dept)
        {
            this.empoyeeId = id;
            this.employeeName = name;
            this.department = dept;
        }

        //Getters and Setters and toString
    }


.. code-block:: java
    :caption: 通过序列化实现深拷贝示例
    :linenos: 
    
    public class DeepCopyMain {
        public static void main(String[] args) throws Exception {
            Department hr = new Department(1, "Human Resource");
            Employee original = new Employee(1, "Admin", hr);
            Employee cloned = deepClone(original);

            cloned.getDepartment().setName("Finance");

            System.out.println(original); 
            //Employee{empoyeeId=1, employeeName='Admin', department=Department{id=1, name='Human Resource'}}
            System.out.println(cloned); 
            //Employee{empoyeeId=1, employeeName='Admin', department=Department{id=1, name='Finance'}}
        }

        //深度拷贝
        public static <T extends Serializable> T deepClone(T origin) throws Exception{
            // 序列化
            ByteArrayOutputStream bos = new ByteArrayOutputStream();
            ObjectOutputStream oos = new ObjectOutputStream(bos);

            oos.writeObject(origin);

            // 反序列化
            ByteArrayInputStream bis = new ByteArrayInputStream(bos.toByteArray());
            ObjectInputStream ois = new ObjectInputStream(bis);

            //需要处理类型变换异常
            T object = (T) ois.readObject();
            return object;
        }
    }




----

.. [#] 原文链接 `Java的深拷贝和浅拷贝 <https://www.cnblogs.com/ysocean/p/8482979.html>`_ 

