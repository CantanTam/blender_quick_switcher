
button_press_global = {
    # 全局模式——“视图”菜单,所有操作模式当中都适用
        'button.action_global_view_selected':(
        "button.action_global_view_selected","框显所选","DOT","all",
    ),
        'button.action_global_view_all':(
        "button.action_global_view_all","框显全部","HOME","all",
    ),
        'button.action_global_localview':(
        "button.action_global_localview","局部视图","RADIOBUT_OFF","all",
    ),
        'view3d.localview_remove_from':(
        "view3d.localview_remove_from","从局部视图中移除","RADIOBUT_OFF","all",
    ),
        'button.action_global_object_as_camera':(
        "button.action_global_object_as_camera","设置活动物体为摄像机","OUTLINER_OB_CAMERA","all",
    ),
        'button.action_global_view_center_camera':(
        "button.action_global_view_center_camera","摄像机边界框","SELECT_SET","all",
    ),
        'button.action_global_call_view_viewpoint_menu':(
        "button.action_global_call_view_viewpoint_menu","视图","PRESET","all",
    ),
        'button.action_global_call_view_navigation_menu':(
        "button.action_global_call_view_navigation_menu","视图切换","PRESET","all",
    ),
        'button.action_global_zoom_border':(
        "button.action_global_zoom_border","框选放大","SELECT_SET","all",
    ),
        'button.action_zoom_camera_1_to_1':(
        "button.action_zoom_camera_1_to_1","1:1缩放摄像机视图","RADIOBUT_OFF","all",
    ),
        'button.action_global_fly':(
        "button.action_global_fly","飞行漫游模式","RADIOBUT_OFF","all",
    ),
        'button.action_global_walk':(
        "button.action_global_walk","行走漫步","RADIOBUT_OFF","all",
    ),
        'button.action_global_call_view_align_selected_menu':(
        "button.action_global_call_view_align_selected_menu","视图对齐活动项","PRESET","all",
    ),
        'button.action_global_call_view_align_menu':(
        "button.action_global_call_view_align_menu","对齐视图","PRESET","all",
    ),
        'button.action_global_view_all_center_true':(
        "button.action_global_view_all_center_true","游标居中并查看全部","CURSOR","all",
    ),
        'button.action_global_view_center_cursor':(
        "button.action_global_view_center_cursor","视图中心对齐游标","PIVOT_CURSOR","all",
    ),
        'button.action_global_camera_to_view':(
        "button.action_global_camera_to_view","活动摄像机对齐当前视角","OUTLINER_DATA_CAMERA","all",
    ),
        'button.action_global_camera_to_view_selected':(
        "button.action_global_camera_to_view_selected","活动摄像机对齐选中的物体","OUTLINER_OB_CAMERA","all",
    ),
        'button.action_global_lock_to_active_or_lock_clear':(
        "button.action_global_lock_to_active_or_lock_clear","锁定/解锁视图","CON_CAMERASOLVER","all",
    ),
        'button.action_global_call_view_regions_menu':(
        "button.action_global_call_view_regions_menu","视图框","PRESET","all",
    ),
        'button.action_global_clip_border':(
        "button.action_global_clip_border","裁剪框","CLIPUV_HLT","all",
    ),
        'button.action_global_render_border':(
        "button.action_global_render_border","开/关渲染框","RADIOBUT_OFF","all",
    ),
        'button.action_global_render_opengl':(
        "button.action_global_render_opengl","视图渲染图像","RENDER_STILL","all",
    ),
        'button.action_global_render_opengl_animation':(
        "button.action_global_render_opengl_animation","视图渲染动画","RENDER_ANIMATION","all",
    ),
        'button.action_global_render_opengl_keyframe':(
        "button.action_global_render_opengl_keyframe","视图渲染关键帧","RENDER_ANIMATION","all",
    ),
        'button.action_global_area_menu':(
        "button.action_global_area_menu","区域","PRESET","all",
    ),
        'screen.region_quadview':(
        "screen.region_quadview","四格视图","IMGDISPLAY","all",
    ),
        'screen.screen_full_area':(
        "screen.screen_full_area","区域最大化","MOD_LENGTH","all",
    ),
        'button.action_global_screen_screen_full_area':(
        "button.action_global_screen_screen_full_area","全屏模式","FULLSCREEN_ENTER","all",
    ),

    # 全局高频操作-移动/缩放/旋转-G/S/R
        'button.action_global_grab':(
        "button.action_global_grab","移动","EVENT_G",
    ),
        'button.action_global_scale':(
        "button.action_global_scale","缩放","EVENT_S",
    ),
        'button.action_global_rotate':(
        "button.action_global_rotate","旋转","EVENT_R",
    ),

    # 全局高频操作—全选/反选/刷选
        'button.action_global_select_all':(
        "button.action_global_select_all","全选","EVENT_A",
    ),
        'button.action_global_select_invert':(
        "button.action_global_select_invert","反选","RADIOBUT_OFF",
    ),
        'button.action_global_select_circle':(
        "button.action_global_select_circle","刷选","EVENT_C",
    ),

    # “选择”菜单
        'button.action_global_select_select_mirror':(
        "button.action_global_select_select_mirror","选择镜像","MOD_MIRROR",
    ),
        'button.action_global_select_select_random':(
        "button.action_global_select_select_random","随机选择","RADIOBUT_OFF",
    ),
        'button.action_call_global_select_more_or_less_menu':(
        "button.action_call_global_select_more_or_less_menu","加选/减选","FORCE_CHARGE",
    ),
        'button.action_global_select_select_parent_or_child':(
        "button.action_global_select_select_parent_or_child","父级/子级","ORIENTATION_PARENT",
    ),
        'button.action_select_select_grouped':(
        "button.action_select_select_grouped","按组选择","PRESET",
    ),
        'button.action_global_select_select_linked':(
        "button.action_global_select_select_linked","选择相连","LINK_BLEND",
    ),

    # 全局高频操作——“添加”菜单/“复制(Shift+D)”/“复制(Ctrl C)”/“粘贴(Ctrl V)”
        'button.action_global_add':(
        "button.action_global_add","添加","PRESET",
    ),
        'button.action_global_duplicate_move':(
        "button.action_global_duplicate_move","复制","DUPLICATE", 
    ),
        'button.action_global_copy':(
        "button.action_global_copy","复制","COPYDOWN",
    ),
        'button.action_global_paste':(
        "button.action_global_paste","粘贴","PASTEDOWN",
    ),
        'button.action_global_call_delete_menu':(
        "button.action_global_call_delete_menu","删除","EVENT_X",
    ),

    # 全局高频操作——“隐藏”/“隐藏未选项”/“显示隐藏项”
        'button.action_global_hide_view_set':(
        "button.action_global_hide_view_set","隐藏","EVENT_H",
    ),
        'button.action_global_hide_view_clear':(
        "button.action_global_hide_view_clear","显示隐藏项","HIDE_OFF",
    ),
        'button.action_global_apply':(
        "button.action_global_apply","应用","PRESET",
    ),
        'button.action_global_transform_mirror':( #“交互镜像”
        "button.action_global_transform_mirror","交互镜像","MOD_MIRROR",
    ),
        'button.action_global_object_pose_clear':( # 清空变换(菜单)
        "button.action_global_object_pose_clear","清空变换","PRESET",
    ),

        # 切换坐标系
        'button.action_switch_orientation_menu':(
        "button.action_switch_orientation_menu","切换坐标系","PRESET",
    ),
        'button.action_orientation_to_global':(
        "button.action_orientation_to_global","全局","ORIENTATION_GLOBAL",
    ),
        'button.action_orientation_to_local':(
        "button.action_orientation_to_local","局部","ORIENTATION_LOCAL",
    ),
        'button.action_orientation_to_normal':(
        "button.action_orientation_to_normal","法向","ORIENTATION_NORMAL",
    ),
        'button.action_orientation_to_gimbal':(
        "button.action_orientation_to_gimbal","万向","ORIENTATION_GIMBAL",
    ),
        'button.action_orientation_to_view':(
        "button.action_orientation_to_view","视图","ORIENTATION_VIEW",
    ),
        'button.action_orientation_to_cursor':(
        "button.action_orientation_to_cursor","游标","ORIENTATION_CURSOR",
    ),
        'button.action_orientation_to_parent':(
        "button.action_orientation_to_parent","父级","ORIENTATION_PARENT",
    ),

    # 切换轴心点
        'button.action_switch_pivot_menu':(
        "button.action_switch_pivot_menu","切换轴心点","PRESET",
    ),
        'button.action_pivot_to_bounding_box_center':(
        "button.action_pivot_to_bounding_box_center","边界框中心","PIVOT_BOUNDBOX",
    ),
        'button.action_pivot_to_cursor':(
        "button.action_pivot_to_cursor","3D 游标","PIVOT_CURSOR",
    ),
        'button.action_pivot_to_individual_origins':(
        "button.action_pivot_to_individual_origins","各自的原点","PIVOT_INDIVIDUAL",
    ),
        'button.action_pivot_to_median_point':(
        "button.action_pivot_to_median_point","质心点","PIVOT_MEDIAN",
    ),
        'button.action_pivot_to_active_element':(
        "button.action_pivot_to_active_element","活动元素","PIVOT_ACTIVE",
    ),

    # 切换吸附
        'button.action_switch_snap_menu':(
        "button.action_switch_snap_menu","切换吸附","PRESET",
    ), 
        'button.action_switch_snap_toggle':(
        "button.action_switch_snap_toggle","开/关吸附","SNAP_ON",
    ),  
        'button.action_switch_snap_increment':(
        "button.action_switch_snap_increment","增量","SNAP_INCREMENT",
    ),    
        'button.action_switch_snap_vertex':(
        "button.action_switch_snap_vertex","顶点","SNAP_VERTEX",
    ),  
        'button.action_switch_snap_edge':(
        "button.action_switch_snap_edge","边","SNAP_EDGE",
    ),  
        'button.action_switch_snap_face':(
        "button.action_switch_snap_face","面投射","SNAP_FACE",
    ),
        'button.action_switch_snap_face_nearest':(
        "button.action_switch_snap_face_nearest","面最近","SNAP_FACE_NEAREST",
    ),
        'button.action_switch_snap_volume':(
        "button.action_switch_snap_volume","体积","SNAP_VOLUME",
    ),
        'button.action_switch_snap_edge_midpoint':(
        "button.action_switch_snap_edge_midpoint","边中点","SNAP_MIDPOINT",
    ),
        'button.action_switch_snap_edge_perpendicular':(
        "button.action_switch_snap_edge_perpendicular","垂直交线","SNAP_PERPENDICULAR",
    ),

    #切换衰减编辑
        'button.action_switch_proportional_menu':(
        "button.action_switch_proportional_menu","衰减编辑","PRESET",
    ),
        'button.action_switch_proportional_toggle':(
        "button.action_switch_proportional_toggle","开/关衰减编辑","PROP_ON",
    ),
        'button.action_switch_proportional_smooth':(
        "button.action_switch_proportional_smooth","平滑","SMOOTHCURVE",
    ),
        'button.action_switch_proportional_sphere':(
        "button.action_switch_proportional_sphere","球体","SPHERECURVE",
    ),
        'button.action_switch_proportional_root':(
        "button.action_switch_proportional_root","根凸","ROOTCURVE",
    ),
        'button.action_switch_proportional_inverse_square':(
        "button.action_switch_proportional_inverse_square","平方反比","INVERSESQUARECURVE",
    ),
        'button.action_switch_proportional_sharp':(
        "button.action_switch_proportional_sharp","锐利","SHARPCURVE",
    ),
        'button.action_switch_proportional_linear':(
        "button.action_switch_proportional_linear","线性","LINCURVE",
    ),
        'button.action_switch_proportional_constant':(
        "button.action_switch_proportional_constant","常值","NOCURVE",
    ),
        'button.action_switch_proportional_random':(
        "button.action_switch_proportional_random","随机","RNDCURVE",
    ),

    #MESHEDIT 的选择菜单
        'button.action_mesh_select_nth':(
        "button.action_mesh_select_nth","间隔式弃选","RADIOBUT_OFF", "MESHEDIT",
    ),
        'button.action_mesh_edges_select_sharp':(
        "button.action_mesh_edges_select_sharp","选择锐边","RADIOBUT_OFF", "MESHEDIT",
    ),
        'button.action_select_select_similar':(
        "button.action_select_select_similar","选择相似","PRESET", 
        "MESHEDIT", "CURVEEDIT", "SURFACEEDIT", "ARMATUREEDIT", "METAEDIT",
    ),
        'button.action_mesh_call_select_by_trait':(
        "button.action_mesh_call_select_by_trait","按特征全选","PRESET", "MESHEDIT",
    ),
        'button.action_call_mesh_select_loops':(
        "button.action_call_mesh_select_loops","选择循环","PRESET", "MESHEDIT",
    ),
        'button.action_mesh_select_axis':(
        "button.action_mesh_select_axis","活动项的同侧","RADIOBUT_OFF", "MESHEDIT",
    ),

    # 一些通用操作
        'button.action_transform_tosphere':(
        "button.action_transform_tosphere","球形化","RADIOBUT_OFF",
    ),
        'button.action_transform_shear':(
        "button.action_transform_shear","切变","RADIOBUT_OFF", 
    ),
        'button.action_transform_bend':(
        "button.action_transform_bend","弯曲","RADIOBUT_OFF", 
    ),

    # 物体模式——“物体”菜单
        'button.action_object_object_duplicate_move_linked':(
        "button.action_object_object_duplicate_move_linked","关联复制","DUPLICATE",
    ),
        'object.join':(
        "object.join","合并","RADIOBUT_OFF", "MESHOBJECT",
    ),
        'button.action_object_object_transform_transform_mode_align':(
        "button.action_object_object_transform_transform_mode_align","对齐到变换坐标系","RADIOBUT_OFF", 
    ),
        'object.randomize_transform':(
        "object.randomize_transform","随机变换","RADIOBUT_OFF", 
    ),
        'object.align':(
        "object.align","对齐物体","RADIOBUT_OFF",
    ),


        'SEPARATOR':("","","REMOVE"),
        'NO_BUTTON':(),
}
