# 装配 bean

在Spring中，对象无需自己查找或创建与其所关联的其他对象。相反，容器会负责把需要相互协作的 **对象引用** 赋予各个对象。

创建应用对象之间协作关系的行为通常称为装配（wiring），这也是依赖注入（DI）的本质。

Spring 容器负责创建应用程序中的 bean 并通过 DI 来协调这些对象之间的关系。但是，作为开发人员，你需要告诉 Spring 要创建哪些 bean 并且如何将其装配在一起。

## 三种主要的装配机制

Spring 提供了三种主要的装配机制：

- 隐式的bean发现机制和自动装配。
- 在Java中进行显式配置。
- 在XML中进行显式配置。

:::{tip}
建议是尽可能地使用自动配置的机制。显式配置越少越好。当你必须要显式配置bean的时候（比如，有些源码不是由你来维护的，而当你需要为这些代码配置bean的时候），推荐使用类型安全并且比XML更加强大的JavaConfig。最后，只有当你想要使用便利的XML命名空间，并且在JavaConfig中没有同样的实现时，才应该使用XML。
:::

## 自动化装配

Spring 从两个方面来实现自动化装配：

- 组件扫描（component scanning） ： Spring 会自动发现应用上下文中所创建的 bean 。
- 自动装配（auto wiring） ： Spring 自动满足 bean 之间的依赖。

### 创建可被发现的 bean 并开启组件扫描———— @Component

具体实现方法：创建可被发现的 bean。
对一个实现类添加 @Component 注解来标识该类会作为组件类，并在所在包被扫描时告知 Spring 要为这类创建 bean。

```{literalinclude} ../example_java/spring/CDPlayer.java
:emphasize-lines: 6
:language: java
:linenos: true
```

:::{note}

Spring 应用上下文中所有的 bean 都会给定一个 ID。对于没有直接设定命名的组件，Spring 可能根据全限定类名来进行命名 （对于上文代码的soundsystem.CDPlayer类，其 ID 可能为 soundsystem.CDPlayer#0）。当然可以直接通过注解来命名如 `@Component("cdPlayer")`。
:::

:::{tip}
**Spring支持将 @Named 作为 @Component 注解的替代方案。** 这种方式不使用@Component 注解，而是使用Java依赖注入规范（Java Dependency Injection）中所提供的 @Named 注解来为 bean 设置ID：`@Named("cdPlayer")`。
:::

不过，**组件扫描默认是不启用的**，所以我们需要显式地配置 Spring 从而命令它去寻找带有 @Component 注解的类并为其创建 bean。

#### JavaConfig 形式开启自动扫描的配置

```java
package soundsystem;
import org.springframework.context.annotation.ComponentScan;
import org.springframework.context.annotation.Configuration;

@Configuration
@ComponentScan
public class CDPlayerConfig {
}
```

如果没有其他配置的话，@ComponentScan 默认会扫描与配置类所在的包。
Spring 将会扫描这个包以及这个包下的所有子包，查找带有 @Component 注解的类。

设置组件扫描的基础包按照默认规则，它会以配置类所在的包作为基础包（base package）来扫描组件。但是，如果你想扫描不同的包，那该怎么办呢？或者，如果你想扫描多个基础包，那又该怎么办呢？

以示例代码为例，可将注解改为以下形式：

- `@ComponentScan("soundsystem")`
- `@ComponentScan(basePackages="soundsystem")`
- `@ComponentScan(basePackages={"soundsystem","otherpackage"})`
- `@ComponentScan(basePackageClasses={CDPlayer.class,OtherPlayer.class})`

从安全性来看，最后一种注解方式是比较安全的。如果使用这种注解方式，那么要避免该类涉及实际业务代码并保证其不会被重构移除，以作为组件扫描的基础包类。【你可以考虑在包中创建一个用来进行扫描的空标记接口（marker interface）。通过标记接口的方式，你依然能够保持对重构友好的接口引用，但是可以避免引用任何实际的应用程序代码。】

对于前三种方式，缺点在于所设置的基础包是以String类型表示的，这种方法是类型不安全（not type-safe）的。

#### XML 形式开启自动扫描的配置

```xml
<?xml version="1.0" encoding="UTF-8"?>
<beans xmlns="http://www.springframework.org/schema/beans"
xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
xmlns:context="http://www.springframework.org/schema/context"
xmlns:c="http://www.springframework.org/schema/c"
xmlns:p="http://www.springframework.org/schema/p"
xsi:schemaLocation="http://www.springframework.org/schema/beans http://www.springframework.org/schema/beans/spring-beans.xsd
      http://www.springframework.org/schema/context http://www.springframework.org/schema/context/spring-context.xsd">

<context:component-scan base-package="soundsystem" />

</beans>
```

