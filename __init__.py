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
    
    # 注册键位映射
    keymap.register()

def unregister():    
    # 注销模式监测功能
    unregister_mode_handler()

    
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
