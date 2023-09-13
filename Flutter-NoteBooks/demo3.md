# Button控件
> Flutter3.0提供了以下的按钮
> * ElevatedButton（替换了之前的RaisedButton）：ElevatedButton是Flutter中的一个内置按钮小部件，用于创建具有升起效果的按钮。
> * TextButton（替换了之前的FlatButton）：一个平面的、带有文本的按钮。
> * OutlinedButton：一个带有边框的按钮。
> * ToggleButtons：一个用于切换状态的按钮组，可以同时选择多个选项。
> * FloatingActionButton：用于创建一个浮动操作按钮。
> * IconButton：一个带有图标的按钮。
> * CupertinoButton：一个iOS风格的按钮，具有半透明的背景和圆角。
> * Switch：用于显示开关控件的小部件。它提供了一个交互式的开关按钮，用于切换两个状态（开或关）。
> * Checkbox：用于显示复选框的小部件。
> * DropdownButton：用于显示下拉菜单的控件，它允许用户从一个选项列表中选择一个值。

## ElevatedButton类
### 默认构造函数
```text
ElevatedButton({
    super.key,
    required super.onPressed,
    super.onLongPress,
    super.onHover,
    super.onFocusChange,
    super.style,
    super.focusNode,
    super.autofocus = false,
    super.clipBehavior = Clip.none,
    super.statesController,
    required super.child,
  })
```

### ElevatedButton(...)参数解析
| 参数名称             | 使用类型                     | 参数介绍                                                                                                                                                 |
|------------------|--------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------|
| key              | Key                      | 用于指定widget的唯一标识符的键（Key）。通常用于在更新widget时进行识别和比较。                                                                                                       |
| onPressed        | Function                 | 必需的回调函数，当按钮被按下时会触发该回调。                                                                                                                               |
| onLongPress      | Function                 | 长按按钮时触发的回调函数。                                                                                                                                        |
| onHover          | Function                 | 鼠标悬停在按钮上时触发的回调函数。                                                                                                                                    |
| onFocusChange    | Function                 | 获取或失去焦点时触发的回调函数。                                                                                                                                     |
| style            | ButtonStyle              | 按钮的样式，可以自定义按钮的外观。                                                                                                                                    |
| focusNode        | FocusNode                | 管理按钮的焦点状态的FocusNode。                                                                                                                                 |
| autofocus        | bool                     | 是否自动获取焦点。                                                                                                                                            |
| clipBehavior     | Clip                     | 内容超出按钮边界时的剪裁行为。                                                                                                                                      |
| statesController | MaterialStatesController | 控制按钮的状态，例如禁用按钮。                                                                                                                                      |
| child            | List<Widget>             | 按钮的子widget，child可以是任何Widget类型，例如Text、Icon、Image、Container等等。你可以通过child参数来自定义按钮的外观和行为，例如更改按钮的标签文本、添加图标、更改按钮的颜色等等                                      |

### 创建带有图标的ElevatedButton的构造函数
```text
ElevatedButton.icon({
    Key? key,
    required VoidCallback? onPressed,
    VoidCallback? onLongPress,
    ValueChanged<bool>? onHover,
    ValueChanged<bool>? onFocusChange,
    ButtonStyle? style,
    FocusNode? focusNode,
    bool? autofocus,
    Clip? clipBehavior,
    MaterialStatesController? statesController,
    required Widget icon,
    required Widget label,
  })
```

### ElevatedButton.icon(...)参数解析
| 参数名称             | 使用类型                     | 参数介绍                                                     |
|------------------|--------------------------|----------------------------------------------------------|
| key              | Key                      | 用于识别Widget的可选键。如果没有提供，则会自动生成一个。                          |
| onPressed        | Function                 | 当按钮被点击时调用的回调函数。它是必需的参数。                                  |
| onLongPress      | Function                 | 当按钮被长按时调用的回调函数。                                          |
| onHover          | Function                 | 当按钮被鼠标悬停在上方时调用的回调函数。                                     |
| onFocusChange    | Function                 | 当按钮的焦点状态改变时调用的回调函数。                                      |
| style            | ButtonStyle              | 定义按钮的样式，例如背景颜色、文本样式等。如果未提供，则使用默认样式。                      |
| focusNode        | FocusNode                | 按钮的焦点节点。                                                 |
| autofocus        | bool                     | 指定按钮是否自动获取焦点。                                            |
| clipBehavior     | Clip                     | 指定按钮的裁剪行为。                                               |
| statesController | MaterialStatesController | 状态控制器，用于自定义按钮在不同状态下的样式。                                  |
| icon             | Widget                   | 显示在按钮上的图标Widget，它是必需的参数。在这里通常使用Icon类传入。                  |
| label            | Widget                   | 显示在按钮上的标签Widget，它是必需的参数。在这里通常会使用Text控件来展示按钮上的标签文本。       |

## TextButton类
### 默认构造函数
```text
TextButton({
    super.key,
    required super.onPressed,
    super.onLongPress,
    super.onHover,
    super.onFocusChange,
    super.style,
    super.focusNode,
    super.autofocus = false,
    super.clipBehavior = Clip.none,
    super.statesController,
    required Widget super.child,
  })
```
### TextButton(...)参数解析
| 参数名称             | 使用类型                     | 参数介绍                    |
|------------------|--------------------------|-------------------------|
| key              | Key                      | 用于识别小部件。                |
| onPressed        | Function                 | 必需回调函数，定义按钮按下时的行为。      |
| onLongPress      | Function                 | 回调函数，定义按钮长按时的行为。        |
| onHover          | Function                 | 回调函数，定义鼠标悬停在按钮上时的行为。    |
| onFocusChange    | Function                 | 回调函数，定义按钮焦点状态变化时的行为。    |
| style            | ButtonStyle              | 样式属性，定义按钮的外观。           |
| focusNode        | FocusNode                | 焦点节点，用于控制按钮的焦点行为。       |
| autofocus        | bool                     | 定义按钮是否自动获取焦点，默认为false。  |
| clipBehavior     | Clip                     | 定义按钮的裁剪行为，默认为Clip.none。 |
| statesController | MaterialStatesController | 状态控制器，用于自定义按钮在不同状态下的样式。 |
| child            | Widget                   | 必需子部件，用于显示在按钮上的文本。      |

### 创建带有图标的构造函数
```text
TextButton.icon({
    Key? key,
    required VoidCallback? onPressed,
    VoidCallback? onLongPress,
    ValueChanged<bool>? onHover,
    ValueChanged<bool>? onFocusChange,
    ButtonStyle? style,
    FocusNode? focusNode,
    bool? autofocus,
    Clip? clipBehavior,
    MaterialStatesController? statesController,
    required Widget icon,
    required Widget label,
  })
```

