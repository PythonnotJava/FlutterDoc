# 事件构建器
> * FutureBuilder：Flutter 中的 FutureBuilder 是一个用于处理异步操作的常用组件。它允许你根据异步操作（例如网络请求、文件读取等）的状态来动态构建 UI。
> * StreamBuilder：是用于处理持续数据流（Stream）的小部件。它依赖于 Stream 对象，并根据 Stream 的数据流动态构建 UI。Stream 表示的是持续产生数据的序列，通常用于实时数据更新、事件监听等场景。
> * ValueListenableBuilder：用于监听和响应值发生变化的小部件，通常用于监听 ValueNotifier 或其他实现了 ValueListenable 接口的对象的变化。与 FutureBuilder 和 StreamBuilder 不同，它并不处理异步操作的结果或数据流的更新。

## FutureBuilder
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

## StreamBuilder
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

## ValueListenableBuilder
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


