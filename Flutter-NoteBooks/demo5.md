# Source资源类
> * Image：用于加载和显示图像的基本资源类。它提供了各种方法来加载和展示图像资源。
> * AssetImage：用于加载应用程序内部的图像资源。可以通过指定资源路径（文件夹一般叫做assets）加载应用程序包中的图像文件。
> * NetworkImage：用于从网络加载图像资源。可以通过指定网络图片的URL来加载远程图像。
> * FileImage：用于加载本地文件系统中的图像资源。可以通过指定本地文件路径加载设备上的图像文件。
> * MemoryImage：用于从内存中加载图像。
> * Icon：显示矢量图标的小部件。它提供了各种内置图标，如箭头、图表、通知图标等，并且还支持自定义图标。
> * ImageIcon：用于显示图标的小部件。它是基于图片资源创建的，可以将图标显示为一个图像。
> * AnimatedIcon：用于显示动画图标。
> * CircleAvatar：用于显示圆形的用户头像或图标。
> * DecorationImage：用于在容器（如 Container）的背景或前景中显示图像。

## Image类
### 默认构造函数
```text
Image({
    super.key,
    required this.image,
    this.frameBuilder,
    this.loadingBuilder,
    this.errorBuilder,
    this.semanticLabel,
    this.excludeFromSemantics = false,
    this.width,
    this.height,
    this.color,
    this.opacity,
    this.colorBlendMode,
    this.fit,
    this.alignment = Alignment.center,
    this.repeat = ImageRepeat.noRepeat,
    this.centerSlice,
    this.matchTextDirection = false,
    this.gaplessPlayback = false,
    this.isAntiAlias = false,
    this.filterQuality = FilterQuality.low,
  })
```

### Image(...)参数解析
| 参数名称                 | 使用类型                   | 参数介绍                                        |
|----------------------|------------------------|---------------------------------------------|
| key                  | Key                    | 用于标识Image实例的可选键                             |
| image                | *ImageProvider<Object> | 要加载和显示的图像资源，可以是AssetImage、NetworkImage类等的实例 |
| frameBuilder         | *Widget                | 用于构建图像帧的回调函数                                |
| loadingBuilder       | Widget                 | 在图像加载过程中显示的占位图像的构建器回调函数                     |
| errorBuilder         | Widget                 | 在图像加载失败时显示的错误图像的构建器回调函数                     |
| semanticLabel        | String                 | 图像的语义标签，用于辅助功能                              |
| excludeFromSemantics | bool                   | 是否将图像排除在辅助功能树之外，默认为false                    |
| width                | double                 | 图像的宽度                                       |
| height               | double                 | 图像的高度                                       |
| color                | Color                  | 要应用于图像的颜色                                   |
| opacity              | Animation<double>      | 图像的不透明度                                     |
| colorBlendMode       | BlendMode              | 图像与颜色混合的模式                                  |
| fit                  | BoxFit                 | 图像在容器中的适应方式                                 |
| alignment            | *Alignment             | 图像在容器中的对齐方式                                 |
| repeat               | ImageRepeat            | 图像在容器中的重复方式                                 |
| centerSlice          | Rect                   | 指定可缩放的图像的中心区域                               |
| matchTextDirection   | bool                   | 是否根据文本的方向来确定图像的方向                           |
| gaplessPlayback      | bool                   | 在更改图像时是否显示过渡效果，默认为false                     |
| isAntiAlias          | bool                   | 图像是否使用抗锯齿，默认为false                          |
| filterQuality        | FilterQuality          | 图像的过滤质量                                     |

> 备注
> * ImageProvider是一个抽象类，用于从不同的数据源获取图像，并将其作为Image的image参数使用。ImageProvider的常用子类包括：
> > * AssetImage: 从应用程序的资源目录加载图像。  
> > * NetworkImage: 从网络加载图像。
> > * FileImage: 从文件系统加载图像。
> > * MemoryImage: 从内存加载图像。
> > > 这些子类都实现了ImageProvider的抽象方法，以实现不同数据源的图像加载和处理逻辑。
> * 相较于之前的参数类型是Function的回调函数（实质是返回值为void），此回调函数的返回值是Widget
> * Alignment和AlignmentGeometry都是用于指定控件在容器中的对齐方式的类，且前者是后者（抽象类）的具体实现。

