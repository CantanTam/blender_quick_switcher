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

ADDON_NAME = __name__

from .operators import CSAWHEEL_OT_ModeSwitchOperator
from .preference import QuickSwitchAddonPreferences
from .operator_mode_transfer import MODE_OT_Transfer
from .operator_mode_transfer import MODE_OT_to_object_and_select
from .operator_mode_switch_normal_uptodown import MODE_NORMAL_UPDOWN_OT_Switch
from .operator_mode_switch_normal_downtoup import MODE_NORMAL_DOWNUP_OT_Switch
from .operator_vertex_edge_face_switch import VERTEX_EDGE_FACE_OT_Switch
from .operator_mode_switch_menu_downtoup import MODE_MENU_OT_Switch
from .operator_mode_switch_tab import MODE_TAB_OT_Switch
from .operator_grab_scale_rotate_switch import (
    GRAB_SCALE_ROTATE_OT_Switch,
    GRAB_SCALE_ROTATE_OT_Switch_action,
)

from .quick_menu_popups.popup_quick_menu_one_object import QUICK_POPUP_MENU_OT_one_object
from .quick_menu_popups.popup_quick_menu_one_meshedit import QUICK_POPUP_MENU_OT_one_meshedit
from .quick_menu_popups.popup_quick_menu_one_meshsculpt import QUICK_POPUP_MENU_OT_one_meshsculpt
from .quick_menu_popups.popup_quick_menu_one_meshtexture import QUICK_POPUP_MENU_OT_one_meshtexture
from .quick_menu_popups.popup_quick_menu_one_meshvertexpaint import QUICK_POPUP_MENU_OT_one_meshvertexpaint
from .quick_menu_popups.popup_quick_menu_one_meshweightpaint import QUICK_POPUP_MENU_OT_one_meshweightpaint
from .quick_menu_popups.popup_quick_menu_one_gpenciledit import QUICK_POPUP_MENU_OT_one_gpenciledit
from .quick_menu_popups.popup_quick_menu_one_gpencilpaint import QUICK_POPUP_MENU_OT_one_gpencilpaint
from .quick_menu_popups.popup_quick_menu_one_gpencilsculpt import QUICK_POPUP_MENU_OT_one_gpencilsculpt
from .quick_menu_popups.popup_quick_menu_one_gpencilvertex import QUICK_POPUP_MENU_OT_one_gpencilvertex
from .quick_menu_popups.popup_quick_menu_one_gpencilweight import QUICK_POPUP_MENU_OT_one_gpencilweight
from .quick_menu_popups.popup_quick_menu_one_greasepenciledit import QUICK_POPUP_MENU_OT_one_greasepenciledit
from .quick_menu_popups.popup_quick_menu_one_greasepencilpaint import QUICK_POPUP_MENU_OT_one_greasepencilpaint
from .quick_menu_popups.popup_quick_menu_one_greasepencilsculpt import QUICK_POPUP_MENU_OT_one_greasepencilsculpt
from .quick_menu_popups.popup_quick_menu_one_greasepencilvertex import QUICK_POPUP_MENU_OT_one_greasepencilvertex
from .quick_menu_popups.popup_quick_menu_one_greasepencilweight import QUICK_POPUP_MENU_OT_one_greasepencilweight
from .quick_menu_popups.popup_quick_menu_one_armatureedit import QUICK_POPUP_MENU_OT_one_armatureedit
from .quick_menu_popups.popup_quick_menu_one_armaturepose import QUICK_POPUP_MENU_OT_one_armaturepose
from .quick_menu_popups.popup_quick_menu_one_curveedit import QUICK_POPUP_MENU_OT_one_curveedit
from .quick_menu_popups.popup_quick_menu_one_surfaceedit import QUICK_POPUP_MENU_OT_one_surfaceedit
from .quick_menu_popups.popup_quick_menu_one_metaedit import QUICK_POPUP_MENU_OT_one_metaedit
from .quick_menu_popups.popup_quick_menu_one_fontedit import QUICK_POPUP_MENU_OT_one_fontedit
from .quick_menu_popups.popup_quick_menu_one_latticeedit import QUICK_POPUP_MENU_OT_one_latticeedit

