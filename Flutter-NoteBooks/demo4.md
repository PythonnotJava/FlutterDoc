# Input控件
> * TexField：用于接收用户的文本输入。它提供了一个文本输入框，用户可以在其中输入和编辑文本。
> * TextFormField：一个表单字段控件，用于接收用户输入的文本。
> * InputDecoration：用于装饰文本输入字段（TextInputField）的类。

## TexField
### 默认构造函数
```text
TextField({
    super.key,
    this.controller,
    this.focusNode,
    this.undoController,
    this.decoration = const InputDecoration(),
    TextInputType? keyboardType,
    this.textInputAction,
    this.textCapitalization = TextCapitalization.none,
    this.style,
    this.strutStyle,
    this.textAlign = TextAlign.start,
    this.textAlignVertical,
    this.textDirection,
    this.readOnly = false,
    @Deprecated(
      'Use `contextMenuBuilder` instead. '
      'This feature was deprecated after v3.3.0-0.5.pre.',
    )
    this.toolbarOptions,
    this.showCursor,
    this.autofocus = false,
    this.obscuringCharacter = '•',
    this.obscureText = false,
    this.autocorrect = true,
    SmartDashesType? smartDashesType,
    SmartQuotesType? smartQuotesType,
    this.enableSuggestions = true,
    this.maxLines = 1,
    this.minLines,
    this.expands = false,
    this.maxLength,
    this.maxLengthEnforcement,
    this.onChanged,
    this.onEditingComplete,
    this.onSubmitted,
    this.onAppPrivateCommand,
    this.inputFormatters,
    this.enabled,
    this.cursorWidth = 2.0,
    this.cursorHeight,
    this.cursorRadius,
    this.cursorOpacityAnimates,
    this.cursorColor,
    this.selectionHeightStyle = ui.BoxHeightStyle.tight,
    this.selectionWidthStyle = ui.BoxWidthStyle.tight,
    this.keyboardAppearance,
    this.scrollPadding = const EdgeInsets.all(20.0),
    this.dragStartBehavior = DragStartBehavior.start,
    bool? enableInteractiveSelection,
    this.selectionControls,
    this.onTap,
    this.onTapOutside,
    this.mouseCursor,
    this.buildCounter,
    this.scrollController,
    this.scrollPhysics,
    this.autofillHints = const <String>[],
    this.contentInsertionConfiguration,
    this.clipBehavior = Clip.hardEdge,
    this.restorationId,
    this.scribbleEnabled = true,
    this.enableIMEPersonalizedLearning = true,
    this.contextMenuBuilder = _defaultContextMenuBuilder,
    this.canRequestFocus = true,
    this.spellCheckConfiguration,
    this.magnifierConfiguration,
  })
```

