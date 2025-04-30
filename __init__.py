import bpy

bl_info = {
    "name": "AA_切换",
    "author": "Your Name",
    "version": (1, 1),
    "blender": (3, 6, 0),
    "location": "View3D",
    "description": "增强模式切换功能（带安全检查）",
    "category": "3D View"
}

from .operators import CSAWHEEL_OT_ModeSwitchOperator
from .preference import QuickSwitchAddonPreferences
from .operator_mode_switch_normal_uptodown import MODE_NORMAL_UPDOWN_OT_Switch
from .operator_mode_switch_normal_downtoup import MODE_NORMAL_DOWNUP_OT_Switch
from .operator_vertex_edge_face_switch import VERTEX_EDGE_FACE_OT_Switch
from .operator_mode_switch_menu_downtoup import MODE_MENU_OT_Switch
from .operator_mode_switch_tab import MODE_TAB_OT_Switch
from .popup_quick_menu_one import QUICK_POPUP_MENU_OT_one
from .popup_quick_menu_two import QUICK_POPUP_MENU_OT_two
from .call_popup_quick_menus import CALLOUT_QUICK_MENU_OT_one
from .call_popup_quick_menus import CALLOUT_QUICK_MENU_OT_two
from .operator_typeandmode_name_mode import register_mode_handler
from .operator_typeandmode_name_mode import unregister_mode_handler
from . import keymap

# 所有按钮操作符的导入：
from .quick_menu_button_functions.button_actions_global_functions import (
    BUTTON_ACTION_OT_grab,
    BUTTON_ACTION_OT_scale,
    BUTTON_ACTION_OT_rotate,
    BUTTON_ACTION_OT_global_select_all,
    BUTTON_ACTION_OT_global_select_invert,
    BUTTON_ACTION_OT_global_select_circle,
    BUTTON_ACTION_OT_global_duplicate_move,
    BUTTON_ACTION_OT_global_add,
)

from .quick_menu_button_functions.button_actions_global_switch_orientation_slots import (
    BUTTON_ACTION_OT_orientation_to_global,
    BUTTON_ACTION_OT_orientation_to_local,
    BUTTON_ACTION_OT_orientation_to_normal,
    BUTTON_ACTION_OT_orientation_to_gimbal,
    BUTTON_ACTION_OT_orientation_to_view,
    BUTTON_ACTION_OT_orientation_to_cursor,
    BUTTON_ACTION_OT_orientation_to_parent,
)
# 切换轴心点
from .quick_menu_button_functions.button_actions_global_switch_pivot_points import (
    BUTTON_ACTION_OT_pivot_to_bounding_box_center,
    BUTTON_ACTION_OT_pivot_to_cursor,
    BUTTON_ACTION_OT_pivot_to_individual_origins,
    BUTTON_ACTION_OT_pivot_to_median_point,
    BUTTON_ACTION_OT_pivot_to_active_element,
)
# “视图”菜单
from .quick_menu_button_functions.button_actions_global_view_menu import (
    BUTTON_ACTION_OT_view_selected_use_all_regions_false,
    BUTTON_ACTION_OT_view_all_center_false,
    BUTTON_ACTION_OT_view_persportho,
    BUTTON_ACTION_OT_view3d_localview,
    BUTTON_ACTION_OT_view3d_localview_remove_from,
    BUTTON_ACTION_OT_view3d_object_as_camera,
    BUTTON_ACTION_OT_view3d_view_camera,
    BUTTON_ACTION_OT_view3d_view_center_camera,
    VIEW3D_MT_view_axis_menu,
    BUTTON_ACTION_OT_view3d_call_menu_view_axis,
    VIEW3D_MT_view_switch_axis_menu,
    BUTTON_ACTION_OT_view3d_call_menu_view_switch_axis,
    BUTTON_ACTION_OT_view3d_zoom_border,
    BUTTON_ACTION_OT_view_pan_left,
    BUTTON_ACTION_OT_view_pan_right,
    BUTTON_ACTION_OT_view_pan_up,
    BUTTON_ACTION_OT_view_pan_down,
    BUTTON_ACTION_OT_view3d_fly,
    BUTTON_ACTION_OT_view3d_walk,
    VIEW3D_MT_view_align_menu,
    BUTTON_ACTION_OT_view3d_call_menu_view_align,
    VIEW3D_MT_view_regions_menu,
    BUTTON_ACTION_OT_view3d_call_menu_view_regions,
    BUTTON_ACTION_OT_view3d_clip_border,
    BUTTON_ACTION_OT_view3d_render_border,
    BUTTON_ACTION_OT_view3d_lock_to_active_or_lock_clear,
)

