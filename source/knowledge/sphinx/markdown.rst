==========================
markdown 支持
==========================

.. _markdown-support:


要配置您的Sphinx项目以支持 Markdown ，请按以下步骤进行：

#. 安装 Markdown 分析程序 推荐标记：

   .. code-block:: default

      pip install myst-parser


#. 添加 推荐标记 到 ``config.py`` 文件中 :

   .. code-block:: python

      extensions = ['myst_parser']



在 Sphinx 项目的“主文档”（Sphinx 文档的登录页面）中，包含myfile.md一个toctree指令，以便将其包含在您的文档中：

.. code-block:: rest

   .. toctree::

      myfile.md


.. attention:: 

   需要注意的是，如果是在.rst文件中的目录使用.md文件，需要指明文件的尾缀。