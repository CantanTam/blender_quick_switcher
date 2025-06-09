import bpy
from .. import ADDON_NAME

def draw_add_to_switcher_greasepencilweight(self, context):

    show_switcher = bpy.context.preferences.addons[ADDON_NAME].preferences.to_show_to_switcher
    if not show_switcher:
        return
    
    op = getattr(context, "operator", None) or getattr(context, "button_operator", None)

    if op and op.bl_rna.identifier == "GREASE_PENCIL_OT_vertex_group_normalize_all":
        layout = self.layout
        layout.separator()
        layout.operator("call.add_to_switcher_menu", text="\"全部规格化\"⟶Switcher", icon='PLUS').action = 'button.action_greasepencilweight_vertex_group_normalize_all'

    elif op and op.bl_rna.identifier == "GREASE_PENCIL_OT_vertex_group_normalize":
        layout = self.layout
        layout.separator()
        layout.operator("call.add_to_switcher_menu", text="\"规格化\"⟶Switcher", icon='PLUS').action = 'button.action_greasepencilweight_vertex_group_normalize'

    elif op and op.bl_rna.identifier == "GREASE_PENCIL_OT_weight_invert":
        layout = self.layout
        layout.separator()
        layout.operator("call.add_to_switcher_menu", text="\"反转\"⟶Switcher", icon='PLUS').action = 'button.action_greasepencilweight_vertex_group_invert'

    elif op and op.bl_rna.identifier == "GREASE_PENCIL_OT_vertex_group_smooth":
        layout = self.layout
        layout.separator()
        layout.operator("call.add_to_switcher_menu", text="\"光滑\"⟶Switcher", icon='PLUS').action = 'button.action_greasepencilweight_vertex_group_smooth'

    elif op and op.bl_rna.identifier == "GREASE_PENCIL_OT_weight_sample":
        layout = self.layout
        layout.separator()
        layout.operator("call.add_to_switcher_menu", text="\"采样权重\"⟶Switcher", icon='PLUS').action = 'button.action_greasepencilweight_weight_sample'


def register():
    bpy.types.UI_MT_button_context_menu.append(draw_add_to_switcher_greasepencilweight)


def unregister():
    bpy.types.UI_MT_button_context_menu.remove(draw_add_to_switcher_greasepencilweight)
