==============================
Pattern matching and Regex(1)
==============================

主要对python的正则表达式进行字符串匹配方法的记录。该部分代码需要导入re模块—— ``import re`` 。

.. tip::
   本章节需要特别注意反斜杠（\）的使用。同时，在这个小节中，所有的匹配字符串搜索都是使 ``regexObject.search('character string')`` 方法，该方法与 ``regexObject.findall('character string')`` 不同在于前者最多只能匹配到一个子字符串，而后者可以匹配所以符合表达式的子字符串。

----

create a regex and using it matches character string 【Basic】
-------------------------------------------------------------------
 
创建一个带有格式的正则表达式对象并通过这个对象来 *匹配字符串* （搜索字符串中的符合正则表达式的格式的子字符串，若没有则返回None）。

.. code-block:: python 

    # python code
    # step1: create a regex in a format.
    phone_number_regex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
    # step2: entity matching regex; if the search is successful, it returns a string.
    result = phone_number_regex.search('My phone number is 4414-555-0192')
    print("The result is ", result)

.. code-block:: word

   # screenshot
   The result is  <re.Match object; span=(20, 32), match='414-555-0192'>

.. note:: 
   在python中，转义字符使用倒斜杠（\），所以在字符串表示换行符时，需要写成 ``"\\n"`` ，同理在写正则表达式的匹配字符串时要用转义字符如例子的匹配字符串为 ``\\d\\d\\d-\\d\\d\\d-\\d\\d\\d\\d`` ，因为正则表达式常常使用倒斜杠，所以输入原始字符串—— ``r'\d\d\d-\d\d\d-\d\d\d\d'`` 就会比较方便。

----

Group by brackets -()-
--------------------------

通过括号进行正则表达式搜索结果分组。

.. code-block:: python

   # step1: create a regex in a format.
   phone_number_regex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
   # step2: entity matching regex; if the search is successful, it returns a string.
   result = phone_number_regex.search('My phone number is 414-555-0192')
   # getting all items by groups()
   print("The result is ", result.groups())
   area_code, main_code = result.groups()
   print("The areaCode is "+area_code+", the mainCode is "+main_code)
   # get all items by subscript
   print("The areaCode is "+result.group(1)+", the mainCode is "+result.group(2))
   print("The phone number is "+result.group(0))
   print("The phone number is "+result.group())

.. code-block:: word

   The result is  ('414', '555-0192')
   The areaCode is 414, the mainCode is 555-0192
   The areaCode is 414, the mainCode is 555-0192
   The phone number is 414-555-0192
   The phone number is 414-555-0192

.. note::  
   需要注意的是，通过regexObject.groups()获取的结果是一个元组，包含用括号分组的元素。同时，如果是使用下表获取分组元素，组要注意的是regexObject.group()或regexObject.group(0)获取的是未分组的匹配字符串。

Group by pipeline(|)
-----------------------

需要 **匹配多个表达式（分组）中的一个** 的情况下，使用管道 ``|``。

.. code-block:: python

   batRegex = re.compile(r'Bat(man|mobile|bat)')
   mo = batRegex.search('Batmobile lost a Batbat')
   print(mo.group())
   print(mo.group(1))
   print(mo)
   print('----------'.center(20))
   batRegex = re.compile(r'Batman|Tina Fey')
   mo = batRegex.search('Batman and Tina Fey.')
   print(mo.group())
   print(mo)

.. code-block:: word

   Batmobile
   mobile
   <re.Match object; span=(0, 9), match='Batmobile'>
      ----------     
   Batman
   <re.Match object; span=(0, 6), match='Batman'>

Group by question mark (?)
----------------------------

需要 **可选匹配表达式（分组）**，使用问号。即想匹配的模式是可选的。 可以认为，``?`` 是在说“匹配这个问号之前的分组零次或者一次”。

.. code-block:: python

   batRegex = re.compile(r'Bat(wo)?man')
   mo = batRegex.search('The Adventures of Batman')
   print(mo.group())
   print("**********".center(20))
   mo = batRegex.search('The Adventures of Batwoman')
   print(mo.group())
   print("**********".center(20))
   mo = batRegex.search('The Adventures of Batwowoman')
   print(mo)

.. code-block:: word

   Batman
      **********     
   Batwoman
      **********     
   None

Group by asterisk(*)
------------------------------

``*`` 意味着“**匹配零次或多次**”，即星号之前的分组可以在被匹配文本中出现任意次。

.. code-block:: python

   batRegex = re.compile(r'Bat(wo)*man')
   mo = batRegex.search('The Adventures of Batman')
   print(mo.group())
   print("**********".center(20))
   mo = batRegex.search('The Adventures of Batwoman')
   print(mo.group())
   print("**********".center(20))
   mo = batRegex.search('The Adventures of Batwowoman')
   print(mo.group())

.. code-block:: word

   Batman
      **********     
   Batwoman
      **********     
   Batwowoman

Group by plus sign (+)
------------------------------

``+`` 意味着“**匹配一次或多次**”，即加号之前的分组可以在被匹配文本中出现一次或一次以上。

.. code-block:: python

   batRegex = re.compile(r'Bat(wo)+man')
   mo = batRegex.search('The Adventures of Batman')
   print(mo)
   print("**********".center(20))
   mo = batRegex.search('The Adventures of Batwoman')
   print(mo.group())
   print("**********".center(20))
   mo = batRegex.search('The Adventures of Batwowoman')
   print(mo.group())

.. code-block:: word

   None
      **********     
   Batwoman
      **********     
   Batwowoman

Group by brace -{}-
------------------------------

**使用花括号匹配特定次数**。如果想要一个分组重复特定次数，就在正则表达式中该分组的后面跟上花括号并包围重复次数数字。

.. code-block:: python

   batRegex = re.compile(r'Bat(wo){0}man')
   mo = batRegex.search('The Adventures of Batman')
   print(mo.group())
   print("**********".center(20))
   mo = batRegex.search('The Adventures of Batwoman')
   print(mo)
   print("**********".center(20))
   mo = batRegex.search('The Adventures of Batwowoman')
   print(mo)

.. code-block:: word

   Batman
      **********     
   None
      **********     
   None

.. note:: 

   花括号除了可以包含一个数字，亦可以指定特定范围，即在花括号写下一个最小值、逗号、一个最大值。如下所示:

.. code-block:: python

   batRegex = re.compile(r'Bat(wo){0,1}man')
   mo = batRegex.search('The Adventures of Batman')
   print(mo)
   print("**********".center(20))
   mo = batRegex.search('The Adventures of Batwoman')
   print(mo)
   print("**********".center(20))
   mo = batRegex.search('The Adventures of Batwowoman')
   print(mo)
   print("**********".center(20))

.. code-block:: word

   <re.Match object; span=(18, 24), match='Batman'>
      **********     
   <re.Match object; span=(18, 26), match='Batwoman'>
      **********     
   None
      ********** 



