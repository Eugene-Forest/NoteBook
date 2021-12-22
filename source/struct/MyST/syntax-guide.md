(myst-syntax-guide)=

# MyST 语法指南

指令语法是用三重反引号和花括号定义的。它实际上是一个用大括号括住语言的代码块，以及代替语言名称的指令名称。它类似于 RMarkdown 定义“可运行单元格”的方式。这是基本结构：

`````{list-table}
---
header-rows: 1
---
* - MyST 写法 1
  - MyST 写法 2
  - reStructuredText
* - ````
    ```{directivename} arguments
    ---
    key1: val1
    key2: val2
    ---
    This is
    directive content
    ```
    ````
  - ````
    ```{directivename} arguments
    :key1: val1
    :key2: val2

    This is
    directive content
    ```
    ````
  - ```rst
    .. directivename:: arguments
       :key1: val1
       :key2: val2

       This is
       directive content
    ```
`````

## MyST Markdown 指令的两种写法

使用 YAML frontmatter
: 指令第一行之后的 YAML 前言块将被解析为指令的选项。这需要用 `---` 线包围。两者之间的所有内容都将由 YAML 解析并作为关键字参数传递给您的指令。
: 如果您的指令有很多选项，或者有一个非常长的值（例如，跨越多行），那么您还可以将选项包装在行中 `---` 并将它们写为 YAML。

    ````
    ```{code-block} python
    ---
    lineno-start: 10
    emphasize-lines: 1, 3
    caption: |
        This is my
        multi-line caption. It is *pretty nifty* ;-)
    ---
    a = 2
    print('my 1st line')
    print(f'my {a}nd line')
    ```
    ````

    ```{code-block} python
    ---
    lineno-start: 10
    emphasize-lines: 1, 3
    caption: |
        This is my
        multi-line caption. It is *pretty nifty* ;-)
    ---
    a = 2
    print('my 1st line')
    print(f'my {a}nd line')
    ```

带有 `:` 字符的简写选项
: 这种写法最接近 reST 语法，无论读者是否在学习 MyST Markdown 之前有关学习 reST 标记语言，笔者个人都推荐使用这种语法，因为这样可以使得我们能够快速切换两种语言的指令的写法。

    ````
    ```{code-block} python
    :lineno-start: 10
    :emphasize-lines: 1, 3

    a = 2
    print('my 1st line')
    print(f'my {a}nd line')
    ```
    ````

    ```{code-block} python
    :lineno-start: 10
    :emphasize-lines: 1, 3

    a = 2
    print('my 1st line')
    print(f'my {a}nd line')
    ```

```{admonition} MyST Markdown 与 reST 标记语言的切换
由本文章开篇第一部分的 MyST Markdown 写法2 与 reST 比较可知，reST 标记语言的原生指令甚至是 [扩展指令](./../extend/ext-index.md) 都是可以和在 MyST Markdown 和 reST 两个语言中相互切换使用的。
```

(syntax/guide/parsing)=

## 指令如何解析指令内容

MyST 将指令内容解析为 Markdown。这意味着 MyST markdown 可以写在任何用 MyST markdown 编写的指令的内容区域中。

````
```{admonition} My markdown link
Here is [markdown link syntax](https://jupyter.org)
```
````

````{card}
> 运行渲染结果：

```{admonition} My markdown link
Here is [markdown link syntax](https://jupyter.org)
```
````

(myst-syntax-guide-eval-rst)=

### eval-rst 指令

对于特殊情况，MySt 还提供 `eval-rst` 指令。这会将内容解析为 **ReStructuredText**：

````
```{eval-rst}
.. figure:: img/fun-fish.png
  :width: 100px
  :name: rst-fun-fish

  Party time!

A reference from inside: :ref:`rst-fun-fish`

A reference from outside: :ref:`syntax/guide/parsing`
```
````

````{card}
```{eval-rst}
.. figure:: img/fun-fish.png
  :width: 100px
  :name: rst-fun-fish

  Party time!

A reference from inside: :ref:`rst-fun-fish`

A reference from outside: :ref:`syntax/guide/parsing`
```
````

当然，我们还可以通过 `eval-rst 指令` 实现 {ref}`myst-md-include-rst`。

## 嵌套指令

您可以通过**确保与最外层指令对应的刻度线长于内部指令的刻度线**来嵌套指令。例如，在注释块中嵌套警告，如下所示：

``````{list-table}
:header-rows: 1

* - MyST Markdown
  - 渲染结果
* - `````
    ````{note}
    The next info should be nested
    ```{warning}
    Here's my warning
    ```
    ````
    `````
  - ````{note}
    The next info should be nested
    ```{warning}
    Here's my warning
    ```
    ````
``````