### TextButton.icon(...)参数解析
| 参数名称             | 使用类型                     | 参数介绍                    |
|------------------|--------------------------|-------------------------|
| key              | Key                      | 用于识别小部件。                |
| onPressed        | Function                 | 必需的回调函数，定义按钮按下时的行为。     |
| onLongPress      | Function                 | 回调函数，定义按钮长按时的行为。        |
| onHover          | Function                 | 回调函数，定义鼠标悬停在按钮上时的行为。    |
| onFocusChange    | Function                 | 回调函数，定义按钮焦点状态变化时的行为。    |
| style            | ButtonStyle              | 按钮样式，用于定义按钮的外观。         |
| focusNode        | FocusNode                | 焦点节点，用于控制按钮的焦点行为。       |
| autofocus        | bool                     | 指定按钮是否自动获取焦点。           |
| clipBehavior     | Clip                     | 定义按钮的裁剪行为。              |
| statesController | MaterialStatesController | 状态控制器，用于自定义按钮在不同状态下的样式。 |
| icon             | Widget                   | 图标小部件，用于显示在按钮旁边的图标。     |
| label            | Widget                   | 文本小部件，用于显示在按钮上的文本。      |

## OutlinedButton类
### 默认的构造函数
```text
OutlinedButton({
    super.key,
    required super.onPressed,
    super.onLongPress,
    super.onHover,
    super.onFocusChange,
    super.style,
    super.focusNode,
    super.autofocus = false,
    super.clipBehavior = Clip.none,
    super.statesController,
    required super.child,
  })
```
### OutlinedButton(...)参数解析
| 参数名称             | 使用类型                     | 参数介绍                                |
|------------------|--------------------------|-------------------------------------|
| key              | Key                      | 继承自父类的可选键，用于识别小部件。                  |
| onPressed        | Function                 | 继承自父类的必需回调函数，定义按钮按下时的行为。            |
| onLongPress      | Function                 | 继承自父类的可选回调函数，定义按钮长按时的行为。            |
| onHover          | Function                 | 继承自父类的可选回调函数，定义鼠标悬停在按钮上时的行为。        |
| onFocusChange    | Function                 | 继承自父类的可选回调函数，定义按钮焦点状态变化时的行为。        |
| style            | ButtonStyle              | 继承自父类的可选样式属性，定义按钮的外观。               |
| focusNode        | FocusNode                | 继承自父类的可选焦点节点，用于控制按钮的焦点行为。           |
| autofocus        | bool                     | 继承自父类的可选属性，定义按钮是否自动获取焦点，默认为 false。  |
| clipBehavior     | Clip                     | 继承自父类的可选属性，定义按钮的裁剪行为，默认为 Clip.none。 |
| statesController | MaterialStatesController | 继承自父类的可选状态控制器，用于自定义按钮在不同状态下的样式。     |
| child            | Widget                   | 继承自父类的必需子部件，用于显示在按钮上的内容。            |

### 创建带有图标的OutlinedButton
```text
OutlinedButton.icon({
    Key? key,
    required VoidCallback? onPressed,
    VoidCallback? onLongPress,
    ButtonStyle? style,
    FocusNode? focusNode,
    bool? autofocus,
    Clip? clipBehavior,
    MaterialStatesController? statesController,
    required Widget icon,
    required Widget label,
  })
```

### OutlinedButton.icon(...)参数解析
| 参数名称             | 使用类型                     | 参数介绍                    |
|------------------|--------------------------|-------------------------|
| key              | Key                      | 用于识别小部件的可选键。            |
| onPressed        | Function                 | 按钮按下时调用的必需回调函数。         |
| onLongPress      | Function                 | 按钮长按时调用的可选回调函数。         |
| style            | ButtonStyle              | 定义按钮的样式，例如背景颜色、文本样式等。   |
| focusNode        | FocusNode                | 按钮的焦点节点。                |
| autofocus        | bool                     | 指定按钮是否自动获取焦点。           |
| clipBehavior     | Clip                     | 指定按钮的裁剪行为。              |
| statesController | MaterialStatesController | 状态控制器，用于自定义按钮在不同状态下的样式。 |
| icon             | Widget                   | 显示在按钮上的图标小部件，它是必需的。     |
| label            | Widget                   | 显示在按钮上的标签小部件，它是必需的。     |

## ToggleButtons类
### 默认构造函数
```text
ToggleButtons({
    super.key,
    required this.children,
    required this.isSelected,
    this.onPressed,
    this.mouseCursor,
    this.tapTargetSize,
    this.textStyle,
    this.constraints,
    this.color,
    this.selectedColor,
    this.disabledColor,
    this.fillColor,
    this.focusColor,
    this.highlightColor,
    this.hoverColor,
    this.splashColor,
    this.focusNodes,
    this.renderBorder = true,
    this.borderColor,
    this.selectedBorderColor,
    this.disabledBorderColor,
    this.borderRadius,
    this.borderWidth,
    this.direction = Axis.horizontal,
    this.verticalDirection = VerticalDirection.down,
  })
```

## ToggleButtons(...)参数解析
| 参数名称                | 使用类型                  | 参数介绍                           |
|---------------------|-----------------------|--------------------------------|
| key                 | Key                   | 继承自父类的可选键，用于识别小部件。             |
| children            | List<Widget>          | 必需参数，一个包含所有按钮的小部件列表。           |
| isSelected          | List<bool>            | 必需参数，一个布尔值列表，用于指示每个按钮是否处于选中状态。 |
| onPressed           | Function              | 一个回调函数，用于处理按钮被点击时的事件。          |
| mouseCursor         | MouseCursor           | 用于指定鼠标指针的样式。                   |
| tapTargetSize       | MaterialTapTargetSize | 指定按钮的点击目标大小。                   |
| textStyle           | TextStyle             | 用于指定按钮文本的样式。                   |
| constraints         | BoxConstraints        | 用于指定按钮的尺寸约束。                   |
| color               | Color                 | 指定按钮的颜色。                       |
| selectedColor       | Color                 | 指定选中按钮的颜色。                     |
| disabledColor       | Color                 | 指定禁用按钮的颜色。                     |
| fillColor           | Color                 | 指定按钮的填充颜色。                     |
| focusColor          | Color                 | 指定按钮获得焦点时的颜色。                  |
| highlightColor      | Color                 | 指定按钮被按下时的颜色。                   |
| hoverColor          | Color                 | 指定鼠标悬停在按钮上时的颜色。                |
| splashColor         | Color                 | 指定按钮被按下时的水波纹颜色。                |
| focusNodes          | List<FocusNode>       | 用于指定每个按钮的焦点节点。                 |
| renderBorder        | bool                  | 指定是否渲染按钮的边框。                   |
| borderColor         | Color                 | 指定按钮边框的颜色。                     |
| selectedBorderColor | Color                 | 指定选中按钮边框的颜色。                   |
| disabledBorderColor | Color                 | 指定禁用按钮边框的颜色。                   |
| borderRadius        | BorderRadius          | 指定按钮边框的圆角半径。                   |
| borderWidth         | double                | 指定按钮边框的宽度。                     |
| direction           | Axis                  | 指定按钮排列的方向，默认为水平方向。             |
| verticalDirection   | VerticalDirection     | 指定按钮在垂直方向上的排列方式，默认为向下排列。       |

