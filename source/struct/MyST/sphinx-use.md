# MyST 与 Sphinx

MyST 解析器与 Sphinx 扩展捆绑在一起，允许您完全在 MyST 中（或在 rST 和 MyST 的组合中）使用编写 Sphinx 文档。以下部分介绍了 Sphinx 扩展的一些主要功能。这些部分描述了使用 Sphinx 编写 MyST 的一些常见场景和用例。

(myst-md-include-rst)=

## 将 rST 文件包含到 Markdown 文件中

如本节所述，所有 MyST 指令都将其内容解析为 Markdown。因此，使用常规 `include` 指令，将文件内容解析为 Markdown：

````md
```{include} example/include-md.md
```
````

```{include} example/include-md.md
```

要包含 rST，我们必须首先将指令“包装”在 [eval-rst 指令](myst-syntax-guide-eval-rst)中：

````md
```{eval-rst}
.. include:: ./example/include-rst.rst
```
````

```{eval-rst}
.. include:: ./example/include-rst.rst
```

(myst-rst-include-md)=

## 将 Markdown 文件包含到 rST 文件中

要在 ReStructuredText 文件中包含 MyST 文件，我们可以使用 `include` 指令并指定 `parser` 选项：

```rest
.. include:: include.md
   :parser: myst_parser.sphinx_
```

```{important}
该parser选项需要docutils>=0.17。但是此主题 sphinx-book-theme 0.1.7 requires docutils<0.17,>=0.15 ；而插件 sphinx-tabs 3.2.0 requires docutils~=0.16.0 。
虽然可以不使用插件 sphinx-tabs，但是主题sphinx-book-theme 0.1.7 依赖于小于 0.17 版本得 docutils ，所以该功能暂时无法使用。
```

## 在 Jupyter Notebooks 中使用 MyST

## 包含来自 docs / source 文件夹之外的文件（如README.md）


## 自动为节标题创建目标

## Sphinx 特定的页面前端

## 将预先存在的 rST 迁移到 MyST
