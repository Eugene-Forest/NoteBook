# 类（class） 与 接口 （interface）

传统的JavaScript程序使用函数和基于原型的继承来创建可重用的组件，

类

* 不允许存在多个构造器实现。
* 



接口：

* 成员属性默认为公有，不能为私有或保护。
* 

## 类 （class）

```{code-block} ts
:caption: 一个简单的类的实例

class Greeter {
    greeting: string;
    constructor(message: string) {
        this.greeting = message;
    }
    greet() {
        return "Hello, " + this.greeting;
    }
}

let greeter = new Greeter("world");
```

### 通过 `extends` 关键字实现继承

```{code-block} ts

class Animal {
    name: string;
    constructor(theName: string) { this.name = theName; }
    move(distanceInMeters: number = 0) {
        console.log(`${this.name} moved ${distanceInMeters}m.`);
    }
}

class Snake extends Animal {
    constructor(name: string) { super(name); }
    move(distanceInMeters = 5) {
        console.log("Slithering...");
        super.move(distanceInMeters);
    }
}

class Horse extends Animal {
    constructor(name: string) { super(name); }
    move(distanceInMeters = 45) {
        console.log("Galloping...");
        super.move(distanceInMeters);
    }
}

let sam = new Snake("Sammy the Python");
let tom: Animal = new Horse("Tommy the Palomino");

sam.move();
tom.move(34);

// -------CONSOLE--------
// Slithering...
// Sammy the Python moved 5m.
// Galloping...
// Tommy the Palomino moved 34m.
// ----------------------
```

派生类包含了一个构造函数，它必须调用 `super()` ，它会执行基类的构造函数。 而且，在构造函数里访问 `this` 的属性之前，我们一定要调用 `super()` 。 这个是 TypeScript 强制执行的一条重要规则。


### 访问控制修饰符

在TypeScript里，如果成员没有被显示地声明访问控制修饰符，成员都默认为 `public` 。

* 当成员被标记为 `public` 时，它可以在声明它的类的外部访问（通过对象）。
* 当成员被标记成 `private` 时，它就不能在声明它的类的外部访问。
* `protected` 修饰符与 `private` 修饰符的行为很相似，但有一点不同， `protected` 成员在派生类中仍然可以访问。
* 当成员被标记为 `readonly` 时，成员将被设置为只读，且必须在声明时或构造函数里被初始化。

#### public

TypeScript 使用的是结构性类型系统。 当我们比较两种不同的类型时，并不在乎它们从何处而来，如果所有成员的类型都是兼容的，我们就认为它们的类型是兼容的。

```{code-block} ts
:caption: 不同类型相同结构的对象的兼容性

class Person {
    public name: string;
    constructor(name: string) {
        this.name = name;
    }
}

class Monkey {
    public name: string;
    constructor(name: string) {
        this.name = name;
    }
}

let human: Person = new Person("Jon");
let monkey: Monkey = new Monkey("A");
human = monkey;

// console.log(human);
// -------CONSOLE--------
// Monkey { name: 'A' }
// ----------------------
```


#### private

不同类型相同结构的对象的兼容性在有成员被 `private` 或 `protect` 修饰时失效。

```{code-block} ts
:caption: 不同类型相同结构的对象的兼容性在有成员被 private 或 protect 修饰时失效

class Person {
    public name: string;
    private age: number;
    constructor(name: string) {
        this.name = name;
    }
}

class Child extends Person {
    private Id = "Kid";
    constructor(name: string) {
        super(name);
    }
}

class Monkey {
    public name: string;
    private age: number;
    constructor(name: string) {
        this.name = name;
    }
}

let human: Person = new Person("Jon");
let monkey: Monkey = new Monkey("A");
let child: Child = new Child("Jack");
human = child;
// human = monkey; //error 类型具有私有属性“age”的单独声明。
console.log(human);

// -------CONSOLE--------
// Child { name: 'Jack', Id: 'Kid' }
// ----------------------
```

#### protect

构造函数也可以被标记成 `protected` 。 这意味着这个类不能在包含它的类外被实例化，但是能被继承。比如:


```{code-block} ts


class Person {
    protected name: string;
    protected constructor(theName: string) { this.name = theName; }
}

// Employee 能够继承 Person
class Employee extends Person {
    private department: string;

    constructor(name: string, department: string) {
        super(name);
        this.department = department;
    }

    public getElevatorPitch() {
        return `Hello, my name is ${this.name} and I work in ${this.department}.`;
    }
}

let howard = new Employee("Howard", "Sales");
let john = new Person("John"); // 错误: 'Person' 的构造函数是被保护的.
```


#### readonly

