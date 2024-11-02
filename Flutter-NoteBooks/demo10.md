# 布局
> * Scaffold：用于实现标准 Material Design 布局结构的主要组件之一。它提供了一个基本的应用程序框架，其中包含了许多常见的应用程序元素，如导航栏、抽屉菜单、底部导航栏、悬浮按钮等，以便您可以快速搭建一个标准的 Material Design 应用程序。
> * Container：用于创建一个矩形容器的小部件。它是一个非常常用的布局容器，允许您创建包裹其他小部件的矩形盒子，并且可以对该盒子进行样式、边距、填充和装饰等设置。
> * BoxConstraints：用于指定矩形框大小限制的类。它可以用来设置容器（如 Container）或其他小部件的尺寸约束，从而控制它们在布局中的大小。
> * Center：用于将其子部件居中显示在其父级容器中。它在水平和垂直方向上都会将子部件居中，并根据子部件的大小来确定其在父级容器中的位置。
> * Column：用于在垂直方向上依次排列其子部件。它将其子部件按照垂直方向从上到下的顺序进行排列，并可以根据需要调整子部件的大小和占用空间。
> * SizedBox：用于创建一个固定大小的空间盒子。它可以用于给子部件指定一个固定的宽度和高度，或者用来添加间距（空白）。
> * Align：用于将其子部件相对于父级容器进行对齐。通过 Align，您可以控制子部件在父级容器中的位置和对齐方式。
> * FractionalOffset：表示了一个相对于矩形尺寸的偏移量，使用小数值来指定相对于矩形宽度和高度的比例。
> * Stack：允许您在重叠的区域放置多个子组件，并根据需要进行定位。
> * IndexedStack：允许您在多个子组件中显示单个子组件。IndexedStack接受一个索引值，并根据该索引值决定哪个子组件可见，其他子组件将处于不可见状态。
> * Row：用于在水平方向上排列多个子组件。
> * Expanded：用于在布局中让子组件填充剩余的可用空间。
> * Flex：用于创建弹性容器的Widget。
> * Flow：用于流式布局的Widget，它可以自动将子组件按照一定规则在水平或垂直方向上进行流式排列。
> * Wrap：用于实现自动换行的布局。
> * Chip：用于显示简短信息的小组件，通常用于标签、标记或选择。
> * Positioned：用于定位子部件的小部件之一。它通常用于 Stack 组件中，用于指定子部件的位置和尺寸。
> * Flexible：用于布局的一个小部件，它允许子控件在主轴方向上占用可用空间的灵活性。
> * ConstrainedBox：用于定义对子组件的约束条件。你可以设置最小宽度、最大宽度、最小高度和最大高度。
> * UnconstrainedBox：用于移除其子组件的约束。这意味着，子组件可以超出父组件设定的大小限制，进而自定义其宽度和高度。
> * AspectRatio：用于按照特定的宽高比来调整子组件的尺寸。它允许你在布局中保持某个组件的特定形状，无论其父组件的大小如何变化。
> * Padding：用于在子 Widget 周围添加内边距的 Widget。


## Scaffold类
```text
Scaffold({
    super.key,
    this.appBar,
    this.body,
    this.floatingActionButton,
    this.floatingActionButtonLocation,
    this.floatingActionButtonAnimator,
    this.persistentFooterButtons,
    this.persistentFooterAlignment = AlignmentDirectional.centerEnd,
    this.drawer,
    this.onDrawerChanged,
    this.endDrawer,
    this.onEndDrawerChanged,
    this.bottomNavigationBar,
    this.bottomSheet,
    this.backgroundColor,
    this.resizeToAvoidBottomInset,
    this.primary = true,
    this.drawerDragStartBehavior = DragStartBehavior.start,
    this.extendBody = false,
    this.extendBodyBehindAppBar = false,
    this.drawerScrimColor,
    this.drawerEdgeDragWidth,
    this.drawerEnableOpenDragGesture = true,
    this.endDrawerEnableOpenDragGesture = true,
    this.restorationId,
  })
```

