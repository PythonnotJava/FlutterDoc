# 容器
> * Form：Flutter中用于创建和管理表单的控件
> * FlexibleSpaceBar：用于在可折叠应用栏的可伸缩空间中创建自定义内容。
> * SliverGrid：用于在可滚动区域中显示网格布局的内容。它是CustomScrollView的一部分，用于创建可滚动的网格视图。
> * SliverGridDelegateWithMaxCrossAxisExtent：用于指定网格布局中子项的大小和布局规则。
> * SliverChildBuilderDelegate：用于构建基于索引的子项的委托类，通常用于构建 SliverList、SliverGrid 等可滚动列表中的子项。
> * SliverFixedExtentList：以固定项高度为基础的滚动列表布局类。
> * CustomScrollView：创建自定义滚动效果的可滚动小部件。
> * ListView：在程序中创建可滚动的列表视图。
> * ListTile：用于在列表视图中显示一个固定样式的列表项。ListTile通常用作ListView或其他类似部件中的子项，以呈现具有一致外观和布局的列表项。
> * Divider：用于在列表视图或其他布局中插入水平或垂直的分割线，以增加列表项或布局元素之间的可视分隔。
> * GridView：用于创建一个二维的可滚动网格布局。
> * GridTile：用于在GridView或CustomScrollView等滚动视图中呈现网格子项的部件。
> * GridTileBar：用于在GridTile中添加标题、副标题、图标和背景的部件。
> * Scrollbar：用于在可滚动组件周围显示滚动条的小部件。
> * ExpansionPanelList：一个可展开的面板列表，它允许您创建一个包含可折叠内容的列表。每个可折叠的面板通常由一个标题和一个内容区域组成，用户可以点击标题来展开或折叠内容。
> * ExpansionPanel：一个单独的可展开面板，是ExpansionPanelList的组成。

## Form类
### 默认构造函数
```text
Form({
    super.key,
    required this.child,
    this.onWillPop,
    this.onChanged,
    AutovalidateMode? autovalidateMode,
  })
```

### Form(...)参数解析
| 参数名称              | 使用类型              | 参数介绍                                                  |
|-------------------|-------------------|-------------------------------------------------------|
| key               | Key               | Form的唯一标识符，用于区分其他控件                                   |
| child             | Widget            | Form的子控件，用于包含表单的其他组件，例如输入字段（TextFormField、TextField等） |
| onWillPop         | Future<bool>      | 一个回调函数，当用户尝试通过返回按钮或返回手势来关闭表单时，会调用该函数                  |
| onChanged         | Function          | 一个回调函数，在表单字段的值发生变化时被调用                                |
| autovalidateMode  | AutovalidateMode  | 指定自动验证模式，控制是否自动验证表单字段                                 |

## FlexibleSpaceBar类
### 默认构造函数
```text
FlexibleSpaceBar({
    super.key,
    this.title,
    this.background,
    this.centerTitle,
    this.titlePadding,
    this.collapseMode = CollapseMode.parallax,
    this.stretchModes = const <StretchMode>[StretchMode.zoomBackground],
    this.expandedTitleScale = 1.5,
  })
```

### FlexibleSpaceBar(...)参数解析
| 参数名称                | 使用类型               | 参数介绍               |
|---------------------|--------------------|--------------------|
| key                 | Key                | 用于在小部件树中唯一标识       |
| title               | Widget             | 用于在空间栏中显示的标题文本     |
| background          | Widget             | 用于在空间栏背景中显示的小部件    |
| centerTitle         | bool               | 用于指定是否将标题居中对齐      |
| titlePadding        | EdgeInsetsGeometry | 用于设置标题的内边距         |
| collapseMode        | CollapseMode       | 指定了空间栏在滚动时的折叠行为    |
| stretchModes        | List<StretchMode>  | 指定了空间栏在拉伸时的行为      |
| expandedTitleScale  | double             | 用于指定标题在空间栏展开时的缩放比例 |

## SliverGrid类
### 默认构造函数
```text
SliverGrid({
    super.key,
    required super.delegate,
    required this.gridDelegate,
  })
```

### SliverGrid(...)参数解析
| 参数名称              | 使用类型                | 参数介绍                             |
|-------------------|---------------------|----------------------------------|
| key               | Key                 | 用于在小部件树中唯一标识                     |
| delegate          | SliverChildDelegate | 一个必需的参数，指定了网格布局的代理，决定了网格的布局方式和行为 |
| childrenDelegate  | SliverGridDelegate  | 一个必需的参数，指定了子项的代理                 |

### 以动态的方式构建网格布局
```text
SliverGrid.builder({
    super.key,
    required this.gridDelegate,
    required NullableIndexedWidgetBuilder itemBuilder,
    ChildIndexGetter? findChildIndexCallback,
    int? itemCount,
    bool addAutomaticKeepAlives = true,
    bool addRepaintBoundaries = true,
    bool addSemanticIndexes = true,
  }) 
```

### SliverGrid.builder(...)参数解析
| 参数名称                   | 使用类型                          | 参数介绍                                   |
|------------------------|-------------------------------|----------------------------------------|
| key                    | Key                           | 用于在小部件树中唯一标识                           |
| gridDelegate           | SliverGridDelegate            | 必需的参数，指定了网格布局的代理，决定了网格的布局方式和行为         |
| itemBuilder            | *NullableIndexedWidgetBuilder | 必需的参数，是一个回调函数，用于构建网格中指定索引位置的子项的小部件     |
| findChildIndexCallback | *ChildIndexGetter             | 回调函数，它接收一个小部件对象，并返回其索引值，用于查找子项的索引      |
| itemCount              | int                           | 一个可选的参数，指定子项的数量                        |
| addAutomaticKeepAlives | bool                          | 指定是否为每个子项添加AutomaticKeepAlive小部件以保持其状态 |
| addRepaintBoundaries   | bool                          | 指定是否为每个子项添加重绘边界，以避免不必要的重绘              |
| addSemanticIndexes     | bool                          | 指定是否为每个子项添加语义索引，以支持辅助功能                |

> 备注
> * NullableIndexedWidgetBuilder是Widget类型的别名
> * ChildIndexGetter是int类型的别名

