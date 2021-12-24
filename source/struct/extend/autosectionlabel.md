# autosectionlabel

```{attention}
`v0.13.0`✨ 中的新功能，myst-parser 现在提供了一个单独的 `autosectionlabel` 实现，它实现了 GitHub Markdown 风格的书签锚，比如`[](file.md#header-anchor)`.
```

<!-- 如果对此界面的标签进行修改，需要对此笔记引用的 html 标签结构进行修改，同时还需要注意此行为产生的此界面的部分链接的失效。 -->

## activate autosectionlabel

将以下内容添加到您的 `conf.py` 文件中，在您的 Sphinx 中激活它：

```python
extensions = [
    'sphinx.ext.autosectionlabel',
]

# Prefix document path to section labels, to use:
# `path/to/file:heading` instead of just `heading`
autosectionlabel_prefix_document = True
```

当然，激活 `autosectionlabel` 后也可以同时使用一般的 `label` 标签。

## 自动为节标题创建目标

此扩展程序允许您引用其标题的部分。

例如：

```rest
A Plain Title
-------------

This is the text of the section.

It refers to the section title, see :ref:`A Plain Title`.
```

在内部，此扩展为每个部分生成标签。如果在整个文档中使用相同的部分名称，则默认情况下使用任何一个作为目标；不过正常来说我们肯定是不希望如此的，所以我们可以使用 `autosectionlabel_prefix_document` 配置变量，它可以使的不同文件下可以有相同的标签，需要注意的是这个标签在一个文件中是唯一的。

## 配置

autosectionlabel_prefix_document
: 如果值为 `True` ， 用它所在的文档的名称作为每个部分标签的前缀，后跟一个冒号。例如，`index:Introduction` 对于 `Introduction` 出现在文档中的名为的部分 `index.rst`。当相同的部分标题出现在不同的文档中时，可用于避免歧义。

autosectionlabel_maxdepth
: 如果设置此配置， `autosectionlabel` 将按深度选择要标记的部分。例如，当设置 `autosectionlabel_maxdepth = 1` 时，只为顶层部分生成标签，而不标记更深的部分。它默认为`None`（禁用）。

## 在 MyST Markdown 中使用 autosectionlabel

```md
{ref}`struct/extend/autosectionlabel:activate autosectionlabel`

{ref}`struct/extend/autosectionlabel:配置`

[标签 activate-autosectionlabel](#activate-autosectionlabel)

[标签 rstautosectionlabel](./autosectionlabel.html#rstautosectionlabel)
```

> 运行渲染效果如下：

```{card}
{ref}`struct/extend/autosectionlabel:activate autosectionlabel`

{ref}`struct/extend/autosectionlabel:配置`

[标签 activate-autosectionlabel](#activate-autosectionlabel)

[标签 rstautosectionlabel](./autosectionlabel.html#rstautosectionlabel)
```

我们在使用 `ref` 来表示内部链接时的两种写法：
* ``` {ref}`struct/extend/autosectionlabel:配置` ``` ： 以文档根目录（`source`文件夹下开始为根）为起点，以路径唯一地确认到一个文件，并用冒号来指向文件中的一个标题。
* ``` {ref}`title <label-name>` ``` ： 直接在尖括号中填写 label 标签名，在 title 中添加表示内部链接的文本。

我们在以 Markdown 链接语法 `[]()` 来表示内部链接时：
* `[标签 activate-autosectionlabel](#activate-autosectionlabel)` ：文件内的链接可以直接通过这个方式表示。
* `[标签 rstautosectionlabel](./autosectionlabel.html#rstautosectionlabel)` ： 文件外的链接可以直接使用相对路径来表示。当然，我们会发现文件名后缀为 html，但是我们实际的源码文件的后缀是 md ，这是因为我们的构建产生的文档是html的。

MyST Markdown 与 RST 的写法中不同的在于前者需要明确指出文件类型，而且还是最终生成文件的类型；但是后者只需要文件名。

需要注意的是，一般来说，我们的构建产生的文档是html的。

## 在RST中使用autosectionlabel

```{eval-rst}
.. include:: ./autoselect.rst
```

## autosectionlabel 自动创建锚点的规律

我们可以通过查看此界面的html文件的标题索引：

```{literalinclude} ./example/example.html
:caption: 此界面的html文件的标题索引
:language: html
:linenos:
```

我们可以发现：

* 对于中文标题
  * `autosectionlabel` 是没有办法识别的，所以它会自动以 `id + 数字` 编排 `label` ；例如本文中的 {ref}`struct/extend/autosectionlabel:自动为节标题创建目标` 标题。
* 如果是中英文混搭的标题
  * 那么它将会只识别英文；然后便是参考下一级的规律编排 `label`。例如本文中的 {ref}`struct/extend/autosectionlabel:在RST中使用autosectionlabel` 标题。
* 对于英文标题
  * 如果是一个单词，那么这个单词会作为 `label` ，如果是多个单词（一般都是以空格间隔），那么单词之间以 `-` 相连作为此标题的 `label` ；例如本文中的 {ref}`struct/extend/autosectionlabel:activate autosectionlabel` 标题。
  * 如果发现在此文件中已经存在相同的 `label` ，那么除了第一个是有效的之外，其他的都是无效的需要重新以 `id + 数字` 编排 `label`的； 例如本文中的 {ref}`struct/extend/autosectionlabel:autosectionlabel 自动创建锚点的规律` 标题。

## 自动为节标题创建标签的另一种实现 myst-anchors

> 由于 myst-anchors 与 autosectionlabel 会相互冲突，所以没有激活此功能，故而下文中的例子没有成功渲染。

常见的扩展Markdown语法是在本地使用标头书签链接; `[](#header-anchor)`，或者跨文件`[](path/to/file.md#header-anchor)`。要实现这一点，必须为节标题分配锚，这可以在`myst-parser` 中实现，方法是在 `conf.py` 中设置 `myst_heading_anchors = 2`。这将为 `h1` 和 `h2` 级别的标题配置标题锚。

锚“slugs”创建的目的是遵循GitHub实现;小写文本，删除标点符号，用`-`替换空格，唯一性通过后缀枚举`-1`。要更改 slug 函数，请将 `conf.py` 中的`myst_heading_slug_func`设置为接受字符串并返回字符串的函数。你可以使用命令行工具来检查将要创建的链接:

```shell
$ myst-anchors -l 2 docs/syntax/optional.md
<h1 id="optional-myst-syntaxes"></h1>
<h2 id="admonition-directives"></h2>
<h2 id="auto-generated-header-anchors"></h2>
<h2 id="definition-lists"></h2>
<h2 id="images"></h2>
<h2 id="markdown-figures"></h2>
<h2 id="direct-latex-math"></h2>
```

For example：

```{card}
* `[](#activate-autosectionlabel)` ：[](#activate-autosectionlabel)

* `[other-file](./autobuild.md#sphinx-autobuild)` : [other-file](./autobuild.md#sphinx-autobuild)
```