## FloatingActionButton类
### 默认构造函数
```text
FloatingActionButton({
    super.key,
    this.child,
    this.tooltip,
    this.foregroundColor,
    this.backgroundColor,
    this.focusColor,
    this.hoverColor,
    this.splashColor,
    this.heroTag = const _DefaultHeroTag(),
    this.elevation,
    this.focusElevation,
    this.hoverElevation,
    this.highlightElevation,
    this.disabledElevation,
    required this.onPressed,
    this.mouseCursor,
    this.mini = false,
    this.shape,
    this.clipBehavior = Clip.none,
    this.focusNode,
    this.autofocus = false,
    this.materialTapTargetSize,
    this.isExtended = false,
    this.enableFeedback,
  })
```
### FloatingActionButton(...)参数解析
| 参数名称                  | 使用类型                  | 参数介绍                 |
|-----------------------|-----------------------|----------------------|
| key                   | Key                   | 继承自父类的可选键，用于识别小部件。   |
| child                 | Widget                | 显示在按钮上的小部件。          |
| tooltip               | String                | 当用户长按按钮时显示的文本提示。     |
| foregroundColor       | Color                 | 按钮的前景色，用于设置图标和标签的颜色。 |
| backgroundColor       | Color                 | 按钮的背景色。              |
| focusColor            | Color                 | 按钮获得焦点时的颜色。          |
| hoverColor            | Color                 | 鼠标悬停在按钮上时的颜色。        |
| splashColor           | Color                 | 按钮被按下时的水波纹颜色。        |
| heroTag               | Object                | 用于实现按钮之间的共享元素转换动画。   |
| elevation             | double                | 按钮的高度。               |
| focusElevation        | double                | 按钮获得焦点时的高度。          |
| hoverElevation        | double                | 鼠标悬停在按钮上时的高度。        |
| highlightElevation    | double                | 按钮被按下时的高度。           |
| disabledElevation     | double                | 按钮禁用时的高度。            |
| onPressed             | Function              | 必需参数，按钮被点击时调用的回调函数。  |
| mouseCursor           | MouseCursor           | 鼠标指针的样式。             |
| mini                  | bool                  | 指定按钮是否是小型按钮。         |
| shape                 | ShapeBorder           | 按钮的形状，如圆形或矩形。        |
| clipBehavior          | Clip                  | 按钮的裁剪行为。             |
| focusNode             | FocusNode             | 按钮的焦点节点。             |
| autofocus             | bool                  | 指定按钮是否自动获取焦点。        |
| materialTapTargetSize | MaterialTapTargetSize | 按钮的目标大小。             |
| isExtended            | bool                  | 指定按钮是否是扩展的。          |
| enableFeedback        | bool                  | 指定按钮是否启用触觉反馈。        |

### 用于创建一个小型的浮动操作按钮
```text
FloatingActionButton.small({
    super.key,
    this.child,
    this.tooltip,
    this.foregroundColor,
    this.backgroundColor,
    this.focusColor,
    this.hoverColor,
    this.splashColor,
    this.heroTag = const _DefaultHeroTag(),
    this.elevation,
    this.focusElevation,
    this.hoverElevation,
    this.highlightElevation,
    this.disabledElevation,
    required this.onPressed,
    this.mouseCursor,
    this.shape,
    this.clipBehavior = Clip.none,
    this.focusNode,
    this.autofocus = false,
    this.materialTapTargetSize,
    this.enableFeedback,
  })
```

### FloatingActionButton.small(...)参数解析
| 参数名称                  | 使用类型                  | 参数介绍                 |
|-----------------------|-----------------------|----------------------|
| key                   | Key                   | 继承自父类的可选键，用于识别小部件。   |
| child                 | Widget                | 显示在按钮上的小部件。          |
| tooltip               | String                | 当用户长按按钮时显示的文本提示。     |
| foregroundColor       | Color                 | 按钮的前景色，用于设置图标和标签的颜色。 |
| backgroundColor       | Color                 | 按钮的背景色。              |
| focusColor            | Color                 | 按钮获得焦点时的颜色。          |
| hoverColor            | Color                 | 鼠标悬停在按钮上时的颜色。        |
| splashColor           | Color                 | 按钮被按下时的水波纹颜色。        |
| heroTag               | Object                | 用于实现按钮之间的共享元素转换动画。   |
| elevation             | double                | 按钮的高度。               |
| focusElevation        | double                | 按钮获得焦点时的高度。          |
| hoverElevation        | double                | 鼠标悬停在按钮上时的高度。        |
| highlightElevation    | double                | 按钮被按下时的高度。           |
| disabledElevation     | double                | 按钮禁用时的高度。            |
| onPressed             | Function              | 必需参数，按钮被点击时调用的回调函数。  |
| mouseCursor           | MouseCursor           | 鼠标指针的样式。             |
| shape                 | ShapeBorder           | 按钮的形状，如圆形或矩形。        |
| clipBehavior          | Clip                  | 按钮的裁剪行为。             |
| focusNode             | FocusNode             | 按钮的焦点节点。             |
| autofocus             | bool                  | 指定按钮是否自动获取焦点。        |
| materialTapTargetSize | MaterialTapTargetSize | 按钮的目标大小。             |
| enableFeedback        | bool                  | 指定按钮是否启用触觉反馈。        |

### 用于创建一个大型的浮动操作按钮
```text
FloatingActionButton.large({
    super.key,
    this.child,
    this.tooltip,
    this.foregroundColor,
    this.backgroundColor,
    this.focusColor,
    this.hoverColor,
    this.splashColor,
    this.heroTag = const _DefaultHeroTag(),
    this.elevation,
    this.focusElevation,
    this.hoverElevation,
    this.highlightElevation,
    this.disabledElevation,
    required this.onPressed,
    this.mouseCursor,
    this.shape,
    this.clipBehavior = Clip.none,
    this.focusNode,
    this.autofocus = false,
    this.materialTapTargetSize,
    this.enableFeedback,
  }) 
```
### FloatingActionButton.large(...)参数解析
| 参数名称                  | 使用类型                  | 参数介绍                 |
|-----------------------|-----------------------|----------------------|
| key                   | Key                   | 继承自父类的可选键，用于识别小部件。   |
| child                 | Widget                | 显示在按钮上的小部件。          |
| tooltip               | String                | 当用户长按按钮时显示的文本提示。     |
| foregroundColor       | Color                 | 按钮的前景色，用于设置图标和标签的颜色。 |
| backgroundColor       | Color                 | 按钮的背景色。              |
| focusColor            | Color                 | 按钮获得焦点时的颜色。          |
| hoverColor            | Color                 | 鼠标悬停在按钮上时的颜色。        |
| splashColor           | Color                 | 按钮被按下时的水波纹颜色。        |
| heroTag               | Object                | 用于实现按钮之间的共享元素转换动画。   |
| elevation             | double                | 按钮的高度。               |
| focusElevation        | double                | 按钮获得焦点时的高度。          |
| hoverElevation        | double                | 鼠标悬停在按钮上时的高度。        |
| highlightElevation    | double                | 按钮被按下时的高度。           |
| disabledElevation     | double                | 按钮禁用时的高度。            |
| onPressed             | Function              | 必需参数，按钮被点击时调用的回调函数。  |
| mouseCursor           | MouseCursor           | 鼠标指针的样式。             |
| shape                 | ShapeBorder           | 按钮的形状，如圆形或矩形。        |
| clipBehavior          | Clip                  | 按钮的裁剪行为。             |
| focusNode             | FocusNode             | 按钮的焦点节点。             |
| autofocus             | bool                  | 指定按钮是否自动获取焦点。        |
| materialTapTargetSize | MaterialTapTargetSize | 按钮的目标大小。             |
| enableFeedback        | bool                  | 指定按钮是否启用触觉反馈。        |

