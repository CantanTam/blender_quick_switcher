import bpy

# 变换——球形化
class BUTTON_ACTION_OT_transform_tosphere(bpy.types.Operator):
    bl_idname = "button.action_transform_tosphere"
    bl_label = "球形化"
    bl_description = "快捷键 Shift Alt S"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.ops.transform.tosphere('INVOKE_DEFAULT')
        return {'FINISHED'}
    
# 变换——切变
class BUTTON_ACTION_OT_transform_shear(bpy.types.Operator):
    bl_idname = "button.action_transform_shear"
    bl_label = "切变"
    bl_description = "快捷键 Ctrl Shift Alt S"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.ops.transform.shear('INVOKE_DEFAULT')
        return {'FINISHED'}
    
# 变换——弯曲
class BUTTON_ACTION_OT_transform_bend(bpy.types.Operator):
    bl_idname = "button.action_transform_bend"
    bl_label = "弯曲"
    bl_description = "快捷键 Shift W"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.ops.transform.bend('INVOKE_DEFAULT')
        return {'FINISHED'}