### 加载网络图片
```text
Image.network(
    String src, {
    super.key,
    double scale = 1.0,
    this.frameBuilder,
    this.loadingBuilder,
    this.errorBuilder,
    this.semanticLabel,
    this.excludeFromSemantics = false,
    this.width,
    this.height,
    this.color,
    this.opacity,
    this.colorBlendMode,
    this.fit,
    this.alignment = Alignment.center,
    this.repeat = ImageRepeat.noRepeat,
    this.centerSlice,
    this.matchTextDirection = false,
    this.gaplessPlayback = false,
    this.filterQuality = FilterQuality.low,
    this.isAntiAlias = false,
    Map<String, String>? headers,
    int? cacheWidth,
    int? cacheHeight,
  })
```

### Image.network(...)参数解析
| 参数名称                 | 使用类型                | 参数介绍                         |
|----------------------|---------------------|------------------------------|
| src                  | String              | 要加载的图像的URL                   |
| key                  | Key                 | 用于标识Image.network实例的可选键      |
| scale                | double              | 图像的缩放比例，默认为1.0               |
| frameBuilder         | Widget              | 用于构建图像帧的回调函数                 |
| loadingBuilder       | Widget              | 在图像加载过程中显示的占位图像的构建器回调函数      |
| errorBuilder         | Widget              | 在图像加载失败时显示的错误图像的构建器回调函数      |
| semanticLabel        | String              | 图像的语义标签，用于辅助功能               |
| excludeFromSemantics | bool                | 是否将图像排除在辅助功能树之外，默认为false     |
| width                | double              | 图像的宽度                        |
| height               | double              | 图像的高度                        |
| color                | Color               | 要应用于图像的颜色                    |
| opacity              | Animation<double>   | 图像的不透明度                      |
| colorBlendMode       | BlendMode           | 图像与颜色混合的模式                   |
| fit                  | BoxFit              | 图像在容器中的适应方式                  |
| alignment            | Alignment           | 图像在容器中的对齐方式，默认为居中对齐          |
| repeat               | ImageRepeat         | 图像在容器中的重复方式                  |
| centerSlice          | Rect                | 指定可缩放的图像的中心区域                |
| matchTextDirection   | bool                | 是否根据文本的方向来确定图像的方向            |
| gaplessPlayback      | bool                | 在更改图像时是否显示过渡效果，默认为false      |
| filterQuality        | FilterQuality       | 图像的过滤质量，默认为FilterQuality.low |
| isAntiAlias          | bool                | 图像是否使用抗锯齿，默认为false           |
| headers              | Map<String, String> | 请求图像时附加的HTTP头信息              |
| cacheWidth           | int                 | 在缓存图像时，指定图像的宽度               |
| cacheHeight          | int                 | 在缓存图像时，指定图像的高度               |

### 加载本地图片
```text
Image.file(
    File file, {
    super.key,
    double scale = 1.0,
    this.frameBuilder,
    this.errorBuilder,
    this.semanticLabel,
    this.excludeFromSemantics = false,
    this.width,
    this.height,
    this.color,
    this.opacity,
    this.colorBlendMode,
    this.fit,
    this.alignment = Alignment.center,
    this.repeat = ImageRepeat.noRepeat,
    this.centerSlice,
    this.matchTextDirection = false,
    this.gaplessPlayback = false,
    this.isAntiAlias = false,
    this.filterQuality = FilterQuality.low,
    int? cacheWidth,
    int? cacheHeight,
  }) 
```

### Image.file(...)参数解析
| 参数名称                 | 使用类型              | 参数介绍                         |
|----------------------|-------------------|------------------------------|
| file                 | File              | 要加载的图像文件的File对象              |
| key                  | key               | 用于标识Image.file实例的可选键         |
| scale                | double            | 图像的缩放比例，默认为1.0               |
| frameBuilder         | Widget            | 用于构建图像帧的回调函数                 |
| errorBuilder         | Widget            | 在图像加载失败时显示的错误图像的构建器回调函数      |
| semanticLabel        | String            | 图像的语义标签，用于辅助功能               |
| excludeFromSemantics | bool              | 是否将图像排除在辅助功能树之外，默认为false     |
| width                | double            | 图像的宽度                        |
| height               | double            | 图像的高度                        |
| color                | Color             | 要应用于图像的颜色                    |
| opacity              | Animation<double> | 图像的不透明度                      |
| colorBlendMode       | BlendMode         | 图像与颜色混合的模式                   |
| fit                  | BoxFit            | 图像在容器中的适应方式                  |
| alignment            | Alignment         | 图像在容器中的对齐方式，默认为居中对齐          |
| repeat               | ImageRepeat       | 图像在容器中的重复方式                  |
| centerSlice          | Rect              | 指定可缩放的图像的中心区域                |
| matchTextDirection   | bool              | 是否根据文本的方向来确定图像的方向            |
| gaplessPlayback      | bool              | 在更改图像时是否显示过渡效果，默认为false      |
| isAntiAlias          | bool              | 图像是否使用抗锯齿，默认为false           |
| filterQuality        | FilterQuality     | 图像的过滤质量，默认为FilterQuality.low |
| cacheWidth           | int               | 在缓存图像时，指定图像的宽度               |
| cacheHeight          | int               | 在缓存图像时，指定图像的高度               |

