=======================
角色
=======================


sphinx使用解释文本角色将语义标记插入到文档中。它们被写为 ``:rolename:`content '``.



交叉引用任意位置 / 锚
=======================

添加锚的步骤：

#. 添加 label
#. 适用 ref 角色 链接 label


为了支持对任何文档中任意位置的交叉引用，使用标准的REST标签。为此，在整个文档中，工作标签名称必须是唯一的。有两种方法可以引用标签：

* ``:ref:`Label``` 
   * 如果将标签直接放置在节标题之前，可以使用 ``:ref:`label-name``` .例如: 

   .. code-block:: rest

      .. _my-reference-label:

      Section to cross-reference
      --------------------------

      This is the text of the section.

      It refers to the section itself, see :ref:`my-reference-label`.

      .. 当节和引用位于不同的源文件中时，这也同样有效。

   * 自动标签同样适用于图像
   
   .. code-block:: rest

      .. _my-figure:

      .. figure:: whatever

         Figure caption
   
   
* ``:ref:`description _<Label>``` 
   * 如果不是以上情况，仍可以引用节标题之前未放置的标签，但必须使用以下语法为链接指定明确的标题： ``:ref:`Link title <label-name>```.

.. attention:: 

   引用标签(label)必须以下划线开头。引用标签时，必须省略下划线（请参见上面的示例）。


:ref:`引用可下载文件 <knowledge/sphinx/rest/roles:引用可下载文件>` 
:ref:`menuselection <knowledge/sphinx/rest/roles:交叉引用任意位置 / 锚>` 


.. code-block:: rest

   .. 上方两个锚点的代码如下：
   
   :ref:`引用可下载文件 <knowledge/sphinx/rest/roles:引用可下载文件>` 
   :ref:`menuselection <knowledge/sphinx/rest/roles:交叉引用任意位置 / 锚>` 


.. important:: 

   手动为每个部分添加一个明确的目标并确保其唯一性是一项艰巨的任务！幸运的是，Sphinx 包含一个扩展来帮助我们解决这个问题， ``autosectionlabel``。

   要激活autosectionlabel扩展，请将其添加到您的conf.py文件中：

   .. code-block:: python

      # Add the extension
      extensions = [
         'sphinx.ext.autosectionlabel',
      ]

      # Make sure the target is unique
      autosectionlabel_prefix_document = True

   Sphinx 将为您的所有部分创建明确的目标，目标名称的形式为 ``{path/to/page}:{title-of-section}``.

   .. code-block:: rest

     - :ref:`guides/cross-referencing-with-sphinx:explicit targets`.

     - :ref:`Custom title <guides/cross-referencing-with-sphinx:explicit targets>`.




引用可下载文件
========================

``:download:`Title <path>``` 

此角色允许您链接到源树中的文件，这些文件不是可以查看的REST文档，而是可以下载的文件。

当您使用此角色时，被引用的文件将在生成时自动标记为包含在输出中（显然，仅用于HTML输出）。所有可下载的文件都放在 ``_downloads/<unique hash>/`` 输出目录的子目录；处理重复的文件名。

See :download:`this example rst file <../example/title1.rst>`.


.. code-block:: rest

   .. 上文下载功能代码如下所示：
   See :download:`this example script <../example/title1.rst>`.



交叉引用文档
==================

``:doc:`/text```

链接到指定的文档；可以绝对或相对方式指定文档名。如果没有给出明确的链接文本（与通常一样：  ``:doc:`Monty Python members </people>``` 链接标题将是给定文档的标题。

:doc:`./basic` 

:doc:`./basic <./basic>` 

.. code-block:: rest

   .. 上方文档链接的实现代码如下：

   :doc:`./basic` 

   :doc:`./basic <./basic>` 

数学
===============


math
-------------------

.. math:: e^{i\pi} + 1 = 0
   :label: euler

Since Pythagoras, we know that :math:`a^2 + b^2 = c^2`.

.. math::

    α_t(i) = P(O_1, O_2, … O_t, q_t = S_i λ)


:math:`α_t(i) = P(O_1 × O_2 × … O_t × q_t = S_i λ)` 

The area of a circle is :math:`A_\text{c} = (\pi/4) d^2`.

Euler's identity, equation :math:numref:`euler`, was elected one of the
most beautiful mathematical formulas.

.. code-block:: rest

   .. 上方数学公式的代码为：

   .. math:: e^{i\pi} + 1 = 0
      :label: euler

   Since Pythagoras, we know that :math:`a^2 + b^2 = c^2`.

   .. math::

      α_t(i) = P(O_1, O_2, … O_t, q_t = S_i λ)


   :math:`α_t(i) = P(O_1 × O_2 × … O_t × q_t = S_i λ)` 

   The area of a circle is :math:`A_\text{c} = (\pi/4) d^2`.

   Euler's identity, equation :math:numref:`euler`, was elected one of the
   most beautiful mathematical formulas.

.. note:: 

   ``:eq:`` 等同于 ``math:numref`` .

raw 
=======================

包括原始目标格式标记。

“raw” 指示非restructuredtext数据，该数据将不受影响地传递给Writer。输出格式的名称在指令参数中给出。对原始数据的解释取决于作者。Writer可以忽略任何不匹配其格式的原始输出。

.. raw:: html

   <hr width=200 size=10>


.. code-block:: rest

   .. 上方分隔线代码如下所示：

   .. raw:: html

      <hr width=200 size=10>


其他语义标记
=================

**以下角色除了以不同的样式格式化文本外，不执行任何特殊操作：**

strong
------------

strong 角色标记的效果等同于双星号的字体加粗效果。

**text**  
:strong:`text`

.. code-block:: rest

   .. 上方 text 的代码如下所示：
   **text**
   :strong:`text`
   

sub / subscript  / 下标
------------------------

The chemical formula for pure water is |H2O|.

.. |H2O| replace:: H\ :sub:`2`\ O

The chemical formula for pure Hydrogen Peroxide is |H2O2|.

.. |H2O2| replace:: :math:`H_2 O_2`

.. code-block:: rest

   .. 上方化学公式的代码表示方式如下：

   The chemical formula for pure water is |H2O|.

   .. |H2O| replace:: H\ :sub:`2`\ O

   The chemical formula for pure Hydrogen Peroxide is |H2O2|.

   .. |H2O2| replace:: :math:`H_2 O_2`

sup / superscript / 上标
--------------------------

|X2Y2| (|X2Y25|).

.. |X2Y2| replace:: X\ :sup:`2`\ + Y\ :sup:`2`\ = 25


.. |X2Y25| replace:: :math:`X^2 + Y^2 = 25` 


.. code-block:: rest

   .. 上方公式的代码表示方式如下：
   |X2Y2| (|X2Y25|).

   .. |X2Y2| replace:: X\ :sup:`2`\ + Y\ :sup:`2`\ = 25


   .. |X2Y25| replace:: :math:`X^2 + Y^2 = 25` 


abbr 文字提示
------------------

缩写。如果角色内容包含一个带括号的解释，它将被特殊处理：它将以HTML的形式显示在工具提示中，并且在LaTex中只输出一次。

:abbr:`LIFO (last-in, first-out)`.

.. code-block:: rest

   .. 文字提示的实现方式：

   :abbr:`LIFO (last-in, first-out)`.




menuselection
-------------------------

菜单选项应使用 menuselection 角色。这用于标记菜单选择的完整序列，包括选择子菜单和选择特定操作，或此类序列的任何子序列。个别选择的名称应以分隔 --> .

例如，要标记选择“开始>程序”，请使用以下标记：

:menuselection:`Start --> Programs`

.. code-block:: rest

   :menuselection:`Start --> Programs`