### 适用于具有固定行数和每行子项数量的网格布局
```text
SliverGrid.count({
    super.key,
    required int crossAxisCount,
    double mainAxisSpacing = 0.0,
    double crossAxisSpacing = 0.0,
    double childAspectRatio = 1.0,
    List<Widget> children = const <Widget>[],
  })
```

### SliverGrid.count(...)参数解析
| 参数名称             | 使用类型          | 参数介绍                 |
|------------------|---------------|----------------------|
| key              | Key           | 用于在小部件树中唯一标识         |
| crossAxisCount   | int           | 必需的参数，指定网格布局中每行的子项数量 |
| mainAxisSpacing  | double        | 指定在主轴上相邻子项之间的间距      |
| crossAxisSpacing | double        | 指定在交叉轴上相邻子项之间的间距     |
| childAspectRatio | double        | 指定子项的宽高比             |
| children         | List<Widget>  | 指定网格中的子项列表           |

### 通过指定最大交叉轴范围来确定子项的大小
```text
SliverGrid.extent({
    super.key,
    required double maxCrossAxisExtent,
    double mainAxisSpacing = 0.0,
    double crossAxisSpacing = 0.0,
    double childAspectRatio = 1.0,
    List<Widget> children = const <Widget>[],
  })
```

### SliverGrid.extent(...)参数解析
| 参数名称               | 使用类型          | 参数介绍                  |
|--------------------|---------------|-----------------------|
| key                | Key           | 用于在小部件树中唯一标识          |
| maxCrossAxisExtent | double        | 必需的参数，指定了子项在交叉轴上的最大范围 |
| mainAxisSpacing    | double        | 指定在主轴上相邻子项之间的间距       |
| crossAxisSpacing   | double        | 指定在交叉轴上相邻子项之间的间距      |
| childAspectRatio   | double        | 指定子项的宽高比              |
| children           | List<Widget>  | 指定网格中的子项列表            |

## SliverGridDelegateWithMaxCrossAxisExtent类
### 默认构造函数
```text
SliverGridDelegateWithMaxCrossAxisExtent({
    required this.maxCrossAxisExtent,
    this.mainAxisSpacing = 0.0,
    this.crossAxisSpacing = 0.0,
    this.childAspectRatio = 1.0,
    this.mainAxisExtent,
  })
```
### SliverGridDelegateWithMaxCrossAxisExtent(...)参数解析
| 参数名称               | 使用类型    | 参数介绍                |
|--------------------|---------|---------------------|
| maxCrossAxisExtent | double  | 必需参数，指定子项在交叉轴上的最大范围 |
| mainAxisSpacing    | double  | 用于指定主轴上相邻子项之间的间距    |
| crossAxisSpacing   | double  | 用于指定交叉轴上相邻子项之间的间距   |
| childAspectRatio   | double  | 用于指定子项的宽高比（宽度除以高度）  |
| mainAxisExtent     | double  | 用于指定子项在主轴上的固定尺寸     |

## SliverChildBuilderDelegate类
### 默认构造函数
```text
SliverChildBuilderDelegate(
    this.builder, {
    this.findChildIndexCallback,
    this.childCount,
    this.addAutomaticKeepAlives = true,
    this.addRepaintBoundaries = true,
    this.addSemanticIndexes = true,
    this.semanticIndexCallback = _kDefaultSemanticIndexCallback,
    this.semanticIndexOffset = 0,
  })
```
### SliverChildBuilderDelegate(...)参数解析
| 参数名称                         | 使用类型   | 参数介绍                   |
|------------------------------|--------|------------------------|
| IndexedWidgetBuilder builder | Widget | 必需参数，用于构建子项的回调函数       |
| findChildIndexCallback       | int    | 用于查找子项的索引              |
| childCount                   | int    | 指定子项的总数                |
| addAutomaticKeepAlives       | bool   | 用于控制是否为子项添加自动保持活动状态的功能 |
| addRepaintBoundaries         | bool   | 用于控制是否为子项添加重绘边界        |
| addSemanticIndexes           | bool   | 用于控制是否为子项添加语义索引        |
| semanticIndexCallback        | int    | 用于构建语义索引的回调函数          |
| semanticIndexOffset          | int    | 用于指定语义索引的偏移量           |

## SliverFixedExtentList类
### 默认构造函数
```text
SliverFixedExtentList({
    super.key,
    required super.delegate,
    required this.itemExtent,
  })
```

### SliverFixedExtentList(...)参数解析
| 参数名称         | 使用类型                | 参数介绍                       |
|--------------|---------------------|----------------------------|
| key          | Key                 | 可选参数，用于在小部件树中唯一标识此小部件      |
| delegate     | SliverChildDelegate | 必需参数，用于提供子项的委托对            |
| itemExtent   | double              | 必需参数，指定每个子项的高度             |

### 使用构建器模式来构建子项
```text
SliverFixedExtentList.builder({
    super.key,
    required NullableIndexedWidgetBuilder itemBuilder,
    required this.itemExtent,
    ChildIndexGetter? findChildIndexCallback,
    int? itemCount,
    bool addAutomaticKeepAlives = true,
    bool addRepaintBoundaries = true,
    bool addSemanticIndexes = true,
  }) 
```

### SliverFixedExtentList.builder(...)参数解析
| 参数名称                   | 使用类型                         | 参数介绍                      |
|------------------------|------------------------------|---------------------------|
| key                    | Key                          | 用于在小部件树中唯一标识此小部件          |
| itemBuilder            | NullableIndexedWidgetBuilder | 必需参数，一个构建器函数，它根据索引构建子项小部件 |
| itemExtent             | double                       | 必需参数，指定每个子项的高度            |
| findChildIndexCallback | ChildIndexGetter             | 回调函数，用于查找子项的索引            |
| itemCount              | int                          | 子项的总数                     |
| addAutomaticKeepAlives | bool                         | 是否在滚动时自动保留子项的状态           |
| addRepaintBoundaries   | bool                         | 是否为子项添加重绘边界               |
| addSemanticIndexes     | bool                         | 是否为子项添加语义索引               |

