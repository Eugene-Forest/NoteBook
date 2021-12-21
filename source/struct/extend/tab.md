
# 选项卡插件 sphinx_tabs.tabs

> **更新时间: {sub-ref}`today` | sphinx-tabs 版本：{{sphinx_tabs}}**

构建 HTML 时在 Sphinx 文档中创建选项卡式内容。本文章参考 [Sphinx Tabs 官方文档](https://sphinx-tabs.readthedocs.io/en/latest/) 。

需要注意的是， sphinx_tabs.tabs 插件相较于 MyST ，更适合在 `.rst` 文件中被解析，所以如果需要在 MyST 或 MyST-NB 解析下的 `.md` 文件下使用选项卡，那么建议使用另一个功能更加强大的插件 [Sphinx Design](./design/design-index.md) 。

```{warning}
sphinx-tabs 3.2.0 requires docutils~=0.16.0；但是由于考虑到将来可能要使用 {ref}`myst-rst-include-md` 的功能，而此功能需要依赖 docutils >=0.17，所以此插件版本可能会被笔者作为过时版本。
```

## 安装

```{code-block}

pip install sphinx-tabs
```

要在 Sphinx 中启用扩展，请将以下内容添加到您的 conf.py：

```{code-block} python

extensions = ['sphinx_tabs.tabs']
```


```{admonition} Read The Docs 来构建文档时的注意事项
:class: dropdown
如果您使用 Read The Docs 来构建文档，则必须添加扩展作为要求。请将 sphinx-tabs 添加到项目根目录或 docs 文件夹中的 requirements.txt。
```

## 在 reST 语法使用

```rest
.. tabs::

   .. tab:: Apples

      Apples are green, or sometimes red.

   .. tab:: Pears

      Pears are green.

   .. tab:: Oranges

      Oranges are orange.
```

> 运行结果如下：

```{eval-rst}
.. include:: ./example/tab/tabs-base.rst
```

```{admonition} 更多指令

sphinx-tabs.tabs 插件还有 group-tab 指令 和 [code-tab](./example/tab/tab-code.rst) 指令与 tabs 指令嵌套使用的语法，在这里就不加以详述，若有学习意向可 [前往 sphinx-tabs 官方文档查看](https://sphinx-tabs.readthedocs.io/en/latest/) 。
```

:::{admonition} 在 rst 文件中使用 Sphinx Design 插件实现选项卡功能

```rest
.. tab-set::

    .. tab-item:: Label1

        Content 1

    .. tab-item:: Label2

        Content 2
```


> 运行结果如下：

```{eval-rst}
.. include:: ./example/design/tab.rst
```

建议使用另一个功能更加强大的插件 [Sphinx Design](./design/design-index.md) 。

:::

## 使用 MyST Parser 的 Markdown 语法使用

```markdown
::::{tabs}

:::{tab} Label1

Content 1
:::

:::{tab} Label2

Content 2
:::

::::
```

> 运行结果如下：(Markdown形式的语法参考RST形式的,需要注意的是这个指令和内容之间必须要有空行)

::::{tabs}

:::{tab} Label1

Content 1
:::

:::{tab} Label2

Content 2
:::

::::


## 实际应用

由于 sphinx tabs 插件的在使用过程中使用到指令的多层嵌套，将其转换为 MyST 语法格式会变得难以阅读，所以采用引用 `.rst` 文件的形式使用在 `.md` 文件中。

:::markdown

```{eval-rst}
.. include:: ./example/tab/tab-code.rst
```

:::

> [代码实际运行界面](./example/tab/tab-code.rst) 可点击源码界面的下载按钮查看实现源码, 引用下的代码运行效果如下

```{eval-rst}
.. include:: ./example/tab/tab-code.rst
``` 

