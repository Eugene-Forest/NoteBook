=====================
箭头函数 [#]_
=====================

箭头函数表达式的语法比函数表达式更简洁，并且没有自己的this，arguments，super或new.target。

**箭头函数表达式更适用于那些本来需要匿名函数的地方，并且它不能用作构造函数。**


.. code-block:: javascript

   (param1, param2, …, paramN) => { statements }
   (param1, param2, …, paramN) => expression
   //相当于：(param1, param2, …, paramN) =>{ return expression; }

   // 当只有一个参数时，圆括号是可选的：
   (singleParam) => { statements }
   singleParam => { statements }

   // 没有参数的函数应该写成一对圆括号。
   () => { statements }

   //加括号的函数体返回对象字面量表达式：
   params => ({foo: bar})

   //支持剩余参数和默认参数
   (param1, param2, ...rest) => { statements }
   (param1 = defaultValue1, param2, …, paramN = defaultValueN) => {
   statements }

   //同样支持参数列表解构
   let f = ([a, b] = [1, 2], {x: c} = {x: a + b}) => a + b + c;
   f();  // 6


.. code-block:: javascript

   var elements = [
   'Hydrogen',
   'Helium',
   'Lithium',
   'Beryllium'
   ];

   elements.map(function(element) {
   return element.length;
   }); // 返回数组：[8, 6, 7, 9]

   // 上面的普通函数可以改写成如下的箭头函数
   elements.map((element) => {
   return element.length;
   }); // [8, 6, 7, 9]

   // 当箭头函数只有一个参数时，可以省略参数的圆括号
   elements.map(element => {
   return element.length;
   }); // [8, 6, 7, 9]

   // 当箭头函数的函数体只有一个 `return` 语句时，可以省略 `return` 关键字和方法体的花括号
   elements.map(element => element.length); // [8, 6, 7, 9]

   // 在这个例子中，因为我们只需要 `length` 属性，所以可以使用参数解构
   // 需要注意的是字符串 `"length"` 是我们想要获得的属性的名称，而 `lengthFooBArX` 则只是个变量名，
   // 可以替换成任意合法的变量名
   elements.map(({ "length": lengthFooBArX }) => lengthFooBArX); // [8, 6, 7, 9]


**引入箭头函数有两个方面的作用：更简短的函数并且不绑定this。**



----

.. [#] 本文摘自 MDN Web Docs 箭头函数 : https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Functions/arrow_functions
