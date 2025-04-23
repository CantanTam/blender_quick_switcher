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
from .quick_menu_button_functions.button_actions_grab_scale_rotate import (
    BUTTON_ACTION_OT_grab,
    BUTTON_ACTION_OT_scale,
    BUTTON_ACTION_OT_rotate
)

from .quick_menu_button_functions.button_actions_switch_orientation_slots import (
    BUTTON_ACTION_OT_orientation_to_global,
    BUTTON_ACTION_OT_orientation_to_local,
    BUTTON_ACTION_OT_orientation_to_normal,
    BUTTON_ACTION_OT_orientation_to_gimbal,
    BUTTON_ACTION_OT_orientation_to_view,
    BUTTON_ACTION_OT_orientation_to_cursor,
    BUTTON_ACTION_OT_orientation_to_parent
)

from .quick_menu_button_functions.button_actions_switch_pivot_points import (
    BUTTON_ACTION_OT_pivot_to_bounding_box_center,
    BUTTON_ACTION_OT_pivot_to_cursor,
    BUTTON_ACTION_OT_pivot_to_individual_origins,
    BUTTON_ACTION_OT_pivot_to_median_point,
    BUTTON_ACTION_OT_pivot_to_active_element
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

    # 所有按钮操作符的注册
    bpy.utils.register_class(BUTTON_ACTION_OT_grab)
    bpy.utils.register_class(BUTTON_ACTION_OT_scale)
    bpy.utils.register_class(BUTTON_ACTION_OT_rotate)

    # 变换坐标系类
    bpy.utils.register_class(BUTTON_ACTION_OT_orientation_to_global)
    bpy.utils.register_class(BUTTON_ACTION_OT_orientation_to_local)
    bpy.utils.register_class(BUTTON_ACTION_OT_orientation_to_normal)
    bpy.utils.register_class(BUTTON_ACTION_OT_orientation_to_gimbal)
    bpy.utils.register_class(BUTTON_ACTION_OT_orientation_to_view)
    bpy.utils.register_class(BUTTON_ACTION_OT_orientation_to_cursor)
    bpy.utils.register_class(BUTTON_ACTION_OT_orientation_to_parent)

    # 枢轴点类
    bpy.utils.register_class(BUTTON_ACTION_OT_pivot_to_bounding_box_center)
    bpy.utils.register_class(BUTTON_ACTION_OT_pivot_to_cursor)
    bpy.utils.register_class(BUTTON_ACTION_OT_pivot_to_individual_origins)
    bpy.utils.register_class(BUTTON_ACTION_OT_pivot_to_median_point)
    bpy.utils.register_class(BUTTON_ACTION_OT_pivot_to_active_element)
    
    # 注册键位映射
    keymap.register()

def unregister():    
    # 注销模式监测功能
    unregister_mode_handler()

    # 枢轴点类
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

    # 移动/缩放/旋转操作类
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
