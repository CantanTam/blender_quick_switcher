import bpy
from .. import ADDON_NAME

def draw_add_to_switcher_meshweight(self, context):
    show_switcher = bpy.context.preferences.addons[ADDON_NAME].preferences.to_show_to_switcher
    if not show_switcher:
        return
    
    op = getattr(context, "operator", None) or getattr(context, "button_operator", None)

    if op and op.bl_rna.identifier == "PAINT_OT_weight_from_bones":
        layout = self.layout
        layout.separator()
        layout.operator("call.add_to_switcher_menu", text="\"自动按骨骼指定\"⟶Switcher", icon='PLUS').action = 'button.action_meshweight_weight_from_bones_auto'
        layout.operator("call.add_to_switcher_menu", text="\"按骨骼封套指定\"⟶Switcher", icon='PLUS').action = 'button.action_meshweight_weight_from_bones_envelope'




def curveedit_transform_mode_curve_shrinkfatten_to_switcher(self, context):
    show_switcher = bpy.context.preferences.addons[ADDON_NAME].preferences.to_show_to_switcher
    if not show_switcher:
        return
    self.layout.separator()
    self.layout.operator("call.add_to_switcher_menu", text="\"半径\"⟶Switcher", icon='PLUS').action = 'button.action_transform_transform_mode_curve_shrinkfatten'




def register():
    bpy.types.UI_MT_button_context_menu.append(draw_add_to_switcher_meshweight)
    bpy.types.VIEW3D_MT_transform.append(curveedit_transform_mode_curve_shrinkfatten_to_switcher)
\
def unregister():
    bpy.types.UI_MT_button_context_menu.remove(draw_add_to_switcher_meshweight)
    bpy.types.VIEW3D_MT_transform.remove(curveedit_transform_mode_curve_shrinkfatten_to_switcher)
