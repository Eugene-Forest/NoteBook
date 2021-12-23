
# Sphinx thebe

使您的代码单元与 [Thebe](http://thebelab.readthedocs.org/) 和 [Binder](https://mybinder.org) 提供的内核进行交互。

例如，单击下面的按钮。请注意，下面的代码块变为可编辑和可运行的！（由于网络问题，运行按钮可能会显示失败）

```{thebe-button} Launch thebe
```

```{code-block} python
:class: thebe

print("hi")
```

`````{toggle}
````{code-block} guess
:caption: 上方实例的源码
```{thebe-button} Launch thebe
```

```{code-block} python
:class: thebe

print("hi")
```
````
`````

## 配置运行环境

To install `sphinx-thebe` :

```{code-block} powershell
pip install sphinx-thebe
```

Then, add it to your Sphinx site’s `conf.py` file:

```{code-block} python
extensions = [
    ...
    "sphinx_thebe"
    ...
]

thebe_config = {
    "repository_url": "https://github.com/binder-examples/jupyter-stacks-datascience",
    "repository_branch": "master",
}
```

```{seealso}

在这里，笔者只是简单的提供一个关于实现交互式笔记的思路，更多关于 `thebe` 的信息前往其官方文档:

* [sphinx-thebe文档](https://sphinx-thebe.readthedocs.io/en/latest/use.html)
* [thebe 文档](https://thebe.readthedocs.io/en/latest/index.html)
* `thebe` 依靠于 `myst_nb` 解析；[MyST-NB 文档](https://myst-nb.readthedocs.io/en/latest/)

不过笔者现阶段不推荐使用 MyST Markdown 语法编写交互式笔记，如果读者有相关需要，那么推荐更加成熟的交互式笔记方案—— Jupyter Notebook 。`myst_nb` 能够解析 Jupyter Notebook(以`.ipynb`结尾)。
```

```{warning}
默认情况下，`sphinx-thebe` 将为 [jupyter-stacks-datascience](https://github.com/binder-examples/jupyter-stacks-datascience) 存储库提供 Binder 环境 。但是需要注意的是，这个是一个实验性的存储库，所以这并不是一个成熟的笔记方案。
```

```{toctree}
:caption: 交互式代码thebe文档实例
:maxdepth: 1

在md文件中使用thebe示例1 <./example/example>
在md文件中使用thebe示例2 <./example/exa>
在rst文件中使用thebe <./example/rst>
```
