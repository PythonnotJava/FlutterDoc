# 工具类
> * LinearProgressIndicator：一个线性、条状的进度条。
> * CircularProgressIndicator：一个圆形进度条。
> * BoxDecoration：用于装饰Container等组件的类，可以让组件拥有背景颜色、渐变、圆角边框、阴影等效果。它提供了一些非常灵活的装饰属性，使你可以轻松地定制组件的外观。
> * InheritedWidget：用于在组件树中向子组件提供共享数据。当数据发生变化时，依赖于这些数据的子组件会自动更新。这种机制被称为“数据的跨组件共享”，尤其适用于跨越多个组件树节点的数据传递，如主题、用户会话、配置等。
> * InheritedProvider：用于在Flutter的widget树中共享和传递数据。它自动处理状态更新的通知和重建工作。
> * Provider：用于实现数据的依赖注入和状态管理。它基于 InheritedWidget，并通过简化的 API 提供了在 Flutter 中共享和管理数据的方式。

## LinearProgressIndicator类
### 默认构造函数
```text
LinearProgressIndicator({
    super.key,
    super.value,
    super.backgroundColor,
    super.color,
    super.valueColor,
    this.minHeight,
    super.semanticsLabel,
    super.semanticsValue,
    this.borderRadius = BorderRadius.zero,
})
```

### LinearProgressIndicator(...)参数解析
| 参数名称              | 使用类型                 | 参数介绍                                                           |
|-------------------|----------------------|----------------------------------------------------------------|
| key               | Key                  | 用于在 Flutter 的组件树中标识该组件，一般用于局部更新、优化等情况                          |
| value             | double               | 表示当前的进度值，范围是 0.0 到 1.0。null 表示不确定的进度（即动画的进度条会一直运动下去），否则会显示具体进度 |
| backgroundColor   | Color                | 进度条的背景颜色，即未填充的部分颜色                                             |
| color             | Color                | 进度条前景颜色，即已填充部分颜色                                               |
| valueColor        | Animation<Color>     | 进度条的颜色动画，可以用于在进度条的前景颜色上设置动画效果                                  |
| minHeight         | double               | 进度条的最小高度，默认为系统默认的进度条高度（一般较细）                                   |
| semanticsLabel    | String               | 用于屏幕阅读器的语义标签，帮助无障碍用户了解组件的用途或状态                                 |
| semanticsValue    | double               | 用于屏幕阅读器的语义值，帮助无障碍用户了解组件的当前进度值                                  |
| borderRadius      | BorderRadiusGeometry | 控制进度条的圆角半径                                                     |

## CircularProgressIndicator类
### 默认构造函数
```text
CircularProgressIndicator({
    super.key,
    super.value,
    super.backgroundColor,
    super.color,
    super.valueColor,
    this.strokeWidth = 4.0,
    this.strokeAlign = strokeAlignCenter,
    super.semanticsLabel,
    super.semanticsValue,
    this.strokeCap,
  })
```

### CircularProgressIndicator(...)参数解析
| 参数名称            | 使用类型             | 参数介绍                                                                 |
|-----------------|------------------|----------------------------------------------------------------------|
| key             | Key              | 用于标识组件的唯一值，主要用于在组件树中查找和控制特定组件实例                                      |
| value           | double           | 进度指示的值                                                               |
| backgroundColor | Color            | 指定进度条背景圆环的颜色，即未完成部分的颜色                                               |
| color           | Color            | 前景色，表示已完成的进度部分的颜色                                                    |
| valueColor      | Animation<Color> | 前景颜色的动画对象，可以设置为 AlwaysStoppedAnimation<Color> 来指定静态颜色，也可以通过动画效果让颜色渐变 |
| strokeWidth     | double           | 指定圆环的宽度                                                              |
| strokeAlign     | double           | 圆环的对齐方式                                                              |
| semanticsLabel  | String           | 无障碍支持的标签，用于描述当前的进度条，通常用于屏幕阅读器读取内容，以帮助视障用户了解组件的作用                     |
| semanticsValue  | String           | 无障碍支持的数值描述，主要用于说明当前进度的数值，以百分比或具体进度形式呈现，供辅助技术使用                       |
| strokeCap       | StrokeCap        | 指定圆环端部的样式                                                            |

