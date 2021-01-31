==============================
Pattern matching and Regex
==============================

主要对python的正则表达式进行字符串匹配方法的记录。该部分代码需要导入re模块—— ``import re`` 。

----


create a regex and using it matches character string 
-------------------------------------------------------------------

*python code*

.. code-block:: python 

    # step1: create a regex in a format.
    phone_number_regex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
    # step2: entity matching regex; if the search is successful, it returns a string.
    result = phone_number_regex.search('My phone number is 4414-555-0192')
    print("The result is ", result)

*screenshot*

.. code-block:: word

   The result is  <re.Match object; span=(20, 32), match='414-555-0192'>

.. note:: 
   在python中，转义字符使用倒斜杠（\），所以在字符串表示换行符时，需要写成 ``"\\n"`` ，同理在写正则表达式的匹配字符串时要用转义字符如例子的匹配字符串为 ``\\d\\d\\d-\\d\\d\\d-\\d\\d\\d\\d`` ，因为正则表达式常常使用倒斜杠，所以输入原始字符串—— ``r'\d\d\d-\d\d\d-\d\d\d\d'`` 就会比较方便。

----

group()
-------------------


