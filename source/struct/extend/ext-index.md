
# Sphinx 扩展工具使用指南

Sphinx 插件分为两种，一种是即插即用型，另一种是配置型。Sphinx 插件还有原生插件和非原生插件之分，原生插件的命名格式以 `sphinx.ext.` 开头，否则就是非原生插件（前提它是 Sphinx 插件）。

## 即插即用型插件

所谓即插即用型插件，即直接在 conf.py 文件中的 extensions 数组中添加插件名字符串后，不添加其他配置代码的情况下即可直接生效。 例如 sphinx_copybutton 插件：

```python
# In your conf.py configuration file, add sphinx_copybutton to your extensions list. E.g.:

extensions = [
    ...
    'sphinx_copybutton'
    ...
]
```


> 即插即用型插件可以直接使用，但是并不意味着没有办法配置。

就目前而言，项目所使用的所有插件中，属于即插即用的有：

* [sphinx_copybutton](https://sphinx-copybutton.readthedocs.io/en/latest/)
* [Sphinx tabs](https://sphinx-tabs.readthedocs.io/en/latest/)

```{toctree}

切换按钮—— sphinx-togglebutton <togglebutton>
选项卡工具—— Sphinx tabs <./tab>

```


## 配置型插件

同理，所谓配置型插件，即在 conf.py 文件中的 extensions 数组中添加插件名字符串后，还必须需要再配置文件中添加其他配置属性才能生效。以下是配置型插件的目录：

```{toctree}

响应式 Web 组件的 Sphinx 扩展—— Sphinx Design <design/design-index>

```
