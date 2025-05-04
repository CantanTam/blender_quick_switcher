import bpy
from . show_switch_notice import show_notice

class VERTEX_EDGE_FACE_OT_Switch(bpy.types.Operator):
    bl_idname = "switch.vertex_edge_face"
    bl_label = "切换点/线/面"
    bl_description = "面→线→点方向快速切换"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self,context):
        # 防止在场景无物体对象的情况下运行报错
        if not bpy.context.active_object:
            return {'CANCELLED'}
        
        else:
            if bpy.context.active_object.type and context.mode == 'EDIT_MESH':
                select_mode = context.tool_settings.mesh_select_mode
                if select_mode[2]:  # 面模式 -> 边模式
                    context.tool_settings.mesh_select_mode = (False, True, False)
                    show_notice("rect.png")
                elif select_mode[1]:  # 边模式 -> 顶点模式
                    context.tool_settings.mesh_select_mode = (True, False, False)
                    show_notice("path1.png")
                else:  # 顶点模式 -> 面模式
                    context.tool_settings.mesh_select_mode = (False, False, True)
                return {'FINISHED'}
            
        return {'FINISHED'}
