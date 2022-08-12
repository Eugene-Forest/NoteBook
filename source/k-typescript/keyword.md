# 关键字


## keyof

*TypeScript* 允许我们遍历某种类型的属性，并通过 `keyof` 操作符提取其属性的名称。

`keyof` 操作符是在 *TypeScript 2.1* 版本引入的，**该操作符可以用于获取某种类型的所有键**，其返回类型是联合类型。

```{code-block} ts

interface Person {
  name: string;
  age: number;
  location: string;
}

type K1 = keyof Person; // "name" | "age" | "location"
type K2 = keyof Person[];  // number | "length" | "push" | "concat" | ...
type K3 = keyof { [x: string]: Person };  // string | number
```



```{code-block} ts


class Person {
  name: string = "Semlinker";
}

let sname: keyof Person;
sname = "name";
// 若把 sname = "name" 改为 sname = "age" 的话，TypeScript 编译器会提示以下错误信息：

// Type '"age"' is not assignable to type '"name"'.
```



### 在泛型约束中使用类型参数

你可以声明一个类型参数，且它被另一个类型参数所约束。 比如，现在我们想要用属性名从对象里获取这个属性。 并且我们想要确保这个属性存在于对象 `obj` 上，因此我们需要在这两个类型之间使用约束。

```{code-block} ts

function getProperty<T, K extends keyof T>(obj: T, key: K) {
    return obj[key];
}

let x = { a: 1, b: 2, c: 3, d: 4 };

getProperty(x, "a"); // okay
getProperty(x, "m"); // error: Argument of type 'm' isn't assignable to 'a' | 'b' | 'c' | 'd'.
```


## typeof 

`typeof` 操作符用于获取变量的类型。因此这个操作符的后面接的始终是一个变量，且需要运用到类型定义当中。为了方便大家理解，我们来举一个具体的示例：

```{code-block} ts

const COLORS = {
  red: 'red',
  blue: 'blue'
}

// 首先通过typeof操作符获取color变量的类型，然后通过keyof操作符获取该类型的所有键，
// 即字符串字面量联合类型 'red' | 'blue'
type Colors = keyof typeof COLORS 
let color: Colors;
color = 'red' // Ok
color = 'blue' // Ok

// Type '"yellow"' is not assignable to type '"red" | "blue"'.
color = 'yellow' // Error
```


<!-- ## instanceof -->