from .quick_menu_button_functions.button_actions_global_select_menu import (
    BUTTON_ACTION_OT_select_select_mirror,
    VIEW3D_MT_select_select_by_type_menu,
    BUTTON_ACTION_OT_view3d_call_select_select_by_type_menu,
    BUTTON_ACTION_OT_select_select_random,
    VIEW3D_MT_object_select_more_or_less_menu,
    BUTTON_ACTION_OT_call_object_select_more_or_less_menu,
    BUTTON_ACTION_OT_object_select_more,
    BUTTON_ACTION_OT_object_select_less,
    BUTTON_ACTION_OT_object_select_hierarchy_parent_child,
    VIEW3D_MT_select_select_grouped_menu,
    BUTTON_ACTION_OT_call_select_select_grouped_menu,
    VIEW3D_MT_select_select_linked_menu,
    BUTTON_ACTION_OT_call_select_select_linked_menu,
)

from .quick_menu_button_functions.button_actions_common_functions import (
    VIEW3D_MT_common_function_transform_menu,
    BUTTON_ACTION_OT_call_common_function_transform_menu,
    BUTTON_ACTION_OT_transform_tosphere,
    BUTTON_ACTION_OT_transform_shear,
    BUTTON_ACTION_OT_transform_bend,
    BUTTON_ACTION_OT_transform_push_pull,
    BUTTON_ACTION_OT_transform_translate_texturespace_true,
    BUTTON_ACTION_OT_transform_resize_texturespace_true,
    BUTTON_ACTION_OT_transform_vertex_random,
)

from .quick_menu_button_functions.button_actions_object_mode_menu import (
    BUTTON_ACTION_OT_object_object_transform_transform_mode_align,
)

from .quick_menu_button_functions.button_actions_armature import (
    BUTTON_ACTION_OT_armature_bone_primitive_add,
)