### 用于创建扩展型的浮动操作按钮。与普通的浮动操作按钮（FloatingActionButton）相比，扩展型的按钮在按钮上方会显示一个标签
```text
FloatingActionButton.extended({
    super.key,
    this.tooltip,
    this.foregroundColor,
    this.backgroundColor,
    this.focusColor,
    this.hoverColor,
    this.heroTag = const _DefaultHeroTag(),
    this.elevation,
    this.focusElevation,
    this.hoverElevation,
    this.splashColor,
    this.highlightElevation,
    this.disabledElevation,
    required this.onPressed,
    this.mouseCursor = SystemMouseCursors.click,
    this.shape,
    this.isExtended = true,
    this.materialTapTargetSize,
    this.clipBehavior = Clip.none,
    this.focusNode,
    this.autofocus = false,
    this.extendedIconLabelSpacing,
    this.extendedPadding,
    this.extendedTextStyle,
    Widget? icon,
    required Widget label,
    this.enableFeedback,
  })
```

### FloatingActionButton.extended(...)参数解析
| 参数名称                     | 使用类型                  | 参数介绍                                                   |
|--------------------------|-----------------------|--------------------------------------------------------|
| key                      | Key                   | 继承自父类的键值（key）                                          |
| tooltip                  | String                | 操作按钮的提示文本                                              |
| foregroundColor          | Color                 | 操作按钮的前景色                                               |
| backgroundColor          | Color                 | 操作按钮的背景色                                               |
| focusColor               | Color                 | 操作按钮获取焦点时的颜色                                           |
| hoverColor               | Color                 | 操作按钮悬停时的颜色                                             |
| heroTag                  | Object                | 操作按钮的hero标签，用于在页面过渡时共享动画                               |
| elevation                | double                | 操作按钮的标准高度                                              |
| focusElevation           | double                | 操作按钮获取焦点时的高度                                           |
| hoverElevation           | double                | 操作按钮悬停时的高度                                             |
| splashColor              | Color                 | 操作按钮被点击时的颜色                                            |
| highlightElevation       | double                | 操作按钮被按下时的高度                                            |
| disabledElevation        | double                | 操作按钮禁用时的高度                                             |
| onPressed                | Function              | 操作按钮被按下时触发的回调函数，是一个必需参数                                |
| mouseCursor              | *SystemMouseCursors   | 鼠标指针悬停在操作按钮上时的样式，默认为系统默认点击样式（SystemMouseCursors.click） |
| shape                    | ShapeBorder           | 操作按钮的形状                                                |
| isExtended               | bool                  | 操作按钮是否为扩展模式，默认为true                                    |
| materialTapTargetSize    | MaterialTapTargetSize | 操作按钮的Tap Target大小                                      |
| clipBehavior             | Clip                  | 操作按钮的裁剪行为                                              |
| focusNode                | FocusNode             | 操作按钮的焦点节点                                              |
| autofocus                | bool                  | 操作按钮是否自动获取焦点，默认为false                                  |
| extendedIconLabelSpacing | double                | 扩展型按钮中图标和标签之间的间距                                       |
| extendedPadding          | EdgeInsetsGeometry    | 扩展型按钮的内边距                                              |
| extendedTextStyle        | TextStyle             | 扩展型按钮中标签的文本样式                                          |
| icon                     | Widget                | 操作按钮的图标部分                                              |
| label                    | Widget                | 操作按钮的标签部分，是一个必需参数                                      |
| enableFeedback           | bool                  | 操作按钮是否启用触觉反馈                                           |

> 备注
> * SystemMouseCursors是独立于MouseCursor的类，使用SystemMouseCursors可以让你的Flutter应用程序在支持系统级别的鼠标指针样式的同时，还能够保持应用程序整体的一致性和易用性。而MouseCursors是一个通用的类，可以在任何Flutter应用程序中使用。如果你需要使用系统级别的鼠标指针样式，就应该使用SystemMouseCursors，否则就应该使用MouseCursors。

## IconButton类
### 默认构造函数
```text
IconButton({
    super.key,
    this.iconSize,
    this.visualDensity,
    this.padding,
    this.alignment,
    this.splashRadius,
    this.color,
    this.focusColor,
    this.hoverColor,
    this.highlightColor,
    this.splashColor,
    this.disabledColor,
    required this.onPressed,
    this.mouseCursor,
    this.focusNode,
    this.autofocus = false,
    this.tooltip,
    this.enableFeedback,
    this.constraints,
    this.style,
    this.isSelected,
    this.selectedIcon,
    required this.icon,
  })
```

### IconButton(...)参数解析
| 参数名称           | 使用类型               | 参数介绍                |
|----------------|--------------------|---------------------|
| key            | Key                | 继承自父类的键值（key）       |
| iconSize       | double             | 图标的尺寸               |
| visualDensity  | VisualDensity      | 按钮的视觉密度             |
| padding        | EdgeInsetsGeometry | 按钮的内边距              |
| alignment      | AlignmentGeometry  | 图标在按钮内的对齐方式         |
| splashRadius   | double             | 点击水波纹效果的半径          |
| color          | Color              | 按钮的颜色               |
| focusColor     | Color              | 按钮获取焦点时的颜色          |
| hoverColor     | Color              | 按钮悬停时的颜色            |
| highlightColor | Color              | 按钮被按下时的颜色           |
| splashColor    | Color              | 点击水波纹效果的颜色          |
| disabledColor  | Color              | 按钮禁用时的颜色            |
| onPressed      | Function           | 按钮被按下时的回调函数，是一个必需参数 |
| mouseCursor    | MouseCursor        | 鼠标指针悬停在按钮上时的样式      |
| focusNode      | FocusNode          | 按钮的焦点节点             |
| autofocus      | bool               | 按钮是否自动获取焦点，默认为false |
| tooltip        | String             | 按钮的提示文本             |
| enableFeedback | bool               | 按钮是否启用触觉反馈          |
| constraints    | BoxConstraints     | 按钮的约束条件             |
| style          | ButtonStyle        | 按钮的文本样式             |
| isSelected     | bool               | 按钮是否处于选中状态          |
| selectedIcon   | Widget             | 按钮选中状态下显示的图标        |
| icon           | Widget             | 按钮的图标部分，是一个必需参数     |

