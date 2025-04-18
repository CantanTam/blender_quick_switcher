import bpy

# 所有操作类列表
_classes = []

# 构建空函数、空名称、空图标按钮，替代
class BUTTON_FUNCTION_OT_noaction(bpy.types.Operator):
    bl_idname = "button.function_no_action"
    bl_label = ""
    bl_description = ""
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self,context):
        return {'CANCELLED'}
    
_classes.append(BUTTON_FUNCTION_OT_noaction)

class BUTTON_FUNCTION_OT_noactiontwo(bpy.types.Operator):
    bl_idname = "button.function_no_action_two"
    bl_label = ""
    bl_description = ""
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self,context):
        return {'FINISHED'}
    
_classes.append(BUTTON_FUNCTION_OT_noactiontwo)

def register():
    for cls in _classes:
        bpy.utils.register_class(cls)

def unregister():
    for cls in reversed(_classes):
        bpy.utils.unregister_class(cls)