### 加载项目中的资源图片
```text
Image.asset(
    String name, {
    super.key,
    AssetBundle? bundle,
    this.frameBuilder,
    this.errorBuilder,
    this.semanticLabel,
    this.excludeFromSemantics = false,
    double? scale,
    this.width,
    this.height,
    this.color,
    this.opacity,
    this.colorBlendMode,
    this.fit,
    this.alignment = Alignment.center,
    this.repeat = ImageRepeat.noRepeat,
    this.centerSlice,
    this.matchTextDirection = false,
    this.gaplessPlayback = false,
    this.isAntiAlias = false,
    String? package,
    this.filterQuality = FilterQuality.low,
    int? cacheWidth,
    int? cacheHeight,
  })
```

### Image.asset(...)参数解析
| 参数名称                 | 使用类型              | 参数介绍                                   |
|----------------------|-------------------|----------------------------------------|
| name                 | String            | 要加载的图像资源的名称                            |
| key                  | Key               | 用于标识Image.asset实例的可选键                  |
| bundle               | AssetBundle       | 要从中加载图像的AssetBundle，默认为当前包的AssetBundle |
| frameBuilder         | Widget            | 用于构建图像帧的回调函数                           |
| errorBuilder         | Widget            | 在图像加载失败时显示的错误图像的构建器回调函数                |
| semanticLabel        | String            | 图像的语义标签，用于辅助功能                         |
| excludeFromSemantics | bool              | 是否将图像排除在辅助功能树之外，默认为false               |
| scale                | double            | 图像的缩放比例                                |
| width                | double            | 图像的宽度                                  |
| height               | double            | 图像的高度                                  |
| color                | Color             | 要应用于图像的颜色                              |
| opacity              | Animation<double> | 图像的不透明度                                |
| colorBlendMode       | BlendMode         | 图像与颜色混合的模式                             |
| fit                  | BoxFit            | 图像在容器中的适应方式                            |
| alignment            | Alignment         | 图像在容器中的对齐方式，默认为居中对齐                    |
| repeat               | ImageRepeat       | 图像在容器中的重复方式                            |
| centerSlice          | Rect              | 指定可缩放的图像的中心区域                          |
| matchTextDirection   | bool              | 是否根据文本的方向来确定图像的方向                      |
| gaplessPlayback      | bool              | 在更改图像时是否显示过渡效果，默认为false                |
| isAntiAlias          | bool              | 图像是否使用抗锯齿，默认为false                     |
| package              | String            | 图像所属的包名称                               |
| filterQuality        | FilterQuality     | 图像的过滤质量，默认为FilterQuality.low           |
| cacheWidth           | int               | 在缓存图像时，指定图像的宽度                         |
| cacheHeight          | int               | 在缓存图像时，指定图像的高度                         |

### 从内存中读取文件资源
```text
Image.memory(
    Uint8List bytes, {
    super.key,
    double scale = 1.0,
    this.frameBuilder,
    this.errorBuilder,
    this.semanticLabel,
    this.excludeFromSemantics = false,
    this.width,
    this.height,
    this.color,
    this.opacity,
    this.colorBlendMode,
    this.fit,
    this.alignment = Alignment.center,
    this.repeat = ImageRepeat.noRepeat,
    this.centerSlice,
    this.matchTextDirection = false,
    this.gaplessPlayback = false,
    this.isAntiAlias = false,
    this.filterQuality = FilterQuality.low,
    int? cacheWidth,
    int? cacheHeight,
  })
```

