==========================
Markdown 支持
==========================

.. _markdown-support:

MyST Markdown
====================

.. note:: 

   MyST Markdown 是 Markdown 的超集。更多关于 MyST Markdown 的信息前往官网 `MyST - Markedly Structured Text <https://myst-parser.readthedocs.io/en/latest/index.html>`_ 。
   
   当然，也可以前往笔者的 :ref:`关于 MyST 的笔记 <get-started-with-myst>` 。

.. important:: 

   更多关于 MyST Markdown 的信息前往官网 `MyST - Markedly Structured Text <https://myst-parser.readthedocs.io/en/latest/index.html>`_ 

要配置您的Sphinx项目以支持 Markdown ，请按以下步骤进行：

#. 安装 Markdown 分析程序 推荐标记：

   .. code-block:: default

      pip install myst-parser


#. 添加 推荐标记 到 ``config.py`` 文件中 :

   .. code-block:: python

      extensions = ['myst_parser']

#. 在项目根目录下添加 requirement.txt 文件，并写入以下字段，以支持额外的Python环境。

   .. code-block:: default

      myst_parser 
   
.. important:: 
   
   `Requirements File Format <https://pip.pypa.io/en/latest/reference/requirements-file-format/#requirements-file-format>`_ 

   Requirements File 样板如下所示：

   .. code-block:: default

      ###### Requirements without Version Specifiers ######
      pytest
      pytest-cov
      beautifulsoup4

      ###### Requirements with Version Specifiers ######
      #   See https://www.python.org/dev/peps/pep-0440/#version-specifiers
      docopt == 0.6.1             # Version Matching. Must be version 0.6.1
      keyring >= 4.1.1            # Minimum version 4.1.1
      coverage != 3.5             # Version Exclusion. Anything except version 3.5
      Mopidy-Dirble ~= 1.1        # Compatible release. Same as >= 1.1, == 1.*

      ###### Refer to other requirements files ######
      -r other-requirements.txt

      ###### A particular file ######
      ./downloads/numpy-1.9.2-cp34-none-win32.whl
      http://wxpython.org/Phoenix/snapshot-builds/wxPython_Phoenix-3.0.3.dev1820+49a8884-cp34-none-win_amd64.whl

      ###### Additional Requirements without Version Specifiers ######
      #   Same as 1st section, just here to show that you can put things in any order.
      rejected
      green

   


