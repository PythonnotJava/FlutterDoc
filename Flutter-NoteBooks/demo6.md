# 导航类
> Flutter3.0提供了以下的导航类
> * AppBar：常用的顶部应用栏小部件，它通常作为Scaffold的一个组件，提供了标题、操作按钮、导航按钮等功能。
> * BottomAppBar：用于在应用程序底部创建一个导航栏。
> * TabBar：用于创建选项卡式的导航栏。它通常与TabBarView和DefaultTabController一起使用，以实现切换不同页面内容的功能。
> * BottomNavigationBar：用于创建底部导航栏。它通常与Scaffold的bottomNavigationBar参数一起使用。
> * PageView：用于在水平方向上显示多个页面，并支持通过滑动或指示器切换页面。它提供了一个类似于轮播图的效果，常用于创建滑动切换的页面布局。
> * CupertinoTabBar：用于创建iOS风格的底部导航栏。它通常与CupertinoTabScaffold一起使用。
> * TabBarView：用于显示与TabBar中的选项卡对应的内容。它通常与TabBar和DefaultTabController一起使用，以实现选项卡式的导航和页面切换功能。
> * SliverAppBar：SliverAppBar通常与CustomScrollView一起使用，用于在滚动视图中创建具有吸顶效果的应用栏。它可以根据滚动行为进行展开和折叠，并提供了一些自定义选项来调整其外观和行为。
> * TabController：用于控制选项卡切换的类。它通常与TabBar和TabBarView一起使用，以便在选项卡之间实现同步切换。
> * BottomNavigationBarItem：用于在底部导航栏中显示单个项目。它通常与BottomNavigationBar一起使用，用于创建底部导航栏的每个项目。
> * PageController：PageController是一个用于控制页面切换的类。它通常与PageView一起使用，用于实现滑动切换多个页面的效果。 
> * LinearProgressIndicator：用于显示线性进度条的小部件
## AppBar类
### 默认构造函数
```text
AppBar({
    super.key,
    this.leading,
    this.automaticallyImplyLeading = true,
    this.title,
    this.actions,
    this.flexibleSpace,
    this.bottom,
    this.elevation,
    this.scrolledUnderElevation,
    this.notificationPredicate = defaultScrollNotificationPredicate,
    this.shadowColor,
    this.surfaceTintColor,
    this.shape,
    this.backgroundColor,
    this.foregroundColor,
    this.iconTheme,
    this.actionsIconTheme,
    this.primary = true,
    this.centerTitle,
    this.excludeHeaderSemantics = false,
    this.titleSpacing,
    this.toolbarOpacity = 1.0,
    this.bottomOpacity = 1.0,
    this.toolbarHeight,
    this.leadingWidth,
    this.toolbarTextStyle,
    this.titleTextStyle,
    this.systemOverlayStyle,
    this.forceMaterialTransparency = false,
    this.clipBehavior,
  })
```

