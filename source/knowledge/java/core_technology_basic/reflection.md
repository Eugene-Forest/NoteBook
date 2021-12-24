# 反射

反射库（ reflection library ） 提供了一个非常丰富且精心设计的工具集， 以便编写能够动态操纵 Java 代码的程序。这项功能被大量地应用于 JavaBeans 中。

能够分析类能力的程序称为反射（reflective）。

反射机制可以用来：

- 在运行时分析类的能力。
- 在运行时查看对象， 例如， 编写一个 toString 方法供所有类使用。
- 实现通用的数组操作代码。
- 利用 Method 对象， 这个对象很像中的函数指针。

反射是一种功能强大且复杂的机制。 使用它的主要人员是工具构造者，而不是应用程序员。

## Class 类

Class 类实际上是一个泛型类。

Class 类实例的获取：

- Object 类中的 getClass( ) 方法将会返回一个 Class 类型的实例。

  > ```java
  > //方法一
  > Integer integer= 10;
  > System.out.println(integer.getClass().getName());
  > /* code run result of the first method :
  > java.lang.Integer
  >  */
  > ```

- **调用静态方法 forName 获得类名对应的 Class 对象。** 如果类名保存在字符串中， 并可在运行中改变， 就可以使用这个方法。当然， 这个方法只有在 className 是类名或接口名时才能够执行。否则，forName 方法将抛出一个 checked exception （已检查异常）。

  > ```java
  > //方法二
  > try {
  >     String dassName = "java.util.Random";
  >     Class<?> cl = Class.forName(dassName);
  >     System.out.println(cl.getName());
  >     dassName = "java.lang.Number";
  >     cl = Class.forName(dassName);
  >     System.out.println(cl.getName());
  > } catch (ClassNotFoundException e) {
  >     e.printStackTrace();
  > }
  > /* code run result of the second method :
  > java.util.Random
  > java.lang.Number
  >  */
  > ```

- 获得 Class类对象的第三种方法非常简单。如果 T 是任意的 Java 类型（或 void 关键字) `T.class` 将代表匹配的类对象。

  > ```java
  > //方法三
  > Class<?> cc=int.class;
  > System.out.println(cc.getName());
  > cc=Integer.class;
  > System.out.println(cc.getName());
  > /* code run result of the third method :
  > int
  > java.lang.Integer
  >  */
  > ```

:::{attention}
请注意， **一个 Class 对象实际上表示的是一个类型，而这个类型未必一定是一种类。** 例如，int 不是类， 但 int.class 是一个 Class 类型的对象。
:::



## 利用反射分析类的能力

**反射机制最重要的内容——检查类的结构。**

Class类中的 `getFields`、 `getMethods` 和 `getConstructors` 方 法 将 分 别 返 回 类 提 供 的 *public* 域、 方法和构造器数组， 其中包括超类的公有成员。

Class 类的 `getDeclareFields` 、 `getDeclareMethods` 和 `getDeclaredConstructors` 方法将分别返回类中声明的全部域、 方法和构造器， 其中包括私有和受保护成员，但不包括超类的成员。

除了以上大范围的分析，还能针对修饰符、返回值以及参数等等的详细分析。

:::{figure} ../../../img/java/core_tech/base/reflect.fmc.png
获取域、方法、构造函数的信息
:::

:::{figure} ../../../img/java/core_tech/base/reflect.modifier.png
获取和比较修饰符信息
:::



## 在运行时使用反射分析对象

:::{sidebar} 类代码
以下为类源码：

- {download}`Employee.java <../example_java/basic/inherit/Employee.java>`
- {download}`Manager.java <../example_java/basic/inherit/Manager.java>`
:::

我们在分析对象时，不仅仅需要分析对象的类的结构，分析对象的属性值也是十分必要的，但是这就出现了一个问题，针对对象中的私有域，除非拥有访问权限，否则 Java 安全机制只允许査看任意对象有哪些域， 而不允许读取它们的值；不然会抛出以下代码的 `java.lang.IllegalAccessException` 错误。

我们看看以下代码：

