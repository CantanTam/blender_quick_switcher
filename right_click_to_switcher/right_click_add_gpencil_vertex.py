import bpy
from .. import ADDON_NAME

def draw_add_to_switcher_gpencilvertex(self, context):

    show_switcher = bpy.context.preferences.addons[ADDON_NAME].preferences.to_show_to_switcher
    if not show_switcher:
        return
    
    op = getattr(context, "operator", None) or getattr(context, "button_operator", None)

    if op and op.bl_rna.identifier == "GPENCIL_OT_select_vertex_color":
        layout = self.layout
        layout.separator()
        layout.operator("call.add_to_switcher_menu", text="\"颜色属性\"⟶Switcher", icon='PLUS').action = 'button.action_gpencilvertex_select_vertex_color'

    elif op and op.bl_rna.identifier == "GPENCIL_OT_vertex_color_set":
        layout = self.layout
        layout.separator()
        layout.operator("call.add_to_switcher_menu", text="\"设置颜色属性\"⟶Switcher", icon='PLUS').action = 'button.action_gpencilvertex_vertex_color_set'

    elif op and op.bl_rna.identifier == "GPENCIL_OT_stroke_reset_vertex_color":
        layout = self.layout
        layout.separator()
        layout.operator("call.add_to_switcher_menu", text="\"重置顶点色\"⟶Switcher", icon='PLUS').action = 'button.action_gpencilvertex_stroke_reset_vertex_color'

    elif op and op.bl_rna.identifier == "GPENCIL_OT_vertex_color_invert":
        layout = self.layout
        layout.separator()
        layout.operator("call.add_to_switcher_menu", text="\"反转\"⟶Switcher", icon='PLUS').action = 'button.action_gpencilvertex_vertex_color_invert'

    elif op and op.bl_rna.identifier == "GPENCIL_OT_vertex_color_levels":
        layout = self.layout
        layout.separator()
        layout.operator("call.add_to_switcher_menu", text="\"层级\"⟶Switcher", icon='PLUS').action = 'button.action_gpencilvertex_vertex_color_levels'

    elif op and op.bl_rna.identifier == "GPENCIL_OT_vertex_color_hsv":
        layout = self.layout
        layout.separator()
        layout.operator("call.add_to_switcher_menu", text="\"色相/饱和度/明度\"⟶Switcher", icon='PLUS').action = 'button.action_gpencilvertex_vertex_color_hsv'

    elif op and op.bl_rna.identifier == "GPENCIL_OT_vertex_color_brightness_contrast":
        layout = self.layout
        layout.separator()
        layout.operator("call.add_to_switcher_menu", text="\"亮度/对比度\"⟶Switcher", icon='PLUS').action = 'button.action_gpencilvertex_brightness_contrast'








def register():
    bpy.types.UI_MT_button_context_menu.append(draw_add_to_switcher_gpencilvertex)

def unregister():
    bpy.types.UI_MT_button_context_menu.remove(draw_add_to_switcher_gpencilvertex)
