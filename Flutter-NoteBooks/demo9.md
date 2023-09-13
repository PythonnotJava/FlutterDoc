# 表格类
> Flutter3.0提供了以下的表格类
> * Table：Table可以让你以行和列的形式来组织数据，并以表格的形式进行展示。每一行可以包含多个单元格，每个单元格可以包含一个小部件，可以是文本、图像或其他自定义的小部件。
> * TableBorder：用于定义表格的边框样式。
> * TableRow：用于在Table中定义一行数据。
> * TableCell：用于在TableRow中定义一个单元格。
> * DataTable：用于创建数据表格的小部件，它以行和列的形式展示数据。DataTable提供了一个灵活的方式来显示结构化数据，并支持对表格的排序和选择。
> * DataRow：用于在DataTable中定义一行数据。
> * DataCell：用于在DataRow中定义一个单元格数据。
> * DataColumn：用于在DataTable中定义一列数据。
> * PaginatedDataTable：用于在数据表格中实现分页功能的小部件。它是 DataTable 的一个扩展，允许您在数据集较大时将表格分成多个页面，以便用户能够浏览和导航。

## Table类
### 默认构造函数
```text
Table({
    super.key,
    this.children = const <TableRow>[],
    this.columnWidths,
    this.defaultColumnWidth = const FlexColumnWidth(),
    this.textDirection,
    this.border,
    this.defaultVerticalAlignment = TableCellVerticalAlignment.top,
    this.textBaseline, 
  }) 
```

### Table(...)参数解析
| 参数名称                     | 使用类型                       | 参数介绍                     |
|--------------------------|----------------------------|--------------------------|
| key                      | Key                        | 小部件的唯一标识符，可以用于查找和操作小部件   |
| children                 | List<TableRow>             | 表格的内容，是一个包含多个TableRow的列表 |
| columnWidths             | Map<int, TableColumnWidth> | 用于指定每一列的宽度的映射表           |
| defaultColumnWidth       | TableColumnWidth           | 默认的列宽度                   |
| textDirection            | TextDirection              | 表格中文本的方向                 |
| border                   | TableBorder                | 表格的边框样式                  |
| defaultVerticalAlignment | TableCellVerticalAlignment | 默认的单元格垂直对齐方式             |
| textBaseline             | TextBaseline               | 用于对齐文本的基线                |

## TableBorder类
### 默认构造函数
```text
TableBorder({
    this.top = BorderSide.none,
    this.right = BorderSide.none,
    this.bottom = BorderSide.none,
    this.left = BorderSide.none,
    this.horizontalInside = BorderSide.none,
    this.verticalInside = BorderSide.none,
    this.borderRadius = BorderRadius.zero,
  })
```

### TableBorder(...)参数解析
| 参数名称                      | 使用类型                  | 参数介绍               |
|---------------------------|-----------------------|--------------------|
| top                       | BorderSide            | 表格的顶部边框样式          |
| right                     | BorderSide            | 表格的右侧边框样式          |
| bottom                    | BorderSide            | 表格的底部边框样式          |
| left                      | BorderSide            | 表格的左侧边框样式          |
| horizontalInside          | BorderSide            | 表格内部水平方向单元格之间的边框样式 |
| BorderSide verticalInside | BorderSide            | 表格内部垂直方向单元格之间的边框样式 |
| borderRadius              | BorderRadiusGeometry  | 表格的边框圆角样式          |

### 快速创建一个具有统一边框样式
```text
TableBorder.all({
    Color color = const Color(0xFF000000),
    double width = 1.0,
    BorderStyle style = BorderStyle.solid,
    BorderRadius borderRadius = BorderRadius.zero,
  })
```

### TableBorder.all(...)参数解析
| 参数名称           | 使用类型          | 参数介绍    |
|----------------|---------------|---------|
| color          | Color         | 边框的颜色   |
| width          | double        | 边框的宽度   |
| style          | BorderStyle   | 边框的样式   |
| borderRadius   | BorderRadius  | 边框的圆角样式 |


