import bpy

class BUTTON_ACTION_OT_gpenciledit_transform_shrink_fatten(bpy.types.Operator):
    bl_idname = "button.action_gpenciledit_transform_shrink_fatten"
    bl_label = "法向缩放"
    bl_description = "快捷键 Alt S"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.ops.transform.transform('INVOKE_DEFAULT',mode='GPENCIL_SHRINKFATTEN')
        return {'FINISHED'}





classes = (
    BUTTON_ACTION_OT_gpenciledit_transform_shrink_fatten,

)

def register():
    for cls in classes:
        bpy.utils.register_class(cls)

def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)