def register():    
    # 注册模式监测功能
    register_mode_handler()

    
    # 注册所有Operator类
    bpy.utils.register_class(CSAWHEEL_OT_ModeSwitchOperator)
    bpy.utils.register_class(QuickSwitchAddonPreferences)
    bpy.utils.register_class(MODE_NORMAL_UPDOWN_OT_Switch)
    bpy.utils.register_class(MODE_NORMAL_DOWNUP_OT_Switch)
    bpy.utils.register_class(VERTEX_EDGE_FACE_OT_Switch)
    bpy.utils.register_class(MODE_MENU_OT_Switch)
    bpy.utils.register_class(MODE_TAB_OT_Switch)
    bpy.utils.register_class(QUICK_POPUP_MENU_OT_one)
    bpy.utils.register_class(QUICK_POPUP_MENU_OT_two)
    bpy.utils.register_class(CALLOUT_QUICK_MENU_OT_one)
    bpy.utils.register_class(CALLOUT_QUICK_MENU_OT_two)

    # 全局高频操作类
    bpy.utils.register_class(BUTTON_ACTION_OT_grab)
    bpy.utils.register_class(BUTTON_ACTION_OT_scale)
    bpy.utils.register_class(BUTTON_ACTION_OT_rotate)
    bpy.utils.register_class(BUTTON_ACTION_OT_global_select_all)
    bpy.utils.register_class(BUTTON_ACTION_OT_global_select_invert)
    bpy.utils.register_class(BUTTON_ACTION_OT_global_select_circle)
    bpy.utils.register_class(BUTTON_ACTION_OT_global_duplicate_move)
    bpy.utils.register_class(BUTTON_ACTION_OT_global_add)

    # 变换坐标系类
    bpy.utils.register_class(BUTTON_ACTION_OT_orientation_to_global)
    bpy.utils.register_class(BUTTON_ACTION_OT_orientation_to_local)
    bpy.utils.register_class(BUTTON_ACTION_OT_orientation_to_normal)
    bpy.utils.register_class(BUTTON_ACTION_OT_orientation_to_gimbal)
    bpy.utils.register_class(BUTTON_ACTION_OT_orientation_to_view)
    bpy.utils.register_class(BUTTON_ACTION_OT_orientation_to_cursor)
    bpy.utils.register_class(BUTTON_ACTION_OT_orientation_to_parent)

    # 切换轴心点
    bpy.utils.register_class(BUTTON_ACTION_OT_pivot_to_bounding_box_center)
    bpy.utils.register_class(BUTTON_ACTION_OT_pivot_to_cursor)
    bpy.utils.register_class(BUTTON_ACTION_OT_pivot_to_individual_origins)
    bpy.utils.register_class(BUTTON_ACTION_OT_pivot_to_median_point)
    bpy.utils.register_class(BUTTON_ACTION_OT_pivot_to_active_element)

    # "视图"菜单功能项
    bpy.utils.register_class(BUTTON_ACTION_OT_view_selected_use_all_regions_false)
    bpy.utils.register_class(BUTTON_ACTION_OT_view_all_center_false)
    bpy.utils.register_class(BUTTON_ACTION_OT_view_persportho)
    bpy.utils.register_class(BUTTON_ACTION_OT_view3d_localview)
    bpy.utils.register_class(BUTTON_ACTION_OT_view3d_localview_remove_from)
    bpy.utils.register_class(BUTTON_ACTION_OT_view3d_object_as_camera)
    bpy.utils.register_class(BUTTON_ACTION_OT_view3d_view_camera)
    bpy.utils.register_class(BUTTON_ACTION_OT_view3d_view_center_camera)
    bpy.utils.register_class(VIEW3D_MT_view_axis_menu)
    bpy.utils.register_class(BUTTON_ACTION_OT_view3d_call_menu_view_axis)
    bpy.utils.register_class(VIEW3D_MT_view_switch_axis_menu)
    bpy.utils.register_class(BUTTON_ACTION_OT_view3d_call_menu_view_switch_axis)
    bpy.utils.register_class(BUTTON_ACTION_OT_view3d_zoom_border)
    bpy.utils.register_class(BUTTON_ACTION_OT_view_pan_left)
    bpy.utils.register_class(BUTTON_ACTION_OT_view_pan_right)
    bpy.utils.register_class(BUTTON_ACTION_OT_view_pan_up)
    bpy.utils.register_class(BUTTON_ACTION_OT_view_pan_down)
    bpy.utils.register_class(BUTTON_ACTION_OT_view3d_fly)
    bpy.utils.register_class(BUTTON_ACTION_OT_view3d_walk)
    bpy.utils.register_class(VIEW3D_MT_view_align_menu)
    bpy.utils.register_class(BUTTON_ACTION_OT_view3d_call_menu_view_align)
    bpy.utils.register_class(VIEW3D_MT_view_regions_menu)
    bpy.utils.register_class(BUTTON_ACTION_OT_view3d_call_menu_view_regions)
    bpy.utils.register_class(BUTTON_ACTION_OT_view3d_clip_border)
    bpy.utils.register_class(BUTTON_ACTION_OT_view3d_render_border)
    bpy.utils.register_class(BUTTON_ACTION_OT_view3d_lock_to_active_or_lock_clear)
    
    # “选择”菜单功能项
    bpy.utils.register_class(BUTTON_ACTION_OT_select_select_mirror)
    bpy.utils.register_class(VIEW3D_MT_select_select_by_type_menu)
    bpy.utils.register_class(BUTTON_ACTION_OT_view3d_call_select_select_by_type_menu)
    bpy.utils.register_class(BUTTON_ACTION_OT_select_select_random)
    bpy.utils.register_class(VIEW3D_MT_object_select_more_or_less_menu)
    bpy.utils.register_class(BUTTON_ACTION_OT_call_object_select_more_or_less_menu)
    bpy.utils.register_class(BUTTON_ACTION_OT_object_select_more)
    bpy.utils.register_class(BUTTON_ACTION_OT_object_select_less)
    bpy.utils.register_class(BUTTON_ACTION_OT_object_select_hierarchy_parent_child)
    bpy.utils.register_class(VIEW3D_MT_select_select_grouped_menu)
    bpy.utils.register_class(BUTTON_ACTION_OT_call_select_select_grouped_menu)
    bpy.utils.register_class(VIEW3D_MT_select_select_linked_menu)
    bpy.utils.register_class(BUTTON_ACTION_OT_call_select_select_linked_menu)

    # 全局通用功能
    bpy.utils.register_class(VIEW3D_MT_common_function_transform_menu)
    bpy.utils.register_class(BUTTON_ACTION_OT_call_common_function_transform_menu)
    bpy.utils.register_class(BUTTON_ACTION_OT_transform_tosphere)
    bpy.utils.register_class(BUTTON_ACTION_OT_transform_shear)
    bpy.utils.register_class(BUTTON_ACTION_OT_transform_bend)
    bpy.utils.register_class(BUTTON_ACTION_OT_transform_push_pull)
    bpy.utils.register_class(BUTTON_ACTION_OT_transform_translate_texturespace_true)
    bpy.utils.register_class(BUTTON_ACTION_OT_transform_resize_texturespace_true)
    bpy.utils.register_class(BUTTON_ACTION_OT_transform_vertex_random)

    # 物体模式—“物体”菜单
    bpy.utils.register_class(BUTTON_ACTION_OT_object_object_transform_transform_mode_align)

    # "骨架"模式相关功能
    bpy.utils.register_class(BUTTON_ACTION_OT_armature_bone_primitive_add)

    # 注册键位映射
    keymap.register()