### 通过对bean添加注解实现自动装配———— @Autowired

为了声明要进行自动装配，我们可以借助Spring的 @Autowired 注解。

**不管是构造器、Setter方法还是其他类的方法，Spring 都会尝试满足方法参数上所声明的依赖。**

假如有且只有一个 bean 匹配依赖需求的话，那么这个 bean 将会被装配进来。

如果没有匹配的 bean，那么在应用上下文创建的时候，Spring 会抛出一个异常。（可以设置注解的 required 属性为 false 【`@Autowired(required=false)`】来避免出现没有匹配的 bean 的时候的异常，但是这样设置需要在代码中检查传入的 参数/bean 是否为 null）。

如果有多个 bean 都能满足依赖关系的话，Spring 将会抛出一个异常，表明没有明确指定要选择哪个 bean 进行自动装配。（自动装配的歧义性）

% //todo : 添加第三章的 自动装配的歧义性

```{literalinclude} ../example_java/spring/CDPlayer.java
:emphasize-lines: 10
:language: java
:linenos: true
```

:::{note}

在自动装配中，Spring 同时支持 @Inject 和 @Autowired 。@Inject 注解来源于 Java 依赖注入规范。尽管 @Inject 和 @Autowired 之间有着一些细微的差别，但是在大多数场景下，它们都是可以互相替换的。 @Named 与 @Component 之间的关系也与它们一样。
:::

### JavaConfig 装配

尽管在很多场景下通过组件扫描和自动装配实现Spring的自动化配置是更为推荐的方式，但有时候自动化配置的方案行不通，因此需要明确配置 Spring。比如说，你想要将第三方库中的组件装配到你的应用中，在这种情况下，是没有办法在它的类上添加 @Component 和 @Autowired 注解的，因此就不能使用自动化装配的方案了。

**创建 JavaConfig 类的关键在于为其添加 @Configuration 注解，@Configuration 注解表明这个类是一个配置类，该类应该包含在 Spring 应用上下文中如何创建 bean 的细节，以及装配 bean 。**

```{literalinclude} ../example_java/spring/CDPlayerConfig.java
:emphasize-lines: 6,9,14,17
:language: java
:linenos: true
```

:::{note}

JavaConfig 的装配方法可以使得所有的装配逻辑都集中在一个配置类中（虽然大多数时候不可能），简化了 bean 的复杂度（比如可以不用写 @Autowired 注解）。
:::

#### 创建/声明 bean

要在 JavaConfig 中声明 bean ，我们需要编写一个方法，这个方法会创建所需类型的实例，然后给这个方法添加 @Bean 注解。@Bean 注解会告诉 Spring 这个方法将会返回一个对象，该对象要注册为 Spring 应用上下文中的 bean。方法体中包含了最终产生 bean 实例的逻辑。

```{literalinclude} ../example_java/spring/CDPlayerConfig.java
:lines: 9-12
```

默认情况下，bean 的 ID 与带有 @Bean 注解的方法名是一样的。在本例中，bean 的名字将会是compactDisc。如果你想为其设置成一个不同的名字的话，那么可以重命名该方法，也可以通过 name 属性指定: `@Bean(name="CD")`。

#### bean 的依赖注入

在 JavaConfig 中装配 bean 的最简单方式就是引用创建 bean 的方法。这个方法要求被注入的 bean 在配置文件中有定义出来。

```java
@Bean
public CDPlayer cdPlayer() {
   // 实现了依赖注入
   return new CDPlayer(compactDisc()); //way 2
}
```

看起来，CompactDisc 是通过调用 sgtPeppers() 得到的，但情况并非完全如此。因为 sgtPeppers() 方法上添加了 @Bean 注解，Spring 将会拦截所有对它的调用，并确保直接返回该方法所创建的 bean，而不是每次都对其进行实际的调用。

假设配置文件为如下代码所示，那么运行测试程序时会发现，控制台会依次打印出三个方法里面的字符串（只打印出3个字符串，说明只创建出3个 bean）。

```java
@Configuration
public class CDPlayerConfig {

@Bean
public CompactDisc compactDisc() {
   System.out.println("cd bean");
   return new SgtPeppers();
}

@Bean
public CDPlayer cdPlayer(CompactDisc compactDisc) {
   System.out.println("cd player");
   return new CDPlayer(compactDisc());
}

@Bean
public CDPlayer otherCDPlayer(CompactDisc compactDisc){
   System.out.println("other cd player");
   return new CDPlayer(compactDisc());}
}
```

