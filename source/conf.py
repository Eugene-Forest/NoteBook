# -*- coding: utf-8 -*-
#
# NoteBook documentation build configuration file, created by
# sphinx-quickstart on Thu Jan 28 12:27:57 2021.
#
# This file is execfile()d with the current directory set to its containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

import sys
import os

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#sys.path.insert(0, os.path.abspath('.'))

# -- General configuration -----------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be extensions
# coming with Sphinx (named 'sphinx.ext.*') or your custom ones.
# 在这里以字符串的形式添加任何Sphinx扩展模块名。
extensions = [
    "sphinx.ext.todo",
    # label 标签自动选中确保唯一性,并允许引用节使用其标题,同时自动为标题创建label
    "sphinx.ext.autosectionlabel",
    # myst 解析器, 默认情况下，myst_parser 会解析 markdown(.md) ,而 .rst 文件会被 Sphinx 原生解析器 restructureText 解析。
    # 'myst_parser',
    "myst_nb",
    # 使您的代码单元与Thebe和Binder提供的内核进行交互。
    "sphinx_thebe",
    # 用于设计美观、视图大小的响应式 Web 组件。
    "sphinx_design",
    # 代码块复制按钮扩展
    "sphinx_copybutton",
    # tab 面板插件
    'sphinx_tabs.tabs',
    # 折叠警告（注释、警告等）的功能按钮
    "sphinx_togglebutton",
    # 美人鱼，通过代码生成时序图等
    "sphinxcontrib.mermaid",
    # 博客
    # 'ablog',
    # 评论区
    # "sphinx_comments",
]

# Make sure the target is unique
autosectionlabel_prefix_document = True

todo_include_todos = True

# 控制切换按钮悬停文本
togglebutton_hint = "展示隐藏内容"

thebe_config = {
    "repository_url": "https://github.com/binder-examples/jupyter-stacks-datascience",
    "repository_branch": "master",
}

myst_enable_extensions = [
    "colon_fence",
    "deflist",
    "tasklist",
    "smartquotes", "replacements",
    "linkify",
    "html_image",
    "substitution"
]
# 如果为false,只有包含方案（例如http）的链接才会被识别为外部链接
myst_linkify_fuzzy_links = False
# myst_footnote_transition = True
# myst_dmath_double_inline = True

# substitution 的扩展的全局替换，作用于 .md
myst_substitutions = {
    "Sphinx": "4.3.2",
    "sphinx_autobuild": "2021.3.14",
    "sphinx_book_theme": "0.1.7",
    "myst_parser": "0.15.2",
    "myst_nb": "0.13.1",
    "Markdown": "3.3.4",
    "markdown_it_py": "1.1.0",
    "sphinx_tabs": "3.2.0",
    "sphinx_thebe": "0.0.10",
    "sphinx_togglebutton": "0.2.3",
    "sphinx_design": "0.0.13",
    "sphinx_copybutton": "0.4.0",
}
# default is ['{', '}']，替换指令分隔符，不建议更改
# myst_sub_delimiters = ["|", "|"]

# 评论区扩展功能配置样例
# comments_config = {
#     "hypothesis": True,
#     "dokieli": False,
#     "utterances": {
#         "repo": "xinetzone/sphinx-demo",
#         "optional": "config",
#     }
# }

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix of source filenames.
# old config : source_suffix = '.rst'
# Here is new configuration
source_suffix = ['.rst', '.md']

# The encoding of source files.
# 建议的编码和默认值是 'utf-8-sig' .
source_encoding = 'utf-8-sig'

# The master toctree document.
# “主控”文档的文档名称，即包含根目录的文档 toctree 指令。
# 在 2.0 版更改: 默认值更改为 'index' 从 'contents' .
master_doc = 'index'

# ------ General information about the project. ---------------------

# project name
project = u' 尤金的一己之见 '

# 版权，著作权
copyright = u'2021, Eugene Forest'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version. 主要项目版本，用作 |version| .
version = 'alpha'
# The full version, including alpha/beta/rc tags. 完整的项目版本，用作 |release|
release = 'alpha'

# -------  End of the configuration of project's general info ----------

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
language = 'zh_CN'

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
#today = ''
# Else, today_fmt is used as the format for a strftime call.
today_fmt = "%Y-%m-%d, %H:%M:%S"

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = []

# The reST default role (used for this markup: `text`) to use for all documents.
#default_role = None

