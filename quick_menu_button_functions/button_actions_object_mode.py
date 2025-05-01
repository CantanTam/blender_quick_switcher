import bpy

# 以下是“物体”模式当中“物体”菜单特有的一些选项

# 变换——缩放纹理空间
class BUTTON_ACTION_OT_object_object_transform_transform_mode_align(bpy.types.Operator):
    bl_idname = "button.action_object_object_transform_transform_mode_align"
    bl_label = "缩放纹理空间"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.ops.transform.transform('INVOKE_DEFAULT', mode='ALIGN')
        return {'FINISHED'}
    
# 物体模式“关联复制 Alt D”按钮功能
class BUTTON_ACTION_OT_object_object_duplicate_move_linked(bpy.types.Operator):
    bl_idname = "button.action_object_object_duplicate_move_linked"
    bl_label = "关联复制"
    bl_description = "快捷键 Alt D"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.ops.object.duplicate_move_linked('INVOKE_DEFAULT')
        return {'FINISHED'}
    
