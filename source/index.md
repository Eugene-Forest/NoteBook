# Eugene forest's notebook

[![GitHub last commit][github-badge]][github-link]
[![Documentation Status][rtd-badge]][rtd-link]

> **文档构建时间: {sub-ref}`today`**

这是笔者在学习过程中的一些笔记，可能包括软件的安装配置、技术的知识点、技术的使用技巧、软件的使用方法、以及学习过程当中的感悟、学习过程中出现的疑问以及疑问的解决。

本项目是通过 [Sphinx](https://www.sphinx-doc.org/zh_CN/master/index.html) 工具来实现的，使用了并涉及了 [reStructureText](https://www.sphinx-doc.org/zh_CN/master/usage/restructuredtext/index.html) 、 Markdown 、[MyST](https://myst-parser.readthedocs.io/en/latest/index.html) 标记语言以及其他基于这些语言的 Sphinx 插件扩展语法来编写文档，并托管与 [Read the Docs](https://readthedocs.org/) 平台运行。

项目分为三个分支。其中， **main** 分支是主分支，是 **k-doc** 和 **builder-doc** 分支的结合；而 **k-doc** 分支记载笔者的工作、学习的笔记和感悟；而 **builder-doc** 分支主要是介绍本项目的相关编写语法和工具，涉及 [MyST](https://myst-parser.readthedocs.io/en/latest/index.html) 、 [reStructureText](https://www.sphinx-doc.org/zh_CN/master/usage/restructuredtext/index.html) 和 [Sphinx](https://www.sphinx-doc.org/zh_CN/master/index.html) 文档工具和插件等。

```{toctree}
:caption: "knowledge 笔记记录"
:hidden:
:maxdepth: 1

Java 笔记记录 <k-java/java-index>
Git 笔记记录 <k-git/git-index>
TypeScript 笔记记录 <k-typescript/typescript-index>
Node 笔记记录 <k-node/node-index>
Linux 和 Shell 笔记记录 <k-linux/linux-index>
SQL 笔记记录 <k-sql/sql-index>
Windows 笔记记录 <k-windows/windows-index>
Vue 笔记记录 <k-vue/vue-index>
Element-UI 笔记记录 <k-element-ui/el-index>
JavaScript 笔记记录 <k-js/js-index>
计算机网络 <k-network/net-index>
Python 笔记记录 <k-python/python-index>
Redis 笔记记录 <k-redis/redis-index>
```

<!-- For Project -->

```{toctree}
:caption: "项目以及常见业务实现"
:hidden:
:maxdepth: 1

常见业务实现 </project/business/b-index>
项目：工具箱 </project/toolbox/box-index>
毕设：医院住院部护士排班ASP系统-管理者端的构建 </project/nsms/nsms-index>
```

<!-- For Software -->

```{toctree}
:caption: "软件或工具包安装以及配置记录"
:hidden:
:maxdepth: 1

bladex 快速开发平台的使用 </software/bladex/bladex-index>
jetbrains </software/jetbrains/index>
vscode </software/vs-code/index>
eclipse </software/eclipse/index>
netbeans </software/netbeans/index>
wireshark </software/wireshark/index>
一些常用软件的快捷键 </software/shortcut-key>
Navicat Premium 实用技巧 </software/navicat/navicat>
```

% ----------- For Builder Doc branch ---------------
% Here is the Toctree for the Builder-Doc branch  

```{toctree}
:caption: "构建文档的工具和标记语言"
:hidden:
:maxdepth: 1

Sphinx 工具和 reST 标记语言 <struct/sphinx/sphinx-index>
Markdown 标记语言 <struct/markdown/md-index>
MyST <struct/MyST/myst-index>
Sphinx 扩展工具 <struct/extend/ext-index>
MyST-NB <struct/MyST-NB/MyST-NB>
```

% ------------------------------------------------------------

## 关于 `MyST`

*MyST* 建立在 *markdown-it* 定义的标记之上，所以 *MyST* 遵守 [CommonMark 规范](https://spec.commonmark.org/)。为此，它使用了 [markdown-it-py 解析器](https://github.com/executablebooks/markdown-it-py)，这是一个结构良好的 *Python* 降价解析器，符合 *CommonMark* 规范且可扩展。

*MyST* 向 *CommonMark* 添加了几个新的语法选项，以便与 *Sphinx* 一起使用，而 *Sphinx* 是 *Python* 生态系统中广泛使用的文档生成引擎。

## 为什么使用 `MyST`

虽然 *Markdown* 无处不在，但它的功能还不足以编写现代的、功能齐全的文档。为此需要一些 *Markdown* 支持功能，但没有围绕这些功能的各种语法选择的社区标准。

*Sphinx* 是一个用 *Python* 编写的文档生成框架。它大量使用了 *reStructuredText* 语法，这是另一种用于编写文档的标记语言。特别是， *Sphinx* 定义了两个非常有用的扩展点： 内联角色和块级指令。

*MyST* 试图将 *Markdown* 的简单性和可读性与 *reStructuredText* 和 *Sphinx* 平台的强大功能和灵活性相结合。它从 *CommonMark* 降价规范开始，并有选择地添加了一些额外的语法片段以利用 *reStructuredText* 最强大的部分。

## `MyST` 、 `reStructuredText` 和 `Sphinx` 之间的关系

*MyST* 提供了与 *reStructuredText* 语法等效的 *Markdown* ，这意味着您可以在 *MyST* 中做任何可以用 *reStructuredText* 做的事情。

*Sphinx* 文档引擎支持多种不同的输入类型。默认情况下， *Sphinx* 读取 *reStructuredText* ( `.rst`) 文件。 *Sphinx* 使用解析器将输入文件解析为它自己的内部文档模型（由核心 *Python* 项目 `docutils` 提供）。

开发人员可以扩展 *Sphinx* 以支持其他类型的输入文件。任何内容文件都可以读入 *Sphinx* 文档结构，前提是有人为该文件编写了 解析器。一旦内容文件被解析为 *Sphinx* ，它的行为与任何其他内容文件几乎相同，无论它是用什么语言编写的。

*MyST* 解析器是用于 *MyST* 降价语言的 *Sphinx* 解析器。当您使用它时， *Sphinx* 将知道如何解析包含 *MyST* 的内容文件（默认情况下， *Sphinx* 会假设任何以 结尾的文件.md都是用 *MyST* 编写的）。一旦文档被解析为 *Sphinx* ，无论它是用 `rST` 还是 *MyST* 编写的，它的行为都是一样的。

```
myst markdown (.md) ------> myst parser ---+
                                           |
                                           +-->Sphinx document (docutils)
                                           |
reStructuredText (.rst) --> rst parser ----+
```

## 项目对应的电子书在线查看

本项目已经挂载在 [Read the Docs](https://readthedocs.org/) 中，点击下方链接即可在线查看项目的实现即电子书。链接如下： https://studynotes.readthedocs.io/zh/k-doc


## 关于免费的开源托管平台 Read the Docs

[Read the Docs](https://readthedocs.org/) 通过自动为您构建，版本控制和托管文档来简化软件文档。 



<!-- For endnote -->

[github-badge]: https://img.shields.io/github/last-commit/Eugene-Forest/NoteBook
[github-link]: https://img.shields.io/github/last-commit/Eugene-Forest/NoteBook
[rtd-badge]: https://readthedocs.org/projects/studynotes/badge/?version=main
[rtd-link]: https://studynotes.readthedocs.io/zh/main/?badge=main