当成员被标记为 `readonly` 时，成员将被设置为只读，且必须在声明时或构造函数里被初始化。且不能被再次赋值。

```{code-block} ts

class Octopus {
    readonly name: string;
    readonly numberOfLegs: number = 8;
    constructor (theName: string) {
        this.name = theName;
    }
}
let dad = new Octopus("Man with the 8 strong legs");
dad.name = "Man with the 3-piece suit"; // 错误! name 是只读的
```

### 参数属性


仅在构造函数里使用参数来创建和初始化成员。即把声明和赋值合并至一处。参数属性通过给构造函数参数添加一个访问限定符来声明。 使用 `private` 限定一个参数属性会声明并初始化一个私有成员；对于 `public` 和 `protected` 来说也是一样。

```{code-block} ts

class ReadOnly {
    public name: string;
    readonly full_name: string;

    constructor(private firstName: string, private lastName: string) {
        this.full_name = `${firstName} * ${lastName}`;
        this.name = this.full_name;
    }

    public changeFullName() {
        // this.full_name = "change it"; //error 无法分配到 "full_name" ，因为它是只读属性。
    }
}

let readonly = new ReadOnly("eugene", "forest");
console.log(readonly);
// readonly.full_name = "change it"; //error 无法分配到 "full_name" ，因为它是只读属性。

// -------CONSOLE--------
// ReadOnly {
//   firstName: 'eugene',
//   lastName: 'forest',
//   full_name: 'eugene * forest',
//   name: 'eugene * forest'
// }
// ----------------------
```


### 存取器

TypeScript 支持通过 *getters/setters* 来截取对对象成员的访问。 它能帮助你有效的控制对对象成员的访问。

对于存取器有下面几点需要注意的：

首先，存取器要求你将编译器设置为输出 *ECMAScript 5* 或更高。 不支持降级到 *ECMAScript 3* 。 **其次，只带有 *get* 不带有 *set* 的存取器自动被推断为 *readonly* 。**

```{code-block} ts

let passcode = "secret passcode";

class Employee {
    private _fullName: string;

    get fullName(): string {
        return this._fullName;
    }

    set fullName(newName: string) {
        if (passcode && passcode == "secret passcode") {
            this._fullName = newName;
        }
        else {
            console.log("Error: Unauthorized update of employee!");
        }
    }
}

let employee = new Employee();
employee.fullName = "Bob Smith";
if (employee.fullName) {
    console.log(employee.fullName);
}


// if passcode = "secret passcode" : outputs  "Bob Smith"
// else : outputs  Error: Unauthorized update of employee!
```


### 静态属性 (`static`)

到目前为止，我们只讨论了类的实例成员，那些仅当类被实例化的时候才会被初始化的属性。 我们也可以创建类的静态成员，这些属性存在于类本身上面而不是类的实例上。如同在实例属性上使用 `this.` 前缀来访问属性一样，这里我们使用 `类名.` 来访问静态属性。

```{code-block} ts

class Grid {
    static origin = {x: 0, y: 0};
    calculateDistanceFromOrigin(point: {x: number; y: number;}) {
        let xDist = (point.x - Grid.origin.x);
        let yDist = (point.y - Grid.origin.y);
        return Math.sqrt(xDist * xDist + yDist * yDist) / this.scale;
    }
    constructor (public scale: number) { }
}

let grid1 = new Grid(1.0);  // 1x scale
let grid2 = new Grid(5.0);  // 5x scale

console.log(grid1.calculateDistanceFromOrigin({x: 10, y: 10}));
console.log(grid2.calculateDistanceFromOrigin({x: 10, y: 10}));
```

### 抽象类

`abstract` 关键字是用于定义抽象类和在抽象类内部定义抽象方法。

抽象类做为其它派生类的基类使用。 它们一般不会直接被实例化。 不同于接口，抽象类可以包含成员的实现细节。

```{code-block} ts
:caption: 简单的抽象类

abstract class Animal {
    abstract makeSound(): void;
    move(): void {
        console.log('roaming the earch...');
    }
}
```

抽象类中的抽象方法不包含具体实现并且必须在 派生类 中实现。


```{code-block} ts



abstract class Creature {

    public print() {
        console.log("I am creature!");
    }

    abstract printMessage(message: string): void;

    abstract communicate(): string;
}

abstract class Person extends Creature {

    public print() {
        console.log("I am Human!");
    }

    abstract printMessage(message: string): void;
}

class Man extends Person {

    public print() {
        console.log("I am iron man!");
    }

    printMessage(message: string): void {
        console.log(message);
    }

    communicate(): string {
        return "I am iron man!";
    }
}

let eugene = new Man();
eugene.print();
eugene.printMessage("eugene forest");
console.log(eugene.communicate());

// -------CONSOLE--------
// I am iron man!
// eugene forest
// I am iron man!
// ----------------------
```

