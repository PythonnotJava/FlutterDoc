# 对话框类
> * showDialog：用于显示各种不同类型对话框的载体。
> * showCupertinoDialog：用于显示Cupertino风格对话框的方法。
> * showGeneralDialog：用于显示通用对话框的方法。与showDialog和showCupertinoDialog相比，showGeneralDialog提供了更高度的自定义能力，可以用于构建更灵活和复杂的对话框。
> * AboutDialog：用于显示关于应用程序的对话框。通常，关于对话框用于显示应用程序的版本号、版权信息、开发者信息等。
> * SimpleDialog：用于显示简单的对话框。通常用于在一组选项中让用户选择其中一个选项。
> *  AlertDialog：用于显示一个警示对话框。
> * SimpleDialogOption：通常用于在一组选项中让用户选择其中一个选项，并且它是SimpleDialog的子部件。

## showDialog类
### 默认构造函数
```text
Future<T?> showDialog<T>({
  required BuildContext context,
  required WidgetBuilder builder,
  bool barrierDismissible = true,
  Color? barrierColor = Colors.black54,
  String? barrierLabel,
  bool useSafeArea = true,
  bool useRootNavigator = true,
  RouteSettings? routeSettings,
  Offset? anchorPoint,
  TraversalEdgeBehavior? traversalEdgeBehavior,
})
```

### showDialog(...)参数解析
| 参数名称                   | 使用类型                  | 参数介绍                                           |
|------------------------|-----------------------|------------------------------------------------|
| context                | BuildContext          | 必需参数，用于展示对话框的上下文                               |
| builder                | WidgetBuilder         | 必需的回调函数，它接收一个BuildContext参数，并返回要显示的对话框Widget   |
| barrierDismissible     | bool                  | 指定点击对话框外部是否可关闭对话框                              |
| barrierColor           | Color                 | 遮罩层的颜色                                         |
| barrierLabel           | String                | 用于辅助技术的文字描述，当对话框出现时，这段文字可以帮助屏幕阅读器等辅助技术标识对话框的用途 |
| useSafeArea            | bool                  | 指定是否在显示对话框时使用安全区域                              |
| useRootNavigator       | bool                  | 指定是否使用根导航器来显示对话框                               |
| routeSettings          | RouteSettings         | 对话框的路由设置，可以用于传递一些路由相关的信息                       |
| anchorPoint            | Offset                | 对话框的锚点，这是一个相对于屏幕的偏移量，用于定位对话框的位置                |
| traversalEdgeBehavior  | TraversalEdgeBehavior | 遍历边缘行为                                         |

## showCupertinoDialog类
### 默认构造函数
```text
Future<T?> showCupertinoDialog<T>({
  required BuildContext context,
  required WidgetBuilder builder,
  String? barrierLabel,
  bool useRootNavigator = true,
  bool barrierDismissible = false,
  RouteSettings? routeSettings,
  Offset? anchorPoint,
}) 
```

### showCupertinoDialog(...)参数解析
| 参数名称               | 使用类型              | 参数介绍                                            |
|--------------------|-------------------|-------------------------------------------------|
| context            | BuildContext      | 必需的参数，用于展示对话框的上下文                               |
| builder            | WidgetBuilder     | 必需的参数，回调函数，它接收一个BuildContext参数，并返回要显示的对话框Widget |
| barrierLabel       | String            | 用于辅助技术的文字描述，当对话框出现时，这段文字可以帮助屏幕阅读器等辅助技术标识对话框的用途  |
| useRootNavigator   | bool              | 指定是否使用根导航器来显示对话框                                |
| barrierDismissible | bool              | 指定点击对话框外部是否可关闭对话框                               |
| routeSettings      | RouteSettings     | 对话框的路由设置，可以用于传递一些路由相关的信息                        |
| anchorPoint        | Offset            | 对话框的锚点，这是一个相对于屏幕的偏移量，用于定位对话框的位置                 |