### AppBar(...)参数解析
| 参数名称                      | 使用类型                  | 参数介绍                                  |
|---------------------------|-----------------------|---------------------------------------|
| key                       | Key                   | 用于继承自父类的Widget的key                    |
| leading                   | Widget                | 在AppBar左侧显示的widget，通常是一个返回按钮或一个菜单图标按钮 |
| automaticallyImplyLeading | bool                  | 如果leading为null，是否自动添加一个默认的返回按钮        |
| title                     | Widget                | AppBar中间显示的widget，通常是一个标题文本           |
| actions                   | List<Widget>          | 在AppBar右侧显示的一组widget，通常是一些操作按钮        |
| flexibleSpace             | Widget                | AppBar的可伸缩区域，通常用于显示背景图片或其他自定义内容       |
| bottom                    | PreferredSizeWidget   | 在AppBar底部显示的widget，通常是一个TabBar或底部导航栏  |
| elevation                 | double                | AppBar的阴影高度                           |
| scrolledUnderElevation    | double                | 当AppBar在滚动视图上方时的阴影高度                  |
| notificationPredicate     | *bool                 | 用于控制是否要显示滚动通知的回调函数                    |
| shadowColor               | Color                 | AppBar的阴影颜色                           |
| surfaceTintColor          | Color                 | AppBar的表面颜色，用于控制透明度                   |
| shape                     | ShapeBorder           | AppBar的形状，可以是一个圆角矩形或其他自定义形状           |
| backgroundColor           | Color                 | AppBar的背景颜色                           |
| foregroundColor           | Color                 | AppBar的前景颜色，包括文本和图标颜色                 |
| iconTheme                 | IconThemeData         | AppBar中图标的主题样式                        |
| actionsIconTheme          | IconThemeData         | AppBar中操作按钮图标的主题样式                    |
| primary                   | bool                  | AppBar是否是页面的主要AppBar                  |
| centerTitle               | bool                  | 是否将标题居中显示                             |
| excludeHeaderSemantics    | bool                  | 是否排除AppBar的语义信息                       |
| titleSpacing              | double                | 标题文本与其他widget之间的间距                    |
| toolbarOpacity            | double                | AppBar的工具栏透明度                         |
| bottomOpacity             | double                | AppBar底部widget的透明度                    |
| toolbarHeight             | double                | AppBar工具栏的高度                          |
| leadingWidth              | double                | leading widget的宽度                     |
| toolbarTextStyle          | TextStyle             | 工具栏文本的样式                              |
| titleTextStyle            | TextStyle             | 标题文本的样式                               |
| systemOverlayStyle        | SystemUiOverlayStyle  | AppBar的系统覆盖样式，用于控制状态栏和导航栏的颜色和样式       |
| forceMaterialTransparency | bool                  | 是否强制使用Material Design的透明度规则           |
| clipBehavior              | Clip                  | AppBar的剪切行为                           |

> 备注
> * notificationPredicate是一个返回值为bool的回调函数

## BottomAppBar类
### 默认构造函数
```text
BottomAppBar({
    super.key,
    this.color,
    this.elevation,
    this.shape,
    this.clipBehavior = Clip.none,
    this.notchMargin = 4.0,
    this.child,
    this.padding,
    this.surfaceTintColor,
    this.shadowColor,
    this.height,
  })
```

### BottomAppBar(...)参数解析
| 参数名称             | 使用类型               | 参数介绍                                             |
|------------------|--------------------|--------------------------------------------------|
| key              | Key                | 用于继承自父类的Widget的key                               |
| color            | Color              | BottomAppBar的背景颜色                                |
| elevation        | double             | BottomAppBar的阴影高度                                |
| shape            | NotchedShape       | BottomAppBar的形状，可以是一个圆角矩形或其他自定义形状                |
| clipBehavior     | Clip               | BottomAppBar的剪切行为                                |
| notchMargin      | double             | 如果使用FloatingActionButton，指定FAB与BottomAppBar之间的间距 |
| child            | Widget             | BottomAppBar中显示的子widget                          |
| padding          | EdgeInsetsGeometry | BottomAppBar的内边距                                 |
| surfaceTintColor | Color              | BottomAppBar的表面颜色，用于控制透明度                        |
| shadowColor      | Color              | BottomAppBar的阴影颜色                                |
| height           | double             | BottomAppBar的高度                                  |

## TabBar类
### 默认构造函数
```text
 TabBar({
    super.key,
    required this.tabs,
    this.controller,
    this.isScrollable = false,
    this.padding,
    this.indicatorColor,
    this.automaticIndicatorColorAdjustment = true,
    this.indicatorWeight = 2.0,
    this.indicatorPadding = EdgeInsets.zero,
    this.indicator,
    this.indicatorSize,
    this.dividerColor,
    this.labelColor,
    this.labelStyle,
    this.labelPadding,
    this.unselectedLabelColor,
    this.unselectedLabelStyle,
    this.dragStartBehavior = DragStartBehavior.start,
    this.overlayColor,
    this.mouseCursor,
    this.enableFeedback,
    this.onTap,
    this.physics,
    this.splashFactory,
    this.splashBorderRadius,
  }) 
```

