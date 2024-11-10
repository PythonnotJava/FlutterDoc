# 管理器
> * FutureBuilder：用于处理异步操作的常用组件。它允许你根据异步操作（例如网络请求、文件读取等）的状态来动态构建 UI。
> * StreamBuilder：用于处理持续数据流（Stream）的小部件。它依赖于 Stream 对象，并根据 Stream 的数据流动态构建 UI。Stream 表示的是持续产生数据的序列，通常用于实时数据更新、事件监听等场景。
> * ValueListenableBuilder：用于监听和响应值发生变化的小部件，通常用于监听 ValueNotifier 或其他实现了 ValueListenable 接口的对象的变化。与 FutureBuilder 和 StreamBuilder 不同，它并不处理异步操作的结果或数据流的更新。
> * FocusNode：用于管理焦点的类。
> * LayoutBuilder：一个响应父容器布局约束的构建器小部件，它允许根据父级的尺寸动态调整子小部件的布局。它特别适合用于自适应布局场景，确保 UI 在不同屏幕尺寸下都能合理显示。
> * ScrollController：用于控制滚动视图的一个类。它允许你在代码中管理滚动位置、监听滚动事件等。
> * RawScrollbar：滚动条小部件，它允许你自定义滚动条的样式和行为。
> * PopScope：用于拦截页面的“返回”操作。

## FutureBuilder类
### 默认构造函数
```text
FutureBuilder({
    super.key,
    this.initialData,
    required super.stream,
    required this.builder,
  })
```

### FutureBuilder(...)参数解析
| 参数名称        | 使用类型   | 参数介绍                                                        |
|-------------|--------|-------------------------------------------------------------|
| key         | Key    | 用于标识 FutureBuilder 的身份                                      |
| future      | Future | 这是一个必需的参数，表示一个 Future 对象，FutureBuilder 会监听这个 Future 对象的状态变化 |
| initialData | T      | 这是未来完成之前的初始数据，如果提供了初始数据，将会用它来构建用户界面                         |
| builder     | Widget | 这是一个必需的回调函数，用于构建基于 Future 返回的数据的 Widget 树                   |

## StreamBuilder类
### 默认构造函数
```text
StreamBuilder({
    super.key,
    this.initialData,
    required super.stream,
    required this.builder,
  })
```

### StreamBuilder(...)参数解析
| 参数名称        | 使用类型   | 参数介绍                                                 |
|-------------|--------|------------------------------------------------------|
| key         | Key    | 用于标识 StreamBuilder 的身份                               |
| initialData | T      | 这是流的初始数据，当流还没有发出任何数据时会使用这个初始数据                       |
| stream      | Stream | 这是 StreamBuilder 必须的参数，用于传入一个 Stream 对象，它会监听这个流的数据变化 |
| builder     | Widget | 这是一个必需的回调函数，用于构建基于流数据的 Widget 树                      |

## ValueListenableBuilder类
### 默认构造函数
```text
ValueListenableBuilder({
    super.key,
    required this.valueListenable,
    required this.builder,
    this.child,
  })
```

### ValueListenableBuilder(...)参数解析
| 参数名称            | 使用类型            | 参数介绍                                                                    |
|-----------------|-----------------|-------------------------------------------------------------------------|
| key             | Key             | 用于标识 ValueListenableBuilder 的身份                                         |
| valueListenable | ValueListenable | 这是一个必需的参数，表示一个 ValueListenable 对象，ValueListenableBuilder 会监听这个可监听对象的值变化 |
| builder         | Widget          | 这是一个必需的回调函数，用于构建基于可监听对象的值的 Widget 树                                     |
| child           | Widget          | 这是一个可选的参数，用于在构建函数中传入一个固定的子组件，通常用于性能优化                                   |

## FocusNode类
### 默认构造函数
```text
FocusNode({
    String? debugLabel,
    this.onKey,
    this.onKeyEvent,
    bool skipTraversal = false,
    bool canRequestFocus = true,
    bool descendantsAreFocusable = true,
    bool descendantsAreTraversable = true,
  })
```

### FocusNode(...)参数解析
| 参数名称                      | 使用类型                                            | 参数介绍                                      |
|---------------------------|-------------------------------------------------|-------------------------------------------|
| debugLabel                | String                                          | 用于调试目的的标签，可以帮助开发者在调试时识别该 FocusNode 或组件的状态 |
| onKey                     | KeyEventResult Function(FocusNode, RawKeyEvent) | 这是一个用于处理键盘事件的回调函数                         |
| onKeyEvent                | KeyEventResult Function(FocusNode, KeyEvent)    | 一个回调函数，当键盘事件发生时触发，可以用于处理键盘输入、快捷键等         |
| skipTraversal             | bool                                            | 表示在焦点遍历时是否跳过这个节点                          |
| canRequestFocus           | bool                                            | 指示该节点是否可以请求焦点                             |
| descendantsAreFocusable   | bool                                            | 指示该节点的子孙组件是否可以获得焦点                        |
| descendantsAreTraversable | bool                                            | 指示该节点的子孙组件在焦点遍历中是否可达                      |

## LayoutBuilder类
### 默认构造函数
```text
LayoutBuilder({
    super.key,
    required super.builder,
})
```

