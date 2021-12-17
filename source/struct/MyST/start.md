# Get started with MyST in Sphinx

本页面描述了如何开始使用MyST解析器，重点介绍如何在Sphinx文档引擎中启用它。

## 安装MyST解析器

安装 MyST 解析器可以访问两个工具：

* 一个 Python 库，可以解析 MyST Markdown，并将其呈现为多种输出格式（特别是`docutils`与 Sphinx 一起使用的格式）。

* 一个 Sphinx 扩展，它利用上述工具来解析文档中的 MyST Markdown。

要安装 MyST 解析器，请在Conda 环境中运行以下命令 （推荐）：

```cmd
conda install -c conda-forge myst-parser
```

或者

```cmd
pip install myst-parser
```

## 在 Sphinx 中启用 MyST

要在 Sphinx 中使用 MyST 解析器，只需将以下内容添加到您的conf.py文件中：

extensions = ["myst_parser"]

这将激活 MyST Parser 扩展，导致所有带有该.md扩展的文档都被解析为 MyST。

:::{admonition} 能够同时使用 MyST 和 reStructuredText
:class: tip

激活MyST解析器只会使用MyST解析markdown文件，而Sphinx附带的rST解析器仍然会以相同的方式工作。以`.md`结尾的文件将被解析为MyST，而以`.rst`结尾的文件将被解析为reStructuredText。
:::

## 编写你的第一个 Markdown 文档

如果现在您已经在 Sphinx 中启用了 `myst-parser` ，您可以在一个 `.md` 扩展名结尾的文件中编写 `MyST Markdown` 。

:::{note}
MyST Markdown 是两种 Markdown 风格的混合体：

它在其基础上支持 [CommonMark Markdown](https://commonmark.org/) 的所有语法。这是许多项目中使用的社区标准的 Markdown 风格。

此外，它还包括对 **CommonMark 的[几个扩展](./syntax.md)**。这些为技术写作添加了额外的语法特性，例如 Sphinx 使用的角色和指令。
:::

首先，创建一个名为的空文件myfile.md并给它一个 Markdown 标题和文本。

```markdown
# My nifty title

Some **text**!
```

在您的 Sphinx 项目的“主文档”（您的 Sphinx 文档的登录页面）中，包含myfile.md一个toctree指令，以便将其包含在您的文档中：

```restructureText
.. toctree::

   myfile.md
```

现在建立你的网站：

```cmd
make html
```

并导航到您的登录页面。您应该会看到一个指向从 生成的页面的链接myfile.md。单击该链接应将您带到呈现的 Markdown！

## 使用指令扩展 markdown

通过了解 [CommonMark Markdown](https://commonmark.org/) ，我们可以知道社区标准的 Markdown 风格的语法和实现的功能十分少，不能编写复杂的文档。

MyST Markdown 最重要的功能是编写指令。指令有点像为编写内容而设计的函数。Sphinx 和 reStructuredText 广泛使用指令。以下是指令在 MyST markdown 中的外观：

````markdown
```{directivename} <directive arguments>
:optionname: <valuename>

<directive content>
```
````

<!-- //todo 如果无法激活 myst markdown 侧边栏则取消使用 -->
````{margin}替代选项语法
如果您的指令有很多选项，或者有一个非常长的值（例如，跨越多行），那么您还可以将选项包装在行中 `---` 并将它们写为 YAML。例如：
```yaml
---
key1: val1
key2: |
  val line 1
  val line 2
---
```
````

如上所述，编写指令时需要考虑四个主要部分。

* 指令名称有点像函数名称。不同的名称触发不同的功能。它们用{}括号括起来。

* 指令参数紧跟在指令名称之后。它们可用于触发指令中的行为。

* 指令选项紧跟在指令的第一行之后。它们还控制指令的行为。

* 指令内容是您放在指令中的降价。该指令通常以特殊方式显示内容。

When you build your documentation, you should see something like this:

```{mermaid}
sequenceDiagram
  participant Alice
  participant Bob
  Alice->John: Hello John, how are you?
  loop Healthcheck
      John->John: Fight against hypochondria
  end
  Note right of John: Rational thoughts <br/>prevail...
  John-->Alice: Great!
  John->Bob: How about you?
  Bob-->John: Jolly good!
```

Term 1
: Definition

Term 2
: Definition