
=================================
Pattern matching and Regex(2)
=================================

主要对python的正则表达式进行字符串匹配方法的记录。该部分代码需要导入re模块—— ``import re`` 。


Greedy and non-greedy match 
----------------------------------

python的正则表达式默认是‘贪心’的，在有二义性的情况下会匹配尽可能长的字符串。需要注意的是，所谓贪心或不贪心匹配是在正则表达式有部分字符串是有重复区间的情况下才有的。

.. code-block:: python

   # greedy match
   greedyRegex = re.compile(r'(la){3,5}')
   mo = greedyRegex.search('lalalalala')
   print(mo.group())
   greedyRegex = re.compile(r'(la)?')
   mo = greedyRegex.search('lalalalala')
   print(mo.group())
   # non-greedy match
   greedyRegex = re.compile(r'(la){3,5}?')
   mo = greedyRegex.search('lalalalala')
   print(mo.group())
   greedyRegex = re.compile(r'(la)*?')
   mo = greedyRegex.search('lalalalala')
   print(mo.group())
   greedyRegex = re.compile(r'(la)+?')
   mo = greedyRegex.search('lalalalala')
   print(mo.group())


.. code-block:: guess

   lalalalala
   la
   lalala

   la

findall()方法
-------------------------

Regex Object 除了有search()方法之外，还有findall()方法；前者得到的结果是被查找字符串中的“第一次”匹配的文本，而findall()方法将返回一组字符串，包含被查找字符串中所有的匹配项。（同时，通过search获得的结果是一个Math对象，而通过fandall()获得的结果是列表）












