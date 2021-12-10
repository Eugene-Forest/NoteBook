==============
配置
==============


简单来说， sphinx 项目中的 ``conf.py`` 文件就是该项目的配置文件，而例如 ``.readthedocs.yaml`` 、 ``requirement.txt`` 文件是在部署在 Read The Docs 网站上是的项目运行环境配置文件。

配置文件：

* ``conf.py`` : sphinx 项目的内部配置
* ``.readthedocs.yaml`` : sphinx 项目的运行环境的宏观配置
* ``requirement.txt`` : sphinx 项目的 python 依赖包 的运行环境配置。当然这类依赖导入文件的命名是无所谓的，只要是 ``.txt`` 并在 ``.readthedocs.yaml`` 中引用即可。

.. note:: 

   需要注意文件的路径问题。在官方的文档中，sphinx 项目是在项目文件夹下名为 docs 文件夹下新建的，所以在项目最外层与 ``README.md`` 同级的情况下， ``requirement.txt`` 放在项目最外层，那么它的路径为 ``docs/requirement.txt`` 。

conf.py
==============

以下文本项目的实际配置文件。

.. important:: 

   更多详细内容请学习官方文档的 `配置篇 <https://www.osgeo.cn/sphinx/usage/configuration.html>`_ 

.. literalinclude:: ../../conf.py
   :language: python





