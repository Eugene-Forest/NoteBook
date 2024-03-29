# Java 中 char 和 String 与字符编码的细节和使用注意

## char 数据类型的使用注意

在 Java 中使用 char 数据类型来表示字符，但是 char 类型并不能表示一切字符。

## Unicode 字符集

首先需要知道我们在 **Java 中使用的是 Unicode 字符集**。在其出现之前有已经有了很多字符集，如 ANSI、GB2312 等等。由于存在众多标准不同的字符集，这就导致了两个问题：

对于任意给定的一个代码值，在不同的字符集中可能对应不同的字符；
采用大字符集的语言其编码长度可能不同，如对常用字符采用单字节编码，而其他字符采用多字节编码。
Unicode 字符集的出现就是为了统一编码，消除以上的问题。所谓字符集就是一个由众多不同的字符组成的集合。**Unicode 字符集对每一个字符都分配了一个唯一的 代码点(code point) 用来标识字符本身**。所谓代码点就是一个添加了 U+ 前缀的十六进制整数，如字母 A 的代码点就是 U+0041。

有了Unicode 字符集后，我们要考虑的就是以什么样的方式对这些字符进行传输和存储，这就是 Unicode 编码的实现方式，我们称为 **Unicode 转换格式(Unicode Transformation Format，简称 UTF)**。我们熟悉的 UTF-8、 UTF-16 等就是不同的 Unicode编码实现方式。

在 Unicode 字符集诞生之初，采用 **UCS-2(2-byte Universal Character Set) 这种定长的编码方式对 Unicode 字符集进行编码，这种方式采用 16 bit 的长度来进行字符编码，所以最多可以对 2^16 = 65536 个字符进行编码(编码范围从 U+0000 ~ U+FFFF)**。在当时的情况下，设计者们用了不到一半的数量就对所有字符进行了编码，并且认为剩余的空间足够用于未来新增字符的编码。

不幸的是，随着中文、日文、韩文等表意文字不断的加入，Unicode 字符集中的字符数量很快超过了 16 位所能编码的最大字符数量，于是设计者们对 Unicode 字符集进行了新的设计。

新的设计将字符集中的所有字符分为 17 个 代码平面(code plane)。*其中 U+0000 ~ U+FFFF 这个代码点范围被划定为* **基本多语言平面(Basic MultilingualPlane，简记为 BMP)**，*其余的字符分别划入 16 个 辅助平面(Supplementary Plane)，代码点范围为 U+10000 ~ U+10FFFF，这些处于辅助平面的字符我们称作 增补字符(supplementary characters)*。

在 Unicode 字符集中的字符被重新划分到不同平面后，需要注意以下两个方面：

**BMP 范围内的字符和 UCS-2 下的字符编码基本保持一致，但是 BMP 中的 U+D800 ~ U+DFFF 部分被留空，不分配给任何字符，作用是用于给辅助平面内的字符进行编码。**

不是每个平面内的每个位置都被分配给了指定的字符，原因是：

- 特殊用途，如 BMP 中的 U+D800 ~ U+DFFF 部分；
- 作为保留空间
- 没有足够的字符



## UTF-8

UTF-8 是一个非常惊艳的编码方式，漂亮的实现了对 ASCII 码的向后兼容，以保证 Unicode 可以被大众接受。

UTF-8 是目前互联网上使用最广泛的一种 Unicode 编码方式，它的最大特点就是可变长。**UTF-8可以使用 1-4 个字节表示一个字符，根据字符的不同变换长度**。编码规则如下：

对于单个字节的字符，第一位设为 0，后面的 7 位对应这个字符的 Unicode 码点。因此，对于英文中的 0 - 127 号字符，与 ASCII 码完全相同。这意味着 ASCII 码那个年代的文档用 UTF-8 编码打开完全没有问题。

对于需要使用 N 个字节来表示的字符（N > 1），第一个字节的前 N 位都设为 1，第 N + 1 位设为0，剩余的 N - 1 个字节的前两位都设位 10，剩下的二进制位则使用这个字符的 Unicode 码点来填充。

| Unicode编码(十六进制) | UTF-8 字节流(二进制)                |
| --------------------- | ----------------------------------- |
| 000000-00007F         | 0xxxxxxx                            |
| 000080-0007FF         | 110xxxxx 10xxxxxx                   |
| 000800-00FFFF         | 1110xxxx 10xxxxxx 10xxxxxx          |
| 010000-10FFFF         | 11110xxx 10xxxxxx 10xxxxxx 10xxxxxx |

UTF-8 的特点是对不同范围的字符使用不同长度的编码。对于 0x00-0x7F 之间的字符，UTF-8 编码与 ASCII 编码完全相同。UTF-8 编码的最大长度是 4 个字节。从上表可以看出，4 字节模板有 21 个x，即可以容纳 21 位二进制数字。Unicode 的最大码位 0x10FFFF 也只有 21 位。

