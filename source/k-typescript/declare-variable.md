# 变量声明 (declare variable)

TypeScript 变量的命名规则：

* 变量名称可以包含数字和字母。

* 除了下划线 `_` 和美元 `$` 符号外，不能包含其他特殊字符，包括空格。

* 变量名不能以数字开头。

变量使用前必须先声明，可以使用 `var` 、 `let` 、 `const` 来声明变量。

TypeScript 遵循强类型，如果将不同的类型赋值给变量会编译错误。

## 变量声明 

`let` 和 `const` 是 JavaScript 里相对较新的变量声明方式。 

一直以来我们都是通过 `var` 关键字定义 JavaScript 变量。对于熟悉其它语言的人来说，`var` 声明有些奇怪的作用域规则。如下代码所示：

```{code-block} ts

function f(shouldInitialize: boolean) {
    if (shouldInitialize) {
        var x = 10;
    }

    return x;
}

f(true);  // returns '10'
f(false); // returns 'undefined'
```

> 变量x是定义在if语句里面，但是我们却可以在语句的外面访问它。这是**因为 `var` 声明可以在包含它的函数，模块，命名空间或全局作用域内部任何位置被访问** 。
> 由于 var 定义的变量的作用域的模糊和没有限制，那么在程序中，会出现相同作用域范围内的同名变量被最后定义的同名变量覆盖。（它不在乎你声明多少次；你只会得到1个。）


### `let` 声明

`let` 与 `var` 主要的区别不在语法上，而是语义:

* 块作用域
* 重定义及屏蔽
* 块级作用域变量的获取

#### 块作用域

拥有块级作用域的变量的另一个特点是，它们不能在被声明之前读或写。注意一点，我们仍然可以在一个拥有块作用域变量被声明前获取它。 只是我们不能在变量声明前去调用那个函数。 

```{code-block} ts

function foo() {
    // okay to capture 'a'
    return a;
}

// 不能在'a'被声明前调用'foo'
// 运行时应该抛出错误
foo();

let a;
```

#### 重定义及屏蔽

在一个 *嵌套作用域里引入* 一个新名字的行为称做屏蔽。 它是一把双刃剑，它可能会不小心地引入新问题，同时也可能会解决一些错误。

```{code-block} ts
function sumMatrix(matrix: number[][]) {
    let sum = 0;
    for (let i = 0; i < matrix.length; i++) {
        var currentRow = matrix[i];
        for (let i = 0; i < currentRow.length; i++) {
            sum += currentRow[i];
        }
    }

    return sum;
}
```

#### 块级作用域变量的获取

直观地讲，每次进入一个作用域时，它创建了一个变量的环境。 就算作用域内代码已经执行完毕，这个环境与其捕获的变量依然存在。

```{code-block} ts

function theCityThatAlwaysSleeps() {
    let getCity;

    if (true) {
        let city = "Seattle";
        getCity = function() {
            return city;
        }
    }

    return getCity();
}
//因为我们已经在city的环境里获取到了city，所以就算if语句执行结束后我们仍然可以访问它。
```

### `const` 声明

`const` 是对 `let` 的一个增强，它们拥有与let相同的作用域规则，还能阻止对一个变量再次赋值，即它们引用的值是*不可变的*。

使用**最小特权原则**，所有变量除了你计划去修改的都应该使用 `const` 。 基本原则就是如果一个变量不需要对它写入，那么其它使用这些代码的人也不能够写入它们，并且要思考为什么会需要对这些变量重新赋值。 使用 `const` 也可以让我们更容易的推测数据的流动。

```{admonition} readonly & const

最简单判断该用 readonly 还是 const 的方法是看要把它做为变量使用还是做为一个属性。 做为变量使用的话用 const ，若做为属性则使用 readonly。
```

## 解构 (**析构声明**)


### 解构数组

```{code-block} ts

let input = [1, 2];
let [first, second] = input;
console.log(first); // outputs 1
console.log(second); // outputs 2
//相当于使用了索引，但更为方便
// first = input[0];
// second = input[1];
```

还可以对函数参数解构：


```{code-block} ts

function f([first, second]: [number, number]) {
    console.log(first);
    console.log(second);
}
f(input);
```


还可以在数组里使用 `...` 语法创建剩余变量:


```{code-block} ts

let [first, ...rest] = [1, 2, 3, 4];
console.log(first); // outputs 1
console.log(rest); // outputs [ 2, 3, 4 ]

let [s] = [1, 2, 3, 4];
console.log(s); // outputs 1
let [, second, , fourth] = [1, 2, 3, 4];
console.log(second); //outputs 2
console.log(fourth); //outputs 4
```

### 对象解构


```{code-block} ts

let o = {
    a: "foo",
    b: 12,
    c: "bar"
};
let { a, b } = o;

// let { a, b } = o; 的析构声明可以简单写为：
// let newName1 = o.a;
// let newName2 = o.b;

//let { a, b } = o; 等价于：
({ a, b } = { a: "baz", b: 101 }); //使用不显示声明的赋值

// 可以使用 ... 语法来说创建剩余变量
let { a, ...passthrough } = o;
let total = passthrough.b + passthrough.c.length;

```

```{attention} 

注意，对一个对象进行不声明地析构时，我们需要用小括号将它括起来，因为Javascript通常会将以 `{` 起始的语句解析为一个块。
```


#### 属性的重命名

你也可以给属性以不同的名字：

```{code-block} ts

let { a: newName1, b: newName2 } = o;
```

这里的冒号不是指示类型的。 如果你想指定它的类型， 仍然需要在其后写上完整的模式。

```{code-block} ts

let {a, b}: {a: string, b: number} = o;
```






```{warning}


要小心使用解构。因为即便是最简单的解构表达式也是难以理解的。解构表达式要尽量保持小而简单。
```