### 用于创建一个带有填充背景颜色的图标按钮
```text
IconButton.filled({
    super.key,
    this.iconSize,
    this.visualDensity,
    this.padding,
    this.alignment,
    this.splashRadius,
    this.color,
    this.focusColor,
    this.hoverColor,
    this.highlightColor,
    this.splashColor,
    this.disabledColor,
    required this.onPressed,
    this.mouseCursor,
    this.focusNode,
    this.autofocus = false,
    this.tooltip,
    this.enableFeedback,
    this.constraints,
    this.style,
    this.isSelected,
    this.selectedIcon,
    required this.icon,
  })
```

### IconButton.filled(...)参数解析
| 参数名称           | 使用类型               | 参数介绍                |
|----------------|--------------------|---------------------|
| key            | Key                | 继承自父类的键值（key）       |
| iconSize       | double             | 图标的尺寸               |
| visualDensity  | VisualDensity      | 按钮的视觉密度             |
| padding        | EdgeInsetsGeometry | 按钮的内边距              |
| alignment      | AlignmentGeometry  | 图标在按钮内的对齐方式         |
| splashRadius   | double             | 点击水波纹效果的半径          |
| color          | Color              | 按钮的背景颜色             |
| focusColor     | Color              | 按钮获取焦点时的颜色          |
| hoverColor     | Color              | 按钮悬停时的颜色            |
| highlightColor | Color              | 按钮被按下时的颜色           |
| splashColor    | Color              | 点击水波纹效果的颜色          |
| disabledColor  | Color              | 按钮禁用时的颜色            |
| onPressed      | Function           | 按钮被按下时的回调函数，是一个必需参数 |
| mouseCursor    | MouseCursor        | 鼠标指针悬停在按钮上时的样式      |
| focusNode      | FocusNode          | 按钮的焦点节点             |
| autofocus      | bool               | 按钮是否自动获取焦点，默认为false |
| tooltip        | String             | 按钮的提示文本             |
| enableFeedback | bool               | 按钮是否启用触觉反馈          |
| constraints    | BoxConstraints     | 按钮的约束条件             |
| style          | ButtonStyle        | 按钮的文本样式             |
| isSelected     | bool               | 按钮是否处于选中状态          |
| selectedIcon   | Widget             | 按钮选中状态下显示的图标        |
| icon           | Widget             | 按钮的图标部分，是一个必需参数     |

### 用于创建一个带有基于主题色调的填充背景颜色的图标按钮
```text
IconButton.filledTonal({
    super.key,
    this.iconSize,
    this.visualDensity,
    this.padding,
    this.alignment,
    this.splashRadius,
    this.color,
    this.focusColor,
    this.hoverColor,
    this.highlightColor,
    this.splashColor,
    this.disabledColor,
    required this.onPressed,
    this.mouseCursor,
    this.focusNode,
    this.autofocus = false,
    this.tooltip,
    this.enableFeedback,
    this.constraints,
    this.style,
    this.isSelected,
    this.selectedIcon,
    required this.icon,
  })
```

### IconButton.filledTonal(...)参数解析
| 参数名称           | 使用类型               | 参数介绍                |
|----------------|--------------------|---------------------|
| key            | Key                | 继承自父类的键值（key）       |
| iconSize       | double             | 图标的尺寸               |
| visualDensity  | VisualDensity      | 按钮的视觉密度             |
| padding        | EdgeInsetsGeometry | 按钮的内边距              |
| alignment      | AlignmentGeometry  | 图标在按钮内的对齐方式         |
| splashRadius   | double             | 点击水波纹效果的半径          |
| color          | Color              | 按钮的背景颜色             |
| focusColor     | Color              | 按钮获取焦点时的颜色          |
| hoverColor     | Color              | 按钮悬停时的颜色            |
| highlightColor | Color              | 按钮被按下时的颜色           |
| splashColor    | Color              | 点击水波纹效果的颜色          |
| disabledColor  | Color              | 按钮禁用时的颜色            |
| onPressed      | Function           | 按钮被按下时的回调函数，是一个必需参数 |
| mouseCursor    | MouseCursor        | 鼠标指针悬停在按钮上时的样式      |
| focusNode      | FocusNode          | 按钮的焦点节点             |
| autofocus      | bool               | 按钮是否自动获取焦点，默认为false |
| tooltip        | String             | 按钮的提示文本             |
| enableFeedback | bool               | 按钮是否启用触觉反馈          |
| constraints    | BoxConstraints     | 按钮的约束条件             |
| style          | ButtonStyle        | 按钮的文本样式             |
| isSelected     | bool               | 按钮是否处于选中状态          |
| selectedIcon   | Widget             | 按钮选中状态下显示的图标        |
| icon           | Widget             | 按钮的图标部分，是一个必需参数     |

### 用于创建一个带有边框的图标按钮
```text
IconButton.outlined({
    super.key,
    this.iconSize,
    this.visualDensity,
    this.padding,
    this.alignment,
    this.splashRadius,
    this.color,
    this.focusColor,
    this.hoverColor,
    this.highlightColor,
    this.splashColor,
    this.disabledColor,
    required this.onPressed,
    this.mouseCursor,
    this.focusNode,
    this.autofocus = false,
    this.tooltip,
    this.enableFeedback,
    this.constraints,
    this.style,
    this.isSelected,
    this.selectedIcon,
    required this.icon,
  })
```

### IconButton.outlined(...)参数解析
| 参数名称           | 使用类型               | 参数介绍                |
|----------------|--------------------|---------------------|
| key            | Key                | 继承自父类的键值（key）       |
| iconSize       | double             | 图标的尺寸               |
| visualDensity  | VisualDensity      | 按钮的视觉密度             |
| padding        | EdgeInsetsGeometry | 按钮的内边距              |
| alignment      | AlignmentGeometry  | 图标在按钮内的对齐方式         |
| splashRadius   | double             | 点击水波纹效果的半径          |
| color          | Color              | 按钮的边框颜色             |
| focusColor     | Color              | 按钮获取焦点时的颜色          |
| hoverColor     | Color              | 按钮悬停时的颜色            |
| highlightColor | Color              | 按钮被按下时的颜色           |
| splashColor    | Color              | 点击水波纹效果的颜色          |
| disabledColor  | Color              | 按钮禁用时的颜色            |
| onPressed      | Function           | 按钮被按下时的回调函数，是一个必需参数 |
| mouseCursor    | MouseCursor        | 鼠标指针悬停在按钮上时的样式      |
| focusNode      | FocusNode          | 按钮的焦点节点             |
| autofocus      | bool               | 按钮是否自动获取焦点，默认为false |
| tooltip        | String             | 按钮的提示文本             |
| enableFeedback | bool               | 按钮是否启用触觉反馈          |
| constraints    | BoxConstraints     | 按钮的约束条件             |
| style          | ButtonStyle        | 按钮的文本样式             |
| isSelected     | bool               | 按钮是否处于选中状态          |
| selectedIcon   | Widget             | 按钮选中状态下显示的图标        |
| icon           | Widget             | 按钮的图标部分，是一个必需参数     |

