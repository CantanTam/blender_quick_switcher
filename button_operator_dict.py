
button_options_list = [
    ('NO_BUTTON',"○无按钮○","默认不显示按钮"),
    ('SEPARATOR', '◂◂◂间隔▸▸▸', '测试按间隔功能'),

    # 常用功能 G S R
    ('NO_BUTTON',"←常用功能G/S/R→","默认不显示按钮"),
    ('button_action_grab','移动','移动'),
    ('button_action_scale','缩放','缩放'),


    ('testone','菜单功能1','测试菜单功能1'),
    ('testtwo', '菜单功能2', '测试菜单功能2'),
    
]

# [0]调用的函数id；[1]按钮名称；[2]按钮图标；[3][4][…]typeandmode包含在其中才显示按钮，“all”则是在所有场景中都显示
button_press_function = {
    # 常用功能 G S R
    'button_action_grab':("button.action_grab","移动","EVENT_G","all"),
    'button_action_scale':("button.action_scale","缩放","EVENT_S","all"),

    
    'testone':("mode.tab_switch","智能切换","CUBE","GREASEPENCILOBJECT","MESHEDIT"),
    'testtwo':("wm.toolbar","系统快捷键","BOOKMARKS","OBJCET","GREASEPENCILOBJECT","MESHEDIT","MESHOBJECT"),
    'SEPARATOR':(),
    'NO_BUTTON':(),
}