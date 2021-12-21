=====================
HTML Theme
=====================

.. _sphinx-html-theme:


本篇章用来讲解 Sphinx 项目的主题设置, Sphinx 项目的默认主题为 "default". 不过由于 default 主题比较难看所以一般都是将主题换为 ``sphinx_rtd_theme`` .

.. note:: 

    可以前往 :ref:`Sphinx Theme 官网 <https://sphinx-themes.org/>` 查看 Sphinx 支持的所有的主题. 

.. important:: 

    需要注意的是, Sphinx 项目的主题需要在 ``conf.py`` 文件中配置.


|75|

sphinx_rtd_theme 主题配置
===========================

.. code-block:: python
   :caption: sphinx_rtd_theme 主题配置
   :linenos:

   # 头部添加导入
   import sphinx_rtd_theme
   # 找到主题属性更改如下
   html_theme = 'sphinx_rtd_theme'

对于 sphinx_rtd_theme 主题，笔者并没有深入了解其配置，如果读者需要了解可 `点击链接前往官方文档学习 sphinx_rtd_theme 主题配置 <https://sphinx-rtd-theme.readthedocs.io/en/stable/index.html>`_ 。

.. _sphinx-sbt-theme-config:

sphinx_book_theme 主题配置
==============================

对于 sphinx_book_theme 主题，如果读者有需要，可 `点击链接前往官方文档学习 sphinx_book_theme 主题配置 <https://sphinx-book-theme.readthedocs.io/en/latest/index.html>`_ 。

.. note:: 

   之所以使用该主题，是为了适应使用 MyST 标记语言的使用，而且 sphinx_rtd_theme 与 sphinx_book_theme 相比，主题不够柔和，而 sphinx_book_theme 还支持 MyST 的一些特殊语法支持如侧边栏的使用。


.. code-block:: python
   :caption: sphinx_book_theme 主题配置
   :linenos:

   # 头部添加导入
   import sphinx_book_theme
   # 找到主题属性更改如下
   html_theme = 'sphinx_book_theme'
   # 以下为 sphinx_book_theme 的主题配置/定制（sphinx_book_theme）
   html_theme_options = {
      # ----------------主题内容中导航栏的功能按钮配置--------
      # 添加存储库链接
      "repository_url": "https://github.com/Eugene-Forest/NoteBook",
      # 添加按钮以链接到存储库
      "use_repository_button": True,
      # 要添加按钮以打开有关当前页面的问题
      "use_issues_button": True,
      # 添加一个按钮来建议编辑
      "use_edit_page_button": True,
      # 默认情况下，编辑按钮将指向master分支，但如果您想更改此设置，请使用以下配置
      "repository_branch": "main",
      # 默认情况下，编辑按钮将指向存储库的根目录；而我们 sphinx项目的 doc文件其实是在 source 文件夹下的，包括 conf.py 和 index(.rst) 主目录
      "path_to_docs": "source",
      # 您可以添加 use_download_button 按钮，允许用户以多种格式下载当前查看的页面
      "use_download_button": True,

      # --------------------------右侧辅助栏配置---------
      # 重命名右侧边栏页内目录名，标题的默认值为Contents。
      "toc_title": "页内目录",
      # 通常，右侧边栏页内目录中仅显示页面的第 2 级标题，只有当它们是活动部分的一部分时（在屏幕上滚动时），才会显示更深的级别。可以使用以下配置显示更深的级别，指示应显示多少级别
      "show_toc_level": 2,

      # --------------------------左侧边栏配置--------------
      # logo 配置
      "logo_only": True,
      # 控制左侧边栏列表的深度展开,默认值为1，它仅显示文档的顶级部分
      "show_navbar_depth": 1,
      # 自定义侧边栏页脚,默认为 Theme by the Executable Book Project
      # "extra_navbar": "<p>Your HTML</p>",
      "home_page_in_toc": True,
      # ------------------------- 单页模式 -----------------
      # 如果您的文档只有一个页面，并且您不需要左侧导航栏，那么您可以 使用以下配置将其配置sphinx-book-theme 为以单页模式运行
      # "single_page": True,
   }

.. code-block:: python
   :caption: 通用配置
   :linenos:

   # 添加你自己的 CSS 规则
   html_static_path = ['_static']
   html_css_files = ["custom.css"]
   # 自定义徽标、和网站图标
   html_logo = "./_static/his-own.svg"
   html_favicon = "./_static/notebook.svg"
   
