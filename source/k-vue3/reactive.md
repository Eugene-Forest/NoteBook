# 响应式数据

你可能会好奇：为什么我们需要使用响应式数据(_带有 .value 的 ref_)，而不是普通的变量？为了解释这一点，我们需要简单地讨论一下 Vue 的响应式系统是如何工作的。

```{admonition} 模板
:class: margin

所谓模板，指 Vue 文件的 `<template>` 标签模块。
```

当你在 **_模板_** 中使用了一个 ref，然后改变了这个 ref 的值时，Vue 会自动检测到这个变化，并且相应地更新 DOM。这是通过一个基于依赖追踪的响应式系统实现的。当一个组件首次渲染时，Vue 会追踪在渲染过程中使用的每一个 ref。然后，当一个 ref 被修改时，它会触发追踪它的组件的一次重新渲染。

在标准的 JavaScript 中，检测普通变量的访问或修改是行不通的。然而，我们可以通过 getter 和 setter 方法来拦截对象属性的 get 和 set 操作。

该 .value 属性给予了 Vue 一个机会来检测 ref 何时被访问或修改。在其内部，Vue 在它的 getter 中执行追踪，在它的 setter 中执行触发。从概念上讲，你可以将 ref 看作是一个像这样的对象：

```{code-block} js

// 伪代码，不是真正的实现
const myRef = {
_value: 0,
get value() {
   track()//触发取值
   return this._value
},
set value(newValue) {
   this._value = newValue
   trigger()//触发赋值
}
}
```

## `ref()`

在组合式 API 中，推荐使用 `ref()` 函数来声明响应式状态，ref() 接收参数，并将其包裹在一个带有 `.value` 属性的 ref 对象中返回。

```ts
import { ref } from "vue";

const count = ref(0);

console.log(count); // { value: 0 }
console.log(count.value); // 0

count.value++;
console.log(count.value); // 1
```

可以发现，我们在 ts 代码块上针对 ref 对象的所有操作都要进行解包操作才能读取到实际的值。

```{code-block} html

<div>{{ count }}</div>
```

但是在模板中使用 ref 时，我们不需要附加 `.value`。为了方便起见，当在模板中使用时，ref 会自动解包。不过需要注意的是，在模板渲染上下文中，只有顶级的 ref 属性才会被解包。在下面的例子中，count 和 object 是顶级属性，但 object.id 不是

```{code-block} ts

const count = ref(0)
const object = { id: ref(1) }

```

```{code-block} html

<!-- 正确 -->
<div>{{ count }}</div>

<!-- 正确 -->
<div>{{ count + 1 }}</div>

<!-- 正确 -->
<div>{{ object.id }}</div>

<!-- 错误 -->
<div>{{ object.id + 1 }}</div>

```

### 深层响应性

Ref 可以持有任何类型的值，包括深层嵌套的对象、数组或者 JavaScript 内置的数据结构，比如 Map。

Ref 会使它的值具有深层响应性。这意味着即使改变嵌套对象或数组时，变化也会被检测到。

```{code-block} js

import { ref } from 'vue'

const obj = ref({
  nested: { count: 0 },
  arr: ['foo', 'bar']
})

function mutateDeeply() {
  // 以下都会按照期望工作
  obj.value.nested.count++
  obj.value.arr.push('baz')
}
```

但是，滥用这个特性将会导致性能问题。可以通过 shallow ref 来放弃深层响应性。对于浅层 ref，只有 .value 的访问会被追踪。浅层 ref 可以用于避免对大型数据的响应性开销来优化性能、或者有外部库管理其内部状态的情况。

### DOM 更新时机

当修改了响应式状态时，DOM 会被自动更新。但是需要注意的是，DOM 更新不是同步的。Vue 会在“`next tick`”更新周期中缓冲所有状态的修改，以确保不管你进行了多少次状态修改，每个组件都只会被更新一次。

通常，我们使用响应式数据就是为了能够在改变数据后进行 Dom 的更新。但是，部分业务可能需要在 Dom 更新完成之后才进行，那么，要等待 DOM 更新完成后再执行额外的代码，可以使用 `nextTick()` 全局 API

```{code-block} js

import { nextTick } from 'vue'

async function increment() {
  count.value++
  await nextTick()
  // 现在 DOM 已经更新了
}
```

## `reactive()`

