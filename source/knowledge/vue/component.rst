===================
组件
===================

组件的使用
===============

无论是使用全局组件还是局部组件，它都需要经过三个步骤：

* 创建组件
* 将组件注册到应用
* 将组件于有root根即有Vue实例的标签内使用


Vue.js 创建组件构造器的方式如下代码所示：

.. code-block:: javascript

		var MyComponent = Vue.extend({
			template: '<p>This is a component</p>'
		});

这样，我们就获得了一个组件构造器，但现在还无法直接使用这个组件，需要将组件注册到应用中。

**对于组件的命名，W3C 规范是字母小写且包含一个短横杠“-”。**

与过滤器和指令一样，组件的注册也有全局和局部之分。

全局注册
----------

.. code-block:: javascript

		Vue.component('my-component', MyComponent);

这个组件是全局注册的。也就是说它们在注册之后可以用在任何新创建的 Vue 根实例 (new Vue) 的模板中。

局部注册
---------

全局注册往往是不够理想的。

局部注册则限定了组件只能在被注册的组件/ Vue 根实例中使用，而无法在其他组件/ Vue 根实例中使用。

.. code-block:: javascript

		var vm2 = new Vue({
			el: '#sign-up2',
			components: {
				'my-component': MyComponent
			}
		});

若使用如上代码注册组件，则说明该组件只能在 vm2 根实例中使用，在该实例之外使用该组件是使用不了该组件的。

实例
--------------


.. code-block:: html

	<body>
		<div id="sign-up">
			<p>sign up 1</p>
			<my-component></my-component>
		</div>
		<my-component></my-component>
		<div id="sign-up2">
			<p>sign up 2</p>
			<my-component></my-component>
			<my-parent>
				<my-child>被覆盖</my-child>
			</my-parent>
			<my-child>不在父组件内，无法转化</my-child>
		</div>
		<my-parent></my-parent>
	</body>

.. code-block:: javascript

		var MyComponent = Vue.extend({
			template: '<p>This is a component</p>'
		});
		Vue.component('my-component', MyComponent);
		var vm = new Vue({
			el: '#sign-up'
		});
		var my_child = Vue.extend({
			template: '<h3>局部注册，需要在父组件模板属性中使用</h3>'
		});
		var my_parent = Vue.extend({
			template: "<div><p>this is parent component</p><my-child></my-child></div>",
			components:{
				'my-child':my_child
			}
		});
		var vm2 = new Vue({
			el: '#sign-up2',
			components: {
				'my-parent': my_parent
			}
		});

.. image:: ../../img/vue/components/sign-in.png

注册简化--注册语法糖
---------------------

.. code-block:: javascript

   // 全局注册
   Vue.component('my-component', {
      template : '<p>This is a component</p>'
   })
   // 局部注册
   var Parent = Vue.extend({
      template: '<div> \
      　　　 <p>This is a parent component</p> \ 
      　　　 <my-child></my-child> \
      　　 </div>',
      components: {
      　　 'my-child': {
      　　　　template : '<p>This is a child component</p>'
      　　 }
      }
   });


.. 
   模块系统
   ====================


.. // todo : add module system record!!

组件的可复用性
=====================

**data 必须是一个函数**

.. code-block:: javascript

		Vue.component('button-counter', {
		  data: function () {
		    return {
		      count: 0
		    }
		  },
		  template: '<button v-on:click="count++">You clicked me {{ count }} times.</button>'
		})

通过代码我们可以发现，组件的 data 属性和我们之前直接的提供对象不同，是通过函数返回值的形式赋值的。这样做的好处是实现组件的可复用性，当一个 Vue 实例有多个组件实例的情况下，每个组件实例可以维护一份被返回对象的独立的拷贝。换而言之，即 Vue 实例本身不提供数据存储，只是为每个组件实例提供初始化数据，而每个组件得数据在其组件实例中各自存储。


prop 属性
============

命令与使用
------------

HTML 中的 attribute 名是大小写不敏感的，所以浏览器会把所有大写字符解释为小写字符。这意味着当你使用 DOM 中的模板时，camelCase (驼峰命名法) 的 prop 名需要使用其等价的 kebab-case (短横线分隔命名) 命名。


.. code-block:: html

	<!-- 在 HTML 中是 kebab-case 的 -->
	<blog-post post-title="hello!"></blog-post>

.. code-block:: javascript

	Vue.component('blog-post', {
	// 在 JavaScript 中是 camelCase 的
	props: ['postTitle'],
	template: '<h3>{{ postTitle }}</h3>'
	})

显式说明 props 的元素的类型
----------------------------

通过前一个例子我们知道，我们通常希望每个 prop 都有指定的值类型，比如上一个例子的 postTitle ，但是我们完全可以传入一个非 String 类型的对象；这个时候，如果我们在 props 中预先设定了目标类型，那么这不仅为你的组件提供了文档，还会在它们遇到错误的类型时从浏览器的 JavaScript 控制台提示用户。

.. code-block:: javascript

	props: {
	title: String,
	likes: Number,
	isPublished: Boolean,
	commentIds: Array,
	author: Object,
	callback: Function,
	contactsPromise: Promise // or any other constructor
	}

传递静态或动态 Prop
---------------------

.. code-block:: html

		<p>通过 Prop 向子组件传递数据</p>
		<div id="simple-example">
			<p>传递静态 prop</p>
			<my-example message="hello world!"></my-example>
		</div>
		<div id="simple-example2">
			<p>动态传递 prop</p>
			<my-example :message="message"></my-example>
			<input type="text" name="" id="" value="" v-model="message" />
		</div>

.. code-block:: javascript

		var MyExample = Vue.extend({
			props: {
				message: String,
			},
			template: '<p>{{message}}</p>'
		})
		var vm = new Vue({
			el: '#simple-example',
			components: {
				'my-example': MyExample
			}
		})
		var vm2 = new Vue({
			el: '#simple-example2',
			data: {
				message: "hello vue"
			},
			components: {
				'my-example': MyExample
			}
		})

.. image:: ../../img/vue/components/props.png
	:alt: props

.. note:: 

	使用不同对象来向子组件传递数据的具体方法大同小异，需要了解更多 `点击前往官网查看更多关于传递静态或动态 Prop <https://cn.vuejs.org/v2/guide/components-props.html#%E4%BC%A0%E9%80%92%E9%9D%99%E6%80%81%E6%88%96%E5%8A%A8%E6%80%81-Prop>`_ 



单向数据流
----------------

通过前面两例子，我们可以发现数据流向是从父组件到子组件的。

所有的 prop 都使得其父子 prop 之间形成了一个单向下行绑定：父级 prop 的更新会向下流动到子组件中，但是反过来则不行。这样会防止从子组件意外变更父级组件的状态，从而导致你的应用的数据流向难以理解。

额外的，每次父级组件发生变更时，子组件中所有的 prop 都将会刷新为最新的值。这意味着你不应该在一个子组件内部改变 prop。如果你这样做了，Vue 会在浏览器的控制台中发出警告。


.. warning:: 

	注意在 JavaScript 中对象和数组是通过引用传入的，所以对于一个数组或对象类型的 prop 来说，在子组件中改变变更这个对象或数组本身将会影响到父组件的状态。

