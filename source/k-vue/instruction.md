# 指令

## 内置指令

### v-bind

**v-bind 指令可以用于响应式地更新 HTML attribute。**

v-bind 主要用于动态绑定 DOM 元素属性（attribute），即元素属性实际的值是由 vm 实例中的 data 属性提供的。

```{literalinclude} ./example/instruction.html
:language: html
:linenos: true
:lines: 16-20
```

```{literalinclude} ./example/instruction.html
:language: javascript
:linenos: true
:lines: 154-160
```

#### Class与Style绑定

在开发过程中，我们经常会遇到动态添加类名或直接修改内联样式（例如 tab 切换）。
class 和 style 都是 DOM 元素的 attribute，我们当然可以直接使用 v-bind 对这两个属性进行数据绑定，例如 \<p v-bind:style='style'>\<p>，然后通过修改 vm.style 的值对元素样式进行修改。但这样未免过于繁琐而且容易出错，所以 Vue.js 为这两个属性单独做了增强处理，表达式的结果类型除了字符串之外，还可以是对象和数组。

```{literalinclude} ./example/instruction.html
:language: html
:linenos: true
:lines: 88-99
```

```{literalinclude} ./example/instruction.html
:language: javascript
:linenos: true
:lines: 173-180
```

(computation-attrs)=

### 计算属性

在项目开发中，我们展示的数据往往需要经过一些处理。除了在模板中绑定表达式或者利用过滤器外，Vue.js 还提供了计算属性这种方法，避免在模板中加入过重的业务逻辑，保证模板的结构清晰和可维护性。

模板内的表达式非常便利，但是设计它们的初衷是用于简单运算的。在模板中放入太多的逻辑会让模板过重且难以维护。

```html
<div id="app">
                  <p>{{ firstName }}</p>
                  <p>{{ lastName }}</p>
                  <p>{{ fullName }}</p>
          </div>
          <div id="app-2">
                  <p>&yen;{{price}}</p>
                  <input type="text" v-model="cents" />
          </div>
```

```javascript
var vm2=new Vue({
    el:'#app-2',
    data:{
        cents: 100
    },
    computed:{
        price : {
            set : function(newValue){
                this.cents=newValue*100;
            },
            get : function(){
                return (this.cents/100).toFixed(2);
            }
        }
    }
});
var vm = new Vue({
    el: '#app',
    data: {
        firstName: 'Gavin',
        lastName:'CLY'
    },
    computed : {
        fullName : function() {
            // this 指向 vm 实例
            return this.firstName + ' ' + this.lastName
        }
    }
});
```

### v-model

该指令主要用于 input、select、textarea （表单控件） 标签中，具有 lazy、number、debounce（2.0 废除）、trim（2.0 新增）这些修饰符。

```{literalinclude} ./example/instruction.html
:language: html
:linenos: true
:lines: 23-24,37-42,44-54,56-63,65-74
```

```{literalinclude} ./example/instruction.html
:language: javascript
:linenos: true
:lines: 161-172
```

Vue.js 为表单控件提供了一些参数，方便处理某些常规操作。

- lazy : 默认情况下，v-model 在 input 事件中同步输入框值与数据，加 lazy 属性后从会改到在 change 事件中同步。
- number : 会自动将用户输入转为 Number 类型，如果原值转换结果为 NaN 则返回原值。
- trim ： 新增了 trim 修饰符，去掉输入值首尾空格。

```{literalinclude} ./example/instruction.html
:language: html
:linenos: true
:lines: 25-34
```

### v-on 事件绑定与监听

**v-on 指令，它用于监听 DOM 事件**。

通过 v-on 可以绑定实例选项属性 methods 中的方法作为事件的处理器，v-on: 后参数接受所有的原生事件名称。

Vue.js 为指令 v-on 提供了多个修饰符，方便我们处理一些 DOM 事件的细节，并且修饰符可以串联使用。主要的修饰符如下。

