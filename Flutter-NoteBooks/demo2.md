# Text控件
> 文本以及属性
> * Text：用于显示文本的基本组件之一，它用于在应用程序中呈现静态文本内容。
> * TextStyle：用于定义文本样式的类。它可以用于定制文本的字体、大小、颜色、加粗、斜体、下划线等属性。
> * TextSpan：用于构建富文本（Rich Text）的类。它允许你在一个文本中应用不同的样式、添加链接、插入小部件等。
> * TextPainter：用于在画布上绘制文本的工具类。它提供了高度灵活的文本布局和绘制功能，特别适合需要精细控制文本布局或在自定义绘制组件中使用的场景。

## Text类
### 默认构造函数
```text
Text(
    String this.data, {
    super.key,
    this.style,
    this.strutStyle,
    this.textAlign,
    this.textDirection,
    this.locale,
    this.softWrap,
    this.overflow,
    this.textScaleFactor,
    this.maxLines,
    this.semanticsLabel,
    this.textWidthBasis,
    this.textHeightBehavior,
    this.selectionColor,
  })
```

### Text(...)参数解析
| 参数名称               | 使用类型               | 参数介绍                          |
|--------------------|--------------------|-------------------------------|
| data               | String             | 要显示的文本字符串，是一个必需参数             |
| key                | Key                | 继承自父类的键值（key）                 |
| style              | TextStyle          | 文本的样式，包括字体、颜色、大小等，是TextStyle类 |
| strutStyle         | StrutStyle         | 文本基线的样式                       |
| textAlign          | TextAlign          | 文本的对齐方式                       |
| textDirection      | TextDirection      | 文本的方向                         |
| locale             | Locale             | 文本的地区设置                       |
| softWrap           | bool               | 是否自动换行                        |
| overflow           | TextOverflow       | 当文本超出可见范围时的处理方式               |
| textScaleFactor    | double             | 文本的缩放因子                       |
| maxLines           | int                | 文本显示的最大行数                     |
| semanticsLabel     | String             | 用于无障碍功能的语义标签                  |
| textWidthBasis     | TextWidthBasis     | 文本宽度的基础设置                     |
| textHeightBehavior | TextHeightBehavior | 文本高度的行为设置                     |
| selectionColor     | Color              | 文本选择时的颜色                      |

### 用于创建富文本的构造函数
```text
Text.rich(
    InlineSpan this.textSpan, {
    super.key,
    this.style,
    this.strutStyle,
    this.textAlign,
    this.textDirection,
    this.locale,
    this.softWrap,
    this.overflow,
    this.textScaleFactor,
    this.maxLines,
    this.semanticsLabel,
    this.textWidthBasis,
    this.textHeightBehavior,
    this.selectionColor,
  })
```
## Text.rich(...)参数解析
| 参数名称               | 使用类型               | 参数介绍               |
|--------------------|--------------------|--------------------|
| textSpan           | InlineSpan         | 要显示的富文本内容，是一个必需参数  |
| key                | Key                | 继承自父类的键值（key）      |
| style              | TextStyle          | 文本的样式，包括字体、颜色、大小等  |
| strutStyle         | StrutStyle         | 文本基线的样式            |
| textAlign          | TextAlign          | 文本的对齐方式            |
| textDirection      | TextDirection      | 文本的方向              |
| locale             | Locale             | 文本的地区设置            |
| softWrap           | bool               | 是否自动换行             |
| overflow           | TextOverflow       | 当文本超出可见范围时的处理方式    |
| textScaleFactor    | double             | 文本的缩放因子            |
| maxLines           | int                | 文本显示的最大行数          |
| semanticsLabel     | String             | 用于无障碍功能的语义标签       |
| textWidthBasis     | TextWidthBasis     | 文本宽度的基础设置          |
| textHeightBehavior | TextHeightBehavior | 文本高度的行为设置          |
| selectionColor     | Color              | 文本选择时的颜色           |

## TextStyle类
### 默认构造函数
```text
TextStyle({
    this.inherit = true,
    this.color,
    this.backgroundColor,
    this.fontSize,
    this.fontWeight,
    this.fontStyle,
    this.letterSpacing,
    this.wordSpacing,
    this.textBaseline,
    this.height,
    this.leadingDistribution,
    this.locale,
    this.foreground,
    this.background,
    this.shadows,
    this.fontFeatures,
    this.fontVariations,
    this.decoration,
    this.decorationColor,
    this.decorationStyle,
    this.decorationThickness,
    this.debugLabel,
    String? fontFamily,
    List<String>? fontFamilyFallback,
    String? package,
    this.overflow,
  })
```

