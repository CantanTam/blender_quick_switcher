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


def register():
    bpy.types.UI_MT_button_context_menu.append(draw_add_to_switcher_meshsculpt)

def unregister():
    bpy.types.UI_MT_button_context_menu.remove(draw_add_to_switcher_meshsculpt)