### TabBar(...)参数解析
| 参数名称                              | 使用类型                         | 参数介绍                          |
|-----------------------------------|------------------------------|-------------------------------|
| key                               | Key                          | 继承自父类的Key对象，用于标识TabBar小部件     |
| tabs                              | List<Widget>                 | 必要参数，一个包含Tab小部件的列表，用于定义选项卡的内容 |
| controller                        | TabController                | 用于控制选项卡的切换                    |
| isScrollable                      | bool                         | 指示选项卡是否可以水平滚动                 |
| padding                           | EdgeInsetsGeometry           | 用于指定选项卡区域的内边距                 |
| indicatorColor                    | Color                        | 选项卡指示器的颜色                     |
| automaticIndicatorColorAdjustment | bool                         | 指示是否自动调整选项卡指示器的颜色             |
| indicatorWeight                   | double                       | 选项卡指示器的高度，以逻辑像素为单位            |
| indicatorPadding                  | *EdgeInsets                  | 选项卡指示器的内边距                    |
| indicator                         | Decoration                   | 自定义选项卡指示器的外观                  |
| indicatorSize                     | TabBarIndicatorSize          | 用于指定选项卡指示器的大小                 |
| dividerColor                      | Color                        | 选项卡之间分隔线的颜色                   |
| labelColor                        | Color                        | 选中选项卡文本的颜色                    |
| labelStyle                        | EdgeInsetsGeometry           | 选中选项卡文本的样式                    |
| labelPadding                      | EdgeInsetsGeometry           | 选中选项卡文本的内边距                   |
| unselectedLabelColor              | Color                        | 未选中选项卡文本的颜色                   |
| unselectedLabelStyle              | TextStyle                    | 未选中选项卡文本的样式                   |
| dragStartBehavior                 | DragStartBehavior            | 指定用户开始拖动操作的行为                 |
| overlayColor                      | MaterialStateProperty<Color> | 当用户触摸选项卡时的覆盖颜色                |
| mouseCursor                       | MouseCursor                  | 鼠标指针的样式                       |
| enableFeedback                    | bool                         | 指示是否启用触摸反馈                    |
| onTap                             | Function                     | 一个回调函数，当选项卡被点击时触发             |
| physics                           | ScrollPhysics                | 滚动物理效果的配置                     |
| splashFactory                     | InteractiveInkFeatureFactory | 用于创建选项卡触摸水波纹效果的工厂             |
| splashBorderRadius                | BorderRadius                 | 选项卡触摸水波纹效果的边界半径               |

* 备注
* > EdgeInsets是继承于抽象类EdgeInsetsGeometry的实类

### 创建具有次要样式的选项卡栏
```text
TabBar.secondary({
    super.key,
    required this.tabs,
    this.controller,
    this.isScrollable = false,
    this.padding,
    this.indicatorColor,
    this.automaticIndicatorColorAdjustment = true,
    this.indicatorWeight = 2.0,
    this.indicatorPadding = EdgeInsets.zero,
    this.indicator,
    this.indicatorSize,
    this.dividerColor,
    this.labelColor,
    this.labelStyle,
    this.labelPadding,
    this.unselectedLabelColor,
    this.unselectedLabelStyle,
    this.dragStartBehavior = DragStartBehavior.start,
    this.overlayColor,
    this.mouseCursor,
    this.enableFeedback,
    this.onTap,
    this.physics,
    this.splashFactory,
    this.splashBorderRadius,
  })
```

