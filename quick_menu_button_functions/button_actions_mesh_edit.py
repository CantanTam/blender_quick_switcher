import bpy

# 以下是“物体”模式当中“物体”菜单特有的一些选项

# 变换——缩放纹理空间
class BUTTON_ACTION_OT_meshedit_select_select_all(bpy.types.Operator):
    bl_idname = "button.action_meshedit_select_select_all"
    bl_label = "全选"
    bl_description = "快捷键 A"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.ops.mesh.select_all(action='SELECT')
        return {'FINISHED'}
    
# 网络——变换——法向缩放
class BUTTON_ACTION_OT_meshedit_transform_shrink_fatten(bpy.types.Operator):
    bl_idname = "button.action_meshedit_transform_shrink_fatten"
    bl_label = "法向缩放"
    bl_description = "快捷键 Alt S"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.ops.transform.shrink_fatten('INVOKE_DEFAULT')
        return {'FINISHED'}





classes = (
    BUTTON_ACTION_OT_meshedit_select_select_all,
    BUTTON_ACTION_OT_meshedit_transform_shrink_fatten,

)

def register():
    for cls in classes:
        bpy.utils.register_class(cls)

def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)