### 根据当前平台（如 iOS 或 Android）自动调整圆形进度指示器的外观
```text
CircularProgressIndicator.adaptive({
    super.key,
    super.value,
    super.backgroundColor,
    super.valueColor,
    this.strokeWidth = 4.0,
    super.semanticsLabel,
    super.semanticsValue,
    this.strokeCap,
    this.strokeAlign = strokeAlignCenter,
  })
```

### CircularProgressIndicator.adaptive(...)参数解析
| 参数名称            | 使用类型             | 参数介绍                                                |
|-----------------|------------------|-----------------------------------------------------|
| key             | Key              | 用于标识组件的唯一值，主要用于在组件树中查找和控制特定组件实例                     |
| value           | double           | 进度指示的值                                              |
| backgroundColor | Color            | 指定进度条背景圆环的颜色，即未完成部分的颜色                              |
| valueColor      | Animation<Color> | 前景颜色的动画对象                                           |
| strokeWidth     | double           | 指定圆环的宽度                                             |
| semanticsLabel  | String           | 无障碍支持的标签，用于描述当前的进度条，便于屏幕阅读器等辅助技术理解组件的功能             |
| semanticsValue  | String           | 无障碍支持的数值描述，主要用于说明当前进度的数值，帮助辅助技术提供更好的用户体验            |
| strokeCap       | StrokeCap        | 指定圆环端部的样式                                           |

## BoxDecoration类
### 默认构造函数
```text
BoxDecoration({
    this.color,
    this.image,
    this.border,
    this.borderRadius,
    this.boxShadow,
    this.gradient,
    this.backgroundBlendMode,
    this.shape = BoxShape.rectangle,
  })
```

### BoxDecoration参数解析
| 参数名称                | 使用类型                 | 参数介绍                                |
|---------------------|----------------------|-------------------------------------|
| color               | Color                | 用于设置背景颜色，接受一个 Color 对象，如 Colors.red |
| image               | DecorationImage      | 设置背景图片                              |
| border              | BoxBorder            | 定义边框，可以设置边框的颜色、宽度和样式                |
| borderRadius        | BorderRadiusGeometry | 用于设置圆角边框                            |
| boxShadow           | List<BoxShadow>      | 设置阴影效果                              |
| gradient            | Gradient             | 设置渐变效果                              |
| backgroundBlendMode | BlendMode            | 设置背景的混合模式                           |
| shape               | BoxShape             | 用于设置组件的形状                           |

## InheritedWidget类
### 默认构造函数
```text
InheritedWidget({ 
    super.key, 
    required super.child
})
```

### InheritedWidget(...)参数解析
| 参数名称   | 使用类型    | 参数介绍                        |
|--------|---------|-----------------------------|
| key    | Key     | 用于唯一标识这个 InheritedWidget 实例 |
| child  | Widget  | 表示 InheritedWidget 的子组件     |

> 注：InheritedWidget是一个抽象类，需要被子类继承且必须实现updateShouldNotify方法；InheritedWidget 的 updateShouldNotify 方法每次返回 true 时，它的依赖者（即子类） 会调用 didChangeDependencies 方法。

## InheritedProvider类
### 默认构造函数
```text
InheritedProvider({
    Key? key,
    Create<T>? create,
    T Function(BuildContext context, T? value)? update,
    UpdateShouldNotify<T>? updateShouldNotify,
    void Function(T value)? debugCheckInvalidValueType,
    StartListening<T>? startListening,
    Dispose<T>? dispose,
    this.builder,
    bool? lazy,
    Widget? child,
  })
```

### InheritedProvider(...)参数解析
| 参数名称                       | 使用类型            | 参数介绍                                                                                                         |
|----------------------------|-----------------|--------------------------------------------------------------------------------------------------------------|
| key                        | Key             | 用于为 InheritedProvider 提供一个唯一标识符                                                                              |
| create                     | T Function      | 一个回调函数，返回要提供给 widget 树的对象（T）                                                                                 |
| update                     | T Function      | 一个回调函数，接收当前的数据对象 T 和 value（之前的数据值），用于在 InheritedProvider 更新时提供更新逻辑                                           |
| updateShouldNotify         | bool Function   | 一个回调函数，接受一个 oldWidget 参数，返回一个布尔值（true 或 false），表示是否通知依赖该数据的 widget 进行重建                                      |
| debugCheckInvalidValueType | void Function   | 一个调试回调函数，用于检查提供给 InheritedProvider 的值类型是否有效                                                                  |
| startListening             | void Function   | 一个回调函数，用于指示 InheritedProvider 何时开始监听数据变化                                                                     |
| dispose                    | void Function   | 一个回调函数，用于在 InheritedProvider 不再需要时清理资源。通常在对象生命周期结束时调用，用于避免内存泄漏                                               |
| builder                    | Widget Function | 一个回调函数，返回一个 Widget。它在 InheritedProvider 内部访问数据并将其传递给子树的 widget。使用 builder 可以解耦数据和 UI                         |
| lazy                       | bool            | 一个布尔值，默认值为 true。如果为 true，则 InheritedProvider 会延迟创建数据对象，直到第一次访问时才会创建。如果为 false，数据会在 InheritedProvider 创建时立即生成 |
| child                      | Widget          | 传递给 InheritedProvider 的子 widget，通常是依赖 InheritedProvider 提供的数据的组件                                             |

