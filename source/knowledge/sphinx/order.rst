==============================
指令
==============================

epigraph 题词
====================


题词是一种适当的(合适的，恰当的或相关的)短题词，通常是引文或诗歌，在文件或章节的开头。

.. epigraph::

   No matter where you go, there you are.

   -- Buckaroo Banzai



代码 ::

   .. epigraph::

   No matter where you go, there you are.

   -- Buckaroo Banzai



topic / 主题 or 总论
==========================

.. epigraph::

   带有标题的段落。

.. topic:: Topic Title

   Subsequent indented lines comprise
   the body of the topic, and are
   interpreted as body elements.

----

.. code-block:: rest

   .. topic:: Topic Title

      Subsequent indented lines comprise
      the body of the topic, and are
      interpreted as body elements.

image 与 figure 
========================

image
-----------

For example ::

   .. image:: picture.jpeg
      :height: 100px
      :width: 200 px
      :scale: 50 %
      :alt: alternate text
      :align: right

* ``align`` 对齐: "top", "middle", "bottom", "left", "center", or "right"。“left”、“center”和“right”值控制图像的水平对齐，允许图像浮动，并让文本围绕它流动。 *值“top”、“middle”和“bottom”控制图像的垂直对齐(相对于文本基线);它们只对内联图像(替换)有用。*
* ``alt`` 替代文本，对图像的简短描述
* ``height`` 图片高；当“scale”选项也被指定时，它们将被合并。例如，一个200px的高度和50的比例相当于一个100px的高度没有比例。
* ``width`` 图片宽；当“scale”选项也被指定时，它们将被合并。
* ``scale`` 缩放，整数百分比(“%”符号是可选的)，默认是“100%”，即没有缩放。

----

.. image:: ./img/grapefruit.jfif
   :alt: hzw
   :scale: 50%
   :align: right

柚（学名：Citrus maxima (Burm) Merr.）是芸香科、柑橘属植物。乔木。嫩枝、叶背、花梗、花萼及子房均被柔毛，嫩叶通常暗紫红色，嫩枝扁且有棱。叶质颇厚，色浓绿，阔卵形或椭圆形，连冀叶长9-16厘米，宽4-8厘米。总状花序，有时兼有腋生单花；花蕾淡紫红色，稀乳白色；花萼不规则5-3浅裂；花瓣长1.5-2厘米；雄蕊25-35枚，有时部分雄蕊不育。果圆球形，扁圆形，梨形或阔圆锥状，果皮甚厚或薄，海绵质，油胞大，凸起，果心实但松软，瓢囊10-15或多至19瓣；种子多达200余粒，亦有无子的，形状不规则，通常近似长方形，单胚。花期4-5月，果期9-12月。
原产东南亚，在中国已有3000多年栽培历史。浙江、江西、广东、广西、台湾、福建、湖南、湖北、四川、贵州、云南等省均有栽种。柚性喜温暖、湿润气候，不耐干旱。生长期最适温度23-29℃，能忍受-7℃低温。
柚的果实表皮、花、叶还可提取优质芳香油，果皮中可提取优质果胶，果肉可以加工成果汁、果酒、柠檬酸、果酱及罐头等。果实综合利用后经济效益可望增长4倍，柚的综合利用还有很大的发掘潜力。果肉含维生素C较高。有消食、解酒毒功效。

----

代码 ::

   .. image:: ./img/grapefruit.jfif
      :alt: hzw
      :scale: 50%
      :align: right
   
   ... 文字文章 ...


figure 
==================

.. epigraph::

   带标题和可选图例的图像

代码样例 ::

   .. figure:: picture.png
      :scale: 50 %
      :alt: map to buried treasure

      This is the caption of the figure (a simple paragraph).【标题】

      The legend consists of all elements after the caption.  In this
      case, the legend consists of this paragraph and the following
      table:（以下为图例）

      +-----------------------+-----------------------+
      | Symbol                | Meaning               |
      +=======================+=======================+
      | .. image:: tent.png   | Campground            |
      +-----------------------+-----------------------+
      | .. image:: waves.png  | Lake                  |
      +-----------------------+-----------------------+
      | .. image:: peak.png   | Mountain              |
      +-----------------------+-----------------------+

----

.. figure:: ./img/grapefruit.jfif
   :alt: 柚子
   :height: 100px
   :width: 200 px
   :scale: 100%
   :align: right

   柚（学名：Citrus maxima (Burm) Merr.）

   The legend consists of all elements after the caption.  In this
   case, the legend consists of this paragraph and the following
   table:

   +----------------------------------+------------+
   | Symbol                           | Meaning    |
   +==================================+============+
   | .. image:: ./img/grapefruit.jfif |            |
   |    :scale: 20%                   | Campground |
   +----------------------------------+------------+
   | .. image:: ./img/grapefruit.jfif |            |
   |    :scale: 20%                   | Campground |
   +----------------------------------+------------+
   | .. image:: ./img/grapefruit.jfif |            |
   |    :scale: 20%                   | Campground |
   +----------------------------------+------------+

----

实例代码 ::

   .. figure:: ./img/grapefruit.jfif
      :alt: 柚子
      :height: 100px
      :width: 200 px
      :scale: 100%
      :align: right

      柚（学名：Citrus maxima (Burm) Merr.）

      The legend consists of all elements after the caption.  In this
      case, the legend consists of this paragraph and the following
      table:

      +----------------------------------+------------+
      | Symbol                           | Meaning    |
      +==================================+============+
      | .. image:: ./img/grapefruit.jfif |            |
      |    :scale: 20%                   | Campground |
      +----------------------------------+------------+
      | .. image:: ./img/grapefruit.jfif |            |
      |    :scale: 20%                   | Campground |
      +----------------------------------+------------+
      | .. image:: ./img/grapefruit.jfif |            |
      |    :scale: 20%                   | Campground |
      +----------------------------------+------------+
   


other ?
=====================