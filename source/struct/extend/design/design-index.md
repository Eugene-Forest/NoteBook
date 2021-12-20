
# Sphinx Design

用于设计漂亮的、屏幕大小的响应式 Web 组件的 Sphinx 扩展。

```{admonition} 适用于多种主题的 Sphinx Design
:class: note
该插件使用多个主题，分别有 `alabaster`、`sphinx-book-theme`、`pydata-sphinx-theme`、`sphinx-rtd-theme`、`furo` 。同时，Sphinx Design在不同主题下的语法可能不一样，所以需要读者根据实际使用的主题来阅读 Sphinx Design 语法。本篇章记录的 Sphinx Design 是适用于 `sphinx-book-theme` 的语法。[点击前往官方文档查看](https://sphinx-design.readthedocs.io/en/sbt-theme/) 其他主题下的 Sphinx Design 的使用。
```

## 安装和配置

只需 pip 安装 Sphinx Design ，并添加扩展到您的 `conf.py` :

```python
extensions = ["sphinx_design"]
```

对于使用 `MyST Parser` (或者基于 `MyST Parser` 的解析器，如 `MyST-NB`)来解析的Markdown文档，建议使用 `colon_fence` 语法扩展:

```python
extensions = ["myst_parser", "sphinx_design"]
# extensions = ["myst_nb", "sphinx_design"]
myst_enable_extensions = ["colon_fence"]
```

## 隐藏页面的标题标题

要隐藏页面的标题标题，请将下方代码添加到页面顶部：

::::{tab-set}

:::{tab-item} MyST Markdown

```markdown
---
sd_hide_title: true
---
```

:::

:::{tab-item} RestructuredText

```rst
:sd_hide_title:
```

:::

::::

```{toctree}
:numbered:
:maxdepth: 2

网格 —— grid <grids>
卡片 —— card <cards>
可下拉选项卡 —— dropdown <dropdowns>
标签选项卡 —— tab-set <tabs>
Badges, Buttons & Icons <badges_buttons>
附加功能 <additional>
样式 css <styling>
```
