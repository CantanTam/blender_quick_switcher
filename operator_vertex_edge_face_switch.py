import bpy
from . show_switch_notice import show_notice

class VERTEX_EDGE_FACE_OT_Switch(bpy.types.Operator):
    bl_idname = "switch.vertex_edge_face"
    bl_label = "切换点/线/面"
    bl_description = "面→线→点方向快速切换"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self,context):
        typeandmode = bpy.context.active_object.type+bpy.context.active_object.mode
        # 防止在场景无物体对象的情况下运行报错
        if not bpy.context.active_object:
            return {'CANCELLED'}
        
        elif typeandmode == "MESHEDIT":
            select_mode = context.tool_settings.mesh_select_mode
            if select_mode[2]:  # 面模式 -> 边模式
                context.tool_settings.mesh_select_mode = (False, True, False)
                show_notice("MESHEDIT_EDGE.png")
            elif select_mode[1]:  # 边模式 -> 顶点模式
                context.tool_settings.mesh_select_mode = (True, False, False)
                show_notice("MESHEDIT_VERTEX.png")
            else:  # 顶点模式 -> 面模式
                context.tool_settings.mesh_select_mode = (False, False, True)
                show_notice("MESHEDIT_FACE.png")

        elif typeandmode in {"MESHVERTEX_PAINT","MESHWEIGHT_PAINT"}:
            if bpy.context.active_object.data.use_paint_mask:
                bpy.context.active_object.data.use_paint_mask = False
                bpy.context.active_object.data.use_paint_mask_vertex = False
                show_notice("MESHVERTEX_NONE.png")
            elif bpy.context.active_object.data.use_paint_mask == False and \
                bpy.context.active_object.data.use_paint_mask_vertex == False:
                bpy.context.active_object.data.use_paint_mask_vertex = True
                show_notice("MESHVERTEX_VERTEX.png")
            elif bpy.context.active_object.data.use_paint_mask_vertex == True:
                bpy.context.active_object.data.use_paint_mask = True
                show_notice("MESHVERTEX_FACE.png")

        elif typeandmode == "MESHTEXTURE_PAINT":
            bpy.context.active_object.data.use_paint_mask = not bpy.context.active_object.data.use_paint_mask
            if bpy.context.active_object.data.use_paint_mask == True:
                show_notice("MESHTEXTURE_FACE.png")
            else:
                show_notice("MESHTEXTURE_NONE.png")
        return {'FINISHED'}