## CupertinoButton类
### 默认构造函数
```text
CupertinoButton({
    super.key,
    required this.child,
    this.padding,
    this.color,
    this.disabledColor = CupertinoColors.quaternarySystemFill,
    this.minSize = kMinInteractiveDimensionCupertino,
    this.pressedOpacity = 0.4,
    this.borderRadius = const BorderRadius.all(Radius.circular(8.0)),
    this.alignment = Alignment.center,
    required this.onPressed,
  })
```

### CupertinoButton(...)参数解析
| 参数名称           | 使用类型               | 参数介绍                                                        |
|----------------|--------------------|-------------------------------------------------------------|
| key            | Key                | 继承自父类的键值（key）                                               |
| child          | Widget             | 按钮的子部件，通常是一个Text小部件，用于显示按钮的文本                               |
| padding        | EdgeInsetsGeometry | 按钮的内边距                                                      |
| color          | Color              | 按钮的背景颜色                                                     |
| disabledColor  | *CupertinoColors   | 按钮禁用时的背景颜色，默认为CupertinoColors.quaternarySystemFill          |
| minSize        | double             | 按钮的最小尺寸，默认为kMinInteractiveDimensionCupertino，即44像素          |
| pressedOpacity | double             | 按钮被按下时的不透明度，默认为0.4                                          |
| borderRadius   | BorderRadius       | 按钮的边框半径，默认为BorderRadius.all(Radius.circular(8.0))，即圆角半径为8像素 |
| alignment      | AlignmentGeometry  | 按钮内子部件的对齐方式，默认为Alignment.center，即居中对齐                       |
| onPressed      | Function           | 按钮被按下时的回调函数，是一个必需参数                                         |

* 备注
* > CupertinoColors是一个包含了Cupertino风格应用程序中常用颜色的类。它提供了一组预定义的颜色常量，用于在iOS风格的应用程序中保持一致的颜色主题。CupertinoColors中的颜色常量可以被Color类或Colors类中的相应颜色常量代替。

### 在Cupertino风格的应用程序中创建填充按钮的构造函数。
```text
CupertinoButton.filled({
    super.key,
    required this.child,
    this.padding,
    this.disabledColor = CupertinoColors.quaternarySystemFill,
    this.minSize = kMinInteractiveDimensionCupertino,
    this.pressedOpacity = 0.4,
    this.borderRadius = const BorderRadius.all(Radius.circular(8.0)),
    this.alignment = Alignment.center,
    required this.onPressed,
  })
```

### CupertinoButton.filled(...)参数解析
| 参数名称           | 使用类型               | 参数介绍                                                        |
|----------------|--------------------|-------------------------------------------------------------|
| key            | Key                | 继承自父类的key参数                                                 |
| child          | Widget             | 按钮的子部件，通常是一个Text小部件，用于显示按钮的文本                               |
| padding        | EdgeInsetsGeometry | 按钮的内边距                                                      |
| disabledColor  | CupertinoColors    | 按钮禁用时的背景颜色，默认为CupertinoColors.quaternarySystemFill          |
| minSize        | double             | 按钮的最小尺寸，默认为kMinInteractiveDimensionCupertino，即44.0像素        |
| pressedOpacity | double             | 按钮被按下时的不透明度，默认为0.4                                          |
| borderRadius   | BorderRadius       | 按钮的边框半径，默认为BorderRadius.all(Radius.circular(8.0))，即圆角半径为8像素 |
| alignment      | AlignmentGeometry  | 按钮内子部件的对齐方式，默认为Alignment.center，即居中对齐                       |
| onPressed      | Function           | 按钮被按下时的回调函数，是一个必需参数                                         |

## Switch类
### 默认构造函数
```text
Switch({
    super.key,
    required this.value,
    required this.onChanged,
    this.activeColor,
    this.activeTrackColor,
    this.inactiveThumbColor,
    this.inactiveTrackColor,
    this.activeThumbImage,
    this.onActiveThumbImageError,
    this.inactiveThumbImage,
    this.onInactiveThumbImageError,
    this.thumbColor,
    this.trackColor,
    this.trackOutlineColor,
    this.thumbIcon,
    this.materialTapTargetSize,
    this.dragStartBehavior = DragStartBehavior.start,
    this.mouseCursor,
    this.focusColor,
    this.hoverColor,
    this.overlayColor,
    this.splashRadius,
    this.focusNode,
    this.onFocusChange,
    this.autofocus = false,
  }) 
```

###  Switch(...)参数解析
| 参数名称                      | 使用类型                         | 参数介绍                                                  |
|---------------------------|------------------------------|-------------------------------------------------------|
| key                       | Key                          | 用于在树中唯一标识该组件                                          |
| value                     | bool                         | 必需参数，当前开关的状态，是一个 bool 值，为 true 表示开启状态，为 false 表示关闭状态  |
| onChanged                 | Function                     | 必需参数，当开关状态发生改变时的回调函数，它接收一个 bool 参数，表示开关的最新状态          |
| activeColor               | Color                        | 开启状态时的颜色                                              |
| activeTrackColor          | Color                        | 开启状态时轨道的颜色                                            |
| inactiveThumbColor        | Color                        | 关闭状态时滑块的颜色                                            |
| inactiveTrackColor        | Color                        | 关闭状态时轨道的颜色                                            |
| activeThumbImage          | ImageProvider<Object>        | 开启状态时滑块的图片                                            |
| onActiveThumbImageError   | Function                     | 当 activeThumbImage 加载失败时的回调函数                         |
| inactiveThumbImage        | ImageProvider<Object>        | 关闭状态时滑块的图片                                            |
| onInactiveThumbImageError | Function                     | 当 inactiveThumbImage 加载失败时的回调函数                       |
| thumbColor                | MaterialStateProperty<Color> | 滑块的颜色                                                 |
| trackColor                | MaterialStateProperty<Color> | 轨道的颜色                                                 |
| trackOutlineColor         | MaterialStateProperty<Color> | 轨道的边框颜色                                               |
| thumbIcon                 | MaterialStateProperty<Icon>  | 滑块上显示的图标                                              |
| materialTapTargetSize     | MaterialTapTargetSize        | 控件的最小大小                                               |
| dragStartBehavior         | DragStartBehavior            | 确定开始拖动时使用的行为                                          |
| mouseCursor               | MouseCursor                  | 指针悬停在控件上时的鼠标光标                                        |
| focusColor                | Color                        | 控件获取焦点时的颜色                                            |
| hoverColor                | Color                        | 鼠标悬停在控件上时的颜色                                          |
| overlayColor              | MaterialStateProperty<Color> | 覆盖在控件上的颜色                                             |
| splashRadius              | double                       | 水波纹的半径                                                |
| focusNode                 | FocusNode                    | 控制控件是否具有焦点                                            |
| onFocusChange             | Function                     | 当控件的焦点状态发生改变时的回调函数                                    |
| autofocus                 | bool                         | 是否自动获取焦点                                              |