```{note}
只要保证最外层指令对应的刻度线长于内部指令的刻度线，那么指令可以一直嵌套（虽然没有必要），就已上方的语法和渲染结果的对比来说，笔者使用了六个 ``` ` ``` 来包裹内容。

如果您想在 Markdown 中显示反引号，可以通过将它们嵌套在更长的反引号中来实现。Markdown 会将最外面的反引号视为“原始”块的边缘，里面的所有内容都会显示出来。
```

``````{dropdown}
:color: info
:animate: fade-in-slide-down

可以缩进内部代码围栏，只要它们的缩进不超过 3 个空格就可以被渲染。否则，它们将被呈现为代码块：

`````
````{note}
The warning block will be properly-parsed

   ```{warning}
   Here's my warning
   ```

But the next block will be parsed as raw text

    ```{warning}
    Here's my raw text warning that isn't parsed...
    ```
````
`````

````{note}
The warning block will be properly-parsed

   ```{warning}
   Here's my warning
   ```

But the next block will be parsed as raw text

    ```{warning}
    Here's my raw text warning that isn't parsed...
    ```
````
``````

## Markdown 友好指令

想使用在标准 Markdown 编辑器中正确呈现的语法吗？请参阅 {ref}`扩展语法选项 <markdown-ext-syntax-colon>`。

```
:::{note}
This text is **standard** _Markdown_
:::
```

:::{note}
This text is **standard** _Markdown_
:::

## 角色

角色类似于指令——它们允许您定义任意的新功能，但它们是内嵌使用的。要定义内联角色，请使用以下形式：

````{list-table}
---
header-rows: 1
---
* - MyST
  - reStructuredText
* - ````
    {role-name}`role content`
    ````
  - ```rst
    :role-name:`role content`
    ```
````

例如，下面的代码:

```
Since Pythagoras, we know that {math}`a^2 + b^2 = c^2`
```

> 运行渲染得:

Since Pythagoras, we know that {math}`a^2 + b^2 = c^2`

## 额外的 MyST Markdown 语法

该表描述了rST和MyST的等价项:

````{list-table}
---
header-rows: 1
---
* - Type
  - MyST
  - reStructuredText
* - Math shortcuts
  - `$x^2$`
  - N/A
* - 指令可选项
  - ```
    ---
    key: val
    ---
    ```
  - ```
    :key: val
    ```
* - 注释
  - `% comment`
  - `.. comment`
* - label 标签
  - `(mytarget)=`
  - `.. _mytarget:`
````

(myst-syntax-guide-target)=

## 目标和交叉引用

目标用于定义您可以在文档中的其他地方引用的自定义锚点。它们通常放在章节标题之前，以便您可以轻松地参考它们。

在 MyST Markdown 中，目标标头使用以下语法定义：

```
(header_target)=
```

然后可以使用 [ref 内联角色引用](https://www.sphinx-doc.org/en/master/usage/restructuredtext/roles.html#role-ref)它们：

:::md
{ref}`header_target`
:::

默认情况下，引用将使用目标的文本（例如部分标题），但您也可以直接指定文本：

:::md
{ref}`my text <header_target>`
:::

例如，请参阅此参考：{ref}`myst-syntax-guide-target`，这是返回此页面顶部的参考：{ref}`返回顶部 <myst-syntax-guide>`。

### 使用 Markdown 的链接语法

```
[my text](header_target)
```

如果您希望将目标的标题插入到您的文本中，您可以将 Markdown 链接的“文本”部分留空。例如，这个 markdown: `[](header.md)` 。

```
    [](./optional-syntax.md)

    [](myst-opational-syntax)
```

> 运行效果如下所示：

[](./optional-syntax.md)

[](myst-opational-syntax)

## 注释

您可以通过将%字符放在行首来添加注释。这将防止该行被解析为输出文档。

例如，这段代码：

```
% my comment
```

在下面，但它不会被解析到文档中。

% my comment

````{seealso}
MyST Markdown 依旧遵循原来 Markdown 语法，所以 Markdown 的注释语法对 MyST Markdown 起作用。

例如，这段代码：

```
<!-- my comment -->
```

在下面，但它不会被解析到文档中。

<!-- my comment -->

````

````{important}
由于注释是块级实体，它们将终止前一个块。实际上，这意味着以下几行将分成两段，从而在它们之间产生新的一行：

```
a line
% a comment
another line
```

a line
% a comment
another line
````

## 块中断

您可以通过放置+++在一行的开头来添加块中断。该构造的预期用例是映射到基于单元格的文档格式，如jupyter notebooks，以指示新的文本单元格。它不会出现在呈现的文本中，而是存储在内部文档结构中供开发人员使用。

例如，这段代码：

```
+++ some text
```

在下面，但它不会被解析到文档中。

+++ some text