### Scaffold(...)参数解析
| 参数名称                           | 使用类型                         | 参数介绍                                    |
|--------------------------------|------------------------------|-----------------------------------------|
| key                            | Key                          | 用于标识 Scaffold                           |
| appBar                         | PreferredSizeWidget          | 顶部导航栏的小部件，通常使用AppBar                    |
| body                           | Widget                       | 主要内容区域的小部件，用于放置应用程序的主要内容                |
| floatingActionButton           | Widget                       | 悬浮按钮的小部件                                |
| floatingActionButtonLocation   | FloatingActionButtonLocation | 悬浮按钮的位置                                 |
| floatingActionButtonAnimator   | FloatingActionButtonAnimator | 悬浮按钮动画控制器                               |
| persistentFooterButtons        | List<Widget>                 | 位于 body 下方的持续显示的按钮列表                    |
| persistentFooterAlignment      | AlignmentDirectional         | 持续按钮的对齐方式                               |
| drawer                         | Widget                       | 抽屉菜单的小部件，通常使用 Drawer                    |
| onDrawerChanged                | Function                     | 抽屉菜单状态变化时的回调函数                          |
| endDrawer                      | Widget                       | 右侧抽屉菜单的小部件                              |
| onEndDrawerChanged             | Function                     | 右侧抽屉菜单状态变化时的回调函数                        |
| bottomNavigationBar            | Widget                       | 底部导航栏的小部件                               |
| bottomSheet                    | Widget                       | 底部弹出的小部件                                |
| backgroundColor                | Color                        | 背景颜色                                    |
| resizeToAvoidBottomInset       | bool                         | 用于控制是否在键盘弹出时调整内容大小以避免被底部键盘遮挡。           |
| primary                        | bool                         | 用于指示是否为主滚动视图                            |
| drawerDragStartBehavior        | DragStartBehavior            | 抽屉菜单的拖动行为起始位置                           |
| extendBody                     | bool                         | 用于控制是否将内容（body 部分）延伸到导航栏、底部导航栏和悬浮按钮的下方。 |
| extendBodyBehindAppBar         | bool                         | 用于控制是否将内容（body 部分）延伸到导航栏（appBar）的背后。    |
| drawerScrimColor               | Color                        | 抽屉菜单背景遮罩的颜色                             |
| drawerEdgeDragWidth            | double                       | 抽屉菜单从屏幕边缘拖拽打开的宽度                        |
| drawerEnableOpenDragGesture    | bool                         | 用于控制是否允许通过拖动手势来打开左侧抽屉菜单（drawer）         |
| endDrawerEnableOpenDragGesture | bool                         | 用于控制是否允许通过拖动手势来打开右侧抽屉菜单（endDrawer）      |
| restorationId                  | bool                         | 用于存储和恢复 Scaffold 的状态的标识符                |

## Container类
### 默认构造函数
```text
Container({
    super.key,
    this.alignment,
    this.padding,
    this.color,
    this.decoration,
    this.foregroundDecoration,
    double? width,
    double? height,
    BoxConstraints? constraints,
    this.margin,
    this.transform,
    this.transformAlignment,
    this.child,
    this.clipBehavior = Clip.none,
  })
```

### Container(...)参数解析
| 参数名称                 | 使用类型                     | 参数介绍                        |
|----------------------|--------------------------|-----------------------------|
| key                  | Key                      | 用于标识 Container              |
| alignment            | AlignmentGeometry        | 指定子小部件在容器内的对齐方式             |
| padding              | EdgeInsetsGeometry       | 定义容器的内边距（即子小部件与容器边缘之间的空白区域） |
| color                | Color                    | 定义容器的背景颜色                   |
| decoration           | Decoration               | 定义容器的装饰，如边框、圆角、阴影等          |
| foregroundDecoration | Decoration               | 定义容器的前景装饰，它位于子小部件之上         |
| width                | double                   | 定义容器的宽度                     |
| height               | double                   | 定义容器的高度                     |
| constraints          | BoxConstraints           | 定义容器的限制条件，如最小宽高、最大宽高等       |
| margin               | EdgeInsetsGeometry       | 定义容器的外边距（即容器与其父级小部件之间的空白区域） |
| transform            | Matrix4                  | 定义容器的变换矩阵，用于实现平移、旋转、缩放等变换效果 |
| transformAlignment   | AlignmentGeometry        | 定义变换矩阵的对齐方式                 |
| child                | Widget                   | 容器中要显示的子小部件                 |
| clipBehavior         | Clip                     | 定义对子小部件的裁剪方式                |

## BoxConstraints类
### 默认构造函数
```text
BoxConstraints({
    this.minWidth = 0.0,
    this.maxWidth = double.infinity,
    this.minHeight = 0.0,
    this.maxHeight = double.infinity,
  })
```

### BoxConstraints类(...)参数解析
| 参数名称       | 使用类型      | 参数介绍      |
|------------|-----------|-----------|
| minWidth   | double    | 限制框的最小宽度  |
| maxWidth   | double    | 限制框的最大宽度  |
| minHeight  | double    | 限制框的最小高度  |
| maxHeight  | double    | 限制框的最大高度  | 

