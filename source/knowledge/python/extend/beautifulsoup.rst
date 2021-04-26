====================
BeautifulSoup(一)
====================

通过 urlopen 获取了网站的一个网页 HTML 文本后，我们就拥有了数据；但是，不能被处理为信息的数据是没有用的，所以我们就需要 BeautifulSoup 对象对数据进行解析。

通过 BeautifulSoup 库的 BeautifulSoup 对象以一定方式（即通过解析器）解析 html 文本对象并返回有一个对象，该对象可以通过 ``.`` 来获取属性（html标签）中的文本或标签属性等。

当创建一个 BeautifulSoup 对象时，需要传入两个参数：

#. 该对象所基于的 HTML 文本
#. 解析器

常见的解析器有三种（解析器对处理 html 文本的速度自上而下提高）：

* ``html.parser``
* ``lxml``
* ``html5lib``

第一个解析器是 python3 的一个解析器，不需要额外安装依赖库；后两个解析器的依赖库是需要额外安装的。【``pip3 install lxml``;``pip3 install html5lib``】

.. code-block:: python

   # way1 
   bs = BeautifulSoup(html.read(),'html.parser')
   # way2
   bs = BeautifulSoup(html.read(),'lxml')
   # way3
   bs = BeautifulSoup(html.read(),'html5lib')

一般而言，使用第一种解析器即 html.parser 即可，因为使用它不会出现可移植性和易用性的问题。只有当需要处理复杂的 HTML 文本且对文本处理速度要求较高时才使用后两种解析器。

.. code-block:: python

   from urllib.request import urlopen
   from bs4 import BeautifulSoup
   html = urlopen('https://www.hzu.edu.cn/main.htm')
   content = html.read()
   bs = BeautifulSoup(content, 'html.parser')
   print(bs.title)

.. code-block:: word

   # code run result
   <title>惠州学院Huizhou University</title>


可靠的网络连接以及异常的处理
-------------------------------

对抓取数据的过程以及数据的处理需要有异常处理以保证程序的正常且正确地运行。

在上文的代码块中，可能会报错的地方有两个，异常类型总共有三种。


.. literalinclude:: ../example_python/base_deal_error.py
   :language: python
   :linenos:
