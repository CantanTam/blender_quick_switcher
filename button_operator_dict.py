
button_options_list = [
    ('NO_BUTTON',"[ 无按钮 ]","默认不显示按钮"),
    ('SEPARATOR', '[ 间隔 ]', '测试按间隔功能'),
    ('testone','菜单功能1','测试菜单功能1'),
    ('testtwo', '菜单功能2', '测试菜单功能2'),
    ('button_action_grab','移动','移动'),
]

# [0]调用的函数id；[1]按钮名称；[2]按钮图标；[3][4][…]typeandmode包含在其中才显示按钮
button_press_function = {
    'button_action_grab':("button.action_grab","移动","EVENT_G","MESHOBJECT","MESHEDIT"),
    'testone':("mode.tab_switch","智能切换","CUBE","GREASEPENCILOBJECT","MESHEDIT"),
    'testtwo':("wm.toolbar","系统快捷键","BOOKMARKS","OBJCET","GREASEPENCILOBJECT","MESHEDIT","MESHOBJECT"),
    'SEPARATOR':(),
    'NO_BUTTON':(),
}