### 用于创建一个特定尺寸的严格约束
```text
BoxConstraints.tight(Size size)
```

### BoxConstraints.tight(...)参数解析
| 参数名称   | 使用类型  | 参数介绍                                                         |
|--------|-------|--------------------------------------------------------------|
| size   | Size  | 传入一个Size对象，用于表示一个矩形的尺寸。它由两个属性组成——width 和 height，分别表示矩形的宽度和高度 |

### 用于创建一个特定宽度和高度的严格约束
```text
BoxConstraints.tightFor({
    double? width,
    double? height,
  })
```

### BoxConstraints.tightFor(...)参数解析
| 参数名称     | 使用类型    | 参数介绍                        |
|----------|---------|-----------------------------|
| width    | double  | 指定宽度的值，可以是一个非负的 double 类型数值 |
| height   | double  | 指定高度的值，可以是一个非负的 double 类型数值 |

### 用于创建一个具有有限宽度和高度的严格约束
```text
BoxConstraints.tightForFinite({
    double width = double.infinity,
    double height = double.infinity,
})
```

### BoxConstraints.tightForFinite(...)参数解析
| 参数名称     | 使用类型    | 参数介绍                                                         |
|----------|---------|--------------------------------------------------------------|
| width    | double  | 指定宽度的值，可以是一个非负的有限的 double 类型数值，默认值为 double.infinity，表示宽度没有限制 |
| height   | double  | 指定高度的值，可以是一个非负的有限的 double 类型数值，默认值为 double.infinity，表示高度没有限制 |

### 用于创建一个宽松约束
```text
BoxConstraints.loose(Size size)
```

### BoxConstraints.loose(...)参数解析
| 参数名称   | 使用类型  | 参数介绍                                                         |
|--------|-------|--------------------------------------------------------------|
| size   | Size  | 传入一个Size对象，用于表示一个矩形的尺寸。它由两个属性组成——width 和 height，分别表示矩形的宽度和高度 |

### 用于创建一个扩展约束
```text
BoxConstraints.expand({
    double? width,
    double? height,
  })
```

### BoxConstraints.expand(...)参数解析
| 参数名称     | 使用类型    | 参数介绍                                                 |
|----------|---------|------------------------------------------------------|
| width    | double  | 扩展的宽度，可以是一个非负的 double 类型数值，如果未指定，则宽度将尽可能地填充父级容器的可用宽度 |
| height   | double  | 扩展的高度，可以是一个非负的 double 类型数值，如果未指定，则高度将尽可能地填充父级容器的可用高度 |

## Center类
### 默认构造函数
```text
Center({ 
    super.key, 
    super.widthFactor, 
    super.heightFactor,
     super.child 
 })
```

### Center(...)参数解析
| 参数名称         | 使用类型    | 参数介绍                  |
|--------------|---------|-----------------------|
| key          | Key     | 用于控制小部件的唯一标识符         |
| widthFactor  | double  | 表示子部件宽度相对于父级容器宽度的因子   |
| heightFactor | double  | 表示子部件高度相对于父级容器高度的因子   |
| child        | Widget  | 表示放置在 Center 中心的子部件   |

## Column类
### 默认构造函数
```text
Column({
    super.key,
    super.mainAxisAlignment,
    super.mainAxisSize,
    super.crossAxisAlignment,
    super.textDirection,
    super.verticalDirection,
    super.textBaseline,
    super.children,
  })
```

### Column(...)参数解析
| 参数名称               | 使用类型               | 参数介绍                  |
|--------------------|--------------------|-----------------------|
| key                | Key                | 用于控制小部件的唯一标识符         |
| mainAxisAlignment  | MainAxisAlignment  | 表示子部件在主轴（垂直方向）上的对齐方式  |
| mainAxisSize       | MainAxisSize       | 表示 Column 在主轴上的尺寸大小   |
| crossAxisAlignment | CrossAxisAlignment | 表示子部件在交叉轴（水平方向）上的对齐方式 |
| textDirection      | TextDirection      | 表示子部件的文本方向            |
| verticalDirection  | VerticalDirection  | 表示子部件的排列方向            |
| textBaseline       | TextBaseline       | 表示子部件的基线对齐方式          |
| children           | List<Widget>       | 包含要放置在 Column 中的子部件列表 |

## SizedBox类
### 默认构造参函数
```text
SizedBox({
    super.key, 
    this.width,
    this.height,
    super.child 
})
```

