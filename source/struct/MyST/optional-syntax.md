---
substitutions:
  key1: "I'm a **substitution**"
  key2: |
    ```{note}
    {{ key1 }}
    ```
  key3: |
    ```{image} img/fun-fish.png
    :alt: fishy
    :width: 200px
    ```
  key4: example
---

(myst-opational-syntax)=

# 可选的 MyST 扩展语法

MyST-Parser 是高度可配置的，利用了 [markdown-it-py](https://markdown-it-py.readthedocs.io/en/latest/index.html) 解析器固有的 “可插入性” 。以下语法是可选的（默认禁用），可以通过 Sphinx 启用`conf.py`（另请参阅 [Sphinx 配置选项](../sphinx/config.rst)。他们的目标通常是添加更多 *Markdown 友好的语法*；通常启用和呈现扩展 [CommonMark 规范](https://commonmark.org/) 的 [markdown-it-py](https://markdown-it-py.readthedocs.io/en/latest/plugins.html#md-plugins) 插件。

```{seealso} 查看所有可选的 MyST 扩展
在 [executablebooks/mdit-py-plugins](https://mdit-py-plugins.readthedocs.io/en/latest/) 中，详细说明了 MyST 支持的所有的扩展以及扩展的使用语法。当然，也可以直接前往 [MyST Parser -- Optional MyST Syntaxes](https://myst-parser.readthedocs.io/en/latest/syntax/optional.html) 的查看 MyST Parser 官网文档语法。
```

```python
myst_enable_extensions = [
    # 用于解析美元$和$$封装的数学和LaTeX 数学公式解析
    "dollarmath","amsmath",
    # 定义列表
    "deflist",
    # 冒号的代码围栏
    "colon_fence",
    # HTML 警告
    "html_admonition",
    # HTML 图像
    "html_image",
    # 智能引号与替换件
    "smartquotes","replacements",
    # 链接
    "linkify",
    # 替换
    "substitution",
    # 任务列表
    "tasklist"
]
```

## 排版

添加 `"smartquotes"` 到 `myst_enable_extensions`（在 sphinx conf.py 配置文件中）将自动将标准报价转换为它们的开始/结束变体：

- `'single quotes'`: 'single quotes'
- `"double quotes"`: "double quotes"

添加 `"replacements"` 到 `myst_enable_extensions`（在 sphinx conf.py 配置文件中）会自动转换一些常见的排版文本。

|        text        | converted |
| :----------------: | :-------: |
|  ``(c)``, ``(C)``  |    (c)    |
| ``(tm)``, ``(TM)`` |   (tm)    |
|  ``(r)``, ``(R)``  |    (r)    |
|  ``(p)``, ``(P)``  |    (p)    |
|       ``+-``       |    +-     |
|      ``...``       |    ...    |
|     ``?....``      |   ?....   |
|     ``!....``      |   !....   |
|    ``????????``    | ????????  |
|     ``!!!!!``      |   !!!!!   |
|      ``,,,``       |    ,,,    |
|       ``--``       |    --     |
|      ``---``       |    ---    |

(markdown-ext-syntax-linkify)=

## 链接

添加 `"linkify"` 到 `myst_enable_extensions`（在 sphinx conf.py 配置文件中，如果另外设置 `myst_linkify_fuzzy_links=False` ,则只有包含方案（例如http）的链接才会被识别为外部链接）将自动识别 bare 网址并添加超链接：

`www.example.com` -> www.example.com

仅匹配以 schema 开头的 URL，例如 `http://example.com`。

此扩展需要安装 [linkify-it-py](https://github.com/tsutsu3/linkify-it-py)。要么直接 `pip install linkify-it-py` 或通过 `pip install myst-parser[linkify]` 安装 Python 模块。

(markdown-ext-syntax-colon)=

## 使用冒号的代码围栏

通过添加`"colon_fence"`到`myst_enable_extensions`（在 sphinxconf.py 配置文件中），这样一来我们就还可以使用`:::`分隔符来表示代码围栏，而不是 ```` ``` ```` .

```
:::{note}
This text is **standard** _Markdown_
:::

:::{table} This is a **standard** _Markdown_ title
:align: center
:widths: grid

| abc | mnp | xyz |
| --- | --- | --- |
| 123 | 456 | 789 |
:::
```

> 运行渲染结果如下所示:

::::{card}

:::{note}
This text is **standard** _Markdown_
:::

:::{table} This is a **standard** _Markdown_ title
:align: center
:width: 50%

| abc | mnp | xyz |
| --- | --- | --- |
| 123 | 456 | 789 |
:::

::::

与 ```` ``` ```` 指令类似，这些指令也可以嵌套：

```
::::{important}
:::{note}
This text is **standard** _Markdown_
:::
::::
```

## 定义列表

通过添加 `"deflist"` 到 `myst_enable_extensions`（在 sphinx conf.py 配置文件中），您将能够使用定义列表。定义列表使用 [markdown-it-py deflist](https://markdown-it-py.readthedocs.io/en/latest/plugins.html#md-plugins) 插件，它本身基于 [Pandoc 定义列表规范](http://johnmacfarlane.net/pandoc/README.html#definition-lists)。

```
First Term
: This is the definition of the first term.
: > This is the definition of the first term.

Second Term
: This is one definition of the second term.
: This is another definition of the second term.
: ![tux](./../markdown/example/tux.png)
```

> 运行渲染如下：

:::{card}

First Term
: This is the definition of the first term.
: > This is the definition of the first term.

Second Term
: This is one definition of the second term.
: This is another definition of the second term.
: ![tux](./../markdown/example/tux.png)

:::

## 任务清单

任务列表使您可以创建带有复选框的项目列表。在支持任务列表的Markdown应用程序中，复选框将显示在内容旁边。要创建任务列表，请在任务列表项之前添加破折号（`-`）和方括号，并`[ ]`在其前面加上一个空格（）。要选择一个复选框，请`x`在方括号（`[x]`）之间添加in 。

通过添加 `"tasklist"` 到 `myst_enable_extensions`（在 sphinx conf.py 配置文件中），您将能够使用任务列表。任务列表利用 [markdown-it-py tasklists](https://markdown-it-py.readthedocs.io/en/latest/plugins.html#md-plugins) 插件。

```
- [x] Write the press release
- [ ] Update the website
- [ ] Contact the media
```

> 呈现的输出如下所示：

:::{card}

- [x] Write the press release
- [ ] Update the website
- [ ] Contact the media

:::

(myst-optional-syntax-img)=

## 图像

MyST 提供了几种不同的语法来在文档中包含图像:

* 第一个是标准的 Markdown 语法 `![fishy](img/fun-fish.png)` 。这种方法简单，但是，它在可以应用的配置方面受到限制，例如设置宽度
* 使用诸如指令 `image` 和 `figure` 

    ````
    ```{image} img/fun-fish.png
    :alt: fishy
    :class: bg-primary
    :width: 200px
    :align: center
    ```
    ````

* 最后一个选项是直接使用 HTML，它也由 MyST 解析。这通常是一个糟糕的选择，因为在构建过程中 HTML 被视为原始文本，因此 sphinx 不会识别要复制的图像文件，并且不会将 HTML 输出为非 HTML 输出格式。

通过添加`"html_image"`到`myst_enable_extensions`（在 sphinx conf.py 配置文件中），MySt-Parser 将尝试将任何孤立的 img 标签（即未包装在任何其他 HTML 中）转换为 sphinx 中使用的内部表示。

允许的属性等同于image指令：src、alt、class、width、height 和 name。任何其他属性都将被删除。

```
<img src="img/fun-fish.png" alt="fishy" width="200px">
<img src="img/fun-fish.png" alt="fishy" width="200px" class="bg-primary">
```

> 运行渲染结果：

```{card}
<img src="img/fun-fish.png" alt="fishy" width="200px">
<img src="img/fun-fish.png" alt="fishy" width="200px" class="bg-primary">
```

### 带有标题的图片

通过添加`"colon_fence"`到`myst_enable_extensions`（在 sphinx conf.py 配置文件中），我们可以组合上述两种扩展语法，以创建figure名为figure-md.

```
:::{figure-md} fig-target
:class: myclass

<img src="img/fun-fish.png" alt="fishy" class="bg-primary mb-1" width="200px">

This is a caption in **Markdown**
:::
```

> 运行渲染结果：

:::{figure-md} fig-target
:class: myclass

<img src="img/fun-fish.png" alt="fishy" class="bg-primary mb-1" width="200px">

This is a caption in **Markdown**
:::

## 替换

该扩展功能类似于 reST 的 {ref}`rest-syntax-replace`。

添加`"substitution"`到`myst_enable_extensions`（在 sphinx `conf.py` 配置文件中）将允许您添加替换功能。

* 全局替换。添加到 `conf.py` 中的 `myst_substitutions`：

    ```python
    # 全局替换
    myst_substitutions = {
    "key1": "I'm a **substitution**"
    }
    ```

* 局部替换，文件内替换。在文件的顶部添加替换文本，即在front-matter部分(见本节)。front-matter中的键值将在此文件中覆盖全局替换配置中的相同键的值:

    ```
    ---
    substitutions:
    key1: "I'm a **substitution**"
    key2: |
        ```{note}
        {{ key1 }}
        ```
    key3: |
        ```{image} img/fun-fish.png
        :alt: fishy
        :width: 200px
        ```
    key4: example
    ---
    ```

::::{tab-set}

:::{tab-item} MyST Markdown

```
Inline: {{ key1 }}

Block level:

{{ key2 }}

| col1     | col2     |
| -------- | -------- |
| {{key2}} | {{key3}} |
```

:::

:::{tab-item} 渲染结果

Inline: {{ key1 }}

Block level:

{{ key2 }}

| col1     | col2     |
| -------- | -------- |
| {{key2}} | {{key3}} |

:::

::::

### 替换的作用区间

替换只会在你通常使用 Markdown 的地方进行评估，即作用于 `.md` 文件；当然，除了那些代码块中的含有替换符的 `{{key1}}`，例如：

````
```
{{key1}}
```
````

```
{{key1}}
```

同时，还应该注意使用不合适的指令进行内联替换。这可能会导致意想不到的结果。

替换引用被评估为Jinja2表达式，该表达式可以使用[过滤器](https://jinja.palletsprojects.com/en/2.11.x/templates/#list-of-builtin-filters)，并且还包含上下文中的[Sphinx环境](https://www.sphinx-doc.org/en/master/extdev/envapi.html)(作为 `env` ,并通过 `env.config.xx variable name` 指向可以获取 `conf.py` 文件中所有的变量值 )。因此，你可以这样做:

```
- version: {{ env.config.version }}
- docname: {{ env.docname}}
- {{ "a" + "b" }}
- extensions = {{env.config.extensions | upper}}
```

- version: {{ env.config.version }}
- docname: {{ env.docname}}
- {{ "a" + "b" }}
- extensions = {{env.config.extensions | upper}}

### 替换和 URL

替换不能直接在url中使用，例如 `[a link](https://{{key4}}.com)` 或 `<https://{{key4}}.com>` 。然而，由于Jinja2的替换允许使用Python方法，你可以使用字符串格式或替换:

```
{{ '[a link](https://{}.com)'.format(key4) }}

{{ '<https://studynotes.readthedocs.io/zh/builder-doc/REPLACE.html>'.replace('REPLACE', env.docname) }}
```

{{ '[a link](https://{}.com)'.format(key4) }}

{{ '<https://studynotes.readthedocs.io/zh/builder-doc/REPLACE.html>'.replace('REPLACE', env.docname) }}


## 数学公式的语法支持

Math 是通过在 sphinx `conf.py` 配置文件中添加 `myst_enable_extensions` 列表选项来解析的:

* 用于解析被 `$` 和 `$$` 封装的数学。
* `amsmath` 用于直接解析 [amsmath LaTeX environments](https://ctan.org/pkg/amsmath) 。

这些选项启用了它们各自的 Markdown 解析器插件，详情请参见 [Markdown-it](https://markdown-it-py.readthedocs.io/en/latest/plugins.html#md-plugins) 插件指南。

````{important}

在 MyST Markdown 中，这两个选项需要配合使用才能发挥出最大功效。
```python
myst_enable_extensions = ["dollarmath", "amsmath"]
```
````

### 美元(`$`)分隔的数学

启用 `dollarmath` 将解析以下语法:

* Inline math (内联数学): `$...$`
* Display (block) math (块数学): `$$...$$`

另外，如果设置了 `myst_dmath_allow_labels=True` (默认值):

* Display (block) math with equation label (带有编号的块数学): `$$...$$ (1)`

````{dropdown} 带有编号的块数学示例
:open:

```
$$
e = mc^2
$$ (eqn:best)

This is the best equation {eq}`eqn:best`
```

$$
e = mc^2
$$ (eqn:best)

This is the best equation {eq}`eqn:best`
````

````{admonition} 扩展了解
:class: seealso

如果了解之前的语法，我们会发现可以使用角色指令来实现与美元分隔的数学，示例如下：

`$x_{hey}=it+is^{math}$` 被解析为 $x_{hey}=it+is^{math}$ 

同样的，通过以下角色指令可达到同样效果：

```rest
{math}`x_{hey}=it+is^{math}`
```

同时，如果是使用 Vs Code 编写文档，那么**可以通过美元分隔符号来触发 LaTeX 的代码提示**。

对于大部分的 LaTeX 支持的符号，在 MyST Markdown 中也能实现。具体的符号对应语法参考 [LaTeX Math Symbols](https://www.caam.rice.edu/~heinken/latex/symbols.pdf) 。
或者点击链接直接本地下载 {download}`》》symbols.pdf《《 <./example/symbols.pdf>`
````


```{admonition} 避免美元符号被解析
:class: tip

可以通过在第一个 `$` 符号前添加一个 `\` 来进行转义(否定)，例如 `\$a$` 呈现为 $a$。转义也可以在数学中使用，例如 `$a=\$3$` 呈现为 $a=\$3$。

相反， `\\` 将否定转义，所以 `\\$a$` 呈现为 \\$a$。

```

### LaTeX 数学

通过添加 `"amsmath"` 到 `myst_enable_extensions` （在 sphinx `conf.py` 配置文件中），您可以启用 `amsmath LaTeX` 方程的直接解析。然后将直接解析这些数学表达：

These *top-level math environments* (以标记语言的角度来说就像是指令) will then be directly parsed:

> equation, multline, gather, align, alignat, flalign, matrix, pmatrix, bmatrix, Bmatrix, vmatrix, Vmatrix, eqnarray.

同时，以 `*` 结尾的环境不会被编号:

```latex
\begin{gather*}
a_1=b_1+c_1\\
a_2=b_2+c_2-d_2+e_2
\end{gather*}

\begin{align}
a_{11}& =b_{11}&
  a_{12}& =b_{12}\\
a_{21}& =b_{21}&
  a_{22}& =b_{22}+c_{22}
\end{align}
```


\begin{gather*}
a_1=b_1+c_1\\
a_2=b_2+c_2-d_2+e_2
\end{gather*}

\begin{align}
a_{11}& =b_{11}&
  a_{12}& =b_{12}\\
a_{21}& =b_{21}&
  a_{22}& =b_{22}+c_{22}
\end{align}
