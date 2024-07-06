# 主题
> * ThemeData：定义了一些应用程序的外观和主题属性。
> * CupertinoThemeData：用于定义 Cupertino风格主题的类

## ThemeData类(ThemeData.raw方法同理)
```text
ThemeData({
    bool? applyElevationOverlayColor,
    NoDefaultCupertinoThemeData? cupertinoOverrideTheme,
    Iterable<ThemeExtension<dynamic>>? extensions,
    InputDecorationTheme? inputDecorationTheme,
    MaterialTapTargetSize? materialTapTargetSize,
    PageTransitionsTheme? pageTransitionsTheme,
    TargetPlatform? platform,
    ScrollbarThemeData? scrollbarTheme,
    InteractiveInkFeatureFactory? splashFactory,
    bool? useMaterial3,
    VisualDensity? visualDensity,
    Brightness? brightness,
    Color? canvasColor,
    Color? cardColor,
    ColorScheme? colorScheme,
    Color? colorSchemeSeed,
    Color? dialogBackgroundColor,
    Color? disabledColor,
    Color? dividerColor,
    Color? focusColor,
    Color? highlightColor,
    Color? hintColor,
    Color? hoverColor,
    Color? indicatorColor,
    Color? primaryColor,
    Color? primaryColorDark,
    Color? primaryColorLight,
    MaterialColor? primarySwatch,
    Color? scaffoldBackgroundColor,
    Color? secondaryHeaderColor,
    Color? shadowColor,
    Color? splashColor,
    Color? unselectedWidgetColor,
    String? fontFamily,
    List<String>? fontFamilyFallback,
    String? package,
    IconThemeData? iconTheme,
    IconThemeData? primaryIconTheme,
    TextTheme? primaryTextTheme,
    TextTheme? textTheme,
    Typography? typography,
    ActionIconThemeData? actionIconTheme,
    AppBarTheme? appBarTheme,
    BadgeThemeData? badgeTheme,
    MaterialBannerThemeData? bannerTheme,
    BottomAppBarTheme? bottomAppBarTheme,
    BottomNavigationBarThemeData? bottomNavigationBarTheme,
    BottomSheetThemeData? bottomSheetTheme,
    ButtonBarThemeData? buttonBarTheme,
    ButtonThemeData? buttonTheme,
    CardTheme? cardTheme,
    CheckboxThemeData? checkboxTheme,
    ChipThemeData? chipTheme,
    DataTableThemeData? dataTableTheme,
    DatePickerThemeData? datePickerTheme,
    DialogTheme? dialogTheme,
    DividerThemeData? dividerTheme,
    DrawerThemeData? drawerTheme,
    DropdownMenuThemeData? dropdownMenuTheme,
    ElevatedButtonThemeData? elevatedButtonTheme,
    ExpansionTileThemeData? expansionTileTheme,
    FilledButtonThemeData? filledButtonTheme,
    FloatingActionButtonThemeData? floatingActionButtonTheme,
    IconButtonThemeData? iconButtonTheme,
    ListTileThemeData? listTileTheme,
    MenuBarThemeData? menuBarTheme,
    MenuButtonThemeData? menuButtonTheme,
    MenuThemeData? menuTheme,
    NavigationBarThemeData? navigationBarTheme,
    NavigationDrawerThemeData? navigationDrawerTheme,
    NavigationRailThemeData? navigationRailTheme,
    OutlinedButtonThemeData? outlinedButtonTheme,
    PopupMenuThemeData? popupMenuTheme,
    ProgressIndicatorThemeData? progressIndicatorTheme,
    RadioThemeData? radioTheme,
    SearchBarThemeData? searchBarTheme,
    SearchViewThemeData? searchViewTheme,
    SegmentedButtonThemeData? segmentedButtonTheme,
    SliderThemeData? sliderTheme,
    SnackBarThemeData? snackBarTheme,
    SwitchThemeData? switchTheme,
    TabBarTheme? tabBarTheme,
    TextButtonThemeData? textButtonTheme,
    TextSelectionThemeData? textSelectionTheme,
    TimePickerThemeData? timePickerTheme,
    ToggleButtonsThemeData? toggleButtonsTheme,
    TooltipThemeData? tooltipTheme,
    Color? toggleableActiveColor,
    Color? selectedRowColor,
    Color? errorColor,
    Color? backgroundColor,
    Color? bottomAppBarColor,
  })
```

