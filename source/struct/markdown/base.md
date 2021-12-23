# Markdown基础语法学习 (1)

## 标题

要创建标题，请在单词或短语的前面添加一定数量的 `#` 符号。（符号数量在1~6，一般来说4级标题足以应对）

| Markdown                 | HTML                       |
| :----------------------- | -------------------------- |
| `# Heading level 1`      | `<h1>Heading level 1</h1>` |
| `## Heading level 2`     | `<h2>Heading level 2</h2>` |
| `### Heading level 3`    | `<h3>Heading level 3</h3>` |
| `#### Heading level 4`   | `<h4>Heading level 4</h4>` |
| `##### Heading level 5`  | `<h5>Heading level 5</h5>` |
| `###### Heading level 6` | `<h6>Heading level 6</h6>` |

---

## 段落

要创建段落，请使用空白行分隔一行或多行文本。您不应缩进带有空格或制表符的段落。

```
我真的很喜欢使用Markdown。

我想从现在开始，我将使用它来格式化所有文档。
```

> 下方为段落示例代码的渲染输出

我真的很喜欢使用Markdown。  

我想从现在开始，我将使用它来格式化所有文档。

## 换行

要创建换行符（`<br>`），请以 **两个或多个空格结束一行，然后键入return**。

```
This is the first line.  
And this is the second line.
```

> 下方为换行示例代码的渲染输出

This is the first line.  
And this is the second line.

## 字体

要加粗文本，请在单词或短语的前后添加两个星号或下划线。要加粗一个单词的中部以强调，请在字母周围添加两个星号，且各空格之间不加空格。Markdown 可以使用以下几种字体：

```
*斜体文本*
_斜体文本_
**粗体文本**
__粗体文本__
***粗斜体文本***
___粗斜体文本___
```

> 下方为字体示例代码的渲染输出

*斜体文本*  
_斜体文本_  
**粗体文本**  
__粗体文本__  
***粗斜体文本***  
___粗斜体文本___

## 块引用

要创建 blockquote，请`>`在段落前面添加一个。

```
> Dorothy followed her through many of the beautiful rooms in her castle.
```

呈现的输出如下所示：

> Dorothy followed her through many of the beautiful rooms in her castle.

### 多个段落块引用

块引用可以包含多个段落。段落之间的空白行上添加一个 `>`。

```
> Dorothy followed her through many of the beautiful rooms in her castle.
>
> The Witch bade her clean the pots and kettles and sweep the floor and keep the fire fed with wood.
```

呈现的输出如下所示：

> Dorothy followed her through many of the beautiful rooms in her castle.
>
> The Witch bade her clean the pots and kettles and sweep the floor and keep the fire fed with wood.

### 嵌套块引用

块引用可以嵌套。>>在要嵌套的段落前面添加一个。

```
> Dorothy followed her through many of the beautiful rooms in her castle.
>
>> The Witch bade her clean the pots and kettles and sweep the floor and keep the fire fed with wood.
```

呈现的输出如下所示：

> Dorothy followed her through many of the beautiful rooms in her castle.
>
>> The Witch bade her clean the pots and kettles and sweep the floor and keep the fire fed with wood.

### 具有其他元素的块引用

块引用可以包含其他Markdown格式的元素。并非所有元素都可以使用-您需要进行实验以查看哪些元素有效。

```
> #### The quarterly results look great!
>
> - Revenue was off the chart.
> - Profits were higher than ever.
>
>  *Everything* is going according to **plan**.
```

呈现的输出如下所示：

> #### 季度业绩看起来不错！
>
> - 收入超出了预期。
> - 利润比以往任何时候都高。
>
> *一切*都按**计划进行**。

### 有序列表

要创建有序列表，请在订单项中添加数字和句点。**数字不必按数字顺序排列，但列表应以数字开头。**

```
1. First item
8. Second item
3. Third item
5. Fourth item
1. First item
2. Second item
3. Third item
    1. Indented item
    2. Indented item
4. Fourth item
```

> 上方有序列表呈现的输出如下所示

1. First item
8. Second item
3. Third item
5. Fourth item
1. First item
2. Second item
3. Third item
    1. Indented item
    2. Indented item
4. Fourth item

### 无序列表

要创建无序列表，请在订单项前添加破折号（`-`），星号（`*`）或加号（`+`）。缩进一个或多个项目以创建嵌套列表。

```
* First item
* Second item
* Third item
    * Indented item
    * Indented item
* Fourth item
```

> 上方无序列表呈现的输出如下所示

* First item
* Second item
* Third item
    * Indented item
    * Indented item
* Fourth item

### 在列表中添加元素

要在保留列表连续性的同时在列表中添加另一个元素，请将该元素缩进四个空格或一个制表符，如以下示例所示。

```
* This is the first list item.

     > A blockquote would look great below the second list item.

* Here's the second list item.

    I need to add another paragraph below the second list item.

* And here's the third list item.

    <head>
        <title>Test</title>
    </head>

* And here's the fourth list item.

    ![tux.png](./example/tux.png)

* And here's the fifth list item.
```

呈现的输出如下所示：

* This is the first list item.

    > A blockquote would look great below the second list item.

* Here's the second list item.

    I need to add another paragraph below the second list item.

* And here's the third list item.

    ```html
    <head>
        <title>Test</title>
    </head>
    ```

* And here's the fourth list item.

    ![tux.png](./example/tux.png)

* And here's the fifth list item.

## 代码

