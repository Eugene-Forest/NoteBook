
# Sphinx 扩展工具使用指南

Sphinx 插件还有原生插件和非原生插件之分，原生插件的命名格式以 `sphinx.ext.` 开头，否则就是非原生插件（前提它是 Sphinx 插件），所有 Sphinx 插件都是需要在 `conf.py` 中被配置的。

对于原生插件，它是不需要在 ``requirements`` 相关文件中添加的，需要添加到在 requirements[^1] 相关文件的插件是那些非原生插件。

直接在 `conf.py` 文件中的 `extensions` 数组中添加插件名字符串后，然后添加一些其他配置代码的情况下即可直接生效。 例如 `sphinx_copybutton` 插件：

```python
# In your conf.py configuration file, add sphinx_copybutton to your extensions list. E.g.:

extensions = [
    ...
    'sphinx_copybutton'
    ...
]

#若要定义要从代码块中复制的文本中删除的提示文本
copybutton_prompt_text = "myinputprompt"
```

```{toctree}
:maxdepth: 2

响应式 Web 组件的 Sphinx 扩展—— Sphinx Design <design/design-index>
下拉框按钮—— sphinx-togglebutton <togglebutton>
选项卡工具—— Sphinx tabs <./tab>
```

```{dropdown} 其他插件
:open:
* [sphinx_copybutton](https://sphinx-copybutton.readthedocs.io/en/latest/)
* {ref}`sphinx_book_theme 主题配置 <sphinx-sbt-theme-config>`
```

[^1]: requirements 相关文件指的是 [pip 要求文件](https://pip.pypa.io/en/latest/user_guide/#requirements-files) , 因为我们在推送到 Read The Docs 平台时，它是不知道我们项目所需要的 Python 依赖模块的，所以需要我们添加 **pip 要求文件** 来构建你的文档；[点击查看pip 要求文件样式要求](https://pip.pypa.io/en/latest/reference/requirements-file-format/#requirements-file-format)。
    点击查看关于 [Sphinx 配置](../sphinx/config.rst) 文档笔记。
