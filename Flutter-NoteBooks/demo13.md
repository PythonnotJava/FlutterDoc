# 路由
> Flutter3.0提供了以下的构建路由功能的类
> * PageRouteBuilder：用于构建自定义页面过渡动画的一个类。它允许你自定义页面切换时的动画、过渡效果、持续时间等属性。
> * MaterialPageRoute：是PageRoute 的一个实现，它提供了一个具有标准的Material Design外观的页面切换效果。
> *


## PageRouteBuilder类
```text
PageRouteBuilder({
    super.settings,
    required this.pageBuilder,
    this.transitionsBuilder = _defaultTransitionsBuilder,
    this.transitionDuration = const Duration(milliseconds: 300),
    this.reverseTransitionDuration = const Duration(milliseconds: 300),
    this.opaque = true,
    this.barrierDismissible = false,
    this.barrierColor,
    this.barrierLabel,
    this.maintainState = true,
    super.fullscreenDialog,
    super.allowSnapshotting = true,
  })
```

### PageRouteBuilder(...)参数解析
| 参数名称                      | 使用类型          | 参数介绍                                                                                                                            |
|---------------------------|---------------|---------------------------------------------------------------------------------------------------------------------------------|
| settings                  | RouteSettings | 表示路由的配置信息                                                                                                                       |
| pageBuilder               | Function      | 是一个回调函数，用于构建页面的内容。它接受三个参数BuildContext（上下文）、Animation<double>（页面切换时的动画）、Animation<double>（次级动画）并返回一个 Widget                      |
| transitionsBuilder        | Function      | 是一个回调函数，用于构建页面切换时的动画。它接受四个参数BuildContext（上下文）、Animation<double>（页面切换时的动画）、Animation<double>（次级动画）、Widget（当前页面的内容）并返回一个新的 Widget |
| transitionDuration        | Duration      | 表示页面切换动画的持续时间                                                                                                                   |
| reverseTransitionDuration | Duration      | 表示页面切换动画的反向持续时间，即返回到上一个页面的动画持续时间                                                                                                |
| opaque                    | bool          | 表示新页面是否是不透明的                                                                                                                    |
| barrierDismissible        | bool          | 表示是否可以通过点击背景来关闭当前页面                                                                                                             |
| barrierColor              | Color         | 表示背景的颜色                                                                                                                         |
| barrierLabel              | String        | 表示用于描述背景的语义标签                                                                                                                   |
| maintainState             | bool          | 表示是否保持上一个页面的状态                                                                                                                  |
| fullscreenDialog          | bool          | 表示是否将页面作为全屏对话框显示                                                                                                                |
| allowSnapshotting         | bool          | 表示是否允许页面截图                                                                                                                      |

## MaterialPageRoute类
```text
MaterialPageRoute({
    required this.builder,
    super.settings,
    this.maintainState = true,
    super.fullscreenDialog,
    super.allowSnapshotting = true,
    super.barrierDismissible = false,
  }) 
```

### MaterialPageRoute(...)参数解析
| 参数名称               | 使用类型          | 参数介绍                |
|--------------------|---------------|---------------------|
| builder            | Function      | 是一个回调函数，用于构建页面的内容   |
| settings           | RouteSettings | 表示路由的配置信息           |
| maintainState      | bool          | 表示是否保持上一个页面的状态      |
| fullscreenDialog   | bool          | 表示是否将页面作为全屏对话框显示    |
| allowSnapshotting  | bool          | 表示是否允许页面截图          |
| barrierDismissible | bool          | 表示是否可以通过点击背景来关闭当前页面 |

