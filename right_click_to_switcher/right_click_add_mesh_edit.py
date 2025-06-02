import bpy
from .. import ADDON_NAME

def draw_add_to_switcher_meshedit(self, context):

    show_switcher = bpy.context.preferences.addons[ADDON_NAME].preferences.to_show_to_switcher
    if not show_switcher:
        return
    
    op = getattr(context, "operator", None) or getattr(context, "button_operator", None)

    if op and op.bl_rna.identifier == "TRANSFORM_OT_shrink_fatten":
        layout = self.layout
        layout.separator()
        layout.operator("call.add_to_switcher_menu", text="\"法向缩放\"⟶Switcher", icon='PLUS').action = 'button.action_meshedit_transform_shrink_fatten'















def global_select_meshedit_moreless_menu_to_switcher(self, context):
    show_switcher = bpy.context.preferences.addons[ADDON_NAME].preferences.to_show_to_switcher
    if not show_switcher:
        return
    self.layout.separator()
    self.layout.operator("call.add_to_switcher_menu", text="\"加选/减选(菜单)\"⟶Switcher", icon='FORCE_CHARGE').action = 'button.action_call_global_select_more_or_less_menu'







def global_select_meshedit_select_linked_menu_to_switcher(self, context):
    show_switcher = bpy.context.preferences.addons[ADDON_NAME].preferences.to_show_to_switcher
    if not show_switcher:
        return
    self.layout.separator()
    self.layout.operator("call.add_to_switcher_menu", text="\"选择相连(菜单)\"⟶Switcher", icon='LINK_BLEND').action = 'button.action_global_select_select_linked'


def register():
    bpy.types.UI_MT_button_context_menu.append(draw_add_to_switcher_meshedit)
    bpy.types.VIEW3D_MT_edit_mesh_select_more_less.append(global_select_meshedit_moreless_menu_to_switcher)
    bpy.types.VIEW3D_MT_edit_mesh_select_linked.append(global_select_meshedit_select_linked_menu_to_switcher)


def unregister():
    bpy.types.VIEW3D_MT_edit_mesh_select_linked.remove(global_select_meshedit_select_linked_menu_to_switcher)
    bpy.types.VIEW3D_MT_edit_mesh_select_more_less.remove(global_select_meshedit_moreless_menu_to_switcher)
    bpy.types.UI_MT_button_context_menu.remove(draw_add_to_switcher_meshedit)