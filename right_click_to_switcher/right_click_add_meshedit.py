import bpy
from .. import ADDON_NAME

def global_select_meshedit_moreless_menu_to_switcher(self, context):
    show_switcher = bpy.context.preferences.addons[ADDON_NAME].preferences.to_show_to_switcher
    if not show_switcher:
        return
    self.layout.separator()
    self.layout.operator("call.add_to_switcher_menu", text="\"加选/减选(菜单)\"添加到Switcher", icon='FORCE_CHARGE').action = 'button.action_call_global_select_more_or_less_menu'
    self.layout.operator("call.add_to_switcher_menu", text="添加分隔符到Switcher", icon='REMOVE').action = 'SEPARATOR'



def register():
    bpy.types.VIEW3D_MT_edit_mesh_select_more_less.append(global_select_meshedit_moreless_menu_to_switcher)


def unregister():
    bpy.types.VIEW3D_MT_edit_mesh_select_more_less.remove(global_select_meshedit_moreless_menu_to_switcher)
