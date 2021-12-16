===============
准备部分
===============

.. note:: 

   Sphinx 项目需要 Python 环境来支持,在此不对如何安装 Python 进行说明. 有需要的可以通过 `Python官网 <https://www.python.org/>`_ 单独下载.


安装 Sphinx 并下载必要的包
------------------------------

安装 Sphinx 库以及 ``sphinx-rtd-theme`` 主题库。

.. code-block:: guess

   pip install sphinx
   pip install sphinx-rtd-theme  


|30|

在项目根目录运行生成文档命令 ``sphinx-quickstart``
---------------------------------------------------


.. code-block:: shell

    > sphinx-quickstart

   Welcome to the Sphinx 3.4.3 quickstart utility.

   Please enter values for the following settings (just press Enter to
   accept a default value, if one is given in brackets).

   Selected root path: .

   # 是否分离source和build目录（输入y,选择分离，方便管理）
   You have two options for placing the build directory for Sphinx output.
   Either, you use a directory "_build" within the root path, or you separate
   "source" and "build" directories within the root path.
   > Separate source and build directories (y/n) [n]: y

   # 配置项目名，作者名，以及项目版本号
   The project name will occur in several places in the built documentation.
   > Project name: EnglishWorld
   > Author name(s): Eugene Forest
   > Project release []: 1.0   

   If the documents are to be written in a language other than English,
   you can select a language here by its language code. Sphinx will then
   translate text that it generates into that language.

   # 配置文档语言,默认为英语
   For a list of supported codes, see
   https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-language.
   > Project language [en]: zh_CN

   Creating file C:\Users\qaz22\LinuxShare\ReadTheDocs\EnglistWorld\source\conf.py.
   Creating file C:\Users\qaz22\LinuxShare\ReadTheDocs\EnglistWorld\source\index.rst.
   Creating file C:\Users\qaz22\LinuxShare\ReadTheDocs\EnglistWorld\Makefile.
   Creating file C:\Users\qaz22\LinuxShare\ReadTheDocs\EnglistWorld\make.bat.

   Finished: An initial directory structure has been created.

   You should now populate your master file C:\Users\qaz22\LinuxShare\ReadTheDocs\EnglistWorld\source\index.rst and create other documentation
   source files. Use the Makefile to build the docs, like so:
      make builder
   where "builder" is one of the supported builders, e.g. html, latex or linkcheck.

最后生成的项目结构如下：

.. image:: ./img/sphinx-project-tree.png
   :alt: sphinx project tree


* build:用来存放通过make html生成文档网页文件的目录
* source：存放用于生成文档的源文件
* conf.py: Sphinx的配置文件
* index.rst: 主文档

|30|

配置主题
-----------------

在conf.py文件中配置以下属性以替换主题：

.. code-block:: python

   # 头部添加导入
   import sphinx_rtd_theme
   # 找到主题属性更改如下
   html_theme = 'sphinx_rtd_theme'

.. note:: 

   更多主题配置点击查看  :ref:`HTML Theme <sphinx-html-theme>`  笔记.


|30|

通过vscode的git插件创建存储库
-------------------------------

创建完之后，添加.gitignore文件以及README.md文件


本项目的.gitignore文件代码如下：

.. literalinclude:: ../../../.gitignore
   :language: git

本项目的README.md文件代码如下：

.. literalinclude:: ../../../README.md
   :language: markdown

|30|

推送
-------------------------

添加远程仓库，可以通过添加url添加仓库；如果使用了GitHub插件，那么可以直接选择并推送到现存的空仓库。


|30|

不同文件下的 tab 键行为控制
-------------------------------

这个功能配置可选择性添加，如果不使用 rst 文件编写笔记，那么这个功能也没有用；但是如果你打算使用 rst 文件编写笔记，甚至打算使用 rst 和 md 文件混合编写笔记，那么就有必要控制 tab 键的行为，因为 RestructureText 语法中的指令的内容和可选项都需要缩进 **3个空格**。，虽然可以连击三个 space，但是显然直接使用 tab 键更快捷。

由于笔者使用 VsCode 编写笔记，然后发现通过分别设置 用户、工作区、文件夹的 ``settings.json`` 文件中的  ``"editor.tabSize": 3`` 属性都没有很好的设置到 tab 的空格数。所以笔者索性通过插件 *EditorConfig for Visual Studio Code* 使用 ``.editorconfig`` 文件来格式化不同文件下的 tab 键。

.. code-block:: guess
   :caption: .editorconfig 文件
   :linenos:

   # EditorConfig is awesome: https://EditorConfig.org

   # top-most EditorConfig file 表示是最顶层的配置文件，发现设为true时，才会停止查找.editorconfig文件
   root = true

   # Set default charset
   [*.{rst,py,md,txt,html,xml,java}]
   charset = utf-8

   # Unix-style newlines with a newline ending every file 对于所有的文件 始终在文件末尾插入一个新行
   [*]
   end_of_line = lf
   insert_final_newline = true

   # 4 space indentation 控制py文件类型的缩进大小
   [*.{py,md,java}]
   indent_style = space
   indent_size = 4

   [*.rst]
   indent_style = space
   indent_size = 3