## showGeneralDialog类
### 默认构造函数
```text
Future<T?> showGeneralDialog<T extends Object?>({
  required BuildContext context,
  required RoutePageBuilder pageBuilder,
  bool barrierDismissible = false,
  String? barrierLabel,
  Color barrierColor = const Color(0x80000000),
  Duration transitionDuration = const Duration(milliseconds: 200),
  RouteTransitionsBuilder? transitionBuilder,
  bool useRootNavigator = true,
  RouteSettings? routeSettings,
  Offset? anchorPoint,
})
```

### showGeneralDialog(...)参数解析
| 参数名称               | 使用类型                    | 参数介绍                                                               |
|--------------------|-------------------------|--------------------------------------------------------------------|
| context            | BuildContext            | 必需参数，对话框的上下文                                                       |
| pageBuilder        | RoutePageBuilder        | 必需参数，一个回调函数，它接收一个BuildContext和Animation<double>参数，并返回要显示的对话框Widget |
| barrierDismissible | bool                    | 指定点击对话框外部是否可关闭对话框                                                  |
| barrierLabel       | String                  | 用于辅助技术的文字描述，当对话框出现时，这段文字可以帮助屏幕阅读器等辅助技术标识对话框的用途                     |
| barrierColor       | Color                   | 遮罩层的颜色                                                             |
| transitionDuration | Duration                | 对话框的过渡动画持续时间                                                       |
| transitionBuilder  | RouteTransitionsBuilder | 回调函数，用于自定义对话框的过渡动画                                                 |
| useRootNavigator   | bool                    | 指定是否使用根导航器来显示对话框                                                   |
| routeSettings      | RouteSettings           | 对话框的路由设置，可以用于传递一些路由相关的信息                                           |
| anchorPoint        | Offset                  | 对话框的锚点，这是一个相对于屏幕的偏移量，用于定位对话框的位置                                    |

## AboutDialog类
### 默认构造函数
```text
AboutDialog({
    super.key,
    this.applicationName,
    this.applicationVersion,
    this.applicationIcon,
    this.applicationLegalese,
    this.children,
  })
```

### AboutDialog(...)参数解析
| 参数名称                | 使用类型         | 参数介绍                   |
|---------------------|--------------|------------------------|
| key                 | Key          | 小部件的唯一标识符，可以用于查找和操作小部件 |
| applicationName     | String       | 应用程序的名称                |
| applicationVersion  | String       | 应用程序的版本号               |
| applicationIcon     | Widget       | 应用程序的图标                |
| applicationLegalese | String       | 应用程序的版权信息或法律声明         |
| children            | List<Widget> | 小部件列表，用于显示其他自定义的内容     |
 
## SimpleDialog类
### 默认构造函数
```text
SimpleDialog({
    super.key,
    this.title,
    this.titlePadding = const EdgeInsets.fromLTRB(24.0, 24.0, 24.0, 0.0),
    this.titleTextStyle,
    this.children,
    this.contentPadding = const EdgeInsets.fromLTRB(0.0, 12.0, 0.0, 16.0),
    this.backgroundColor,
    this.elevation,
    this.shadowColor,
    this.surfaceTintColor,
    this.semanticLabel,
    this.insetPadding = _defaultInsetPadding,
    this.clipBehavior = Clip.none,
    this.shape,
    this.alignment,
  })
```

### SimpleDialog(..)参数解析
| 参数名称             | 使用类型                  | 参数介绍                   |
|------------------|-----------------------|------------------------|
| key              | Key                   | 小部件的唯一标识符，可以用于查找和操作小部件 |
| title            | Widget                | 对话框的标题                 |
| titlePadding     | EdgeInsetsGeometry    | 标题区域的内边距               |
| titleTextStyle   | TextStyle             | 标题的文本样式                |
| children         | List<Widget>          | 小部件列表，用于显示对话框的内容       |
| contentPadding   | EdgeInsetsGeometry    | 内容区域的内边距               |
| backgroundColor  | Color                 | 对话框的背景颜色               |
| elevation        | double                | 对话框的阴影高度               |
| shadowColor      | Color                 | 对话框的阴影颜色               |
| surfaceTintColor | Color                 | 表面的着色颜色                |
| semanticLabel    | String                | 用于辅助技术的文本标签            |
| insetPadding     | EdgeInsets            | 内边距                    |
| clipBehavior     | Clip                  | 用于决定如何裁剪对话框的内容         |
| shape            | ShapeBorder           | 对话框的形状                 |
| alignment        | AlignmentGeometry     | 对话框的内容在对话框内的对齐方式       |

