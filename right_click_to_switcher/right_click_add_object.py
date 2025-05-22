import bpy
from .. import ADDON_NAME

def draw_add_to_switcher_object(self, context):
    show_switcher = bpy.context.preferences.addons[ADDON_NAME].preferences.to_show_to_switcher
    if not show_switcher:
        return
    
    op = getattr(context, "operator", None) or getattr(context, "button_operator", None)

    if op and op.bl_rna.identifier == "OBJECT_OT_select_by_type":
        layout = self.layout
        layout.separator()
        layout.operator("call.add_to_switcher_menu", text="\"按类型全选(菜单)\"添加到Switcher", icon='PRESET').action = 'button.action_object_select_select_by_type_menu'

    elif op and op.bl_rna.identifier == "OBJECT_OT_select_camera":
        layout = self.layout
        layout.separator()
        layout.operator("call.add_to_switcher_menu", text="\"选择活动摄像机\"添加到Switcher", icon='OUTLINER_OB_CAMERA').action = 'object.select_camera'
    






def register():
    bpy.types.UI_MT_button_context_menu.append(draw_add_to_switcher_object)

def unregister():
    bpy.types.UI_MT_button_context_menu.remove(draw_add_to_switcher_object)