### SizedBox(...)参数解析
| 参数名称    | 使用类型    | 参数介绍                 |
|---------|---------|----------------------|
| key     | Key     | 用于控制小部件的唯一标识符        |
| width   | double  | 用于指定 SizedBox 的宽度    |
| height  | double  | 用于指定 SizedBox 的高度    |
| child   | Widget  | 表示放置在 SizedBox 中的子部件 |

### 用于创建一个可以尽可能地填充父级容器的SizedBox
```text
SizedBox.expand({ 
    super.key,
    super.child 
    })
```

### SizedBox.expand(...)参数解析
| 参数名称  | 使用类型   | 参数介绍                        |
|-------|--------|-----------------------------|
| key   | Key    | 用于控制小部件的唯一标识符               |
| child | Widget | 表示放置在 SizedBox.expand 中的子部件 |

### 创建一个将在父控件框允许的范围内变小的框
```text
SizedBox.shrink({ 
    super.key,
    super.child 
    })
```

### SizedBox.shrink(...)参数解析
| 参数名称  | 使用类型   | 参数介绍                        |
|-------|--------|-----------------------------|
| key   | Key    | 用于控制小部件的唯一标识符               |
| child | Widget | 表示放置在 SizedBox.expand 中的子部件 |


### 用于根据指定的大小来创建
```text
SizedBox.fromSize({ 
    super.key, 
    super.child,
    Size? size 
    })
```

### SizedBox.fromSize(...)参数解析
| 参数名称   | 使用类型   | 参数介绍                          |
|--------|--------|-------------------------------|
| key    | Key    | 用于控制小部件的唯一标识符                 |
| child  | Widget | 表示放置在 SizedBox.fromSize 中的子部件 |
| size   | Size   | 表示希望 SizedBox 拥有的大小           |

### 用于创建一个正方形的样式
```text
SizedBox.square({
    super.key,
    super.child, 
    double? dimension
 })
```

### SizedBox.square(...)参数解析
| 参数名称        | 使用类型    | 参数介绍                        |
|-------------|---------|-----------------------------|
| key         | Key     | 用于控制小部件的唯一标识符               |
| child       | Widget  | 表示放置在 SizedBox.square 中的子部件 |
| dimension   | double  | 用于指定正方形的边长                  |

## Align类
### 默认构造函数
```text
Align({
    super.key,
    this.alignment = Alignment.center,
    this.widthFactor,
    this.heightFactor,
    super.child,
  }) 
```

### Align(...)参数解析
| 参数名称         | 使用类型              | 参数介绍                |
|--------------|-------------------|---------------------|
| key          | Key               | 用于控制小部件的唯一标识符       |
| alignment    | AlignmentGeometry | 表示子部件在父级容器中的对齐方式    |
| widthFactor  | double            | 表示子部件宽度相对于父级容器宽度的因子 |
| heightFactor | double            | 表示子部件高度相对于父级容器高度的因子 |
| child        | Widget            | 表示放置在 Align 中的子部件   |

## FractionalOffset类
### 默认构造函数
```text
FractionalOffset(double dx, double dy)
```

### FractionalOffset(...)参数解析
| 参数名称 | 使用类型    | 参数介绍                           |
|------|---------|--------------------------------|
| dx   | double  | 表示相对于矩形宽度的偏移量，取值范围为 -1.0 到 1.0 |
| dy   | double  | 表示相对于矩形高度的偏移量，取值范围为 -1.0 到 1.0 |

### 根据给定的偏移量和尺寸创建
```text
FractionalOffset.fromOffsetAndSize(Offset offset, Size size)
```

### FractionalOffset.fromOffsetAndSize(...)参数解析
| 参数名称   | 使用类型   | 参数介绍        |
|--------|--------|-------------|
| offset | Offset | 表示相对于矩形的偏移量 |
| size   | Size   | 表示矩形的尺寸     |

### 根据给定的偏移量和矩形范围创建
```text
FractionalOffset.fromOffsetAndRect(Offset offset, Rect rect)
```

### FractionalOffset.fromOffsetAndRect(...)参数解析
| 参数名称    | 使用类型    | 参数介绍        |
|---------|---------|-------------|
| offset  | Offset  | 表示相对于矩形的偏移量 |
| rect    | Rect    | 传入一个矩形范围    |

## Stack类
### 默认构造函数
```text
Stack({
    super.key,
    this.alignment = AlignmentDirectional.topStart,
    this.textDirection,
    this.fit = StackFit.loose,
    this.clipBehavior = Clip.hardEdge,
    super.children,
  })
```