### 用于快速创建一个具有对称边框样式
```text
TableBorder.symmetric({
    BorderSide inside = BorderSide.none,
    BorderSide outside = BorderSide.none,
  })
```

### TableBorder.symmetric(...)参数解析
| 参数名称      | 使用类型        | 参数介绍           |
|-----------|-------------|----------------|
| inside    | BorderSide  | 表格内部单元格之间的边框样式 |
| outside   | BorderSide  | 表格外部边框样式       |

## TableRow类
### 默认构造函数
```text
TableRow({ 
    this.key, 
    this.decoration, 
    this.children = const <Widget>[]
    })
```

### TableRow(...)参数解析
| 参数名称       | 使用类型          | 参数介绍                        |
|------------|---------------|-----------------------------|
| key        | Key           | 小部件的唯一标识符，可以用于查找和操作小部件      |
| decoration | Decoration    | 用于为表格行添加装饰效果的样式             |
| children   | List<Widget>  | 行中的子小部件列表，通常为一组TableCell小部件 |

## TableCell类
### 默认构造函数
```text
TableCell({
    super.key,
    this.verticalAlignment,
    required super.child,
  })
```

### 参数解析
| 参数名称              | 使用类型                       | 参数介绍                                 |
|-------------------|----------------------------|--------------------------------------|
| key               | Key                        | 小部件的唯一标识符，可以用于查找和操作小部件               |
| verticalAlignment | TableCellVerticalAlignment | 用于控制单元格中内容的垂直对齐方式                    |
| child             | Widget                     | 必需的参数，单元格中显示的内容，可以是一个文本、图像或其他自定义的小部件 |

## DataTable类
### 默认构造函数
```text
DataTable({
    super.key,
    required this.columns,
    this.sortColumnIndex,
    this.sortAscending = true,
    this.onSelectAll,
    this.decoration,
    this.dataRowColor,
    double? dataRowHeight,
    double? dataRowMinHeight,
    double? dataRowMaxHeight,
    this.dataTextStyle,
    this.headingRowColor,
    this.headingRowHeight,
    this.headingTextStyle,
    this.horizontalMargin,
    this.columnSpacing,
    this.showCheckboxColumn = true,
    this.showBottomBorder = false,
    this.dividerThickness,
    required this.rows,
    this.checkboxHorizontalMargin,
    this.border,
    this.clipBehavior = Clip.none,
  })
```

### DataTable(...)参数解析
| 参数名称                     | 使用类型                         | 参数介绍                       |
|--------------------------|------------------------------|----------------------------|
| key                      | Key                          | Widget的唯一标识符               |
| columns                  | List<DataColumn>             | 必需参数，定义DataColumn组件列表      |
| sortColumnIndex          | int                          | 数据表当前排序的列索引                |
| sortAscending            | bool                         | 指示排序顺序是升序（true）还是降序（false） |
| onSelectAll              | Function                     | 当"全选"复选框被选中或取消选中时调用的回调函数   |
| decoration               | Decoration                   | 用于渲染数据表背景的装饰               |
| dataRowColor             | MaterialStateProperty<Color> | 数据行的背景色                    |
| dataRowHeight            | double                       | 数据行的高度                     |
| dataRowMinHeight         | double                       | 数据行的最小高度                   |
| dataRowMaxHeight         | double                       | 数据行的最大高度                   |
| dataTextStyle            | TextStyle                    | 数据单元格内文本的样式                |
| headingRowColor          | MaterialStateProperty<Color> | 标题行的背景色                    |
| headingRowHeight         | double                       | 标题行的高度                     |
| headingTextStyle         | TextStyle                    | 标题单元格内文本的样式                |
| horizontalMargin         | double                       | 数据表的水平边距                   |
| columnSpacing            | double                       | 列之间的间距                     |
| showCheckboxColumn       | bool                         | 指示是否在左侧显示复选框列              |
| showBottomBorder         | bool                         | 指示是否在数据表底部显示边框             |
| dividerThickness         | double                       | 行之间分隔线的粗细                  |
| rows                     | List<DataRow>                | 必需参数，定义DataRow组件列表         |
| checkboxHorizontalMargin | double                       | 复选框列的水平边距                  |
| border                   | TableBorder                  | 用于围绕数据表绘制边框                |
| clipBehavior             | Clip                         | 数据表内容溢出时的剪裁行为              |

