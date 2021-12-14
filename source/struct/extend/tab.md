
# 选项卡插件


构建 HTML 时在 Sphinx 文档中创建选项卡式内容。本文章参考 [Sphinx Tabs 官方文档](https://sphinx-tabs.readthedocs.io/en/latest/) 。

## 安装

```{code-block} 

pip install sphinx-tabs
```

要在 Sphinx 中启用扩展，请将以下内容添加到您的 conf.py：

```{code-block} python

extensions = ['sphinx_tabs.tabs']
```


```{note} Read The Docs 来构建文档时的注意事项
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


:::{note} 在 rst 文件中使用 Sphinx Design 插件实现选项卡功能

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

<!-- //todo 添加链接向 design 笔记的 -->

:::



## 在 Markdown 语法使用

```markdown

::::{tab-set}

:::{tab-item} Label1
Content 1
:::

:::{tab-item} Label2
Content 2
:::

::::

```

> 运行结果如下：

::::{tab-set}

:::{tab-item} Label1
Content 1
:::

:::{tab-item} Label2
Content 2
:::

::::