### TextField(...)参数解析
| 参数名称                          | 使用类型                          | 参数介绍                 |
|-------------------------------|-------------------------------|----------------------|
| key                           | Key                           | Widget的标识符           |
| controller                    | TextEditingController         | 用于控制文本输入             |
| focusNode                     | FocusNode                     | 用于管理小部件的焦点           |
| undoController                | UndoController                | 用于管理撤销和恢复操作          |
| decoration                    | InputDecoration               | 用于装饰输入字段             |
| keyboardType                  | TextInputType                 | 指定键盘的类型              |
| textInputAction               | TextInputAction               | 与键盘关联的操作             |
| textCapitalization            | TextCapitalization            | 指定文本的大小写格式化规则        |
| style                         | TextStyle                     | 定义文本的样式              |
| strutStyle                    | StrutStyle                    | 定义基线对齐文本的样式          |
| textAlign                     | TextAlign                     | 指定文本的对齐方式            |
| textAlignVertical             | TextAlignVertical             | 指定文本的垂直对齐方式          |
| textDirection                 | TextDirection                 | 指定文本的方向              |
| readOnly                      | bool                          | 指示输入字段是否只读           |
| toolbarOptions                | ToolbarOptions                | 定义文本字段的工具栏选项         |
| showCursor                    | bool                          | 指示是否显示光标             |
| autofocus                     | bool                          | 指示是否自动获取焦点           |
| obscuringCharacter            | String                        | 用于替代隐藏字符的字符          |
| obscureText                   | bool                          | 指示输入字段是否应隐藏文本        |
| autocorrect                   | bool                          | 指示是否启用自动纠正           |
| smartDashesType               | SmartDashesType               | 指定连字符的智能替换行为         |
| smartQuotesType               | SmartQuotesType               | 指定引号的智能替换行为          |
| enableSuggestions             | bool                          | 指示是否启用建议             |
| maxLines                      | int                           | 指定输入字段的最大行数          |
| minLines                      | int                           | 指定输入字段的最小行数          |
| expands                       | bool                          | 指示输入字段是否应根据内容扩展      |
| maxLength                     | int                           | 指定输入字段的最大字符数         |
| maxLengthEnforcement          | MaxLengthEnforcement          | 指定最大长度的强制执行方式        |
| onChanged                     | Function                      | 回调函数，每当文本发生变化时调用     |
| onEditingComplete             | Function                      | 回调函数，当编辑操作完成时调用      |
| onSubmitted                   | Function                      | 回调函数，当用户提交文本时调用      |
| onAppPrivateCommand           | Function                      | 回调函数，处理应用程序私有命令      |
| inputFormatters               | List<TextInputFormatter>      | 用于格式化和约束用户输入         |
| enabled                       | bool                          | 指示输入字段是否可用           |
| cursorWidth                   | double                        | 指定光标的宽度              |
| cursorHeight                  | double                        | 指定光标的高度              |
| cursorRadius                  | Radius                        | 指定光标的边界半径            |
| cursorOpacityAnimates         | bool                          | 指示光标的不透明度是否动画化       |
| cursorColor                   | Color                         | 指定光标的颜色              |
| selectionHeightStyle          | BoxHeightStyle                | 指定选择文本的高度样式          |
| selectionWidthStyle           | BoxWidthStyle                 | 指定选择文本的宽度样式          |
| keyboardAppearance            | Brightness                    | 指定键盘的外观              |
| scrollPadding                 | EdgeInsets                    | 指定在滚动视图中显示输入字段时的内边距  |
| dragStartBehavior             | DragStartBehavior             | 指定开始拖动的行为            |
| enableInteractiveSelection    | bool                          | 指示是否启用交互式选择          |
| selectionControls             | TextSelectionControls         | 定义选择文本的控件            |
| onTap                         | Function                      | 回调函数，当用户点击输入字段时调用    |
| onTapOutside                  | Function                      | 回调函数，当用户在输入字段外部点击时调用 |
| mouseCursor                   | MouseCursor                   | 指定鼠标指针的样式            |
| buildCounter                  | Function                      | 回调函数，用于构建计数器小部件      |
| scrollController              | ScrollController              | 用于控制滚动视图             |
| scrollPhysics                 | ScrollPhysics                 | 用于指定滚动行为             |
| autofillHints                 | Iterable<String>              | 指定自动填充提示             |
| contentInsertionConfiguration | ContentInsertionConfiguration | 用于配置内容插入             |
| clipBehavior                  | Clip                          | 指定小部件如何裁剪            |
| restorationId                 | String                        | 用于恢复状态的唯一标识符         |
| scribbleEnabled               | bool                          | 指示是否启用涂鸦功能           |
| enableIMEPersonalizedLearning | bool                          | 指示是否启用个性化学习功能        |
| contextMenuBuilder            | Function                      | 回调函数，用于构建上下文菜单       |
| canRequestFocus               | bool                          | 指示是否允许请求焦点           |
| spellCheckConfiguration       | TextConfiguration             | 用于配置拼写检查             |
| magnifierConfiguration        | TextMagnifierConfiguration    | 用于配置放大镜              |

> 备注
> * @Deprecated(
    'Use `contextMenuBuilder` instead. '
    'This feature was deprecated after v3.3.0-0.5.pre.',
    )这段代码是对参数toolbarOptions的注释，具体请去查看Dart的语法

