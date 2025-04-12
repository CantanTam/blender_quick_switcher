import bpy

class VERTEX_EDGE_FACE_OT_Switch(bpy.types.Operator):
    bl_idname = "switch.vertex_edge_face"
    bl_label = "切换点/线/面"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self,context):
        if bpy.context.active_object.type and context.mode == 'EDIT_MESH':
            select_mode = context.tool_settings.mesh_select_mode
            if select_mode[2]:  # 面模式 -> 边模式
                context.tool_settings.mesh_select_mode = (False, True, False)
            elif select_mode[1]:  # 边模式 -> 顶点模式
                context.tool_settings.mesh_select_mode = (True, False, False)
            else:  # 顶点模式 -> 面模式
                context.tool_settings.mesh_select_mode = (False, False, True)
            return {'FINISHED'}
        return {'CANCELLED'}