### 接收一个包含子项小部件的列表作为参数
```text
SliverFixedExtentList.list({
    super.key,
    required List<Widget> children,
    required this.itemExtent,
    bool addAutomaticKeepAlives = true,
    bool addRepaintBoundaries = true,
    bool addSemanticIndexes = true,
  }) 
```

### SliverFixedExtentList.list(...)参数解析
| 参数名称                   | 使用类型           | 参数介绍             |
|------------------------|----------------|------------------|
| key                    | Key            | 用于在小部件树中唯一标识此小部件 |
| children               | List<Widget>   | 必需参数，包含子项小部件的列表  |
| itemExtent             | double         | 必需参数，指定每个子项的高度   |
| addAutomaticKeepAlives | bool           | 可是否在滚动时自动保留子项的状态 |
| addRepaintBoundaries   | bool           | 是否为子项添加重绘边界      |
| addSemanticIndexes     | bool           | 是否为子项添加语义索引      |


## CustomScrollView类
### 默认构造函数
```text
CustomScrollView({
    super.key,
    super.scrollDirection,
    super.reverse,
    super.controller,
    super.primary,
    super.physics,
    super.scrollBehavior,
    super.shrinkWrap,
    super.center,
    super.anchor,
    super.cacheExtent,
    this.slivers = const <Widget>[],
    super.semanticChildCount,
    super.dragStartBehavior,
    super.keyboardDismissBehavior,
    super.restorationId,
    super.clipBehavior,
  })
```

### CustomScrollView(...)参数解析
| 参数名称                    | 使用类型                              | 参数介绍                             |
|-------------------------|-----------------------------------|----------------------------------|
| key                     | Key                               | 小部件的唯一标识符                        |
| scrollDirection         | Axis                              | 指定滚动方向                           |
| reverse                 | bool                              | 确定滚动方向是否反向                       |
| controller              | ScrollController                  | 控制滚动位置和监听滚动事件的ScrollController对象 |
| primary                 | bool                              | 指示是否为主滚动视图，主滚动视图通常用于嵌套滚动         |
| physics                 | ScrollPhysics                     | 指定滚动物理属性的滚动物理对象                  |
| scrollBehavior          | ScrollBehavior                    | 滚动行为对象，用于自定义滚动交互                 |
| shrinkWrap              | bool                              | 指示是否根据子部件的大小来调整滚动视图的大小           |
| center                  | Key                               | 用于指定滚动视图的对齐方式的Key对象              |
| anchor                  | double                            | 指定滚动视图在可滚动范围内的对齐位置，介于0.0和1.0之间   |
| cacheExtent             | double                            | 用于确定缓存区域的大小                      |
| semanticChildCount      | int                               | 指定语义子部件的数量                       |
| dragStartBehavior       | DragStartBehavior                 | 指定拖动开始行为的枚举值                     |
| keyboardDismissBehavior | ScrollViewKeyboardDismissBehavior | 指定键盘消失行为的枚举值                     |
| restorationId           | String                            | 用于恢复滚动视图状态的ID                    |
| clipBehavior            | Clip                              | 定义子部件裁剪行为的枚举值                    |

## ListView类
### 默认构造函数
```text
ListView({
    super.key,
    super.scrollDirection,
    super.reverse,
    super.controller,
    super.primary,
    super.physics,
    super.shrinkWrap,
    super.padding,
    this.itemExtent,
    this.prototypeItem,
    bool addAutomaticKeepAlives = true,
    bool addRepaintBoundaries = true,
    bool addSemanticIndexes = true,
    super.cacheExtent,
    List<Widget> children = const <Widget>[],
    int? semanticChildCount,
    super.dragStartBehavior,
    super.keyboardDismissBehavior,
    super.restorationId,
    super.clipBehavior,
  })
```

### ListView(...)参数解析
| 参数名称                    | 使用类型                              | 参数介绍                       |
|-------------------------|-----------------------------------|----------------------------|
| key                     | Key                               | Widget的唯一标识符，用于识别和检索Widget |
| scrollDirection         | Axis                              | 列表滚动的方向                    |
| reverse                 | bool                              | 是否反向滚动                     |
| controller              | ScrollController                  | 滚动控制器，用于控制列表的滚动位置和行为       |
| primary                 | bool                              | 是否将列表视为主要滚动视图              |
| physics                 | ScrollPhysics                     | 指定用于控制列表滚动行为的物理效果          |
| shrinkWrap              | bool                              | 是否根据子部件的总长度来调整列表的大小        |
| padding                 | EdgeInsetsGeometry                | 列表的内边距                     |
| itemExtent              | double                            | 指定子部件的固定长度，用于优化性能          |
| prototypeItem           | Widget                            | 用于估算子部件大小的原型部件             |
| addAutomaticKeepAlives  | bool                              | 是否自动保持子部件的状态               |
| addRepaintBoundaries    | bool                              | 是否添加重绘边界                   |
| addSemanticIndexes      | bool                              | 是否添加语义索引                   |
| cacheExtent             | double                            | 预加载区域的长度，用于提前加载子部件以改善滚动性能  |
| children                | List<Widget>                      | 子部件的列表，用于构建列表的内容           |
| semanticChildCount      | int                               | 语义子部件的数量，用于辅助功能            |
| dragStartBehavior       | DragStartBehavior                 | 确定滚动操作的启动行为                |
| keyboardDismissBehavior | ScrollViewKeyboardDismissBehavior | 确定滚动时键盘的行为                 |
| restorationId           | String                            | 用于恢复滚动位置的唯一标识符             |
| clipBehavior            | Clip                              | 指定如何剪裁子部件                  |

### 按需构建子部件
```text
ListView.builder({
    super.key,
    super.scrollDirection,
    super.reverse,
    super.controller,
    super.primary,
    super.physics,
    super.shrinkWrap,
    super.padding,
    this.itemExtent,
    this.prototypeItem,
    required NullableIndexedWidgetBuilder itemBuilder,
    ChildIndexGetter? findChildIndexCallback,
    int? itemCount,
    bool addAutomaticKeepAlives = true,
    bool addRepaintBoundaries = true,
    bool addSemanticIndexes = true,
    super.cacheExtent,
    int? semanticChildCount,
    super.dragStartBehavior,
    super.keyboardDismissBehavior,
    super.restorationId,
    super.clipBehavior,
  })
```