## 接口 （interface）

TypeScript 的核心原则之一是对值所具有的结构进行类型检查。 它有时被称做“鸭式辨型法”或“结构性子类型化”。 *在 TypeScript 里，接口的作用就是为这些类型命名和为你的代码或第三方代码定义契约。*


类型检查器会检查函数的调用。我们向函数传入的对象参数实际上会包含很多属性，但是*编译器只会检查那些必需的属性是否存在，并且其类型是否匹配*。

```{code-block} ts
:caption: 例一：函数的对象参数的类型检查

function printLabel(labelledObj: { label: string }) {
  console.log(labelledObj.label);
}

let myObj = { size: 10, label: "Size 10 Object" };
printLabel(myObj);
```


```{code-block} ts
:caption: 例二：通过接口来实现函数的对象参数的类型检查

interface LabelledValue {
  label: string;
}

function printLabel(labelledObj: LabelledValue) {
  console.log(labelledObj.label);
}

let myObj = {size: 10, label: "Size 10 Object"};
printLabel(myObj);
```

需要注意的是，我们在这里并不能像在其它语言里一样，说传给 *printLabel* 的对象实现了这个接口。我们只会去关注值的外形。 只要传入的对象满足上面提到的必要条件，那么它就是被允许的。

对比例一和例二，可以知道对于以接口实现的函数参数，类型检查器会检查传入的参数的属性名及其类型，只有当传入的参数的值的结构与接口定义的相同时，编译才不会报错。


### 可选属性

接口里的属性不全都是必需的。 有些是只在某些条件下存在，或者根本不存在。 可选属性在应用 *“option bags”* 模式时很常用，即给函数传入的参数对象中只有部分属性赋值了。


带有可选属性的接口与普通的接口定义差不多，只是在可选属性名字定义的后面加一个 `?` 符号。

```{code-block} ts
:caption: option bags 模式的应用

interface SquareConfig {
  color?: string;
  width?: number;
}

function createSquare(config: SquareConfig): {color: string; area: number} {
  let newSquare = {color: "white", area: 100};
  if (config.color) {
    newSquare.color = config.color;
  }
  if (config.width) {
    newSquare.area = config.width * config.width;
  }
  return newSquare;
}

let mySquare = createSquare({color: "black"});
```

可选属性的好处之一是可以对可能存在的属性进行预定义，好处之二是可以捕获引用了不存在的属性时的错误。


### 只读属性

一些对象属性只能在对象刚刚创建的时候修改其值。 你可以在属性名前用 `readonly` 来指定只读属性:

```{code-block} ts

interface Point {
    readonly x: number;
    readonly y: number;
}
```



### 额外的属性检查

我们在上面了解了可选函数的用法，而且也知道了 TypeScript 可以让我们传入 { size: number; label: string; } 到仅期望得到 { label: string; } 的函数里。那么，如果同时在一个函数里使用使用这两个语法，会如何？

如下代码所示，我们期望能够将一个包含了部分接口的可选属性的对象传入函数中：

```{code-block} ts

interface SquareConfig {
    color?: string;
    width?: number;
}

function createSquare(config: SquareConfig): { color: string; area: number } {
    // ...
}

let mySquare = createSquare({ colour: "red", width: 100 }); //error:对象文字只能指定已知的属性，但“colour”中不存在于类型“SquareConfig”。

//绕开这些检查非常简单。 最简便的方法是使用类型断言：

let myNewSquare = createSquare({ width: 100, opacity: 0.5 } as SquareConfig);
```

对象字面量赋值给变量或作为参数传递的时候，会被特殊对待而且会经过额外属性检查。如果一个对象字面量存在任何“目标类型”不包含的属性时，你会得到一个错误。


```{code-block} ts
:caption: 避免对象字面量与可选属性接口的函数参数混合使用

interface SquareConfig {
    color?: string;
    width?: number;
}

function createSquare(config: SquareConfig): void {
    // ...
    console.log(config)
}

let config = { colour: "red", width: 100 }; //没有指定类型，所以对象字面量赋值成功

createSquare(config);  //success
```


如果你能够确定这个对象可能具有某些做为特殊用途使用的额外属性,最佳的方式是能够添加一个字符串索引签名。

```{code-block} ts

//接口带有定义的类型的color和width属性，并且还会带有任意数量的其它属性
interface SquareConfig {
    color?: string;
    width?: number;
    [propName: string]: any;
}
```


