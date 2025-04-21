import bpy

class BUTTON_ACTION_OT_grab(bpy.types.Operator):
    bl_idname = "button.action_grab"
    bl_label = "移动"
    bl_description = "移动"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.ops.transform.translate('INVOKE_DEFAULT')
        return {'FINISHED'}