### TabBar.secondary(...)参数解析
| 参数名称                              | 使用类型                         | 参数介绍                          |
|-----------------------------------|------------------------------|-------------------------------|
| key                               | Key                          | 继承自父类的Key对象，用于标识TabBar小部件     |
| tabs                              | List<Widget>                 | 必要参数，一个包含Tab小部件的列表，用于定义选项卡的内容 |
| controller                        | TabController                | 用于控制选项卡的切换                    |
| isScrollable                      | bool                         | 指示选项卡是否可以水平滚动                 |
| padding                           | EdgeInsetsGeometry           | 用于指定选项卡区域的内边距                 |
| indicatorColor                    | Color                        | 选项卡指示器的颜色                     |
| automaticIndicatorColorAdjustment | bool                         | 指示是否自动调整选项卡指示器的颜色             |
| indicatorWeight                   | double                       | 选项卡指示器的高度，以逻辑像素为单位            |
| indicatorPadding                  | *EdgeInsets                  | 选项卡指示器的内边距                    |
| indicator                         | Decoration                   | 自定义选项卡指示器的外观                  |
| indicatorSize                     | TabBarIndicatorSize          | 用于指定选项卡指示器的大小                 |
| dividerColor                      | Color                        | 选项卡之间分隔线的颜色                   |
| labelColor                        | Color                        | 选中选项卡文本的颜色                    |
| labelStyle                        | EdgeInsetsGeometry           | 选中选项卡文本的样式                    |
| labelPadding                      | EdgeInsetsGeometry           | 选中选项卡文本的内边距                   |
| unselectedLabelColor              | Color                        | 未选中选项卡文本的颜色                   |
| unselectedLabelStyle              | TextStyle                    | 未选中选项卡文本的样式                   |
| dragStartBehavior                 | DragStartBehavior            | 指定用户开始拖动操作的行为                 |
| overlayColor                      | MaterialStateProperty<Color> | 当用户触摸选项卡时的覆盖颜色                |
| mouseCursor                       | MouseCursor                  | 鼠标指针的样式                       |
| enableFeedback                    | bool                         | 指示是否启用触摸反馈                    |
| onTap                             | Function                     | 一个回调函数，当选项卡被点击时触发             |
| physics                           | ScrollPhysics                | 滚动物理效果的配置                     |
| splashFactory                     | InteractiveInkFeatureFactory | 用于创建选项卡触摸水波纹效果的工厂             |
| splashBorderRadius                | BorderRadius                 | 选项卡触摸水波纹效果的边界半径               |

## BottomNavigationBar类
### 默认构造函数
```text
BottomNavigationBar({
    super.key,
    required this.items,
    this.onTap,
    this.currentIndex = 0,
    this.elevation,
    this.type,
    Color? fixedColor,
    this.backgroundColor,
    this.iconSize = 24.0,
    Color? selectedItemColor,
    this.unselectedItemColor,
    this.selectedIconTheme,
    this.unselectedIconTheme,
    this.selectedFontSize = 14.0,
    this.unselectedFontSize = 12.0,
    this.selectedLabelStyle,
    this.unselectedLabelStyle,
    this.showSelectedLabels,
    this.showUnselectedLabels,
    this.mouseCursor,
    this.enableFeedback,
    this.landscapeLayout,
    this.useLegacyColorScheme = true,
  })
```

### BottomNavigationBar参数解析
| 参数名称                   | 使用类型                               | 参数介绍                                      |
|------------------------|------------------------------------|-------------------------------------------|
| key                    | Key                                | Widget的唯一标识符，用于在Flutter中识别小部件             |
| items                  | List<BottomNavigationBarItem>      | 必需，BottomNavigationBarItem的列表，定义了底部导航栏的项目 |
| onTap                  | Function                           | 当底部导航栏的项目被选中时触发的回调函数                      |
| currentIndex           | int                                | 当前选中的项目的索引，默认为0（第一个项目）                    |
| elevation              | double                             | 底部导航栏的阴影高度                                |
| type                   | BottomNavigationBarType            | 底部导航栏的类型                                  |
| fixedColor             | Color                              | 选中项目的颜色，如果未设置，则使用主题颜色                     |
| backgroundColor        | Color                              | 底部导航栏的背景颜色                                |
| iconSize               | double                             | 项目图标的大小                                   |
| selectedItemColor      | Color                              | 选中项目的图标和标签颜色，如果未设置，则使用主题颜色                |
| unselectedItemColor    | Color                              | 未选中项目的图标和标签颜色，如果未设置，则使用主题颜色               |
| selectedIconTheme      | IconThemeData                      | 选中项目的图标主题，包括大小、颜色等                        |
| unselectedIconTheme    | IconThemeData                      | 未选中项目的图标主题，包括大小、颜色等                       |
| selectedFontSize       | double                             | 选中项目标签的字体大小                               |
| unselectedFontSize     | double                             | 未选中项目标签的字体大小                              |
| selectedLabelStyle     | TextStyle                          | 选中项目标签的样式，包括字体、颜色等                        |
| unselectedLabelStyle   | TextStyle                          | 未选中项目标签的样式，包括字体、颜色等                       |
| showSelectedLabels     | bool                               | 是否显示选中项目的标签                               |
| showUnselectedLabels   | bool                               | 是否显示未选中项目的标签                              |
| mouseCursor            | MouseCursor                        | 鼠标指针的样式                                   |
| enableFeedback         | bool                               | 是否启用触觉反馈                                  |
| landscapeLayout        | BottomNavigationBarLandscapeLayout | 横屏布局样式                                    |
| useLegacyColorScheme   | bool                               | 是否使用传统的颜色方案                               |

