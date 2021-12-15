===============
基本配置
===============


配置java文件的代码提示的触发条件
---------------------------------

eclipse 对java的代码提示默认触发条件为键入 ``.``,为了方便起见，应当使所有大小写字母都能触发代码提示。

.. tip:: 

   点击 eclipse 顶部菜单栏的 window -> Preferences 打开配置窗口；点击 Java–>Editor–>Content Assist，把Auto Activation部分的属性 Auto activation triggers for Java 里面的内容改为：``.abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ``


配置java文件的代码提示的选择选项条件
----------------------------------------

默认情况下，我们使用 ``Esc`` 键可以退出代码提示，如果键入空格或回车会选定所指定的选项。

从笔者的习惯来说，更习惯使用空格来退出代码提示，用回车来选定代码提示。

.. tip::

   点击 eclipse 顶部菜单栏的 window -> Preferences 打开配置窗口；点击 Java→Editor→Content Assist, 把 Insertion部分的属性 Disabled insertion triggers except 'Enter' 点击勾选使之为真。

对编辑器字体的配置
--------------------

.. tip::

   点击 eclipse 顶部菜单栏的 window -> Preferences 打开配置窗口；点击 General->Appearance->Colors and Fonts; 将里面的Java或Basic部分设置即可。

对文件或项目的编码配置
-------------------------

.. tip:: 

   点击 eclipse 顶部菜单栏的 window -> Preferences 打开配置窗口；点击 General->Workspace ; 修改Text file encoding 部分。