### LayoutBuilder(...)参数解析
| 参数名称      | 使用类型            | 参数介绍                                                                 |
|-----------|-----------------|----------------------------------------------------------------------|
| key       | Key             | 一个可选的标识符，用于标记和唯一识别该小部件                                               |
| builder   | Widget Function |  回调函数，包含当前 LayoutBuilder 所能使用的布局约束信息（例如最大宽度和高度）。可以根据这些约束动态地调整子小部件的布局 |

## ScrollController类
### 默认构造函数
```text
ScrollController({
    double initialScrollOffset = 0.0,
    this.keepScrollOffset = true,
    this.debugLabel,
    this.onAttach,
    this.onDetach,
  }) 
```

### ScrollController(...)参数解析
| 参数名称                | 使用类型           | 参数介绍                            |
|---------------------|----------------|---------------------------------|
| initialScrollOffset | double         | 指定滚动控制器的初始滚动偏移量                 |
| keepScrollOffset    | bool           | 指定在控制器附加到 Scrollable 时是否保持滚动偏移量 |
| debugLabel          | String         | 提供调试信息，帮助在调试输出中识别这个控制器          |
| onAttach            | void Function  | 在控制器附加到 Scrollable 时调用的回调函数     |
| onDetach            | void Function  | 在控制器从 Scrollable 分离时调用的回调函数     |

## RawScrollbar类
### 默认构造函数
```text
RawScrollbar({
    super.key,
    required this.child,
    this.controller,
    this.thumbVisibility,
    this.shape,
    this.radius,
    this.thickness,
    this.thumbColor,
    this.minThumbLength = _kMinThumbExtent,
    this.minOverscrollLength,
    this.trackVisibility,
    this.trackRadius,
    this.trackColor,
    this.trackBorderColor,
    this.fadeDuration = _kScrollbarFadeDuration,
    this.timeToFade = _kScrollbarTimeToFade,
    this.pressDuration = Duration.zero,
    this.notificationPredicate = defaultScrollNotificationPredicate,
    this.interactive,
    this.scrollbarOrientation,
    this.mainAxisMargin = 0.0,
    this.crossAxisMargin = 0.0,
    this.padding,
  })
```

### RawScrollbar(...)参数解析
| 参数名称                  | 使用类型                                          | 参数介绍                                             |
|-----------------------|-----------------------------------------------|--------------------------------------------------|
| key                   | Key                                           | 用于标识这个小部件，通常用于构建 widget 树时的性能优化                  |
| child                 | Widget                                        | 必填参数，表示要包裹的子组件                                   |
| controller            | ScrollController                              | ScrollController 实例，用于控制和监听滚动事件                  |
| thumbVisibility       | bool                                          | 控制滑块的可见性，类型为 ScrollbarVisibility                 |
| shape                 | OutlinedBorder                                | 用于定义滚动条的形状                                       |
| radius                | Radius                                        | 定义滑块的圆角半径                                        |
| thickness             | double                                        | 定义滑块的宽度                                          |
| thumbColor            | Color                                         | 定义滑块的颜色                                          |
| minThumbLength        | double                                        | 定义滑块的最小长度，默认为 _kMinThumbExtent                   |
| minOverscrollLength   | double                                        | 定义滑块在超出可滚动区域时的最小长度                               |
| trackVisibility       | bool                                          | 控制轨道的可见性                                         |
| trackRadius           | Radius                                        | 定义轨道的圆角半径                                        |
| trackColor            | Color                                         | 定义轨道的颜色                                          |
| trackBorderColor      | Color                                         | 定义轨道边框的颜色                                        |
| fadeDuration          | Duration                                      | 定义滑块淡入淡出的持续时间，默认为 _kScrollbarFadeDuration        |
| timeToFade            | Duration                                      | 定义滑块消失的时间，默认为 _kScrollbarTimeToFade              |
| pressDuration         | Duration                                      | 定义滑块被按下的持续时间，默认为 Duration.zero                   |
| notificationPredicate | bool Function                                 | 定义通知的预测条件，默认为 defaultScrollNotificationPredicate |
| interactive           | bool                                          | 定义滚动条是否支持交互                                      |
| scrollbarOrientation  | ScrollbarOrientation     ScrollbarOrientation | 定义滚动条的方向（水平或垂直）                                  |
| mainAxisMargin        | double                                        | 定义滑块在主轴方向上的边距，默认为 0.0                            |
| crossAxisMargin       | double                                        | 定义滑块在交叉轴方向上的边距，默认为 0.0                           |
| padding               | EdgeInsets                                    | 定义滑块的内边距                                         |

## PopScope类
### 默认构造函数
```text
PopScope({
    super.key,
    required this.child,
    this.canPop = true,
    this.onPopInvokedWithResult,
    @Deprecated(
      'Use onPopInvokedWithResult instead. '
      'This feature was deprecated after v3.22.0-12.0.pre.',
    )
    this.onPopInvoked,
  })
```

### PopScope(...)参数解析
| 参数名称                   | 使用类型                   | 参数介绍                                  |
|------------------------|------------------------|---------------------------------------|
| key                    | Key                    | 用于标记和保持 Widget 的状态                    |
| child                  | Widget                 | PopScope 的子组件，即页面的主要内容                |
| canPop                 | bool                   | 控制是否允许页面返回操作                          |
| onPopInvokedWithResult | Future<bool> Function  | 当用户触发页面返回时的异步回调，用于执行自定义逻辑，并决定页面是否允许关闭 |
| onPopInvoked           | Future<bool> Function  | 已被弃用                                  |