### ListView.builder(...)参数解析
| 参数名称                    | 使用类型                              | 参数介绍                              |
|-------------------------|-----------------------------------|-----------------------------------|
| key                     | Key                               | 用于标识ListView.builder的可选键（Key）     |
| scrollDirection         | Axis                              | 列表滚动方向                            |
| reverse                 | bool                              | 是否反转列表的滚动方向                       |
| controller              | ScrollController                  | 滚动控制器，用于控制列表的滚动位置和监听滚动事件          |
| primary                 | bool                              | 是否将列表视图置于滚动视图中的主滚动视图中             |
| physics                 | ScrollPhysics                     | 用于控制列表滚动行为的滚动物理效果                 |
| shrinkWrap              | bool                              | 是否根据子部件的大小来调整列表的大小                |
| padding                 | EdgeInsetsGeometry                | 列表的内边距                            |
| itemExtent              | double                            | 如果所有子部件具有相同的固定高度或宽度，则可以指定此参数来优化性能 |
| prototypeItem           | Widget                            | 用于确定子部件的大小的原型部件（Widget）           |
| itemBuilder             | *NullableIndexedWidgetBuilder     | 必需的参数，是一个回调函数，用于根据索引构建子部件         |
| findChildIndexCallback  | *ChildIndexGetter                 | 回调函数，用于查找指定子部件的索引                 |
| itemCount               | int                               | 子部件的数量，用于确定列表的长度                  |
| addAutomaticKeepAlives  | bool                              | 是否在子部件中自动添加保持活动                   |
| addRepaintBoundaries    | bool                              | 是否在子部件之间自动添加重绘边界                  |
| addSemanticIndexes      | bool                              | 是否为子部件自动添加语义索引                    |
| cacheExtent             | double                            | 在滚动前和后缓存的列表部件的长度                  |
| semanticChildCount      | int                               | 子部件的语义数量                          |
| dragStartBehavior       | DragStartBehavior                 | 确定滚动视图如何响应拖动手势                    |
| keyboardDismissBehavior | ScrollViewKeyboardDismissBehavior | 确定键盘关闭行为                          |
| restorationId           | String                            | 用于恢复滚动位置的唯一标识符                    |
| clipBehavior            | Clip                              | 子部件的剪裁行为                          |

> 备注
> * NullableIndexedWidgetBuilder是返回值为Widget的回调函数
> * ChildIndexGetter是返回值为int的回调函数

### 创建一个带有分隔符的列表视图
```text
ListView.separated({
    super.key,
    super.scrollDirection,
    super.reverse,
    super.controller,
    super.primary,
    super.physics,
    super.shrinkWrap,
    super.padding,
    required NullableIndexedWidgetBuilder itemBuilder,
    ChildIndexGetter? findChildIndexCallback,
    required IndexedWidgetBuilder separatorBuilder,
    required int itemCount,
    bool addAutomaticKeepAlives = true,
    bool addRepaintBoundaries = true,
    bool addSemanticIndexes = true,
    super.cacheExtent,
    super.dragStartBehavior,
    super.keyboardDismissBehavior,
    super.restorationId,
    super.clipBehavior,
  })
```

### ListView.separated(...)参数解析
| 参数名称                    | 使用类型                              | 参数介绍                               |
|-------------------------|-----------------------------------|------------------------------------|
| key                     | Key                               | 用于标识ListView.separated的可选键         |
| scrollDirection         | Axis                              | 列表滚动方向                             |
| reverse                 | bool                              | 是否反转列表的滚动方向                        |
| controller              | ScrollController                  | 用于控制列表的滚动位置和监听滚动事件                 |
| primary                 | bool                              | 是否将列表视图置于滚动视图中的主滚动视图中              |
| physics                 | ScrollPhysics                     | 用于控制列表滚动行为的滚动物理效果                  |
| shrinkWrap              | bool                              | 是否根据子项的总长度来调整列表的大小                 |
| padding                 | EdgeInsetsGeometry                | 列表的内边距                             |
| itemBuilder             | NullableIndexedWidgetBuilder      | 必需的参数，一个回调函数，用于根据索引构建列表项的小部件       |
| separatorBuilder        | IndexedWidgetBuilder              | 必需的参数，一个回调函数，用于根据索引构建列表项之间的分隔符的小部件 |
| findChildIndexCallback  | *ChildIndexGetter                 | 回调函数，用于查找指定子部件的索引                  |
| itemCount               | int                               | 必需的参数，列表项的数量                       |
| addAutomaticKeepAlives  | bool                              | 是否自动保持列表项的活动状态                     |
| addRepaintBoundaries    | bool                              | 是否在列表项之间添加重绘边界                     |
| addSemanticIndexes      | bool                              | 是否为列表项添加语义索引                       |
| cacheExtent             | double                            | 在滚动视图中缓存列表项的区域长度                   |
| semanticChildCount      | List<Widget>                      | 列表项的语义子项数                          |
| dragStartBehavior       | DragStartBehavior                 | 定义拖动开始行为的方式                        |
| keyboardDismissBehavior | ScrollViewKeyboardDismissBehavior | 定义当用户滚动列表时键盘的行为方式                  |
| restorationId           | String                            | 用于恢复列表视图的标识符                       |
| clipBehavior            | Clip                              | 定义如何裁剪列表项的内容                       |


## ListTile类
### 默认构造函数
```text
ListTile({
    super.key,
    this.leading,
    this.title,
    this.subtitle,
    this.trailing,
    this.isThreeLine = false,
    this.dense,
    this.visualDensity,
    this.shape,
    this.style,
    this.selectedColor,
    this.iconColor,
    this.textColor,
    this.titleTextStyle,
    this.subtitleTextStyle,
    this.leadingAndTrailingTextStyle,
    this.contentPadding,
    this.enabled = true,
    this.onTap,
    this.onLongPress,
    this.onFocusChange,
    this.mouseCursor,
    this.selected = false,
    this.focusColor,
    this.hoverColor,
    this.splashColor,
    this.focusNode,
    this.autofocus = false,
    this.tileColor,
    this.selectedTileColor,
    this.enableFeedback,
    this.horizontalTitleGap,
    this.minVerticalPadding,
    this.minLeadingWidth,
    this.titleAlignment,
  })
```