### ThemeData(...)参数解析
| 参数名称                       | 使用类型                              | 参数介绍                                      |
|----------------------------|-----------------------------------|-------------------------------------------|
| applyElevationOverlayColor | bool                              | 控制是否应用高程覆盖颜色                              |
| cupertinoOverrideTheme     | NoDefaultCupertinoThemeData       | 用于覆盖Cupertino主题的数据                        |
| extensions                 | Iterable<ThemeExtension<dynamic>> | 扩展主题数据的可迭代对象                              |
| inputDecorationTheme       | InputDecorationTheme              | 输入框装饰的主题数据                                |
| materialTapTargetSize      | MaterialTapTargetSize             | 材料设计控件的点击目标尺寸                             |
| pageTransitionsTheme       | PageTransitionsTheme              | 页面切换动画的主题数据                               |
| platform                   | TargetPlatform                    | 定义当前运行的平台                                 |
| scrollbarTheme             | ScrollbarThemeData                | 滚动条的主题数据                                  |
| splashFactory              | InteractiveInkFeatureFactory      | 交互墨水特性工厂，用于定义水波纹效果                        |
| useMaterial3               | bool                              | 控制是否使用Material Design 3.0样式               |
| visualDensity              | VisualDensity                     | 控制布局的像素密度                                 |
| brightness                 | Brightness                        | 主题的亮度，可以是Brightness.light或Brightness.dark |
| canvasColor                | Color                             | 画布的颜色                                     |
| cardColor                  | Color                             | 卡片的颜色                                     |
| colorScheme                | ColorScheme                       | 颜色方案，包括主要和次要颜色                            |
| colorSchemeSeed            | Color                             | 用于生成颜色方案的种子                               |
| dialogBackgroundColor      | Color                             | 对话框的背景颜色                                  |
| disabledColor              | Color                             | 禁用状态下的颜色                                  |
| dividerColor               | Color                             | 分隔线的颜色                                    |
| focusColor                 | Color                             | 获取焦点时的颜色                                  |
| highlightColor             | Color                             | 高亮颜色                                      |
| hintColor                  | Color                             | 提示文本颜色                                    |
| hoverColor                 | Color                             | 悬停时的颜色                                    |
| indicatorColor             | Color                             | 指示器的颜色                                    |
| primaryColor               | Color                             | 主要颜色                                      |
| primaryColorDark           | Color                             | 主要颜色的较暗版本                                 |
| primaryColorLight          | Color                             | 主要颜色的较亮版本                                 |
| primarySwatch              | MaterialColor                     | 主要颜色的材料颜色                                 |
| scaffoldBackgroundColor    | Color                             | Scaffold（脚手架）的背景颜色                        |
| secondaryHeaderColor       | Color                             | 次要标题的颜色                                   |
| shadowColor                | Color                             | 阴影颜色                                      |
| splashColor                | Color                             | 水波纹颜色                                     |
| unselectedWidgetColor      | Color                             | 未选中控件的颜色                                  |
| fontFamily                 | String                            | 默认字体系列                                    |
| fontFamilyFallback         | List<String>                      | 字体系列的备用列表                                 |
| package                    | String                            | 字体包的名称                                    |
| iconTheme                  | IconThemeData                     | 图标的主题数据                                   |
| primaryIconTheme           | IconThemeData                     | 主要图标的主题数据                                 |
| primaryTextTheme           | TextTheme                         | 主要文本的主题数据                                 |
| textTheme                  | TextTheme                         | 文本的主题数据                                   |
| typography                 | Typography                        | 字体排印的主题数据                                 |
| actionIconTheme            | ActionIconThemeData               | 操作图标的主题数据                                 |
| appBarTheme                | AppBarTheme                       | AppBar的主题数据                               |
| badgeTheme                 | BadgeThemeData                    | 徽章的主题数据                                   |
| bannerTheme                | MaterialBannerThemeData           | 材料横幅的主题数据                                 |
| bottomAppBarTheme          | BottomAppBarTheme                 | 底部应用栏的主题数据                                |
| bottomNavigationBarTheme   | BottomNavigationBarThemeData      | 底部导航栏的主题数据                                |
| bottomSheetTheme           | BottomSheetThemeData              | 底部表单的主题数据                                 |
| buttonBarTheme             | ButtonBarThemeData                | 按钮栏的主题数据                                  |
| buttonTheme                | ButtonThemeData                   | 按钮的主题数据                                   |
| cardTheme                  | CardTheme                         | 卡片的主题数据                                   |
| checkboxTheme              | CheckboxThemeData                 | 复选框的主题数据                                  |
| chipTheme                  | ChipThemeData                     | 芯片的主题数据                                   |
| dataTableTheme             | DataTableThemeData                | 数据表的主题数据                                  |
| datePickerTheme            | DatePickerThemeData               | 日期选择器的主题数据                                |
| dialogTheme                | DialogTheme                       | 对话框的主题数据                                  |
| dividerTheme               | DividerThemeData                  | 分隔线的主题数据                                  |
| drawerTheme                | DrawerThemeData                   | 抽屉的主题数据                                   |
| dropdownMenuTheme          | DropdownMenuThemeData             | 下拉菜单的主题数据                                 |
| elevatedButtonTheme        | ElevatedButtonThemeData           | 高程按钮的主题数据                                 |
| expansionTileTheme         | ExpansionTileThemeData            | 展开瓦片的主题数据                                 |
| filledButtonTheme          | FilledButtonThemeData             | 填充按钮的主题数据                                 |
| floatingActionButtonTheme  | FloatingActionButtonThemeData     | 悬浮操作按钮的主题数据                               |
| iconButtonTheme            | IconButtonThemeData               | 图标按钮的主题数据                                 |
| listTileTheme              | ListTileThemeData                 | 列表瓦片的主题数据                                 |
| menuBarTheme               | MenuBarThemeData                  | 菜单栏的主题数据                                  |
| menuButtonTheme            | MenuButtonThemeData               | 菜单按钮的主题数据                                 |
| menuTheme                  | MenuThemeData                     | 菜单的主题数据                                   |
| navigationBarTheme         | NavigationBarThemeData            | 导航栏的主题数据                                  |
| navigationDrawerTheme      | NavigationDrawerThemeData         | 导航抽屉的主题数据                                 |
| navigationRailTheme        | NavigationRailThemeData           | 导航栏轨道的主题数据                                |
| outlinedButtonTheme        | OutlinedButtonThemeData           | 轮廓按钮的主题数据                                 |
| popupMenuTheme             | PopupMenuThemeData                | 弹出菜单的主题数据                                 |
| progressIndicatorTheme     | ProgressIndicatorThemeData        | 进度指示器的主题数据                                |
| radioTheme                 | RadioThemeData                    | 单选框的主题数据                                  |
| searchBarTheme             | SearchBarThemeData                | 搜索栏的主题数据                                  |
| searchViewTheme            | SearchViewThemeData               | 搜索视图的主题数据                                 |
| segmentedButtonTheme       | SegmentedButtonThemeData          | 分段按钮的主题数据                                 |
| sliderTheme                | SliderThemeData                   | 滑块的主题数据                                   |
| snackBarTheme              | SnackBarThemeData                 | Snackbar的主题数据                             |
| switchTheme                | SwitchThemeData                   | 开关的主题数据                                   |
| tabBarTheme                | TabBarTheme                       | 选项卡栏的主题数据                                 |
| textButtonTheme            | TextButtonThemeData               | 文本按钮的主题数据                                 |
| textSelectionTheme         | TextSelectionThemeData            | 文本选择的主题数据                                 |
| timePickerTheme            | TimePickerThemeData               | 时间选择器的主题数据                                |
| toggleButtonsTheme         | ToggleButtonsThemeData            | 切换按钮的主题数据                                 |
| tooltipTheme               | TooltipThemeData                  | 工具提示的主题数据                                 |
| toggleableActiveColor      | Color                             | 可切换控件激活状态的颜色                              |
| errorColor                 | Color                             | 错误状态的颜色                                   |
| backgroundColor            | Color                             | 背景颜色                                      |
| bottomAppBarColor          | Color                             | 底部应用栏的颜色                                  |

