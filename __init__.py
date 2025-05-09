import bpy

bl_info = {
    "name": "AA_switch",
    "author": "Your Name",
    "version": (1, 1),
    "blender": (3, 6, 0),
    "location": "View3D",
    "description": "增强模式切换功能（带安全检查）",
    "category": "3D View"
}

from .operators import CSAWHEEL_OT_ModeSwitchOperator
from .preference import QuickSwitchAddonPreferences
from .operator_mode_transfer import MODE_OT_Transfer
from .operator_mode_transfer import MODE_OT_to_object_and_select
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
from . import show_switch_notice
from . import keymap

from .npanel import (
    QUICKPOPUP_PT_NPanel,
    QUICKPOPUP_OT_UpdateEnum,
)

# 全局通用高频操作按钮：
from .quick_menu_button_functions.button_actions_global_functions import (
    BUTTON_ACTION_OT_grab,
    BUTTON_ACTION_OT_scale,
    BUTTON_ACTION_OT_rotate,
    BUTTON_ACTION_OT_global_select_all,
    BUTTON_ACTION_OT_global_select_invert,
    BUTTON_ACTION_OT_global_select_circle,
    BUTTON_ACTION_OT_global_duplicate_move,
    BUTTON_ACTION_OT_global_add,
    BUTTON_ACTION_OT_global_copy,
    BUTTON_ACTION_OT_global_paste,
    BUTTON_ACTION_OT_call_global_delete_menu,
    VIEW3D_MT_global_delete_menu,
    BUTTON_ACTION_OT_global_hide_view_set,
    BUTTON_ACTION_OT_global_hide_view_clear,
    BUTTON_ACTION_OT_global_apply,
    BUTTON_ACTION_OT_global_transform_mirror,
    BUTTON_ACTION_OT_global_object_pose_clear,
)

from .quick_menu_button_functions.button_actions_global_switch_orientation_slots import (
    BUTTON_ACTION_OT_switch_orientation_menu,
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
    BUTTON_ACTION_OT_switch_pivot_menu,
)
# “视图”菜单
from .quick_menu_button_functions.button_actions_global_view_menu import (
    BUTTON_ACTION_OT_view3d_call_view_viewpoint_menu,
    BUTTON_ACTION_OT_view3d_call_view_navigation_menu,
    BUTTON_ACTION_OT_view3d_zoom_border,
    BUTTON_ACTION_OT_view_pan_left,
    BUTTON_ACTION_OT_view_pan_right,
    BUTTON_ACTION_OT_view_pan_up,
    BUTTON_ACTION_OT_view_pan_down,
    BUTTON_ACTION_OT_view3d_walk,
    BUTTON_ACTION_OT_view3d_call_view_align_menu,
    VIEW3D_MT_view_regions_menu,
    BUTTON_ACTION_OT_view3d_call_view_regions_menu,
    BUTTON_ACTION_OT_view3d_clip_border,
    BUTTON_ACTION_OT_view3d_render_border,
    BUTTON_ACTION_OT_view3d_lock_to_active_or_lock_clear,
    BUTTON_ACTION_OT_view3d_view_all_center_true,
    BUTTON_ACTION_OT_view3d_area_menu,
    BUTTON_ACTION_OT_view3d_screen_screen_full_area,
)

from .quick_menu_button_functions.button_actions_global_select_menu import (
    BUTTON_ACTION_OT_select_select_mirror,
    VIEW3D_MT_select_select_by_type_menu,
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
    BUTTON_ACTION_OT_transform_tosphere,
    BUTTON_ACTION_OT_transform_shear,
    BUTTON_ACTION_OT_transform_bend,
)

from .quick_menu_button_functions.button_actions_object_mode import (
    BUTTON_ACTION_OT_object_object_transform_transform_mode_align,
    BUTTON_ACTION_OT_object_object_duplicate_move_linked,
)

from .quick_menu_button_functions.button_actions_armature import (
    BUTTON_ACTION_OT_armature_bone_primitive_add,
)