### ListTile(...)参数解析
| 参数名称                        | 使用类型                    | 参数介绍                                 |
|-----------------------------|-------------------------|--------------------------------------|
| key                         | Key                     | 继承自父类 Widget 的参数，用于在构建部件时标识 ListTile |
| leading                     | Widget                  | 在 ListTile 前面显示的小部件，通常是一个图标          |
| title                       | Widget                  | ListTile 的主标题，通常是一个文本部件              |
| subtitle                    | Widget                  | ListTile 的副标题，通常是一个文本部件              |
| trailing                    | Widget                  | 在 ListTile 后面显示的小部件，通常是一个图标          |
| isThreeLine                 | bool                    | 用于指定是否将 ListTile 的副标题显示为三行           |
| dense                       | bool                    | 用于指定 ListTile 是否使用较小的垂直尺寸            |
| visualDensity               | VisualDensity           | 控制 ListTile 的尺寸和填充                   |
| shape                       | ShapeBorder             | 定义 ListTile 的边框形状                    |
| style                       | ListTileStyle           | 定义 ListTile 中文本的样式                   |
| selectedColor               | Color                   | 当 ListTile 被选中时的背景颜色                 |
| iconColor                   | Color                   | ListTile 中图标的颜色                      |
| textColor                   | Color                   | ListTile 中文本的颜色                      |
| titleTextStyle              | TextStyle               | 用于自定义 title 文本的样式                    |
| subtitleTextStyle           | TextStyle               | 用于自定义 subtitle 文本的样式                 |
| leadingAndTrailingTextStyle | TextStyle               | 用于自定义 leading 和 trailing 文本的样式       |
| contentPadding              | EdgeInsetsGeometry      | ListTile 内容的内边距                      |
| enabled                     | bool                    | 指定 ListTile 是否可点击                    |
| onTap                       | Function                | 当 ListTile 被点击时触发的回调函数               |
| onLongPress                 | Function                | 当 ListTile 被长按时触发的回调函数               |
| onFocusChange               | Function                | 当 ListTile 获得或失去焦点时触发的回调函数           |
| mouseCursor                 | MouseCursor             | 指定鼠标指针在 ListTile 上的样式                |
| selected                    | bool                    | 指定 ListTile 是否被选中                    |
| focusColor                  | Color                   | 当 ListTile 获得焦点时的背景颜色                |
| hoverColor                  | Color                   | 当鼠标悬停在 ListTile 上时的背景颜色              |
| splashColor                 | Color                   | 当用户点击 ListTile 时的水波纹颜色               |
| focusNode                   | FocusNode               | 指定用于管理 ListTile 的焦点状态的 FocusNode     |
| autofocus                   | bool                    | 指定是否自动获取焦点                           |
| tileColor                   | Color                   | ListTile 的背景颜色                       |
| selectedTileColor           | Color                   | 当 ListTile 被选中时的背景颜色                 |
| enableFeedback              | bool                    | 指定是否启用触觉反馈                           |
| horizontalTitleGap          | double                  | title 和 subtitle 之间的水平间距             |
| minVerticalPadding          | double                  | ListTile 内容的最小垂直填充                   |
| minLeadingWidth             | double                  | leading 小部件的最小宽度                     |
| titleAlignment              | ListTileTitleAlignment  | 指定 title 的对齐方式                       |

## Divider类
### 默认构造函数
```text
Divider({
    super.key,
    this.height,
    this.thickness,
    this.indent,
    this.endIndent,
    this.color,
  })
```

### Divider(...)参数解析
| 参数名称      | 使用类型   | 参数介绍                                |
|-----------|--------|-------------------------------------|
| key       | Key    | 继承自父类 Widget 的参数，用于在构建部件时标识 Divider |
| height    | double | 分隔线的高度，即垂直方向上的尺寸                    |
| thickness | double | 分隔线的粗细度量，即水平方向上的宽度                  |
| indent    | double | 分隔线的起始缩进量，即分隔线距离容器左侧的距离             |
| endIndent | double | 分隔线的结束缩进量，即分隔线距离容器右侧的距离             |
| color     | Color  | 分隔线的颜色                              |


## GridView类
### 默认构造函数
```text
GridView({
    super.key,
    super.scrollDirection,
    super.reverse,
    super.controller,
    super.primary,
    super.physics,
    super.shrinkWrap,
    super.padding,
    required this.gridDelegate,
    bool addAutomaticKeepAlives = true,
    bool addRepaintBoundaries = true,
    bool addSemanticIndexes = true,
    super.cacheExtent,
    List<Widget> children = const <Widget>[],
    int? semanticChildCount,
    super.dragStartBehavior,
    super.clipBehavior,
    super.keyboardDismissBehavior,
    super.restorationId,
  })
```

### GridView(...)参数解析
| 参数名称                    | 使用类型                              | 参数介绍                          |
|-------------------------|-----------------------------------|-------------------------------|
| key                     | Key                               | 组件的唯一标识符，可以用于查找特定的组件          |
| scrollDirection         | Axis                              | 指定滚动的方向                       |
| reverse                 | bool                              | 表示是否反转滚动方向                    |
| controller              | ScrollController                  | 可以用于控制滚动位置和监听滚动事件             |
| primary                 | bool                              | 表示是否将此 GridView 设置为主滚动视图      |
| physics                 | ScrollPhysics                     | 指定滚动行为的滚动物理属性                 |
| shrinkWrap              | bool                              | 表示是否根据子组件的总长度来调整 GridView 的大小 |
| padding                 | EdgeInsetsGeometry                | 表示 GridView 的内边距              |
| gridDelegate            | SliverGridDelegate                | 一个必需的参数，它指定了网格的布局规则           |
| addAutomaticKeepAlives  | bool                              | 表示是否在可见范围内自动保持子组件的状态          |
| addRepaintBoundaries    | bool                              | 表示是否在子组件之间添加重绘边界，可以提高性能       |
| addSemanticIndexes      | bool                              | 表示是否为语义框架添加语义索引               |
| cacheExtent             | double                            | 指定预加载的区域，可以缓存超出屏幕的子组件         |
| children                | List<Widget>                      | 一个包含子组件的列表                    |
| semanticChildCount      | int                               | 用于指定语义子组件的数量                  |
| dragStartBehavior       | DragStartBehavior                 | 用于确定开始拖动手势的处理方式               |
| clipBehavior            | Clip                              | 用于指定子组件的裁剪行为                  |
| keyboardDismissBehavior | ScrollViewKeyboardDismissBehavior | 用于控制键盘如何响应滚动行为                |
| restorationId           | String                            | 用于保存组件的状态并进行恢复                |

