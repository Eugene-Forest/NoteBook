# 基础语法

````{admonition} html 元素基础


```{image} ./image/grumpy-cat-small.png
:alt: grumpy-cat-small.png
```

这个元素的主要部分有：

-   开始标签（Opening tag）：包含元素的名称（本例为 p），被大于号、小于号所包围。表示元素从这里开始或者开始起作用——在本例中即段落由此开始。
-   结束标签（Closing tag）：与开始标签相似，只是其在元素名之前包含了一个斜杠。这表示着元素的结尾——在本例中即段落在此结束。初学者常常会犯忘记包含结束标签的错误，这可能会产生一些奇怪的结果。
-   内容（Content）：元素的内容，本例中就是所输入的文本本身。
-   元素（Element）：开始标签、结束标签与内容相结合，便是一个完整的元素。

----

```{image} ./image/grumpy-cat-attribute-small.png
:alt: grumpy-cat-attribute-small
```
属性包含了关于元素的一些额外信息，这些信息本身不应显现在内容中。本例中，`class` 是属性名称，`editor-note` 是属性的值。`class` 属性可为元素提供一个标识名称，以便进一步为元素指定样式或进行其他操作时使用。

````

## 模板

### 文本插值 Content

### 属性 Attribute

> HTML 中的元素拥有属性（attribute）；这些额外的值可以配置元素或者以各种方式来调整元素的行为，进而满足用户所需的标准。

### 指令 Directives

指令是带有 `v-` 前缀的特殊 attribute。

**然而，如果存在自定义指定，那么就不一定可以通过前缀来判断，这个要根据各自项目的约定和实际上下文来判断。**

//TODO: 指向一个用例用来说明

### 响应式数据

ref toRef 和 toRefs

### 计算属性