### Stack(...)参数解析
| 参数名称          | 使用类型              | 参数介绍                               |
|---------------|-------------------|------------------------------------|
| key           | Key               | 这是继承自父类的key属性，用于在Widget树中唯一标识Stack |
| alignment     | AlignmentGeometry | 用于控制子组件在Stack中的对齐方式                |
| textDirection | TextDirection     | 用于指定文本方向，影响alignment参数的解释          |
| fit           | StackFit          | 用于控制子组件在Stack中的大小调整方式              |
| clipBehavior  | Clip              | 用于控制子组件在Stack范围外的裁剪行为              |
| children      | List<Widget>      | 用于传递Stack的子组件列表                    |

## IndexedStack类
### 默认构造函数
```text
IndexedStack({
    super.key,
    this.alignment = AlignmentDirectional.topStart,
    this.textDirection,
    this.clipBehavior = Clip.hardEdge,
    this.sizing = StackFit.loose,
    this.index = 0,
    this.children = const <Widget>[],
  })
```

### IndexedStack(...)参数解析
| 参数名称          | 使用类型              | 参数介绍                         |
|---------------|-------------------|------------------------------|
| key           | Key               | 用于在Widget树中唯一标识IndexedStack  |
| alignment     | AlignmentGeometry | 用于控制子组件在IndexedStack中的对齐方式   |
| textDirection | TextDirection     | 用于指定文本方向，影响alignment参数的解释    |
| clipBehavior  | Clip              | 用于控制子组件在IndexedStack范围外的裁剪行为 |
| sizing        | StackFit          | 用于控制子组件在IndexedStack中的大小调整方式 |
| index         | int               | 必需的参数，用于指定当前应该显示的子组件的索引      |
| children      | List<Widget>      | 这些子组件将在IndexedStack中进行切换显示   |

## Row类
### 默认构造函数
```text
Row({
    super.key,
    super.mainAxisAlignment,
    super.mainAxisSize,
    super.crossAxisAlignment,
    super.textDirection,
    super.verticalDirection,
    super.textBaseline, // NO DEFAULT: we don't know what the text's baseline should be
    super.children,
  })
```

### Row(...)类
| 参数名称               | 使用类型               | 参数介绍                                                   |
|--------------------|--------------------|--------------------------------------------------------|
| key                | Key                | 这是继承自父类的key属性，用于在Widget树中唯一标识Row                       |
| mainAxisAlignment  | MainAxisAlignment  | 这是继承自父类的mainAxisAlignment属性，用于控制子组件在主轴方向（水平方向）上的对齐方式   |
| mainAxisSize       | MainAxisSize       | 这是继承自父类的mainAxisSize属性，用于控制Row在主轴方向上的大小                |
| crossAxisAlignment | CrossAxisAlignment | 这是继承自父类的crossAxisAlignment属性，用于控制子组件在交叉轴方向（垂直方向）上的对齐方式 |
| textDirection      | TextDirection      | 这是继承自父类的textDirection属性，用于指定文本方向，影响子组件的排列方向            |
| verticalDirection  | VerticalDirection  | 这是继承自父类的verticalDirection属性，用于控制子组件在交叉轴方向上的顺序          |
| textBaseline       | TextBaseline       | 这是继承自父类的textBaseline属性，用于指定基线对齐方式                      |
| children           | List<Widget>       | 这是继承自父类的children属性，用于传递Row的子组件列表                       |

## Expanded类
### 默认构造函数
```text
Expanded({
    super.key,
    super.flex,
    required super.child,
  }) 
```

### Expanded(...)参数解析
| 参数名称   | 使用类型    | 参数介绍                    |
|--------|---------|-------------------------|
| key    | Key     | 用于在Widget树中唯一标识Expanded |
| flex   | int     | 用于指定Expanded在可用空间中的分配比例 |
| child  | Widget  | 用于指定Expanded的子组件        |

## Flex类
### 默认构造函数
```text
Flex({
    super.key,
    required this.direction,
    this.mainAxisAlignment = MainAxisAlignment.start,
    this.mainAxisSize = MainAxisSize.max,
    this.crossAxisAlignment = CrossAxisAlignment.center,
    this.textDirection,
    this.verticalDirection = VerticalDirection.down,
    this.textBaseline, // NO DEFAULT: we don't know what the text's baseline should be
    this.clipBehavior = Clip.none,
    super.children,
  }) 
```