## PageView类
### 默认构造函数
```text
PageView({
    super.key,
    this.scrollDirection = Axis.horizontal,
    this.reverse = false,
    PageController? controller,
    this.physics,
    this.pageSnapping = true,
    this.onPageChanged,
    List<Widget> children = const <Widget>[],
    this.dragStartBehavior = DragStartBehavior.start,
    this.allowImplicitScrolling = false,
    this.restorationId,
    this.clipBehavior = Clip.hardEdge,
    this.scrollBehavior,
    this.padEnds = true,
  })
```

### PageView(...)参数解析
| 参数名称                   | 使用类型              | 参数介绍                         |
|------------------------|-------------------|------------------------------|
| key                    | Key               | 继承自父类的键，用于控制小部件的标识           |
| scrollDirection        | Axis              | 页面滚动的方向                      |
| reverse                | bool              | 决定页面是否按相反顺序显示                |
| controller             | PageController    | 用于控制页面的切换和滚动                 |
| physics                | ScrollPhysics     | 控制滚动行为的滚动物理特性，例如滚动到边界时的反弹效果等 |
| pageSnapping           | bool              | 指定页面是否在滚动停止时对齐到页面的边界         |
| onPageChanged          | Function          | 页面切换完成时的回调函数，接收当前页面的索引作为参数   |
| children               | List<Widget       | 页面的小部件列表，用于显示多个页面            |
| dragStartBehavior      | DragStartBehavior | 指定拖动行为的开始方式                  |
| allowImplicitScrolling | bool              | 是否允许通过隐式手势滚动页面               |
| restorationId          | String            | 用于恢复页面视图的标识                  |
| clipBehavior           | Clip              | 用于控制小部件剪裁行为的枚举值              |
| scrollBehavior         | ScrollBehavior    | 定义滚动行为的滚动行为对象                |
| padEnds                | bool              | 指定是否在第一个和最后一个页面的前后添加额外的填充    |

### 使用了一个构建器函数来按需创建页面的小部件的PageView
```text
PageView.builder({
    super.key,
    this.scrollDirection = Axis.horizontal,
    this.reverse = false,
    PageController? controller,
    this.physics,
    this.pageSnapping = true,
    this.onPageChanged,
    required NullableIndexedWidgetBuilder itemBuilder,
    ChildIndexGetter? findChildIndexCallback,
    int? itemCount,
    this.dragStartBehavior = DragStartBehavior.start,
    this.allowImplicitScrolling = false,
    this.restorationId,
    this.clipBehavior = Clip.hardEdge,
    this.scrollBehavior,
    this.padEnds = true,
  })
```

### PageView.builder(...)参数解析
| 参数名称                   | 使用类型              | 参数介绍                         |
|------------------------|-------------------|------------------------------|
| key                    | Key               | 继承自父类的键，用于控制小部件的标识           |
| scrollDirection        | Axis              | 页面滚动的方向                      |
| reverse                | bool              | 决定页面是否按相反顺序显示                |
| controller             | PageController    | 用于控制页面的切换和滚动                 |
| physics                | ScrollPhysics     | 控制滚动行为的滚动物理特性，例如滚动到边界时的反弹效果等 |
| pageSnapping           | bool              | 指定页面是否在滚动停止时对齐到页面的边界         |
| onPageChanged          | Function          | 页面切换完成时的回调函数，接收当前页面的索引作为参数   |
| itemBuilder            | Widget            | 必需的构建器函数，根据索引构建页面的小部件        |
| findChildIndexCallback | int               | 用于解决子项顺序发生变化时的问题的回调函数        |
| itemCount              | int               | 页面的数量                        |
| dragStartBehavior      | DragStartBehavior | 指定拖动行为的开始方式                  |
| allowImplicitScrolling | bool              | 是否允许通过隐式手势滚动页面               |
| restorationId          | String            | 用于恢复页面视图的标识                  |
| clipBehavior           | Clip              | 用于控制小部件剪裁行为的枚举值              |
| scrollBehavior         | ScrollBehavior    | 定义滚动行为的滚动行为对象                |
| padEnds                | bool              | 指定是否在第一个和最后一个页面的前后添加额外的填充    |