## DataRow类
### 默认构造函数
```text
DataRow({
    this.key,
    this.selected = false,
    this.onSelectChanged,
    this.onLongPress,
    this.color,
    this.mouseCursor,
    required this.cells,
  })
```

### DataRow(...)参数解析
| 参数名称                                      | 使用类型                               | 参数介绍                                  |
|-------------------------------------------|------------------------------------|---------------------------------------|
| key                                       | Key                                | DataRow 的唯一标识符，用于区分相同类型的不同 DataRow 实例 |
| selected                                  | bool                               | 表示此行是否处于选中状态                          |
| onSelectChanged                           | Function                           | 当数据行的选中状态发生改变时的回调函数                   |
| onLongPre MaterialStateProperty<Color?>ss | Function                           | 当长按数据行时触发的回调函数                        |
| color                                     | MaterialStateProperty<Color>       | 数据行的背景颜色                              |
| mouseCursor                               | MaterialStateProperty<MouseCursor> | 当鼠标悬停在数据行上方时显示的鼠标指针样式                 |
| cells                                     | List<DataCell>                     | 必需参数，DataRow 中的数据单元格组件列表              |

### 对一行创建配置
```text
DataRow.byIndex({
    int? index,
    this.selected = false,
    this.onSelectChanged,
    this.onLongPress,
    this.color,
    this.mouseCursor,
    required this.cells,
  }) 
```

### DataRow.byIndex(...)参数解析
| 参数名称            | 使用类型                               | 参数介绍                                      |
|-----------------|------------------------------------|-------------------------------------------|
| index           | int                                | 数据行在数据表中的索引位置                             |
| selected        | bool                               | 表示此行是否处于选中状态                              |
| onSelectChanged | Function                           | 当数据行的选中状态发生改变时的回调函数                       |
| onLongPress     | Function                           | 当长按数据行时触发的回调函数                            |
| color           | MaterialStateProperty<Color>       | 数据行的背景颜色                                  |
| mouseCursor     | MaterialStateProperty<MouseCursor> | 当鼠标悬停在数据行上方时显示的鼠标指针样式                     |
| cells           | List<DataCell>                     | DataRow.byIndex 中的数据单元格 (DataCell) 组件列表   |

## DataCell类
### 默认构造函数
```text
DataCell(
    this.child, {
    this.placeholder = false,
    this.showEditIcon = false,
    this.onTap,
    this.onLongPress,
    this.onTapDown,
    this.onDoubleTap,
    this.onTapCancel,
  })
```

### DataCell(...)参数解析
| 参数名称          | 使用类型      | 参数介绍                               |
|---------------|-----------|------------------------------------|
| child         | Widget    | 必需参数，用于显示在单元格中的内容，通常是一个小部件（Widget） |
| placeholder   | bool      | 用于指示单元格是否处于占位符状态                   |
| showEditIcon  | bool      | 用于指示是否在单元格中显示编辑图标                  |
| onTap         | Function  | 回调函数，当用户轻触单元格时将被调用                 |
| onLongPress   | Function  | 回调函数，当用户长时间按住单元格时将被调用              |
| onTapDown     | Function  | 回调函数，当用户按下单元格时将被调用                 |
| onDoubleTap   | Function  | 回调函数，当用户双击单元格时将被调用                 |
| onTapCancel   | Function  | 回调函数，在用户按下但取消轻触单元格时将被调用            |

## DataColumn类
### 默认构造函数
```text
DataColumn({
    required this.label,
    this.tooltip,
    this.numeric = false,
    this.onSort,
    this.mouseCursor,
  })
```