要将单词或短语表示为代码，请将其括在勾号（```）中。

```
At the command prompt, type `nano`.
```

呈现的输出如下所示：

At the command prompt, type `nano`.

### 转义刻度线

如果要表示为代码的单词或短语包含一个或多个刻度线，可以通过将单词或短语括在双刻度线（````）中来对其进行转义。

```
``Use `code` in your Markdown file.``
```

呈现的输出如下所示：

``Use `code` in your Markdown file.``

### 代码块

要创建代码块，请在代码块的每一行缩进至少四个空格或一个制表符。

```
    <head>
        <title>Test</title>
    </head>
```

呈现的输出如下所示：

    <head>
        <title>Test</title>
    </head>

> 扩展语法中有代码块的扩展语法 围栏代码块。

## 链接

要创建链接，请将链接文本括在方括号（例如`[Duck Duck Go]`）中，然后立即在URL后面加上括号（例如`(https://duckduckgo.com)`）中的URL 。

```
My favorite search engine is [Duck Duck Go](https://duckduckgo.com).
```

呈现的输出如下所示：

My favorite search engine is [Duck Duck Go](https://duckduckgo.com).

### 添加标题

您可以选择为链接添加标题。当用户将鼠标悬停在链接上时，这将显示为工具提示。要添加标题，请将其括在URL后面的括号中。

```
My favorite search engine is [Duck Duck Go](https://duckduckgo.com "The best search engine for privacy").
```

呈现的输出如下所示：

My favorite search engine is [Duck Duck Go](https://duckduckgo.com "The best search engine for privacy").

### 网址和电子邮件地址

要将URL或电子邮件地址快速转换为链接，请将其括在尖括号中。

```
<https://markdown.p2hp.com>

<fake@example.com>
```

呈现的输出如下所示：

<https://markdown.p2hp.com>

<fake@example.com>

### 格式化链接

为了[强调](http://markdown.p2hp.com/basic-syntax/index.html#emphasis)链接，请在方括号和括号之前和之后添加星号。

```
I love supporting the **[EFF](https://eff.org)**.

This is the *[Markdown Guide](https://markdown.p2hp.com)*.
```

呈现的输出如下所示：

I love supporting the **[EFF](https://eff.org)**.

This is the *[Markdown Guide](https://markdown.p2hp.com)*.

### 引用样式链接

引用样式链接是一种特殊的链接，它使URL在Markdown中更易于显示和阅读。引用样式的链接分为两部分：与文本保持内联的部分以及在文件中其他位置存储的部分，以使文本易于阅读。

```
In a hole in the ground there lived a hobbit. Not a nasty, dirty, wet hole, filled with the ends
of worms and an oozy smell, nor yet a dry, bare, sandy hole with nothing in it to sit down on or to
eat: it was a [hobbit-hole][1], and that means comfort.

[1]: <https://en.wikipedia.org/wiki/Hobbit#Lifestyle> "Hobbit lifestyles"
```

呈现的输出如下所示：

In a hole in the ground there lived a hobbit. Not a nasty, dirty, wet hole, filled with the ends of worms and an oozy smell, nor yet a dry, bare, sandy hole with nothing in it to sit down on or to eat: it was a [hobbit-hole][1], and that means comfort.

[1]: <https://en.wikipedia.org/wiki/Hobbit#Lifestyle> "Hobbit lifestyles"

---

## 图片

要添加图像，请添加感叹号（`!`），然后在括号中添加替代文本，并在括号中添加图像资源的路径或URL。您可以选择在括号中的URL之后添加标题。

> **注意：** 使用Markdown并不意味着您也不能使用HTML。可以将HTML标签添加到任何Markdown文件中。如果您更喜欢某些HTML标记而不是Markdown语法，这将很有帮助。例如，将HTML标签用于图像更容易调整图片。当然，我们需要添加 markdown-it-py 扩展配置，配置方法参考 {ref}`可选的 MyST 扩展语法 <myst-opational-syntax>` 的 {ref}`MyST 提供的几种不同的语法来在文档中包含图像 <myst-optional-syntax-img>`

```
![tux.png](./example/tux.png)

<img src="./example/tux.png" alt="tux.png" style="zoom:33%;" />
```

![tux.png](./example/tux.png)

<img src="./example/tux.png" alt="tux.png" style="zoom:33%;" />

## 水平线

要创建水平线`***`，请单独在一行上使用三个或更多的星号（），破折号（`---`）或下划线（`___`）

---

## 转义字符

要显示原义字符，否则将用于设置Markdown文档中的文本格式`\`，请在字符前面添加反斜杠（）。

```
\* Without the backslash, this would be a bullet in an unordered list.
```

呈现的输出如下所示：

\* 如果没有反斜杠，这将是无序列表中的项目符号。

### 可以使用反斜杠转义以下字符

| 字符 | 名称                                                                                                                     |
| :--- | ------------------------------------------------------------------------------------------------------------------------ |
| \    | 反斜杠                                                                                                                   |
| `    | 刻度线（另请参见[转义刻度线中的代码](http://markdown.p2hp.com/basic-syntax/index.html#escaping-tick-marks)）             |
| *    | 星号                                                                                                                     |
| _    | 下划线                                                                                                                   |
| {}   | 大括号                                                                                                                   |
| []   | 中括号                                                                                                                   |
| ()   | 括号                                                                                                                     |
| #    | 井号                                                                                                                     |
| +    | 加号                                                                                                                     |
| -    | 减号（连字符）                                                                                                           |
| .    | 点                                                                                                                       |
| !    | 感叹号                                                                                                                   |
| \|   | 管道（另请参见表中的[转义管道](http://markdown.p2hp.com/extended-syntax/index.html#escaping-pipe-characters-in-tables)） |
