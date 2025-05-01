
button_options_list = [
    ('NO_BUTTON',"○无按钮○","默认不显示按钮"),
    ('SEPARATOR', '◂◂◂间隔▸▸▸', '弹出菜单间隔符'),

    # 全局高频操作：
    ('NO_BUTTON',"←全局常用操作→","全局都使用的高频操作"),
    ('button.action_global_grab','移动','移动'),
    ('button.action_global_scale','缩放','缩放'),
    ('button.action_global_rotate','旋转','旋转'),
    ('button.action_global_select_all','全选','快捷键(A)'),
    ('button.action_global_select_invert','反选','快捷键(Ctrl I)'),
    ('button.action_global_select_circle','刷选','快捷键(C)'),
    ('button.action_global_add',"添加(菜单)","不同的模式当中，调出不同的添加菜单"),
    ('button.action_global_duplicate_move',"复制","快捷键(Shift D)"),
    ('button.action_global_copy',"复制","物体模式/蜡笔编辑模式共用的“复制(Ctrl C)”操作"),
    ('button.action_global_paste',"粘贴","物体模式/蜡笔编辑模式共用的“粘贴(Ctrl V)”操作"),
    ('button.action_call_global_delete_menu',"删除","多种编辑模式共用的“删除(X)”操作"),



    # 切换坐标系
    ('NO_BUTTON',"←切换坐标系→",""),
    ('button_action_orientation_to_global','全局','全局坐标系'),
    ('button_action_orientation_to_local','局部','局部坐标系'),
    ('button_action_orientation_to_normal','法向','法向坐标系'),
    ('button_action_orientation_to_gimbal','万向','万向坐标系'),
    ('button_action_orientation_to_view','视图','视图坐标系'),
    ('button_action_orientation_to_cursor','游标','游标坐标系'),
    ('button_action_orientation_to_parent','父级','父级坐标系'),

    # 切换轴心点
    ('NO_BUTTON',"←切换轴心点→",""),
    ('button_action_pivot_to_bounding_box_center','边界框中心','边界框中心'),
    ('button_action_pivot_to_cursor','3D 游标','3D 游标'),
    ('button_action_pivot_to_individual_origins','各自的原点','各自的原点'),
    ('button_action_pivot_to_median_point','质心点','质心点'),
    ('button_action_pivot_to_active_element','活动元素','活动元素'),

    # 通用模式——共用功能
    ('NO_BUTTON',"←通用模式-“变换”菜单→","不同模式下“变换”菜单中都会出现的选项，被合并到这里"),
    ('button.action_call_common_function_transform_menu',"变换(菜单)","多种编辑模式调出“变换”菜单"),
    ('button.action_transform_tosphere',"变换—球形化","多种模式共用的“球形化”操作"),
    ('button.action_transform_shear',"变换—切变","多种模式共用的“切变”操作"),
    ('button.action_transform_bend',"变换—弯曲","多种模式共用的“弯曲”操作"),
    ('button.action_transform_push_pull',"变换—推/拉","多种模式共用的“推/拉”操作"),
    ('button.action_transform_translate_texturespace_true',"变换—移动纹理空间","多种模式共用的“移动纹理空间”操作"),
    ('button.action_transform_resize_texturespace_true',"变换—缩放纹理空间","多种模式共用的“缩放纹理空间”操作"),
    ('transform.vertex_warp',"变换—弯绕","多种模式共用的“弯绕”操作"),
    ('button.action_transform_vertex_random',"变换—随机","多种模式共用的“随机”操作"),


    # 通用模式——“视图”菜单，在所有模式都可以调出的菜单
    ('NO_BUTTON',"←通用模式-视图菜单→",""),
    ('button.action_view_selected_use_all_regions_false','框显所选','快捷键(.)'),
    ('button.action_view_all_center_false','框显全部','快捷键(Home)'),
    ('button.action_view_persportho','透视/正交','快捷键(Num_5)'),
    ('button.action_view3d_localview','局部视图','快捷键(/)'),
    ('button.action_view3d_localview_remove_from','从局部视图中移除','快捷键(Alt+/)'),
    ('button.action_view3d_object_as_camera','设置活动物体为摄像机','快捷键(Ctrl+Num_0)'),
    ('button.action_view3d_view_camera','活动摄像机','快捷键(Num_0)'),
    ('button.action_view3d_view_center_camera','摄像机边界框','快捷键(Home)'),
    ('button.action_view3d_call_menu_view_axis','视图(菜单)',''),
    ('button.action_view3d_call_menu_view_switch_axis','视图切换(菜单)',''),
    ('button.action_view3d_zoom_border','视图切换—框选放大','快捷键(Shift+B)'),
    ('button.action_view3d_fly','视图切换—飞行漫步',''),
    ('button.action_view3d_walk','视图切换—行走漫步','快捷键(Shift+`)'),
    ('button.action_view3d_call_menu_view_align','对齐视图(菜单)',''),
    ('view3d.camera_to_view','对齐视图—活动摄像机对齐当前视角','快捷键(Ctrl+Alt+Num_0)'),
    ('view3d.camera_to_view_selected','对齐视图—活动摄像机对齐选中的物体',''),
    ('button.action_view3d_lock_to_active_or_lock_clear','对齐视图—锁定/解锁视图',''),
    ('button.action_view3d_call_menu_view_regions','视图框(菜单)',''),
    ('button.action_view3d_clip_border','视图框—裁剪框','快捷键(Alt+B)'),
    ('button.action_view3d_render_border','视图框—渲染框','快捷键(Ctrl+B)'),
    ('view3d.clear_render_border','视图框—清除渲染框','快捷键(Ctrl+B)'),

    # 通用模式——“选择”菜单，不同模式实现不同的“选择”功能
    ('NO_BUTTON',"←通用模式-选择菜单→",""),
    ('button.action_select_select_mirror','选择镜像','快捷键(Ctrl Shift M)'),
    ('button.action_select_select_random','随机选择',''),
    ('button.action_call_object_select_more_or_less_menu','加选/减选(菜单)',''),
    ('button.action_object_select_more','加选','快捷键(Ctrl Num_+)'),
    ('button.action_object_select_less','减选','快捷键(Ctrl Num_-)'),
    ('button.action_object_select_hierarchy_parent_child','父级/子级','父级/子级/扩展父级/扩展子级功能集合'),
    ('button.action_call_select_select_grouped_menu','按组/相似选择(菜单)','快捷键(Shift G)'),
    ('button.action_call_select_select_linked_menu','选择相连元素(菜单)',''),
    ('object.select_pattern','按名称选择',''),

    # 物体模式——“选择”菜单
    ('NO_BUTTON',"←物体模式-选择菜单→","“物体—选择”菜单中显示的选项"),
    ('button.action_view3d_call_select_select_by_type_menu','按类型全选(菜单)',''),
    ('object.select_camera','选择活动摄像机','此按钮只在“物体”模式下出现'),

    # 物体模式——“物体”菜单
    ('NO_BUTTON',"←物体模式-物体菜单→","“物体—物体”菜单中显示的选项"),
    ('button.action_global_duplicate_move_linked',"关联复制","快捷键(Alt D)"),
    ('object.join',"合并","快捷键(Ctrl J)"),

    ('button.action_object_object_transform_transform_mode_align',"变换—对齐到变换坐标系",""),
    ('object.randomize_transform',"变换—随机变换",""),
    ('object.align',"变换—对齐物体",""),

    # “骨架”——相关按钮
    ('NO_BUTTON',"←骨架-编辑模式→","“骨架—编辑模式”菜单中显示的选项"),




    ('testone','菜单功能1','测试菜单功能1'),
    ('testtwo', '菜单功能2', '测试菜单功能2'),
    
]

