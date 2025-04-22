
button_options_list = [
    ('NO_BUTTON',"○无按钮○","默认不显示按钮"),
    ('SEPARATOR', '◂◂◂间隔▸▸▸', '弹出菜单间隔符'),

    # 常用功能 G S R
    ('NO_BUTTON',"←常用功能G/S/R→",""),
    ('button_action_grab','移动','移动'),
    ('button_action_scale','缩放','缩放'),
    ('button_action_rotate','旋转','旋转'),

    # 切换坐标系
    ('NO_BUTTON',"←切换坐标系→",""),
    ('button_action_orientation_to_global','全局','全局坐标系'),
    ('button_action_orientation_to_local','局部','局部坐标系'),
    ('button_action_orientation_to_normal','法向','法向坐标系'),
    ('button_action_orientation_to_gimbal','万向','万向坐标系'),
    ('button_action_orientation_to_view','视图','视图坐标系'),
    ('button_action_orientation_to_cursor','游标','游标坐标系'),
    ('button_action_orientation_to_parent','父级','父级坐标系'),

    ('testone','菜单功能1','测试菜单功能1'),
    ('testtwo', '菜单功能2', '测试菜单功能2'),
    
]

# [0]调用的函数id；[1]按钮名称；[2]按钮图标；[3][4][…]typeandmode包含在其中才显示按钮，“all”则是在所有场景中都显示
button_press_function = {
    # 常用功能 G S R
    'button_action_grab':("button.action_grab","移动","EVENT_G","all"),
    'button_action_scale':("button.action_scale","缩放","EVENT_S","all"),
    'button_action_rotate':("button.action_rotate","旋转","EVENT_R","all"),

    # 切换坐标系
    'button_action_orientation_to_global':(
        "button.action_orientation_to_global","全局","ORIENTATION_GLOBAL",
        "CURVEOBJECT","CURVEEDIT","SURFACEOBJECT","SURFACEEDIT","METAOBJECT","METAEDIT","FONTOBJECT","FONTEDIT",
        "VOLUMEOBJECT","EMPTYOBJECT","LATTICEOBJECT","LATTICEEDIT","LIGHTOBJECT","LIGHT_PROBEOBJECT","CAMERAOBJECT",
        "SPEAKEROBJECT","MESHOBJECT","MESHEDIT","GPENCILOBJECT","GPENCILEDIT_GPENCIL","GREASEPENCILOBJECT",
        "GREASEPENCILEDIT","ARMATUREOBJECT","ARMATUREEDIT","ARMATUREPOSE",
    ),
    'button_action_orientation_to_local':(
        "button.action_orientation_to_local","局部","ORIENTATION_LOCAL",
        "CURVEOBJECT","CURVEEDIT","SURFACEOBJECT","SURFACEEDIT","METAOBJECT","METAEDIT","FONTOBJECT","FONTEDIT",
        "VOLUMEOBJECT","EMPTYOBJECT","LATTICEOBJECT","LATTICEEDIT","LIGHTOBJECT","LIGHT_PROBEOBJECT","CAMERAOBJECT",
        "SPEAKEROBJECT","MESHOBJECT","MESHEDIT","GPENCILOBJECT","GPENCILEDIT_GPENCIL","GREASEPENCILOBJECT",
        "GREASEPENCILEDIT","ARMATUREOBJECT","ARMATUREEDIT","ARMATUREPOSE",
    ),
    'button_action_orientation_to_normal':(
        "button.action_orientation_to_normal","法向","ORIENTATION_NORMAL",
        "CURVEOBJECT","CURVEEDIT","SURFACEOBJECT","SURFACEEDIT","METAOBJECT","METAEDIT","FONTOBJECT","FONTEDIT",
        "VOLUMEOBJECT","EMPTYOBJECT","LATTICEOBJECT","LATTICEEDIT","LIGHTOBJECT","LIGHT_PROBEOBJECT","CAMERAOBJECT",
        "SPEAKEROBJECT","MESHOBJECT","MESHEDIT","GPENCILOBJECT","GPENCILEDIT_GPENCIL","GREASEPENCILOBJECT",
        "GREASEPENCILEDIT","ARMATUREOBJECT","ARMATUREEDIT","ARMATUREPOSE",
    ),
    'button_action_orientation_to_gimbal':(
        "button.action_orientation_to_gimbal","万向","ORIENTATION_GIMBAL",
        "CURVEOBJECT","CURVEEDIT","SURFACEOBJECT","SURFACEEDIT","METAOBJECT","METAEDIT","FONTOBJECT","FONTEDIT",
        "VOLUMEOBJECT","EMPTYOBJECT","LATTICEOBJECT","LATTICEEDIT","LIGHTOBJECT","LIGHT_PROBEOBJECT","CAMERAOBJECT",
        "SPEAKEROBJECT","MESHOBJECT","MESHEDIT","GPENCILOBJECT","GPENCILEDIT_GPENCIL","GREASEPENCILOBJECT",
        "GREASEPENCILEDIT","ARMATUREOBJECT","ARMATUREEDIT","ARMATUREPOSE",
    ),
    'button_action_orientation_to_view':(
        "button.action_orientation_to_view","视图","ORIENTATION_VIEW",
        "CURVEOBJECT","CURVEEDIT","SURFACEOBJECT","SURFACEEDIT","METAOBJECT","METAEDIT","FONTOBJECT","FONTEDIT",
        "VOLUMEOBJECT","EMPTYOBJECT","LATTICEOBJECT","LATTICEEDIT","LIGHTOBJECT","LIGHT_PROBEOBJECT","CAMERAOBJECT",
        "SPEAKEROBJECT","MESHOBJECT","MESHEDIT","GPENCILOBJECT","GPENCILEDIT_GPENCIL","GREASEPENCILOBJECT",
        "GREASEPENCILEDIT","ARMATUREOBJECT","ARMATUREEDIT","ARMATUREPOSE",
    ),
    'button_action_orientation_to_cursor':(
        "button.action_orientation_to_cursor","游标","ORIENTATION_CURSOR",
        "CURVEOBJECT","CURVEEDIT","SURFACEOBJECT","SURFACEEDIT","METAOBJECT","METAEDIT","FONTOBJECT","FONTEDIT",
        "VOLUMEOBJECT","EMPTYOBJECT","LATTICEOBJECT","LATTICEEDIT","LIGHTOBJECT","LIGHT_PROBEOBJECT","CAMERAOBJECT",
        "SPEAKEROBJECT","MESHOBJECT","MESHEDIT","GPENCILOBJECT","GPENCILEDIT_GPENCIL","GREASEPENCILOBJECT",
        "GREASEPENCILEDIT","ARMATUREOBJECT","ARMATUREEDIT","ARMATUREPOSE",
    ),
    'button_action_orientation_to_parent':(
        "button.action_orientation_to_parent","父级","ORIENTATION_PARENT",
        "CURVEOBJECT","CURVEEDIT","SURFACEOBJECT","SURFACEEDIT","METAOBJECT","METAEDIT","FONTOBJECT","FONTEDIT",
        "VOLUMEOBJECT","EMPTYOBJECT","LATTICEOBJECT","LATTICEEDIT","LIGHTOBJECT","LIGHT_PROBEOBJECT","CAMERAOBJECT",
        "SPEAKEROBJECT","MESHOBJECT","MESHEDIT","GPENCILOBJECT","GPENCILEDIT_GPENCIL","GREASEPENCILOBJECT",
        "GREASEPENCILEDIT","ARMATUREOBJECT","ARMATUREEDIT","ARMATUREPOSE",
    ),









    # 测试功能
    'testone':("mode.tab_switch","智能切换","CUBE","GREASEPENCILOBJECT","MESHEDIT"),
    'testtwo':("wm.toolbar","系统快捷键","BOOKMARKS","OBJCET","GREASEPENCILOBJECT","MESHEDIT","MESHOBJECT"),
    'SEPARATOR':(),
    'NO_BUTTON':(),
}