def unregister():    
    # 注销模式监测功能
    unregister_mode_handler()

    # ”骨架“模式相关功能
    bpy.utils.unregister_class(BUTTON_ACTION_OT_armature_bone_primitive_add)

    # 物体模式—“物体”菜单
    bpy.utils.unregister_class(BUTTON_ACTION_OT_object_object_transform_transform_mode_align)

    # 全局通用功能
    bpy.utils.unregister_class(BUTTON_ACTION_OT_transform_vertex_random)
    bpy.utils.unregister_class(BUTTON_ACTION_OT_transform_resize_texturespace_true)
    bpy.utils.unregister_class(BUTTON_ACTION_OT_transform_translate_texturespace_true)
    bpy.utils.unregister_class(BUTTON_ACTION_OT_transform_push_pull)
    bpy.utils.unregister_class(BUTTON_ACTION_OT_transform_bend)
    bpy.utils.unregister_class(BUTTON_ACTION_OT_transform_shear)
    bpy.utils.unregister_class(BUTTON_ACTION_OT_transform_tosphere)
    bpy.utils.unregister_class(BUTTON_ACTION_OT_call_common_function_transform_menu)
    bpy.utils.unregister_class(VIEW3D_MT_common_function_transform_menu)

    # “选择”菜单功能项
    bpy.utils.unregister_class(BUTTON_ACTION_OT_call_select_select_linked_menu)
    bpy.utils.unregister_class(VIEW3D_MT_select_select_linked_menu)
    bpy.utils.unregister_class(BUTTON_ACTION_OT_call_select_select_grouped_menu)
    bpy.utils.unregister_class(VIEW3D_MT_select_select_grouped_menu)
    bpy.utils.unregister_class(BUTTON_ACTION_OT_object_select_hierarchy_parent_child)
    bpy.utils.unregister_class(BUTTON_ACTION_OT_object_select_less)
    bpy.utils.unregister_class(BUTTON_ACTION_OT_object_select_more)
    bpy.utils.unregister_class(BUTTON_ACTION_OT_call_object_select_more_or_less_menu)
    bpy.utils.unregister_class(VIEW3D_MT_object_select_more_or_less_menu)
    bpy.utils.unregister_class(BUTTON_ACTION_OT_select_select_random)
    bpy.utils.unregister_class(BUTTON_ACTION_OT_view3d_call_select_select_by_type_menu)
    bpy.utils.unregister_class(VIEW3D_MT_select_select_by_type_menu)
    bpy.utils.unregister_class(BUTTON_ACTION_OT_select_select_mirror)


    # “视图”菜单
    bpy.utils.unregister_class(BUTTON_ACTION_OT_view3d_lock_to_active_or_lock_clear)
    bpy.utils.unregister_class(BUTTON_ACTION_OT_view3d_render_border)
    bpy.utils.unregister_class(BUTTON_ACTION_OT_view3d_clip_border)
    bpy.utils.unregister_class(BUTTON_ACTION_OT_view3d_call_menu_view_regions)
    bpy.utils.unregister_class(VIEW3D_MT_view_regions_menu)
    bpy.utils.unregister_class(BUTTON_ACTION_OT_view3d_call_menu_view_align)
    bpy.utils.unregister_class(VIEW3D_MT_view_align_menu)
    bpy.utils.unregister_class(BUTTON_ACTION_OT_view3d_walk)
    bpy.utils.unregister_class(BUTTON_ACTION_OT_view3d_fly)
    bpy.utils.unregister_class(BUTTON_ACTION_OT_view3d_zoom_border)
    bpy.utils.unregister_class(BUTTON_ACTION_OT_view_pan_down)
    bpy.utils.unregister_class(BUTTON_ACTION_OT_view_pan_up)
    bpy.utils.unregister_class(BUTTON_ACTION_OT_view_pan_right)
    bpy.utils.unregister_class(BUTTON_ACTION_OT_view_pan_left)
    bpy.utils.unregister_class(BUTTON_ACTION_OT_view3d_call_menu_view_switch_axis)
    bpy.utils.unregister_class(VIEW3D_MT_view_switch_axis_menu)
    bpy.utils.unregister_class(BUTTON_ACTION_OT_view3d_call_menu_view_axis)
    bpy.utils.unregister_class(VIEW3D_MT_view_axis_menu)
    bpy.utils.unregister_class(BUTTON_ACTION_OT_view3d_view_center_camera)
    bpy.utils.unregister_class(BUTTON_ACTION_OT_view3d_view_camera)
    bpy.utils.unregister_class(BUTTON_ACTION_OT_view3d_object_as_camera)
    bpy.utils.unregister_class(BUTTON_ACTION_OT_view3d_localview_remove_from)
    bpy.utils.unregister_class(BUTTON_ACTION_OT_view3d_localview)
    bpy.utils.unregister_class(BUTTON_ACTION_OT_view_persportho)
    bpy.utils.unregister_class(BUTTON_ACTION_OT_view_all_center_false)
    bpy.utils.unregister_class(BUTTON_ACTION_OT_view_selected_use_all_regions_false)

    # 切换轴心点
    bpy.utils.unregister_class(BUTTON_ACTION_OT_pivot_to_active_element)
    bpy.utils.unregister_class(BUTTON_ACTION_OT_pivot_to_median_point)
    bpy.utils.unregister_class(BUTTON_ACTION_OT_pivot_to_individual_origins)
    bpy.utils.unregister_class(BUTTON_ACTION_OT_pivot_to_cursor)
    bpy.utils.unregister_class(BUTTON_ACTION_OT_pivot_to_bounding_box_center)

    # 变换坐标系类
    bpy.utils.unregister_class(BUTTON_ACTION_OT_orientation_to_parent)
    bpy.utils.unregister_class(BUTTON_ACTION_OT_orientation_to_cursor)
    bpy.utils.unregister_class(BUTTON_ACTION_OT_orientation_to_view)
    bpy.utils.unregister_class(BUTTON_ACTION_OT_orientation_to_gimbal)
    bpy.utils.unregister_class(BUTTON_ACTION_OT_orientation_to_normal)
    bpy.utils.unregister_class(BUTTON_ACTION_OT_orientation_to_local)
    bpy.utils.unregister_class(BUTTON_ACTION_OT_orientation_to_global)

    # 全局高频操作类
    bpy.utils.unregister_class(BUTTON_ACTION_OT_global_add)
    bpy.utils.unregister_class(BUTTON_ACTION_OT_global_duplicate_move)
    bpy.utils.unregister_class(BUTTON_ACTION_OT_global_select_circle)
    bpy.utils.unregister_class(BUTTON_ACTION_OT_global_select_invert)
    bpy.utils.unregister_class(BUTTON_ACTION_OT_global_select_all)
    bpy.utils.unregister_class(BUTTON_ACTION_OT_rotate)
    bpy.utils.unregister_class(BUTTON_ACTION_OT_scale)
    bpy.utils.unregister_class(BUTTON_ACTION_OT_grab)

    # 注销所有Operator类
    bpy.utils.unregister_class(CALLOUT_QUICK_MENU_OT_two)
    bpy.utils.unregister_class(CALLOUT_QUICK_MENU_OT_one)
    bpy.utils.unregister_class(QUICK_POPUP_MENU_OT_two)
    bpy.utils.unregister_class(QUICK_POPUP_MENU_OT_one)
    bpy.utils.unregister_class(MODE_TAB_OT_Switch)
    bpy.utils.unregister_class(VERTEX_EDGE_FACE_OT_Switch)
    bpy.utils.unregister_class(MODE_NORMAL_DOWNUP_OT_Switch)
    bpy.utils.unregister_class(MODE_NORMAL_UPDOWN_OT_Switch)
    bpy.utils.unregister_class(MODE_MENU_OT_Switch)
    bpy.utils.unregister_class(QuickSwitchAddonPreferences)
    bpy.utils.unregister_class(CSAWHEEL_OT_ModeSwitchOperator)
    
    # 注销键位映射
    keymap.unregister()

if __name__ == "__main__":
    register()