### 用于将一个现成的数据（即 value）提供给widget树
```text
 InheritedProvider.value({
    Key? key,
    required T value,
    UpdateShouldNotify<T>? updateShouldNotify,
    StartListening<T>? startListening,
    bool? lazy,
    this.builder,
    Widget? child,
  }) 
```

### InheritedProvider.value(...)参数解析
| 参数名称               | 使用类型             | 参数介绍                                                                                                         |
|--------------------|------------------|--------------------------------------------------------------------------------------------------------------|
| key                | Key              | 用于为 InheritedProvider 提供一个唯一标识符                                                                              |
| value              | T                | 必须提供的参数，表示你要提供给 widget 树的数据对象                                                                                |
| updateShouldNotify | bool Function    | 一个回调函数，接受一个 oldWidget 参数，返回一个布尔值（true 或 false），表示是否通知依赖该数据的 widget 进行重建                                      |
| startListening     | void Function    | 一个回调函数，用于指示 InheritedProvider 何时开始监听数据变化                                                                     |
| builder            | Widget Function  | 一个回调函数，返回一个 Widget。它在 InheritedProvider 内部访问数据并将其传递给子树的 widget。使用 builder 可以解耦数据和 UI                         |
| lazy               | bool             | 一个布尔值，默认值为 true。如果为 true，则 InheritedProvider 会延迟创建数据对象，直到第一次访问时才会创建。如果为 false，数据会在 InheritedProvider 创建时立即生成 |
| child              | Widget           |  传递给 InheritedProvider 的子 widget，通常是依赖 InheritedProvider 提供的数据的组件                                            |

## Provider类
### 默认构造函数
```text
Provider({
    Key? key,
    required Create<T> create,
    Dispose<T>? dispose,
    bool? lazy,
    TransitionBuilder? builder,
    Widget? child,
  })
```

### Provider类(...)参数解析
| 参数名称    | 使用类型             | 参数介绍                                                               |
|---------|------------------|--------------------------------------------------------------------|
| key     | Key              | 用于为Provider类提供一个唯一标识符                                              |
| create  | T Function       | 必需的参数，create 是一个回调函数，负责创建并返回一个你想要提供给 widget 树的对象                   |
| dispose | void Function    | 在 Provider 被销毁时调用。它用于清理资源，比如关闭流、取消订阅或释放内存等                         |
| lazy    | bool             | 表示是否延迟创建提供的数据。                                                     |
| builder | Widget Function  |      回调函数，用来动态构建 widget 树                                          |
| child   | Widget           | 这是 Provider 的子 widget，通常是你应用的根 widget。child 会作为 Provider 提供的对象的消费者 |

### 用于提供已经存在的数据（value）给widget树
```text
Provider.value({
  Key? key,
  required T value,
  UpdateShouldNotify<T>? updateShouldNotify,
  TransitionBuilder? builder,
  Widget? child,
})

```

### Provider.value参数解析
| 参数名称               | 使用类型            | 参数介绍                                                                                                   |
|--------------------|-----------------|--------------------------------------------------------------------------------------------------------|
| key                | Key             | 用于为Provider类提供一个唯一标识符                                                                                  |
| value              | T               | 表示你想要提供给 widget 树的现有数据对象                                                                               |
| updateShouldNotify | bool Function   | 可选的回调函数，接受旧的 Provider 和当前的 Provider，返回一个布尔值。如果返回 true，表示数据发生了变化，依赖该数据的 widget 会被通知重建；如果返回 false，则不通知更新 |
| builder            | Widget Function | 回调函数，用来动态构建 widget 树                                                                                   |
| child              | Widget          | 这是 Provider 的子 widget，通常是你应用的根 widget。child 会作为 Provider 提供的对象的消费者                                     |