### TextStyle(...)参数解析
| 参数名称                | 使用类型                    | 参数介绍               |
|---------------------|-------------------------|--------------------|
| inherit             | bool                    | 是否继承父级文本样式，默认为true |
| color               | *Color                  | 文本颜色               |
| backgroundColor     | Color                   | 文本背景颜色             |
| fontSize            | double                  | 字体大小               |
| fontWeight          | FontWeight              | 字体粗细               |
| fontStyle           | FontStyle               | 字体样式，如斜体           |
| letterSpacing       | double                  | 字母间距               |
| wordSpacing         | double                  | 单词间距               |
| textBaseline        | TextBaseline            | 文本基线               |
| height              | double                  | 行高                 |
| leadingDistribution | TextLeadingDistribution | 行高分布               |
| locale              | Locale                  | 地区设置               |
| foreground          | Paint                   | 前景装饰               |
| background          | Paint                   | 背景装饰               |
| shadows             | List<Shadow>            | 阴影效果               |
| fontFeatures        | List<FontFeature>       | 字体特征               |
| fontVariations      | List<FontVariation>     | 字体变体               |
| decoration          | TextDecoration          | 装饰样式               |
| decorationColor     | Color                   | 装饰颜色               |
| decorationStyle     | TextDecorationStyle     | 装饰风格，如虚线           |
| decorationThickness | double                  | 装饰线粗细              |
| debugLabel          | String                  | 调试标签               |
| fontFamily          | String                  | 字体系列               |
| fontFamilyFallback  | List<String>            | 字体系列备选项            |
| package             | String                  | 字体所在的包             |
| overflow            | TextOverflow            | 文本溢出时的处理方式         |
> 备注 
> * Colors类，这里其实使用的Color类，也可以是Colors类，Colors类是一个抽象类型，但是提供了一些颜色的直接指定方式，比如说，Colors.blue。Colors是抽象类，被Color继承接口并拓展，在很多实质是Color类的属性中，你也可以使用Colors类

## TextSpan类
### 默认构造函数
```text
TextSpan({
    this.text,
    this.children,
    super.style,
    this.recognizer,
    MouseCursor? mouseCursor,
    this.onEnter,
    this.onExit,
    this.semanticsLabel,
    this.locale,
    this.spellOut,
  })
```
### TextSpan(...)参数解析
| 参数名称            | 使用类型               | 参数介绍                    |
|-----------------|--------------------|-------------------------|
| text            | String             | 文本内容                    |
| children        | *List<InlineSpan>  | 包含在该文本片段内的子文本片段列表       |
| style           | TextStyle          | 继承自父类的文本样式              |
| recognizer      | *GestureRecognizer | 用于处理识别操作（如点击、长按等）的手势识别器 |
| mouseCursor     | *MouseCursor       | 指定鼠标悬停在该文本片段上时的鼠标指针样式   |
| onEnter         | *Function          | 当鼠标进入该文本片段时的回调函数        |
| onExit          | Function           | 当鼠标离开该文本片段时的回调函数        |
| semanticsLabel  | String             | 用于无障碍功能的语义标签            |
| locale          | Locale             | 文本片段的地区设置               |
| spellOut        | bool               | 是否对该文本片段进行拼写            |
> 备注
> * InlineSpan是一个抽象数据类型，用于创建一个可嵌入文本的可选文本片段。包含TextSpan、WidgetSpan、IconSpan等
> * GestureRecognizer是一个抽象类，用于手势识别交互
> * MouseCursor是一个抽象类，表示鼠标指针样式
> * 这里的Function类实质指的是PointerEnterEventListener，这实际上是一个返回空值的匿名函数，在Flutter的很多控件中，都有这样的链接函数的功能的参数，它们大多都是返回空值的匿名函数，没有特别强调，我都会把它们统一声明为Function类

## TextPainter类
### 默认构造函数
```text
TextPainter({
    InlineSpan? text,
    TextAlign textAlign = TextAlign.start,
    TextDirection? textDirection,
    @Deprecated(
      'Use textScaler instead. '
      'Use of textScaleFactor was deprecated in preparation for the upcoming nonlinear text scaling support. '
      'This feature was deprecated after v3.12.0-2.0.pre.',
    )
    double textScaleFactor = 1.0,
    TextScaler textScaler = TextScaler.noScaling,
    int? maxLines,
    String? ellipsis,
    Locale? locale,
    StrutStyle? strutStyle,
    TextWidthBasis textWidthBasis = TextWidthBasis.parent,
    TextHeightBehavior? textHeightBehavior,
  })
```

### TextPainter(...)参数解析
| 参数名称                  | 使用类型                | 参数介绍                                        |
|-----------------------|---------------------|---------------------------------------------|
| text                  | InlineSpan          | 这是要绘制的文本内容                                  |
| textAlign             | TextAlign           | 设置文本的对齐方式                                   |
| textDirection         | TextDirection       | 定义文本的书写方向                                   |
| textScaleFactor       | TextScaler          | 控制文本的缩放比例                                   |
| textScaler            | double              | 替代textScaleFactor使用的参数，用于控制文本的缩放行为          |
| maxLines              | int                 | 设置文本的最大行数                                   |
| ellipsis              | String              | 如果文本的行数超过了 maxLines，则会在文本末尾添加此省略符号（如 "..."） |
| locale                | Locale              | 设置文本的区域设置，影响字体选择、排版规则等                      |
| strutStyle            | StrutStyle          | 设置文本的 strut 样式，用于定义行间距的样式                   |
| textWidthBasis        | TextWidthBasis      | 设置文本布局时如何计算宽度                               |
| textHeightBehavior    | TextHeightBehavior  | 控制文本的高度行为                                   |


