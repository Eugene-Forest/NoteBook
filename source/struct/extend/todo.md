# `sphinx.ext.todo` 

该插件提供了对 ``TODO`` 项的支持，使用此扩展时有两个附加指令( rest 语法 )：

* ``.. todo::`` 
* ``.. todolist::`` (``todolist`` 指令暂时不知道写法，也可能 *sphinx_book_theme* 主题不支持此指令)

只有在 Sphinx 配置文件中添加扩展以及扩展配置才能使得附加指令生效。

```python
extensions = [
    "sphinx.ext.todo",
]
todo_include_todos = True
```

```{note}
``todo`` 指令于 1.3.2 新版功能: 此指令支持 class 用于确定HTML输出的类属性的选项。如果未给定，则类默认为 ``admonition-todo`` .

我们可以通过改变 todo 指令的 class 值来改变，如同 admonition 指令一样，大体来说， ``class`` 值的不同在 *sphinx_boot_theme* 主题中的 表现/颜色可以用以下这些值表示 ： ``warning`` 、 ``danger`` (红色) ， ``seealso`` (绿色) ， ``note`` (蓝色) 、 ``hint`` 、 ``tip`` (黄色) ， ``attention`` ``caution`` (橙色)

```

```{todo}

don't have class

```

```{todo}
:class: warning

class values is warning

```

```{todo}
:class: attention

class values is attention

```

```{todo}
:class: tip

class values is tip

```

```{todo}
:class: seealso

class values is seealso

```

## `config.py` 配置

`todo_include_todos`
: 如果这是 True ， todo 和 todolist 产出，否则什么也不产出。默认值为 False .

`todo_emit_warnings`
: 如果这是 True ， todo 对每个TODO条目发出警告。默认值为 False . (1.5 新版功能.)

`todo_link_only`
: 如果这是 True ， todolist 生成不带文件路径和行的输出，默认为 False . (1.4 新版功能.)

```{note}

AutoDoc提供以下附加事件：

`todo-defined(app, node)`
: 在定义TODO时发出。 node 是定义的 sphinx.ext.todo.todo_node 节点。 (1.5 新版功能.)
```