# [0]调用的函数id；[1]按钮名称；[2]按钮图标；[3][4][…]typeandmode包含在其中才显示按钮，“all”则是在所有场景中都显示
button_press_function = {
    # 全局高频操作-移动/缩放/旋转-G/S/R
        'button.action_global_grab':(
        "button.action_global_grab","移动","EVENT_G",
        "CURVEOBJECT","CURVEEDIT","SURFACEOBJECT","SURFACEEDIT","METAOBJECT","METAEDIT","FONTOBJECT",
        "VOLUMEOBJECT","EMPTYOBJECT","LATTICEOBJECT","LATTICEEDIT","LIGHTOBJECT","LIGHT_PROBEOBJECT","CAMERAOBJECT",
        "SPEAKEROBJECT","MESHOBJECT","MESHEDIT","GPENCILOBJECT","GPENCILEDIT_GPENCIL","GREASEPENCILOBJECT",
        "GREASEPENCILEDIT","ARMATUREOBJECT","ARMATUREEDIT","ARMATUREPOSE",'MESHSCULPT',
    ),
        'button.action_global_scale':(
        "button.action_global_scale","缩放","EVENT_S",
        "CURVEOBJECT","CURVEEDIT","SURFACEOBJECT","SURFACEEDIT","METAOBJECT","METAEDIT","FONTOBJECT",
        "VOLUMEOBJECT","EMPTYOBJECT","LATTICEOBJECT","LATTICEEDIT","LIGHTOBJECT","LIGHT_PROBEOBJECT","CAMERAOBJECT",
        "SPEAKEROBJECT","MESHOBJECT","MESHEDIT","GPENCILOBJECT","GPENCILEDIT_GPENCIL","GREASEPENCILOBJECT",
        "GREASEPENCILEDIT","ARMATUREOBJECT","ARMATUREEDIT","ARMATUREPOSE",'MESHSCULPT',
    ),
        'button.action_global_rotate':(
        "button.action_global_rotate","旋转","EVENT_R",
        "CURVEOBJECT","CURVEEDIT","SURFACEOBJECT","SURFACEEDIT","METAOBJECT","METAEDIT","FONTOBJECT",
        "VOLUMEOBJECT","EMPTYOBJECT","LATTICEOBJECT","LATTICEEDIT","LIGHTOBJECT","LIGHT_PROBEOBJECT","CAMERAOBJECT",
        "SPEAKEROBJECT","MESHOBJECT","MESHEDIT","GPENCILOBJECT","GPENCILEDIT_GPENCIL","GREASEPENCILOBJECT",
        "GREASEPENCILEDIT","ARMATUREOBJECT","ARMATUREEDIT","ARMATUREPOSE",'MESHSCULPT',
    ),

    # 全局高频操作—全选/反选/刷选
        'button.action_global_select_all':(
        "button.action_global_select_all","全选","EVENT_A",
        "CURVEOBJECT", "CURVEEDIT", "SURFACEOBJECT", "SURFACEEDIT",  "METAOBJECT", "METAEDIT",
        "FONTOBJECT", "FONTEDIT", "VOLUMEOBJECT", "EMPTYOBJECT", "LATTICEOBJECT", "LATTICEEDIT",
        "LIGHTOBJECT", "LIGHT_PROBEOBJECT", "CAMERAOBJECT", "SPEAKEROBJECT", "MESHOBJECT",
        "MESHEDIT", "GPENCILOBJECT", "GPENCILEDIT_GPENCIL", "GPENCILVERTEX_GPENCIL", 
        "GREASEPENCILOBJECT", "GREASEPENCILEDIT", "GREASEPENCILVERTEX_GREASE_PENCIL", 
        "ARMATUREOBJECT", "ARMATUREEDIT", "ARMATUREPOSE",
    ),
        'button.action_global_select_invert':(
        "button.action_global_select_invert","反选","RADIOBUT_OFF",
        "CURVEOBJECT", "CURVEEDIT", "SURFACEOBJECT", "SURFACEEDIT",  "METAOBJECT", "METAEDIT",
        "FONTOBJECT", "FONTEDIT", "VOLUMEOBJECT", "EMPTYOBJECT", "LATTICEOBJECT", "LATTICEEDIT",
        "LIGHTOBJECT", "LIGHT_PROBEOBJECT", "CAMERAOBJECT", "SPEAKEROBJECT", "MESHOBJECT",
        "MESHEDIT", "GPENCILOBJECT", "GPENCILEDIT_GPENCIL", "GPENCILVERTEX_GPENCIL", 
        "GREASEPENCILOBJECT", "GREASEPENCILEDIT", "GREASEPENCILVERTEX_GREASE_PENCIL", 
        "ARMATUREOBJECT", "ARMATUREEDIT", "ARMATUREPOSE",
    ),
        'button.action_global_select_circle':(
        "button.action_global_select_circle","刷选","EVENT_C",
        "CURVEOBJECT", "CURVEEDIT", "SURFACEOBJECT", "SURFACEEDIT",  "METAOBJECT", "METAEDIT",
        "FONTOBJECT", "FONTEDIT", "VOLUMEOBJECT", "EMPTYOBJECT", "LATTICEOBJECT", "LATTICEEDIT",
        "LIGHTOBJECT", "LIGHT_PROBEOBJECT", "CAMERAOBJECT", "SPEAKEROBJECT", "MESHOBJECT",
        "MESHEDIT", "GPENCILOBJECT", "GPENCILEDIT_GPENCIL", "GREASEPENCILOBJECT", "GREASEPENCILEDIT", 
        "ARMATUREOBJECT", "ARMATUREEDIT", "ARMATUREPOSE",
    ),

    # 全局高频操作——“添加”菜单/“复制(Shift+D)”/“复制(Ctrl C)”/“粘贴(Ctrl V)”
        'button.action_global_add':(
        "button.action_global_add","添加","COLLAPSEMENU", "CURVEOBJECT", "SURFACEOBJECT", "METAOBJECT",
        "FONTOBJECT", "VOLUMEOBJECT", "EMPTYOBJECT", "LATTICEOBJECT", "LIGHTOBJECT", "LIGHT_PROBEOBJECT", 
        "CAMERAOBJECT", "SPEAKEROBJECT", "MESHOBJECT","GPENCILOBJECT", "GREASEPENCILOBJECT","ARMATUREOBJECT",
        "CURVEEDIT",'SURFACEEDIT','METAEDIT','MESHEDIT','ARMATUREEDIT',
    ),
        'button.action_global_duplicate_move':(
        "button.action_global_duplicate_move","复制","DUPLICATE", "CURVEOBJECT", "SURFACEOBJECT", "METAOBJECT",
        "FONTOBJECT", "VOLUMEOBJECT", "EMPTYOBJECT", "LATTICEOBJECT", "LIGHTOBJECT", "LIGHT_PROBEOBJECT", 
        "CAMERAOBJECT", "SPEAKEROBJECT", "MESHOBJECT","GPENCILOBJECT", "GPENCILEDIT_GPENCIL", "GREASEPENCILOBJECT",
        "GREASEPENCILEDIT","ARMATUREOBJECT", "CURVEEDIT",'SURFACEEDIT','METAEDIT','MESHEDIT','ARMATUREEDIT',
    ),
        'button.action_global_copy':(
        "button.action_global_copy","复制","COPYDOWN", "CURVEOBJECT", "SURFACEOBJECT", "METAOBJECT",
        "FONTOBJECT", "VOLUMEOBJECT", "EMPTYOBJECT", "LATTICEOBJECT", "LIGHTOBJECT", "LIGHT_PROBEOBJECT", 
        "CAMERAOBJECT", "SPEAKEROBJECT", "MESHOBJECT","GPENCILOBJECT", "GPENCILEDIT_GPENCIL", "GREASEPENCILOBJECT",
        "GREASEPENCILEDIT","ARMATUREOBJECT", 
    ),
        'button.action_global_paste':(
        "button.action_global_paste","粘贴","PASTEDOWN", "CURVEOBJECT", "SURFACEOBJECT", "METAOBJECT",
        "FONTOBJECT", "VOLUMEOBJECT", "EMPTYOBJECT", "LATTICEOBJECT", "LIGHTOBJECT", "LIGHT_PROBEOBJECT", 
        "CAMERAOBJECT", "SPEAKEROBJECT", "MESHOBJECT","GPENCILOBJECT", "GPENCILEDIT_GPENCIL", "GREASEPENCILOBJECT",
        "GREASEPENCILEDIT","ARMATUREOBJECT", 
    ),
        'button.action_call_global_delete_menu':(
        "button.action_call_global_delete_menu","删除","EVENT_X", "CURVEOBJECT", "SURFACEOBJECT", "METAOBJECT",
        "FONTOBJECT", "VOLUMEOBJECT", "EMPTYOBJECT", "LATTICEOBJECT", "LIGHTOBJECT", "LIGHT_PROBEOBJECT", 
        "CAMERAOBJECT", "SPEAKEROBJECT", "MESHOBJECT","GPENCILOBJECT", "GPENCILEDIT_GPENCIL", "GREASEPENCILOBJECT",
        "GREASEPENCILEDIT","ARMATUREOBJECT", "MESHEDIT","METAEDIT","GPENCILPAINT_GPENCIL","ARMATUREEDIT",
        "CURVEEDIT","SURFACEEDIT",
    ),

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

    # 切换轴心点
        'button_action_pivot_to_bounding_box_center':(
        "button.action_pivot_to_bounding_box_center","边界框中心","PIVOT_BOUNDBOX",
        "CURVEOBJECT","CURVEEDIT","SURFACEOBJECT","SURFACEEDIT","METAOBJECT","METAEDIT","FONTOBJECT","FONTEDIT",
        "VOLUMEOBJECT","EMPTYOBJECT","LATTICEOBJECT","LATTICEEDIT","LIGHTOBJECT","LIGHT_PROBEOBJECT","CAMERAOBJECT",
        "SPEAKEROBJECT","MESHOBJECT","MESHEDIT","GPENCILOBJECT","GPENCILEDIT_GPENCIL","GREASEPENCILOBJECT",
        "GREASEPENCILEDIT","ARMATUREOBJECT","ARMATUREEDIT","ARMATUREPOSE",
    ),
        'button_action_pivot_to_cursor':(
        "button.action_pivot_to_cursor","3D 游标","PIVOT_CURSOR",
        "CURVEOBJECT","CURVEEDIT","SURFACEOBJECT","SURFACEEDIT","METAOBJECT","METAEDIT","FONTOBJECT","FONTEDIT",
        "VOLUMEOBJECT","EMPTYOBJECT","LATTICEOBJECT","LATTICEEDIT","LIGHTOBJECT","LIGHT_PROBEOBJECT","CAMERAOBJECT",
        "SPEAKEROBJECT","MESHOBJECT","MESHEDIT","GPENCILOBJECT","GPENCILEDIT_GPENCIL","GREASEPENCILOBJECT",
        "GREASEPENCILEDIT","ARMATUREOBJECT","ARMATUREEDIT","ARMATUREPOSE",
    ),
        'button_action_pivot_to_individual_origins':(
        "button.action_pivot_to_individual_origins","各自的原点","PIVOT_INDIVIDUAL",
        "CURVEOBJECT","CURVEEDIT","SURFACEOBJECT","SURFACEEDIT","METAOBJECT","METAEDIT","FONTOBJECT","FONTEDIT",
        "VOLUMEOBJECT","EMPTYOBJECT","LATTICEOBJECT","LATTICEEDIT","LIGHTOBJECT","LIGHT_PROBEOBJECT","CAMERAOBJECT",
        "SPEAKEROBJECT","MESHOBJECT","MESHEDIT","GPENCILOBJECT","GPENCILEDIT_GPENCIL","GREASEPENCILOBJECT",
        "GREASEPENCILEDIT","ARMATUREOBJECT","ARMATUREEDIT","ARMATUREPOSE",
    ),
        'button_action_pivot_to_median_point':(
        "button.action_pivot_to_median_point","质心点","PIVOT_MEDIAN",
        "CURVEOBJECT","CURVEEDIT","SURFACEOBJECT","SURFACEEDIT","METAOBJECT","METAEDIT","FONTOBJECT","FONTEDIT",
        "VOLUMEOBJECT","EMPTYOBJECT","LATTICEOBJECT","LATTICEEDIT","LIGHTOBJECT","LIGHT_PROBEOBJECT","CAMERAOBJECT",
        "SPEAKEROBJECT","MESHOBJECT","MESHEDIT","GPENCILOBJECT","GPENCILEDIT_GPENCIL","GREASEPENCILOBJECT",
        "GREASEPENCILEDIT","ARMATUREOBJECT","ARMATUREEDIT","ARMATUREPOSE",
    ),
        'button_action_pivot_to_active_element':(
        "button.action_pivot_to_active_element","活动元素","PIVOT_ACTIVE",
        "CURVEOBJECT","CURVEEDIT","SURFACEOBJECT","SURFACEEDIT","METAOBJECT","METAEDIT","FONTOBJECT","FONTEDIT",
        "VOLUMEOBJECT","EMPTYOBJECT","LATTICEOBJECT","LATTICEEDIT","LIGHTOBJECT","LIGHT_PROBEOBJECT","CAMERAOBJECT",
        "SPEAKEROBJECT","MESHOBJECT","MESHEDIT","GPENCILOBJECT","GPENCILEDIT_GPENCIL","GREASEPENCILOBJECT",
        "GREASEPENCILEDIT","ARMATUREOBJECT","ARMATUREEDIT","ARMATUREPOSE",
    ),

    # “视图”菜单
        'button.action_view_selected_use_all_regions_false':(
        "button.action_view_selected_use_all_regions_false","框显所选","DOT","all",
    ),
        'button.action_view_all_center_false':(
        "button.action_view_all_center_false","框显全部","HOME","all",
    ),
        'button.action_view_persportho':(
        "button.action_view_persportho","透视/正交","RADIOBUT_OFF","all",
    ),
        'button.action_view3d_localview':(
        "button.action_view3d_localview","局部视图","RADIOBUT_OFF","all",
    ),
        'button.action_view3d_localview_remove_from':(
        "button.action_view3d_localview_remove_from","从局部视图中移除","RADIOBUT_OFF","all",
    ),
        'button.action_view3d_object_as_camera':(
        "button.action_view3d_object_as_camera","设置活动物体为摄像机","OUTLINER_OB_CAMERA","all",
    ),
        'button.action_view3d_view_camera':(
        "button.action_view3d_view_camera","摄像机","CAMERA_DATA","all",
    ),
        'button.action_view3d_view_center_camera':(
        "button.action_view3d_view_center_camera","摄像机边界框","OUTLINER_DATA_CAMERA","all",
    ),
        'button.action_view3d_call_menu_view_axis':(
        "button.action_view3d_call_menu_view_axis","视图","COLLAPSEMENU","all",
    ),
        'button.action_view3d_call_menu_view_switch_axis':(
        "button.action_view3d_call_menu_view_switch_axis","视图切换","COLLAPSEMENU","all",
    ),
        'button.action_view3d_zoom_border':(
        "button.action_view3d_zoom_border","框选放大","SELECT_SET","all",
    ),
        'button.action_view3d_fly':(
        "button.action_view3d_fly","飞行漫步","RADIOBUT_OFF","all",
    ),
        'button.action_view3d_walk':(
        "button.action_view3d_walk","行走漫步","RADIOBUT_OFF","all",
    ),
        'button.action_view3d_call_menu_view_align':(
        "button.action_view3d_call_menu_view_align","对齐视图","COLLAPSEMENU","all",
    ),
        'view3d.camera_to_view':(
        "view3d.camera_to_view","活动摄像机对齐当前视角","OUTLINER_DATA_CAMERA","all",
    ),
        'view3d.camera_to_view_selected':(
        "view3d.camera_to_view_selected","活动摄像机对齐选中的物体","OUTLINER_DATA_CAMERA","all",
    ),
        'button.action_view3d_lock_to_active_or_lock_clear':(
        "button.action_view3d_lock_to_active_or_lock_clear","锁定/解锁视图","CON_CAMERASOLVER","all",
    ),
        'button.action_view3d_call_menu_view_regions':(
        "button.action_view3d_call_menu_view_regions","视图框","COLLAPSEMENU","all",
    ),
        'button.action_view3d_clip_border':(
        "button.action_view3d_clip_border","裁剪框","CLIPUV_DEHLT","all",
    ),
        'button.action_view3d_render_border':(
        "button.action_view3d_render_border","渲染框","RADIOBUT_OFF","all",
    ),
        'view3d.clear_render_border':(
        "view3d.clear_render_border","清除渲染框","RADIOBUT_OFF","all",
    ),

    # “选择”菜单
        'button.action_view3d_call_select_select_by_type_menu':(
        "button.action_view3d_call_select_select_by_type_menu","按类型选择","COLLAPSEMENU",
        "CURVEOBJECT",  "SURFACEOBJECT", "METAOBJECT", "FONTOBJECT", "VOLUMEOBJECT", "EMPTYOBJECT", "LATTICEOBJECT", 
        "LIGHTOBJECT", "LIGHT_PROBEOBJECT", "CAMERAOBJECT", "SPEAKEROBJECT", "MESHOBJECT",
        "GPENCILOBJECT", "GREASEPENCILOBJECT", "ARMATUREOBJECT",
    ),
        'object.select_camera':(
        "object.select_camera","选择活动摄像机","CAMERA_DATA",
        "CURVEOBJECT",  "SURFACEOBJECT", "METAOBJECT", "FONTOBJECT", "VOLUMEOBJECT", "EMPTYOBJECT", "LATTICEOBJECT", 
        "LIGHTOBJECT", "LIGHT_PROBEOBJECT", "CAMERAOBJECT", "SPEAKEROBJECT", "MESHOBJECT",
        "GPENCILOBJECT", "GREASEPENCILOBJECT", "ARMATUREOBJECT",
    ),
        'button.action_select_select_mirror':(
        "button.action_select_select_mirror","选择镜像","MOD_MIRROR",
        "CURVEOBJECT", "SURFACEOBJECT", "METAOBJECT", "FONTOBJECT", "VOLUMEOBJECT", "EMPTYOBJECT", "LATTICEOBJECT", 
        "LATTICEEDIT", "LIGHTOBJECT", "LIGHT_PROBEOBJECT", "CAMERAOBJECT", "SPEAKEROBJECT", "MESHOBJECT",
        "MESHEDIT", "GPENCILOBJECT", "GREASEPENCILOBJECT", "ARMATUREOBJECT", "ARMATUREEDIT", "ARMATUREPOSE",
    ),
        'button.action_select_select_random':(
        "button.action_select_select_random","随机选择","RADIOBUT_OFF",
        "CURVEOBJECT", "CURVEEDIT", "SURFACEOBJECT", "SURFACEEDIT",  "METAOBJECT", "METAEDIT",
        "FONTOBJECT", "VOLUMEOBJECT", "EMPTYOBJECT", "LATTICEOBJECT", "LATTICEEDIT",
        "LIGHTOBJECT", "LIGHT_PROBEOBJECT", "CAMERAOBJECT", "SPEAKEROBJECT", "MESHOBJECT",
        "MESHEDIT", "GPENCILOBJECT", "GPENCILEDIT_GPENCIL", "GREASEPENCILOBJECT", "GREASEPENCILEDIT", 
        "GREASEPENCILVERTEX_GREASE_PENCIL", "ARMATUREOBJECT",
    ),
        'button.action_call_object_select_more_or_less_menu':(
        "button.action_call_object_select_more_or_less_menu","加选/减选","COLLAPSEMENU",
        "CURVEOBJECT", "CURVEEDIT", "SURFACEOBJECT", "SURFACEEDIT",  "METAOBJECT",
        "FONTOBJECT", "VOLUMEOBJECT", "EMPTYOBJECT", "LATTICEOBJECT", "LATTICEEDIT",
        "LIGHTOBJECT", "LIGHT_PROBEOBJECT", "CAMERAOBJECT", "SPEAKEROBJECT", "MESHOBJECT",
        "MESHEDIT", "GPENCILOBJECT", "GREASEPENCILOBJECT", "ARMATUREOBJECT", "ARMATUREEDIT", "ARMATUREPOSE",
    ),
        'button.action_object_select_more':(
        "button.action_object_select_more","加选","ADD",
        "CURVEOBJECT", "CURVEEDIT", "SURFACEOBJECT", "SURFACEEDIT",  "METAOBJECT",
        "FONTOBJECT", "VOLUMEOBJECT", "EMPTYOBJECT", "LATTICEOBJECT", "LATTICEEDIT",
        "LIGHTOBJECT", "LIGHT_PROBEOBJECT", "CAMERAOBJECT", "SPEAKEROBJECT", "MESHOBJECT",
        "MESHEDIT", "GPENCILOBJECT", "GPENCILEDIT_GPENCIL", "GREASEPENCILOBJECT", "GREASEPENCILEDIT", 
        "ARMATUREOBJECT", "ARMATUREEDIT",
    ),
        'button.action_object_select_less':(
        "button.action_object_select_less","减选","REMOVE",
        "CURVEOBJECT", "CURVEEDIT", "SURFACEOBJECT", "SURFACEEDIT",  "METAOBJECT",
        "FONTOBJECT", "VOLUMEOBJECT", "EMPTYOBJECT", "LATTICEOBJECT", "LATTICEEDIT",
        "LIGHTOBJECT", "LIGHT_PROBEOBJECT", "CAMERAOBJECT", "SPEAKEROBJECT", "MESHOBJECT",
        "MESHEDIT", "GPENCILOBJECT", "GPENCILEDIT_GPENCIL", "GREASEPENCILOBJECT", "GREASEPENCILEDIT", 
        "ARMATUREOBJECT", "ARMATUREEDIT",
    ),
        'button.action_object_select_hierarchy_parent_child':(
        "button.action_object_select_hierarchy_parent_child","父级/子级","ORIENTATION_PARENT",
        "CURVEOBJECT", "SURFACEOBJECT", "METAOBJECT",
        "FONTOBJECT", "VOLUMEOBJECT", "EMPTYOBJECT", "LATTICEOBJECT", 
        "LIGHTOBJECT", "LIGHT_PROBEOBJECT", "CAMERAOBJECT", "SPEAKEROBJECT", "MESHOBJECT",
        "GPENCILOBJECT", "GREASEPENCILOBJECT","ARMATUREOBJECT", "ARMATUREEDIT","ARMATUREPOSE",
    ),
        'button.action_call_select_select_grouped_menu':(
        "button.action_call_select_select_grouped_menu","按组/相似选择","COLLAPSEMENU",
        "CURVEOBJECT", "SURFACEOBJECT", "METAOBJECT","MESHEDIT","GPENCILEDIT_GPENCIL","GPENCILVERTEX_GPENCIL",
        "FONTOBJECT", "VOLUMEOBJECT", "EMPTYOBJECT", "LATTICEOBJECT", "GREASEPENCILEDIT",
        "GREASEPENCILVERTEX_GREASE_PENCIL", "LIGHTOBJECT", "LIGHT_PROBEOBJECT", "CAMERAOBJECT", "SPEAKEROBJECT", 
        "MESHOBJECT","GPENCILOBJECT", "GREASEPENCILOBJECT","ARMATUREOBJECT", "ARMATUREEDIT",
        "ARMATUREPOSE","CURVEEDIT","SURFACEEDIT","METAEDIT",
    ),
        'button.action_call_select_select_linked_menu':(
        "button.action_call_select_select_linked_menu","选择相连元素","COLLAPSEMENU",
        "CURVEOBJECT", "SURFACEOBJECT", "METAOBJECT", "FONTOBJECT", "VOLUMEOBJECT", "EMPTYOBJECT", 
        "LATTICEOBJECT", "LIGHTOBJECT", "LIGHT_PROBEOBJECT", "CAMERAOBJECT", "SPEAKEROBJECT", 
        "MESHOBJECT","GPENCILOBJECT", "GREASEPENCILOBJECT","ARMATUREOBJECT","CURVEEDIT","SURFACEEDIT",
        "MESHEDIT","GPENCILEDIT_GPENCIL", "GREASEPENCILEDIT","ARMATUREEDIT", "ARMATUREPOSE",
    ),
        'object.select_pattern':(
        "object.select_pattern","按名称选择","RADIOBUT_OFF",
        "CURVEOBJECT", "SURFACEOBJECT", "METAOBJECT", "FONTOBJECT", "VOLUMEOBJECT", "EMPTYOBJECT", 
        "LATTICEOBJECT", "LIGHTOBJECT", "LIGHT_PROBEOBJECT", "CAMERAOBJECT", "SPEAKEROBJECT", 
        "MESHOBJECT","GPENCILOBJECT", "GREASEPENCILOBJECT","ARMATUREOBJECT","ARMATUREEDIT", "ARMATUREPOSE",
    ),

    # 一些通用操作
        'button.action_call_common_function_transform_menu':(
        "button.action_call_common_function_transform_menu","变换","COLLAPSEMENU", "CURVEOBJECT", "SURFACEOBJECT", "METAOBJECT",
        "FONTOBJECT", "VOLUMEOBJECT", "EMPTYOBJECT", "LATTICEOBJECT", "LIGHTOBJECT", "LIGHT_PROBEOBJECT", 
        "CAMERAOBJECT", "SPEAKEROBJECT", "MESHOBJECT","GPENCILOBJECT", "GREASEPENCILOBJECT","ARMATUREOBJECT","LATTICEEDIT",
        "CURVEEDIT",'SURFACEEDIT','METAEDIT','MESHEDIT','ARMATUREEDIT',"ARMATUREPOSE","GPENCILEDIT_GPENCIL","GREASEPENCILEDIT",
    ),
        'button.action_transform_tosphere':(
        "button.action_transform_tosphere","球形化","RADIOBUT_OFF", "CURVEOBJECT", "SURFACEOBJECT", "METAOBJECT",
        "FONTOBJECT", "VOLUMEOBJECT", "EMPTYOBJECT", "LATTICEOBJECT", "LIGHTOBJECT", "LIGHT_PROBEOBJECT", 
        "CAMERAOBJECT", "SPEAKEROBJECT", "MESHOBJECT","GPENCILOBJECT", "GREASEPENCILOBJECT","ARMATUREOBJECT","LATTICEEDIT",
        "CURVEEDIT",'SURFACEEDIT','METAEDIT','MESHEDIT','ARMATUREEDIT',"ARMATUREPOSE","GPENCILEDIT_GPENCIL","GREASEPENCILEDIT",
    ),
        'button.action_transform_shear':(
        "button.action_transform_shear","切变","RADIOBUT_OFF", "CURVEOBJECT", "SURFACEOBJECT", "METAOBJECT",
        "FONTOBJECT", "VOLUMEOBJECT", "EMPTYOBJECT", "LATTICEOBJECT", "LIGHTOBJECT", "LIGHT_PROBEOBJECT", 
        "CAMERAOBJECT", "SPEAKEROBJECT", "MESHOBJECT","GPENCILOBJECT", "GREASEPENCILOBJECT","ARMATUREOBJECT","LATTICEEDIT",
        "CURVEEDIT",'SURFACEEDIT','METAEDIT','MESHEDIT','ARMATUREEDIT',"ARMATUREPOSE","GPENCILEDIT_GPENCIL","GREASEPENCILEDIT",
    ),
        'button.action_transform_bend':(
        "button.action_transform_bend","弯曲","RADIOBUT_OFF", "CURVEOBJECT", "SURFACEOBJECT", "METAOBJECT",
        "FONTOBJECT", "VOLUMEOBJECT", "EMPTYOBJECT", "LATTICEOBJECT", "LIGHTOBJECT", "LIGHT_PROBEOBJECT", 
        "CAMERAOBJECT", "SPEAKEROBJECT", "MESHOBJECT","GPENCILOBJECT", "GREASEPENCILOBJECT","ARMATUREOBJECT","LATTICEEDIT",
        "CURVEEDIT",'SURFACEEDIT','METAEDIT','MESHEDIT','ARMATUREEDIT',"ARMATUREPOSE","GPENCILEDIT_GPENCIL","GREASEPENCILEDIT",
    ),
        'button.action_transform_push_pull':(
        "button.action_transform_push_pull","推/拉","RADIOBUT_OFF", "CURVEOBJECT", "SURFACEOBJECT", "METAOBJECT",
        "FONTOBJECT", "VOLUMEOBJECT", "EMPTYOBJECT", "LATTICEOBJECT", "LIGHTOBJECT", "LIGHT_PROBEOBJECT", 
        "CAMERAOBJECT", "SPEAKEROBJECT", "MESHOBJECT","GPENCILOBJECT", "GREASEPENCILOBJECT","ARMATUREOBJECT","LATTICEEDIT",
        "CURVEEDIT",'SURFACEEDIT','METAEDIT','MESHEDIT','ARMATUREEDIT',"ARMATUREPOSE","GPENCILEDIT_GPENCIL","GREASEPENCILEDIT",
    ),
        'button.action_transform_translate_texturespace_true':(
        "button.action_transform_translate_texturespace_true","移动纹理空间","RADIOBUT_OFF", "CURVEOBJECT", "SURFACEOBJECT", "METAOBJECT",
        "FONTOBJECT", "VOLUMEOBJECT", "EMPTYOBJECT", "LATTICEOBJECT", "LIGHTOBJECT", "LIGHT_PROBEOBJECT", 
        "CAMERAOBJECT", "SPEAKEROBJECT", "MESHOBJECT","GPENCILOBJECT", "GREASEPENCILOBJECT","ARMATUREOBJECT","LATTICEEDIT",
        "CURVEEDIT",'SURFACEEDIT','METAEDIT','MESHEDIT','ARMATUREEDIT',"ARMATUREPOSE","GPENCILEDIT_GPENCIL","GREASEPENCILEDIT",
    ),
        'button.action_transform_resize_texturespace_true':(
        "button.action_transform_resize_texturespace_true","缩放纹理空间","RADIOBUT_OFF", "CURVEOBJECT", "SURFACEOBJECT", "METAOBJECT",
        "FONTOBJECT", "VOLUMEOBJECT", "EMPTYOBJECT", "LATTICEOBJECT", "LIGHTOBJECT", "LIGHT_PROBEOBJECT", 
        "CAMERAOBJECT", "SPEAKEROBJECT", "MESHOBJECT","GPENCILOBJECT", "GREASEPENCILOBJECT","ARMATUREOBJECT","LATTICEEDIT",
        "CURVEEDIT",'SURFACEEDIT','METAEDIT','MESHEDIT','ARMATUREEDIT',"ARMATUREPOSE","GPENCILEDIT_GPENCIL","GREASEPENCILEDIT",
    ),
        'transform.vertex_warp':(
        "transform.vertex_warp","弯绕","RADIOBUT_OFF", 
        "LATTICEEDIT", "CURVEEDIT",'SURFACEEDIT','METAEDIT','MESHEDIT','ARMATUREEDIT',
    ),
        'button.action_transform_vertex_random':(
        "button.action_transform_vertex_random","随机","RADIOBUT_OFF", 
        "LATTICEEDIT", "CURVEEDIT",'SURFACEEDIT','METAEDIT','MESHEDIT','ARMATUREEDIT',
    ),

    # 物体模式——“物体”菜单
        'button.action_global_duplicate_move_linked':(
        "button.action_global_duplicate_move_linked","关联复制","DUPLICATE", "CURVEOBJECT", "SURFACEOBJECT",
        "FONTOBJECT", "VOLUMEOBJECT", "EMPTYOBJECT", "LATTICEOBJECT", "LIGHTOBJECT", "LIGHT_PROBEOBJECT", 
        "CAMERAOBJECT", "SPEAKEROBJECT", "MESHOBJECT","GPENCILOBJECT", "GREASEPENCILOBJECT", "METAOBJECT",
    ),
        'object.join':(
        "object.join","合并","RADIOBUT_OFF", "MESHOBJECT",
    ),
        'button.action_object_object_transform_transform_mode_align':(
        "button.action_object_object_transform_transform_mode_align","对齐到变换坐标系","RADIOBUT_OFF", "CURVEOBJECT", "SURFACEOBJECT", 
        "METAOBJECT", "FONTOBJECT", "VOLUMEOBJECT", "EMPTYOBJECT", "LATTICEOBJECT", "LIGHTOBJECT", "LIGHT_PROBEOBJECT", 
        "CAMERAOBJECT", "SPEAKEROBJECT", "MESHOBJECT","GPENCILOBJECT", "GREASEPENCILOBJECT","ARMATUREOBJECT",
    ),
        'object.randomize_transform':(
        "object.randomize_transform","随机变换","RADIOBUT_OFF", "CURVEOBJECT", "SURFACEOBJECT", "METAOBJECT",
        "FONTOBJECT", "VOLUMEOBJECT", "EMPTYOBJECT", "LATTICEOBJECT", "LIGHTOBJECT", "LIGHT_PROBEOBJECT", 
        "CAMERAOBJECT", "SPEAKEROBJECT", "MESHOBJECT","GPENCILOBJECT", "GREASEPENCILOBJECT","ARMATUREOBJECT",
    ),
        'object.align':(
        "object.align","对齐物体","RADIOBUT_OFF", "CURVEOBJECT", "SURFACEOBJECT", "METAOBJECT",
        "FONTOBJECT", "VOLUMEOBJECT", "EMPTYOBJECT", "LATTICEOBJECT", "LIGHTOBJECT", "LIGHT_PROBEOBJECT", 
        "CAMERAOBJECT", "SPEAKEROBJECT", "MESHOBJECT","GPENCILOBJECT", "GREASEPENCILOBJECT","ARMATUREOBJECT",
    ),

    # 测试功能
    'testone':("mode.tab_switch","智能切换","CUBE","GREASEPENCILOBJECT","MESHEDIT"),
    'testtwo':("wm.toolbar","系统快捷键","BOOKMARKS","OBJCET","GREASEPENCILOBJECT","MESHEDIT","MESHOBJECT"),
    'SEPARATOR':(),
    'NO_BUTTON':(),
}
