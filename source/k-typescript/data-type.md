# 数据类型以及变量

## 数据类型

* **布尔值** (`boolean`)
  
   简单的 true/false 值

   ```{code-block} ts
   let isDone: boolean = false;
   ```

* **字符串** (`string`)
   
   可以使用双引号（"）或单引号（'）表示字符串。

    ```{code-block} ts

    let name: string = "bob";
    name = "smith";
    ```

* **数值** (`number`)

    和JavaScript一样，TypeScript里的所有数字都是 **浮点数** 。*除了支持十进制和十六进制字面量，TypeScript还支持ECMAScript 2015中引入的二进制和八进制字面量。*

    ```{code-block} ts

    let decLiteral: number = 6;
    let hexLiteral: number = 0xf00d;
    let binaryLiteral: number = 0b1010;
    let octalLiteral: number = 0o744;
    ```

* **数组** 

    TypeScript像JavaScript一样可以操作数组元素。

    ```{code-block} ts

    //第一种方法：可以在元素类型后面接上[]，表示由此类型元素组成的一个数组：
    let list: number[] = [1, 2, 3];
    //第二种方法 ：使用数组泛型，Array<元素类型>：
    let list: Array<number> = [1, 2, 3];
    ```


* **元组** (`tuple`) [^tuple]

    元组类型允许表示一个已知元素数量和类型的数组。

    * 访问元组，元组中元素使用索引来访问，第一个元素的索引值为 0，第二个为 1，以此类推
    * 元组是可变的，这意味着我们可以用过通过索引对元组进行更新操作。
    * 可以使用以下两个函数向元组添加新元素或者删除元素：
      * push() 向元组添加元素，添加在最后面。
      * pop() 从元组中移除元素（最后一个），并返回移除的元素。
    * 解构元组\*，可以把元组元素赋值给变量

    ```{code-block} ts

    // Declare a tuple type
    let x: [string, number];
    // Initialize it
    x = ['hello', 10]; // OK
    // Initialize it incorrectly
    x = [10, 'hello']; // Error
    ```

* **枚举** (`enum`)
  使用枚举类型可以为 **一组数值** 赋予友好的名字。默认情况下，从0开始为元素编号。当然你也可以手动的指定成员的开始数值或全部数值。

    ```{code-block} ts

    //默认
    enum Color {Red, Green, Blue}
    let c: Color = Color.Green;
    //指定首个成员的值
    enum Color {Red = 1, Green, Blue}
    let c: Color = Color.Green;
    //指定所有成员的值
    enum Color {Red = 1, Green=3, Blue=6}
    let c: Color = Color.Green;
    ```

* **任意类型** (`any`)

    它允许你在编译时可选择地包含或移除类型检查。

* **void** 

    当一个函数没有返回值时，通常会见到其返回值类型是 void。*声明一个 void 类型的变量没有什么大用，因为你只能为它赋予 undefined 和 null 。*

* **null 和 undefined** (`null` / `undefine`)

    默认情况下 null 和 undefined 是所有类型的子类型。 就是说你可以把null和undefined赋值给 number 类型的变量。

    然而，当你指定了`--strictNullChecks`标记， null 和 undefined 只能赋值给 void 和它们各自（ void 和它们各自类型的对象）。这能避免很多常见的问题。

* **never**

  never 类型表示的是那些永不存在的值的类型。 例如，never 类型是那些总是会抛出异常或根本就不会有返回值的函数表达式或箭头函数表达式的返回值类型； 变量也可能是 never 类型，当它们被永不为真的类型保护所约束时。never 类型是任何类型的子类型，也可以赋值给任何类型。

    ```{code-block} ts

    // 返回never的函数必须存在无法达到的终点
    function error(message: string): never {
        throw new Error(message);
    }

    // 推断的返回值类型为never
    function fail() {
        return error("Something failed");
    }

    // 返回never的函数必须存在无法达到的终点
    function infiniteLoop(): never {
        while (true) {
        }
    }
    ```

````{admonition} 模版字符串

使用模版字符串，它可以定义多行文本和内嵌表达式。 这种字符串是被反引号包围（`` ` ``），并且以 `${ expr }` 这种形式嵌入表达式。

```{code-block} ts

let name: string = `Gene`;
let age: number = 37;
//使用模板字符串
let sentence: string = `Hello, my name is ${ name }.

I'll be ${ age + 1 } years old next month.`;
//上文 sentence 变量的定义与此举定义相同：
let sentence: string = "Hello, my name is " + name + ".\n\n" +
    "I'll be " + (age + 1) + " years old next month.";
```

````


````{admonition} 元组的定义和直接赋值的区别

```{code-block} ts
:caption: 先定义元组，再赋值

//定义元组
let my_tuple: [string, number, string];
//赋值
my_tuple = ["eugene", 1, "forest"];
console.log(my_tuple[0]);
console.log(my_tuple);

my_tuple.push("eugene")
console.log(my_tuple);

my_tuple[3] = 3; //error
console.log(my_tuple);

// 控制台输出：
// eugene
// ['eugene', 1, 'forest']
// ['eugene', 1, 'forest', 'eugene']
// ['eugene', 1, 'forest', 'eugene']
```

```{code-block} ts
:caption: 直接赋值元组

//直接赋值元组
let my_tuple = ["eugene", 1, "forest"];
console.log(my_tuple[0]);
console.log(my_tuple);

my_tuple.push("eugene")
console.log(my_tuple);

my_tuple[3] = 3; 
console.log(my_tuple);

//控制台输出：
//eugene
//[ 'eugene', 1, 'forest' ]
//[ 'eugene', 1, 'forest', 'eugene' ]
//[ 'eugene', 1, 'forest', 3 ]
```
````

## 类型断言

**类型断言好比其它语言里的类型转换**，但是不进行特殊的数据检查和解构。 它没有运行时的影响，只是在编译阶段起作用。

类型断言有两种形式。 其一是`“尖括号”`语法：

```{code-block} ts

let someValue: any = "this is a string";

let strLength: number = (<string>someValue).length;
```


另一个为 `as` 语法：

```{code-block} ts

let someValue: any = "this is a string";

let strLength: number = (someValue as string).length;
```

两种形式是等价的。*然而，当在TypeScript里使用JSX时，只有as语法断言是被允许的。*



----

[^tuple]: 元组（tuple）是关系数据库中的基本概念，关系是一张表，表中的每行（即数据库中的每条记录）就是一个元组，每列就是一个属性。 在二维表里，元组也称为行。 