from .quick_menu_popups.popup_quick_menu_two_object import QUICK_POPUP_MENU_OT_two_object
from .quick_menu_popups.popup_quick_menu_two_meshedit import QUICK_POPUP_MENU_OT_two_meshedit
from .quick_menu_popups.popup_quick_menu_two_meshsculpt import QUICK_POPUP_MENU_OT_two_meshsculpt
from .quick_menu_popups.popup_quick_menu_two_meshtexture import QUICK_POPUP_MENU_OT_two_meshtexture
from .quick_menu_popups.popup_quick_menu_two_meshvertexpaint import QUICK_POPUP_MENU_OT_two_meshvertexpaint
from .quick_menu_popups.popup_quick_menu_two_meshweightpaint import QUICK_POPUP_MENU_OT_two_meshweightpaint
from .quick_menu_popups.popup_quick_menu_two_gpenciledit import QUICK_POPUP_MENU_OT_two_gpenciledit
from .quick_menu_popups.popup_quick_menu_two_gpencilpaint import QUICK_POPUP_MENU_OT_two_gpencilpaint
from .quick_menu_popups.popup_quick_menu_two_gpencilsculpt import QUICK_POPUP_MENU_OT_two_gpencilsculpt
from .quick_menu_popups.popup_quick_menu_two_gpencilvertex import QUICK_POPUP_MENU_OT_two_gpencilvertex
from .quick_menu_popups.popup_quick_menu_two_gpencilweight import QUICK_POPUP_MENU_OT_two_gpencilweight
from .quick_menu_popups.popup_quick_menu_two_greasepenciledit import QUICK_POPUP_MENU_OT_two_greasepenciledit
from .quick_menu_popups.popup_quick_menu_two_greasepencilpaint import QUICK_POPUP_MENU_OT_two_greasepencilpaint
from .quick_menu_popups.popup_quick_menu_two_greasepencilsculpt import QUICK_POPUP_MENU_OT_two_greasepencilsculpt
from .quick_menu_popups.popup_quick_menu_two_greasepencilvertex import QUICK_POPUP_MENU_OT_two_greasepencilvertex
from .quick_menu_popups.popup_quick_menu_two_greasepencilweight import QUICK_POPUP_MENU_OT_two_greasepencilweight
from .quick_menu_popups.popup_quick_menu_two_armatureedit import QUICK_POPUP_MENU_OT_two_armatureedit
from .quick_menu_popups.popup_quick_menu_two_armaturepose import QUICK_POPUP_MENU_OT_two_armaturepose
from .quick_menu_popups.popup_quick_menu_two_curveedit import QUICK_POPUP_MENU_OT_two_curveedit
from .quick_menu_popups.popup_quick_menu_two_surfaceedit import QUICK_POPUP_MENU_OT_two_surfaceedit
from .quick_menu_popups.popup_quick_menu_two_metaedit import QUICK_POPUP_MENU_OT_two_metaedit
from .quick_menu_popups.popup_quick_menu_two_fontedit import QUICK_POPUP_MENU_OT_two_fontedit
from .quick_menu_popups.popup_quick_menu_two_latticeedit import QUICK_POPUP_MENU_OT_two_latticeedit

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