- `.stop`: 等同于调用 event. stopPropagation()。
- `.prevent`: 等同于调用 event.preventDefault()。
- `.capture`: 使用 capture 模式添加事件监听器。
- `.self`: 只当事件是从监听元素本身触发时才触发回调。

```{literalinclude} ./example/instruction.html
:language: html
:linenos: true
:lines: 133-145,149
```

```{literalinclude} ./example/instruction.html
:language: javascript
:linenos: true
:lines: 210-227
```

% -----------
% 键盘事件
% -----------

% //todo :add key event for vue

### 条件渲染

v-if/v-else/v-show 这三个指令主要用于根据条件展示对应的模板内容。

```{literalinclude} ./example/instruction.html
:language: html
:linenos: true
:lines: 102-113
```

```{literalinclude} ./example/instruction.html
:language: javascript
:linenos: true
:lines: 181-186
```

### v-for

当包含参数 index 或 key 时，对象参数修改为（item, index）或（value, key），这样与 JS Array 对象的新方法 forEach 和 map，以及一些对象迭代器（例如 lodash）的参数能保持一致。

:::{note}

v-for="n in 10" 中的 n 由原来的 0 ～ 9 迭代变成 1 ～ 10 迭代。
:::

```{literalinclude} ./example/instruction.html
:language: html
:linenos: true
:lines: 116-129
```

```{literalinclude} ./example/instruction.html
:language: javascript
:linenos: true
:lines: 187-208
```

### 其他

```{literalinclude} ./example/instruction.html
:language: html
:linenos: true
:lines: 77-85
```

```{literalinclude} ./example/instruction.html
:language: javascript
:linenos: true
:lines: 229-235
```

#### v-text

v-text，参数类型为 String，作用是更新元素的 textContent。`{{}}` 文本插值本身也会被编译成 textNode 的一个 v-text 指令。而与直接使用 `{{}}` 不同的是，v-text 需要绑定在某个元素上，能避免未编译前的闪现问题。

#### v-HTML

v-HTML, 参数类型为 String，作用为更新元素的 innerHTML，接受的字符串不会进行编译等操作，按普通 HTML 处理。

#### v-once

v-once 指令是 Vue.js 2.0 中新增的内置指令，用于标明元素或组件只渲染一次，即使随后发生绑定数据的变化或更新，该元素或组件及包含的子元素都不会再次被编译和渲染。

#### v-pre

v-pre 指令相对简单，就是跳过编译这个元素和子元素，用来减少编译时间。

#### v-cloak

v-cloak 指令相当于在元素上添加了一个 `[v-cloak]` 的属性，直到关联的实例结束编译。官方推荐可以和 css 规则 `[v-cloak]{ display :none }` 一起使用，可以隐藏未编译的（`{{}}`） Mustache 标签直到实例准备完毕。

## 自定义指令

### 指令的注册

#### 全局注册

可以通过 Vue.directive(id, definition) 方法注册一个全局自定义指令，接收参数 id 和定义对象。

```html
<body>
    <h2>指令的注册</h2>
    <div id="basic">
            <span>全局指令注册</span>
            <div v-if="isExist" v-consloe-show="param"></div>
    </div>
</body>
```

```javascript
Vue.directive('consloe-show',{
    bind : function(){
        console.log('bind',arguments)
    },
    update:function(value,oldValue){
        console.log('update',value,oldValue)
    },
    unbind:function(){
        console.log('unbind',arguments)
    }
})
var consloe_show=new Vue({
    el:'#basic',
    data:{
        param:'first',
        isExist:true
    }
})
```

#### 组件局部注册

也可以通过在组件的 directives 选项注册一个局部的自定义指令。

```javascript
var comp=Vue.extend({
    directives:{
        'localDirective':{} //
    }
})
```

% // todo : add 指令在组件局部注册的实例

% 指令实例属性
% ---------------

% //todo : add 指令实例属性,指令的高级选项

% 指令的高级选项
% ------------------
