import bpy
from .. import ADDON_NAME

def draw_add_to_switcher_gpenciledit(self, context):

    show_switcher = bpy.context.preferences.addons[ADDON_NAME].preferences.to_show_to_switcher
    if not show_switcher:
        return
    
    op = getattr(context, "operator", None) or getattr(context, "button_operator", None)

    if op and op.bl_rna.identifier == "GPENCIL_OT_layer_add":
        layout = self.layout
        layout.separator()
        layout.operator("call.add_to_switcher_menu", text="\"新建层\"⟶Switcher", icon='ADD').action = 'button.action_gpenciledit_layer_add'


def gpenciledit_layer_add_menu_to_switcher(self, context):
    show_switcher = bpy.context.preferences.addons[ADDON_NAME].preferences.to_show_to_switcher
    if not show_switcher:
        return
    self.layout.separator()
    self.layout.operator("call.add_to_switcher_menu", text="\"活动层(菜单)\"⟶Switcher", icon='PRESET').action = 'button.action_gpenciledit_layer_active_menu'



def register():
    bpy.types.UI_MT_button_context_menu.append(draw_add_to_switcher_gpenciledit)
    if bpy.app.version <= (4, 2, 0):
        bpy.types.GPENCIL_MT_layer_active.append(gpenciledit_layer_add_menu_to_switcher)

def unregister():
    if bpy.app.version <= (4, 2, 0):
        bpy.types.GPENCIL_MT_layer_active.remove(gpenciledit_layer_add_menu_to_switcher)
    bpy.types.UI_MT_button_context_menu.remove(draw_add_to_switcher_gpenciledit)