例1：“汉”字的 Unicode 编码是 0x6C49。0x6C49 在 0x0800-0xFFFF 之间，使用 3 字节模板：1110xxxx 10xxxxxx 10xxxxxx。将 0x6C49 写成二进制是：0110 1100 0100 1001， 用这个比特流依次代替模板中的 x，得到：11100110 10110001 10001001，即 E6 B1 89。

例2：Unicode 编码 0x20C30 在 0x010000-0x10FFFF 之间，使用 4 字节模板：11110xxx 10xxxxxx 10xxxxxx 10xxxxxx。将 0x20C30 写成 21 位二进制数字（不足 21 位就在前面补 0）：0 0010 0000 1100 0011 0000，用这个比特流依次代替模板中的 x，得到：11110000 10100000 10110000 10110000，即 F0 A0 B0 B0。

解码的过程也十分简单：如果一个字节的第一位是 0 ，则说明这个字节对应一个字符；如果一个字节的第一位1，那么连续有多少个 1，就表示该字符占用多少个字节。

:::{note}

Java 字符编码 [了解更多](https://www.cnblogs.com/binarylei/p/10760233.html)
:::



## UTF-16

UTF-16 是 Unicode 的一种编码方式，它用两个字节来编码 BMP 里的代码点，用四个字节编码其余平面里的代码点（暂不考虑字节顺序）。由于 BMP 里只有 65535 个代码点，所以直接把代码点转换成 2 个字节就可以了。BMP 之外的平面稍微复杂一点，需要先将代码点转化为一个代理对，然后再转为 4 个字节。

UTF-16 同样使用 16 bit 的编码来表示 Unicode 字符，也就是说 UTF-16 的 代码单元(code unit) 为 16 位。代码单元指的是字符编码的一个最基本单元，即任意一个字符必然是由 n(n≥1) 个代码单元组成的。

在 UTF-16 下，由于 16 位长度只能表示 65536 个字符，所以就默认映射所有在 BMP 范围内的字符，由此 U+D800 ~ U+DFFF 这个部分就留空了，那么辅助平面的字符也就能借助这个留空的部分来表达。这就是 UTF-16 设计的巧妙之处，在不浪费空间的情况下解决所有字符的编码问题。

那么怎么表达辅助平面的字符呢？其实就是将辅助平面字符的代码点编码为 一对 16 bit 长的代码单元，称之为 代理对(surrogate pair)，而代理对必然落在 BMP 中的 U+D800 ~ U+DFFF 部分。这样就解决了用 16 位的代码单元编码整个 Unicode 字符集的问题。需要注意的是 U+D800 ~ U+DFFF 这个部分我们可以称作 代理区，其中 U+D800 ~ U+DBFF 这个部分称为 高位代理区(前导代理区)，U+DC00 ~ U+DFFF 这个部分称为 低位代理区(后尾代理区)。

下面通过将 U+64321 这个处于辅助平面的字符进行 UTF-16 编码的实例来讲解辅助平面字符的编码方式。

1、首先将这个字符的代码点减去 0x10000，得到长度为 20 bit 的一个值，这个值的范围必然在 0x0000 ~ 0xFFFF之内。

```java
V = 0x64321
Vx= V - 0x10000 = 0x54321  = 0101 0100 0011 0010 0001
```

2、将 Vx 的高位 10 bit 的值作为高位代理的运算基数 Vh，将低位 10 bit 的值作为低位代理的运算基数 Vl。这两个 10 bit 的值的取值范围都必然在 0x0000 ~ 0x3FF 之间。

```java
Vh = 0101 0100 00
Vl = 11 0010 0001
```

3、将 Vh 和 Vl 分别与高位代理区和低位代理区起始位置的代码点进行 按位或 运算，得到的结果就是这个处于辅助平面的字符 U+64321 的 UTF-16 编码。

```java
W1 = 0xD800
   = 1101 1000 0000 0000
W2 = 0xDC00
   = 1101 1100 0000 0000
W1 = W1 | Vh
   = 1101 1000 0000 0000     |       01 0101 0000
   = 1101 1001 0101 0000    = 0xD950
W2 = W2 | Vl
   = 1101 1100 0000 0000     |       11 0010 0001
   = 1101 1111 0010 0001    = 0xDF21
```

4、所以最终 U+64321 这个字符就被编码成了由高位代理和低位代理组成的一个代理对，我们需要同时用 0xD950 和 0xDF21 来表示这个字符。

通过上面的例子我们可以看到，**任何辅助平面内的字符在 UTF-16 下都会被编码为由两个长度为 16 位的代理编码组成的代理对，在程序中表示这个字符时，需要占用的就不再是 16 位的空间，而是 32 位。**



(not-using-char)=

## 不建议在 Java 程序中使用 char 数据类型

经过上面对 Unicode 字符集和 UTF-16 的讲解，我们现在来讨论为什么不建议在 Java 程序中使用 char 数据类型。

**由于 Java 采用的是 16 位的 Unicode 字符集，即 UTF-16，所以在 Java 中 char 数据类型是定长的，其长度永远只有 16 位，char 数据类型永远只能表示代码点在 U+0000 ~ U+FFFF 之间的字符，也就是在 BMP 内的字符。如果代码点超过了这个范围，即使用了增补字符，那么 char 数据类型将无法支持，因为增补字符需要 32 位的长度来存储，我们只能转而使用 String 来存储这个字符。**

```{code-block} java
:caption: "编译器将会报错——字符文字中的字符数过多"

char c1 = '��';
char c2 = '\u64321';
```

如上编写的代码，使用 char 数据类型来保存辅助平面的字符，编译器将会报错 Invalid character constant。

随着互联网用户的不断增多以及互联网语言的不断丰富，用户越来越高频率的在互联网上使用一些特殊字符来表达丰富的语义，而这些字符很有可能是属于辅助平面里的增补字符，所以如果我们使用 char 类型来进行处理，就很有可能减低我们程序的健壮性。

:::{note}

char 数据类型永远只能表示代码点在 U+0000 ~ U+FFFF 之间的字符，也就是在 BMP 内的字符。如果代码点超过了这个范围，即使用了增补字符，那么 char 数据类型将无法支持，因为增补字符需要 32 位的长度来存储。
:::



## String 的细节

### 获取字符串长度

String 是我们在编程时使用的非常多的数据类型，它用来表示一个字符串。查看 String 的源码，我们可以看到其底层实际是使用一个 char 类型数组在存储我们的字符。

```{code-block} java
:caption: "String 的存储是由 char 类型数组实现的"

public final class String
         implements java.io.Serializable, Comparable<String>, CharSequence {
   /** The value is used for character storage. */
   private final char value[];

   //...
}
```

我们也知道调用其 length() 方法可以得到字符串的长度，即字符串中字符的数量。其实现是直接返回底层 value 数组的长度，代码如下：

```{code-block} java
:caption: "String.length()的实现"

/**
   * Returns the length of this string.
   * The length is equal to the number of Unicode code units in the string.
   *
   * @return  the length of the sequence of characters represented by this object.
   */
   public int length() {
      return value.length;
   }
```

结合我们上面对于字符编码的知识，我们知道 Java 中 char 的长度永远是 16 位，如果我们在字符串中使用了增补字符，那就意味着需要 2 个 char 类型的长度才能存储，对于 String 底层存储字符的数组 value 来说，就需要 2 个数组元素的位置。所以下面的这个程序我们将得到一个意料之外的结果：

```{code-block} java
:caption: "�� 字符的测试"

String tt = "我喜欢��这个字符";
System.out.println(tt.length()); // 9
```

按照我们的想法，字符串 tt 中应该只有 8 个字符，然而实际输出却是 9 个。上面我们已经讲过 Java 采用的是 16 位的 Unicode 字符集，所以在 Java 中一个代码单元的长度也是 16 位。一个增补字符需要两个代码单元来表示，所以 tt 字符串中的字符 �� 需要占用 value 数组的两个位置，这就是输出 9 而不是 8 的原因。

这里就体现了 Java 中 char 类型无法表示一个增补字符的问题。其实我们仔细阅读 length() 方法上的注释也可以知道，这个方法返回的是这个字符串中 Unicode 代码单元的数量。

那么有没有什么办法能够获取到我们想要的 8 呢？我们可以调用 codePointCount(int beginIndex, int endIndex) 这个方法来实现。顾名思义，这个方法返回的是字符串中指定部分的代码点的数量，不管你是处于 BMP 范围内的字符还是辅助平面的字符，你的代码点都只能是一个，所以这就可以精确的得到字符串中的字符数量，我们来看这个方法的实现：

```java
public int codePointCount(int beginIndex, int endIndex) {
      if (beginIndex < 0 || endIndex > value.length || beginIndex > endIndex) {
         throw new IndexOutOfBoundsException();
      }
      return Character.codePointCountImpl(value, beginIndex, endIndex - beginIndex);
   }
```

这个方法首先是判断传入的范围是否合法，然后调用 java.lang.Character 的 static int codePointCountImpl(char\[\] a, int offset, int count) 方法进行代码点计算，我们来看具体实现：

```java
static int codePointCountImpl(char[] a, int offset, int count) {
      int endIndex = offset + count;
      int n = count;
      for (int i = offset; i < endIndex; ) {
         if (isHighSurrogate(a[i++]) && i < endIndex && isLowSurrogate(a[i])) {
            n--;
            i++;
            }
      }
      return n;
   }
```

这个方法默认返回的是传入的指定的字符串的长度，也就是说默认字符串中每个字符都是 BMP 中的字符。接下来的 for 循环里就是核心逻辑，依次判断字符串中的第 n 个字符和 n+1 个字符是否分别落在高位代理区和低位代理区。如果满足判断条件，则默认返回的字符总数减一。

因为如果第 n 个字符和 n+1 个字符分别落在高位代理区和低位代理区就表示这是一个增补字符，增补字符占用两个代码单元，所以需要将默认返回的字符总数减一，这样得到的才是真正的字符总数。
