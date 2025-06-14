import bpy
from .. import ADDON_NAME

def draw_add_to_switcher_meshsculpt(self, context):
    show_switcher = bpy.context.preferences.addons[ADDON_NAME].preferences.to_show_to_switcher
    if not show_switcher:
        return
    
    op = getattr(context, "operator", None) or getattr(context, "button_operator", None)

    if op and op.bl_rna.identifier == "SCULPT_OT_mesh_filter":
        layout = self.layout
        layout.separator()
        layout.operator("call.add_to_switcher_menu", text="\"球形化\"⟶Switcher", icon='SPHERE').action = 'action.meshsculpt_mesh_filter_sphere'

    elif op and op.bl_rna.identifier == "PAINT_OT_hide_show":
        layout = self.layout
        layout.separator()
        layout.operator("call.add_to_switcher_menu", text="\"框选隐藏\"⟶Switcher", icon='HIDE_ON').action = 'action.meshsculpt_paint_hide_show_hide'
        layout.operator("call.add_to_switcher_menu", text="\"框选显示\"⟶Switcher", icon='HIDE_OFF').action = 'action.meshsculpt_paint_hide_show_show'
        layout.operator("call.add_to_switcher_menu", text="\"显示全部\"⟶Switcher", icon='HIDE_OFF').action = 'action.meshsculpt_paint_hide_show_all'
        layout.operator("call.add_to_switcher_menu", text="\"隐藏遮罩作用项\"⟶Switcher", icon='HIDE_ON').action = 'action.meshsculpt_paint_hide_show_hide_masked'

    elif op and op.bl_rna.identifier == "SCULPT_OT_face_set_change_visibility":
        layout = self.layout
        layout.separator()
        layout.operator("call.add_to_switcher_menu", text="\"切换可见性\"⟶Switcher", icon='PLUS').action = 'action.meshsculpt_face_set_change_visibility_toggle_modal'
        layout.operator("call.add_to_switcher_menu", text="\"隐藏活动面组\"⟶Switcher", icon='PLUS').action = 'action.meshsculpt_face_set_change_visibility_hide_modal'

    elif op and op.bl_rna.identifier == "SCULPT_OT_face_set_invert_visibility":
        layout = self.layout
        layout.separator()
        layout.operator("call.add_to_switcher_menu", text="\"反转可见\"⟶Switcher", icon='PLUS').action = 'action.meshsculpt_face_set_invert_visibility'

    elif op and op.bl_rna.identifier == "SCULPT_OT_trim_box_gesture":
        layout = self.layout
        layout.separator()
        layout.operator("call.add_to_switcher_menu", text="\"框选修剪\"⟶Switcher", icon='PLUS').action = 'action.meshsculpt_trim_box_gesture_difference'
        layout.operator("call.add_to_switcher_menu", text="\"框选添加\"⟶Switcher", icon='PLUS').action = 'action.meshsculpt_trim_box_gesture_join'

    elif op and op.bl_rna.identifier == "SCULPT_OT_trim_lasso_gesture":
        layout = self.layout
        layout.separator()
        layout.operator("call.add_to_switcher_menu", text="\"套索修剪\"⟶Switcher", icon='PLUS').action = 'action.meshsculpt_trim_lasso_gesture_difference_modal'
        layout.operator("call.add_to_switcher_menu", text="\"套索添加\"⟶Switcher", icon='PLUS').action = 'action.meshsculpt_trim_lasso_gesture_join_modal'

    elif op and op.bl_rna.identifier == "SCULPT_OT_project_line_gesture":
        layout = self.layout
        layout.separator()
        layout.operator("call.add_to_switcher_menu", text="\"划线投影\"⟶Switcher", icon='PLUS').action = 'action.meshsculpt_project_line_gesture'

    elif op and op.bl_rna.identifier == "SCULPT_OT_face_set_edit":
        layout = self.layout
        layout.separator()
        layout.operator("call.add_to_switcher_menu", text="\"平顺位置\"⟶Switcher", icon='PLUS').action = 'action.meshsculpt_face_set_edit_position_modal'






def register():
    bpy.types.UI_MT_button_context_menu.append(draw_add_to_switcher_meshsculpt)

def unregister():
    bpy.types.UI_MT_button_context_menu.remove(draw_add_to_switcher_meshsculpt)
