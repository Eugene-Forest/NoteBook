====================
序
====================

**Spring有两个核心特性，也就是依赖注入（dependency injection，DI）和面向切面编程（aspect-oriented programming，AOP）**

.. note:: 

   关键词： 
   
   * DI ：依赖注入
   * AOP ： 面向切面编程

在诞生之初，创建Spring的主要目的是用来替代更加重量级的企业级Java技术，尤其是EJB。

Spring用bean或者JavaBean来表示应用组件。一个Spring组件可以是任何形式的POJO。 :ref:`查看 <POJO>` 

Spring最根本的使命：简化Java开发。

为了降低Java开发的复杂性，Spring采取了以下4种关键策略：

* 基于POJO的轻量级和最小侵入性编程；
* 通过依赖注入和面向接口实现松耦合；
* 基于切面和惯例进行声明式编程；
* 通过切面和模板减少样板式代码。