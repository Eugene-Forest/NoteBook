==============================
Pattern matching and Regex
==============================

主要对python的正则表达式进行字符串匹配方法的记录。该部分代码需要导入re模块—— ``import re`` 。

.. tip::
   本章节需要特别注意反斜杠（\）的使用。

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

.. note:: text
   需要注意的是，通过regexObject.groups()获取的结果是一个元组，包含用括号分组的元素。同时，如果是使用下表获取分组元素，组要注意的是regexObject.group()或regexObject.group(0)获取的东西是未分组的匹配字符串。

Group by pipeline(|)
-----------------------


Group by question mark (?)
----------------------------



Group by asterisk(*)
------------------------------


Group by plus sign (+)
------------------------------



Group by brace -{}-
------------------------------





