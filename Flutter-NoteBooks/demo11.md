# 手势操作
> GestureDetector：是一个用于处理用户手势操作的组件，它可以包裹其他组件，并监听用户的点击、滑动、缩放等手势事件。以下是一些 GestureDetector 常用的手势属性和事件处理
> Scrollable：用于实现可滚动的内容。

## GestureDetector类
### 默认构造函数
```text
GestureDetector({
    super.key,
    this.child,
    this.onTapDown,
    this.onTapUp,
    this.onTap,
    this.onTapCancel,
    this.onSecondaryTap,
    this.onSecondaryTapDown,
    this.onSecondaryTapUp,
    this.onSecondaryTapCancel,
    this.onTertiaryTapDown,
    this.onTertiaryTapUp,
    this.onTertiaryTapCancel,
    this.onDoubleTapDown,
    this.onDoubleTap,
    this.onDoubleTapCancel,
    this.onLongPressDown,
    this.onLongPressCancel,
    this.onLongPress,
    this.onLongPressStart,
    this.onLongPressMoveUpdate,
    this.onLongPressUp,
    this.onLongPressEnd,
    this.onSecondaryLongPressDown,
    this.onSecondaryLongPressCancel,
    this.onSecondaryLongPress,
    this.onSecondaryLongPressStart,
    this.onSecondaryLongPressMoveUpdate,
    this.onSecondaryLongPressUp,
    this.onSecondaryLongPressEnd,
    this.onTertiaryLongPressDown,
    this.onTertiaryLongPressCancel,
    this.onTertiaryLongPress,
    this.onTertiaryLongPressStart,
    this.onTertiaryLongPressMoveUpdate,
    this.onTertiaryLongPressUp,
    this.onTertiaryLongPressEnd,
    this.onVerticalDragDown,
    this.onVerticalDragStart,
    this.onVerticalDragUpdate,
    this.onVerticalDragEnd,
    this.onVerticalDragCancel,
    this.onHorizontalDragDown,
    this.onHorizontalDragStart,
    this.onHorizontalDragUpdate,
    this.onHorizontalDragEnd,
    this.onHorizontalDragCancel,
    this.onForcePressStart,
    this.onForcePressPeak,
    this.onForcePressUpdate,
    this.onForcePressEnd,
    this.onPanDown,
    this.onPanStart,
    this.onPanUpdate,
    this.onPanEnd,
    this.onPanCancel,
    this.onScaleStart,
    this.onScaleUpdate,
    this.onScaleEnd,
    this.behavior,
    this.excludeFromSemantics = false,
    this.dragStartBehavior = DragStartBehavior.start,
    this.trackpadScrollCausesScale = false,
    this.trackpadScrollToScaleFactor = kDefaultTrackpadScrollToScaleFactor,
    this.supportedDevices,
  })
```