def register():
    # 注册模式监测功能
    register_mode_handler()

    show_switch_notice.register()

    # npanel.py 设置
    bpy.utils.register_class(QUICKPOPUP_PT_NPanel)
    bpy.utils.register_class(QUICKPOPUP_OT_UpdateEnum)
    
    # 注册所有Operator类
    bpy.utils.register_class(CSAWHEEL_OT_ModeSwitchOperator)
    bpy.utils.register_class(QuickSwitchAddonPreferences)
    bpy.utils.register_class(MODE_NORMAL_UPDOWN_OT_Switch)
    bpy.utils.register_class(MODE_NORMAL_DOWNUP_OT_Switch)
    bpy.utils.register_class(VERTEX_EDGE_FACE_OT_Switch)
    bpy.utils.register_class(MODE_MENU_OT_Switch)
    bpy.utils.register_class(MODE_TAB_OT_Switch)
    bpy.utils.register_class(MODE_OT_Transfer)
    bpy.utils.register_class(MODE_OT_to_object_and_select)
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
    bpy.utils.register_class(BUTTON_ACTION_OT_global_copy)
    bpy.utils.register_class(BUTTON_ACTION_OT_global_paste)
    bpy.utils.register_class(VIEW3D_MT_global_delete_menu)
    bpy.utils.register_class(BUTTON_ACTION_OT_call_global_delete_menu)
    bpy.utils.register_class(BUTTON_ACTION_OT_global_hide_view_set)
    bpy.utils.register_class(BUTTON_ACTION_OT_global_hide_view_clear)
    bpy.utils.register_class(BUTTON_ACTION_OT_global_apply)
    bpy.utils.register_class(BUTTON_ACTION_OT_global_transform_mirror)
    bpy.utils.register_class(BUTTON_ACTION_OT_global_object_pose_clear)


    # 变换坐标系类
    bpy.utils.register_class(BUTTON_ACTION_OT_switch_orientation_menu)
    bpy.utils.register_class(BUTTON_ACTION_OT_orientation_to_global)
    bpy.utils.register_class(BUTTON_ACTION_OT_orientation_to_local)
    bpy.utils.register_class(BUTTON_ACTION_OT_orientation_to_normal)
    bpy.utils.register_class(BUTTON_ACTION_OT_orientation_to_gimbal)
    bpy.utils.register_class(BUTTON_ACTION_OT_orientation_to_view)
    bpy.utils.register_class(BUTTON_ACTION_OT_orientation_to_cursor)
    bpy.utils.register_class(BUTTON_ACTION_OT_orientation_to_parent)

    # 切换轴心点
    bpy.utils.register_class(BUTTON_ACTION_OT_switch_pivot_menu)
    bpy.utils.register_class(BUTTON_ACTION_OT_pivot_to_bounding_box_center)
    bpy.utils.register_class(BUTTON_ACTION_OT_pivot_to_cursor)
    bpy.utils.register_class(BUTTON_ACTION_OT_pivot_to_individual_origins)
    bpy.utils.register_class(BUTTON_ACTION_OT_pivot_to_median_point)
    bpy.utils.register_class(BUTTON_ACTION_OT_pivot_to_active_element)

    # "视图"菜单功能项
    bpy.utils.register_class(BUTTON_ACTION_OT_view3d_call_view_viewpoint_menu)
    bpy.utils.register_class(BUTTON_ACTION_OT_view3d_call_view_navigation_menu)
    bpy.utils.register_class(BUTTON_ACTION_OT_view3d_zoom_border)
    bpy.utils.register_class(BUTTON_ACTION_OT_view_pan_left)
    bpy.utils.register_class(BUTTON_ACTION_OT_view_pan_right)
    bpy.utils.register_class(BUTTON_ACTION_OT_view_pan_up)
    bpy.utils.register_class(BUTTON_ACTION_OT_view_pan_down)
    bpy.utils.register_class(BUTTON_ACTION_OT_view3d_walk)
    bpy.utils.register_class(BUTTON_ACTION_OT_view3d_call_view_align_menu)
    bpy.utils.register_class(VIEW3D_MT_view_regions_menu)
    bpy.utils.register_class(BUTTON_ACTION_OT_view3d_call_view_regions_menu)
    bpy.utils.register_class(BUTTON_ACTION_OT_view3d_clip_border)
    bpy.utils.register_class(BUTTON_ACTION_OT_view3d_render_border)
    bpy.utils.register_class(BUTTON_ACTION_OT_view3d_lock_to_active_or_lock_clear)
    bpy.utils.register_class(BUTTON_ACTION_OT_view3d_view_all_center_true)
    bpy.utils.register_class(BUTTON_ACTION_OT_view3d_area_menu)
    bpy.utils.register_class(BUTTON_ACTION_OT_view3d_screen_screen_full_area)
        
    # “选择”菜单功能项
    bpy.utils.register_class(BUTTON_ACTION_OT_select_select_mirror)
    bpy.utils.register_class(VIEW3D_MT_select_select_by_type_menu)
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
    bpy.utils.register_class(BUTTON_ACTION_OT_transform_tosphere)
    bpy.utils.register_class(BUTTON_ACTION_OT_transform_shear)
    bpy.utils.register_class(BUTTON_ACTION_OT_transform_bend)

    # 物体模式—“物体”菜单
    bpy.utils.register_class(BUTTON_ACTION_OT_object_object_transform_transform_mode_align)
    bpy.utils.register_class(BUTTON_ACTION_OT_object_object_duplicate_move_linked)

    # "骨架"模式相关功能
    bpy.utils.register_class(BUTTON_ACTION_OT_armature_bone_primitive_add)

    # 注册键位映射
    keymap.register()

