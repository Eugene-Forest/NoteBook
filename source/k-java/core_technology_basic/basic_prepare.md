# java的基本程序设计结构

## java命名规范 [^id13]

- java是区分大小写的
- 类的命名，使用驼峰式命名的规范；如\`\`FirstSample\`\`
- 常量以全大写以及用下划线分割单词；如：`public static final String GAME_COLOR=”RED”`
- 方法的名字的第一个单词应以小写字母作为开头，后面的单词则用大写字母开头。例如： `sendMessge`，`send`。方法
- 变量名同方法名一样，第一个第一个单词应以小写字母作为开头，后面的单词则用大写字母开头 `message`,。
- 包名一律小写，使用小写字母同时不要使用下划线将单词分开，如 `com.xxx.settlment`，不要 `com.xxx.Settlement`，也不要 `com.xxx.settlement.jsf_util`。

:::{note}

为了更好区分方法名以及变量名，同时在为变量和方法命名时最好取些有意义的名字，应尽量使用简短的英文单词。 较好的方法是：

- 方法名以 **动词+名词** 为组合命名，如 `initInformation`
- 变量以 **冠词+名词/名词+名词** 为组合,如 `studentInformation`, `aInformation`
:::

:::{warning}
所有命名规则必须遵循以下规则：

1. 名称只能由字母、数字、下划线、\$符号组成
2. 不能以数字开头
3. 名称不能使用JAVA中的关键字
4. 最好不要出现中文及拼音命名
:::

## 注释

在 Java 中，有 3 种标记注释的方式。

- 最常用的方式是使用 // ，其注释内容从 // 开始到本行结尾。
- 当需要长篇的注释时，既可以在每行的注释前面标记 //，也可以使用 /\* 和 \*/ 将一段比较长的注释括起来。
- 第 3 种注释可以用来自动地生成文档。这种注释以 /\*\* 开始， 以 \*/ 结束。

(java-basic-datatypes)=

## 数据类型

**Java 是一种强类型语言**。这就意味着必须为每一个变量声明一种类型: **在Java 中，一共有 8 种基本类型（ primitive type )**, 其中有 4 种整型、2 种浮点类型、 1 种用于表示 Unicode 编码的字符单元的字符类型 char (请参见论述 char 类型的章节） 和 1 种用于表示真值的 boolean 类型。

| 类别   | 类型   | 存储需求 | 取值范围                                                |
| ------ | ------ | -------- | ------------------------------------------------------- |
| 整型   | int    | 4 字节   | -2 147 483 648 ~ 2 147 483 647 (正好超过 20 亿)         |
|        | short  | 2 字节   | -32 768 ~ 32 767                                        |
|        | long   | 8字节    | -9 223 372 036 854 775 B08 ~ 9 223 372 036 854 775 807  |
| 浮点数 | float  | 4 字节   | 大约 ± 3.402 823 47E+38F (有效位数为 6 ~ 7 位）         |
|        | double | 8 宇节   | 大约 ± 1.797 693 134 862 315 70E+308 (有效位数为 15 位> |
| 字符   | char   | 2字节    |                                                         |

:::{note}

下面是用于表示溢出和出错情况的三个特殊的浮点数值：

- 正无穷大
- 负无穷大
- NaN (不是一个数字）
:::

:::{attention}

- 不同于 C++， Java 没有任何无符号（unsigned) 形式的 int、 long、short 或 byte 类型。
- Java 有一个能够表示任意精度的算术包， 通常称为“大数值”（ big number。) 虽然被称为大数值，但它并不是一种新的 Java 类型，而是一个 Java 对象。
:::

:::{warning}

- 不建议在 Java 程序中使用 char 数据类型。 {ref}`参见 Java 中 char 和 String 的细节和使用注意 <not-using-char>` 。
- 注意基本数据类型的封装类的使用方法。 {ref}`参见 Java 的基本数据类型及其封装类 <java-basic-datatype-and-class>` 。
:::

## 枚举类型

有时候，变量的取值只在一个有限的集合内。例如： 销售的服装或比萨饼只有小、中、大和超大这四种尺寸。当然， 可以将这些尺寸分别编码为 1、2、3、4 或 S、 M、 L、X。但这样存在着一定的隐患。在变量中很可能保存的是一个错误的值（如 0 或 m)。

针对这种情况， 可以自定义枚举类型。枚举类型包括有限个命名的值。

```java
enum Size {SMALL,MEDIUM,LARGE,EXTRA_LARGE};