## TextFormField类
### 默认构造函数
```text
TextFormField({
    super.key,
    this.controller,
    String? initialValue,
    FocusNode? focusNode,
    InputDecoration? decoration = const InputDecoration(),
    TextInputType? keyboardType,
    TextCapitalization textCapitalization = TextCapitalization.none,
    TextInputAction? textInputAction,
    TextStyle? style,
    StrutStyle? strutStyle,
    TextDirection? textDirection,
    TextAlign textAlign = TextAlign.start,
    TextAlignVertical? textAlignVertical,
    bool autofocus = false,
    bool readOnly = false,
    @Deprecated(
      'Use `contextMenuBuilder` instead. '
      'This feature was deprecated after v3.3.0-0.5.pre.',
    )
    ToolbarOptions? toolbarOptions,
    bool? showCursor,
    String obscuringCharacter = '•',
    bool obscureText = false,
    bool autocorrect = true,
    SmartDashesType? smartDashesType,
    SmartQuotesType? smartQuotesType,
    bool enableSuggestions = true,
    MaxLengthEnforcement? maxLengthEnforcement,
    int? maxLines = 1,
    int? minLines,
    bool expands = false,
    int? maxLength,
    ValueChanged<String>? onChanged,
    GestureTapCallback? onTap,
    TapRegionCallback? onTapOutside,
    VoidCallback? onEditingComplete,
    ValueChanged<String>? onFieldSubmitted,
    super.onSaved,
    super.validator,
    List<TextInputFormatter>? inputFormatters,
    bool? enabled,
    double cursorWidth = 2.0,
    double? cursorHeight,
    Radius? cursorRadius,
    Color? cursorColor,
    Brightness? keyboardAppearance,
    EdgeInsets scrollPadding = const EdgeInsets.all(20.0),
    bool? enableInteractiveSelection,
    TextSelectionControls? selectionControls,
    InputCounterWidgetBuilder? buildCounter,
    ScrollPhysics? scrollPhysics,
    Iterable<String>? autofillHints,
    AutovalidateMode? autovalidateMode,
    ScrollController? scrollController,
    super.restorationId,
    bool enableIMEPersonalizedLearning = true,
    MouseCursor? mouseCursor,
    EditableTextContextMenuBuilder? contextMenuBuilder = _defaultContextMenuBuilder,
    SpellCheckConfiguration? spellCheckConfiguration,
    TextMagnifierConfiguration? magnifierConfiguration,
  })
```

### TextFormField(...)参数解析
| 参数名称                          | 使用类型                            | 参数介绍                         |
|-------------------------------|---------------------------------|------------------------------|
| key                           | Key                             | 控件的唯一标识符                     |
| controller                    | TextEditingController           | 控制输入框的文本编辑器，可以用于获取或设置输入框中的文本 |
| initialValue                  | String                          | 输入框的初始值，可以在构建时设置             |
| focusNode                     | FocusNode                       | 用于管理输入框的焦点状态                 |
| decoration                    | InputDecoration                 | 输入框的装饰，用于配置外观                |
| keyboardType                  | TextInputType                   | 键盘类型，指定输入框的键盘样式              |
| textCapitalization            | TextCapitalization              | 输入框的文本大写格式                   |
| textInputAction               | TextInputAction                 | 输入框完成输入后要执行的操作               |
| style                         | TextStyle                       | 输入框中文本的样式                    |
| strutStyle                    | StrutStyle                      | 输入框中文本行的样式                   |
| textDirection                 | TextDirection                   | 输入框中文本的方向                    |
| textAlign                     | TextAlign                       | 输入框中文本的水平对齐方式                |
| textAlignVertical             | TextAlignVertical               | 输入框中文本的垂直对齐方式                |
| autofocus                     | bool                            | 是否自动获取焦点                     |
| readOnly                      | bool                            | 输入框是否为只读状态                   |
| toolbarOptions                | ToolbarOptions                  | 工具栏选项，用于配置输入框相关的工具栏功能        |
| showCursor                    | bool                            | 是否显示光标                       |
| obscuringCharacter            | String                          | 用于遮蔽文本的字符                    |
| obscureText                   | bool                            | 是否隐藏输入文本，用于密码输入              |
| autocorrect                   | bool                            | 是否自动纠正输入的文本                  |
| smartDashesType               | SmartDashesType                 | 智能破折号类型，用于自动修正连字符            |
| smartQuotesType               | SmartQuotesType                 | 智能引号类型，用于自动修正引号              |
| enableSuggestions             | bool                            | 是否启用输入建议                     |
| maxLengthEnforcement          | MaxLengthEnforcement            | 输入文本的最大长度限制类型                |
| maxLines                      | int                             | 输入框的最大行数                     |
| minLines                      | int                             | 输入框的最小行数                     |
| expands                       | bool                            | 输入框是否在垂直方向上扩展以适应内容           |
| maxLength                     | int                             | 输入文本的最大字符数限制                 |
| *onChanged                    | Function                        | 当输入框的文本值发生变化时调用的回调函数         |
| onTap                         | Function                        | 当输入框被点击时调用的回调函数              |
| onTapOutside                  | Function                        | 当输入框外部被点击时调用的回调函数            |
| onEditingComplete             | Function                        | 当输入框完成编辑时调用的回调函数             |
| onFieldSubmitted              | Function                        | 当用户提交输入框的内容时调用的回调函数          |
| onSaved                       | Function                        | 当表单保存时调用的回调函数                |
| validator                     | String                          | 用于表单验证的回调函数                  |
| inputFormatters               | List<TextInputFormatter>        | 用于格式化输入文本的输入格式器列表            |
| enabled                       | bool                            | 是否启用输入框                      |
| cursorWidth                   | double                          | 光标的宽度                        |
| cursorHeight                  | double                          | 光标的高度                        |
| cursorRadius                  | Radius                          | 光标的圆角半径                      |
| cursorColor                   | Color                           | 光标的颜色                        |
| keyboardAppearance            | Brightness                      | 键盘外观样式，如浅色或深色                |
| scrollPadding                 | EdgeInsets                      | 滚动填充边距，用于在滚动视图中滚动到输入框时提供填充   |
| enableInteractiveSelection    | bool                            | 是否启用交互式选择                    |
| selectionControls             | TextSelectionControls           | 用于控制选择操作的控件                  |
| buildCounter                  | InputCounterWidgetBuilder       | 用于构建输入计数器的构建器函数              |
| scrollPhysics                 | ScrollPhysics                   | 滚动物理效果，用于控制滚动行为              |
| autofillHints                 | Iterable<String>                | 自动填充提示，用于提供自动填充建议            |
| autovalidateMode              | AutovalidateMode                | 自动验证模式，控制是否自动验证表单字段          |
| scrollController              | ScrollController                | 滚动控制器，用于控制输入框滚动行为            |
| restorationId                 | String                          | 用于恢复控件状态                     |
| enableIMEPersonalizedLearning | bool                            | 是否启用个性化学习                    |
| mouseCursor                   | MouseCursor                     | 鼠标指针样式                       |
| contextMenuBuilder            | *EditableTextContextMenuBuilder | 上下文菜单构建器，用于自定义上下文菜单          |
| spellCheckConfiguration       | SpellCheckConfiguration         | 拼写检查配置                       |
| magnifierConfiguration        | TextMagnifierConfiguration      | 文本放大镜配置                      |