### Image.memory(...)参数解析
| 参数名称                 | 使用类型              | 参数介绍                                                  |
|----------------------|-------------------|-------------------------------------------------------|
| bytes                | Uint8List         | 要加载的图像数据的字节列表（Uint8List）                              |
| key                  | Key               | 用于标识Image.memory实例的可选键                                |
| scale                | double            | 图像的缩放比例，默认为1.0                                        |
| frameBuilder         | Widget            | 用于构建图像帧的回调函数                                          |
| errorBuilder         | Widget            | 在图像加载失败时显示的错误图像的构建器回调函数                               |
| semanticLabel        | String            | 图像的语义标签，用于辅助功能                                        |
| excludeFromSemantics | bool              | 是否将图像排除在辅助功能树之外，默认为false                              |
| width                | double            | 图像的宽度                                                 |
| height               | double            | 图像的高度                                                 |
| color                | Color             | 要应用于图像的颜色                                             |
| opacity              | Animation<double> | 图像的不透明度                                               |
| colorBlendMode       | BlendMode         | 图像与颜色混合的模式                                            |
| fit                  | BoxFit            | 图像在容器中的适应方式，如BoxFit.contain、BoxFit.cover等             |
| alignment            | Alignment         | 图像在容器中的对齐方式，默认为居中对齐                                   |
| repeat               | ImageRepeat       | 图像在容器中的重复方式，如ImageRepeat.noRepeat、ImageRepeat.repeat等 |
| centerSlice          | Rect              | 指定可缩放的图像的中心区域                                         |
| matchTextDirection   | bool              | 是否根据文本的方向来确定图像的方向                                     |
| gaplessPlayback      | bool              | 在更改图像时是否显示过渡效果，默认为false                               |
| isAntiAlias          | bool              | 图像是否使用抗锯齿，默认为false                                    |
| filterQuality        | FilterQuality     | 图像的过滤质量，默认为FilterQuality.low                          |
| cacheWidth           | int               | 在缓存图像时，指定图像的宽度                                        |
| cacheHeight          | int               | 在缓存图像时，指定图像的高度                                        |


## AssetImage类
### 默认构造函数
```text
AssetImage(
    this.assetName, {
    this.bundle,
    this.package,
  })
```
### AssetImage(...)参数解析
| 参数名称      | 使用类型        | 参数介绍                                   |
|-----------|-------------|----------------------------------------|
| assetName | String      | 要加载的图像资源的名称                            |
| bundle    | AssetBundle | 要从中加载图像的AssetBundle，默认为当前包的AssetBundle |
| package   | String      | 图像所属的包名称                               |

## NetworkImage类
### 默认构造函数
```text
NetworkImage(   
    String url, 
    {   
        ouble scale,   
        Map<String, String>? headers, 
    })
```

### NetworkImage(...)参数解析
| 参数名称    | 使用类型                | 参数介绍            |
|---------|---------------------|-----------------|
| url     | String              | 要加载的图像的URL地址    |
| scale   | double              | 图像的缩放比例，默认为1.0  |
| headers | Map<String, String> | 用于发送HTTP请求时的请求头 |

## FileImage类
### 默认构造函数
```text
FileImage(
    this.file, { 
    this.scale = 1.0 
})
```

### FileImage(...)参数解析
| 参数名称   | 使用类型    | 参数介绍               |
|--------|---------|--------------------|
| file   | File    | 要显示的图像文件           |
| scale  | double  | 可选参数，用于指定图像的缩放比例   |

## MemoryImage类
### 默认构造函数
```text
MemoryImage(
    this.bytes, { 
    this.scale = 1.0 
    })
```

### MemoryImage(...)参数解析
| 参数名称   | 使用类型      | 参数介绍             |
|--------|-----------|------------------|
| bytes  | Uint8List | 要显示的图像的字节数据      |
| scale  | double    | 可选参数，用于指定图像的缩放比例 |

## Icon类
### 默认构造函数
```text
Icon(
    this.icon, {
    super.key,
    this.size,
    this.fill,
    this.weight,
    this.grade,
    this.opticalSize,
    this.color,
    this.shadows,
    this.semanticLabel,
    this.textDirection,
  })
```

### Icon(...)参数解析
| 参数名称            | 使用类型            | 参数介绍                |
|-----------------|-----------------|---------------------|
| icon            | IconData        | 必需的参数，用于指定图标的标识符    |
| key             | Key             | 用于在小部件树中唯一标识Icon小部件 |
| size            | double          | 用于指定图标的大小           |
| fill            | double          | 用于指定填充颜色            |
| weight          | double          | 用于指定图标的权重           |
| grade           | double          | 用于指定图标的等级           |
| opticalSize     | double          | 用于指定图标的视觉大小         |
| color           | Color           | 用于指定图标的颜色           |
| shadows         | List<Shadow>    | 用于指定阴影效果            |
| semanticLabel   | String          | 用于为图标提供语义描述，用于辅助功能  |
| textDirection   | TextDirection   | 用于指定文本方向            |

## ImageIcon类
### 默认构造函数
```text
ImageIcon(
    this.image, {
    super.key,
    this.size,
    this.color,
    this.semanticLabel,
  })
```