```{literalinclude} ../example_java/spring/CDPlayerConfig.java
:lines: 14-18
```

**通过向方法中传入参数来引用其他的 bean 通常是最佳的选择，因为它不会要求将 CompactDisc 声明到同一个配置类之中。在这里甚至没有要求 CompactDisc 必须要在 JavaConfig 中声明，实际上它可以通过组件扫描功能自动发现或者通过 XML 来进行配置。**

### XML 装配

声明一个 bean 的方法：

- `<bean class="soundsystem.CDPlayer" />`; 声明一个 bean, 其命名由全限定的类名构成；如这段代码创建的 bean 的 ID 可能为："soundsystem.CDPlayer#0"。"#0"是一个计数，用来区分其他相同类的 bean。
- `<bean id="cdPlayer" class="soundsystem.CDPlayer" />`;这段代码创建的 bean 的 ID 为"cdPlayer"。

这里声明了一个很简单的bean，创建这个 bean 的类通过 class 属性来指定的，并且要使用 **全限定的类名**。

使用 XML 配置需要注意以下两点：

> 在 XML 配置中，bean 的创建显得更加被动，它不需要主动的创建 bean 实例；不过，它并没有 JavaConfig 那样强大，在 JavaConfig 配置方式中，你可以通过任何可以想象到的方法来创建 bean 实例。
>
> 在这个简单的\<bean>声明中，我们将 bean 的类型以字符串的形式设置在了 class 属性中。谁能保证设置给 class 属性的值是真正的类呢？Spring 的 XML 配置并不能从编译期的类型检查中受益。

#### xml 通过构造器对 bean 实现依赖注入

```{literalinclude} ../example_java/spring/CDPlayer.java
:lines: 7-19
```

以下两段代码功能相同：

```{literalinclude} ../example_java/spring/CDPlayerConfig.java
:lines: 9-18
```

```XML
<bean id="compactDisc" class="soundsystem.SgtPeppers" />

<bean id="cdPlayer" class="soundsystem.CDPlayer">
   <constructor-arg ref="compactDisc" />
<bean>
```

当 Spring 遇到这个 \<bean> 元素时，它会创建一个CDPlayer 实例。\<constructor-arg> 元素会告知Spring 要将一个 ID 为 compactDisc 的 bean 引用传递到 CDPlayer 的构造器中。

#### xml 通过属性方法（setter方法）对 bean 实现依赖注入

在 xml 配置中，构造器注入于属性方法注入（setter方法注入）是一样的。这两种方法可以相互调换。

为上文中 CDPlayer 类添加 cd 属性的 setter 方法后，使用下方代码也可正常运行：

```XML
<bean id="compactDisc" class="soundsystem.SgtPeppers" />

<bean id="cdPlayer" class="soundsystem.CDPlayer">
   <property name="cd" ref="compactDisc"></property>
</bean>
```

property 标签中的 name 对应的是所在 bean 的字段名，ref 对应的是被注入的 bean 的 ID。

:::{note}

在此不对 xml 配置做更加详细的说明；
:::

% 查看更多前往 spring xml 配置详解。

% //todo : 添加 spring xml 配置详解

## 混合装配

不管使用 JavaConfig 还是使用 XML 进行装配，我通常都会创建一个 **根配置（root configuration）**，这个配置会将两个或更多的装配类或 XML 文件组合起来。

### JavaConfig 配置导入 其他配置文件

```java
@Configuration
@Import(CDPlayerConfig.class)
@ImportResource("classpath:cd-config.xml")
public class SoundSystemConfig {

}
```

通过 @Import 注解可以导入其他的 JavaConfig 文件；导入多个文件的方法类如： `@Import({CDConfig.class,CDPlayerConfig.class})`

通过 @ImportResource 注解可以导入其他的 XML 配置文件；导入多个文件的方法类如：`@ImportResource({"classpath:cd-config.xml","classpath:cdPlayer-config.xml"})`

这两种导入方法可以混合使用。

```{image} ../../../img/spring/MixJavaConfig.png
:alt: MixJavaConfig
```

### xml 配置导入 其他配置文件

有导入两种方法：

- 对于 JavaConfig : `<bean class="soundsystem.CDConfig" />`
- 对于 XML 文件 ： `<import resource="cdplayer-config.xml"></import>`