### 创建一个*懒加载的网格列表
```text
GridView.builder({
    super.key,
    super.scrollDirection,
    super.reverse,
    super.controller,
    super.primary,
    super.physics,
    super.shrinkWrap,
    super.padding,
    required this.gridDelegate,
    required NullableIndexedWidgetBuilder itemBuilder,
    ChildIndexGetter? findChildIndexCallback,
    int? itemCount,
    bool addAutomaticKeepAlives = true,
    bool addRepaintBoundaries = true,
    bool addSemanticIndexes = true,
    super.cacheExtent,
    int? semanticChildCount,
    super.dragStartBehavior,
    super.keyboardDismissBehavior,
    super.restorationId,
    super.clipBehavior,
  })
```

### GridView.builder(...)参数解析
| 参数名称                    | 使用类型                              | 参数介绍                          |
|-------------------------|-----------------------------------|-------------------------------|
| key                     | Key                               | 组件的唯一标识符，可选参数                 |
| scrollDirection         | Axis                              | 指定滚动的方向                       |
| reverse                 | bool                              | 表示是否反转滚动方向                    |
| controller              | ScrollController                  | 用于控制滚动位置和监听滚动事件               |
| primary                 | bool                              | 表示是否将此 GridView 设置为主滚动视图      |
| physics                 | ScrollPhysics                     | 指定滚动行为的滚动物理属性，继承自父类 GridView  |
| shrinkWrap              | bool                              | 表示是否根据子组件的总长度来调整 GridView 的大小 |
| padding                 | EdgeInsetsGeometry                | 表示 GridView 的内边距              |
| gridDelegate            | SliverGridDelegate                | 必需的参数，它指定了网格的布局规则             |
| itemBuilder             | *NullableIndexedWidgetBuilder     | 构建子组件的回调函数                    |
| findChildIndexCallback  | *ChildIndexGetter                 | 回调函数，用于查找给定键的子组件索引            |
| itemCount               | int                               | 子组件的数量                        |
| addAutomaticKeepAlives  | bool                              | 表示是否在可见范围内自动保持子组件的状态          |
| addRepaintBoundaries    | bool                              | 表示是否在子组件之间添加重绘边界，可以提高性能       |
| addSemanticIndexes      | bool                              | 表示是否为语义框架添加语义索引               |
| cacheExtent             | double                            | 指定预加载的区域，可以缓存超出屏幕的子组件         |
| semanticChildCount      | int                               | 用于指定语义子组件的数量                  |
| dragStartBehavior       | DragStartBehavior                 | 用于确定开始拖动手势的处理方式               |
| keyboardDismissBehavior | ScrollViewKeyboardDismissBehavior | 用于控制键盘如何响应滚动行为                |
| restorationId           | String                            | 用于保存组件的状态并进行恢复                |
| clipBehavior            | Clip                              | 用于指定子组件的裁剪行为                  |


> 备注
> * 所谓懒加载，是指用到才会创建。懒加载可以应用于各种情况，如构建大型列表或网格，加载大型图片或资源等。
> * NullableIndexedWidgetBuilder是返回值为Widget类型的函数的别名
> * ChildIndexGetter是返回值为int类型的函数的别名

### 用于创建自定义网格列表的构造函数
```text
GridView.custom({
    super.key,
    super.scrollDirection,
    super.reverse,
    super.controller,
    super.primary,
    super.physics,
    super.shrinkWrap,
    super.padding,
    required this.gridDelegate,
    required this.childrenDelegate,
    super.cacheExtent,
    super.semanticChildCount,
    super.dragStartBehavior,
    super.keyboardDismissBehavior,
    super.restorationId,
    super.clipBehavior,
  })
```

### GridView.custom(...)参数解析
| 参数名称                    | 使用类型                              | 参数介绍                          |
|-------------------------|-----------------------------------|-------------------------------|
| key                     | Key                               | 组件的唯一标识符，可选参数                 |
| scrollDirection         | Axis                              | 指定滚动的方向                       |
| reverse                 | bool                              | 表示是否反转滚动方向                    |
| controller              | ScrollController                  | 可以用于控制滚动位置和监听滚动事件             |
| primary                 | bool                              | 表示是否将此 GridView 设置为主滚动视图      |
| physics                 | ScrollPhysics                     | 指定滚动行为的滚动物理属性                 |
| shrinkWrap              | bool                              | 表示是否根据子组件的总长度来调整 GridView 的大小 |
| padding                 | EdgeInsetsGeometry                | 表示 GridView 的内边距              |
| gridDelegate            | SliverGridDelegate                | 必需的参数，它指定了网格的布局规则             |
| childrenDelegate        | SliverChildDelegate               | 必需的参数，用于自定义子组件的构建逻辑           |
| cacheExtent             | double                            | 指定预加载的区域，可以缓存超出屏幕的子组件         |
| semanticChildCount      | int                               | 用于指定语义子组件的数量                  |
| dragStartBehavior       | DragStartBehavior                 | 用于确定开始拖动手势的处理方式               |
| keyboardDismissBehavior | ScrollViewKeyboardDismissBehavior | 用于控制键盘如何响应滚动行为                |
| restorationId           | String                            | 用于保存组件的状态并进行恢复                |
| clipBehavior            | Clip                              | 用于指定子组件的裁剪行为                  |


### 
```text
GridView.count({
    super.key,
    super.scrollDirection,
    super.reverse,
    super.controller,
    super.primary,
    super.physics,
    super.shrinkWrap,
    super.padding,
    required int crossAxisCount,
    double mainAxisSpacing = 0.0,
    double crossAxisSpacing = 0.0,
    double childAspectRatio = 1.0,
    bool addAutomaticKeepAlives = true,
    bool addRepaintBoundaries = true,
    bool addSemanticIndexes = true,
    super.cacheExtent,
    List<Widget> children = const <Widget>[],
    int? semanticChildCount,
    super.dragStartBehavior,
    super.keyboardDismissBehavior,
    super.restorationId,
    super.clipBehavior,
  })
```

