import bpy

class BUTTON_ACTION_OT_gpenciledit_transform_shrink_fatten(bpy.types.Operator):
    bl_idname = "button.action_gpenciledit_transform_shrink_fatten"
    bl_label = "法向缩放"
    bl_description = "快捷键 Alt S"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.ops.transform.transform('INVOKE_DEFAULT',mode='GPENCIL_SHRINKFATTEN')
        return {'FINISHED'}

class BUTTON_ACTION_OT_gpenciledit_layer_active_menu(bpy.types.Operator):
    bl_idname = "button.action_gpenciledit_layer_active_menu"
    bl_label = "活动层"
    bl_description = "快捷键 Y"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.ops.wm.call_menu(name="GPENCIL_MT_layer_active")
        return {'FINISHED'}
    
class BUTTON_ACTION_OT_gpenciledit_layer_add(bpy.types.Operator):
    bl_idname = "button.action_gpenciledit_layer_add"
    bl_label = "新建层"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.ops.gpencil.layer_add('INVOKE_DEFAULT', layer=-1)
        return {'FINISHED'}
    





classes = (
    BUTTON_ACTION_OT_gpenciledit_transform_shrink_fatten,
    BUTTON_ACTION_OT_gpenciledit_layer_active_menu,
    BUTTON_ACTION_OT_gpenciledit_layer_add,

)

def register():
    for cls in classes:
        bpy.utils.register_class(cls)

def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)