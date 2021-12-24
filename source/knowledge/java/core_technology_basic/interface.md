# 接口

接口（ interface) 技术， 这种技术主要用来描述类具有什么功能，而并不给出每个功能的具体实现。一个类可以实现（ implement ) 一个或多个接口，并在需要接口的地方， 随时使用实现了相应接口的对象。

(interfacem)=

## 接口(interface)

- 接口中的所有方法自动地属于 `public`。 因此，在接口中声明方法时，不必提供关键字 `public`。不过，在实现接口时， 必须把方法声明为 `public` 。
- 接口绝不能含有实例域 [^id10]，提供实例域和方法实现的任务应该由实现接口的那个类来完成。
- 接口可以定义常量，与接口中的方法都自动地被设置为 `public` 一样，接口中的域将被自动设为 `public static final`。 [^id11]
- 在 Java SE 8 之前， 也不能在接口中实现方法，但是现在已经可以在接口中提供简单方法了， 当然， 这些方法不能引用实例域—— *接口没有实例* 。
- 如同使用 `instanceof` 检查一个对象是否属于某个特定类一样， 也可以使用 `instanceof` 检查一个对象是否实现了某个特定的接口
- 有些接口只定义了常量， 而没有定义方法。然而，这样应用接口似乎有点偏离了接口概念的初衷， 最好不要这样使用它。【使用类】
- 实现类实现多个接口 `class Employee implements Cloneable, Comparable` ；这也是为什么设计接口的原因之一，因为如果实现类仅仅能实现一个接口的话，那么实现类直接继承实现 {ref}`抽象类 <abstract-class>`  [^id12] 即可。

### 静态方法

- 在 Java SE 8 中，允许在接口中增加静态方法，只是这有违于将接口作为抽象规范的初衷。目前为止， 通常的做法都是将静态方法放在伴随类中。

  - 在标准库中， 你会看到成对出现的接口和实用工具类， 如 Collection/Collections 或 Path/Paths。但是通过接口的静态方法可以直接获取 Path 而不用使用伴随类的静态方法，这样一来就不需要额外定义和使用 Paths [^id13] 类了。所以我们在实现自己的接口时，不再需要为实用工具方法另外提供一个伴随类。

### 方法的默认实现

- 可以为接口方法提供一个默认实现。 必须用 `default` 修饰符标记这样一个方法。当然， 这并没有太大用处， 因为接口的每一个实际实现都要覆盖这个方法。

  - 默认方法的一个重要用法是“接口演化” (interface evolution) [^id14]。
  - 还有一种情况就是当一个接口可以被实现的方法有很多，但是我们只需要用到/实现其中的一两个方法时，我们可以使用默认方法；例如 `MouseListener` 鼠标监听器有5个方法，但是我们只需要关心其中的 1、2 个事件类型。在 Java SE 8 中， 可以把所有方法声明为默认方法， 这些默认方法什么也不做。

- 如果先在一个接口中将一个方法定义为默认方法， 然后又在超类或另一个接口中定义了同样的方法时：

  - 超类优先。如果超类提供了一个具体方法，同名而且有相同参数类型的默认方法会被忽略
  - 接口冲突。 如果一个超接口提供了一个默认方法，另一个接口提供了一个同名而且参数类型（不论是否是默认参数）相同的方法， 必须覆盖这个方法来解决冲突。

:::{note}

“ 类优先” 规则可以确保与 Java SE 7 的兼容性。如果为一个接口增加默认方法，这对于有这个默认方法之前能正常工作的代码不会有任何影响。
:::

## 接口回调

回调（ callback) 是一种常见的程序设计模式。在这种模式中，可以指出某个特定事件发生时应该采取的动作。例如，可以指出在按下鼠标或选择某个菜单项时应该采取什么行动。

```{code-block} java
:caption: "回调示例"

public class RunMain {
    public static void main(String[] args) {
        Thread thread=new Thread(new RunTestThread());
        thread.start();
    }
}

class RunTestThread implements Runnable{

    @Override
    public void run() {
        Logger.getGlobal().info("This is a function called run");
    }
}
```

## Comparator 接口

**Arrays.sort** 数组对象比较问题

1. 对一个实现了 Comparable 接口的类的对象数组排序，可以直接通过此类的 compareTo 方法来比较并排序。
2. 有一个数组和一个比较器 ( comparator ) 作为参数；而比较器是实现了 Comparator 接口的类的实例，其可以实现自定义的比较方法。

```{code-block} java
:caption: "Comparator 接口实现比较"

public class StringLengthComparator implements Comparator<String> {
    @Override
    public int compare(String o1, String o2) {
        return o1.length()-o2.length();
    }

    public static void main(String[] args) {
      String message1="eugene";
      String message2="forest";
      StringLengthComparator stringLengthComparator=new StringLengthComparator();
      if (stringLengthComparator.compare(message1,message2)>0){
          Logger.getGlobal().info(message1+" > "+message2);
      }else if(stringLengthComparator.compare(message1,message2)==0){
          Logger.getGlobal().info(message1+" = "+message2);
      }else {
          Logger.getGlobal().info(message1+" < "+message2);
      }
  }
}
```
 
[^id10]: 实例域对应的英文应该是 `Object field`， 也就是我们常说的对象域，或者说是类对象的字段、类对象的属性。

[^id11]: 有人会疑惑，前面不是说接口不能有实例域吗？那么我们就需要明白类域和对象域之间的区别：当类没有实例化时，不存在对象域，但是却存在类域；所有该类的实例化对象都共享一个类域，而其对象域是相互独立的。而被 `static` 声明的常量就属于类域。

[^id12]: 使用抽象类表示通用属性存在这样一个问题： 每个类只能扩展于一个类。

[^id13]: 通过查看 JDK 1.8 的文档我们可以知道，Paths 类中只有两个静态方法分别为 `public static Path get(String first,String... more)` 和 `public static Path get(URI uri)` 。在 JavaAPI 中，你会看到很多接口都有相应的伴随类，这个伴随类中实现了相应接口的部分或所有方法，如 Collection/AbstractCollection 或 MouseListener/MouseAdapter 在 JavaSE 8 中， 这个技术已经过时。现在可以直接在接口中实现方法。

[^id14]: 假设很久以前你提供了这样一个类 `Big` ，并用该类实现了一个接口 `Collection` 。后来，又为这个接口增加了一个 stream 方法；如果这个方法不是默认方法，那么，如果不实现这个方法那么一定无法通过编译或调用。而是用默认方法可以有效避免这种情况，只需要直接添加方法而不需要为所有实现了该接口的实现类实现该方法。
