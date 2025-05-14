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

from .operator_typeandmode_name_mode import (
    register as register_operator_typeandmode_name_mode,
    unregister as unregister_operator_typeandmode_name_mode,
)

from .show_switch_notice import (
    register as register_show_switch_notice,
    unregister as unregister_show_switch_notice,
)
from . import keymap

from .npanel import (
    register as register_npanel,
    unregister as unregister_npanel,
)

# 全局通用高频操作按钮：
from .quick_menu_button_functions.button_actions_global_functions import (
    register as register_button_actions_global_functions,
    unregister as unregister_button_actions_global_functions,
)

from .quick_menu_button_functions.button_actions_global_switch_orientation_slots import (
    register as register_button_actions_global_switch_orientation_slots,
    unregister as unregister_button_actions_global_switch_orientation_slots,
)
# 切换轴心点
from .quick_menu_button_functions.button_actions_global_switch_pivot_points import (
    register as register_button_actions_global_switch_pivot_points,
    unregister as unregister_button_actions_global_switch_pivot_points,
)

# 切换吸附
from .quick_menu_button_functions.button_actions_global_switch_snap import (
    register as register_button_actions_global_switch_snap,
    unregister as unregister_button_actions_global_switch_snap,
)

# 切换衰减编辑
from .quick_menu_button_functions.button_actions_global_switch_proportional import (
    register as register_button_actions_global_switch_proportional,
    unregister as unregister_button_actions_global_switch_proportional,
)
# “视图”菜单
from .quick_menu_button_functions.button_actions_global_view_menu import (
    register as register_button_actions_global_view_menu,
    unregister as unregister_button_actions_global_view_menu,
)

from .quick_menu_button_functions.button_actions_global_select_menu import (
    register as register_button_actions_global_select_menu,
    unregister as unregister_button_actions_global_select_menu,
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

from .right_click_add_common_actions import (
    register as register_right_click_add_common_actions,
    unregister as unregister_right_click_add_common_actions,
)

from .right_click_global_view_actions import (
    register as register_right_click_global_view_actions,
    unregister as unregister_right_click_global_view_actions,
)

from .right_click_add_setting_panel import (
    register as register_right_click_add_setting_panel,
    unregister as unregister_right_click_add_setting_panel,
)

def register():
    # 注册右键添加到设置面板
    register_right_click_add_setting_panel()

    # 注册视图右键菜单功能
    register_right_click_global_view_actions()

    # 注册右键菜单功能
    register_right_click_add_common_actions()
    # 注册模式监测功能
    register_operator_typeandmode_name_mode()

    register_show_switch_notice()

    # npanel.py 设置
    register_npanel()
    
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
    register_button_actions_global_functions()

    # 变换坐标系类
    register_button_actions_global_switch_orientation_slots()

    # 切换轴心点
    register_button_actions_global_switch_pivot_points()

    # 切换吸附
    register_button_actions_global_switch_snap()

    # 切换衰减编辑
    register_button_actions_global_switch_proportional()

    # "视图"菜单功能项
    register_button_actions_global_view_menu()
        
    # “选择”菜单功能项
    register_button_actions_global_select_menu()

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
    # 注销右键添加到设置面板
    unregister_right_click_add_setting_panel()

    # 注销视图右键菜单功能
    unregister_right_click_global_view_actions()

    # 注销右键菜单功能
    unregister_right_click_add_common_actions()
    # 注销模式监测功能
    unregister_operator_typeandmode_name_mode()

    unregister_show_switch_notice()

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
    unregister_button_actions_global_select_menu()


    # “视图”菜单
    unregister_button_actions_global_view_menu()

    # 切换衰减编辑
    unregister_button_actions_global_switch_proportional()

    # 切换吸附
    unregister_button_actions_global_switch_snap()
    # 切换轴心点
    unregister_button_actions_global_switch_pivot_points()

    # 变换坐标系类
    unregister_button_actions_global_switch_orientation_slots()

    # 全局高频操作类
    unregister_button_actions_global_functions()

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
    unregister_npanel()
    
    # 注销键位映射
    keymap.unregister()

if __name__ == "__main__":
    register()
