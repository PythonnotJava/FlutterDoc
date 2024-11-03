# 工具类
> * LinearProgressIndicator：一个线性、条状的进度条。
> * CircularProgressIndicator：一个圆形进度条。
> * BoxDecoration：用于装饰Container等组件的类，可以让组件拥有背景颜色、渐变、圆角边框、阴影等效果。它提供了一些非常灵活的装饰属性，使你可以轻松地定制组件的外观。


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
    this.borderRadius = BorderRadius.zero,
})
```

### LinearProgressIndicator(...)参数解析
| 参数名称              | 使用类型                 | 参数介绍                                                           |
|-------------------|----------------------|----------------------------------------------------------------|
| key               | Key                  | 用于在 Flutter 的组件树中标识该组件，一般用于局部更新、优化等情况                          |
| value             | double               | 表示当前的进度值，范围是 0.0 到 1.0。null 表示不确定的进度（即动画的进度条会一直运动下去），否则会显示具体进度 |
| backgroundColor   | Color                | 进度条的背景颜色，即未填充的部分颜色                                             |
| color             | Color                | 进度条前景颜色，即已填充部分颜色                                               |
| valueColor        | Animation<Color>     | 进度条的颜色动画，可以用于在进度条的前景颜色上设置动画效果                                  |
| minHeight         | double               | 进度条的最小高度，默认为系统默认的进度条高度（一般较细）                                   |
| semanticsLabel    | String               | 用于屏幕阅读器的语义标签，帮助无障碍用户了解组件的用途或状态                                 |
| semanticsValue    | double               | 用于屏幕阅读器的语义值，帮助无障碍用户了解组件的当前进度值                                  |
| borderRadius      | BorderRadiusGeometry | 控制进度条的圆角半径                                                     |

## CircularProgressIndicator类
### 默认构造函数
```text
CircularProgressIndicator({
    super.key,
    super.value,
    super.backgroundColor,
    super.color,
    super.valueColor,
    this.strokeWidth = 4.0,
    this.strokeAlign = strokeAlignCenter,
    super.semanticsLabel,
    super.semanticsValue,
    this.strokeCap,
  })
```

### CircularProgressIndicator(...)参数解析
| 参数名称            | 使用类型             | 参数介绍                                                                 |
|-----------------|------------------|----------------------------------------------------------------------|
| key             | Key              | 用于标识组件的唯一值，主要用于在组件树中查找和控制特定组件实例                                      |
| value           | double           | 进度指示的值                                                               |
| backgroundColor | Color            | 指定进度条背景圆环的颜色，即未完成部分的颜色                                               |
| color           | Color            | 前景色，表示已完成的进度部分的颜色                                                    |
| valueColor      | Animation<Color> | 前景颜色的动画对象，可以设置为 AlwaysStoppedAnimation<Color> 来指定静态颜色，也可以通过动画效果让颜色渐变 |
| strokeWidth     | double           | 指定圆环的宽度                                                              |
| strokeAlign     | double           | 圆环的对齐方式                                                              |
| semanticsLabel  | String           | 无障碍支持的标签，用于描述当前的进度条，通常用于屏幕阅读器读取内容，以帮助视障用户了解组件的作用                     |
| semanticsValue  | String           | 无障碍支持的数值描述，主要用于说明当前进度的数值，以百分比或具体进度形式呈现，供辅助技术使用                       |
| strokeCap       | StrokeCap        | 指定圆环端部的样式                                                            |

### 根据当前平台（如 iOS 或 Android）自动调整圆形进度指示器的外观
```text
CircularProgressIndicator.adaptive({
    super.key,
    super.value,
    super.backgroundColor,
    super.valueColor,
    this.strokeWidth = 4.0,
    super.semanticsLabel,
    super.semanticsValue,
    this.strokeCap,
    this.strokeAlign = strokeAlignCenter,
  })
```

### CircularProgressIndicator.adaptive(...)参数解析
| 参数名称            | 使用类型             | 参数介绍                                                |
|-----------------|------------------|-----------------------------------------------------|
| key             | Key              | 用于标识组件的唯一值，主要用于在组件树中查找和控制特定组件实例                     |
| value           | double           | 进度指示的值                                              |
| backgroundColor | Color            | 指定进度条背景圆环的颜色，即未完成部分的颜色                              |
| valueColor      | Animation<Color> | 前景颜色的动画对象                                           |
| strokeWidth     | double           | 指定圆环的宽度                                             |
| semanticsLabel  | String           | 无障碍支持的标签，用于描述当前的进度条，便于屏幕阅读器等辅助技术理解组件的功能             |
| semanticsValue  | String           | 无障碍支持的数值描述，主要用于说明当前进度的数值，帮助辅助技术提供更好的用户体验            |
| strokeCap       | StrokeCap        | 指定圆环端部的样式                                           |

## BoxDecoration类
### 默认构造函数
```text
BoxDecoration({
    this.color,
    this.image,
    this.border,
    this.borderRadius,
    this.boxShadow,
    this.gradient,
    this.backgroundBlendMode,
    this.shape = BoxShape.rectangle,
  })
```

### CircularProgressIndicator.adaptive(...)参数解析
| 参数名称                | 使用类型                 | 参数介绍                                |
|---------------------|----------------------|-------------------------------------|
| color               | Color                | 用于设置背景颜色，接受一个 Color 对象，如 Colors.red |
| image               | DecorationImage      | 设置背景图片                              |
| border              | BoxBorder            | 定义边框，可以设置边框的颜色、宽度和样式                |
| borderRadius        | BorderRadiusGeometry | 用于设置圆角边框                            |
| boxShadow           | List<BoxShadow>      | 设置阴影效果                              |
| gradient            | Gradient             | 设置渐变效果                              |
| backgroundBlendMode | BlendMode            | 设置背景的混合模式                           |
| shape               | BoxShape             | 用于设置组件的形状                           |