### 允许使用自定义的ChildrenDelegate来构建页面
```text
PageView.custom({
    super.key,
    this.scrollDirection = Axis.horizontal,
    this.reverse = false,
    PageController? controller,
    this.physics,
    this.pageSnapping = true,
    this.onPageChanged,
    required this.childrenDelegate,
    this.dragStartBehavior = DragStartBehavior.start,
    this.allowImplicitScrolling = false,
    this.restorationId,
    this.clipBehavior = Clip.hardEdge,
    this.scrollBehavior,
    this.padEnds = true,
  })
```

### PageView.custom(...)参数解析
| 参数名称                   | 使用类型                | 参数介绍                                    |
|------------------------|---------------------|-----------------------------------------|
| super.key              | Key                 | 继承自父类的键，用于控制小部件的标识                      |
| scrollDirection        | Axis                | 页面滚动的方向                                 |
| reverse                | bool                | 决定页面是否按相反顺序显示                           |
| controller             | PageController      | 用于控制页面的切换和滚动                            |
| physics                | ScrollPhysics       | 控制滚动行为的滚动物理特性，例如滚动到边界时的反弹效果等            |
| pageSnapping           | bool                | 指定页面是否在滚动停止时对齐到页面的边界                    |
| onPageChanged          | Function            | 页面切换完成时的回调函数，接收当前页面的索引作为参数              |
| childrenDelegate       | SliverChildDelegate | 必需的ChildrenDelegate对象，用于定义页面的构建和布局      |
| dragStartBehavior      | DragStartBehavior   | 指定拖动行为的开始方式，默认为 DragStartBehavior.start |
| allowImplicitScrolling | bool                | 是否允许通过隐式手势滚动页面                          |
| restorationId          | String              | 用于恢复页面视图的标识                             |
| clipBehavior           | Clip                | 用于控制小部件剪裁行为的枚举值                         |
| scrollBehavior         | ScrollBehavior      | 定义滚动行为的滚动行为对象                           |
| padEnds                | bool                | 指定是否在第一个和最后一个页面的前后添加额外的填充               |

## CupertinoTabBar类
### 默认构造函数
```text
CupertinoTabBar({
    super.key,
    required this.items,
    this.onTap,
    this.currentIndex = 0,
    this.backgroundColor,
    this.activeColor,
    this.inactiveColor = _kDefaultTabBarInactiveColor,
    this.iconSize = 30.0,
    this.height = _kTabBarHeight,
    this.border = const Border(
      top: BorderSide(
        color: _kDefaultTabBarBorderColor,
        width: 0.0, // 0.0 means one physical pixel
      ),
    ),
  })
```

### CupertinoTabBar(...)参数解析
| 参数名称            | 使用类型                          | 参数介绍                          |
|-----------------|-------------------------------|-------------------------------|
| key             | Key                           | 用于唯一标识该组件的键                   |
| items           | List<BottomNavigationBarItem> | 必需参数，表示底部导航栏的各个标签项            |
| onTap           | Function                      | 点击底部导航栏标签时触发的回调函数             |
| currentIndex    | int                           | 当前选中的标签项的索引，默认为0，表示第一个标签项     |
| backgroundColor | Color                         | 底部导航栏的背景颜色                    |
| activeColor     | Color                         | 选中的标签项的颜色                     |
| inactiveColor   | Color                         | 未选中的标签项的颜色                    |
| iconSize        | double                        | 标签项中图标的大小                     |
| this.height     | double                        | 底部导航栏的高度                      |
| this.border     | Border                        | 底部导航栏的边框样式，默认为一个带有默认颜色和宽度的上边框 |

## TabBarView类
### 默认构造函数
```text
TabBarView({
    super.key,
    required this.children,
    this.controller,
    this.physics,
    this.dragStartBehavior = DragStartBehavior.start,
    this.viewportFraction = 1.0,
    this.clipBehavior = Clip.hardEdge,
  })
```