### 在外观上根据平台自适应
```text
Switch.adaptive({
    super.key,
    required this.value,
    required this.onChanged,
    this.activeColor,
    this.activeTrackColor,
    this.inactiveThumbColor,
    this.inactiveTrackColor,
    this.activeThumbImage,
    this.onActiveThumbImageError,
    this.inactiveThumbImage,
    this.onInactiveThumbImageError,
    this.materialTapTargetSize,
    this.thumbColor,
    this.trackColor,
    this.trackOutlineColor,
    this.thumbIcon,
    this.dragStartBehavior = DragStartBehavior.start,
    this.mouseCursor,
    this.focusColor,
    this.hoverColor,
    this.overlayColor,
    this.splashRadius,
    this.focusNode,
    this.onFocusChange,
    this.autofocus = false,
    this.applyCupertinoTheme,
  }) 
```

### Switch.adaptive(...)参数解析
| 参数名称                      | 使用类型                         | 参数介绍                                                         |
|---------------------------|------------------------------|--------------------------------------------------------------|
| key                       | Key                          | 用于在树中唯一标识该组件                                                 |
| value                     | bool                         | 必需参数，当前开关的状态，是一个 bool 值，为 true 表示开启状态，为 false 表示关闭状态         |
| onChanged                 | Function                     | 必需参数，当开关状态发生改变时的回调函数，它接收一个 bool 参数，表示开关的最新状态                 |
| activeColor               | Color                        | 开启状态时的颜色                                                     |
| activeTrackColor          | Color                        | 开启状态时轨道的颜色                                                   |
| inactiveThumbColor        | Color                        | 关闭状态时滑块的颜色                                                   |
| inactiveTrackColor        | Color                        | 关闭状态时轨道的颜色                                                   |
| activeThumbImage          | ImageProvider<Object>        | 开启状态时滑块的图片                                                   |
| onActiveThumbImageError   | Function                     | 当 activeThumbImage 加载失败时的回调函数                                |
| inactiveThumbImage        | ImageProvider<Object>        | 关闭状态时滑块的图片                                                   |
| onInactiveThumbImageError | Function                     | 当 inactiveThumbImage 加载失败时的回调函数                              |
| thumbColor                | MaterialStateProperty<Color> | 滑块的颜色                                                        |
| trackColor                | MaterialStateProperty<Color> | 轨道的颜色                                                        |
| trackOutlineColor         | MaterialStateProperty<Color> | 轨道的边框颜色                                                      |
| thumbIcon                 | MaterialStateProperty<Icon>  | 滑块上显示的图标                                                     |
| materialTapTargetSize     | MaterialTapTargetSize        | 控件的最小大小                                                      |
| dragStartBehavior         | DragStartBehavior            | 确定开始拖动时使用的行为                                                 |
| mouseCursor               | MouseCursor                  | 指针悬停在控件上时的鼠标光标                                               |
| focusColor                | Color                        | 控件获取焦点时的颜色                                                   |
| hoverColor                | Color                        | 鼠标悬停在控件上时的颜色                                                 |
| overlayColor              | MaterialStateProperty<Color> | 覆盖在控件上的颜色                                                    |
| splashRadius              | double                       | 水波纹的半径                                                       |
| focusNode                 | FocusNode                    | 控制控件是否具有焦点                                                   |
| onFocusChange             | Function                     | 当控件的焦点状态发生改变时的回调函数                                           |
| autofocus                 | bool                         | 是否自动获取焦点                                                     |
| applyCupertinoTheme       | bool                         | 用于指示是否应该应用 Cupertino 风格的主题样式（true）还是 Material 风格的主题样式（false） | 

## Checkbox类
### 默认构造函数
```text
Checkbox({
    super.key,
    required this.value,
    this.tristate = false,
    required this.onChanged,
    this.mouseCursor,
    this.activeColor,
    this.fillColor,
    this.checkColor,
    this.focusColor,
    this.hoverColor,
    this.overlayColor,
    this.splashRadius,
    this.materialTapTargetSize,
    this.visualDensity,
    this.focusNode,
    this.autofocus = false,
    this.shape,
    this.side,
    this.isError = false,
  }) 
```

### CheckBox(...)参数解析
| 参数名称                  | 使用类型                         | 参数介绍                                              |
|-----------------------|------------------------------|---------------------------------------------------|
| key                   | Key                          | 用于在树中唯一标识该组件                                      |
| value                 | bool                         | 当前复选框的状态，是一个 bool 值，为 true 表示选中状态，为 false 表示未选中状态 |
| tristate              | bool                         | 是否启用三态复选框                                         |
| onChanged             | Function                     | 当复选框状态发生改变时的回调函数，它接收一个 bool? 参数，表示复选框的最新状态        |
| mouseCursor           | MouseCursor                  | 指针悬停在控件上时的鼠标光标                                    |
| activeColor           | Color                        | 选中状态时的颜色                                          |
| fillColor             | MaterialStateProperty<Color> | 复选框的填充颜色                                          |
| checkColor            | Color                        | 复选框中勾选图标的颜色                                       |
| focusColor            | Color                        | 控件获取焦点时的颜色                                        |
| hoverColor            | Color                        | 鼠标悬停在控件上时的颜色                                      |
| overlayColor          | MaterialStateProperty<Color> | 覆盖在控件上的颜色                                         |
| splashRadius          | double                       | 水波纹的半径                                            |
| materialTapTargetSize | MaterialTapTargetSize        | 控件的最小大小                                           |
| visualDensity         | VisualDensity                | 用于控制复选框的布局密度                                      |
| focusNode             | FocusNode                    | 控制控件是否具有焦点                                        |
| autofocus             | bool                         | 是否自动获取焦点                                          |
| shape                 | OutlinedBorder               | 复选框的形状                                            |
| side                  | BorderSide                   | 复选框的边框                                            |
| isError               | bool                         | 是否将复选框渲染为错误状态                                     |

### 根据平台自适应
```text
Checkbox.adaptive({
    super.key,
    required this.value,
    this.tristate = false,
    required this.onChanged,
    this.mouseCursor,
    this.activeColor,
    this.fillColor,
    this.checkColor,
    this.focusColor,
    this.hoverColor,
    this.overlayColor,
    this.splashRadius,
    this.materialTapTargetSize,
    this.visualDensity,
    this.focusNode,
    this.autofocus = false,
    this.shape,
    this.side,
    this.isError = false,
  }) 
```

### Checkbox.adaptive(...)参数解析
| 参数名称                  | 使用类型                         | 参数介绍                                              |
|-----------------------|------------------------------|---------------------------------------------------|
| key                   | Key                          | Widget的唯一标识符，用于在树中唯一标识该组件                         |
| value                 | bool                         | 当前复选框的状态，是一个 bool 值，为 true 表示选中状态，为 false 表示未选中状态 |
| tristate              | bool                         | 是否启用三态复选框                                         |
| onChanged             | Function                     | 当复选框状态发生改变时的回调函数，它接收一个 bool? 参数，表示复选框的最新状态        |
| mouseCursor           | MouseCursor                  | 指针悬停在控件上时的鼠标光标                                    |
| activeColor           | Color                        | 选中状态时的颜色                                          |
| fillColor             | MaterialStateProperty<Color> | 复选框的填充颜色                                          |
| checkColor            | Color                        | 复选框中勾选图标的颜色                                       |
| focusColor            | Color                        | 控件获取焦点时的颜色                                        |
| hoverColor            | Color                        | 鼠标悬停在控件上时的颜色                                      |
| overlayColor          | MaterialStateProperty<Color> | 覆盖在控件上的颜色                                         |
| splashRadius          | double                       | 水波纹的半径                                            |
| materialTapTargetSize | MaterialTapTargetSize        | 控件的最小大小                                           |
| visualDensity         | VisualDensity                | 用于控制复选框的布局密度                                      |
| focusNode             | FocusNode                    | 控制控件是否具有焦点                                        |
| autofocus             | bool                         | 是否自动获取焦点                                          |
| shape                 | OutlinedBorder               | 复选框的形状                                            |
| side                  | BorderSide                   | 复选框的边框                                            |
| isError               | bool                         | 是否将复选框渲染为错误状态                                     |

