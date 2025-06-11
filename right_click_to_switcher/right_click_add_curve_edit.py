import bpy
from .. import ADDON_NAME

def draw_add_to_switcher_curveedit(self, context):
    show_switcher = bpy.context.preferences.addons[ADDON_NAME].preferences.to_show_to_switcher
    if not show_switcher:
        return
    
    op = getattr(context, "operator", None) or getattr(context, "button_operator", None)

    if op and op.bl_rna.identifier == "CURVE_OT_select_nth":
        layout = self.layout
        layout.separator()
        layout.operator("call.add_to_switcher_menu", text="\"间隔式弃选\"⟶Switcher", icon='PLUS').action = 'button.action_curveedit_select_nth'

    elif op and op.bl_rna.identifier == "CURVE_OT_de_select_first":
        layout = self.layout
        layout.separator()
        layout.operator("call.add_to_switcher_menu", text="\"选中/弃选首点\"⟶Switcher", icon='PLUS').action = 'button.action_curveedit_select_first'

    elif op and op.bl_rna.identifier == "CURVE_OT_de_select_last":
        layout = self.layout
        layout.separator()
        layout.operator("call.add_to_switcher_menu", text="\"选中/弃选末点\"⟶Switcher", icon='PLUS').action = 'button.action_curveedit_select_last'

    elif op and op.bl_rna.identifier == "CURVE_OT_select_row":
        layout = self.layout
        layout.separator()
        layout.operator("call.add_to_switcher_menu", text="\"控制点行\"⟶Switcher", icon='PLUS').action = 'button.action_curveedit_select_row'

    elif op and op.bl_rna.identifier == "CURVE_OT_spin":
        layout = self.layout
        layout.separator()
        layout.operator("call.add_to_switcher_menu", text="\"旋绕\"⟶Switcher", icon='PLUS').action = 'button.action_curveedit_spin'

    elif op and op.bl_rna.identifier == "CURVE_OT_split":
        layout = self.layout
        layout.separator()
        layout.operator("call.add_to_switcher_menu", text="\"拆分\"⟶Switcher", icon='EVENT_Y').action = 'button.action_curveedit_split'

    elif op and op.bl_rna.identifier == "CURVE_OT_separate":
        layout = self.layout
        layout.separator()
        layout.operator("call.add_to_switcher_menu", text="\"分离\"⟶Switcher", icon='EVENT_P').action = 'button.action_curveedit_separate'

    elif op and op.bl_rna.identifier == "CURVE_OT_cyclic_toggle":
        layout = self.layout
        layout.separator()
        layout.operator("call.add_to_switcher_menu", text="\"切换循环\"⟶Switcher", icon='PLUS').action = 'button.action_curveedit_cyclic_toggle'

    elif op and op.bl_rna.identifier == "CURVE_OT_spline_type_set":
        layout = self.layout
        layout.separator()
        layout.operator("call.add_to_switcher_menu", text="\"设置样条类型\"⟶Switcher", icon='PRESET').action = 'button.action_curveedit_spline_type_set'

    elif op and op.bl_rna.identifier == "CURVE_OT_decimate":
        layout = self.layout
        layout.separator()
        layout.operator("call.add_to_switcher_menu", text="\"精简曲线\"⟶Switcher", icon='PLUS').action = 'button.action_curveedit_decimate'



def curveedit_transform_mode_curve_shrinkfatten_to_switcher(self, context):
    show_switcher = bpy.context.preferences.addons[ADDON_NAME].preferences.to_show_to_switcher
    if not show_switcher:
        return
    self.layout.separator()
    self.layout.operator("call.add_to_switcher_menu", text="\"半径\"⟶Switcher", icon='PLUS').action = 'button.action_transform_transform_mode_curve_shrinkfatten'

def curveedit_curve_clean_menu_to_switcher(self, context):
    show_switcher = bpy.context.preferences.addons[ADDON_NAME].preferences.to_show_to_switcher
    if not show_switcher:
        return
    self.layout.separator()
    self.layout.operator("call.add_to_switcher_menu", text="\"清理\"⟶Switcher", icon='PRESET').action = 'button.action_curveedit_curve_clean_menu'






def register():
    bpy.types.UI_MT_button_context_menu.append(draw_add_to_switcher_curveedit)
    bpy.types.VIEW3D_MT_transform.append(curveedit_transform_mode_curve_shrinkfatten_to_switcher)
    bpy.types.VIEW3D_MT_edit_curve_clean.append(curveedit_curve_clean_menu_to_switcher)

def unregister():
    bpy.types.VIEW3D_MT_edit_curve_clean.remove(curveedit_curve_clean_menu_to_switcher)
    bpy.types.UI_MT_button_context_menu.remove(draw_add_to_switcher_curveedit)
    bpy.types.VIEW3D_MT_transform.remove(curveedit_transform_mode_curve_shrinkfatten_to_switcher)