### 给定的ColorScheme对象生成一个合适的主题
```text
ThemeData.from({
    required ColorScheme colorScheme,
    TextTheme? textTheme,
    bool? useMaterial3,
}) 
```

### ThemeData.from(...)参数解析
| 参数名称          | 使用类型        | 参数介绍                              |
|---------------|-------------|-----------------------------------|
| colorScheme   | ColorScheme | ColorScheme 对象，包含主要和次要颜色方案，以及亮度信息 |
| textTheme     | TextTheme   | 可选的 TextTheme 对象，定义应用程序中文本样式的集合   |
| useMaterial3  | bool        | 是否使用 Material Design 3.0 样式       |


### 用于创建亮（暗）色主题
```text
ThemeData.light({bool? useMaterial3}) => ThemeData(
    brightness: Brightness.light, // Brightness.dark
    useMaterial3: useMaterial3,
  )
```

### ThemeData.from(...)参数解析
| 参数名称          | 使用类型        | 参数介绍                              |
|---------------|-------------|-----------------------------------|
| useMaterial3  | bool        | 是否使用 Material Design 3.0 样式       |

## CupertinoThemeData类
```text
CupertinoThemeData({
    Brightness? brightness,
    Color? primaryColor,
    Color? primaryContrastingColor,
    CupertinoTextThemeData? textTheme,
    Color? barBackgroundColor,
    Color? scaffoldBackgroundColor,
    bool? applyThemeToAll,
  })
```

### CupertinoThemeData(...)参数解析
| 参数名称                    | 使用类型                   | 参数介绍                                                        |
|-------------------------|------------------------|-------------------------------------------------------------|
| brightness              | Brightness             | 指定主题的亮度模式，可以是 Brightness.light（浅色模式）或 Brightness.dark（深色模式） |
| primaryColor            | Color                  | 定义应用程序的主要颜色                                                 |
| primaryContrastingColor | Color                  | 定义与 primaryColor 对比的颜色，用于一些需要强调的元素                          |
| textTheme               | CupertinoTextThemeData | 定义文字样式，包括标题、正文等                                             |
| barBackgroundColor      | Color                  | 定义导航栏、底部栏等条形元素的背景颜色                                         |
| scaffoldBackgroundColor | Color                  | 定义整个页面（Scaffold）的背景颜色                                       |
| applyThemeToAll         | bool                   | 指定是否将主题应用于整个应用程序                                            |

