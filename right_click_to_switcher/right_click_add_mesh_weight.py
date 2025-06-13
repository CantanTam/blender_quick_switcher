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
        layout.operator("call.add_to_switcher_menu", text="\"自动按骨骼指定\"⟶Switcher", icon='PLUS').action = 'action.meshweight_weight_from_bones_auto'
        layout.operator("call.add_to_switcher_menu", text="\"按骨骼封套指定\"⟶Switcher", icon='PLUS').action = 'action.meshweight_weight_from_bones_envelope'

    elif op and op.bl_rna.identifier == "OBJECT_OT_vertex_group_normalize":
        layout = self.layout
        layout.separator()
        layout.operator("call.add_to_switcher_menu", text="\"规格化\"⟶Switcher", icon='PLUS').action = 'action.meshweight_object_vertex_group_normalize'

    elif op and op.bl_rna.identifier == "OBJECT_OT_vertex_group_mirror":
        layout = self.layout
        layout.separator()
        layout.operator("call.add_to_switcher_menu", text="\"镜像\"⟶Switcher", icon='MOD_MIRROR').action = 'action.meshweight_object_vertex_group_mirror'





def register():
    bpy.types.UI_MT_button_context_menu.append(draw_add_to_switcher_meshweight)

def unregister():
    bpy.types.UI_MT_button_context_menu.remove(draw_add_to_switcher_meshweight)
