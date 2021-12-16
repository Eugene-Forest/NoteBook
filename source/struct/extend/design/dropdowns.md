# 可下拉选项卡

下拉框可以用来切换内容，通常是非必要的，并且只有当用户点击标题面板时才会显示。

下拉菜单可以有一个标题，作为指令参数，并且打开选项可以用来初始化下拉菜单的打开状态。

:::{dropdown}
Dropdown content
:::

:::{dropdown} Dropdown title
Dropdown content
:::

:::{dropdown} Open dropdown
:open:

Dropdown content
:::

`````{dropdown} Syntax
:open:
:icon: code
:color: light

````{tab-set-code}
```{literalinclude} ./snippets/myst/dropdown-basic.txt
:language: markdown
```
```{literalinclude} ./snippets/rst/dropdown-basic.txt
:language: rst
```
````
`````

## 下拉框打开时的动画

使用 `:animate: fade-in` 或 `:animate: fade-in-slide-down` 选项使隐藏的内容得以呈现。

:::{dropdown} Dropdown `fade-in`
:animate: fade-in

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed iaculis arcu vitae odio gravida congue. Donec porttitor ac risus et condimentum. Phasellus bibendum ac risus a sollicitudin. Proin pulvinar risus ac mauris aliquet fermentum et varius nisi. Etiam sit amet metus ac ipsum placerat congue semper non diam. Nunc luctus tincidunt ipsum id eleifend. Ut sed faucibus ipsum. Aliquam maximus dictum posuere. Nunc vitae libero nec enim tempus euismod. Aliquam sed lectus ac nisl sollicitudin ultricies id at neque. Aliquam fringilla odio vitae lorem ornare, sit amet scelerisque orci fringilla. Nam sed arcu dignissim, ultrices quam sit amet, commodo ipsum. Etiam quis nunc at ligula tincidunt eleifend.
:::

:::{dropdown} Dropdown `fade-in-slide-down`
:animate: fade-in-slide-down

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed iaculis arcu vitae odio gravida congue. Donec porttitor ac risus et condimentum. Phasellus bibendum ac risus a sollicitudin. Proin pulvinar risus ac mauris aliquet fermentum et varius nisi. Etiam sit amet metus ac ipsum placerat congue semper non diam. Nunc luctus tincidunt ipsum id eleifend. Ut sed faucibus ipsum. Aliquam maximus dictum posuere. Nunc vitae libero nec enim tempus euismod. Aliquam sed lectus ac nisl sollicitudin ultricies id at neque. Aliquam fringilla odio vitae lorem ornare, sit amet scelerisque orci fringilla. Nam sed arcu dignissim, ultrices quam sit amet, commodo ipsum. Etiam quis nunc at ligula tincidunt eleifend.
:::

## 在其他组件下的下拉框

::::{dropdown} Parent dropdown title
:open:

:::{dropdown} Child dropdown title
:color: warning
:icon: alert

Dropdown content
:::
::::

:::::{grid} 1 1 2 2
:gutter: 1

::::{grid-item}
:::{dropdown} Dropdown Column 1
Dropdown content
:::
::::

::::{grid-item}
:::{dropdown} Dropdown Column 2
Dropdown content
:::
::::

:::::


## dropdowns 可选项

```{eval-rst}
.. include:: ./snippets/dropdowns-option.rst
```