public class Test {
   public static void main(String[] args) {
      Size size=Size.SMALL;
      System.out.println(size);
   }
}
```

枚举类型（如上代码中的Size类）的变量只能存储这个类型声明中给定的某个枚举值，或者 null 值，null 表示这个变量没有设置任何值。

## 字符串类型 --String类

**Java 字符串大致类似于 char\\* 指针**

String 类没有提供用于修改字符串的方法。由于不能修改 Java 字符串中的字符， 所以在 Java 文档中将 String 类对象称为不可变字符串。

不可变字符串有一个优点：编译器可以让字符串共享。可以想象将各种字符串存放在公共的存储池中。字符串变量指向存储池中相应的位置。如果复制一个字符串变量，原始字符串与复制的字符串共享相同的字符。这样做会不会产生内存遗漏呢？ 毕竞， 原始字符串放置在堆中。十分幸运，Java 将自动地进行垃圾回收。 如果一块内存不再使用了， 系统最终会将其回收。

### 字符串之间的比较

对于字符串，一定不要使用=运算符检测两个字符串是否相等！ 这个运算符只能够确定两个字串是否放置在同一个位置上。可以使用 equals 方法检测两个字符串是否相等。如： `s.equals(t)`。

### 空字符串与null

空串 "" 是长度为 0 的字符串。空串是一个 Java 对象， 有自己的串长度（ 0 ) 和内容（空）。不过， String 变量还可以存放一个特殊的值， 名为 null, 这表示目前没有任何对象与该变量关联。

有时要检查一个字符串既不是 null 也不为空串，首先要检查字符串是否为空。这种情况下就需要使用如下条件

`if (str != null && str.length() != 0)`

:::{note}

了解java虚拟机的垃圾回收机制；了解String的字符串共享存储池机制。
:::

% //todo 添加java虚拟机的垃圾回收机制；了解String的字符串共享存储池机制方面的笔记链接

## 输入输出

### 标准输入流

打印输出到“ 标准输出流”（即控制台窗口）是一件非常容易的事情，只要调用 `System.out.println` 即可。然而，读取“ 标准输人流” `System.in` 就没有那么简单了。要想通过控制台进行输人，首先需要构造一个 Scanner 对象，并与“ 标准输人流” `System.in` 关联。

```{code-block} java
:emphasize-lines: 5

import java.util.Scanner;

public class StringTest {
   public static void main(String[] args) {
      Scanner in=new Scanner(System.in);
      System.out.println("Please inter your name?");
      String name=in.nextLine();
      System.out.println("Hello, "+name);
   }
}
```

运行截图：

```guess
Please inter your name?
Eugene Forest
Hello, Eugene Forest
```

:::{warning}
读取输入操作在实际使用中基本不使用。了解更多与标准输入流相关请前往查看API文档 Scanner。
:::

### 格式化输出

在早期的 Java 版本中，格式化数值曾引起过一些争议。庆幸的是，Java SE 5.0 沿用了 C 语言库函数中的 printf方法。

| 转换符 | 类 型          | 举 例      |
| ------ | -------------- | ---------- |
| d      | 十进制整数     | 159        |
| f      | 定点浮点数     | 15.9       |
| s      | 字符串         | Hello      |
| x      | 十六进制整数   | 9f         |
| c      | 字符           | H          |
| o      | 八进制整数     | 237        |
| b      | 布尔           | True       |
| h      | 散列码         | 42628b2    |
| e      | 指数浮点数     | 1.59e+01   |
| g      | 通用浮点数     |            |
| a      | 十六进制浮点数 | 0xl.fccdp3 |

:::{note}

在实际使用中，浮点数的标准输出流的格式化使用地比较多。
:::

```java
import java.util.Scanner;

