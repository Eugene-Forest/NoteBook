(get-started-with-myst)=

# MyST

> **更新时间: 2021-12-21, 11:46:56 | myst_parser 版本：{{myst_parser}}**

MyST 是一种丰富且可扩展的 Markdown 风格，用于技术文档和发布。

## 为什么使用 MyST

虽然 Markdown 无处不在，但它的功能还不足以编写现代的、功能齐全的文档。为此需要一些 Markdown 支持功能，但没有围绕这些功能的各种语法选择的社区标准。

Sphinx 是一个用 Python 编写的文档生成框架。它大量使用了 reStructuredText 语法，这是另一种用于编写文档的标记语言。特别是，Sphinx 定义了两个非常有用的扩展点： 内联角色和块级指令。

MyST 试图将 Markdown 的简单性和可读性与 reStructuredText 和 Sphinx 平台的强大功能和灵活性相结合。它从CommonMark 降价规范开始，并有选择地添加了一些额外的语法片段以利用 reStructuredText 最强大的部分。

## MyST、reStructuredText 和 Sphinx 之间的关系

MyST Markdown 提供了与 reStructuredText 语法等效的 Markdown，这意味着您可以在 MyST 中做任何可以用 reStructuredText 做的事情。

Sphinx 文档引擎支持多种不同的输入类型。默认情况下，Sphinx 读取reStructuredText ( .rst) 文件。Sphinx 使用解析器将输入文件解析为它自己的内部文档模型（由核心 Python 项目 docutils 提供）。

开发人员可以扩展 Sphinx以支持其他类型的输入文件。任何内容文件都可以读入 Sphinx 文档结构，前提是有人为该文件编写了 解析器。一旦内容文件被解析为 Sphinx，它的行为与任何其他内容文件几乎相同，无论它是用什么语言编写的。

MyST 解析器是用于 MyST 降价语言的 Sphinx 解析器。当您使用它时，Sphinx 将知道如何解析包含 MyST Markdown 的内容文件（默认情况下，Sphinx 会假设任何以 结尾的文件.md都是用 MyST Markdown 编写的）。一旦文档被解析为 Sphinx，无论它是用 rST 还是 MyST Markdown 编写的，它的行为都是一样的。

```
myst markdown (.md) ------> myst parser ---+
                                           |
                                           +-->Sphinx document (docutils)
                                           |
reStructuredText (.rst) --> rst parser ----+
```

```{note} 可以同时使用 MyST 和 reStructuredText
激活 MyST 解析器将简单地启用 MyST解析 Markdown 文件，Sphinx 附带的 rST 解析器仍将以相同的方式工作。以 结尾的文件.md将被解析为 MyST，以 结尾的文件.rst将被解析为 reStructuredText。
```

## 关于 MyST 语法

作为基础，MyST 建立在 markdown-it 定义的标记之上，所以 MyST 遵守 [CommonMark 规范](https://spec.commonmark.org/)。为此，它使用了[markdown-it-py解析器](https://github.com/executablebooks/markdown-it-py)，这是一个结构良好的 Python 降价解析器，符合 CommonMark 规范且可扩展。

MyST 向 CommonMark 添加了几个新的语法选项，以便与 Sphinx 一起使用，而 Sphinx 是 Python 生态系统中广泛使用的文档生成引擎。

```{seealso} VS Code 扩展
查看 [MyST-Markdown VS Code](https://marketplace.visualstudio.com/items?itemName=ExecutableBookProject.myst-highlight) 扩展，了解 MyST 扩展语法高亮。
```

本章节目的是讲解 MyST 的语法以及对应的渲染结果，所以需要频繁变动指令和查看结果。虽然 VS Code 支持 MyST 语法高亮，但是不支持对应的 ``.md`` 文件的预览功能，但是需要主动构建html文件或者通过预览 `rst` 文件来更新 `md` 文件的本地html构建结果，效率十分差；为此，我们可以使用 {ref}`sphinx-autobuild 插件 <sphinx-ext-autobuild>`，它能够支持在浏览器中实时重新加载有关更改的 Sphinx 文档。

```{toctree}
:caption: MyST 语法学习
:numbered:

入门 MyST <./start>
MyST 语法指南 <./syntax-guide>
MyST 的扩展语法 <./optional-syntax>
MyST 与 Sphinx <sphinx-use>
sphinx_book_theme 下的 MyST 扩展语法 <sbt-ext-syntax>
```

```{toctree}
:caption: 交互式代码（目前支持 python）

示例1 <./example/example>
示例2 <./example/exa>
```
