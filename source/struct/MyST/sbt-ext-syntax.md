
(sbt-special-blocks)=

# sphinx book theme 特殊内容块

> **更新时间: 2021年12月22日16点29分  | sphinx_book_theme 版本：{{sphinx_book_theme}}**

这个主题的一些特别的指令语法。

## epigraph 引文

没有署名的引用：

> Here’s my quote, it’s pretty neat. I wonder how many lines I can create with a single stream-of-consciousness quote. I could try to add a list of ideas to talk about. I suppose I could just keep going on forever, but I’ll stop here.

:::{toggle}

```md
> Here’s my quote, it’s pretty neat. I wonder how many lines I can create with a single stream-of-consciousness quote. I could try to add a list of ideas to talk about. I suppose I could just keep going on forever, but I’ll stop here.
```

:::

有时候你会想让引用更引人注意。为此，使用 `{epigraph}` 指令。下面是一个引文，点击它右边的按钮，显示用于生成它的代码:

```{epigraph}
Here's my quote, it's pretty neat.
I wonder how many lines I can create with
a single stream-of-consciousness quote.
I could try to add a list of ideas to talk about.
I suppose I could just keep going on forever,
but I'll stop here.
```

:::{toggle}

````md
```{epigraph}
Here's my quote, it's pretty neat.
I wonder how many lines I can create with
a single stream-of-consciousness quote.
I could try to add a list of ideas to talk about.
I suppose I could just keep going on forever,
but I'll stop here.
```
````

:::

还可以通过添加空行，后跟以 `--` 开头的行，向题词添加属性。这将被渲染成这样:

```{epigraph}
Here's my quote, it's pretty neat.
I wonder how many lines I can create with
a single stream-of-consciousness quote.
I could try to add a list of ideas to talk about.
I suppose I could just keep going on forever,
but I'll stop here.

-- Jo the Jovyan, *[the jupyter book docs](https://beta.jupyterbook.org)*
```

:::{toggle}

````md
```{epigraph}
Here's my quote, it's pretty neat.
I wonder how many lines I can create with
a single stream-of-consciousness quote.
I could try to add a list of ideas to talk about.
I suppose I could just keep going on forever,
but I'll stop here.

-- Jo the Jovyan, *[the jupyter book docs](https://beta.jupyterbook.org)*
```
````

:::

## Sidebars

`sphinx-book-theme` 中有两种不同类型的类似边栏的内容，典型且通用的的 `{sidebar}` 指令，以及特定于此主题的 `{margin}` 指令。本节将涵盖这两方面。两者都允许你将额外内容与主要内容分开放置。

```{tip}
侧边栏的内容通常会与站点内容表所在的空白区域重叠。当阅读器将侧边栏内容滚动到视图中时，右边的导航栏应该自动隐藏。
```

`````{toggle}
````md
```{sidebar} 有两种方式添加内容到左侧边栏中

* 通过`{margin}`指令
* 通过添加 `margin` 这个CSS类到你自己的内容块中。
```
````
`````

```{sidebar} 有两种方式添加内容到左侧边栏中

* 通过`{margin}`指令
* 通过添加 `margin` 这个CSS类到你自己的内容块中。
```

### 通过指令添加

margin 侧边栏语法如下：

```{margin} **margin 侧边栏标题**

margin 侧边栏标题内容

```

````md
```{margin} **margin 侧边栏标题**

margin 侧边栏标题内容

```
````

```{margin} margin 侧边栏标题

margin 侧边栏标题内容

```

通过上文我们可以知道，margin 侧边栏标题与代码块之类的组件是没有办法处于同一行（水平的）位置的，我们在使用 margin 侧边栏标题时需要注意其放置的位置。

### 通过CSS类 margin 添加

:::{note}
:class: margin
This note will be in the margin!
:::

```md
:::{note}
:class: margin
This note will be in the margin!
:::
```

这适用于页面上的大多数指令，但一般来说，这适用于“父容器”，即内容包的顶部指令。

```{figure} img/fun-fish.png
---
figclass: margin
alt: My figure text
name: myfig4
---
And here is my figure caption
```

例如： figure图片

:::md

```{figure} img/fun-fish.png
---
figclass: margin
alt: My figure text
name: myfig4
---
And here is my figure caption
```

:::

### 在页边空白处加上图片的文字说明

```{figure} img/fun-fish.png
---
width: 60%
figclass: margin-caption
alt: My figure text
name: myfig54
---
And here is my figure caption, if you look to the left, you can see that COOL is in big red letters. But you probably already noticed that, really I am just taking up space to see how the margin caption looks like when it is really long :-)
```

````md
```{figure} img/fun-fish.png
---
width: 60%
figclass: margin-caption
alt: My figure text
name: myfig54
---
And here is my figure caption, if you look to the left, you can see that COOL is in big red letters. But you probably already noticed that, really I am just taking up space to see how the margin caption looks like when it is really long :-)
```
````

## 宽屏的内容

全宽度的内容延伸到右边，使它在你的书的其他内容中脱颖而出。要向页面添加全宽内容，请向文档中的任何元素添加类全宽内容。例如，你可以像这样给 `note` 指令或其他指令添加一个全宽类属性:

````md
```{note}
:class: full-width
This content will be full-width
```

```{code-block} java
:class: full-width

public class main {
    public static void main(String[] args) {
        System.out.println("hello world");
    }
}
```
````

> 这段代码的结果如下:

```{note}
:class: full-width
This content will be full-width
```

```{code-block} java
:class: full-width

public class main {
    public static void main(String[] args) {
        System.out.println("hello world");
    }
}
```