# If true, '()' will be appended to :func: etc. cross-reference text.
#add_function_parentheses = True

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
#add_module_names = True

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
#show_authors = False

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# A list of ignored prefixes for module index sorting.
#modindex_common_prefix = []


# -- Options for HTML output ---------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
# html_theme = 'default'
# html_theme = 'sphinx_rtd_theme'
html_theme = "sphinx_book_theme"

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
# html_theme_options = {}

# 以下为 sphinx_book_theme 的主题配置/定制（sphinx_book_theme）
html_theme_options = {
    # （仅限开发人员）触发一些功能，使开发主题更容易。默认 `False`
    # "theme_dev_mode": False,

    # ----------------主题内容中导航栏的功能按钮配置--------
    # 添加存储库链接
    "repository_url": "https://github.com/Eugene-Forest/NoteBook",
    # 添加按钮以链接到存储库
    "use_repository_button": True,
    # 要添加按钮以打开有关当前页面的问题
    "use_issues_button": True,
    # 添加一个按钮来建议编辑
    "use_edit_page_button": True,
    # 在导航栏添加一个按钮来切换全屏的模式。
    "use_fullscreen_button": True,  # 默认 `True`
    # 默认情况下，编辑按钮将指向master分支，但如果您想更改此设置，请使用以下配置
    "repository_branch": "main",
    # 默认情况下，编辑按钮将指向存储库的根目录；而我们 sphinx项目的 doc文件其实是在 source 文件夹下的，包括 conf.py 和 index(.rst) 主目录
    "path_to_docs": "source",
    # 您可以添加 use_download_button 按钮，允许用户以多种格式下载当前查看的页面
    "use_download_button": True,

    # --------------------------右侧辅助栏配置---------
    # 重命名右侧边栏页内目录名，标题的默认值为Contents。
    "toc_title": "导航",
    # -- 在导航栏中显示子目录，向下到这里列出的深度。 ----
    "show_toc_level": 2,
    # --------------------------左侧边栏配置--------------
    # -- 只显示标识，不显示 `html_title`，如果它存在的话。-----
    "logo_only": True,
    # 控制左侧边栏列表的深度展开,默认值为1，它仅显示文档的顶级部分
    "show_navbar_depth": 1,
    # 自定义侧边栏页脚,默认为 Theme by the Executable Book Project
    # "extra_navbar": "<p>Your HTML</p>",
    "home_page_in_toc": False,  # 是否将主页放在导航栏（顶部）
    # ------------------------- 单页模式 -----------------
    # 如果您的文档只有一个页面，并且您不需要左侧导航栏，那么您可以 使用以下配置将其配置sphinx-book-theme 为以单页模式运行
    # "single_page": True,

    # 用于交互的启动按钮
    # Thebe将您的静态代码块转换 为由 Jupyter 内核提供支持的交互式代码块。它通过要求一个BinderHub内核做到这一点 的引擎盖下，您的所有代码细胞转换成互动码单元。这允许用户在不离开页面的情况下在您的页面上运行代码。
    # "launch_buttons": {
    #     "binderhub_url": "https://mybinder.org",
    #     # 控制打开的用户界面
    #     "notebook_interface": "jupyterlab",
    #     "thebe": True,
    # },
    # -- 在每个页面的页脚添加额外的 HTML。---
    # "extra_footer": '',
}

# Add any paths that contain custom themes here, relative to this directory.
#html_theme_path = []

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
#html_title = None

# A shorter title for the navigation bar.  Default is the same as html_title.
#html_short_title = None

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
#html_logo = None

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
#html_favicon = None

# 自定义徽标、和网站图标
html_logo = "./_static/notebook-badge.svg"
# html_logo = "./_static/notebook-logo.svg"
html_favicon = "./_static/notebook-badge.svg"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
# html_static_path = ['_static']

# 添加你自己的 CSS 规则
html_static_path = ['_static']
html_css_files = ["custom.css"]

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
#html_last_updated_fmt = '%b %d, %Y'

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
#html_use_smartypants = True

# Custom sidebar templates, maps document names to template names.
# 通过html文件定制主侧栏
#html_sidebars = {}

# Additional templates that should be rendered to pages, maps page names to
# template names.
#html_additional_pages = {}

# If false, no module index is generated.
#html_domain_indices = True

# If false, no index is generated.
#html_use_index = True

# If true, the index is split into individual pages for each letter.
#html_split_index = False

