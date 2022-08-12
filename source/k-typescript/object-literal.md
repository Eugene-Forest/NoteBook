# 字面量

先来做个小小的测试题，你能准确猜出来，下面 TS 代码中变量的类型吗？

```{code-block} ts

const companyName = "Eugene";
let companyArea = "beijing";
var companyPeopleCount = 200;
```

:::{dropdown} 答案


```{code-block} ts

const companyName = "Eugene"; // Eugene
let companyArea = "beijing";    // string
var companyPeopleCount = 200;   // number
```

因为 TS 的类型推断，TS 会把能改变（var 和 let 声明的变量）的变量 companyArea 和 companyPeopleCount 自动推断为合适的类型，const 声明的常量如果赋值为普通类型，因为其永远不会再改变了，则推断为字面量类型。
:::


## 字符串字面量


这里，我们创建了一个被称为 foo 变量，它仅接收一个字面量值为 Hello 的变量

```{code-block} ts

let foo: 'Hello';
foo = 'Bar'; // Error: 'bar' 不能赋值给类型 'Hello'
```

它们本身并不是很实用，但是可以在一个联合类型中组合创建一个强大的（实用的）抽象：


```{code-block} ts

type CardinalDirection = 'North' | 'East' | 'South' | 'West';
function move(distance: number, direction: CardinalDirection) {
  // ...
}
move(1, 'North'); // ok
move(1, 'Nurth'); // Error
```


````{admonition} [keyword] *type* 类型注解

其作用就是给类型起一个新名字，可以作用于原始值（基本类型），联合类型，元组以及其它任何你需要手写的类型:

```{code-block}

type Second = number; // 基本类型
let timeInSecond: number = 10;
let time: Second = 10;  // time的类型其实就是number类型
type userOjb = {name:string} // 对象
type getName = ()=>string  // 函数
type data = [number,string] // 元组
type numOrFun = Second | getName  // 联合类型
```

起别名不会新建一个类型，而是创建了一个新名字来引用那个类型。

当然，给基本类型起别名通常没什么用。**类型别名常用于联合类型。**
````


## 其他基本类型字面量

```{code-block} ts

type OneToFive = 1 | 2 | 3 | 4 | 5;
type Bools = true | false;
```


## 对象字面量（JS）/类型字面量（TS）


```{code-block} ts
:caption: 函数的对象参数的类型检查

function printLabel(labelledObj: { label: string }) {
  console.log(labelledObj.label);
}

let myObj = { size: 10, label: "Size 10 Object" };
printLabel(myObj);
```


````{admonition} const 与类型字面量的类型推导

```{code-block} ts

function iTakeFoo(foo: 'foo') {}
const test = {
  someProp: 'foo'
};

iTakeFoo(test.someProp); // Error: Argument of type string is not assignable to parameter of type 'foo'
```

这是由于 test 被推断为 { someProp: string }，我们可以采用一个简单的类型断言来告诉 TypeScript 你想推断的字面量：


```{code-block} ts

function iTakeFoo(foo: 'foo') {}

const test = {
  someProp: 'foo' as 'foo'
};

iTakeFoo(test.someProp); // ok
```

或者使用类型注解的方式，来帮助 TypeScript 推断正确的类型：

```{code-block} ts

function iTakeFoo(foo: 'foo') {}

type Test = {
  someProp: 'foo';
};

const test: Test = {
  // 推断 `someProp` 永远是 'foo'
  someProp: 'foo'
};

iTakeFoo(test.someProp); // ok
```

````