### GestureDetector类(...)参数解析
| 参数名称                           | 使用类型                    | 参数介绍                                               |
|--------------------------------|-------------------------|----------------------------------------------------|
| key                            | Key                     | 用于接收父类的 key，用于构建 Widget 树的唯一标识                     |
| child                          | Widget                  | 被 GestureDetector 包裹的子组件，这是 GestureDetector 所作用的范围 |
| onTapDown                      | Function                | 当用户按下屏幕时触发的回调函数                                    |
| onTapUp                        | Function                | 当用户在屏幕上抬起手指时触发的回调函数                                |
| onTap                          | Function                | 用户轻触屏幕时触发的回调函数                                     |
| onTapCancel                    | Function                | 当轻触被取消时触发的回调函数，例如，用户按下后移出 GestureDetector 区域       |
| onSecondaryTap                 | Function                | 当用户使用第二个手指轻触屏幕时触发的回调函数                             |
| onSecondaryTapDown             | Function                | 当用户用第二个手指按下屏幕时触发的回调函数                              |
| onSecondaryTapUp               | Function                | 当用户用第二个手指在屏幕上抬起时触发的回调函数                            |
| onSecondaryTapCancel           | Function                | 当第二个手指轻触被取消时触发的回调函数                                |
| onTertiaryTapDown              | Function                | 当用户用第三个手指按下屏幕时触发的回调函数                              |
| onTertiaryTapUp                | Function                | 当用户用第三个手指在屏幕上抬起时触发的回调函数                            |
| onTertiaryTapCancel            | Function                | 当第三个手指轻触被取消时触发的回调函数                                |
| onDoubleTapDown                | Function                | 当用户双击屏幕时触发的回调函数                                    |
| onDoubleTap                    | Function                | 当用户双击屏幕时触发的回调函数                                    |
| onDoubleTapCancel              | Function                | 当双击被取消时触发的回调函数                                     |
| onLongPressDown                | Function                | 当用户长按屏幕时触发的回调函数                                    |
| onLongPressCancel              | Function                | 当长按被取消时触发的回调函数                                     |
| onLongPress                    | Function                | 当用户长按屏幕一定时间后触发的回调函数                                |
| onLongPressStart               | Function                | 当长按开始时触发的回调函数                                      |
| onLongPressMoveUpdate          | Function                | 当长按移动时触发的回调函数                                      |
| onLongPressUp                  | Function                | 当长按抬起时触发的回调函数                                      |
| onLongPressEnd                 | Function                | 当长按结束时触发的回调函数                                      |
| onSecondaryLongPressDown       | Function                | 当用户使用第二个手指长按屏幕时触发的回调函数                             |
| onSecondaryLongPressCancel     | Function                | 当第二个手指长按被取消时触发的回调函数                                |
| onSecondaryLongPress           | Function                | 当用户使用第二个手指长按屏幕一定时间后触发的回调函数                         |
| onSecondaryLongPressStart      | Function                | 当第二个手指长按开始时触发的回调函数                                 |
| onSecondaryLongPressMoveUpdate | Function                | 当第二个手指长按移动时触发的回调函数                                 |
| onSecondaryLongPressUp         | Function                | 当第二个手指长按抬起时触发的回调函数                                 |
| onSecondaryLongPressEnd        | Function                | 当第二个手指长按结束时触发的回调函数                                 |
| onTertiaryLongPressDown        | Function                | 当用户使用第三个手指长按屏幕时触发的回调函数                             |
| onTertiaryLongPressCancel      | Function                | 当第三个手指长按被取消时触发的回调函数                                |
| onTertiaryLongPress            | Function                | 当用户使用第三个手指长按屏幕一定时间后触发的回调函数                         |
| onTertiaryLongPressStart       | Function                | 当第三个手指长按开始时触发的回调函数                                 |
| onTertiaryLongPressMoveUpdate  | Function                | 当第三个手指长按移动时触发的回调函数                                 |
| onTertiaryLongPressUp          | Function                | 当第三个手指长按抬起时触发的回调函数                                 |
| onTertiaryLongPressEnd         | Function                | 当第三个手指长按结束时触发的回调函数                                 |
| onVerticalDragDown             | Function                | 当用户在垂直方向开始拖动时触发的回调函数                               |
| onVerticalDragStart            | Function                | 当用户在垂直方向开始拖动时触发的回调函数                               |
| onVerticalDragUpdate           | Function                | 当用户在垂直方向拖动时触发的回调函数                                 |
| onVerticalDragEnd              | Function                | 当用户在垂直方向拖动结束时触发的回调函数                               |
| onVerticalDragCancel           | Function                | 当垂直拖动被取消时触发的回调函数                                   |
| onHorizontalDragDown           | Function                | 当用户在水平方向开始拖动时触发的回调函数                               |
| onHorizontalDragStart          | Function                | 当用户在水平方向开始拖动时触发的回调函数                               |
| onHorizontalDragUpdate         | Function                | 当用户在水平方向拖动时触发的回调函数                                 |
| onHorizontalDragEnd            | Function                | 当用户在水平方向拖动结束时触发的回调函数                               |
| onHorizontalDragCancel         | Function                | 当水平拖动被取消时触发的回调函数                                   |
| onForcePressStart              | Function                | 当用户使用力按压屏幕时触发的回调函数                                 |
| onForcePressPeak               | Function                | 当力按压的强度达到峰值时触发的回调函数                                |
| onForcePressUpdate             | Function                | 当力按压的强度更新时触发的回调函数                                  |
| onForcePressEnd                | Function                | 当力按压结束时触发的回调函数                                     |
| onPanDown                      | Function                | 当用户开始拖动（手指接触屏幕）时触发的回调函数                            |
| onPanStart                     | Function                | 当用户开始拖动时触发的回调函数                                    |
| onPanUpdate                    | Function                | 当用户拖动时触发的回调函数                                      |
| onPanEnd                       | Function                | 当用户拖动结束时触发的回调函数                                    |
| onPanCancel                    | Function                | 当拖动被取消时触发的回调函数                                     |
| onScaleStart                   | Function                | 当用户开始缩放时触发的回调函数                                    |
| onScaleUpdate                  | Function                | 当用户缩放时触发的回调函数                                      |
| onScaleEnd                     | Function                | 当用户缩放结束时触发的回调函数                                    |
| behavior                       | HitTestBehavior         | 定义了用户如何与 GestureDetector 交互的策略                     |
| excludeFromSemantics           | bool                    | 是否排除此 GestureDetector 从语义树中                        |
| dragStartBehavior              | DragStartBehavior       | 定义了拖动行为的启动方式                                       |
| trackpadScrollCausesScale      | bool                    | 定义了是否使用触摸板滚动触发缩放                                   |
| trackpadScrollToScaleFactor    | Offset                  | 触摸板滚动触发缩放的因子                                       |
| supportedDevices               | Set<PointerDeviceKind>  | 一个可选的设备列表，定义了支持 GestureDetector 的设备                |