### DataColumn(...)参数解析
| 参数名称         | 使用类型                               | 参数介绍                                        |
|--------------|------------------------------------|---------------------------------------------|
| label        | Widget                             | 必需参数，用于显示在列标题中的内容，通常是一个 Text 或 RichText 小部件 |
| tooltip      | String                             | 用于指定当用户将鼠标悬停在列标题上时显示的工具提示文本                 |
| numeric      | bool                               | 用于指示列是否包含数字类型的数据                            |
| onSort       | Function                           | 回调函数，当用户点击列标题时将被调用，用于处理排序逻辑                 |
| mouseCursor  | MaterialStateProperty<MouseCursor> | 用于指定当用户将鼠标悬停在列标题上时显示的鼠标指针样式                 |

## PaginatedDataTable类
### 默认构造函数
```text
PaginatedDataTable({
    super.key,
    this.header,
    this.actions,
    required this.columns,
    this.sortColumnIndex,
    this.sortAscending = true,
    this.onSelectAll,
    double? dataRowHeight,
    double? dataRowMinHeight,
    double? dataRowMaxHeight,
    this.headingRowHeight = 56.0,
    this.horizontalMargin = 24.0,
    this.columnSpacing = 56.0,
    this.showCheckboxColumn = true,
    this.showFirstLastButtons = false,
    this.initialFirstRowIndex = 0,
    this.onPageChanged,
    this.rowsPerPage = defaultRowsPerPage,
    this.availableRowsPerPage = const <int>[defaultRowsPerPage, defaultRowsPerPage * 2, defaultRowsPerPage * 5, defaultRowsPerPage * 10],
    this.onRowsPerPageChanged,
    this.dragStartBehavior = DragStartBehavior.start,
    this.arrowHeadColor,
    required this.source,
    this.checkboxHorizontalMargin,
    this.controller,
    this.primary,
  })
```

### PaginatedDataTable(...)参数解析
| 参数名称                     | 使用类型                | 参数介绍                           |
|--------------------------|---------------------|--------------------------------|
| key                      | Key                 | 用于标识 PaginatedDataTable        |
| header                   | Widget              | 显示在数据表格顶部的标题部分                 |
| actions                  | List<Widget>        | 小部件列表，显示在数据表格顶部右侧，可以放置自定义操作按钮等 |
| columns                  | List<DataColumn>    | DataColumn对象的列表，定义数据表格的列       |
| sortColumnIndex          | int                 | 表示当前按照哪一列进行排序                  |
| sortAscending            | bool                | 用于指示当前排序是否为升序                  |
| onSelectAll              | Function            | 回调函数，当用户点击全选复选框时将被调用           |
| dataRowHeight            | double              | 已弃用                            |
| dataRowMinHeight         | double              | 用于指定数据行的最小高度                   |
| dataRowMaxHeight         | double              | 用于指定数据行的最大高度                   |
| headingRowHeight         | double              | 用于指定表头行的高度                     |
| horizontalMargin         | double              | 用于指定表格左右边缘与屏幕边缘之间的空白区域宽度       |
| columnSpacing            | double              | 用于指定列之间的间距                     |
| showCheckboxColumn       | bool                | 用于指示是否显示表格的复选框列                |
| showFirstLastButtons     | bool                | 用于指示是否显示第一页和最后一页的导航按钮          |
| initialFirstRowIndex     | int                 | 用于指定初始时显示的第一行索引                |
| onPageChanged            | Function            | 回调函数，当用户更改页面时将被调用              |
| rowsPerPage              | int                 | 用于指定每页显示的行数                    |
| availableRowsPerPage     | List<int>           | 表示可供选择的每页行数选项                  |
| onRowsPerPageChanged     | Function            | 回调函数，当用户更改每页行数时将被调用            |
| dragStartBehavior        | DragStartBehavior   | 指定拖动行为的起始位置                    |
| arrowHeadColor           | Color               | 用于指定排序箭头的颜色                    |
| source                   | DataTableSource     | 必需参数，提供表格的数据和行的配置              |
| checkboxHorizontalMargin | double              | 用于指定复选框水平边距                    |
| controller               | DataTableController | 用于控制数据表格的状态和行为                 |
| primary                  | bool                | 用于指示是否为主滚动视图                   |
