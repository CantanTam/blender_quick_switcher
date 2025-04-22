import bpy

class BUTTON_ACTION_OT_grab(bpy.types.Operator):
    bl_idname = "button.action_grab"
    bl_label = "移动"
    bl_description = "移动(G)"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.ops.transform.translate('INVOKE_DEFAULT')
        return {'FINISHED'}
    

class BUTTON_ACTION_OT_scale(bpy.types.Operator):
    bl_idname = "button.action_scale"
    bl_label = "缩放"
    bl_description = "缩放(S)"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.ops.transform.resize('INVOKE_DEFAULT')
        return {'FINISHED'}
    
class BUTTON_ACTION_OT_rotate(bpy.types.Operator):
    bl_idname = "button.action_rotate"
    bl_label = "旋转(R)"
    bl_description = "旋转(R)"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.ops.transform.rotate('INVOKE_DEFAULT')
        return {'FINISHED'}
