# 流程处理

基本上， Typescript 的流程处理的语法和 Java 没有太大的出入，所以此篇章主要了解和记录一些与 Java 语法常识不同的 Typescript 流程处理语法。


## if

* `if` 语句 - 只有当指定条件为 `true` 时，使用该语句来执行代码
* `if...else` 语句 - 当条件为 `true` 时执行代码，当条件为 `false` 时执行其他代码
* `if...else if....else` 语句- 使用该语句来选择多个代码块之一来执行

```{code-block} ts
:caption: if 示例

var num:number = 2 
if(num > 0) { 
    console.log(num+" 是正数") 
} else if(num < 0) { 
    console.log(num+" 是负数") 
} else { 
    console.log(num+" 不是正数也不是负数") 
}
```

## switch

switch 语句必须遵循下面的规则：

* switch 语句中的 expression 是一个常量表达式，必须是一个整型或枚举类型。
* 在一个 switch 中可以有任意数量的 case 语句。每个 case 后跟一个要比较的值和一个冒号。
* case 的 constant-expression 必须与 switch 中的变量具有相同的数据类型，且必须是一个常量或字面量。
* 当被测试的变量等于 case 中的常量时，case 后跟的语句将被执行，直到遇到 break 语句为止。
* 当遇到 break 语句时，switch 终止，控制流将跳转到 switch 语句后的下一行。
* 不是每一个 case 都需要包含 break。如果 case 语句不包含 break，控制流将会 继续 后续的 case，直到遇到 break 为止。
* 一个 switch 语句可以有一个可选的 default case，出现在 switch 的结尾。default case 可用于在上面所有 case 都不为真时执行一个任务。default case 中的 break 语句不是必需的。

```{code-block} ts
:caption: switch case 示例

switch(expression){
    case constant-expression  :
       statement(s);
       break; /* 可选的 */
    case constant-expression  :
       statement(s);
       break; /* 可选的 */
  
    /* 您可以有任意数量的 case 语句 */
    default : /* 可选的 */
       statement(s);
}
```

## 三目运算

同大多数语言一样， Typescript 也有三目运算，且语法雷同。

```{code-block} ts

let myName = "";
console.log(myName != "" ? "My name is " + myName : "Please inter your name") //output :Please inter your name
```


## for


## while



