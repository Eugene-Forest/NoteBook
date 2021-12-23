(myst-nb)=

# MyST-NB

> **更新时间: 2021-12-21, 11:46:56  | myst_nb 版本：{{myst_nb}}**

默认情况下，`MyST-NB` 会同时解析 markdown(`.md`) 和 notebooks(`.ipynb`)。如果您在文档中使用 `MyST-NB`，请不要激活 `myst-parser`. 它将被 `myst-nb` 自动激活（因为 `myst-nb` 依赖于 `myst-parser`）。

本节介绍如何开始使用`MyST-NB` `Sphinx`扩展。`Sphinx`扩展允许您读取markdown (`.md`)和Jupyter笔记本(`.ipynb`)文件到您的`Sphinx`网站。它还允许您在页面中编写`MyST markdown`。

**MyST-NB 主要工具是ipynb文件的 Sphinx 解析器。这允许您直接将 Jupyter Notebooks 转换为 Sphinx 文档，即在 Sphinx 中解析和执行 ipynb 文件。**

要开始使用扩展，可以遵循以下步骤：

* 使用以下命令安装myst-nb:

    ```shell
    pip install myst-nb
    ```

* 在你的`Sphinx`站点中激活myst_nb扩展名，把它添加到`conf.py`中的`Sphinx`扩展名列表中:

    ```python
    extensions = [
        ...,
        "myst_nb"
    ]
    source_suffix = {
    '.rst': 'restructuredtext',
    '.ipynb': 'myst-nb',
    '.myst': 'myst-nb',
    }
    ```

* 将MyST和笔记本内容添加到文档的源文件中。`Sphinx`现在可以解析使用`MyST markdown`编写的markdown文件，Jupyter笔记本(以`.ipynb`结尾)，以及使用`MyST markdown`编写的纯文本的Jupyter笔记本。请确保在``Sphinx` toctree`指令中包含到内容的路径!

* 建立你的文档。`MyST-NB`现在将解析任何markdown (`.md`)、Jupyter笔记本(`.ipynb`)和基于文本的笔记本(``.md``)到`Sphinx`站点，并将它们包含在输出中。（当然，如果你使用`reStructureText`编写文档，那么`Sphinx`将会根据其默认解析器解析 (`.rst`)）。
