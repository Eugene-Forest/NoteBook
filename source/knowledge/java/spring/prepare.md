# 序

**Spring有两个核心特性，也就是依赖注入（dependency injection，DI）和面向切面编程（aspect-oriented programming，AOP）**

关键词：
: - DI ：依赖注入
  - AOP ： 面向切面编程

在诞生之初，创建Spring的主要目的是用来替代更加重量级的企业级Java技术，尤其是EJB。

Spring用bean或者JavaBean来表示应用组件。一个Spring组件可以是任何形式的POJO [^id5]。

创建应用组件之间协作的行为通常称为装配（wiring）; DI 主要体现在装配过程中。

Spring最根本的使命：简化Java开发。

为了降低Java开发的复杂性，Spring采取了以下4种关键策略：

- 基于POJO的轻量级和最小侵入性编程；
- 通过依赖注入和面向接口实现松耦合 [^id6]；--装配
- 基于切面和惯例进行声明式编程；
- 通过切面和模板减少样板式代码。

:::{note}

依赖注入（DI）以及切面编程（AOP）的都可以减小耦合度。

DI 是组装应用对象的一种方式，借助这种方式对象无需知道依赖来自何处或者依赖的实现方式。不同于自己获取依赖对象，对象会在运行期赋予它们所依赖的对象。依赖对象通常会通过接口了解所注入的对象，这样的话就能确保低耦合。

AOP 可以帮助应用将散落在各处的逻辑汇集于一处————切面（即将逻辑集中在配置文件的一种行为）。当Spring装配bean的时候，这些切面能够在运行期编织起来，这样就能非常有效地赋予bean新的行为。
:::

## Containing your beans

在基于 Spring 的应用中，应用对象生存于 Spring 容器（container）中。Spring 容器负责创建对象，装配它们，配置并管理它们的整个生命周期。不难看出，容器是Spring框架的核心。

Spring 容器使用 DI 管理构成应用的组件，它会创建相互协作的组件之间的关联。毫无疑问，这些对象更简单干净，更易于理解，更易于重用并且更易于进行单元测试。

Spring 容器不止一个，Spring 自带的容器实现可以归为两种：

- bean 工厂 ：（由org.springframework.beans.factory.eanFactory接口定义）是最简单的容器，提供基本的 DI 支持
- 应用上下文 ：（由org.springframework.context.ApplicationContext接口定义）基于BeanFactory构建，并提供应用框架级别的服务

虽然我们可以在bean工厂和应用上下文之间任选一种，但bean工厂对大多数应用来说往往太低级了，因此，应用上下文要比bean工厂更受欢迎。

### 使用应用上下文

较常用的应用上下文：

- AnnotationConfigApplicationContext：从一个或多个基于Java的配置类中加载Spring应用上下文。
- AnnotationConfigWebApplicationContext：从一个或多个基于Java的配置类中加载Spring Web应用上下文。
- ClassPathXmlApplicationContext：从类路径下的一个或多个XML配置文件中加载上下文定义，把应用上下文的定义文件作为类资源。
- FileSystemXmlApplicationContext：从文件系统下的一个或多个XML配置文件中加载上下文定义。
- XmlWebApplicationContext：从Web应用下的一个或多个XML配置文件中加载上下文定义。

以 ClassPathXmlApplicationContext 为例：

```java
//从项目资源文件中加载应用上下文
ClassPathXmlApplicationContext context =
   new ClassPathXmlApplicationContext("META-INF/spring/minstrel.xml");
Knight knight = context.getBean(Knight.class);
context.close();
```

### Spring 中的 bean 的生命周期

% //todo Spring 中的 bean 的生命周期
 
[^id5]: {ref}`查看POJO笔记 <POJO>`

[^id6]: {ref}`点击查看耦合笔记 <coupling>`