## AlertDialog类
### 默认构造函数
```text
AlertDialog({
    super.key,
    this.icon,
    this.iconPadding,
    this.iconColor,
    this.title,
    this.titlePadding,
    this.titleTextStyle,
    this.content,
    this.contentPadding,
    this.contentTextStyle,
    this.actions,
    this.actionsPadding,
    this.actionsAlignment,
    this.actionsOverflowAlignment,
    this.actionsOverflowDirection,
    this.actionsOverflowButtonSpacing,
    this.buttonPadding,
    this.backgroundColor,
    this.elevation,
    this.shadowColor,
    this.surfaceTintColor,
    this.semanticLabel,
    this.insetPadding = _defaultInsetPadding,
    this.clipBehavior = Clip.none,
    this.shape,
    this.alignment,
    this.scrollable = false,
  })
```

### AlertDialog(...)参数解析
| 参数名称                         | 使用类型                 | 参数介绍                                   |
|------------------------------|----------------------|----------------------------------------|
| key                          | Key                  | 用于识别AlertDialog的键，通常用于在测试或构建小部件树中查找小部件 |
| icon                         | Widget               | 可选的图标，显示在对话框的左上角                       |
| iconPadding                  | EdgeInsetsGeometry   | 图标的内边距                                 |
| iconColor                    | Color                | 图标的颜色                                  |
| title                        | Widget               | 对话框的标题文本                               |
| titlePadding                 | EdgeInsetsGeometry   | 标题文本的内边距                               |
| titleTextStyle               | TextStyle            | 标题文本的样式                                |
| content                      | Widget               | 对话框的内容文本                               |
| contentPadding               | EdgeInsetsGeometry   | 内容文本的内边距                               |
| contentTextStyle             | TextStyle            | 内容文本的样式                                |
| actions                      | List<Widget>         | 对话框的操作按钮列表，通常用于触发一些操作或关闭对话框            |
| actionsPadding               | EdgeInsetsGeometry   | 操作按钮的内边距                               |
| actionsAlignment             | MainAxisAlignment    | 操作按钮的对齐方式                              |
| actionsOverflowAlignment     | OverflowBarAlignment | 当操作按钮溢出对话框时的对齐方式                       |
| actionsOverflowDirection     | VerticalDirection    | 当操作按钮溢出对话框时的溢出方向                       |
| actionsOverflowButtonSpacing | double               | 溢出的操作按钮之间的间距                           |
| buttonPadding                | EdgeInsetsGeometry   | 操作按钮的内边距                               |
| backgroundColor              | Color                | 对话框的背景色                                |
| elevation                    | double               | 对话框的阴影高度                               |
| shadowColor                  | Color                | 对话框的阴影颜色                               |
| surfaceTintColor             | Color                | 表面的颜色                                  |
| semanticLabel                | String               | 对话框的语义标签，用于无障碍访问                       |
| insetPadding                 | EdgeInsets           | 对话框的内边距                                |
| clipBehavior                 | Clip                 | 对话框的裁剪行为                               |
| shape                        | ShapeBorder          | 对话框的形状                                 |
| alignment                    | AlignmentGeometry    | 对话框的对齐方式                               |
| scrollable                   | bool                 | 内容是否可滚动                                |

## SimpleDialogOption类
### 默认构造函数
```text
SimpleDialogOption({
    super.key,
    this.onPressed,
    this.padding,
    this.child,
  })
```

### SimpleDialogOption(...)参数解析
| 参数名称      | 使用类型       | 参数介绍                   |
|-----------|------------|------------------------|
| key       | Key        | 小部件的唯一标识符，可以用于查找和操作小部件 |
| onPressed | Function   | 点击选项时触发的回调函数           |
| padding   | EdgeInsets | 选项的内边距                 |
| child     | Widget     | 选项的内容                  |