def unregister():    
    # 注销模式监测功能
    unregister_mode_handler()

    show_switch_notice.unregister()

    # ”骨架“模式相关功能
    bpy.utils.unregister_class(BUTTON_ACTION_OT_armature_bone_primitive_add)

    # 物体模式—“物体”菜单
    bpy.utils.unregister_class(BUTTON_ACTION_OT_object_object_transform_transform_mode_align)
    bpy.utils.unregister_class(BUTTON_ACTION_OT_object_object_duplicate_move_linked)

    # 全局通用功能
    bpy.utils.unregister_class(BUTTON_ACTION_OT_transform_bend)
    bpy.utils.unregister_class(BUTTON_ACTION_OT_transform_shear)
    bpy.utils.unregister_class(BUTTON_ACTION_OT_transform_tosphere)

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
    bpy.utils.unregister_class(VIEW3D_MT_select_select_by_type_menu)
    bpy.utils.unregister_class(BUTTON_ACTION_OT_select_select_mirror)


    # “视图”菜单
    bpy.utils.unregister_class(BUTTON_ACTION_OT_view3d_screen_screen_full_area)
    bpy.utils.unregister_class(BUTTON_ACTION_OT_view3d_area_menu)
    bpy.utils.unregister_class(BUTTON_ACTION_OT_view3d_view_all_center_true)
    bpy.utils.unregister_class(BUTTON_ACTION_OT_view3d_lock_to_active_or_lock_clear)
    bpy.utils.unregister_class(BUTTON_ACTION_OT_view3d_render_border)
    bpy.utils.unregister_class(BUTTON_ACTION_OT_view3d_clip_border)
    bpy.utils.unregister_class(BUTTON_ACTION_OT_view3d_call_view_regions_menu)
    bpy.utils.unregister_class(VIEW3D_MT_view_regions_menu)
    bpy.utils.unregister_class(BUTTON_ACTION_OT_view3d_call_view_align_menu)
    bpy.utils.unregister_class(BUTTON_ACTION_OT_view3d_walk)
    bpy.utils.unregister_class(BUTTON_ACTION_OT_view3d_zoom_border)
    bpy.utils.unregister_class(BUTTON_ACTION_OT_view_pan_down)
    bpy.utils.unregister_class(BUTTON_ACTION_OT_view_pan_up)
    bpy.utils.unregister_class(BUTTON_ACTION_OT_view_pan_right)
    bpy.utils.unregister_class(BUTTON_ACTION_OT_view_pan_left)
    bpy.utils.unregister_class(BUTTON_ACTION_OT_view3d_call_view_navigation_menu)
    bpy.utils.unregister_class(BUTTON_ACTION_OT_view3d_call_view_viewpoint_menu)

    # 切换轴心点
    bpy.utils.unregister_class(BUTTON_ACTION_OT_switch_pivot_menu)
    bpy.utils.unregister_class(BUTTON_ACTION_OT_pivot_to_active_element)
    bpy.utils.unregister_class(BUTTON_ACTION_OT_pivot_to_median_point)
    bpy.utils.unregister_class(BUTTON_ACTION_OT_pivot_to_individual_origins)
    bpy.utils.unregister_class(BUTTON_ACTION_OT_pivot_to_cursor)
    bpy.utils.unregister_class(BUTTON_ACTION_OT_pivot_to_bounding_box_center)

    # 变换坐标系类
    bpy.utils.unregister_class(BUTTON_ACTION_OT_switch_orientation_menu)
    bpy.utils.unregister_class(BUTTON_ACTION_OT_orientation_to_parent)
    bpy.utils.unregister_class(BUTTON_ACTION_OT_orientation_to_cursor)
    bpy.utils.unregister_class(BUTTON_ACTION_OT_orientation_to_view)
    bpy.utils.unregister_class(BUTTON_ACTION_OT_orientation_to_gimbal)
    bpy.utils.unregister_class(BUTTON_ACTION_OT_orientation_to_normal)
    bpy.utils.unregister_class(BUTTON_ACTION_OT_orientation_to_local)
    bpy.utils.unregister_class(BUTTON_ACTION_OT_orientation_to_global)

    # 全局高频操作类
    bpy.utils.unregister_class(BUTTON_ACTION_OT_global_object_pose_clear)
    bpy.utils.unregister_class(BUTTON_ACTION_OT_global_transform_mirror)
    bpy.utils.unregister_class(BUTTON_ACTION_OT_global_apply)
    bpy.utils.unregister_class(BUTTON_ACTION_OT_global_hide_view_clear)
    bpy.utils.unregister_class(BUTTON_ACTION_OT_global_hide_view_set)
    bpy.utils.unregister_class(BUTTON_ACTION_OT_call_global_delete_menu)
    bpy.utils.unregister_class(VIEW3D_MT_global_delete_menu)
    bpy.utils.unregister_class(BUTTON_ACTION_OT_global_paste)
    bpy.utils.unregister_class(BUTTON_ACTION_OT_global_copy)
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
    bpy.utils.unregister_class(MODE_OT_to_object_and_select)
    bpy.utils.unregister_class(MODE_OT_Transfer)
    bpy.utils.unregister_class(MODE_TAB_OT_Switch)
    bpy.utils.unregister_class(VERTEX_EDGE_FACE_OT_Switch)
    bpy.utils.unregister_class(MODE_NORMAL_DOWNUP_OT_Switch)
    bpy.utils.unregister_class(MODE_NORMAL_UPDOWN_OT_Switch)
    bpy.utils.unregister_class(MODE_MENU_OT_Switch)
    bpy.utils.unregister_class(QuickSwitchAddonPreferences)
    bpy.utils.unregister_class(CSAWHEEL_OT_ModeSwitchOperator)

    # npanel 设置
    bpy.utils.unregister_class(QUICKPOPUP_PT_NPanel)
    bpy.utils.unregister_class(QUICKPOPUP_OT_UpdateEnum)
    
    # 注销键位映射
    keymap.unregister()

if __name__ == "__main__":
    register()