### TabBarView(...)参数解析
| 参数名称              | 使用类型              | 参数介绍                      |
|-------------------|-------------------|---------------------------|
| key               | Key               | 用于唯一标识该组件的键               |
| children          | List<Widget>      | 必需参数，表示选项卡视图中的子视图列表       |
| controller        | TabController     | 控制TabBarView中的选项卡切换行为的控制器 |
| physics           | ScrollPhysics     | 滚动行为的物理特性，可以控制滚动的效果       |
| dragStartBehavior | DragStartBehavior | 定义拖动的起始行为                 |
| viewportFraction  | double            | 每个子视图在视口中的占比              |
| clipBehavior      | Clip              | 子视图的剪裁行为                  |

## SliverAppBar类
### 默认构造函数
```text
SliverAppBar({
    super.key,
    this.leading,
    this.automaticallyImplyLeading = true,
    this.title,
    this.actions,
    this.flexibleSpace,
    this.bottom,
    this.elevation,
    this.scrolledUnderElevation,
    this.shadowColor,
    this.surfaceTintColor,
    this.forceElevated = false,
    this.backgroundColor,
    this.foregroundColor,
    this.iconTheme,
    this.actionsIconTheme,
    this.primary = true,
    this.centerTitle,
    this.excludeHeaderSemantics = false,
    this.titleSpacing,
    this.collapsedHeight,
    this.expandedHeight,
    this.floating = false,
    this.pinned = false,
    this.snap = false,
    this.stretch = false,
    this.stretchTriggerOffset = 100.0,
    this.onStretchTrigger,
    this.shape,
    this.toolbarHeight = kToolbarHeight,
    this.leadingWidth,
    this.toolbarTextStyle,
    this.titleTextStyle,
    this.systemOverlayStyle,
    this.forceMaterialTransparency = false,
    this.clipBehavior,
  })
```

### SliverAppBar(...)参数解析
| 参数名称                      | 使用类型                 | 参数介绍                            |
|---------------------------|----------------------|---------------------------------|
| key                       | Key                  | 用于唯一标识该组件的键                     |
| leading                   | Widget               | 在应用栏的开始位置显示的小部件，通常是一个返回按钮       |
| automaticallyImplyLeading | bool                 | 当leading为空时，是否自动显示默认的返回按钮       |
| title                     | Widget               | 应用栏的标题部分显示的小部件                  |
| actions                   | List<Widget>         | 在应用栏的末尾位置显示的小部件列表，通常用于放置操作按钮    |
| flexibleSpace             | Widget               | 应用栏的可伸缩空间，可以放置自定义的内容，如图片、渐变背景等  |
| bottom                    | PreferredSizeWidget  | 应用栏的底部部分显示的小部件，通常用于放置选项卡栏或类似的内容 |
| elevation                 | double               | 应用栏的阴影高度                        |
| scrolledUnderElevation    | double               | 应用栏折叠时，内容滚动时的阴影高度               |
| shadowColor               | Color                | 应用栏阴影的颜色                        |
| surfaceTintColor          | Color                | 表面元素的颜色，如返回按钮、标题和操作按钮           |
| forceElevated             | bool                 | 是否强制显示应用栏的阴影，即使内容不滚动            |
| backgroundColor           | Color                | 应用栏的背景色                         |
| foregroundColor           | Color                | 应用栏的前景色，包括文本和图标                 |
| iconTheme                 | IconThemeData?       | 应用栏中图标的主题样式                     |
| actionsIconTheme          | IconThemeData?       | 应用栏中操作按钮图标的主题样式                 |
| primary                   | bool                 | 是否将应用栏视为滚动视图的主要部分               |
| centerTitle               | bool                 | 是否将标题居中显示                       |
| excludeHeaderSemantics    | bool                 | 是否排除应用栏的语义信息，用于无障碍访问            |
| titleSpacing              | double               | 标题和操作按钮之间的间距                    |
| collapsedHeight           | double               | 应用栏折叠时的高度                       |
| expandedHeight            | double               | 应用栏展开时的最大高度                     |
| floating                  | bool                 | 是否在滚动时自动隐藏应用栏，并在滚动停止时恢复显示       |
| pinned                    | bool                 | 是否将应用栏固定在顶部，无论是否发生滚动            |
| snap                      | bool                 | 滚动时是否自动将应用栏展开或折叠到折叠和展开高度的最接近位置  |
| stretch                   | bool                 | 是否允许应用栏在展开时拉伸以填充剩余的空间           |
| stretchTriggerOffset      | double               | 在应用栏开始拉伸之前触发拉伸的滚动偏移量            |
| onStretchTrigger          | Future<void>         | 应用栏拉伸触发时的回调函数                   |
| shape                     | ShapeBorder          | 应用栏的形状，可以是圆角矩形、圆形等              |
| toolbarHeight             | double               | 应用栏的高度                          |
| leadingWidth              | double               | leading小部件的宽度                   |
| toolbarTextStyle          | TextStyle            | 应用栏中文本的样式                       |
| titleTextStyle            | TextStyle            | 标题文本的样式                         |
| systemOverlayStyle        | SystemUiOverlayStyle | 系统覆盖样式，用于控制状态栏和系统导航栏的颜色和样式      |
| forceMaterialTransparency | bool                 | 是否强制应用栏具有材料透明效果                 |
| clipBehavior              | Clip                 | 应用栏的剪辑行为                        |