## DropdownButton类
###  默认构造函数
```text
DropdownButton({
    super.key,
    required this.items,
    this.selectedItemBuilder,
    this.value,
    this.hint,
    this.disabledHint,
    required this.onChanged,
    this.onTap,
    this.elevation = 8,
    this.style,
    this.underline,
    this.icon,
    this.iconDisabledColor,
    this.iconEnabledColor,
    this.iconSize = 24.0,
    this.isDense = false,
    this.isExpanded = false,
    this.itemHeight = kMinInteractiveDimension,
    this.focusColor,
    this.focusNode,
    this.autofocus = false,
    this.dropdownColor,
    this.menuMaxHeight,
    this.enableFeedback,
    this.alignment = AlignmentDirectional.centerStart,
    this.borderRadius,
    this.padding
  })
```

### DropdownButton(...)参数解析
| 参数名称                | 使用类型                      | 参数介绍                                          |
|---------------------|---------------------------|-----------------------------------------------|
| key                 | Key                       | 用于在树中唯一标识该组件                                  |
| items               | List<DropdownMenuItem<T>> | 一个包含所有选项的列表，每个选项由 DropdownMenuItem<T> 小部件表示   |
| selectedItemBuilder | List<Widget>              | 一个构建器函数，用于在选择的值下方构建一个小部件                      |
| value               | T                         | 当前选中的值，必须与 items 中的某个值相匹配，用于确定默认选中项           |
| hint                | Widget                    | 在下拉菜单中显示的提示内容，通常用于指示用户进行选择                    |
| disabledHint        | Widget                    | 在下拉菜单中显示的禁用时的提示内容，通常用于在 DropdownButton 被禁用时显示 |
| onChanged           | Function                  | 当用户选择一个选项时的回调函数，接收一个泛型参数 T?，表示选择的值            |
| onTap               | Function                  | 当用户点击 DropdownButton 时的回调函数                   |
| elevation           | int                       | 下拉菜单的阴影高度                                     |
| style               | TextStyle                 | 下拉菜单中选项的文本样式                                  |
| underline           | Widget                    | 下拉菜单底部的线条，通常用于指示菜单的边界                         |
| icon                | Widget                    | 下拉箭头图标                                        |
| iconDisabledColor   | Color                     | 下拉箭头图标在禁用状态时的颜色                               |
| iconEnabledColor    | Color                     | 下拉箭头图标在可用状态时的颜色                               |
| iconSize            | double                    | 下拉箭头图标的大小                                     |
| isDense             | bool                      | 是否使用较小的垂直大小，通常用于在较密集的布局中                      |
| isExpanded          | bool                      | 是否将下拉菜单的宽度展开到与父容器一样宽                          |
| itemHeight          | double                    | 每个选项的高度                                       |
| focusColor          | Color                     | 控件获取焦点时的颜色                                    |
| focusNode           | FocusNode                 | 控制控件是否具有焦点                                    |
| autofocus           | bool                      | 是否自动获取焦点                                      |
| dropdownColor       | Color                     | 下拉菜单的背景颜色                                     |
| menuMaxHeight       | double                    | 下拉菜单的最大高度                                     |
| enableFeedback      | bool                      | 是否启用触觉反馈                                      |
| alignment           | AlignmentGeometry         | 下拉菜单的对齐方式                                     |
| borderRadius        | BorderRadius              | 下拉菜单的圆角                                       |
| padding             | EdgeInsetsGeometry        | 下拉菜单的内边距                                      |

### 用于创建一个表单字段版本的下拉框
| 参数名称                | 使用类型                      | 参数介绍                                          |
|---------------------|---------------------------|-----------------------------------------------|
| key                 | Key                       | 用于在树中唯一标识该组件                                  |
| items               | List<DropdownMenuItem<T>> | 一个包含所有选项的列表，每个选项由 DropdownMenuItem<T> 小部件表示   |
| selectedItemBuilder | List<Widget>              | 一个构建器函数，用于在选择的值下方构建一个小部件                      |
| value               | T                         | 当前选中的值，必须与 items 中的某个值相匹配，用于确定默认选中项           |
| hint                | Widget                    | 在下拉菜单中显示的提示内容，通常用于指示用户进行选择                    |
| disabledHint        | Widget                    | 在下拉菜单中显示的禁用时的提示内容，通常用于在 DropdownButton 被禁用时显示 |
| onChanged           | Function                  | 当用户选择一个选项时的回调函数，接收一个泛型参数 T?，表示选择的值            |
| onTap               | Function                  | 当用户点击 DropdownButton 时的回调函数                   |
| elevation           | int                       | 下拉菜单的阴影高度                                     |
| style               | TextStyle                 | 下拉菜单中选项的文本样式                                  |
| underline           | Widget                    | 下拉菜单底部的线条，通常用于指示菜单的边界                         |
| icon                | Widget                    | 下拉箭头图标                                        |
| iconDisabledColor   | Color                     | 下拉箭头图标在禁用状态时的颜色                               |
| iconEnabledColor    | Color                     | 下拉箭头图标在可用状态时的颜色                               |
| iconSize            | double                    | 下拉箭头图标的大小                                     |
| isDense             | bool                      | 是否使用较小的垂直大小，通常用于在较密集的布局中                      |
| isExpanded          | bool                      | 是否将下拉菜单的宽度展开到与父容器一样宽                          |
| itemHeight          | double                    | 每个选项的高度                                       |
| focusColor          | Color                     | 控件获取焦点时的颜色                                    |
| focusNode           | FocusNode                 | 控制控件是否具有焦点                                    |
| autofocus           | bool                      | 是否自动获取焦点                                      |
| dropdownColor       | Color                     | 下拉菜单的背景颜色                                     |
| menuMaxHeight       | double                    | 下拉菜单的最大高度                                     |
| enableFeedback      | bool                      | 是否启用触觉反馈                                      |
| alignment           | AlignmentGeometry         | 下拉菜单的对齐方式                                     |
| borderRadius        | BorderRadius              | 下拉菜单的圆角                                       |
| padding             | EdgeInsetsGeometry        | 下拉菜单的内边距                                      |
| inputDecoration     | InputDecoration           | 用于在表单字段中显示的外观装饰                               |
| isEmpty             | bool                      | 表单字段是否为空                                      |
| isFocused           | bool                      | 表单字段是否获得焦点                                    |