### GridView.count(...)参数解析
| 参数名称                    | 使用类型                              | 参数介绍                          |
|-------------------------|-----------------------------------|-------------------------------|
| key                     | Key                               | 组件的唯一标识符                      |
| scrollDirection         | Axis                              | 指定滚动的方向                       |
| reverse                 | bool                              | 表示是否反转滚动方向                    |
| controller              | ScrollController                  | 用于控制滚动位置和监听滚动事件               |
| primary                 | bool                              | 表示是否将此 GridView 设置为主滚动视图      |
| physics                 | ScrollPhysics                     | 指定滚动行为的滚动物理属性                 |
| shrinkWrap              | bool                              | 表示是否根据子组件的总长度来调整 GridView 的大小 |
| padding                 | EdgeInsetsGeometry                | 表示 GridView 的内边距              |
| crossAxisCount          | int                               | 必需参数，指定每行显示的子项数量              |
| mainAxisSpacing         | double                            | 主轴（垂直方向）上的间距                  |
| crossAxisSpacing        | double                            | 交叉轴（水平方向）上的间距                 |
| childAspectRatio        | double                            | 子项的宽高比，即子项的宽度与高度的比例           |
| addAutomaticKeepAlives  | bool                              | 表示是否在可见范围内自动保持子组件的状态          |
| addRepaintBoundaries    | bool                              | 表示是否在子组件之间添加重绘边界，可以提高性能       |
| addSemanticIndexes      | bool                              | 表示是否为语义框架添加语义索引               |
| cacheExtent             | double                            | 指定预加载的区域，可以缓存超出屏幕的子组件         |
| children                | List<Widget>                      | 一个包含子组件的列表                    |
| semanticChildCount      | int                               | 用于指定语义子组件的数量                  |
| dragStartBehavior       | DragStartBehavior                 | 用于确定开始拖动手势的处理方式               |
| keyboardDismissBehavior | ScrollViewKeyboardDismissBehavior | 用于控制键盘如何响应滚动行为                |
| restorationId           | String                            | 用于保存组件的状态并进行恢复                |
| clipBehavior            | Clip                              | 用于指定子组件的裁剪行为                  |

### 用于创建具有固定列宽的网格列表
```text
GridView.extent({
    super.key,
    super.scrollDirection,
    super.reverse,
    super.controller,
    super.primary,
    super.physics,
    super.shrinkWrap,
    super.padding,
    required double maxCrossAxisExtent,
    double mainAxisSpacing = 0.0,
    double crossAxisSpacing = 0.0,
    double childAspectRatio = 1.0,
    bool addAutomaticKeepAlives = true,
    bool addRepaintBoundaries = true,
    bool addSemanticIndexes = true,
    super.cacheExtent,
    List<Widget> children = const <Widget>[],
    int? semanticChildCount,
    super.dragStartBehavior,
    super.keyboardDismissBehavior,
    super.restorationId,
    super.clipBehavior,
  }) 
```

### GridView.extent(...)参数解析
| 参数名称                    | 使用类型                              | 参数介绍                          |
|-------------------------|-----------------------------------|-------------------------------|
| key                     | Key                               | 组件的唯一标识符                      |
| scrollDirection         | Axis                              | 指定滚动的方向                       |
| reverse                 | bool                              | 表示是否反转滚动方向                    |
| controller              | ScrollController                  | 可以用于控制滚动位置和监听滚动事件             |
| primary                 | bool                              | 表示是否将此 GridView 设置为主滚动视图      |
| physics                 | ScrollPhysics                     | 指定滚动行为的滚动物理属性                 |
| shrinkWrap              | bool                              | 表示是否根据子组件的总长度来调整 GridView 的大小 |
| padding                 | EdgeInsetsGeometry                | 表示 GridView 的内边距              |
| maxCrossAxisExtent      | double                            | 必需参数，指定每列的最大宽度                |
| mainAxisSpacing         | double                            | 主轴（垂直方向）上的间距                  |
| crossAxisSpacing        | double                            | 交叉轴（水平方向）上的间距                 |
| childAspectRatio        | double                            | 子项的宽高比，即子项的宽度与高度的比例           |
| addAutomaticKeepAlives  | bool                              | 表示是否在可见范围内自动保持子组件的状态          |
| addRepaintBoundaries    | bool                              | 表示是否在子组件之间添加重绘边界，可以提高性能       |
| addSemanticIndexes      | bool                              | 表示是否为语义框架添加语义索引               |
| cacheExtent             | double                            | 指定预加载的区域，可以缓存超出屏幕的子组件         |
| children                | List<Widget>                      | 一个包含子组件的列表                    |
| semanticChildCount      | int                               | 用于指定语义子组件的数量                  |
| dragStartBehavior       | DragStartBehavior                 | 用于确定开始拖动手势的处理方式               |
| keyboardDismissBehavior | ScrollViewKeyboardDismissBehavior | 用于控制键盘如何响应滚动行为                |
| restorationId           | String                            | 用于保存组件的状态并进行恢复                |
| clipBehavior            | Clip                              | 用于指定子组件的裁剪行为                  |


## GridTile类
### 默认构造函数
```text
GridTile({
    super.key,
    this.header,
    this.footer,
    required this.child,
  })
```

### GridView(...)参数解析
| 参数名称    | 使用类型    | 参数介绍                                                |
|---------|---------|-----------------------------------------------------|
| key     | Key     | 组件的唯一标识符                                            |
| header  | Widget  | 用于在网格项顶部显示一个标题或者其他内容的小部件                            |
| footer  | Widget  | 用于在网格项底部显示一个脚注或者其他内容的小部件                            |
| child   | Widget  |  必需的参数，用于指定网格项中的主要内容，通常是一个子组件，例如 Image、Text 或者其他小部件 |

## GridTileBar类
### 默认构造函数
```text
GridTileBar({
    super.key,
    this.backgroundColor,
    this.leading,
    this.title,
    this.subtitle,
    this.trailing,
  })
```