# If true, links to the reST sources are added to the pages.
#html_show_sourcelink = True

# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
#html_show_sphinx = True

# If true, "(C) Copyright ..." is shown in the HTML footer. Default is True.
#html_show_copyright = True

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
#html_use_opensearch = ''

# This is the file name suffix for HTML files (e.g. ".xhtml").
#html_file_suffix = None

# Output file base name for HTML help builder.
htmlhelp_basename = 'NoteBookdoc'


# -- Options for LaTeX output --------------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    # 'papersize': 'letterpaper',

    # The font size ('10pt', '11pt' or '12pt').
    # 'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    # 'preamble': '',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title, author, documentclass [howto/manual]).
latex_documents = [
    ('index', 'NoteBook.tex', u'NoteBook Documentation',
     u'Eugene Forest', 'manual'),
]

# The name of an image file (relative to this directory) to place at the top of
# the title page.
#latex_logo = None

# For "manual" documents, if this is true, then toplevel headings are parts,
# not chapters.
#latex_use_parts = False

# If true, show page references after internal links.
#latex_show_pagerefs = False

# If true, show URL addresses after external links.
#latex_show_urls = False

# Documents to append as an appendix to all manuals.
#latex_appendices = []

# If false, no module index is generated.
#latex_domain_indices = True


# -- Options for manual page output --------------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    ('index', 'notebook', u'NoteBook Documentation',
     [u'Eugene Forest'], 1)
]

# If true, show URL addresses after external links.
#man_show_urls = False


# -- Options for Texinfo output ------------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    ('index', 'NoteBook', u'NoteBook Documentation',
     u'Eugene Forest', 'NoteBook', 'One line description of project.',
     'Miscellaneous'),
]

# Documents to append as an appendix to all manuals.
#texinfo_appendices = []

# If false, no module index is generated.
#texinfo_domain_indices = True

# How to display URL addresses: 'footnote', 'no', or 'inline'.
#texinfo_show_urls = 'footnote'

# -- global replace order configuration are as follows---
# 全局字符串替换指令
# 需要注意的是，全局加入替换的功能要谨慎使用，要酌情使用；因为在这里添加后会影响到项目所有的 rst 文件（在所有 rst 文件中添加定义的替换指令）
# 一串 reStructuredText，它将包含在每个读取的源文件的末尾。 这是一个可以添加应该在每个文件中可用的替换的地方
rst_prolog = """
.. |15| raw:: html
      
      <hr width='15%'>

.. |30| raw:: html
      
      <hr width='30%'>
      
.. |50| raw:: html
      
      <hr width='50%'>

.. |75| raw:: html
      
      <hr width='75%'>

.. |mysql| replace:: **MySQL**

.. |mssql| replace:: **SQL Server**

"""
# ".. |java| replace::  **Java**"
# ".. |centos| replace:: **CentOS 7.x**"
# ".. |idea| replace:: **IntelliJ IDEA**"


# 图片编号功能
# -- numfig configuration are as follows---
# 表格和代码块如果有标题则会自动编号
numfig = True
# -- numfig_secnum_depth configuration are as follows---
# 如果设置为“0”，则数字，表格和代码块从“1”开始连续编号。
# 如果“1”(默认)，数字将是“x.1”。“x.2”，… 与“x”的节号(顶级切片;没有“x”如果没有部分)。只有当通过 toctree 指令的“:numbered:”选项激活了段号时，这才自然适用。
# 如果“2”，表示数字将是“x.y.1”，“x.y.2”，…如果位于子区域(但仍然是 x.1 ，x.2 ，… 如果直接位于一个部分和 1 ，2 ， … 如果不在任何顶级部分。)
numfig_secnum_depth = 2
# -- numfig_format configuration are as follows---
# 一个字典将“‘figure’”，“‘table’”，“‘code-block’”和“‘section’”映射到用于图号格式的字符串。作为一个特殊字符，“%s”将被替换为图号。
# 默认是使用“‘Fig.%s’”为“‘figure’”, “‘Table%s’”为“‘table’”，“‘Listing%s’”为“‘code-block’”和“‘Section’”为 “‘section’”。
numfig_format = {'code-block': '代码块 %s', }
# -- html_codeblock_linenos_style configuration are as follows---
# 代码块的行号样式
html_codeblock_linenos_style = 'table'
# html_codeblock_linenos_style = 'inline'