还有另一种声明响应式状态的方式，即使用 reactive() API。与将内部值包装在特殊对象中的 ref 不同，reactive() 将使对象本身具有响应性：

```{code-block} html

<template>
    <button @click="state.count++">
    {{ state.count }}
    </button>
</template>

<script setup>
import { reactive } from 'vue'

const state = reactive({ count: 0 })
</script>
```

-   值得注意的是，reactive() 返回的是一个原始对象的 Proxy，它和原始对象是不相等的

-   **只有代理对象是响应式的，更改原始对象不会触发更新。因此，使用 Vue 的响应式系统的最佳实践是仅使用你声明对象的代理版本。**

-   为保证访问代理的一致性，对同一个原始对象调用 reactive() 会总是返回同样的代理对象，而对一个已存在的代理对象调用 reactive() 会返回其本身

-   依靠深层响应性，响应式对象内的嵌套对象依然是代理

```{code-block}js

const raw = {}
const proxy = reactive(raw)

// 代理对象和原始对象不是全等的
console.log(proxy === raw) // false

// 在同一个对象上调用 reactive() 会返回相同的代理
console.log(reactive(raw) === proxy) // true

// 在一个代理上调用 reactive() 会返回它自己
console.log(reactive(proxy) === proxy) // true


```

reactive() API 有一些局限性：

-   有限的值类型：它只能用于对象类型 (对象、数组和如 Map、Set 这样的集合类型)。它不能持有如 string、number 或 boolean 这样的原始类型。

-   不能替换整个对象：由于 Vue 的响应式跟踪是通过属性访问实现的，因此我们必须始终保持对响应式对象的相同引用。这意味着我们不能轻易地“替换”响应式对象，因为这样的话与第一个引用的响应性连接将丢失：

```js
let state = reactive({ count: 0 });

// 上面的 ({ count: 0 }) 引用将不再被追踪
// (响应性连接已丢失！)
state = reactive({ count: 1 });
```

-   对解构操作不友好：当我们将响应式对象的原始类型属性解构为本地变量时，或者将该属性传递给函数时，我们将丢失响应性连接：

```js
const state = reactive({ count: 0 });

// 当解构时，count 已经与 state.count 断开连接
let { count } = state;
// 不会影响原始的 state
count++;

// 该函数接收到的是一个普通的数字
// 并且无法追踪 state.count 的变化
// 我们必须传入整个对象以保持响应性
callSomeFunction(state.count);
```

## ref 、 toRef 和 toRefs

-   ref
    1. 生成值类型的响应式数据, 通过 .value 修改值
    2. 可用于 reactive 中
    3. 可用于获取 Dom
-   toRef
    -   针对一个响应式对象的 prop, 创建一个 ref，具有响应式, 两者保持引用关系
-   toRefs
    -   toRefs 将响应式对象变成普通对象后，每一个属性都具有响应式 ref

由于 `reactive` 命令封装的响应对象在解构的时候会丢失响应特性，所以引申出 `toRef` 以及 `toRefs` 命令。

```{code-block} js

const proxyTom = reactive({
    name: 'JL',
    age: 18
})

//1. 通过 toRef 进行指定属性的解构
const ageRef = toRef(proxyTom, "age");
//2. 通过 toRefs 进行的所有属性的解构，需要特别注意这个解构对象的各个属性与代理对象的属性同名
const { name, age } = toRefs(proxyTom);
//3. 解构成普通对象，但是所有属性都是响应式
const tempTom = toRefs(proxyTom);
```

从写法上来说，不建议第二个方式的解构方式，除非能保证代理对象的属性名不会出现业务上的重名问题（这是比较困难的）。

```{note}

***“`reactive` 做对象的响应式，`ref` 做值类型响应式”***

可能你会认为上面这句是有道理的，但是这句话是比较片面甚至误导初学者的。

首先从语法上， `ref` 既可以做值响应，也可以做对象响应；而 `reactive` 只能做对象响应而没有办法做值响应。由于命令最初的定义问题，导致 `reactive` 可以相对于 `ref` 在非模板代码中更加方便的解构，但是其部分特性带来的歧义也不可小视，例如解构后的解构不再带有响应式。

`reactive` 带来的解构语法的便利性是否会带来最终代码的阅读和维护问题，这个可能也是因人而异的问题。

```
