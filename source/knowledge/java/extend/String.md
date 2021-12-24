# Java 字符串

实际上任何语言都没有提供字符串这个概念，而是使用字符数组来描述字符串。Java 里面严格来说也是没有字符串的，在所有的开发里面字符串的应用有很多，于是 Java 为了应对便创建了 String 类这个字符串类。使用 `""` 定义的内容都是字符串，理解 Java 的 String 类需要从类的角度和内存关系上分析这个类。

(realize-string)=

## String

### String 的定义

注意一个常见的错误，不要记错了。因为 String 是 final 修饰的，无法被继承。所以 String 不是 Java 的基本数据类型。

字符串在 Java 中是不可变的，因此适合在多线程环境下使用。

```{code-block} java
:caption: "String \u7684\u5B9A\u4E49"

public final class String
    implements java.io.Serializable, Comparable<String>, CharSequence
```

```{code-block} java
:caption: "String \u5B57\u7B26\u4E32\u7684\u5B58\u50A8\u65B9\u5F0F"

/** The value is used for character storage. */
private final char value[];
```

### String类对象的实例化方式

```{code-block} java
:caption: "String\u7C7B\u5BF9\u8C61\u7684\u5B9E\u4F8B\u5316\u65B9\u5F0F"

String name1 = "Sakura";    //直接赋值方式
String name2 = new String("Sakura");  //利用构造方法实例化
```

当我们使用双引号创建一个字符串时，如上 name1，JVM 首先在字符串池中寻找具有相同值的字符串。如果找到了，它将返回字符串池中的字符串对象的引用。否则，它会在字符串池中创建字符串对象并返回引用。JVM 通过在不同的线程中使用相同的字符串，节省了大量的内存。

如果使用 new 运算符创建字符串，则会直接在堆中创建它。

### String 类对象运算

#### 使用"=="和equals比较字符串是否相等

```{code-block} java
:caption: "\"==\"\u548Cequals\u6BD4\u8F83\u5B57\u7B26\u4E32\u662F\u5426\u76F8\u7B49"

String name1 = "Sakura";
String name2 = new String("Sakura");
System.out.println("name1==name2 :"+ (name1 == name2));
System.out.println("name1.equal(name2) : "+name1.equals(name2));
System.out.println("name=='Sakura' : "+ (name1=="Sakura"));
System.out.println("name1.equal("sakura") :" +name1.equals("sakura") );
/** code running result :
    *
    * name1==name2 :false
    * name1.equal(name2) : true
    * name=='Sakura' : true
    * name1.equal(sakura) :false
    */
```

使用"=="比较的是两个对象在内存中的地址是否一致，也就是比较两个对象是否为同一个对象。
使用equals()方法比较的是对象的值是否相等，

两个字符串只有在它们具有相同字符串的时候才相等， `equals()` 方法区分大小写。如果您正在寻找不区分大小写的检查，您应该使用 `equalsIgnoreCase()` 方法。

#### 字符串拼接

Java中不允许程序员重载任何操作符，但是Java内部重载了两个用于String类的操作符"+"和"+="。操作符"+"可以用于连接字符串，操作符"+="用于将连接后的字符串再次赋给原字符串引用。尽管在内部它使用 StringBuilder 来执行这个动作。

由于 String 在 Java 中是不可变的，因此每当我们执行字符串拼接操作时，它都会生成一个新的 String 并丢弃旧的 String 以进行垃圾收集。

:::{note}
这些重复的操作会在堆中产生大量垃圾冗余。所以 Java 提供了 StringBuffer 和 StringBuilder 类，用于字符串操作。StringBuffer 和 StringBuilder 是 Java 中的可变对象。
:::

```{code-block} java
:caption: "\u5B57\u7B26\u4E32\u62FC\u63A5\u6D4B\u8BD5\u4EE3\u7801"

public static void main(String[] args) {
    String name1 = "Sakura";
    String name2 = new String("Sakura");
    name1=name1+name2;
}
```

```{code-block} guess
:caption: "\u53CD\u7F16\u8BD1\u5B57\u7B26\u4E32\u62FC\u63A5\u6D4B\u8BD5\u4EE3\u7801\
:  \uFF08javap -c\uFF09"

public static void main(java.lang.String[]);
Code:
    0: ldc           #2                  // String Sakura
    2: astore_1
    3: new           #3                  // class java/lang/String
    6: dup
    7: ldc           #2                  // String Sakura
    9: invokespecial #4                  // Method java/lang/String."<init>":(Ljava/lang/String;)V
    12: astore_2
    13: new           #5                  // class java/lang/StringBuilder
    16: dup
    17: invokespecial #6                  // Method java/lang/StringBuilder."<init>":()V
    20: aload_1
    21: invokevirtual #7                  // Method java/lang/StringBuilder.append:(Ljava/lang/String;)Ljava/lang/StringBuilder;
    24: aload_2
    25: invokevirtual #7                  // Method java/lang/StringBuilder.append:(Ljava/lang/String;)Ljava/lang/StringBuilder;
    28: invokevirtual #8                  // Method java/lang/StringBuilder.toString:()Ljava/lang/String;
    31: astore_1
    32: return
```

我们通过反汇编测试代码的 class 文件，然后我们可以看到在 main 方法中的行编号为13的地方新建了一个 StringBuilder 对象，而且通过之后的代码可知，字符串的拼接运算是通过 StringBuilder.append 方法来执行的。

:::{note}
javap 是 Java class文件分解器，可以反编译（即对javac编译的文件进行反编译），也可以查看java编译器生成的字节码；用于分解class文件。javap 的可选选项可以通过命令 `javap -help` 了解。 关于 javap 的更多信息 {ref}`点击查看 javap 命令 笔记 <command-javap>`
:::

## StringBuffer 和 StringBuilder

它们为字符串操作提供了 append、insert、delete 和 substring 方法。

| StringBuffer  | StringBuilder |
| ------------- | ------------- |
| 线程安全      | 非线程安全    |
| 同步          | 非同步        |
| 始于 Java 1.0 | 始于 Java 1.5 |
| 慢            | 快            |

在 Java 1.4 之前，StringBuffer 是字符串操作的唯一选择。但是，它的一个缺点是所有公共方法都是同步的。 StringBuffer 提供线程安全性，但以性能为代价。

在大多数情况下，我们不会在多线程环境中使用 String。假设在单线程环境中或无关线程安全，要使用 StringBuilder。反之，使用 StringBuffer 进行线程安全的操作。

## 总结

- String 是不可变的，而 StringBuffer 和 StringBuilder 是可变类。
- StringBuffer 是线程安全和同步的，而 StringBuilder 不是。这就是 StringBuilder 比 StringBuffer 快的原因。
- 字符串连接运算符 (+) 在内部使用 StringBuilder 类。
- 对于非多线程环境中的字符串操作，我们应该使用 StringBuilder 否则使用 StringBuffer 类。
