import bpy
from .. import ADDON_NAME

def draw_add_to_switcher_gpencilweight(self, context):

    show_switcher = bpy.context.preferences.addons[ADDON_NAME].preferences.to_show_to_switcher
    if not show_switcher:
        return
    
    op = getattr(context, "operator", None) or getattr(context, "button_operator", None)

    if op and op.bl_rna.identifier == "GPENCIL_OT_vertex_group_normalize_all":
        layout = self.layout
        layout.separator()
        layout.operator("call.add_to_switcher_menu", text="\"全部规格化\"⟶Switcher", icon='PLUS').action = 'action.gpencilweight_vertex_group_normalize_all'

    elif op and op.bl_rna.identifier == "GPENCIL_OT_vertex_group_normalize":
        layout = self.layout
        layout.separator()
        layout.operator("call.add_to_switcher_menu", text="\"规格化\"⟶Switcher", icon='PLUS').action = 'action.gpencilweight_vertex_group_normalize'

    elif op and op.bl_rna.identifier == "GPENCIL_OT_vertex_group_invert":
        layout = self.layout
        layout.separator()
        layout.operator("call.add_to_switcher_menu", text="\"反转\"⟶Switcher", icon='PLUS').action = 'action.gpencilweight_vertex_group_invert'

    elif op and op.bl_rna.identifier == "GPENCIL_OT_vertex_group_smooth":
        layout = self.layout
        layout.separator()
        layout.operator("call.add_to_switcher_menu", text="\"光滑\"⟶Switcher", icon='PLUS').action = 'action.gpencilweight_vertex_group_smooth'




def gpencilweight_autoweights_menu_to_switcher(self, context):
    show_switcher = bpy.context.preferences.addons[ADDON_NAME].preferences.to_show_to_switcher
    if not show_switcher:
        return
    self.layout.separator()
    self.layout.operator("call.add_to_switcher_menu", text="\"生成权重(菜单)\"⟶Switcher", icon='PRESET').action = 'action.gpencilweight_gpencil_autoweights_menu'


def register():
    bpy.types.UI_MT_button_context_menu.append(draw_add_to_switcher_gpencilweight)
    if bpy.app.version <= (4, 2, 0):
        bpy.types.VIEW3D_MT_gpencil_autoweights.append(gpencilweight_autoweights_menu_to_switcher)

def unregister():
    if bpy.app.version <= (4, 2, 0):
        bpy.types.VIEW3D_MT_gpencil_autoweights.remove(gpencilweight_autoweights_menu_to_switcher)
    bpy.types.UI_MT_button_context_menu.remove(draw_add_to_switcher_gpencilweight)