### ImageIcon(...)参数解析
| 参数名称            | 使用类型                  | 参数介绍                     |
|-----------------|-----------------------|--------------------------|
| image           | ImageProvider<Object> | 必需的参数，用于指定图像的来源          |
| key             | Key                   | 用于在小部件树中唯一标识ImageIcon小部件 |
| size            | double                | 用于指定图像图标的大小              |
| color           | Color                 | 用于指定图像图标的颜色              |
| semanticLabel   | String                | 用于为图像图标提供语义描述，用于辅助功能     |

## AnimatedIcon类
### 默认构造函数
```text
AnimatedIcon({
    super.key,
    required this.icon,
    required this.progress,
    this.color,
    this.size,
    this.semanticLabel,
    this.textDirection,
  })
```

### AnimatedIcon(...)参数解析
| 参数名称              | 使用类型              | 参数介绍                    |
|-------------------|-------------------|-------------------------|
| key               | key               | 小部件的标识符，用于识别和检索小部件      |
| icon              | AnimatedIconData  | 要显示的动画图标                |
| progress          | Animation<double> | 动画的进度，是一个从0.0到1.0之间的动画值 |
| color             | Color             | 图标的颜色                   |
| size              | double            | 图标的大小                   |
| semanticLabel     | String            | 用于辅助功能的语义标签，描述了图标的含义    |
| textDirection     | TextDirection     | 文本方向                    |

## CircleAvatar类
### 默认构造函数
```text
CircleAvatar({
    super.key,
    this.child,
    this.backgroundColor,
    this.backgroundImage,
    this.foregroundImage,
    this.onBackgroundImageError,
    this.onForegroundImageError,
    this.foregroundColor,
    this.radius,
    this.minRadius,
    this.maxRadius,
  }) 
```

### CircleAvatar参数解析
| 参数名称                   | 使用类型                  | 参数介绍                       |
|------------------------|-----------------------|----------------------------|
| key                    | Key                   | 继承自父类的可选参数，用于标识控件的唯一性      |
| child                  | Widget                | 要显示在圆形区域中心的控件，可以是图像、图标、文本等 |
| backgroundColor        | Color                 | 圆形区域的背景颜色                  |
| backgroundImage        | ImageProvider<Object> | 圆形区域的背景图像                  |
| foregroundImage        | ImageProvider<Object> | 圆形区域的前景图像                  |
| onBackgroundImageError | Function              | 当背景图像加载出错时的回调函数            |
| onForegroundImageError | Function              | 当前景图像加载出错时的回调函数            |
| foregroundColor        | Color                 | 前景图像的颜色                    |
| radius                 | double                | 圆形区域的半径大小                  |
| minRadius              | double                | 圆形区域的最小半径大小                |
| maxRadius              | double                | 圆形区域的最大半径大小                |

## DecorationImage类
### 默认构造函数
```text
DecorationImage({
    required this.image,
    this.onError,
    this.colorFilter,
    this.fit,
    this.alignment = Alignment.center,
    this.centerSlice,
    this.repeat = ImageRepeat.noRepeat,
    this.matchTextDirection = false,
    this.scale = 1.0,
    this.opacity = 1.0,
    this.filterQuality = FilterQuality.low,
    this.invertColors = false,
    this.isAntiAlias = false,
  })
```

### DecorationImage(...)参数解析
| 参数名称               | 使用类型                  | 参数介绍                                                                            |
|--------------------|-----------------------|---------------------------------------------------------------------------------|
| image              | ImageProvider<Object> | 必需参数，表示要显示的图像                                                                   |
| onError            | Function              | 当加载图像时发生错误时会调用的回调函数                                                             |
| colorFilter        | ColorFilter           | 用于对图像应用颜色滤镜                                                                     |
| fit                | BoxFit                | 表示如何适应容器来展示图像                                                                   |
| alignment          | AlignmentGeometry     | 表示图像在容器中的对齐方式                                                                   |
| centerSlice        | Rect                  | 用于定义一个九宫格区域（center slice），该区域会保持其原始大小，而其他部分将被拉伸以填充容器。仅在 fit 设置为 BoxFit.fill 时生效 |
| repeat             | ImageRepeat           | 表示图像如何在容器中平铺                                                                    |
| matchTextDirection | bool                  | 表示是否根据文本的方向来匹配图像的方向                                                             |
| scale              | double                | 用于对图像进行缩放                                                                       |
| opacity            | double                | 表示图像的不透明度                                                                       |
| filterQuality      | FilterQuality         | 表示图像的滤镜质量                                                                       |
| invertColors       | bool                  | 表示是否反转图像的颜色                                                                     |
| isAntiAlias        | bool                  | 表示是否使用抗锯齿来渲染图像                                                                  |
