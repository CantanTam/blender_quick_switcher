import bpy

class BUTTON_ACTION_OT_transform_transform_mode_curve_shrinkfatten(bpy.types.Operator):
    bl_idname = "button.action_transform_transform_mode_curve_shrinkfatten"
    bl_label = "半径"
    bl_description = "快捷键 Alt S"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.ops.transform.transform('INVOKE_DEFAULT',mode='CURVE_SHRINKFATTEN')
        return {'FINISHED'}






classes = (
    BUTTON_ACTION_OT_transform_transform_mode_curve_shrinkfatten,

)

def register():
    for cls in classes:
        bpy.utils.register_class(cls)

def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)