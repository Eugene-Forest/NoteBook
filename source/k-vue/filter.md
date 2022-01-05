# 过滤器

Vue.js 允许在表达式后面添加可选的过滤器，以管道符表示。

过滤器的本质是一个函数，接受管道符前面的值作为初始值，同时也能接受额外的参数，返回值为经过处理后的输出值。多个过滤器也可以进行串联。

:::{note}

`{{ message | filterA | filterB }}`

在这个例子中，filterA 被定义为接收单个参数的过滤器函数，表达式 message 的值将作为参数传入到函数中。然后继续调用同样被定义为接收单个参数的过滤器函数 filterB，将 filterA 的结果传递到 filterB 中。

`{{ message | filterA('arg1', arg2) }}`:

filterA 被定义为接收三个参数的过滤器函数。其中 message 的值作为第一个参数，普通字符串 'arg1' 作为第二个参数，表达式 arg2 的值作为第三个参数。
:::

## 过滤器注册

Vue.js 提供了全局方法 Vue.filter() 注册一个自定义过滤器，接受过滤器 ID 和过滤器函数两个参数。需要注意的是，**过滤器可以用在两个地方：双花括号插值和 v-bind 表达式 (后者从 2.1.0+ 开始支持)**。

```html
<div id="date-filter">
        <h1>{{new_date | format-date}}</h1>
</div>
```

```javascript
Vue.filter('format-date',function(value){
    return value.getMonth()
})
var vm=new Vue({
    el:'#date-filter',
    data:{
        new_date:new Date(),
    }
})
```

:::{note}

除了可以通过全局定义一个过滤器，也可以同自定义指令一样定义一个组件内的过滤器。在Vue()实例内使用参数filters定义对应过滤器。

```javascript
new Vue({
...
   filters: {
      capitalize: function (value) {
         if (!value) return ''
         value = value.toString()
         return value.charAt(0).toUpperCase() + value.slice(1)
      }
}
...
})
```

:::

## 双向过滤器

之前提及的过滤器都是在数据输出到视图之前，对数据进行转化显示，但不影响数据本身。Vue.js 也提供了在改变视图中数据的值，写回 data 绑定属性中的过滤器，称为双向过滤器。

从使用场景和功能来看，双向过滤器和第 2 章中提到的计算属性有点雷同。若对写操作有转化要求的数据，建议使用计算属性这一特性来实现。 {ref}`点击前往 <computation-attrs>` 。

## 动态参数

过滤器除了能接受单引号（''）括起来的参数外，也支持接受在 vm 实例中绑定的数据，称之为动态参数。使用区别就在于不需要用单引号将参数括起来。

```html
<div id="dynamic-filter">
        <p>动态参数</p>
        <span>{{date | dynamic('string-args',price)}}</span>
</div>
```

```javascript
var dynamic = new Vue({
        el: '#dynamic-filter',
        data: {
                date: new Date(),
                price: [151,151,151]
        },
        filters:{
                'dynamic': function(date,string,price) {
                        return date.toLocaleString()+" : "+string+" : "+ price;
                }
        }
})
```
