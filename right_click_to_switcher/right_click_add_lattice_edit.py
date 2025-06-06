import bpy
from .. import ADDON_NAME

def draw_add_to_switcher_lattice(self, context):

    show_switcher = bpy.context.preferences.addons[ADDON_NAME].preferences.to_show_to_switcher
    if not show_switcher:
        return
    
    op = getattr(context, "operator", None) or getattr(context, "button_operator", None)

    if op and op.bl_rna.identifier == "LATTICE_OT_flip":
        layout = self.layout
        layout.separator()
        layout.operator("call.add_to_switcher_menu", text="\"反转(免畸变)(菜单)\"⟶Switcher", icon='PRESET').action = 'button.action_call_latticeedit_flip_menu'

    elif op and op.bl_rna.identifier == "LATTICE_OT_make_regular":
        layout = self.layout
        layout.separator()
        layout.operator("call.add_to_switcher_menu", text="\"均匀分布\"⟶Switcher", icon='PLUS').action = 'button.action_latticeedit_make_regular'






def register():
    bpy.types.UI_MT_button_context_menu.append(draw_add_to_switcher_lattice)

def unregister():
    bpy.types.UI_MT_button_context_menu.remove(draw_add_to_switcher_lattice)
