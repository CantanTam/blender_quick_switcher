import bpy
from .. import ADDON_NAME

def draw_add_to_switcher_meshvertex(self, context):

    show_switcher = bpy.context.preferences.addons[ADDON_NAME].preferences.to_show_to_switcher
    if not show_switcher:
        return
    
    op = getattr(context, "operator", None) or getattr(context, "button_operator", None)

    if op and op.bl_rna.identifier == "PAINT_OT_vertex_color_set":
        layout = self.layout
        layout.separator()
        layout.operator("call.add_to_switcher_menu", text="\"设置顶点色\"⟶Switcher", icon='PLUS').action = 'action.meshvertex_vertex_color_set'

    elif op and op.bl_rna.identifier == "PAINT_OT_vertex_color_smooth":
        layout = self.layout
        layout.separator()
        layout.operator("call.add_to_switcher_menu", text="\"平滑顶点色\"⟶Switcher", icon='PLUS').action = 'action.meshvertex_vertex_color_smooth'

    elif op and op.bl_rna.identifier == "PAINT_OT_vertex_color_dirt":
        layout = self.layout
        layout.separator()
        layout.operator("call.add_to_switcher_menu", text="\"脏旧顶点色\"⟶Switcher", icon='PLUS').action = 'action.meshvertex_vertex_color_dirt'

    elif op and op.bl_rna.identifier == "PAINT_OT_vertex_color_from_weight":
        layout = self.layout
        layout.separator()
        layout.operator("call.add_to_switcher_menu", text="\"来自权重的顶点色\"⟶Switcher", icon='PLUS').action = 'action.meshvertex_vertex_color_from_weight'

    elif op and op.bl_rna.identifier == "PAINT_OT_vertex_color_invert":
        layout = self.layout
        layout.separator()
        layout.operator("call.add_to_switcher_menu", text="\"反转\"⟶Switcher", icon='PLUS').action = 'action.meshvertex_vertex_color_invert'

    elif op and op.bl_rna.identifier == "PAINT_OT_vertex_color_levels":
        layout = self.layout
        layout.separator()
        layout.operator("call.add_to_switcher_menu", text="\"层级\"⟶Switcher", icon='PLUS').action = 'action.meshvertex_vertex_color_levels'

    elif op and op.bl_rna.identifier == "PAINT_OT_vertex_color_hsv":
        layout = self.layout
        layout.separator()
        layout.operator("call.add_to_switcher_menu", text="\"色相/饱和度/明度\"⟶Switcher", icon='PLUS').action = 'action.meshvertex_vertex_color_hsv'

    elif op and op.bl_rna.identifier == "PAINT_OT_vertex_color_brightness_contrast":
        layout = self.layout
        layout.separator()
        layout.operator("call.add_to_switcher_menu", text="\"亮度/对比度\"⟶Switcher", icon='PLUS').action = 'action.meshvertex_vertex_color_brightness_contrast'
    # 4.3 版本有效
    elif op and op.bl_rna.identifier == "PAINT_OT_sample_color":
        layout = self.layout
        layout.separator()
        layout.operator("call.add_to_switcher_menu", text="\"色彩取样\"⟶Switcher", icon='PLUS').action = 'action.paint_sample_color'




def register():
    bpy.types.UI_MT_button_context_menu.append(draw_add_to_switcher_meshvertex)

def unregister():
    bpy.types.UI_MT_button_context_menu.remove(draw_add_to_switcher_meshvertex)
