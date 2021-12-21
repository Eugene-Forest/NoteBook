# 下拉框插件 sphinx-togglebutton

> **更新时间: {sub-ref}`today` | sphinx_togglebutton 版本：{{sphinx_togglebutton}}**

如果需要在 MyST 或 MyST-NB 解析下的 `.md` 文件下使用选项卡，那么建议使用另一个功能更加强大的插件 [Sphinx Design](./design/design-index.md) 。当然，如果只是要使用下拉框功能，那么可以直接使用这个插件。

## 安装

You can install sphinx-togglebutton with pip:

`pip install sphinx-togglebutton`

Then, activate it in your sphinx build by adding it to your `conf.py` configuration file, like so:

```python
extensions = [
    ...
    'sphinx_togglebutton'
    ...
]
```

**sphinx-togglebutton 专为 sphinx-book-theme 设计。** 所以在其他主题中使用可能会出现问题。

## 配置：控制切换按钮悬停文本

当下拉框的内容折叠时，您可以控制其旁边显示的“提示”文本。为此，请在您的 `conf.py` 文件中使用以下配置变量：

```python
# default value is 'click to show'
togglebutton_hint = "展示隐藏内容"
```

## 语法和效果

### 与admonition选项卡一同使用

与 admonition、note等选项卡一同使用，在选项卡指令中添加选项 class 的属性，如 `dropdown`(使用 toggle 并默认隐藏内容) 、 `dropdown,toggle-shown` (使用 toggle 并默认显示内容)

::::{tab-set-code} 

:::{code-block} markdown

```{admonition} What could be inside this warning?
:class: warning, dropdown, toggle-shown

A whale of a joke!

![A whale of a joke](https://media.giphy.com/media/FaKV1cVKlVRxC/giphy.gif)

(sorry)
```

:::

:::{code-block} rst

.. admonition:: What could be inside this warning?
:class: warning, dropdown, toggle-shown

A whale of a joke!

.. image:: https://media.giphy.com/media/FaKV1cVKlVRxC/giphy.gif

(sorry)

:::

::::

> 运行结果如下：

```{admonition} What could be inside this warning?
:class: warning, dropdown, toggle-shown

A whale of a joke!

![A whale of a joke](https://media.giphy.com/media/FaKV1cVKlVRxC/giphy.gif)

(sorry)
```

我们可以注意到，我们可以使用自定义标题告诫和应用的“内置”的训诫（例如，风格note，warning用等）`admonition` 指令。

<!-- 
```{eval-rst}
.. include:: ./example/tab/tab-code.rst
``` 
-->

### 使用 toggle 指令

要添加可切换的内容，请使用 `toggle` 指令。该指令将其内容包装在一个可切换的容器中。要默认显示可切换的内容，请使用 `:show:` 标志。

```{eval-rst}
.. include:: ./togglebutton-toggle.rst
```

> 渲染结果如下：

```{toggle}
:show:
Here is my toggle-able content!
```