### Flex(...)参数解析
| 参数名称               | 使用类型               | 参数介绍                 |
|--------------------|--------------------|----------------------|
| key                | Key                | 用于在Widget树中唯一标识Flex  |
| direction          | Axis               | 必需的参数，用于指定Flex的主轴方向  |
| mainAxisAlignment  | MainAxisAlignment  | 用于控制子组件在主轴方向上的对齐方式   |
| mainAxisSize       | MainAxisSize       | 用于控制Flex在主轴方向上的大小    |
| crossAxisAlignment | CrossAxisAlignment | 用于控制子组件在交叉轴方向上的对齐方式  |
| textDirection      | TextDirection      | 用于指定文本方向，影响子组件的排列方向  |
| verticalDirection  | VerticalDirection  | 用于控制子组件在交叉轴方向上的顺序    |
| textBaseline       | TextBaseline       | 用于指定基线对齐方式           |
| clipBehavior       | Clip               | 用于控制子组件在Flex范围外的裁剪行为 |
| children           | List<Widget>       | 用于传递Flex的子组件列表       |

## Flow类
### 默认构造函数
```text
Flow({
    super.key,
    required this.delegate,
    List<Widget> children = const <Widget>[],
    this.clipBehavior = Clip.hardEdge,
  }) 
```

### Flow(...)参数解析
| 参数名称         | 使用类型          | 参数介绍                  |
|--------------|---------------|-----------------------|
| key          | Key           | 用于在Widget树中唯一标识Flow   |
| delegate     | FlowDelegate  | 必需的参数，用于指定Flow的布局规则   |
| children     | List<Widget>  | 用于传递Flow的子组件列表        |
| clipBehavior | Clip          | 用于控制子组件在Flow范围外的裁剪行为  |

### 用于创建一个非包裹的流式布局
```text
Flow.unwrapped({
    super.key,
    required this.delegate,
    super.children,
    this.clipBehavior = Clip.hardEdge,
  });
```

### Flow.unwrapped(...)参数解析
| 参数名称          | 使用类型         | 参数介绍                           |
|---------------|--------------|--------------------------------|
| key           | Key          | 用于在Widget树中唯一标识                |
| delegate      | FlowDelegate | 必需的参数，用于指定布局规则                 |
| children      | List<Widget> | 用于传递Flow.unwrapped的子组件列表       |
| clipBehavior  | Clip         | 用于控制子组件在Flow.unwrapped范围外的裁剪行为 |

## Wrap类
### 默认构造函数
```text
Wrap({
    super.key,
    this.direction = Axis.horizontal,
    this.alignment = WrapAlignment.start,
    this.spacing = 0.0,
    this.runAlignment = WrapAlignment.start,
    this.runSpacing = 0.0,
    this.crossAxisAlignment = WrapCrossAlignment.start,
    this.textDirection,
    this.verticalDirection = VerticalDirection.down,
    this.clipBehavior = Clip.none,
    super.children,
  })
```

### Wrap(...)参数解析
| 参数名称               | 使用类型                 | 参数介绍                      |
|--------------------|----------------------|---------------------------|
| key                | Key                  | Widget的唯一标识符，用于在树中唯一标识该组件 |
| direction          | Axis                 | 设置子组件的排列方向                |
| alignment          | WrapAlignment        | 设置子组件在主轴（水平或垂直）上的对齐方式     |
| spacing            | double               | 设置子组件在主轴方向上的间距            |
| runAlignment       | WrapAlignment        | 设置子组件在交叉轴（与主轴垂直的方向）上的对齐方式 |
| runSpacing         | double               | 设置子组件在交叉轴方向上的间距           |
| crossAxisAlignment |   WrapCrossAlignment | 设置子组件在交叉轴方向上的对齐方式         |
| textDirection      | TextDirection        | 设置文本方向                    |
| verticalDirection  | VerticalDirection    | 设置子组件在垂直方向的对齐方式           |
| clipBehavior       | Clip                 | 定义如何剪辑超出容器边界的内容           |
| children           | List<Widget>         | 要在 Wrap 中显示的子组件列表         |

## Chip类
### 默认构造函数
```text
Chip({
    super.key,
    this.avatar,
    required this.label,
    this.labelStyle,
    this.labelPadding,
    this.deleteIcon,
    this.onDeleted,
    this.deleteIconColor,
    this.deleteButtonTooltipMessage,
    this.side,
    this.shape,
    this.clipBehavior = Clip.none,
    this.focusNode,
    this.autofocus = false,
    this.backgroundColor,
    this.padding,
    this.visualDensity,
    this.materialTapTargetSize,
    this.elevation,
    this.shadowColor,
    this.surfaceTintColor,
    this.iconTheme,
    this.useDeleteButtonTooltip = true,
  }) 
```

