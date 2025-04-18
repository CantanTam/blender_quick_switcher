
button_options_list = [
    ('NO_BUTTON',"[ 无按钮 ]","默认不显示按钮"),
    ('SEPARATOR',"[ 分隔符 ]","分隔上下按钮，但第一行按钮不能为分隔符"),
    ('testone','菜单功能1','测试菜单功能1'),
    ('testtwo', '菜单功能2', '测试菜单功能2'),
    ('EMPTY_BUTTON', '[ 无功能 ]', '测试按钮留空功能'),
]

# [0]调用的函数id；[1]按钮名称；[2]按钮图标；[3][4][…]typeandmode包含在其中才显示按钮
button_press_function = {
    # SEPARATOR 键对应的元组，必须包含所有的 typeandmode 值
    'SEPARATOR':("GREASEPENCILOBJECT","MESHEDIT","MESHOBJECT"),
    'testone':("mode.tab_switch","智能切换","CUBE","GREASEPENCILOBJECT","MESHEDIT"),
    'testtwo':("switch.vertex_edge_face","切换点线面","BOOKMARKS","OBJCET","GREASEPENCILOBJECT","MESHEDIT"),
    'EMPTY_BUTTON':("button.function_no_action","","")
}