public class StringTest {
   public static void main(String[] args) {
      Scanner in=new Scanner(System.in);
      System.out.println("Please inter your name:");
      String name=in.nextLine();
      System.out.println("Please inter your age:");
      Integer age=in.nextInt();
      System.out.printf("Your age is %d .\n", age);
      System.out.printf("If you live to 90 years, you have already spent %.2f persent of your life!",((float)age/90)*100);
   }
}
```

```guess
Please inter your name:
Eugene forest
Please inter your age:
22
Your age is 22 .
If you live to 90 years, you have already spent 24.44 persent of your life!
```

## 数组

可以使用下面两种形式声明数组

`int[] a;` 或 `int a[];`

大多数 Java 应用程序员喜欢使用第一种风格， 因为它将类型 int\[\] ( 整型数组）与变量名分开了。

**创建一个数字数组时， 所有元素都初始化为 0。boolean 数组的元素会初始化为 false。对象数组的元素则初始化为一个特殊值 null, 这表示这些元素（还）未存放任何对象。**

:::{note}

对于对象数组类型的，在Java中一般使用集合来实现和使用。
:::

% //todo 添加Java集合笔记链接

### for each 循环

```java
int[] a={1,2,3,4};
for (int element : a)
   System.out.println(element);
```

for each 循环语句的循环变量将会遍历数组中的每个元素， 而不需要使用下标值。

### 实例

```java
import java.util.Arrays;

public class ArrayTest {

   public static void main(String[] args) {
      int[] a=new int[3];
      char[] message= {'E','u','g','e','n','e'};
      boolean[] flag=new boolean[2];
      String[] names=new String[2];
      for (boolean b : flag) {
         System.out.print(b);
      }
      System.out.println("\n*******");
      for (int i : a) {
         System.out.print(i);
      }
      System.out.println("\n********");
      for (char b : message) {
         System.out.print(b);
      }
      System.out.println("\n********");
      for (String string : names) {
         System.out.print(string);
      }
      System.out.println("\n********");
      System.out.println(Arrays.toString(message));

   }

}
```

```guess
falsefalse
*******
000
********
Eugene
********
nullnull
```

### 数组拷贝

在 Java 中，允许将一个数组变量拷贝（赋值）给另一个数组变量。这时，两个变量将引用同一个数。

`int[] a={1,2,3,4};
int[] b=a;`

如果希望将一个数组的所有值拷贝到一个新的数组中去，就要使用 Arrays 类的 copyOf 方法：

`Arrays.copyOf(int[] original, int newLength)`

拷贝后的数组长度可以大于源数组（即newLength > original.length），多余的未被赋值的部分自动数组初始化，即如果数组元素是数值型，那么多余的元素将被赋值为 0 ; 如果数组元素是布尔型，则将赋值为 false。相反，如果长度小于原始数组的长度，则只拷贝最前面的数据元素。

```java
import java.util.Arrays;

public class CopyArrayTest {

   public static void main(String[] args) {
      int[] a={1,2,3,4};
      int[] b=a;
      int[] c=Arrays.copyOf(a, a.length);
      a[0]=127;
      System.out.println(Arrays.toString(a));
      System.out.println("**********");
      System.out.println(Arrays.toString(b));
      System.out.println("**********");
      System.out.println(Arrays.toString(c));
   }

}
```

```guess
[127, 2, 3, 4]
**********
[127, 2, 3, 4]
**********
[1, 2, 3, 4]
```

[^id13]: 虽然java的命名规范是宽松的，但是作为一个程序员要有良好的编程命名规范。