> 备注
> * 或许你已经发现了，凡是“on”开头的回调函数，返回值全部都是void
> * contextMenuBuilder默认是一个Widget类，使用“Widget _defaultContextMenuBuilde”这个默认值，而EditableTextContextMenuBuilde实质是一个返回值为Widget的回调函数

## InputDecoration类
### 默认构造函数
```text
InputDecoration({
    this.icon,
    this.iconColor,
    this.label,
    this.labelText,
    this.labelStyle,
    this.floatingLabelStyle,
    this.helperText,
    this.helperStyle,
    this.helperMaxLines,
    this.hintText,
    this.hintStyle,
    this.hintTextDirection,
    this.hintMaxLines,
    this.errorText,
    this.errorStyle,
    this.errorMaxLines,
    this.floatingLabelBehavior,
    this.floatingLabelAlignment,
    this.isCollapsed = false,
    this.isDense,
    this.contentPadding,
    this.prefixIcon,
    this.prefixIconConstraints,
    this.prefix,
    this.prefixText,
    this.prefixStyle,
    this.prefixIconColor,
    this.suffixIcon,
    this.suffix,
    this.suffixText,
    this.suffixStyle,
    this.suffixIconColor,
    this.suffixIconConstraints,
    this.counter,
    this.counterText,
    this.counterStyle,
    this.filled,
    this.fillColor,
    this.focusColor,
    this.hoverColor,
    this.errorBorder,
    this.focusedBorder,
    this.focusedErrorBorder,
    this.disabledBorder,
    this.enabledBorder,
    this.border,
    this.enabled = true,
    this.semanticCounterText,
    this.alignLabelWithHint,
    this.constraints,
  })
```