# 全局通用高频操作按钮：
from .quick_menu_button_functions.button_actions_global import (
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

from .quick_menu_button_functions.button_actions_global_select_menu import (
    register as register_button_actions_global_select_menu,
    unregister as unregister_button_actions_global_select_menu,
)

from .quick_menu_button_functions.button_actions_object import (
    register as register_button_actions_object,
    unregister as unregister_button_actions_object,
)

from .quick_menu_button_functions.button_actions_mesh_edit import (
    register as register_button_actions_mesh_edit,
    unregister as unregister_button_actions_mesh_edit,
)

from .quick_menu_button_functions.button_actions_mesh_vertex import (
    register as register_button_actions_mesh_vertex,
    unregister as unregister_button_actions_mesh_vertex,
)

from .quick_menu_button_functions.button_actions_gpencil_edit import (
    register as register_button_actions_gpencil_edit,
    unregister as unregister_button_actions_gpencil_edit,
)

from .quick_menu_button_functions.button_actions_gpencil_weight import (
    register as register_button_actions_gpencil_weight,
    unregister as unregister_button_actions_gpencil_weight,
)

from .quick_menu_button_functions.button_actions_gpencil_vertex import (
    register as register_button_actions_gpencil_vertex,
    unregister as unregister_button_actions_gpencil_vertex,
)

from .quick_menu_button_functions.button_actions_greasepencil_edit import (
    register as register_button_actions_greasepencil_edit,
    unregister as unregister_button_actions_greasepencil_edit,
)

from .quick_menu_button_functions.button_actions_greasepencil_weight import (
    register as register_button_actions_greasepencil_weight,
    unregister as unregister_button_actions_greasepencil_weight,
)

from .quick_menu_button_functions.button_actions_greasepencil_vertex import (
    register as register_button_actions_greasepencil_vertex,
    unregister as unregister_button_actions_greasepencil_vertex,
)

from .quick_menu_button_functions.button_actions_armature_edit import (
    register as register_button_actions_armature_edit,
    unregister as unregister_button_actions_armature_edit,
)

from .quick_menu_button_functions.button_actions_curve_edit import (
    register as register_button_actions_curve_edit,
    unregister as unregister_button_actions_curve_edit,
)

from .quick_menu_button_functions.button_actions_lattice import (
    register as register_button_actions_lattice,
    unregister as unregister_button_actions_lattice,
)

from .right_click_to_switcher.right_click_add_global import (
    register as register_right_click_add_global,
    unregister as unregister_right_click_add_global,
)

from .right_click_to_switcher.right_click_add_object import (
    register as register_right_click_add_object,
    unregister as unregister_right_click_add_object,
)

from .right_click_to_switcher.right_click_add_mesh_edit import (
    register as register_right_click_add_mesh_edit,
    unregister as unregister_right_click_add_mesh_edit,
)

from .right_click_to_switcher.right_click_add_mesh_vertex import (
    register as register_right_click_add_mesh_vertex,
    unregister as unregister_right_click_add_mesh_vertex,
)

from .right_click_to_switcher.right_click_add_gpencil_edit import (
    register as register_right_click_add_gpencil_edit,
    unregister as unregister_right_click_add_gpencil_edit,
)

from .right_click_to_switcher.right_click_add_gpencil_weight import (
    register as register_right_click_add_gpencil_weight,
    unregister as unregister_right_click_add_gpencil_weight,
)

from .right_click_to_switcher.right_click_add_gpencil_vertex import (
    register as register_right_click_add_gpencil_vertex,
    unregister as unregister_right_click_add_gpencil_vertex,
)

from .right_click_to_switcher.right_click_add_greasepencil_edit import (
    register as register_right_click_add_greasepencil_edit,
    unregister as unregister_right_click_add_greasepencil_edit,
)

from .right_click_to_switcher.right_click_add_greasepencil_weight import (
    register as register_right_click_add_greasepencil_weight,
    unregister as unregister_right_click_add_greasepencil_weight,
)

from .right_click_to_switcher.right_click_add_greasepencil_vertex import (
    register as register_right_click_add_greasepencil_vertex,
    unregister as unregister_right_click_add_greasepencil_vertex,
)

from .right_click_to_switcher.right_click_add_armature_edit import (
    register as register_right_click_add_armature_edit,
    unregister as unregister_right_click_add_armature_edit,
)

from .right_click_to_switcher.right_click_add_curve_edit import (
    register as register_right_click_add_curve_edit,
    unregister as unregister_right_click_add_curve_edit,
)

from .right_click_to_switcher.right_click_add_armature_pose import (
    register as register_right_click_add_armature_pose,
    unregister as unregister_right_click_add_armature_pose,
)

from .right_click_to_switcher.right_click_add_lattice_edit import (
    register as register_right_click_add_lattice_edit,
    unregister as unregister_right_click_add_lattice_edit,
)

from .right_click_to_switcher.right_click_global_view_menu_actions import (
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

    # 注册物体模式——添加到右键
    register_right_click_add_object()

    # 注册“网格编辑”模式
    register_right_click_add_mesh_edit()

    register_right_click_add_mesh_vertex()

    register_right_click_add_gpencil_edit()

    register_right_click_add_gpencil_weight()

    register_right_click_add_gpencil_vertex()


    register_right_click_add_greasepencil_edit()

    register_right_click_add_greasepencil_weight()

    register_right_click_add_greasepencil_vertex()

    # 注册“骨架编辑”模式
    register_right_click_add_armature_edit()

    register_right_click_add_curve_edit()

    # 注册“骨架姿态”
    register_right_click_add_armature_pose()

    register_right_click_add_lattice_edit()

    # 注册右键菜单功能
    register_right_click_add_global()
    # 注册模式监测功能
    register_operator_typeandmode_name_mode()

    register_show_switch_notice()
    
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
    bpy.utils.register_class(GRAB_SCALE_ROTATE_OT_Switch)
    bpy.utils.register_class(GRAB_SCALE_ROTATE_OT_Switch_action)

    # 注册所有QUICK_POPUP_MENU_OT_*类
    bpy.utils.register_class(QUICK_POPUP_MENU_OT_one_object)
    bpy.utils.register_class(QUICK_POPUP_MENU_OT_one_meshedit)
    bpy.utils.register_class(QUICK_POPUP_MENU_OT_one_meshsculpt)
    bpy.utils.register_class(QUICK_POPUP_MENU_OT_one_meshtexture)
    bpy.utils.register_class(QUICK_POPUP_MENU_OT_one_meshvertexpaint)
    bpy.utils.register_class(QUICK_POPUP_MENU_OT_one_meshweightpaint)
    bpy.utils.register_class(QUICK_POPUP_MENU_OT_one_gpenciledit)
    bpy.utils.register_class(QUICK_POPUP_MENU_OT_one_gpencilpaint)
    bpy.utils.register_class(QUICK_POPUP_MENU_OT_one_gpencilsculpt)
    bpy.utils.register_class(QUICK_POPUP_MENU_OT_one_gpencilvertex)
    bpy.utils.register_class(QUICK_POPUP_MENU_OT_one_gpencilweight)
    bpy.utils.register_class(QUICK_POPUP_MENU_OT_one_greasepenciledit)
    bpy.utils.register_class(QUICK_POPUP_MENU_OT_one_greasepencilpaint)
    bpy.utils.register_class(QUICK_POPUP_MENU_OT_one_greasepencilsculpt)
    bpy.utils.register_class(QUICK_POPUP_MENU_OT_one_greasepencilvertex)
    bpy.utils.register_class(QUICK_POPUP_MENU_OT_one_greasepencilweight)
    bpy.utils.register_class(QUICK_POPUP_MENU_OT_one_armatureedit)
    bpy.utils.register_class(QUICK_POPUP_MENU_OT_one_armaturepose)
    bpy.utils.register_class(QUICK_POPUP_MENU_OT_one_curveedit)
    bpy.utils.register_class(QUICK_POPUP_MENU_OT_one_surfaceedit)
    bpy.utils.register_class(QUICK_POPUP_MENU_OT_one_metaedit)
    bpy.utils.register_class(QUICK_POPUP_MENU_OT_one_fontedit)
    bpy.utils.register_class(QUICK_POPUP_MENU_OT_one_latticeedit)

    bpy.utils.register_class(QUICK_POPUP_MENU_OT_two_object)
    bpy.utils.register_class(QUICK_POPUP_MENU_OT_two_meshedit)
    bpy.utils.register_class(QUICK_POPUP_MENU_OT_two_meshsculpt)
    bpy.utils.register_class(QUICK_POPUP_MENU_OT_two_meshtexture)
    bpy.utils.register_class(QUICK_POPUP_MENU_OT_two_meshvertexpaint)
    bpy.utils.register_class(QUICK_POPUP_MENU_OT_two_meshweightpaint)
    bpy.utils.register_class(QUICK_POPUP_MENU_OT_two_gpenciledit)
    bpy.utils.register_class(QUICK_POPUP_MENU_OT_two_gpencilpaint)
    bpy.utils.register_class(QUICK_POPUP_MENU_OT_two_gpencilsculpt)
    bpy.utils.register_class(QUICK_POPUP_MENU_OT_two_gpencilvertex)
    bpy.utils.register_class(QUICK_POPUP_MENU_OT_two_gpencilweight)
    bpy.utils.register_class(QUICK_POPUP_MENU_OT_two_greasepenciledit)
    bpy.utils.register_class(QUICK_POPUP_MENU_OT_two_greasepencilpaint)
    bpy.utils.register_class(QUICK_POPUP_MENU_OT_two_greasepencilsculpt)
    bpy.utils.register_class(QUICK_POPUP_MENU_OT_two_greasepencilvertex)
    bpy.utils.register_class(QUICK_POPUP_MENU_OT_two_greasepencilweight)
    bpy.utils.register_class(QUICK_POPUP_MENU_OT_two_armatureedit)
    bpy.utils.register_class(QUICK_POPUP_MENU_OT_two_armaturepose)
    bpy.utils.register_class(QUICK_POPUP_MENU_OT_two_curveedit)
    bpy.utils.register_class(QUICK_POPUP_MENU_OT_two_surfaceedit)
    bpy.utils.register_class(QUICK_POPUP_MENU_OT_two_metaedit)
    bpy.utils.register_class(QUICK_POPUP_MENU_OT_two_fontedit)
    bpy.utils.register_class(QUICK_POPUP_MENU_OT_two_latticeedit)

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

    # “选择”菜单功能项
    register_button_actions_global_select_menu()

    # 物体模式—“物体”菜单
    register_button_actions_object()

    # 物体模式
    register_button_actions_mesh_edit()

    register_button_actions_mesh_vertex()

    register_button_actions_gpencil_edit()

    register_button_actions_gpencil_weight()

    register_button_actions_gpencil_vertex()

    register_button_actions_greasepencil_edit()

    register_button_actions_greasepencil_weight()

    register_button_actions_greasepencil_vertex()

    register_button_actions_armature_edit()

    register_button_actions_curve_edit()

    register_button_actions_lattice()

    # 注册键位映射
    keymap.register()

def unregister():
    # 注销右键添加到设置面板
    unregister_right_click_add_setting_panel()

    # 注销视图右键菜单功能
    unregister_right_click_global_view_actions()

    # 注销右键菜单功能
    unregister_right_click_add_global()

    # 注销 物体模式——添加到右键
    unregister_right_click_add_object()

    unregister_right_click_add_greasepencil_vertex()

    unregister_right_click_add_greasepencil_weight()

    unregister_right_click_add_greasepencil_edit()

    unregister_right_click_add_gpencil_vertex()

    unregister_right_click_add_gpencil_weight()

    unregister_right_click_add_gpencil_edit()

    unregister_right_click_add_mesh_vertex()
    # 注销 “网格编辑”模式
    unregister_right_click_add_mesh_edit()

    unregister_right_click_add_curve_edit()

    # 注销“骨架编辑”
    unregister_right_click_add_armature_edit()

    unregister_right_click_add_lattice_edit()

    # 注销“骨架姿态”
    unregister_right_click_add_armature_pose()
    
    # 注销模式监测功能
    unregister_operator_typeandmode_name_mode()

    unregister_show_switch_notice()

    unregister_button_actions_lattice()

    unregister_button_actions_curve_edit()

    unregister_button_actions_armature_edit()

    unregister_button_actions_greasepencil_vertex()

    unregister_button_actions_greasepencil_weight()

    unregister_button_actions_greasepencil_edit()

    unregister_button_actions_gpencil_vertex()

    unregister_button_actions_gpencil_weight()

    unregister_button_actions_gpencil_edit()

    unregister_button_actions_mesh_vertex()

    #网格编辑模式
    unregister_button_actions_mesh_edit()

    # 物体模式—“物体”菜单
    unregister_button_actions_object()

    # “选择”菜单功能项
    unregister_button_actions_global_select_menu()

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

    # 注销所有QUICK_POPUP_MENU_OT_*类
    bpy.utils.unregister_class(QUICK_POPUP_MENU_OT_two_latticeedit)
    bpy.utils.unregister_class(QUICK_POPUP_MENU_OT_two_fontedit)
    bpy.utils.unregister_class(QUICK_POPUP_MENU_OT_two_metaedit)
    bpy.utils.unregister_class(QUICK_POPUP_MENU_OT_two_surfaceedit)
    bpy.utils.unregister_class(QUICK_POPUP_MENU_OT_two_curveedit)
    bpy.utils.unregister_class(QUICK_POPUP_MENU_OT_two_armaturepose)
    bpy.utils.unregister_class(QUICK_POPUP_MENU_OT_two_armatureedit)
    bpy.utils.unregister_class(QUICK_POPUP_MENU_OT_two_greasepencilweight)
    bpy.utils.unregister_class(QUICK_POPUP_MENU_OT_two_greasepencilvertex)
    bpy.utils.unregister_class(QUICK_POPUP_MENU_OT_two_greasepencilsculpt)
    bpy.utils.unregister_class(QUICK_POPUP_MENU_OT_two_greasepencilpaint)
    bpy.utils.unregister_class(QUICK_POPUP_MENU_OT_two_greasepenciledit)
    bpy.utils.unregister_class(QUICK_POPUP_MENU_OT_two_gpencilweight)
    bpy.utils.unregister_class(QUICK_POPUP_MENU_OT_two_gpencilvertex)
    bpy.utils.unregister_class(QUICK_POPUP_MENU_OT_two_gpencilsculpt)
    bpy.utils.unregister_class(QUICK_POPUP_MENU_OT_two_gpencilpaint)
    bpy.utils.unregister_class(QUICK_POPUP_MENU_OT_two_gpenciledit)
    bpy.utils.unregister_class(QUICK_POPUP_MENU_OT_two_meshweightpaint)
    bpy.utils.unregister_class(QUICK_POPUP_MENU_OT_two_meshvertexpaint)
    bpy.utils.unregister_class(QUICK_POPUP_MENU_OT_two_meshtexture)
    bpy.utils.unregister_class(QUICK_POPUP_MENU_OT_two_meshsculpt)
    bpy.utils.unregister_class(QUICK_POPUP_MENU_OT_two_meshedit)
    bpy.utils.unregister_class(QUICK_POPUP_MENU_OT_two_object)

    bpy.utils.unregister_class(QUICK_POPUP_MENU_OT_one_latticeedit)
    bpy.utils.unregister_class(QUICK_POPUP_MENU_OT_one_fontedit)
    bpy.utils.unregister_class(QUICK_POPUP_MENU_OT_one_metaedit)
    bpy.utils.unregister_class(QUICK_POPUP_MENU_OT_one_surfaceedit)
    bpy.utils.unregister_class(QUICK_POPUP_MENU_OT_one_curveedit)
    bpy.utils.unregister_class(QUICK_POPUP_MENU_OT_one_armaturepose)
    bpy.utils.unregister_class(QUICK_POPUP_MENU_OT_one_armatureedit)
    bpy.utils.unregister_class(QUICK_POPUP_MENU_OT_one_greasepencilweight)
    bpy.utils.unregister_class(QUICK_POPUP_MENU_OT_one_greasepencilvertex)
    bpy.utils.unregister_class(QUICK_POPUP_MENU_OT_one_greasepencilsculpt)
    bpy.utils.unregister_class(QUICK_POPUP_MENU_OT_one_greasepencilpaint)
    bpy.utils.unregister_class(QUICK_POPUP_MENU_OT_one_greasepenciledit)
    bpy.utils.unregister_class(QUICK_POPUP_MENU_OT_one_gpencilweight)
    bpy.utils.unregister_class(QUICK_POPUP_MENU_OT_one_gpencilvertex)
    bpy.utils.unregister_class(QUICK_POPUP_MENU_OT_one_gpencilsculpt)
    bpy.utils.unregister_class(QUICK_POPUP_MENU_OT_one_gpencilpaint)
    bpy.utils.unregister_class(QUICK_POPUP_MENU_OT_one_gpenciledit)
    bpy.utils.unregister_class(QUICK_POPUP_MENU_OT_one_meshweightpaint)
    bpy.utils.unregister_class(QUICK_POPUP_MENU_OT_one_meshvertexpaint)
    bpy.utils.unregister_class(QUICK_POPUP_MENU_OT_one_meshtexture)
    bpy.utils.unregister_class(QUICK_POPUP_MENU_OT_one_meshsculpt)
    bpy.utils.unregister_class(QUICK_POPUP_MENU_OT_one_meshedit)
    bpy.utils.unregister_class(QUICK_POPUP_MENU_OT_one_object)

    # 注销所有Operator类
    bpy.utils.unregister_class(CALLOUT_QUICK_MENU_OT_two)
    bpy.utils.unregister_class(CALLOUT_QUICK_MENU_OT_one)
    bpy.utils.unregister_class(GRAB_SCALE_ROTATE_OT_Switch_action)
    bpy.utils.unregister_class(GRAB_SCALE_ROTATE_OT_Switch)
    bpy.utils.unregister_class(MODE_OT_to_object_and_select)
    bpy.utils.unregister_class(MODE_OT_Transfer)
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
