# 网格

有接触过前端的应当知道 Grid 网页布局，而 Sphinx Design 插件能够实现相同的效果。（所以它才能称之为响应式的 Web 组件）。

网格是基于12列系统，它可以适应观看屏幕的大小。

**网格指令可以设置默认列数(1到12);对所有屏幕尺寸使用单个数字，或对 extra-small(<576px)、 small (768px)、 medium(992px)和 large screens(>1200px)使用四个数字，然后为每个项目设置子网格项指令。**

网格有三种指令，分别为 `gird`、 `grid-item`、 `grid-item-card`。

## gird option

```{eval-rst}
.. include:: ./snippets/grid-option.rst
```

## grid-item option

```{eval-rst}
.. include:: ./snippets/grid-item-option.rst
```

## grid-item-card option

```{eval-rst}
.. include:: ./snippets/grid-item-card-option.rst
```

## 实例应用

### 简单示例

::::{grid} 4
:outline:

:::{grid-item}
A
:::
:::{grid-item}
B
:::
:::{grid-item}
C
:::
:::{grid-item}
D
:::
::::

`````{dropdown} Syntax
:open:
:icon: code
:color: light

````{tab-set-code}
```{literalinclude} ./snippets/myst/grid-basic.txt
:language: markdown
```
```{literalinclude} ./snippets/rst/grid-basic.txt
:language: rst
```
````
`````

### 卡片网格的简单示例

::::{grid} 2
:::{grid-item-card} Title 1
A
:::
:::{grid-item-card} Title 2
B
:::
::::

`````{dropdown} Syntax
:open:
:icon: code
:color: light

````{tab-set-code}
```{literalinclude} ./snippets/myst/grid-card.txt
:language: markdown
```
```{literalinclude} ./snippets/rst/grid-card.txt
:language: rst
```
````
`````

### 控制网格子项的间距

::::{grid} 2
:gutter: 1

:::{grid-item-card}
A
:::
:::{grid-item-card}
B
:::
::::

::::{grid} 2
:gutter: 5

:::{grid-item-card}
A
:::
:::{grid-item-card}
B
:::
::::

`````{dropdown} Syntax
:open:
:icon: code
:color: light

````{tab-set-code}
```{literalinclude} ./snippets/myst/grid-gutter.txt
:language: markdown
```
```{literalinclude} ./snippets/rst/grid-gutter.txt
:language: rst
```
````
`````

### 网格子项级列宽度

您可以使用grid-item指令的columns选项来覆盖单个条目所占的列数。假设总列为12，这意味着12表示一个条目占了整个网格行，即6 / 2。或者，使用auto可以根据项目内容自动决定使用多少列。与网格列一样，对于小、中、大和超大屏幕，您可以提供单个数字，也可以提供4个数字。

::::{grid} 2
:::{grid-item-card}
:columns: auto

A
:::
:::{grid-item-card}
:columns: 12 6 6 6

B
:::
:::{grid-item-card}
:columns: 12

C
:::
::::

`````{dropdown} Syntax
:open:
:icon: code
:color: light

````{tab-set-code}
```{literalinclude} ./snippets/myst/grid-card-columns.txt
:language: markdown
```
```{literalinclude} ./snippets/rst/grid-card-columns.txt
:language: rst
```
````
`````

```{note}
在此语法中，如果选项的值只接受一个，如果出现如 `:columns: 12 6 6 6` 的情况，这是因为它可以根据屏幕的大小（四种屏幕）来调整占据的列数。
```