### Chip(...)参数解析
| 参数名称                       | 使用类型                  | 参数介绍                          |
|----------------------------|-----------------------|-------------------------------|
| key                        | Key                   | 用于唯一标识该组件                     |
| avatar                     | Widget                | 在 Chip 左侧显示的小组件，通常用于显示一个图标或头像 |
| label                      | Widget                | Chip 的文本标签，是一个必需参数，用于显示主要内容   |
| labelStyle                 | TextStyle             | 用于设置 label 的样式                |
| labelPadding               | EdgeInsetsGeometry    | 文本标签的内边距                      |
| deleteIcon                 | Widget                | 在 Chip 右侧显示的删除图标              |
| onDeleted                  | Function              | 当删除图标被点击时的回调函数                |
| deleteIconColor            | Color                 | 删除图标的颜色                       |
| deleteButtonTooltipMessage | String                | 删除按钮的提示信息                     |
| side                       | BorderSide            | Chip 组件周围的边框样式                |
| shape                      | OutlinedBorder        | Chip 的形状，可以是圆形或矩形             |
| clipBehavior               | Clip                  | 定义如何剪辑超出 Chip 边界的内容           |
| focusNode                  | FocusNode             | 聚焦节点，用于处理焦点事件                 |
| autofocus                  | bool                  | 是否自动聚焦                        |
| backgroundColor            | Color                 | Chip 的背景颜色                    |
| padding                    | EdgeInsetsGeometry    | 内边距                           |
| visualDensity              | VisualDensity         | 视觉密度                          |
| materialTapTargetSize      | MaterialTapTargetSize | Material风格的点击目标大小             |
| elevation                  | double                | Chip 的阴影高度                    |
| shadowColor                | Color                 | 阴影颜色                          |
| surfaceTintColor           | Color                 | 表面颜色                          |
| iconTheme                  | IconThemeData         | 图标主题                          |
| useDeleteButtonTooltip     | bool                  | 标记是否使用删除按钮的工具提示               |

## Positioned类
### 默认构造函数
```text
Positioned({
    super.key,
    this.left,
    this.top,
    this.right,
    this.bottom,
    this.width,
    this.height,
    required super.child,
  })
```

### Positioned(...)参数解析
| 参数名称    | 使用类型    | 参数介绍            |
|---------|---------|-----------------|
| key     | Key     | 用于在树中唯一标识该组件    |
| left    | double  | 子部件相对于左边缘的偏移量   |
| top     | double  | 子部件相对于顶部边缘的偏移量  |
| right   | double  | 子部件相对于右边缘的偏移量   |
| bottom  | double  | 子部件相对于底部边缘的偏移量  |
| width   | double  | 子部件的宽度          |
| height  | double  | 子部件的高度          |
| child   | Widget  | 要定位的子部件，是一个必需参数 |

### 用于通过矩形区域来定位子部件。
```text
Positioned.fromRect({
    super.key,
    required Rect rect,
    required super.child,
}) 
```

### Positioned.fromRect(...)参数解析
| 参数名称   | 使用类型    | 参数介绍                              |
|--------|---------|-----------------------------------|
| key    | Key     | 用于在树中唯一标识该组件                      |
| rect   | Rect    | 一个 Rect 对象，用于指定子部件在 Stack 中的位置和大小 |
| child  | Widget  | 要定位的子部件，是一个必需参数                   |

### 相对于父容器来定位子部件
```text
Positioned.fromRelativeRect({
    super.key,
    required RelativeRect rect,
    required super.child,
  })
```

### Positioned.fromRelativeRect(...)参数解析
| 参数名称    | 使用类型         | 参数介绍                                    |
|---------|--------------|-----------------------------------------|
| key     | Key          | 用于在树中唯一标识该组件                            |
| rect    | RelativeRect | 一个 RelativeRect 对象，用于指定子部件在父容器中的相对位置和大小 |
| child   | Widget       | 要定位的子部件，是一个必需参数                         |

### 允许子部件填充父容器的所有可用空间
```text
Positioned.fill({
    super.key,
    this.left = 0.0,
    this.top = 0.0,
    this.right = 0.0,
    this.bottom = 0.0,
    required super.child,
  })
```

### Positioned.fill(...)参数解析
| 参数名称    | 使用类型    | 参数介绍            |
|---------|---------|-----------------|
| key     | Key     | 用于在树中唯一标识该组件    |
| left    | double  | 子部件相对于左边缘的偏移量   |
| top     | double  | 子部件相对于顶部边缘的偏移量  |
| right   | double  | 子部件相对于右边缘的偏移量   |
| bottom  | double  | 子部件相对于底部边缘的偏移量  |
| child   | Widget  | 要定位的子部件，是一个必需参数 |

