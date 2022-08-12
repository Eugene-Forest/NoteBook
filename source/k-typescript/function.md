# 函数

函数是 JavaScript 应用程序的基础。 它帮助你实现抽象层，模拟类，信息隐藏和模块。 在 TypeScript 里，虽然已经支持类，命名空间和模块，但 *函数仍然是主要的定义行为的地方*。 TypeScript 为 JavaScript 函数添加了额外的功能，让我们可以更容易地使用。

和JavaScript一样，TypeScript函数可以创建有名字的函数和匿名函数。 你可以随意选择适合应用程序的方式，不论是定义一系列API函数还是只使用一次的函数。


```{code-block} ts
:caption: 函数的声明定义

// Named function
function add(x, y) {
    return x + y;
}

// Anonymous function
let myAdd = function(x, y) { return x + y; };
```

> 在 JavaScript 里，函数可以使用函数体外部的变量。 当函数这么做时，我们说它‘捕获’了这些变量。

```{code-block} ts
:caption: 函数使用函数体外的变量（函数定义前的变量）

let z = 100;

function addToZ(x, y) {
    return x + y + z;
}
```


## 函数类型

我们可以给函数的每个参数添加类型之后再为函数本身添加返回值类型。 

虽然 TypeScript 能够根据返回语句自动推断出返回值类型，但是为了函数便于维护，最好还是在函数定义的同时加入返回值类型。

```{code-block} ts
:caption: 函数参数的类型的声明

function add(x: number, y: number): number {
    return x + y;
}

let myAdd = function(x: number, y: number): number { return x + y; };
```

我们可以给每个参数添加类型之后再为函数本身添加返回值类型。 TypeScript 能够根据返回语句自动推断出返回值类型，因此我们通常省略它。

```{code-block} ts
:caption: 完整的函数类型（将变量声明为函数）

    let myAdd: (x:number, y:number) => number =
    function(x: number, y: number): number { return x + y; };
```

**函数类型包含两部分：参数类型和返回值类型。** 当写出完整函数类型的时候，这两部分都是需要的。 我们以参数列表的形式写出参数类型，为每个参数指定一个名字和类型。 这个名字只是为了增加可读性。只要参数类型是匹配的，那么就认为它是有效的函数类型，而不在乎参数名是否正确。故而我们也可以这么写：

```{code-block} ts
:caption: 完整的函数类型2

let myAdd: (baseValue: number, increment: number) => number =
    function(x: number, y: number): number { return x + y; };
```

## 可选参数和默认参数

TypeScript 里的每个函数参数都是必须的 （即：传递给一个函数的参数个数必须与函数期望的参数个数一致。）。这不是指不能传递 null 或 undefined 作为参数，而是说编译器检查用户是否为每个参数都传入了值。

JavaScript 里，每个参数都是可选的，可传可不传。没传参的时候，它的值就是 `undefined` 。 在 TypeScript 里我们可以在参数名旁使用 `?` 实现可选参数的功能。*可选参数必须跟在必须参数后面。* 

```{code-block} ts

function buildName(firstName: string, lastName?: string) {
    if (lastName)
        return firstName + " " + lastName;
    else
        return firstName;
}

let result1 = buildName("Bob");  // works correctly now
let result2 = buildName("Bob", "Adams", "Sr.");  // error, too many parameters
let result3 = buildName("Bob", "Adams");  // ah, just right
```

也可以为参数提供一个默认值，当用户没有传递这个参数或传递的值是 undefined 时。它们叫做有默认初始化值的参数。与普通可选参数不同的是，带默认值的参数不需要放在必须参数的后面。 

为了简化或方便，有默认值的参数可以省略类型定义，直接根据值进行类型推导。

```{code-block} ts

function buildName(firstName: string, lastName = "Smith") {
    return firstName + " " + lastName;
}

let result1 = buildName("Bob");                  // works correctly now, returns "Bob Smith"
let result2 = buildName("Bob", undefined);       // still works, also returns "Bob Smith"
let result3 = buildName("Bob", "Adams", "Sr.");  // error, too many parameters
let result4 = buildName("Bob", "Adams");         // ah, just right
```


## 剩余参数

必要参数，默认参数和可选参数有个共同点：它们表示某一个参数。 有时，你想同时操作多个参数，或者你并不知道会有多少参数传递进来。 在 JavaScript 里，你可以使用 `arguments` 来访问所有传入的参数。在TypeScript里，你可以把所有参数收集到一个变量里:

```{code-block} ts

function buildName(firstName: string, ...restOfName: string[]) {
  return firstName + " " + restOfName.join(" ");
}

let employeeName = buildName("Joseph", "Samuel", "Lucas", "MacKinzie");
```


剩余参数会被当做个数不限的可选参数。 可以一个都没有，同样也可以有任意个。 编译器创建参数数组，名字是你在省略号（`...`）后面给定的名字，你可以在函数体内使用这个数组。


