# 对IO流的多重封装的使用的理解

## java IO 流介绍

以下是java的基本IO流：

```{image} ../../../img/java/network/java-basic-io-stream.png
:alt: java basic io stream
```
 
举例子，我们在对一个文件进行数据读取时，使用的是FileInputStream,但是使用该类获取的数据是字节流/二进制流，我们在读取文件数据时只能通过字节来读取；如果希望提高读取效率可以使用BufferedInputStream作为二级流，对输入缓冲流提供更多控制。当然，如果希望直接从文件中返回各种基本类型的数据，可以使用DataInputStream作为三级流。

```{image} ../../../img/java/network/io-stream-reader.png
:alt: io stream read
```

```java
//构建文件输入流
DataInputStream in=new DataInputStream(new BufferedInputStream(new FileInputStream()));
```

:::{note}

多重封装的好处是提高程序效率；在网络通讯程序中，字符流对一句话的传输比字节流一个字节一个字节得传输要好，有缓冲得BufferedInputStream要比没有缓冲的InputStream要好。以上三重封装适用于文本以及文本文件的传输，对于非文本文件的传输需要另外考虑。
:::
 
## FileOutputStream与ObjectOutputStream的组合理解

For example to write an object that can be read by the example inObjectInputStream:

```java
FileOutputStream fos = new FileOutputStream("t.tmp");
ObjectOutputStream oos = new ObjectOutputStream(fos);

oos.writeInt(12345);
oos.writeObject("Today");
oos.writeObject(new Date());

oos.close();
```

new FileOutputStream("t.tmp")创建的是一个文件流，所有通过该对象进行写操作的数据都将写入t.tmp文件中。

上文代码块可理解为：通过ObjectOutputStream对象把对象数据写入文件t.tmp中，即创建ObjectOutputStream对象的同时，确定了通过该对象进行的写操作的数据流是流向FileOutputStream对象的。

:::{note}

通过API文档可知，ObjectOutputStream类的构造函数有两个，分别为有参和无参。

其中,无参构造函数即 `ObjectOutputStream()` 是为完全重新实现ObjectOutputStream的子类提供一种方法，实际上是不能无参生成对象输出流对象的。

有参构造函数即 `ObjectOutputStream(OutputStream out)` 创建一个写入指定的OutputStream的ObjectOutputStream。
:::

## ByteArrayOutputStream与ObjectOutputStream的组合理解

```{literalinclude} ../example_java/extend/Translate.java
:language: java
```

:::{note}

通过API文档可知，ByteArrayOutputStream类实现了将数据写入字节数组的输出流。 当数据写入缓冲区时，缓冲区会自动增长。
:::
 
## 小结

对于一个OutputStream/InputStream 类及其子类，如果其类对象拥有缓冲区/文件空间，那么这种类型的流对象可以作为IO流多重封装的最内层。
