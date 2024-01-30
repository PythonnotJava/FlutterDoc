# 动画
> Flutter3.0提供了以下的动画类
> * AnimationController：用于管理动画的执行。它控制动画的时间、速度、方向等。
> * CurvedAnimation： Flutter 动画库中的一个类，它用于将一个线性的动画转换为一个非线性的动画，以实现一些弹性、缓冲或自定义的动画效果。
> * Tween：用于在动画的起始值和结束值之间插值。它通常与 AnimationController 和 CurvedAnimation 一起使用，帮助你在动画的生命周期内生成一个值的范围。
> * AnimatedBuilder：用于在动画执行期间重建部件树。通常，它用于包裹需要根据动画值进行重建的小部件树，以避免重新构建整个页面，提高性能。
> * Hero：Hero动画是一种通过在页面之间共享共同的Widget，实现平滑过渡的动画效果。这种动画通常用于在两个页面之间传递共享的UI元素，比如在列表页面和详情页面之间切换时，可以使用Hero动画来产生更流畅的过渡效果。

## AnimationController类
```text
AnimationController({
    double? value,
    this.duration,
    this.reverseDuration,
    this.debugLabel,
    this.lowerBound = 0.0,
    this.upperBound = 1.0,
    this.animationBehavior = AnimationBehavior.normal,
    required TickerProvider vsync,
  })
```

### AnimationController(...)参数解析
| 参数名称              | 使用类型              | 参数介绍                                 |
|-------------------|-------------------|--------------------------------------|
| value             | double            | 动画的当前值                               |
| duration          | Duration          | 正向动画的持续时间（从 lowerBound 到 upperBound） |
| reverseDuration   | Duration          | 反向动画的持续时间（从 upperBound 到 lowerBound） |
| debugLabel        | String            | 用于调试的标签，可选参数，用于标识此动画控制器              |
| lowerBound        | double            | 动画值的下限                               |
| upperBound        | double            | 动画值的上限                               |
| animationBehavior | AnimationBehavior | 动画行为，指定动画如何处理其范围                     |
| vsync             | TickerProvider    | 提供 Ticker 对象的对象，通常是 State 对象，用于驱动动画  |

## 不受限制的动画控制器（这意味着它没有明确的上限和下限）
```text
AnimationController.unbounded({
    double value = 0.0,
    this.duration,
    this.reverseDuration,
    this.debugLabel,
    required TickerProvider vsync,
    this.animationBehavior = AnimationBehavior.preserve,
  })
```

### AnimationController.unbounded(...)参数解析
| 参数名称                | 使用类型                 | 参数介绍                                |
|---------------------|----------------------|-------------------------------------|
| value               | double               | 动画的初始值，默认为 0.0                      |
| duration            | Duration             | 正向动画的持续时间（从当前值到目标值）                 |
| reverseDuration     | Duration             | 反向动画的持续时间（从目标值返回到当前值）               |
| debugLabel          | String               | 用于调试的标签，可选参数，用于标识此动画控制器             |
| vsync               | TickerProvider       | 提供 Ticker 对象的对象，通常是 State 对象，用于驱动动画 |
| animationBehavior   | AnimationBehavior    | 动画行为，指定动画如何处理其范围                    |

## CurvedAnimation类
```text
CurvedAnimation({
    required this.parent,
    required this.curve,
    this.reverseCurve,
  })
```

### CurvedAnimation(...)参数解析
| 参数名称         | 使用类型          | 参数介绍           |
|--------------|---------------|----------------|
| parent       | Animation     | 要包装的父动画        |
| curve        | Curve         | 用于描述动画曲线的对象    |
| reverseCurve | Curve         | 一个可选的曲线，用于反向动画 |

## Tween类
```text
Tween({
    this.begin,
    this.end,
  })
```

### Tween(...)参数解析
| 参数名称   | 使用类型  | 参数介绍                    |
|--------|-------|-------------------------|
| begin  | T     | 动画区间的起始值，可以是任何类型 T 的对象  |
| end    | T     | 动画区间的结束值，也是类型 T 的对象     |

## AnimatedBuilder类
```text
AnimatedBuilder({
    super.key,
    required Listenable animation,
    required super.builder,
    super.child,
  }) 
```

### AnimatedBuilder(...)参数解析
| 参数名称      | 使用类型       | 参数介绍                                                         |
|-----------|------------|--------------------------------------------------------------|
| key       | Key        | 小部件的标识符，可选参数                                                 |
| animation | Listenable | 与此构建器关联的 Listenable 对象，通常是一个 Animation 或 AnimationController |
| builder   | Widget     | BuildContext 和 Widget?，并返回一个小部件树                             |
| child     | Widget     | 一个可选的小部件，作为静态部分，不会在 builder 回调中动态变化                          |

## Hero类
```text
Hero({
    super.key,
    required this.tag,
    this.createRectTween,
    this.flightShuttleBuilder,
    this.placeholderBuilder,
    this.transitionOnUserGestures = false,
    required this.child,
  })
```

### Hero(...)参数解析
| 参数名称                     | 使用类型         | 参数介绍                        |
|--------------------------|--------------|-----------------------------|
| key                      | Key          | 用于传递给Widget类的key参数          |
| tag                      | Object       | 用于标识Hero动画的共享元素             |
| createRectTween          | Tween<Rect>  | 用于定义共享元素在动画过程中的插值           |
| flightShuttleBuilder     | Function     | 用于定义在Hero元素飞行时的过渡Widget的构建器 |
| placeholderBuilder       | Function     | 用于构建Hero动画中的占位Widget        |
| transitionOnUserGestures | bool         | 布尔值，默认为false                |
| child                    | Widget       | 包含Hero动画的实际Widget           |



