## Scrollable类
### 默认构造函数
```text
Scrollable({
    super.key,
    this.axisDirection = AxisDirection.down,
    this.controller,
    this.physics,
    required this.viewportBuilder,
    this.incrementCalculator,
    this.excludeFromSemantics = false,
    this.semanticChildCount,
    this.dragStartBehavior = DragStartBehavior.start,
    this.restorationId,
    this.scrollBehavior,
    this.clipBehavior = Clip.hardEdge,
    this.hitTestBehavior = HitTestBehavior.opaque,
  }) 
```

### Scrollable(...)参数解析
| 参数名称                 | 使用类型              | 参数介绍                             |
|----------------------|-------------------|----------------------------------|
| key                  | Key               | 用于接收父类的 key，用于构建 Widget 树的唯一标识   |
| axisDirection        | AxisDirection     | 指定滚动的方向                          |
| controller           | ScrollController  | 用于控制滚动的位置和行为，可以在需要时手动控制滚动或监听滚动事件 |
| physics              | ScrollPhysics     | 控制滚动的物理效果，例如弹性、吸附等               |
| viewportBuilder      | Widget Function(  | 回调函数，返回一个构建视口内容的 Widget          |
| incrementCalculator  | double Function   | 允许自定义滚动增量的计算方式，用于更复杂的滚动需求        |
| excludeFromSemantics | bool              | 是否参与语义树的构建                       |
| semanticChildCount   | int               | 指定可滚动区域中子组件的数量，用于辅助功能的描述         |
| dragStartBehavior    | DragStartBehavior | 控制拖动手势的起始行为                      |
| restorationId        | Stri              | 用于状态恢复的标识符，支持在应用恢复时保存和恢复滚动位置     |
| scrollBehavior       | ScrollBehavior    | 用于自定义滚动行为，可以通过这个参数更改滚动的视觉效果和交互   |
| clipBehavior         | Cl                | 指定如何剪裁内容，控制可视区域的边界行为             |
| hitTestBehavior      | HitTestBehavior   | 指定组件的点击区域，控制是否响应触摸事件             |




