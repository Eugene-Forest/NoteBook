====================
reStructuredText
====================

reStructuredText 是Sphinx使用的默认纯文本标记语言。本节简要介绍 reStructuredText（reST）的概念和语法，旨在为作者提供足够的信息，以便高效地编写文档。

本章节目的是讲解 reStructuredText 的语法以及对应的渲染结果，所以需要频繁变动指令和查看结果。虽然 VS Code 支持 reStructuredText 原生语法和 ``.rst`` 文件的预览功能，但是需要等待渲染，所以效率还是比较差的；为此，我们可以使用 :ref:`sphinx-autobuild 插件 <sphinx-ext-autobuild>`，它能够支持在浏览器中实时重新加载有关更改的 Sphinx 文档。

.. important:: 

   1) `reStructureText 学习文档（Created using Sphinx 5.0.0+） <https://www.sphinx-doc.org/zh_CN/master/usage/restructuredtext/basics.html>`_ 


.. warning:: 

   需要注意的是，在本篇章笔记中记录的知识部分语法；更多详细全面的语法请前往上文提供的官方文档中学习。

.. toctree::
   :caption: reStructureText 笔记目录
   :maxdepth: 3
   
   标题学习 <title>
   基础杂糅 <basic>
   指令 <order>
   表格 <Table>
   表格指令 <table-directive>
   使用文件 <usingFile>
   代码显示 <UsingFileCode>
   角色 <roles>
   域 <domains>
   推荐文章形式 <recommend-format>
   文章类笔记推荐写法 <recommend-format-txt>
