# 响应式数据

````{note}

你可能会好奇：为什么我们需要使用响应式数据(*带有 .value 的 ref*)，而不是普通的变量？为了解释这一点，我们需要简单地讨论一下 Vue 的响应式系统是如何工作的。

当你在模板中使用了一个 ref，然后改变了这个 ref 的值时，Vue 会自动检测到这个变化，并且相应地更新 DOM。这是通过一个基于依赖追踪的响应式系统实现的。当一个组件首次渲染时，Vue 会追踪在渲染过程中使用的每一个 ref。然后，当一个 ref 被修改时，它会触发追踪它的组件的一次重新渲染。

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
````

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

ref toRef 和 toRefs
