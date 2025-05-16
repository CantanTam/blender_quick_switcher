
button_options_list = [
    ('NO_BUTTON',"○无按钮○","默认不显示按钮"),
    ('SEPARATOR', '◂◂◂间隔▸▸▸', '弹出菜单间隔符'),

    # 全局高频操作：
    ('NO_BUTTON',"←全局通用常用操作→","全局都使用的高频操作"),
    ('button.action_global_grab','移动','移动'),        #已添加Switcher
    ('button.action_global_scale','缩放','缩放'),       #switcher
    ('button.action_global_rotate','旋转','旋转'),      #已添加Switcher
    ('button.action_global_select_all','全选','快捷键(A)'), #Switcher
    ('button.action_global_select_invert','反选','快捷键(Ctrl I)'), #Switcher
    ('button.action_global_select_circle','刷选','快捷键(C)'),  #Switcher
    ('button.action_global_add',"添加(菜单)","不同的模式当中，调出不同的添加菜单"),     #Switcher
    ('button.action_global_duplicate_move',"复制","快捷键(Shift D)"),   #Switcher
    ('button.action_global_copy',"复制","物体模式/蜡笔编辑模式共用的“复制(Ctrl C)”操作"),   #Switcher
    ('button.action_global_paste',"粘贴","物体模式/蜡笔编辑模式共用的“粘贴(Ctrl V)”操作"),  #Swithcer
    ('button.action_global_call_delete_menu',"删除","多种编辑模式共用的“删除(X)”操作"),     #Switcher
    ('button.action_global_hide_view_set',"隐藏","多种编辑模式共用的“隐藏(H)”操作"),    #Switcher
    ('button.action_global_hide_view_clear',"显示隐藏项","多种编辑模式共用的“显示隐藏项(Alt H)”操作"),  #Switcher
    ('button.action_global_apply',"应用","物体模式/骨架姿态模式共用的“应用(Ctrl A)”操作"),  #Switcher
    ('button.action_global_transform_mirror',"交互镜像","物体模式/网格编辑模式/骨架姿态模式共用的“交互镜像(Ctrl M)”操作"),  #Switcher
    ('button.action_global_object_pose_clear',"清空变换(菜单)","物体模式/骨骼姿态模式“清空变换”菜单"),  #Switcher


    # 切换坐标系
    ('NO_BUTTON',"←切换坐标系→",""),
    ('button.action_switch_orientation_menu','切换坐标系(菜单)','弹出切换坐标系菜单'),  #Switcher
    ('button.action_orientation_to_global','切换坐标系-全局','全局坐标系'),  #Switcher
    ('button.action_orientation_to_local','切换坐标系-局部','局部坐标系'),  #Switcher
    ('button.action_orientation_to_normal','切换坐标系-法向','法向坐标系'),  #Switcher
    ('button.action_orientation_to_gimbal','切换坐标系-万向','万向坐标系'),  #Switcher
    ('button.action_orientation_to_view','切换坐标系-视图','视图坐标系'),  #Switcher
    ('button.action_orientation_to_cursor','切换坐标系-游标','游标坐标系'),  #Switcher
    ('button.action_orientation_to_parent','切换坐标系-父级','父级坐标系'),  #Switcher

    # 切换轴心点
    ('NO_BUTTON',"←切换轴心点→",""),
    ('button.action_switch_pivot_menu','切换轴心点(菜单)','弹出切换轴心点菜单'),
    ('button.action_pivot_to_bounding_box_center','切换轴心点—边界框中心','边界框中心'),
    ('button.action_pivot_to_cursor','切换轴心点—3D 游标','3D 游标'),
    ('button.action_pivot_to_individual_origins','切换轴心点—各自的原点','各自的原点'),
    ('button.action_pivot_to_median_point','切换轴心点—质心点','质心点'),
    ('button.action_pivot_to_active_element','切换轴心点—活动元素','活动元素'),

    # 切换吸附
    ('NO_BUTTON',"←切换吸附→",""),
    ('button.action_switch_snap_menu','切换吸附(菜单)','弹出切换切换菜单'), #Swithcer
    ('button.action_switch_snap_toggle','开/关吸附','快捷键(Shift Tab)'),   #Swithcer
    ('button.action_switch_snap_increment','切换吸附-增量',''), #Swithcer
    ('button.action_switch_snap_vertex','切换吸附-顶点',''),    #Swithcer
    ('button.action_switch_snap_edge','切换吸附-边',''),    #Swithcer
    ('button.action_switch_snap_face','切换吸附-面投射',''),    #Swithcer
    ('button.action_switch_snap_face_nearest','切换吸附-面最近',''),    #Swithcer
    ('button.action_switch_snap_volume','切换吸附-体积',''),    #Swithcer
    ('button.action_switch_snap_edge_midpoint','切换吸附-边中点',''),   #Swithcer
    ('button.action_switch_snap_edge_perpendicular','切换吸附-垂直交线',''),    #Swithcer

    # 切换衰减编辑
    ('NO_BUTTON',"←切换衰减编辑→",""),
    ('button.action_switch_proportional_menu','切换衰减编辑(菜单)','弹出衰减编辑菜单'), #Swithcer
    ('button.action_switch_proportional_toggle','开/关衰减编辑','快捷键(O)'),   #Swithcer
    ('button.action_switch_proportional_smooth','切换衰减-平滑',''), #Swithcer
    ('button.action_switch_proportional_sphere','切换衰减-球体',''),    #Swithcer
    ('button.action_switch_proportional_root','切换衰减-根凸',''),    #Swithcer
    ('button.action_switch_proportional_inverse_square','切换衰减-平方反比',''),    #Swithcer
    ('button.action_switch_proportional_sharp','切换衰减-锐利',''),    #Swithcer
    ('button.action_switch_proportional_linear','切换衰减-线性',''),   #Swithcer
    ('button.action_switch_proportional_constant','切换衰减-常值',''),    #Swithcer
    ('button.action_switch_proportional_random','切换衰减-随机',''),    #Swithcer

    # 通用模式——共用功能
    ('NO_BUTTON',"←通用模式-“变换”菜单→","不同模式下“变换”菜单中都会出现的选项，被合并到这里"),
    ('button.action_transform_tosphere',"变换—球形化","多种模式共用的“球形化”操作"),
    ('button.action_transform_shear',"变换—切变","多种模式共用的“切变”操作"),
    ('button.action_transform_bend',"变换—弯曲","多种模式共用的“弯曲”操作"),

    # 通用模式——“视图”菜单，在所有模式都可以调出的菜单
    ('NO_BUTTON',"←全局模式-视图(菜单)→","全局模式当中的按钮功能可以在所有模式当中使用"),
    ('button.action_view3d_view_selected','框显所选','快捷键(.)'),    #Switcher
    ('button.action_view3d_view_all','框显全部','快捷键(Home)'),  #Switcher
    ('button.action_view3d_localview','局部视图—切换局部视图','快捷键(/)'),   #Switcher
    ('view3d.localview_remove_from','局部视图—从局部视图中移除','快捷键(Alt+/)'),   #Switcher
    ('button.action_view3d_object_as_camera','摄像机—设置活动物体为摄像机','快捷键(Ctrl+Num_0)'), #Switcher
    ('button.action_view3d_view_center_camera','摄像机—摄像机边界框','快捷键(Home)'), #Switcher
    ('button.action_view3d_call_view_viewpoint_menu','视图(菜单)',''),  #Switcher
    ('button.action_view3d_call_view_navigation_menu','视图切换(菜单)',''), #Switcher
    ('button.action_view3d_zoom_border','视图切换—框选放大','快捷键(Shift+B)'), #Switcher
    ('button.action_zoom_camera_1_to_1','视图切换—1:1缩放摄像机视图',''),    #Switcher
    ('button.action_view3d_fly','视图切换—飞行漫游模式',''),    #Switcher
    ('button.action_view3d_walk','视图切换—行走漫步','快捷键(Shift+`)'),    #Switcher
    ('button.action_view3d_call_view_align_selected_menu','对齐视图-视图对齐活动项(菜单)',''),    #Switcher
    ('button.action_view3d_call_view_align_menu','对齐视图(菜单)',''),
    ('button.action_view3d_camera_to_view','对齐视图—活动摄像机对齐当前视角','快捷键(Ctrl+Alt+Num_0)'), #Switcher
    ('button.action_view3d_camera_to_view_selected','对齐视图—活动摄像机对齐选中的物体',''), #Switcher
    ('button.action_view3d_view_all_center_true','对齐视图—游标居中并查看全部','快捷键(Shift+C)'),  #Switcher
    ('button.action_view3d_view_center_cursor','对齐视图—视图中心对齐游标',''), #Switcher
    ('button.action_view3d_lock_to_active_or_lock_clear','对齐视图—锁定/解锁视图',''),  #Switcher
    ('button.action_view3d_call_view_regions_menu','视图框(菜单)',''),  #Switcher
    ('button.action_view3d_clip_border','视图框—裁剪框','快捷键(Alt+B)'),   #Switcher
    ('button.action_view3d_render_border','视图框—开/关渲染框','快捷键(Ctrl+B)'),    #Switcher

    ('button.action_view3d_render_opengl','视图渲染图像',''),   #Switcher
    ('button.action_view3d_render_opengl_animation','视图渲染动画',''),     #Switcher
    ('button.action_view3d_render_opengl_keyframe','视图渲染关键帧',''),    #Switcher

    ('button.action_view3d_area_menu','区域(菜单)',''), #Switcher
    ('screen.region_quadview','区域—切换四格视图','快捷键(Ctrl Alt Q)'),    #Switcher
    ('screen.screen_full_area','区域—区域最大化','快捷键(Ctrl 空格)'),  #Switcher
    ('button.action_view3d_screen_screen_full_area','区域—切换全屏模式','快捷键(Ctrl Alt 空格)'),   #Switcher

    # 通用模式——“选择”菜单，不同模式实现不同的“选择”功能
    ('NO_BUTTON',"←共用模式——“选择”菜单→","不同模式当中含有相同快捷键，而且功能名称接近的按钮被整合到这里"),
    ('button.action_call_select_select_by_type_menu','按类型全选(菜单)',''), #Switcher
    ('object.select_camera','选择活动摄像机',''),   #Switcher

    ('button.action_select_select_mirror','选择镜像','快捷键(Ctrl Shift M)'),   #Switcher
    ('button.action_select_select_random','随机选择',''),   #Switcher

    ('button.action_call_object_select_more_or_less_menu','加选/减选(菜单)',''),    #Switcher
    ('button.action_object_select_hierarchy_parent_child','父级/子级','父级/子级/扩展父级/扩展子级功能集合'),   #Switcher
    ('button.action_select_select_grouped','按组选择(菜单)','快捷键(Shift G)'), #Switcher
    ('button.action_select_select_linked','选择相连',''), #Switcher

    # 物体模式——“选择”菜单
    ('NO_BUTTON',"←物体模式-选择菜单→","“物体—选择”菜单中显示的选项"),

    # 物体模式——“物体”菜单
    ('NO_BUTTON',"←物体模式-物体菜单→","“物体—物体”菜单中显示的选项"),
    ('button.action_object_object_duplicate_move_linked',"关联复制","快捷键(Alt D)"),
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
        "button.action_global_add","添加","PLUS", "CURVEOBJECT", "SURFACEOBJECT", "METAOBJECT",
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
        "GREASEPENCILEDIT","ARMATUREOBJECT", "ARMATUREPOSE",
    ),
        'button.action_global_paste':(
        "button.action_global_paste","粘贴","PASTEDOWN", "CURVEOBJECT", "SURFACEOBJECT", "METAOBJECT",
        "FONTOBJECT", "VOLUMEOBJECT", "EMPTYOBJECT", "LATTICEOBJECT", "LIGHTOBJECT", "LIGHT_PROBEOBJECT", 
        "CAMERAOBJECT", "SPEAKEROBJECT", "MESHOBJECT","GPENCILOBJECT", "GPENCILEDIT_GPENCIL", "GREASEPENCILOBJECT",
        "GREASEPENCILEDIT","ARMATUREOBJECT", "ARMATUREPOSE",
    ),
        'button.action_global_call_delete_menu':(
        "button.action_global_call_delete_menu","删除","EVENT_X", "CURVEOBJECT", "SURFACEOBJECT", "METAOBJECT",
        "FONTOBJECT", "VOLUMEOBJECT", "EMPTYOBJECT", "LATTICEOBJECT", "LIGHTOBJECT", "LIGHT_PROBEOBJECT", 
        "CAMERAOBJECT", "SPEAKEROBJECT", "MESHOBJECT","GPENCILOBJECT", "GPENCILEDIT_GPENCIL", "GREASEPENCILOBJECT",
        "GREASEPENCILEDIT","ARMATUREOBJECT", "MESHEDIT","METAEDIT","GPENCILPAINT_GPENCIL","ARMATUREEDIT",
        "CURVEEDIT","SURFACEEDIT","GREASEPENCILPAINT_GREASE_PENCIL",
    ),

    # 全局高频操作——“隐藏”/“隐藏未选项”/“显示隐藏项”
        'button.action_global_hide_view_set':(
        "button.action_global_hide_view_set","隐藏","EVENT_H", "CURVEOBJECT", "SURFACEOBJECT", "METAOBJECT",
        "FONTOBJECT", "VOLUMEOBJECT", "EMPTYOBJECT", "LATTICEOBJECT", "LIGHTOBJECT", "LIGHT_PROBEOBJECT", 
        "CAMERAOBJECT", "SPEAKEROBJECT", "MESHOBJECT","GPENCILOBJECT", "GPENCILEDIT_GPENCIL", "GREASEPENCILOBJECT",
        "GREASEPENCILEDIT","ARMATUREOBJECT", "MESHEDIT","METAEDIT","GPENCILPAINT_GPENCIL","ARMATUREEDIT",
        "CURVEEDIT","SURFACEEDIT","ARMATUREEDIT","ARMATUREPOSE",
    ),
        'button.action_global_hide_view_clear':(
        "button.action_global_hide_view_clear","显示隐藏项","HIDE_OFF", "CURVEOBJECT", "SURFACEOBJECT", "METAOBJECT",
        "FONTOBJECT", "VOLUMEOBJECT", "EMPTYOBJECT", "LATTICEOBJECT", "LIGHTOBJECT", "LIGHT_PROBEOBJECT", 
        "CAMERAOBJECT", "SPEAKEROBJECT", "MESHOBJECT","GPENCILOBJECT", "GPENCILEDIT_GPENCIL", "GREASEPENCILOBJECT",
        "GREASEPENCILEDIT","ARMATUREOBJECT", "MESHEDIT","METAEDIT","GPENCILPAINT_GPENCIL","ARMATUREEDIT",
        "CURVEEDIT","SURFACEEDIT","ARMATUREEDIT","ARMATUREPOSE",
    ),
        'button.action_global_apply':(
        "button.action_global_apply","应用","PRESET", "CURVEOBJECT", "SURFACEOBJECT", "METAOBJECT",
        "FONTOBJECT", "VOLUMEOBJECT", "EMPTYOBJECT", "LATTICEOBJECT", "LIGHTOBJECT", "LIGHT_PROBEOBJECT", 
        "CAMERAOBJECT", "SPEAKEROBJECT", "MESHOBJECT","GPENCILOBJECT", "GREASEPENCILOBJECT",
        "ARMATUREOBJECT", "ARMATUREEDIT", "ARMATUREPOSE",
    ),
        'button.action_global_transform_mirror':( #“交互镜像”
        "button.action_global_transform_mirror","交互镜像","MOD_MIRROR", "CURVEOBJECT", "SURFACEOBJECT", "METAOBJECT",
        "FONTOBJECT", "VOLUMEOBJECT", "EMPTYOBJECT", "LATTICEOBJECT", "LIGHTOBJECT", "LIGHT_PROBEOBJECT", 
        "CAMERAOBJECT", "SPEAKEROBJECT", "MESHOBJECT","GPENCILOBJECT", "GREASEPENCILOBJECT",
        "ARMATUREOBJECT", "MESHEDIT","CURVEEDIT","SURFACEEDIT","METAEDIT","GPENCILEDIT_GPENCIL","GREASEPENCILEDIT",
        "ARMATUREEDIT","ARMATUREPOSE","LATTICEEDIT",
    ),
        'button.action_global_object_pose_clear':( # 清空变换(菜单)
        "button.action_global_object_pose_clear","清空变换","PRESET", "CURVEOBJECT", "SURFACEOBJECT", "METAOBJECT",
        "FONTOBJECT", "VOLUMEOBJECT", "EMPTYOBJECT", "LATTICEOBJECT", "LIGHTOBJECT", "LIGHT_PROBEOBJECT", 
        "CAMERAOBJECT", "SPEAKEROBJECT", "MESHOBJECT","GPENCILOBJECT", "GREASEPENCILOBJECT",
        "ARMATUREOBJECT", "ARMATUREPOSE",
    ),

        # 切换坐标系
        'button.action_switch_orientation_menu':(
        "button.action_switch_orientation_menu","切换坐标系","PRESET",
        "CURVEOBJECT","CURVEEDIT","SURFACEOBJECT","SURFACEEDIT","METAOBJECT","METAEDIT","FONTOBJECT","FONTEDIT",
        "VOLUMEOBJECT","EMPTYOBJECT","LATTICEOBJECT","LATTICEEDIT","LIGHTOBJECT","LIGHT_PROBEOBJECT","CAMERAOBJECT",
        "SPEAKEROBJECT","MESHOBJECT","MESHEDIT","GPENCILOBJECT","GPENCILEDIT_GPENCIL","GREASEPENCILOBJECT",
        "GREASEPENCILEDIT","ARMATUREOBJECT","ARMATUREEDIT","ARMATUREPOSE",
    ),
        'button.action_orientation_to_global':(
        "button.action_orientation_to_global","全局","ORIENTATION_GLOBAL",
        "CURVEOBJECT","CURVEEDIT","SURFACEOBJECT","SURFACEEDIT","METAOBJECT","METAEDIT","FONTOBJECT","FONTEDIT",
        "VOLUMEOBJECT","EMPTYOBJECT","LATTICEOBJECT","LATTICEEDIT","LIGHTOBJECT","LIGHT_PROBEOBJECT","CAMERAOBJECT",
        "SPEAKEROBJECT","MESHOBJECT","MESHEDIT","GPENCILOBJECT","GPENCILEDIT_GPENCIL","GREASEPENCILOBJECT",
        "GREASEPENCILEDIT","ARMATUREOBJECT","ARMATUREEDIT","ARMATUREPOSE",
    ),
        'button.action_orientation_to_local':(
        "button.action_orientation_to_local","局部","ORIENTATION_LOCAL",
        "CURVEOBJECT","CURVEEDIT","SURFACEOBJECT","SURFACEEDIT","METAOBJECT","METAEDIT","FONTOBJECT","FONTEDIT",
        "VOLUMEOBJECT","EMPTYOBJECT","LATTICEOBJECT","LATTICEEDIT","LIGHTOBJECT","LIGHT_PROBEOBJECT","CAMERAOBJECT",
        "SPEAKEROBJECT","MESHOBJECT","MESHEDIT","GPENCILOBJECT","GPENCILEDIT_GPENCIL","GREASEPENCILOBJECT",
        "GREASEPENCILEDIT","ARMATUREOBJECT","ARMATUREEDIT","ARMATUREPOSE",
    ),
        'button.action_orientation_to_normal':(
        "button.action_orientation_to_normal","法向","ORIENTATION_NORMAL",
        "CURVEOBJECT","CURVEEDIT","SURFACEOBJECT","SURFACEEDIT","METAOBJECT","METAEDIT","FONTOBJECT","FONTEDIT",
        "VOLUMEOBJECT","EMPTYOBJECT","LATTICEOBJECT","LATTICEEDIT","LIGHTOBJECT","LIGHT_PROBEOBJECT","CAMERAOBJECT",
        "SPEAKEROBJECT","MESHOBJECT","MESHEDIT","GPENCILOBJECT","GPENCILEDIT_GPENCIL","GREASEPENCILOBJECT",
        "GREASEPENCILEDIT","ARMATUREOBJECT","ARMATUREEDIT","ARMATUREPOSE",
    ),
        'button.action_orientation_to_gimbal':(
        "button.action_orientation_to_gimbal","万向","ORIENTATION_GIMBAL",
        "CURVEOBJECT","CURVEEDIT","SURFACEOBJECT","SURFACEEDIT","METAOBJECT","METAEDIT","FONTOBJECT","FONTEDIT",
        "VOLUMEOBJECT","EMPTYOBJECT","LATTICEOBJECT","LATTICEEDIT","LIGHTOBJECT","LIGHT_PROBEOBJECT","CAMERAOBJECT",
        "SPEAKEROBJECT","MESHOBJECT","MESHEDIT","GPENCILOBJECT","GPENCILEDIT_GPENCIL","GREASEPENCILOBJECT",
        "GREASEPENCILEDIT","ARMATUREOBJECT","ARMATUREEDIT","ARMATUREPOSE",
    ),
        'button.action_orientation_to_view':(
        "button.action_orientation_to_view","视图","ORIENTATION_VIEW",
        "CURVEOBJECT","CURVEEDIT","SURFACEOBJECT","SURFACEEDIT","METAOBJECT","METAEDIT","FONTOBJECT","FONTEDIT",
        "VOLUMEOBJECT","EMPTYOBJECT","LATTICEOBJECT","LATTICEEDIT","LIGHTOBJECT","LIGHT_PROBEOBJECT","CAMERAOBJECT",
        "SPEAKEROBJECT","MESHOBJECT","MESHEDIT","GPENCILOBJECT","GPENCILEDIT_GPENCIL","GREASEPENCILOBJECT",
        "GREASEPENCILEDIT","ARMATUREOBJECT","ARMATUREEDIT","ARMATUREPOSE",
    ),
        'button.action_orientation_to_cursor':(
        "button.action_orientation_to_cursor","游标","ORIENTATION_CURSOR",
        "CURVEOBJECT","CURVEEDIT","SURFACEOBJECT","SURFACEEDIT","METAOBJECT","METAEDIT","FONTOBJECT","FONTEDIT",
        "VOLUMEOBJECT","EMPTYOBJECT","LATTICEOBJECT","LATTICEEDIT","LIGHTOBJECT","LIGHT_PROBEOBJECT","CAMERAOBJECT",
        "SPEAKEROBJECT","MESHOBJECT","MESHEDIT","GPENCILOBJECT","GPENCILEDIT_GPENCIL","GREASEPENCILOBJECT",
        "GREASEPENCILEDIT","ARMATUREOBJECT","ARMATUREEDIT","ARMATUREPOSE",
    ),
        'button.action_orientation_to_parent':(
        "button.action_orientation_to_parent","父级","ORIENTATION_PARENT",
        "CURVEOBJECT","CURVEEDIT","SURFACEOBJECT","SURFACEEDIT","METAOBJECT","METAEDIT","FONTOBJECT","FONTEDIT",
        "VOLUMEOBJECT","EMPTYOBJECT","LATTICEOBJECT","LATTICEEDIT","LIGHTOBJECT","LIGHT_PROBEOBJECT","CAMERAOBJECT",
        "SPEAKEROBJECT","MESHOBJECT","MESHEDIT","GPENCILOBJECT","GPENCILEDIT_GPENCIL","GREASEPENCILOBJECT",
        "GREASEPENCILEDIT","ARMATUREOBJECT","ARMATUREEDIT","ARMATUREPOSE",
    ),

    # 切换轴心点
        'button.action_switch_pivot_menu':(
        "button.action_switch_pivot_menu","切换轴心点","PRESET",
        "CURVEOBJECT","CURVEEDIT","SURFACEOBJECT","SURFACEEDIT","METAOBJECT","METAEDIT","FONTOBJECT","FONTEDIT",
        "VOLUMEOBJECT","EMPTYOBJECT","LATTICEOBJECT","LATTICEEDIT","LIGHTOBJECT","LIGHT_PROBEOBJECT","CAMERAOBJECT",
        "SPEAKEROBJECT","MESHOBJECT","MESHEDIT","GPENCILOBJECT","GPENCILEDIT_GPENCIL","GREASEPENCILOBJECT",
        "GREASEPENCILEDIT","ARMATUREOBJECT","ARMATUREEDIT","ARMATUREPOSE",
    ),
        'button.action_pivot_to_bounding_box_center':(
        "button.action_pivot_to_bounding_box_center","边界框中心","PIVOT_BOUNDBOX",
        "CURVEOBJECT","CURVEEDIT","SURFACEOBJECT","SURFACEEDIT","METAOBJECT","METAEDIT","FONTOBJECT","FONTEDIT",
        "VOLUMEOBJECT","EMPTYOBJECT","LATTICEOBJECT","LATTICEEDIT","LIGHTOBJECT","LIGHT_PROBEOBJECT","CAMERAOBJECT",
        "SPEAKEROBJECT","MESHOBJECT","MESHEDIT","GPENCILOBJECT","GPENCILEDIT_GPENCIL","GREASEPENCILOBJECT",
        "GREASEPENCILEDIT","ARMATUREOBJECT","ARMATUREEDIT","ARMATUREPOSE",
    ),
        'button.action_pivot_to_cursor':(
        "button.action_pivot_to_cursor","3D 游标","PIVOT_CURSOR",
        "CURVEOBJECT","CURVEEDIT","SURFACEOBJECT","SURFACEEDIT","METAOBJECT","METAEDIT","FONTOBJECT","FONTEDIT",
        "VOLUMEOBJECT","EMPTYOBJECT","LATTICEOBJECT","LATTICEEDIT","LIGHTOBJECT","LIGHT_PROBEOBJECT","CAMERAOBJECT",
        "SPEAKEROBJECT","MESHOBJECT","MESHEDIT","GPENCILOBJECT","GPENCILEDIT_GPENCIL","GREASEPENCILOBJECT",
        "GREASEPENCILEDIT","ARMATUREOBJECT","ARMATUREEDIT","ARMATUREPOSE",
    ),
        'button.action_pivot_to_individual_origins':(
        "button.action_pivot_to_individual_origins","各自的原点","PIVOT_INDIVIDUAL",
        "CURVEOBJECT","CURVEEDIT","SURFACEOBJECT","SURFACEEDIT","METAOBJECT","METAEDIT","FONTOBJECT","FONTEDIT",
        "VOLUMEOBJECT","EMPTYOBJECT","LATTICEOBJECT","LATTICEEDIT","LIGHTOBJECT","LIGHT_PROBEOBJECT","CAMERAOBJECT",
        "SPEAKEROBJECT","MESHOBJECT","MESHEDIT","GPENCILOBJECT","GPENCILEDIT_GPENCIL","GREASEPENCILOBJECT",
        "GREASEPENCILEDIT","ARMATUREOBJECT","ARMATUREEDIT","ARMATUREPOSE",
    ),
        'button.action_pivot_to_median_point':(
        "button.action_pivot_to_median_point","质心点","PIVOT_MEDIAN",
        "CURVEOBJECT","CURVEEDIT","SURFACEOBJECT","SURFACEEDIT","METAOBJECT","METAEDIT","FONTOBJECT","FONTEDIT",
        "VOLUMEOBJECT","EMPTYOBJECT","LATTICEOBJECT","LATTICEEDIT","LIGHTOBJECT","LIGHT_PROBEOBJECT","CAMERAOBJECT",
        "SPEAKEROBJECT","MESHOBJECT","MESHEDIT","GPENCILOBJECT","GPENCILEDIT_GPENCIL","GREASEPENCILOBJECT",
        "GREASEPENCILEDIT","ARMATUREOBJECT","ARMATUREEDIT","ARMATUREPOSE",
    ),
        'button.action_pivot_to_active_element':(
        "button.action_pivot_to_active_element","活动元素","PIVOT_ACTIVE",
        "CURVEOBJECT","CURVEEDIT","SURFACEOBJECT","SURFACEEDIT","METAOBJECT","METAEDIT","FONTOBJECT","FONTEDIT",
        "VOLUMEOBJECT","EMPTYOBJECT","LATTICEOBJECT","LATTICEEDIT","LIGHTOBJECT","LIGHT_PROBEOBJECT","CAMERAOBJECT",
        "SPEAKEROBJECT","MESHOBJECT","MESHEDIT","GPENCILOBJECT","GPENCILEDIT_GPENCIL","GREASEPENCILOBJECT",
        "GREASEPENCILEDIT","ARMATUREOBJECT","ARMATUREEDIT","ARMATUREPOSE",
    ),

    # 切换吸附
        'button.action_switch_snap_menu':(
        "button.action_switch_snap_menu","切换吸附","PRESET",
        "CURVEOBJECT","CURVEEDIT","SURFACEOBJECT","SURFACEEDIT","METAOBJECT","METAEDIT","FONTOBJECT","FONTEDIT",
        "VOLUMEOBJECT","EMPTYOBJECT","LATTICEOBJECT","LATTICEEDIT","LIGHTOBJECT","LIGHT_PROBEOBJECT","CAMERAOBJECT",
        "SPEAKEROBJECT","MESHOBJECT","MESHEDIT","GPENCILOBJECT","GPENCILEDIT_GPENCIL","GREASEPENCILOBJECT",
        "GREASEPENCILEDIT","ARMATUREOBJECT","ARMATUREEDIT","ARMATUREPOSE",
    ), 
        'button.action_switch_snap_toggle':(
        "button.action_switch_snap_toggle","开/关吸附","SNAP_ON",
        "CURVEOBJECT","CURVEEDIT","SURFACEOBJECT","SURFACEEDIT","METAOBJECT","METAEDIT","FONTOBJECT","FONTEDIT",
        "VOLUMEOBJECT","EMPTYOBJECT","LATTICEOBJECT","LATTICEEDIT","LIGHTOBJECT","LIGHT_PROBEOBJECT","CAMERAOBJECT",
        "SPEAKEROBJECT","MESHOBJECT","MESHEDIT","GPENCILOBJECT","GPENCILEDIT_GPENCIL","GREASEPENCILOBJECT",
        "GREASEPENCILEDIT","ARMATUREOBJECT","ARMATUREEDIT","ARMATUREPOSE",
    ),  
        'button.action_switch_snap_increment':(
        "button.action_switch_snap_increment","增量","SNAP_INCREMENT",
        "CURVEOBJECT","CURVEEDIT","SURFACEOBJECT","SURFACEEDIT","METAOBJECT","METAEDIT","FONTOBJECT","FONTEDIT",
        "VOLUMEOBJECT","EMPTYOBJECT","LATTICEOBJECT","LATTICEEDIT","LIGHTOBJECT","LIGHT_PROBEOBJECT","CAMERAOBJECT",
        "SPEAKEROBJECT","MESHOBJECT","MESHEDIT","GPENCILOBJECT","GPENCILEDIT_GPENCIL","GREASEPENCILOBJECT",
        "GREASEPENCILEDIT","ARMATUREOBJECT","ARMATUREEDIT","ARMATUREPOSE",
    ),    
        'button.action_switch_snap_vertex':(
        "button.action_switch_snap_vertex","顶点","SNAP_VERTEX",
        "CURVEOBJECT","CURVEEDIT","SURFACEOBJECT","SURFACEEDIT","METAOBJECT","METAEDIT","FONTOBJECT","FONTEDIT",
        "VOLUMEOBJECT","EMPTYOBJECT","LATTICEOBJECT","LATTICEEDIT","LIGHTOBJECT","LIGHT_PROBEOBJECT","CAMERAOBJECT",
        "SPEAKEROBJECT","MESHOBJECT","MESHEDIT","GPENCILOBJECT","GPENCILEDIT_GPENCIL","GREASEPENCILOBJECT",
        "GREASEPENCILEDIT","ARMATUREOBJECT","ARMATUREEDIT","ARMATUREPOSE",
    ),  
        'button.action_switch_snap_edge':(
        "button.action_switch_snap_edge","边","SNAP_EDGE",
        "CURVEOBJECT","CURVEEDIT","SURFACEOBJECT","SURFACEEDIT","METAOBJECT","METAEDIT","FONTOBJECT","FONTEDIT",
        "VOLUMEOBJECT","EMPTYOBJECT","LATTICEOBJECT","LATTICEEDIT","LIGHTOBJECT","LIGHT_PROBEOBJECT","CAMERAOBJECT",
        "SPEAKEROBJECT","MESHOBJECT","MESHEDIT","GPENCILOBJECT","GPENCILEDIT_GPENCIL","GREASEPENCILOBJECT",
        "GREASEPENCILEDIT","ARMATUREOBJECT","ARMATUREEDIT","ARMATUREPOSE",
    ),  
        'button.action_switch_snap_face':(
        "button.action_switch_snap_face","面投射","SNAP_FACE",
        "CURVEOBJECT","CURVEEDIT","SURFACEOBJECT","SURFACEEDIT","METAOBJECT","METAEDIT","FONTOBJECT","FONTEDIT",
        "VOLUMEOBJECT","EMPTYOBJECT","LATTICEOBJECT","LATTICEEDIT","LIGHTOBJECT","LIGHT_PROBEOBJECT","CAMERAOBJECT",
        "SPEAKEROBJECT","MESHOBJECT","MESHEDIT","GPENCILOBJECT","GPENCILEDIT_GPENCIL","GREASEPENCILOBJECT",
        "GREASEPENCILEDIT","ARMATUREOBJECT","ARMATUREEDIT","ARMATUREPOSE",
    ),
        'button.action_switch_snap_face_nearest':(
        "button.action_switch_snap_face_nearest","面最近","SNAP_FACE_NEAREST",
        "CURVEOBJECT","CURVEEDIT","SURFACEOBJECT","SURFACEEDIT","METAOBJECT","METAEDIT","FONTOBJECT","FONTEDIT",
        "VOLUMEOBJECT","EMPTYOBJECT","LATTICEOBJECT","LATTICEEDIT","LIGHTOBJECT","LIGHT_PROBEOBJECT","CAMERAOBJECT",
        "SPEAKEROBJECT","MESHOBJECT","MESHEDIT","GPENCILOBJECT","GPENCILEDIT_GPENCIL","GREASEPENCILOBJECT",
        "GREASEPENCILEDIT","ARMATUREOBJECT","ARMATUREEDIT","ARMATUREPOSE",
    ),
        'button.action_switch_snap_volume':(
        "button.action_switch_snap_volume","体积","SNAP_VOLUME",
        "CURVEOBJECT","CURVEEDIT","SURFACEOBJECT","SURFACEEDIT","METAOBJECT","METAEDIT","FONTOBJECT","FONTEDIT",
        "VOLUMEOBJECT","EMPTYOBJECT","LATTICEOBJECT","LATTICEEDIT","LIGHTOBJECT","LIGHT_PROBEOBJECT","CAMERAOBJECT",
        "SPEAKEROBJECT","MESHOBJECT","MESHEDIT","GPENCILOBJECT","GPENCILEDIT_GPENCIL","GREASEPENCILOBJECT",
        "GREASEPENCILEDIT","ARMATUREOBJECT","ARMATUREEDIT","ARMATUREPOSE",
    ),
        'button.action_switch_snap_edge_midpoint':(
        "button.action_switch_snap_edge_midpoint","边中点","SNAP_MIDPOINT",
        "CURVEOBJECT","CURVEEDIT","SURFACEOBJECT","SURFACEEDIT","METAOBJECT","METAEDIT","FONTOBJECT","FONTEDIT",
        "VOLUMEOBJECT","EMPTYOBJECT","LATTICEOBJECT","LATTICEEDIT","LIGHTOBJECT","LIGHT_PROBEOBJECT","CAMERAOBJECT",
        "SPEAKEROBJECT","MESHOBJECT","MESHEDIT","GPENCILOBJECT","GPENCILEDIT_GPENCIL","GREASEPENCILOBJECT",
        "GREASEPENCILEDIT","ARMATUREOBJECT","ARMATUREEDIT","ARMATUREPOSE",
    ),
        'button.action_switch_snap_edge_perpendicular':(
        "button.action_switch_snap_edge_perpendicular","垂直交线","SNAP_PERPENDICULAR",
        "CURVEOBJECT","CURVEEDIT","SURFACEOBJECT","SURFACEEDIT","METAOBJECT","METAEDIT","FONTOBJECT","FONTEDIT",
        "VOLUMEOBJECT","EMPTYOBJECT","LATTICEOBJECT","LATTICEEDIT","LIGHTOBJECT","LIGHT_PROBEOBJECT","CAMERAOBJECT",
        "SPEAKEROBJECT","MESHOBJECT","MESHEDIT","GPENCILOBJECT","GPENCILEDIT_GPENCIL","GREASEPENCILOBJECT",
        "GREASEPENCILEDIT","ARMATUREOBJECT","ARMATUREEDIT","ARMATUREPOSE",
    ),

    #切换衰减编辑
        'button.action_switch_proportional_menu':(
        "button.action_switch_proportional_menu","衰减编辑","PRESET",
        "CURVEOBJECT","CURVEEDIT","SURFACEOBJECT","SURFACEEDIT","METAOBJECT","METAEDIT","FONTOBJECT","FONTEDIT",
        "VOLUMEOBJECT","EMPTYOBJECT","LATTICEOBJECT","LATTICEEDIT","LIGHTOBJECT","LIGHT_PROBEOBJECT","CAMERAOBJECT",
        "SPEAKEROBJECT","MESHOBJECT","MESHEDIT","GPENCILOBJECT","GPENCILEDIT_GPENCIL","GREASEPENCILOBJECT",
        "GREASEPENCILEDIT","ARMATUREOBJECT","ARMATUREEDIT",
    ),
        'button.action_switch_proportional_toggle':(
        "button.action_switch_proportional_toggle","开/关衰减编辑","PROP_ON",
        "CURVEOBJECT","CURVEEDIT","SURFACEOBJECT","SURFACEEDIT","METAOBJECT","METAEDIT","FONTOBJECT","FONTEDIT",
        "VOLUMEOBJECT","EMPTYOBJECT","LATTICEOBJECT","LATTICEEDIT","LIGHTOBJECT","LIGHT_PROBEOBJECT","CAMERAOBJECT",
        "SPEAKEROBJECT","MESHOBJECT","MESHEDIT","GPENCILOBJECT","GPENCILEDIT_GPENCIL","GREASEPENCILOBJECT",
        "GREASEPENCILEDIT","ARMATUREOBJECT","ARMATUREEDIT",
    ),
        'button.action_switch_proportional_smooth':(
        "button.action_switch_proportional_smooth","平滑","SMOOTHCURVE",
        "CURVEOBJECT","CURVEEDIT","SURFACEOBJECT","SURFACEEDIT","METAOBJECT","METAEDIT","FONTOBJECT","FONTEDIT",
        "VOLUMEOBJECT","EMPTYOBJECT","LATTICEOBJECT","LATTICEEDIT","LIGHTOBJECT","LIGHT_PROBEOBJECT","CAMERAOBJECT",
        "SPEAKEROBJECT","MESHOBJECT","MESHEDIT","GPENCILOBJECT","GPENCILEDIT_GPENCIL","GREASEPENCILOBJECT",
        "GREASEPENCILEDIT","ARMATUREOBJECT","ARMATUREEDIT",
    ),
        'button.action_switch_proportional_sphere':(
        "button.action_switch_proportional_sphere","球体","SPHERECURVE",
        "CURVEOBJECT","CURVEEDIT","SURFACEOBJECT","SURFACEEDIT","METAOBJECT","METAEDIT","FONTOBJECT","FONTEDIT",
        "VOLUMEOBJECT","EMPTYOBJECT","LATTICEOBJECT","LATTICEEDIT","LIGHTOBJECT","LIGHT_PROBEOBJECT","CAMERAOBJECT",
        "SPEAKEROBJECT","MESHOBJECT","MESHEDIT","GPENCILOBJECT","GPENCILEDIT_GPENCIL","GREASEPENCILOBJECT",
        "GREASEPENCILEDIT","ARMATUREOBJECT","ARMATUREEDIT",
    ),
        'button.action_switch_proportional_root':(
        "button.action_switch_proportional_root","根凸","ROOTCURVE",
        "CURVEOBJECT","CURVEEDIT","SURFACEOBJECT","SURFACEEDIT","METAOBJECT","METAEDIT","FONTOBJECT","FONTEDIT",
        "VOLUMEOBJECT","EMPTYOBJECT","LATTICEOBJECT","LATTICEEDIT","LIGHTOBJECT","LIGHT_PROBEOBJECT","CAMERAOBJECT",
        "SPEAKEROBJECT","MESHOBJECT","MESHEDIT","GPENCILOBJECT","GPENCILEDIT_GPENCIL","GREASEPENCILOBJECT",
        "GREASEPENCILEDIT","ARMATUREOBJECT","ARMATUREEDIT",
    ),
        'button.action_switch_proportional_inverse_square':(
        "button.action_switch_proportional_inverse_square","平方反比","INVERSESQUARECURVE",
        "CURVEOBJECT","CURVEEDIT","SURFACEOBJECT","SURFACEEDIT","METAOBJECT","METAEDIT","FONTOBJECT","FONTEDIT",
        "VOLUMEOBJECT","EMPTYOBJECT","LATTICEOBJECT","LATTICEEDIT","LIGHTOBJECT","LIGHT_PROBEOBJECT","CAMERAOBJECT",
        "SPEAKEROBJECT","MESHOBJECT","MESHEDIT","GPENCILOBJECT","GPENCILEDIT_GPENCIL","GREASEPENCILOBJECT",
        "GREASEPENCILEDIT","ARMATUREOBJECT","ARMATUREEDIT",
    ),
        'button.action_switch_proportional_sharp':(
        "button.action_switch_proportional_sharp","锐利","SHARPCURVE",
        "CURVEOBJECT","CURVEEDIT","SURFACEOBJECT","SURFACEEDIT","METAOBJECT","METAEDIT","FONTOBJECT","FONTEDIT",
        "VOLUMEOBJECT","EMPTYOBJECT","LATTICEOBJECT","LATTICEEDIT","LIGHTOBJECT","LIGHT_PROBEOBJECT","CAMERAOBJECT",
        "SPEAKEROBJECT","MESHOBJECT","MESHEDIT","GPENCILOBJECT","GPENCILEDIT_GPENCIL","GREASEPENCILOBJECT",
        "GREASEPENCILEDIT","ARMATUREOBJECT","ARMATUREEDIT",
    ),
        'button.action_switch_proportional_linear':(
        "button.action_switch_proportional_linear","线性","LINCURVE",
        "CURVEOBJECT","CURVEEDIT","SURFACEOBJECT","SURFACEEDIT","METAOBJECT","METAEDIT","FONTOBJECT","FONTEDIT",
        "VOLUMEOBJECT","EMPTYOBJECT","LATTICEOBJECT","LATTICEEDIT","LIGHTOBJECT","LIGHT_PROBEOBJECT","CAMERAOBJECT",
        "SPEAKEROBJECT","MESHOBJECT","MESHEDIT","GPENCILOBJECT","GPENCILEDIT_GPENCIL","GREASEPENCILOBJECT",
        "GREASEPENCILEDIT","ARMATUREOBJECT","ARMATUREEDIT",
    ),
        'button.action_switch_proportional_constant':(
        "button.action_switch_proportional_constant","常值","NOCURVE",
        "CURVEOBJECT","CURVEEDIT","SURFACEOBJECT","SURFACEEDIT","METAOBJECT","METAEDIT","FONTOBJECT","FONTEDIT",
        "VOLUMEOBJECT","EMPTYOBJECT","LATTICEOBJECT","LATTICEEDIT","LIGHTOBJECT","LIGHT_PROBEOBJECT","CAMERAOBJECT",
        "SPEAKEROBJECT","MESHOBJECT","MESHEDIT","GPENCILOBJECT","GPENCILEDIT_GPENCIL","GREASEPENCILOBJECT",
        "GREASEPENCILEDIT","ARMATUREOBJECT","ARMATUREEDIT",
    ),
        'button.action_switch_proportional_random':(
        "button.action_switch_proportional_random","随机","RNDCURVE",
        "CURVEOBJECT","CURVEEDIT","SURFACEOBJECT","SURFACEEDIT","METAOBJECT","METAEDIT","FONTOBJECT","FONTEDIT",
        "VOLUMEOBJECT","EMPTYOBJECT","LATTICEOBJECT","LATTICEEDIT","LIGHTOBJECT","LIGHT_PROBEOBJECT","CAMERAOBJECT",
        "SPEAKEROBJECT","MESHOBJECT","MESHEDIT","GPENCILOBJECT","GPENCILEDIT_GPENCIL","GREASEPENCILOBJECT",
        "GREASEPENCILEDIT","ARMATUREOBJECT","ARMATUREEDIT",
    ),

    # 全局模式——“视图”菜单
        'button.action_view3d_view_selected':(
        "button.action_view3d_view_selected","框显所选","DOT","all",
    ),
        'button.action_view3d_view_all':(
        "button.action_view3d_view_all","框显全部","HOME","all",
    ),
        'button.action_view3d_localview':(
        "button.action_view3d_localview","局部视图","RADIOBUT_OFF","all",
    ),
        'view3d.localview_remove_from':(
        "view3d.localview_remove_from","从局部视图中移除","RADIOBUT_OFF","all",
    ),
        'button.action_view3d_object_as_camera':(
        "button.action_view3d_object_as_camera","设置活动物体为摄像机","OUTLINER_OB_CAMERA","all",
    ),
        'button.action_view3d_view_center_camera':(
        "button.action_view3d_view_center_camera","摄像机边界框","SELECT_SET","all",
    ),
        'button.action_view3d_call_view_viewpoint_menu':(
        "button.action_view3d_call_view_viewpoint_menu","视图","PRESET","all",
    ),
        'button.action_view3d_call_view_navigation_menu':(
        "button.action_view3d_call_view_navigation_menu","视图切换","PRESET","all",
    ),
        'button.action_view3d_zoom_border':(
        "button.action_view3d_zoom_border","框选放大","SELECT_SET","all",
    ),
        'button.action_zoom_camera_1_to_1':(
        "button.action_zoom_camera_1_to_1","1:1缩放摄像机视图","RADIOBUT_OFF","all",
    ),
        'button.action_view3d_fly':(
        "button.action_view3d_fly","飞行漫游模式","RADIOBUT_OFF","all",
    ),
        'button.action_view3d_walk':(
        "button.action_view3d_walk","行走漫步","RADIOBUT_OFF","all",
    ),
        'button.action_view3d_call_view_align_selected_menu':(
        "button.action_view3d_call_view_align_selected_menu","视图对齐活动项","PRESET","all",
    ),
        'button.action_view3d_call_view_align_menu':(
        "button.action_view3d_call_view_align_menu","对齐视图","PRESET","all",
    ),
        'button.action_view3d_view_all_center_true':(
        "button.action_view3d_view_all_center_true","游标居中并查看全部","CURSOR","all",
    ),
        'button.action_view3d_view_center_cursor':(
        "button.action_view3d_view_center_cursor","视图中心对齐游标","PIVOT_CURSOR","all",
    ),
        'button.action_view3d_camera_to_view':(
        "button.action_view3d_camera_to_view","活动摄像机对齐当前视角","OUTLINER_DATA_CAMERA","all",
    ),
        'button.action_view3d_camera_to_view_selected':(
        "button.action_view3d_camera_to_view_selected","活动摄像机对齐选中的物体","OUTLINER_OB_CAMERA","all",
    ),
        'button.action_view3d_lock_to_active_or_lock_clear':(
        "button.action_view3d_lock_to_active_or_lock_clear","锁定/解锁视图","CON_CAMERASOLVER","all",
    ),
        'button.action_view3d_call_view_regions_menu':(
        "button.action_view3d_call_view_regions_menu","视图框","PRESET","all",
    ),
        'button.action_view3d_clip_border':(
        "button.action_view3d_clip_border","裁剪框","CLIPUV_HLT","all",
    ),
        'button.action_view3d_render_border':(
        "button.action_view3d_render_border","开/关渲染框","RADIOBUT_OFF","all",
    ),
        'button.action_view3d_render_opengl':(
        "button.action_view3d_render_opengl","视图渲染图像","RENDER_STILL","all",
    ),
        'button.action_view3d_render_opengl_animation':(
        "button.action_view3d_render_opengl_animation","视图渲染动画","RENDER_ANIMATION","all",
    ),
        'button.action_view3d_render_opengl_keyframe':(
        "button.action_view3d_render_opengl_keyframe","视图渲染关键帧","RENDER_ANIMATION","all",
    ),
        'button.action_view3d_area_menu':(
        "button.action_view3d_area_menu","区域","PRESET","all",
    ),
        'screen.region_quadview':(
        "screen.region_quadview","四格视图","IMGDISPLAY","all",
    ),
        'screen.screen_full_area':(
        "screen.screen_full_area","区域最大化","MOD_LENGTH","all",
    ),
        'button.action_view3d_screen_screen_full_area':(
        "button.action_view3d_screen_screen_full_area","全屏模式","FULLSCREEN_ENTER","all",
    ),

    # “选择”菜单
        'button.action_call_select_select_by_type_menu':(
        "button.action_call_select_select_by_type_menu","按类型全选","PRESET",
        "CURVEOBJECT", "SURFACEOBJECT", "METAOBJECT", "FONTOBJECT", "VOLUMEOBJECT", "EMPTYOBJECT", "LATTICEOBJECT", 
        "LIGHTOBJECT", "LIGHT_PROBEOBJECT", "CAMERAOBJECT", "SPEAKEROBJECT", "MESHOBJECT",
        "GPENCILOBJECT", "GREASEPENCILOBJECT", "ARMATUREOBJECT",
    ),
        'object.select_camera':(
        "object.select_camera","选择活动摄像机","OUTLINER_OB_CAMERA",
        "CURVEOBJECT", "SURFACEOBJECT", "METAOBJECT", "FONTOBJECT", "VOLUMEOBJECT", "EMPTYOBJECT", "LATTICEOBJECT", 
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
        "CURVEOBJECT", "SURFACEOBJECT", "METAOBJECT", "FONTOBJECT", "VOLUMEOBJECT", "EMPTYOBJECT", "LATTICEOBJECT", 
        "LATTICEEDIT", "LIGHTOBJECT", "LIGHT_PROBEOBJECT", "CAMERAOBJECT", "SPEAKEROBJECT", "MESHOBJECT",
        "MESHEDIT", "GPENCILOBJECT", "GREASEPENCILOBJECT", "ARMATUREOBJECT", "CURVEEDIT", "SURFACEEDIT",
        "METAEDIT", "GPENCILEDIT_GPENCIL", "GREASEPENCILEDIT", "LATTICEEDIT",
    ),
        'button.action_call_object_select_more_or_less_menu':(
        "button.action_call_object_select_more_or_less_menu","加选/减选","FORCE_CHARGE",
        "CURVEOBJECT", "CURVEEDIT", "SURFACEOBJECT", "SURFACEEDIT",  "METAOBJECT",
        "FONTOBJECT", "VOLUMEOBJECT", "EMPTYOBJECT", "LATTICEOBJECT", "LATTICEEDIT",
        "LIGHTOBJECT", "LIGHT_PROBEOBJECT", "CAMERAOBJECT", "SPEAKEROBJECT", "MESHOBJECT",
        "MESHEDIT", "GPENCILOBJECT", "GREASEPENCILOBJECT", "ARMATUREOBJECT", "ARMATUREEDIT", 
        "GPENCILEDIT_GPENCIL", "GREASEPENCILEDIT",
    ),
        'button.action_object_select_hierarchy_parent_child':(
        "button.action_object_select_hierarchy_parent_child","父级/子级","ORIENTATION_PARENT",
        "CURVEOBJECT", "SURFACEOBJECT", "METAOBJECT",
        "FONTOBJECT", "VOLUMEOBJECT", "EMPTYOBJECT", "LATTICEOBJECT", 
        "LIGHTOBJECT", "LIGHT_PROBEOBJECT", "CAMERAOBJECT", "SPEAKEROBJECT", "MESHOBJECT",
        "GPENCILOBJECT", "GREASEPENCILOBJECT","ARMATUREOBJECT", "ARMATUREEDIT","ARMATUREPOSE",
    ),
        'button.action_select_select_grouped':(
        "button.action_select_select_grouped","按组选择","PRESET",
        "CURVEOBJECT", "SURFACEOBJECT", "METAOBJECT", "GPENCILEDIT_GPENCIL",
        "FONTOBJECT", "VOLUMEOBJECT", "EMPTYOBJECT", "LATTICEOBJECT", "ARMATUREPOSE",
        "LIGHTOBJECT", "LIGHT_PROBEOBJECT", "CAMERAOBJECT", "SPEAKEROBJECT", 
        "MESHOBJECT","GPENCILOBJECT", "GREASEPENCILOBJECT","ARMATUREOBJECT", 
    ),
        'button.action_select_select_linked':(
        "button.action_select_select_linked","选择相连","LINK_BLEND", "ARMATUREPOSE",
        "CURVEOBJECT", "SURFACEOBJECT", "METAOBJECT", "GPENCILEDIT_GPENCIL",
        "FONTOBJECT", "VOLUMEOBJECT", "EMPTYOBJECT", "LATTICEOBJECT", "ARMATUREPOSE",
        "LIGHTOBJECT", "LIGHT_PROBEOBJECT", "CAMERAOBJECT", "SPEAKEROBJECT", 
        "MESHOBJECT","GPENCILOBJECT", "GREASEPENCILOBJECT","ARMATUREOBJECT", "GREASEPENCILEDIT",
        "GPENCILEDIT_GPENCIL", "CURVEEDIT", "SURFACEEDIT", "MESHEDIT", "ARMATUREEDIT",
    ),
    # 一些通用操作
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

    # 物体模式——“物体”菜单
        'button.action_object_object_duplicate_move_linked':(
        "button.action_object_object_duplicate_move_linked","关联复制","DUPLICATE", "CURVEOBJECT", "SURFACEOBJECT",
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
