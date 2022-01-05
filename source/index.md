# Eugene forest's notebook

[![GitHub last commit][github-badge]][github-link]
[![Documentation Status][rtd-badge]][rtd-link]

> **文档构建时间: {sub-ref}`today`**

这是笔者在学习过程中的一些笔记，可能包括软件的安装配置、技术的知识点、技术的使用技巧、软件的使用方法、以及学习过程当中的感悟、学习过程中出现的疑问以及疑问的解决。

% //todo 主页待更新

## 关于本项目

本项目是通过 Sphinx 来实现的，使用了 reStructuredText、Markdown、MyST Markdown 标记语言以及其他基于这些语言的 Sphinx 插件扩展语法来编写文档，并托管与 Read The Docs 平台运行。

## 主目录

```{toctree}
:caption: "knowledge 笔记记录"
:maxdepth: 1

Java 笔记记录 </knowledge/java/java-index>
Git 笔记记录 </knowledge/git/git-index>
Vue 笔记记录 </knowledge/vue/vue-index>
Element-UI 笔记记录 </knowledge/element-ui/el-index>
JavaScript 笔记记录 </knowledge/js/js-index>
计算机网络 </knowledge/network/net-index>
Python 笔记记录 </knowledge/python/python-index>
SQL 笔记记录 </knowledge/sql/sql-index>
Linux 笔记记录 </knowledge/linux/linux-index>
Redis 笔记记录 </knowledge/redis/redis-index>
```

```{toctree}
:caption: "项目以及常见业务实现"
:maxdepth: 1

常见业务实现 </project/business/b-index>
项目：工具箱 </project/toolbox/box-index>
毕设：医院住院部护士排班ASP系统-管理者端的构建 </project/nsms/nsms-index>
```

```{toctree}
:caption: "软件或工具包安装以及配置记录"
:maxdepth: 1

bladex 快速开发平台的使用 </software/bladex/bladex-index>
jetbrains </software/jetbrains/index>
vscode </software/vs_code/index>
eclipse </software/eclipse/index>
netbeans </software/netbeans/index>
wireshark </software/wireshark/index>
xshell以及xftp的教育版下载 </software/xshell>
一些常用软件的快捷键 </software/shortcut-key>
```

```{toctree}
:caption: "构建文档的工具和标记语言"
:maxdepth: 1

Sphinx 工具和 reST 标记语言 <struct/sphinx/sphinx-index>
Markdown 标记语言 <struct/markdown/md-index>
MyST <struct/MyST/myst-index>
Sphinx 扩展工具 <struct/extend/ext-index>
MyST-NB <struct/MyST-NB/MyST-NB>
```

[github-badge]: https://img.shields.io/github/last-commit/Eugene-Forest/NoteBook
[github-link]: https://img.shields.io/github/last-commit/Eugene-Forest/NoteBook
[rtd-badge]: https://readthedocs.org/projects/studynotes/badge/?version=builder-doc
[rtd-link]: https://studynotes.readthedocs.io/zh/builder-doc/?badge=builder-doc