### InputDecoration(...)参数解析
| 参数名称                   | 使用类型                   | 参数介绍                   |
|------------------------|------------------------|------------------------|
| icon                   | Widget                 | 在输入字段前面显示的图标           |
| iconColor              | Color                  | 图标的颜色                  |
| label                  | Widget                 | 输入字段的标签，可以是Text或Widget |
| labelText              | String                 | 输入字段的标签文本              |
| labelStyle             | TextStyle              | 标签文本的样式                |
| floatingLabelStyle     | TextStyle              | 悬浮标签文本的样式              |
| helperText             | String                 | 帮助文本，通常用于提供关于输入字段的额外说明 |
| helperStyle            | TextStyle              | 帮助文本的样式                |
| helperMaxLines         | int                    | 帮助文本的最大行数              |
| hintText               | String                 | 提示文本，通常用于提示用户应该输入什么    |
| hintStyle              | TextStyle              | 提示文本的样式                |
| hintTextDirection      | TextDirection          | 提示文本的方向                |
| hintMaxLines           | int                    | 提示文本的最大行数              |
| errorText              | String                 | 错误文本，用于显示输入字段的错误消息     |
| errorStyle             | TextStyle              | 错误文本的样式                |
| errorMaxLines          | int                    | 错误文本的最大行数              |
| floatingLabelBehavior  | FloatingLabelBehavior  | 悬浮标签的行为方式，如始终显示、自动显示等  |
| floatingLabelAlignment | FloatingLabelAlignment | 悬浮标签的对齐方式              |
| isCollapsed            | bool                   | 输入字段是否与其他字段合并为单个视觉单元   |
| isDense                | bool                   | 输入字段是否应该是紧凑型的          |
| contentPadding         | EdgeInsetsGeometry     | 输入字段内容的内边距             |
| prefixIcon             | Widget                 | 输入字段前面显示的图标            |
| prefixIconConstraints  | BoxConstraints         | 前缀图标的约束条件              |
| prefix                 | Widget                 | 输入字段前面显示的文本或控件         |
| prefixText             | String                 | 输入字段前面显示的文本            |
| prefixStyle            | TextStyle              | 前缀文本的样式                |
| prefixIconColor        | Color                  | 前缀图标的颜色                |
| suffixIcon             | Widget                 | 输入字段后面显示的图标            |
| suffix                 | Widget                 | 输入字段后面显示的文本或控件         |
| suffixText             | String                 | 输入字段后面显示的文本            |
| suffixStyle            | TextStyle              | 后缀文本的样式                |
| suffixIconColor        | Color                  | 后缀图标的颜色                |
| suffixIconConstraints  | BoxConstraints         | 后缀图标的约束条件              |
| counter                | Widget                 | 输入字段的计数器，用于显示已输入的字符数量  |
| counterText            | String                 | 计数器显示的文本               |
| counterStyle           | TextStyle              | 计数器文本的样式               |
| filled                 | bool                   | 是否给输入字段添加背景填充色         |
| fillColor              | Color                  | 输入字段的背景填充色             |
| focusColor             | Color                  | 输入字段在获得焦点时的颜色          |
| hoverColor             | Color                  | 鼠标悬停在输入字段上时的颜色         |
| errorBorder            | InputBorder            | 错误状态下的边框样式             |
| focusedBorder          | InputBorder            | 获得焦点时的边框样式             |
| focusedErrorBorder     | InputBorder            | 获得焦点但存在错误时的边框样式        |
| disabledBorder         | InputBorder            | 禁用状态下的边框样式             |
| enabledBorder          | InputBorder            | 可用状态下的边框样式             |
| border                 | InputBorder            | 默认边框样式                 |
| enabled                | bool                   | 输入字段是否可用               |
| semanticCounterText    | String                 | 用于辅助功能的计数器文本           |
| alignLabelWithHint     | bool                   | 是否将标签对齐到提示文本的位置        |
| constraints            | BoxConstraints         | 输入字段的约束条件              |

### 用于创建一个折叠的装饰样式，通常用于输入字段没有边框时。
```text
InputDecoration.collapsed({
    required this.hintText,
    this.floatingLabelBehavior,
    this.floatingLabelAlignment,
    this.hintStyle,
    this.hintTextDirection,
    this.filled = false,
    this.fillColor,
    this.focusColor,
    this.hoverColor,
    this.border = InputBorder.none,
    this.enabled = true,
  })
```

### InputDecoration.collapsed(...)参数解析
| 参数名称                   | 使用类型                   | 参数介绍                           |
|------------------------|------------------------|--------------------------------|
| hintText               | String                 | 提示文本，用于提示用户应该输入什么              |
| floatingLabelBehavior  | FloatingLabelBehavior  | 悬浮标签的行为方式，如始终显示、自动显示等          |
| floatingLabelAlignment | FloatingLabelAlignment | 悬浮标签的对齐方式                      |
| hintStyle              | TextStyle              | 提示文本的样式                        |
| hintTextDirection      | TextDirection          | 提示文本的方向                        |
| filled                 | bool                   | 是否给输入字段添加背景填充色                 |
| fillColor              | Color                  | 输入字段的背景填充色                     |
| focusColor             | Color                  | 输入字段在获得焦点时的颜色                  |
| hoverColor             | Color                  | 鼠标悬停在输入字段上时的颜色                 |
| border                 | InputBorder            | 边框样式，默认为InputBorder.none，即没有边框 |
| enabled                | bool                   | 输入字段是否可用                       |




