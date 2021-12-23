# 卡片

卡片包含一个主题的内容和动作。卡片是一种灵活和可扩展的内容容器，它可以用包括页眉和页脚、标题和图像在内的组件进行格式化。

## 简单卡片

:::{card} Card Title

Card content
:::

`````{dropdown} Syntax
:open:
:icon: code
:color: light

````{tab-set-code}
```{literalinclude} ./snippets/myst/card-basic.txt
:language: markdown
```
```{literalinclude} ./snippets/rst/card-basic.txt
:language: rst
```
````
`````

## 含有头部和尾部的卡片

所有第一次出现三个或三个以上' ^^^ '之前的内容被认为是页眉，所有最后出现三个或三个以上' +++ '之后的内容被认为是页脚:

:::{card} Card Title
Header
^^^
Card content
+++
Footer
:::

`````{dropdown} Syntax
:open:
:icon: code
:color: light

````{tab-set-code}
```{literalinclude} ./snippets/myst/card-head-foot.txt
:language: markdown
```
```{literalinclude} ./snippets/rst/card-head-foot.txt
:language: rst
```
````
`````

(sphinx-design-image-cards)=

## 带有图片的卡片

你也可以添加一个图像作为卡的背景或在卡的顶部/底部, 使用 `img-background`, `img-top`, `img-bottom` 选项:

:::::{grid} 2 3 3 4

::::{grid-item}

:::{card} Title
:img-background: ./snippets/particle_background.jpg
:class-card: sd-text-black

Text
:::

::::

::::{grid-item-card} Title
:img-top: ./snippets/particle_background.jpg

Header
^^^
Content
+++
Footer
::::

::::{grid-item-card} Title
:img-bottom: ./snippets/particle_background.jpg

Header
^^^
Content
+++
Footer
::::

:::::

`````{dropdown} Syntax
:open:
:icon: code
:color: light

````{tab-set-code}
```{literalinclude} ./snippets/myst/card-images.txt
:language: markdown
```
```{literalinclude} ./snippets/rst/card-images.txt
:language: rst
```
````
`````

(sphinx-design-cards-clickable)=

## 可点击的卡片

使用`link`和`link-type`选项，你可以把整张卡变成一个可点击的链接。试着把鼠标悬停在上面，然后点击下面的卡片:

可点击卡片的链接形式有两种：

* 一种是外部链接，这种只需要直接在 `card` 指令下添加 `link` 选项以及对应的链接即可。
* 另一种是内部链接，这种需要在 `card` 指令下添加选项 `:link-type: ref` 和 `link` 选项以及对应的目标和交叉引用。

:::{card} Clickable Card (external)
:link: https://example.com

The entire card can be clicked to navigate to <https://example.com>.
:::

:::{card} Clickable Card (internal)
:link: sphinx-design-image-cards
:link-type: ref

The entire card can be clicked to navigate to the `cards-clickable` reference target.
:::

`````{dropdown} Syntax
:open:
:icon: code
:color: light

````{tab-set-code}
```{literalinclude} ./snippets/myst/card-link.txt
:language: markdown
```
```{literalinclude} ./snippets/rst/card-link.txt
:language: rst
```
````
`````

## 卡片的对齐

你可以使用 `text-align` 选项来对齐卡片中的文本，以及 `auto` 对齐卡片的边距 (margin)。

* 使用 `text-align` 选项来对齐卡片中的文本
* 使用 `margin` 选项来

:::{card} Align Center
:width: 75%
:margin: 0 2 auto auto
:text-align: center

Content
:::

:::{card} Align Right
:width: 50%
:margin: 0 2 auto 0
:text-align: right

Content
:::

:::{card} Align Left
:width: 50%
:margin: 0 2 0 auto
:text-align: left

Content
:::

```
:::{card} Align Center
:width: 75%
:margin: 0 2 auto auto
:text-align: center

Content
:::

:::{card} Align Right
:width: 50%
:margin: 0 2 auto 0
:text-align: right

Content
:::

:::{card} Align Left
:width: 50%
:margin: 0 2 0 auto
:text-align: left

Content
:::

```

## 卡片传送带

`card-carousel`指令可用于创建单行固定宽度的可滚动卡片。参数应该是1到12之间的数字，表示要显示的牌的数量。

当滚动一个传送带时，滚动条将从最近的卡片开始:

::::{card-carousel} 2

:::{card} card 1
content
:::
:::{card} card 2
Longer

content
:::
:::{card} card 3
:::
:::{card} card 4
:::
:::{card} card 5
:::
:::{card} card 6
:::
::::

`````{dropdown} Syntax
:open:
:icon: code
:color: light

````{tab-set-code}
```{literalinclude} ./snippets/myst/card-carousel.txt
:language: markdown
```
```{literalinclude} ./snippets/rst/card-carousel.txt
:language: rst
```
````
`````

## card 可选项

```{eval-rst}
.. include:: ./snippets/card-option.rst
```
