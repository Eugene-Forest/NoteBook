# 标签选项卡

选项卡组织并允许在相同层次结构的相关内容组之间进行导航。每个选项卡应该包含与集合中其他选项卡不同的内容。

::::{tab-set}

:::{tab-item} Label1
Content 1
:::

:::{tab-item} Label2
Content 2
:::

::::

`````{dropdown} Syntax
:icon: code
:color: light

````{tab-set-code}
```{literalinclude} ./snippets/myst/tab-basic.txt
:language: markdown
```
```{literalinclude} ./snippets/rst/tab-basic.txt
:language: rst
```
````
`````

## 同步选项卡

使用 `sync` 选项来跨多个选项卡集同步选中的选项卡项。注意，同步需要启用JavaScript。

::::{tab-set}

:::{tab-item} Label1
:sync: key1

Content 1
:::

:::{tab-item} Label2
:sync: key2

Content 2
:::

::::

::::{tab-set}

:::{tab-item} Label1
:sync: key1

Content 1
:::

:::{tab-item} Label2
:sync: key2

Content 2
:::

::::

`````{dropdown} Syntax
:icon: code
:color: light

````{tab-set-code}
```{literalinclude} ./snippets/myst/tab-sync.txt
:language: markdown
```
```{literalinclude} ./snippets/rst/tab-sync.txt
:language: rst
```
````
`````

## 选项卡式的代码示例

The `tab-set-code` directive provides a shorthand for synced code examples.
You can place any directives in a `tab-set-code` that produce a `literal_block` node with a `language` attribute, for example `code`, `code-block` and `literalinclude`.
Tabs will be labelled and synchronised by the `language` attribute (in upper-case).

`tab-set-code`指令为同步代码示例提供了一种简写方式。你可以在 `tab-set-code` 中放置任何指令，从而产生带有`language`属性的`literal_block`节点，例如 `code` ， `code-block` 和`literalinclude`。标签将被标记并通过`language`属性(大写)进行同步。

````{tab-set-code}

```{literalinclude} ./snippets/snippet.py
:language: python
```

```{code-block} javascript
a = 1;
```

````

```````{tab-set}

``````{tab-item} Markdown
:sync: markdown

````{literalinclude} ./snippets/myst/tab-code-set.txt
:language: markdown
````
``````

``````{tab-item} RST
:sync: rst

````{literalinclude} ./snippets/rst/tab-code-set.txt
:language: rst
````
``````

```````

## 其他组件中的选项卡

Tabs can be nested inside other components, such as inside [dropdowns](./dropdowns.md) or within [grid items](./grids.md).

:::::{dropdown} Tabs in dropdown
:open:

Paragraph

::::{tab-set}

:::{tab-item} Label1
:sync: label-1

Content 1
:::

:::{tab-item} Label2
:sync: label-2

Content 2
:::

::::
:::::

::::::{grid} 1 1 2 2

:::::{grid-item}
:outline:

Initial paragraph

::::{tab-set}

:::{tab-item} Label1
:sync: label-1

Content 1
:::

:::{tab-item} Label2
:sync: label-2

Content 2
:::

::::

:::::

:::::{grid-item}
:outline:

::::{tab-set}

:::{tab-item} Label1
:sync: label-1

Content 1
:::

:::{tab-item} Label2
:sync: label-2

Content 2
:::

::::

Ending paragraph

:::::

::::::

## `tab-set` options

```{eval-rst}
.. include:: ./snippets/tab-set-option.rst
```


## `tab-item` options

```{eval-rst}
.. include:: ./snippets/tab-item-option.rst
```