```java
Employee eugene = new Manager("1244", "eugene", 2000, 2021, 8, 10);
Class c=eugene.getClass();
try {
    Field field=c.getDeclaredField("bonus");
    Object o=field.get(eugene);
    System.out.println(o.toString());
} catch (NoSuchFieldException | IllegalAccessException e) {
    e.printStackTrace();
}

/* code run result :
java.lang.IllegalAccessException: Class core.base.reflection.Main can not access a member of class core.base.inherit.Manager with modifiers "private"
    at sun.reflect.Reflection.ensureMemberAccess(Reflection.java:102)
*/
```

反射机制的默认行为受限于 Java 的访问控制。然而， 如果一个 Java 程序没有受到安全管理器的控制， 就可以覆盖访问控制。 为了达到这个目的， 需要调用 `Field、` `Method` 或 `Constructor` 对象的 `setAccessible` 方法。

```{code-block} java
:emphasize-lines: 5

Employee eugene = new Employee("1244", "eugene", 2000, 2021, 8, 10);
Class c=eugene.getClass();
try {
    Field field=c.getDeclaredField("name");
    field.setAccessible(true);
    Object o=field.get(eugene);
    System.out.println(o.toString());
} catch (NoSuchFieldException | IllegalAccessException e) {
    e.printStackTrace();
}
/* code run result :
eugene
*/
```

:::{note}

setAccessible 方法是 AccessibleObject 类中的一个方法， 它是 Field、 Method 和 Constructor 类的公共超类。这个特性是为调试、 持久存储和相似机制提供的。
:::

get 方法还有一个需要解决的问题。name 域是一个 String, 因此把它作为 Object 返回没有什么问题。但是， 假定我们想要查看 salary 域。它属于 double 类型，而 Java中数值类型不是对象。 可以使用 Field 的 getDouble 方法来获取（Field 有所有基本类型的 get 方法）。当然，可以获得就可以设置。 调用 field.set(obj，value) 可以将 obj 对象的 field 域设置成新值。

以下为实例：

```{literalinclude} ../example_java/basic/reflection/ObjectAnalyzer.java
:language: java
```



## 调用任意方法

在 C 和 C++ 中， 可以从函数指针执行任意函数。从表面上看， Java 没有提供方法指针，即将一个方法的存储地址传给另外一个方法。然而， 反射机制允许你调用任意方法。

在 Method 类中有一个 invoke 方法， 它允许调用包装在当前 Method 对象中的方法。invoke 方法的签名是： `Object invoke(Object obj, Object... args)`

对于静态方法，第一个参数可以被忽略， 即可以将它设置为 null。

例如， 假设用 ml 代表 Employee 类的 getName 方法，下面这条语句显示了如何调用这个方法：

`String n = (String) ml.invoke(harry);`

如何得到 Method 对象呢？ 当然， 可以通过调用 getDeclareMethods 方法， 然后对返回的 Method 对象数组进行查找， 直到发现想要的方法为止。 也可以通过调用 Class类中的 getMethod方法得到想要的方法。然而， 有可能存在若干个相同名字的方法，因此要格外小心，以确保能够准确地得到想要的那个方法。有鉴于此，可能还必须提供想要的方法的参数类型。

例如， 下面说明了如何获得 Employee 类的 getName 方法和 raiseSalary 方法的方法指针。

```java
Method ml = Employee.class.getMethod("getName");
Method m2 = Employee.class.getMethod("raiseSalary", double.class);
```

以下为实例演示：

```java
Manager eugene = new Manager("1244", "eugene", 2000, 2021, 8, 10);
try {
    Method ml = Manager.class.getMethod("setBonus", double.class);
    ml.invoke(eugene,100);
    ml = Manager.class.getMethod("getSalary");
    // invoke 的参数和返回值必须是 Object 类型的。这就意味着必须进行多次的类型转换。
    // 这样做将会使编译器错过检查代码的机会。
    Double sum= (Double) ml.invoke(eugene);
    System.out.println(sum);
} catch (NoSuchMethodException | IllegalAccessException | InvocationTargetException e) {
    e.printStackTrace();
}
/* code run result :
2100.0
*/
```