## TabController类
### 默认构造函数
```text
TabController({
    int initialIndex = 0,
    Duration? animationDuration,
    required this.length,
    required TickerProvider vsync,
  })
```

### TabController(...)参数解析
| 参数名称              | 使用类型           | 参数介绍                               |
|-------------------|----------------|------------------------------------|
| initialIndex      | int            | 初始选中的选项卡索引，默认为0，表示选项卡视图中的第一个选项卡    |
| animationDuration | Duration       | 选项卡切换动画的持续时间                       |
| length            | int            | 必需参数，表示选项卡的数量                      |
| vsync             | TickerProvider | 提供给选项卡控制器的TickerProvider，用于管理动画的时钟 |

## BottomNavigationBarItem类
### 默认构造函数
```text
BottomNavigationBarItem({
    required this.icon,
    this.label,
    Widget? activeIcon,
    this.backgroundColor,
    this.tooltip,
  })
```

### BottomNavigationBarItem参数解析
| 参数名称            | 使用类型    | 参数介绍                    |
|-----------------|---------|-------------------------|
| icon            | Widget  | 必需参数，表示标签项的图标           |
| label           | String  | 标签项的文本标签，可以选择性地提供       |
| activeIcon      | Widget  | 选中标签项时显示的图标             |
| backgroundColor | Color   | 标签项的背景颜色，可以选择性地提供       |
| tooltip         | String  | 标签项的工具提示，当用户长按标签项时显示的文本 |

## PageController类
### 默认构造函数
```text
PageController({
    this.initialPage = 0,
    this.keepPage = true,
    this.viewportFraction = 1.0,
  })
```
### PageController(...)参数解析
| 参数名称              | 使用类型    | 参数介绍                            |
|-------------------|---------|---------------------------------|
| initialPage       | int     | 初始页面的索引，默认为0，表示第一个页面            |
| keepPage          | bool    | 是否保持页面状态                        |
| viewportFraction  | double  | 页面在视口中的占比，默认为1.0，表示每个页面都占据整个视口  |

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
  })
```

### LinearProgressIndicator(...)参数解析
| 参数名称            | 使用类型    | 参数介绍                                                                                 |
|-----------------|---------|--------------------------------------------------------------------------------------|
| key             | Key     | 用于在树中唯一标识该组件                                                                         |
| value           | double  | 表示进度的值，取值范围为 0.0 到 1.0，0.0 表示没有进度，1.0 表示进度完成                                         |
| backgroundColor | Color   | 进度条的背景颜色                                                                             |
| color           | Color   | 进度条的颜色，它会覆盖 valueColor                                                               |
| valueColor      | Color   | 进度条的颜色，可以使用 AlwaysStoppedAnimation<Color> 对象来指定单一颜色，也可以使用 Animation<Color> 对象来指定渐变颜色 |
| minHeight       | double  | 进度条的最小高度                                                                             |
| semanticsLabel  | String  | 用于无障碍访问的标签，用于描述进度条的用途                                                                |
| semanticsValue  | String  | 用于无障碍访问的值，用于描述进度的百分比                                                                 |
