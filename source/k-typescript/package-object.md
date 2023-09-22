# 封装对象


## Number

TypeScript 与 JavaScript 类似，支持 Number 对象。

Number 对象是原始数值的包装对象。

```{code-block} ts

let num = new Number(value);
//如果一个参数值不能转换为一个数字将返回 NaN (非数字值)。
```

1.	toExponential()
把对象的值转换为指数计数法。

//toExponential() 
var num1 = 1225.30 
var val = num1.toExponential(); 
console.log(val) // 输出： 1.2253e+3


2.	toFixed()
把数字转换为字符串，并对小数点指定位数。

var num3 = 177.234 
console.log("num3.toFixed() 为 "+num3.toFixed())    // 输出：177
console.log("num3.toFixed(2) 为 "+num3.toFixed(2))  // 输出：177.23
console.log("num3.toFixed(6) 为 "+num3.toFixed(6))  // 输出：177.234000


3.	toLocaleString()
把数字转换为字符串，使用本地数字格式顺序。

var num = new Number(177.1234); 
console.log( num.toLocaleString());  // 输出：177.1234


4.	toPrecision()
把数字格式化为指定的长度。

var num = new Number(7.123456); 
console.log(num.toPrecision());  // 输出：7.123456 
console.log(num.toPrecision(1)); // 输出：7
console.log(num.toPrecision(2)); // 输出：7.1


5.	toString()
把数字转换为字符串，使用指定的基数。数字的基数是 2 ~ 36 之间的整数。若省略该参数，则使用基数 10。

var num = new Number(10); 
console.log(num.toString());  // 输出10进制：10
console.log(num.toString(2)); // 输出2进制：1010
console.log(num.toString(8)); // 输出8进制：12


6.	valueOf()
返回一个 Number 对象的原始数字值。

var num = new Number(10); 
console.log(num.valueOf()); // 输出：10



## String