### 通过给定的TextDirection来相对于父容器定位子部件
```text
Positioned.directional({
    Key? key,
    required TextDirection textDirection,
    double? start,
    double? top,
    double? end,
    double? bottom,
    double? width,
    double? height,
    required Widget child,
  }) 
```

### Positioned.directional(...)参数解析
| 参数名称          | 使用类型          | 参数介绍                     |
|---------------|---------------|--------------------------|
| key           | Key           | 用于在树中唯一标识该组件             |
| textDirection | TextDirection | 指定子部件相对于父容器的文本方向，是一个必需参数 |
| start         | double        | 子部件相对于起始边缘的偏移量           |
| top           | double        | 子部件相对于顶部边缘的偏移量           |
| end           | double        | 子部件相对于结束边缘的偏移量           |
| bottom        | double        | 子部件相对于底部边缘的偏移量           |
| width         | double        | 子部件的宽度                   |
| height        | double        | 子部件的高度                   |
| child         | Widget        | 要定位的子部件，是一个必需参数          |

## Flexible类
### 默认构造函数
```text
Flexible({
    super.key,
    this.flex = 1,
    this.fit = FlexFit.loose,
    required super.child,
  })
```

### Flexible(...)参数解析
| 参数名称    | 使用类型    | 参数介绍                       |
|---------|---------|----------------------------|
| key     | Key     | 用于在树中唯一标识该组件               |
| flex    | int     | 决定该控件在主轴方向上所占的比例           |
| fit     | FlexFit | 决定子控件如何适应可用空间              |
| child   | Widget  | 必需参数，指定要在 Flexible 中显示的子控件 |

## ConstrainedBox类
### 默认构造函数
```text
ConstrainedBox({
    super.key,
    required this.constraints,
    super.child,
  })
```

### ConstrainedBox(...)参数解析
| 参数名称        | 使用类型           | 参数介绍                                                                       |
|-------------|----------------|----------------------------------------------------------------------------|
| key         | Key            | 用于在树中唯一标识该组件                                                               |
| constraints | BoxConstraints | 用于定义对子组件的约束条件。你可以设置最小宽度、最大宽度、最小高度和最大高度。通过传入 BoxConstraints 对象，可以灵活控制子组件的尺寸 |
| child       | Widget         | ConstrainedBox的子组件                                                         |

## UnconstrainedBox类
### 默认构造函数
```text
UnconstrainedBox({
    super.key,
    this.child,
    this.textDirection,
    this.alignment = Alignment.center,
    this.constrainedAxis,
    this.clipBehavior = Clip.none,
  })
```

### UnconstrainedBox(...)参数解析
| 参数名称            | 使用类型              | 参数介绍                                                                     |
|-----------------|-------------------|--------------------------------------------------------------------------|
| key             | Key               | 用于标识组件的唯一值，主要用于在组件树中查找和控制特定组件实例                                          |
| child           | Widget            | UnconstrainedBox的子组件，表示将要展示的内容。该组件可以自由扩展，不受父组件约束的影响                      |
| textDirection   | TextDirection     | 用于指定文本方向                                                                 |
| alignment       | AlignmentGeometry | 定义子组件在 UnconstrainedBox 内的对齐方式                                           |
| constrainedAxis | Axis              | 指定限制的轴方向。这个参数可以帮助决定在水平或垂直方向上施加约束。如果不设置，UnconstrainedBox 将允许子组件在所有方向上自由扩展 |
| clipBehavior    | Clip              | 定义如何处理超出 UnconstrainedBox 边界的内容                                          |

## AspectRatio类
### 默认构造函数
```text
AspectRatio({
    super.key,
    required this.aspectRatio,
    super.child,
  })
```

### AspectRatio(...)参数解析
| 参数名称        | 使用类型   | 参数介绍                            |
|-------------|--------|---------------------------------|
| key         | Key    | 用于标识组件的唯一值，主要用于在组件树中查找和控制特定组件实例 |
| aspectRatio | double | 指定宽高比。宽高比是一个浮点数，表示组件的宽度与高度之比    |
| child       | Widget | 需要应用宽高比的子组件                     |

## Padding类
### 默认构造函数
```text
Padding({
    super.key,
    required this.padding,
    super.child,
  })
```

### Padding(...)参数解析
| 参数名称      | 使用类型                | 参数介绍                           |
|-----------|---------------------|--------------------------------|
| key       | Key                 | 用于标识 Widget 的可选参数              |
| padding   | EdgeInsetsGeometry  | 一个 EdgeInsets 对象，用于定义内边距的大小和方向 |
| child     | Widget              | 要添加内边距的子 Widget                |

> 注：EdgeInsetsGeometry是一个抽象类，我们一般都使用其子类EdgeInsets
