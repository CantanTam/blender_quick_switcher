import bpy

class BUTTON_ACTION_OT_switch_orientation_menu(bpy.types.Operator):
    bl_idname = "button.action_switch_orientation_menu"
    bl_label = "切换坐标系"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        #bpy.ops.wm.context_menu_enum(data_path="scene.transform_orientation_slots[0].type")
        bpy.ops.wm.call_panel(name="VIEW3D_PT_transform_orientations")
        return {'FINISHED'}

class BUTTON_ACTION_OT_orientation_to_global(bpy.types.Operator):
    bl_idname = "button.action_orientation_to_global"
    bl_label = "全局坐标系"
    bl_description = "全局坐标系"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.context.scene.transform_orientation_slots[0].type = 'GLOBAL'
        return {'FINISHED'}
    
class BUTTON_ACTION_OT_orientation_to_local(bpy.types.Operator):
    bl_idname = "button.action_orientation_to_local"
    bl_label = "局部坐标系"
    bl_description = "局部坐标系"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.context.scene.transform_orientation_slots[0].type = 'LOCAL'
        return {'FINISHED'}

class BUTTON_ACTION_OT_orientation_to_normal(bpy.types.Operator):
    bl_idname = "button.action_orientation_to_normal"
    bl_label = "法向坐标系"
    bl_description = "法向坐标系"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.context.scene.transform_orientation_slots[0].type = 'NORMAL'
        return {'FINISHED'}

class BUTTON_ACTION_OT_orientation_to_gimbal(bpy.types.Operator):
    bl_idname = "button.action_orientation_to_gimbal"
    bl_label = "万向坐标系"
    bl_description = "万向坐标系"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.context.scene.transform_orientation_slots[0].type = 'GIMBAL'
        return {'FINISHED'}

class BUTTON_ACTION_OT_orientation_to_view(bpy.types.Operator):
    bl_idname = "button.action_orientation_to_view"
    bl_label = "视图坐标系"
    bl_description = "视图坐标系"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.context.scene.transform_orientation_slots[0].type = 'VIEW'
        return {'FINISHED'}

class BUTTON_ACTION_OT_orientation_to_cursor(bpy.types.Operator):
    bl_idname = "button.action_orientation_to_cursor"
    bl_label = "游标坐标系"
    bl_description = "游标坐标系"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.context.scene.transform_orientation_slots[0].type = 'CURSOR'
        return {'FINISHED'}

class BUTTON_ACTION_OT_orientation_to_parent(bpy.types.Operator):
    bl_idname = "button.action_orientation_to_parent"
    bl_label = "父级坐标系"
    bl_description = "父级坐标系"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.context.scene.transform_orientation_slots[0].type = 'PARENT'
        return {'FINISHED'}
    
classes = (
    BUTTON_ACTION_OT_switch_orientation_menu,
    BUTTON_ACTION_OT_orientation_to_global,
    BUTTON_ACTION_OT_orientation_to_local,
    BUTTON_ACTION_OT_orientation_to_normal,
    BUTTON_ACTION_OT_orientation_to_gimbal,
    BUTTON_ACTION_OT_orientation_to_view,
    BUTTON_ACTION_OT_orientation_to_cursor,
    BUTTON_ACTION_OT_orientation_to_parent,
)

def register():
    for cls in classes:
        bpy.utils.register_class(cls)

def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)
