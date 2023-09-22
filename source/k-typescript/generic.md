# 泛型

软件工程中，我们不仅要创建一致的定义良好的API，同时也要考虑可重用性。 组件不仅能够支持当前的数据类型，同时也能支持未来的数据类型，这在创建大型系统时为你提供了十分灵活的功能。

## 泛型方法

一个简单的值返回方法，不用泛型的话，这个函数可能是下面这样：

```{code-block} ts
:caption: 例一

function identity(arg: number): number {
    return arg;
}
```

或者使用  `any` 类型来适应代码复用：

```{code-block} ts
:caption: 例二

function identity(arg: any): any {
    return arg;
}
```

使用 `any` 类型虽然可以使得这个函数可以接收任何类型的 `arg` 参数，这样就丢失了一些信息：传入的类型与返回的类型应该是相同的。 如果使用例二的函数，那么我们传入一个数字，这时候我们只知道任何类型的值都有可能被返回。

因此，我们需要一种方法使返回值的类型与传入参数的类型是相同的。 这里，我们使用了 *类型变量* ，它是一种特殊的变量，只用于表示类型而不是值。

```{code-block} ts
:caption: 类型变量

function identity<T>(arg: T): T {
    return arg;
}
```

我们把这个版本的 *identity* 函数叫做泛型函数，因为它可以适用于多个类型。 不同于使用 any ，它不会丢失信息，像第一个例子那像保持准确性，传入数值类型并返回数值类型。

泛型函数可以用两种方法使用。

* 第一种是，传入所有的参数，包含类型参数：

```{code-block} ts

let output = identity<string>("myString");  // type of output will be 'string'

```

* 利用类型推论 – 即编译器会根据传入的参数自动地帮助我们确定T的类型：

```{code-block} ts

let output = identity("myString");  // type of output will be 'string'

```


注意我们没必要使用尖括号（`<>`）来明确地传入类型；编译器可以查看 *myString* 的值，然后把 `T` 设置为它的类型。 **类型推论帮助我们保持代码精简和高可读性。** 如果编译器不能够自动地推断出类型的话，只能像上面那样明确的传入 `T` 的类型，在一些复杂的情况下，这是可能出现的。


## 泛型变量以及约束

我们有时候想操作某类型的一组值，并且我们知道这组值具有什么样的属性，但是作为一个类型变量没有约束的泛型方法，如果想要对泛型变量进行操作是比较麻烦的：

```{code-block} ts
:caption: 没有类型约束的泛型方法和 any 方法

function identity<T>(arg: T): T {
    return arg.length; //error，编译错误
}

function print(arg: any): any {
    return arg.length; //maybe error
}

```

我们可以定义一个接口或类用来描述类型变量的约束：

```{code-block} ts

enum Gender {
    woman, man
}

class Person {
    private _name: string;
    private _age: number;
    private _gender: Gender;
    //getter && setter

}

function whoAmI<T extends Person>(human: T): string {
    return "My name is " + human.Name;
}
```

## 泛型变量

泛型函数的类型与非泛型函数的类型没什么不同，只是有一个类型参数在最前面，像函数声明一样：

```{code-block} ts

function identity<T>(arg: T): T {
    return arg;
}

let myIdentity: <T>(arg: T) => T = identity;
```

## 泛型类


```{code-block} ts

class GenericNumber<T> {
    zeroValue: T;
    add: (x: T, y: T) => T;
}

let myGenericNumber = new GenericNumber<number>();
myGenericNumber.zeroValue = 0;
myGenericNumber.add = function(x, y) { return x + y; };
```

我们在类那节说过，类有两部分：静态部分和实例部分。 **泛型类指的是实例部分的类型，所以类的静态属性不能使用这个泛型类型。**



## 在泛型约束中使用类型参数

你可以声明一个类型参数，且它被另一个类型参数所约束。 比如，现在我们想要用属性名从对象里获取这个属性。 并且我们想要确保这个属性存在于对象 `obj` 上，因此我们需要在这两个类型之间使用约束。

```{code-block} ts

function getProperty<T, K extends keyof T>(obj: T, key: K) {
    return obj[key];
}

let x = { a: 1, b: 2, c: 3, d: 4 };

getProperty(x, "a"); // okay
getProperty(x, "m"); // error: Argument of type 'm' isn't assignable to 'a' | 'b' | 'c' | 'd'.
```