### GridView(...)参数解析
| 参数名称            | 使用类型    | 参数介绍                            |
|-----------------|---------|---------------------------------|
| key             | Key     | 组件的唯一标识符                        |
| backgroundColor | Color   | 用于设置标题栏的背景颜色                    |
| leading         | Widget  | 用于在标题栏的前面显示一个小部件，通常是一个图标        |
| title           | Widget  | 用于设置标题栏的主标题，通常是一个 Text 小部件      |
| subtitle        | Widget  | 用于设置标题栏的副标题，通常是一个 Text 小部件      |
| trailing        | Widget  | 用于在标题栏的后面显示一个小部件，通常是一个图标或其他装饰内容 |

## Scrollbar类
### 默认构造函数
```text
Scrollbar({
    super.key,
    required this.child,
    this.controller,
    this.thumbVisibility,
    this.trackVisibility,
    this.thickness,
    this.radius,
    this.notificationPredicate,
    this.interactive,
    this.scrollbarOrientation,
    this.isAlwaysShown,
    this.showTrackOnHover,
    this.hoverThickness,
  }) 
```

### Scrollbar(...)参数解析
| 参数名称                  | 使用类型                 | 参数介绍                      |
|-----------------------|----------------------|---------------------------|
| key                   | Key                  | 组件的唯一标识符                  |
| child                 | Widget               | 必需的参数，用于指定要添加滚动条的可滚动组件    |
| controller            | ScrollController     | 用于控制滚动位置和监听滚动事件           |
| thumbVisibility       | bool                 | 表示滚动条拇指（滑块）的可见性           |
| trackVisibility       | bool                 | 表示滚动条轨道的可见性               |
| thickness             | double               | 滚动条的宽度或高度，具体取决于滚动方向       |
| radius                | Radius               | 滚动条的圆角半径                  |
| notificationPredicate | bool                 | 回调函数，用于决定是否应发送滚动条通知       |
| interactive           | bool                 | 表示滚动条是否可交互                |
| scrollbarOrientation  | ScrollbarOrientation | 表示滚动条的方向                  |
| isAlwaysShown         | bool                 | 表示是否始终显示滚动条，即使可滚动组件没有发生滚动 |
| showTrackOnHover      | bool                 | 表示在鼠标悬停时是否显示滚动轨道          |
| hoverThickness        | double               | 悬停时滚动条的宽度或高度              |

## ExpansionPanelList类
### 默认构造函数
```text
ExpansionPanelList({
    super.key,
    this.children = const <ExpansionPanel>[],
    this.expansionCallback,
    this.animationDuration = kThemeAnimationDuration,
    this.expandedHeaderPadding = _kPanelHeaderExpandedDefaultPadding,
    this.dividerColor,
    this.elevation = 2,
    this.expandIconColor,
  }) 
```

### ExpansionPanelList(...)参数解析
| 参数名称                  | 使用类型                 | 参数介绍                                            |
|-----------------------|----------------------|-------------------------------------------------|
| key                   | Key                  | 用于标识ExpansionPanelList                          |
| children              | List<ExpansionPanel> | 包含ExpansionPanel的列表，表示ExpansionPanelList中的可折叠面板 |
| expansionCallback     | Function             | 回调函数，当用户展开或折叠面板时调用                              |
| animationDuration     | Duration             | 用于控制面板展开/折叠动画的持续时间                              |
| expandedHeaderPadding | EdgeInsets           | 表示展开面板时标题部分的内边距                                 |
| dividerColor          | Color                | 表示用于绘制面板之间分隔线的颜色                                |
| elevation             | double               | 表示面板的高度                                         |
| expandIconColor       | Color                | 表示展开图标的颜色                                       |


### 用于创建一组单选的可展开面板，类似于单选框的行为
```text
ExpansionPanelList.radio({
    super.key,
    this.children = const <ExpansionPanelRadio>[],
    this.expansionCallback,
    this.animationDuration = kThemeAnimationDuration,
    this.initialOpenPanelValue,
    this.expandedHeaderPadding = _kPanelHeaderExpandedDefaultPadding,
    this.dividerColor,
    this.elevation = 2,
    this.expandIconColor,
  }) 
```

### ExpansionPanelList.radio(...)参数解析
| 参数名称                  | 使用类型                       | 参数介绍                                                         |
|-----------------------|----------------------------|--------------------------------------------------------------|
| key                   | Key                        | 用于标识ExpansionPanelList.radio                                 |
| children              | *List<ExpansionPanelRadio> | 一个包含ExpansionPanelRadio的列表，表示ExpansionPanelList.radio中的可折叠面板 |
| expansionCallback     | Function                   | 回调函数，当用户展开或折叠面板时调用                                           |
| animationDuration     | Duration                   | 用于控制面板展开/折叠动画的持续时间                                           |
| initialOpenPanelValue | Object                     | 表示默认情况下展开的面板的值                                               |
| expandedHeaderPadding | EdgeInsets                 | 表示展开面板时标题部分的内边距                                              |
| dividerColor          | Color                      | 表示用于绘制面板之间分隔线的颜色                                             |
| elevation             | double                     | 表示面板的高度                                                      |
| expandIconColor       | Color                      | 表示展开图标的颜色                                                    |

> 备注
> * ExpansionPanelRadio是继承于ExpansionPanel的子类

## ExpansionPanel类
### 默认构造函数
```text
ExpansionPanel({
    required this.headerBuilder,
    required this.body,
    this.isExpanded = false,
    this.canTapOnHeader = false,
    this.backgroundColor,
  })
```

### ExpansionPanel(...)参数解析
| 参数名称              | 使用类型     | 参数介绍                                                |
|-------------------|----------|-----------------------------------------------------|
| headerBuilder     | Widget   | 回调函数，该函数接受BuildContext和bool类型的isExpanded参数，并返回一个小部件 |
| body              | Widget   | 表示面板展开时显示的内容部分                                      |
| isExpanded        | bool     | 表示面板是否默认展开                                          |
| canTapOnHeader    | bool     | 表示用户是否可以点击面板的标题来展开或折叠内容                             |
| backgroundColor   | Color    | 表示面板的背景颜色                                           |