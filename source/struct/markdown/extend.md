# Markdown扩展语法学习

```{seealso}

Markdown 是可以通过 [`markdown-it-py`](https://markdown-it-py.readthedocs.io/en/latest/index.html) 来扩展语法。因为本项目的 Markdown 解析器是 MyST-NB (依赖 MyST )，相关的 Markdown 语法扩展的添加可以前往 {ref}`可选的 MyST 扩展语法 <myst-opational-syntax>` 查看。

下文中 {ref}`定义清单 <markdown-deflist-syntax>` 和 {ref}`任务清单 <markdown-tasklist-syntax>` 以及 {ref}`自动识别网址链接 <markdown-url-syntax>` 都是通过 {ref}`可选的 MyST 扩展语法 <myst-opational-syntax>` 实现的。
```

## 表格

要添加表，请使用三个或多个连字符（`---`）创建每列的标题，并使用管道（`|`）分隔每列。您可以选择在表的任一端添加管道。

```
| Syntax    | Description |
| --------- | ----------- |
| Header    | Title       |
| Paragraph | Text        |
```

呈现的输出如下所示：

| Syntax    | Description |
| --------- | ----------- |
| Header    | Title       |
| Paragraph | Text        |


>  **提示：** 使用连字符和管道创建表可能很麻烦。为了加快这一过程，请尝试使用Markdown Tables Generator。使用图形界面构建表，然后将生成的Markdown格式的文本复制到文件中。当然也可以直接使用  Typora 编辑器，该编辑提供了表格的快速创建和编辑功能。

### 格式化表格中的文字

您可以格式化表格中的文本。例如，您可以添加[链接](http://markdown.p2hp.com/basic-syntax/index.html#links)，[代码](http://markdown.p2hp.com/basic-syntax/index.html#code-1)（```仅在刻度线（）中显示单词或短语，而不能在[代码块中添加](http://markdown.p2hp.com/basic-syntax/index.html#code-blocks)）和[强调](http://markdown.p2hp.com/basic-syntax/index.html#emphasis)。

您不能添加标题，块引用，列表，水平规则，图像或HTML标签。


----

## 围栏代码块 

```{seealso}
由于此电子书是基于 MyST Parser 来解析的，所以其代码高亮是适用 pygments 实现的； [点击查看关于代码高亮 pygments 支持的语言](https://pygments.org/languages/)。
```

Markdown基本语法允许您通过将行缩进四个空格或一个制表符来创建代码块。如果发现不方便，请尝试使用受保护的代码块。根据Markdown处理器或编辑器的不同，您将在代码块之前和之后的行上使用三个刻度线（```` ``` ````）或三个波浪号（~~~）。如果想要包含一个含有三个刻度线（```），可以使用四个刻度： 

:::markdown

```` ``` ````

:::

    ```
    {
    "firstName": "John",
    "lastName": "Smith",
    "age": 25
    }
    ```

呈现的输出如下所示：

:::{card}

```
{
  "firstName": "John",
  "lastName": "Smith",
  "age": 25
}
```

:::

### 语法高亮

许多Markdown处理器都支持围栏代码块的语法突出显示。此功能使您可以为代码编写时使用的任何语言添加颜色突出显示。要添加语法突出显示，请在受防护的代码块之前的对号旁指定一种语言。

~~~markdown
```json
{
  "firstName": "John",
  "lastName": "Smith",
  "age": 25
}
```
~~~

呈现的输出如下所示：

:::{card}

```json
{
  "firstName": "John",
  "lastName": "Smith",
  "age": 25
}
```

:::

## 脚注

脚注使您可以添加注释和参考，而不会使文档正文混乱。创建脚注时，带有脚注引用的链接将出现带有链接的上标编号。读者可以单击链接跳至页面底部的脚注内容。

要创建脚注参考，请在方括号（`[^1]`）内添加插入符号和标识符。标识符可以是数字或文字，但他们不能包含空格或制表符。标识符仅将脚注参考与脚注本身相关联-在输出中，脚注按顺序编号。

在括号内使用另一个插入符号和数字添加脚注，并用冒号和文本（`[^1]: My footnote.`）括起来。您不必在文档末尾添加脚注。你可以把他们的任何地方，除了像列表一样，块报价，和表格等元素里面。

```
Here's a simple footnote,[^1] and here's a longer one.[^bignote]

[^1]: This is the first footnote.

[^bignote]: Here's one with multiple paragraphs and code.

    Indent paragraphs to include them in the footnote.

    `{ my code }`

    Add as many paragraphs as you like.
```

呈现的输出如下所示：


Here's a simple footnote,[^1] and here's a longer one.[^bignote]

----

(markdown-deflist-syntax)=

## 定义清单

一些Markdown处理器允许您创建*自定义列表*和术语及其相应的定义。要创建定义列表，请在第一行上键入术语。下一行，键入一个冒号后跟一个空格和定义。

```
First Term
: This is the definition of the first term.

Second Term
: This is one definition of the second term.
: This is another definition of the second term.
```

> 运行效果：

:::{card}

First Term
: This is the definition of the first term.

Second Term
: This is one definition of the second term.
: This is another definition of the second term.

:::

## 删除线

您可以通过在单词中心放置一条水平线来“删除”单词。结果看起来~~像这样~~。此功能使您可以指示某些单词是一个错误，并不表示要包含在文档中。若要删除单词，请`~~`在单词前后使用两个波浪号（）。

```
~~The world is flat.~~ We now know that the world is round.
```

呈现的输出如下所示：

~~The world is flat.~~ We now know that the world is round.


----

(markdown-tasklist-syntax)=

## 任务清单

任务列表使您可以创建带有复选框的项目列表。在支持任务列表的Markdown应用程序中，复选框将显示在内容旁边。要创建任务列表，请在任务列表项之前添加破折号（`-`）和方括号，并`[ ]`在其前面加上一个空格（）。要选择一个复选框，请`x`在方括号（`[x]`）之间添加in 。

```
- [x] Write the press release
- [ ] Update the website
- [ ] Contact the media
```

> 呈现的输出如下所示：

:::{card}

- [x] Write the press release
- [ ] Update the website
- [ ] Contact the media

:::

(markdown-url-syntax)=

## 自动识别网址链接

许多Markdown处理器会自动将URL转换为链接。这意味着如果您输入http://www.example.com，即使您没有[使用方括号](http://markdown.p2hp.com/basic-syntax/index.html#links)，您的Markdown处理器也会自动将其转换为链接。

这个功能需要使用到 Markdown 的扩展 [linkify-it-py](https://github.com/tsutsu3/linkify-it-py)。要么直接 `pip install linkify-it-py` 或通过 `pip install myst-parser[linkify]` 安装 Python 模块。 相关笔记可前往笔记—— {ref}`可选的 MyST 扩展语法中的链接扩展语法的开启和使用 <markdown-ext-syntax-linkify>`

```
http://www.example.com
```

呈现的输出如下所示：

http://www.example.com

### 禁用自动URL链接

如果您不希望自动链接URL，则可以通过[将URL表示为](http://markdown.p2hp.com/basic-syntax/index.html#code)带有刻度线的[代码](http://markdown.p2hp.com/basic-syntax/index.html#code)来删除该链接。

```
`http://www.example.com`
```

呈现的输出如下所示：

`http://www.example.com`


[^1]: This is the first footnote.

[^bignote]: Here's one with multiple paragraphs and code.

    Indent paragraphs to include them in the footnote.
    
    `{ my code }`
    
    Add as many paragraphs as you like.
