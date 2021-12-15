==============
Sphinx 配置
==============


简单来说， Sphinx 项目中的 ``conf.py`` 文件就是该项目的配置文件，而例如 ``.readthedocs.yaml`` 、 ``requirement.txt`` 文件是在部署在 Read The Docs 网站上是的项目运行环境配置文件。

配置文件：

* ``.readthedocs.yaml`` : Sphinx 项目的运行环境的宏观配置
* ``requirement.txt`` : Sphinx 项目的 python 依赖包 的运行环境配置。当然这类依赖导入文件的命名是无所谓的，只要是 ``.txt`` 并在 ``.readthedocs.yaml`` 中引用即可。
* ``conf.py`` : Sphinx 项目的内部配置

.readthedocs.yaml
========================

Sphinx 项目的运行环境的宏观配置，包括指向Sphinx 项目的 python 依赖包 的运行环境配置文件。这是推荐的设置项目的方法。在使用此配置文件时， Read The Docs 项目的 ``管理 --> 高级设置 --> Default settings`` 列出的设置将被忽略。


Read The Docs 支持使用 YAML 文件配置文档构建。 **该配置文件必须在你的项目的根目录下** ，并命名 ``.readthedocs.yaml``。 

.. literalinclude:: ./example/example.yaml
   :language: yaml
   :linenos:
   :caption: YAML 文件配置示例

如果想要了解更多关于 YAML 文件配置， `点击前往 <https://docs.readthedocs.io/en/stable/config-file/v2.html>`_  。

需要注意文件的路径问题。在官方的文档中，Sphinx 项目是在项目文件夹下名为 docs 文件夹下新建的，所以在项目最外层与 ``README.md`` 同级的情况下， ``requirement.txt`` 放在项目最外层，那么它的路径为 ``docs/requirement.txt`` 。

requirement.txt
==========================

Sphinx 项目的 python 依赖包 的运行环境配置。当然这类依赖导入文件的命名是无所谓的，只要是 ``.txt`` 并在 ``.readthedocs.yaml`` 中引用即可。

因为我们在推送到 Read The Docs 平台时，它是不知道我们项目所需要的 Python 依赖模块的，所以需要我们添加 `pip 要求文件 <https://pip.pypa.io/en/latest/user_guide/#requirements-files>`_  来构建文档； `点击查看pip 要求文件样式要求 <https://pip.pypa.io/en/latest/reference/requirements-file-format/#requirements-file-format>`_ 。

.. literalinclude:: ./example/example.txt
   :language: guess
   :linenos:
   :caption: requirement.txt 文件配置示例

conf.py
==============

以下文本项目的实际配置文件。

.. important:: 

   更多详细内容请学习官方文档的 `配置篇 <https://www.osgeo.cn/sphinx/usage/configuration.html>`_ 

.. literalinclude:: ../../conf.py
   :language: python
   :caption: 项目的实际 conf.py
   :linenos:
