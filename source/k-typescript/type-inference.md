# 类型推导 (type inference)

合理的使用类型推论帮助我们保持代码精简和高可读性。

这节介绍TypeScript里的类型推论。即，类型是在哪里如何被推断的。

首先，我们知道，在 TypeScript 里，在有些没有明确指出类型的地方，类型推论会帮助提供类型。如：

```{code-block} ts

let x = 3; //x 被类型推导为 number
```

> 这种推断发生在初始化变量和成员，设置默认参数值和决定函数返回值时。


## 最佳通用类型


当需要从几个表达式中推断类型时候，会使用这些表达式的类型来推断出一个最合适的通用类型。例如，

```{code-block} ts

let x = [0, 1, null];
//let x: (number | null)[]
```

为了推断 *x* 的类型，我们必须考虑所有元素的类型。 这里有两种选择： `number` 和 `null` 。 计算通用类型算法会考虑所有的候选类型，并给出一个兼容所有候选类型的类型（**通常使用联合类型**）。


由于最终的通用类型取自候选类型，有些时候候选类型共享相同的通用类型，但是却没有一个类型能做为所有候选类型的类型。例如：

```{code-block} ts

class Animal{

}

class Rhino extends Animal{

}

class Elephant extends Animal {

}

class Snake extends Animal {

}

let zoo = [new Rhino(), new Elephant(), new Snake()];
// let zoo: (Rhino | Elephant | Snake)[]
let westZoo = [new Rhino(), new Elephant(), new Snake(), new Animal()];
// let westZoo: Animal[]

let eastZoo: Animal[] = [new Rhino(), new Elephant(), new Snake()];
```

很明显，我们想要 zoo 的类型为 Animal[] ，但是这个数组里没有对象是 Animal 类型的，因此不能推断出这个结果。 这个时候需要我们手动添加类型。


## 上下文类型


TypeScript类型推论也可能按照相反的方向进行（即从左至右推导类型）。 这被叫做“按上下文归类”。按上下文归类会发生在表达式的类型与所处的位置相关时。比如：

```{code-block} ts

window.onmousedown = function(mouseEvent) {
    console.log(mouseEvent.button);  //<- Error
};
```
