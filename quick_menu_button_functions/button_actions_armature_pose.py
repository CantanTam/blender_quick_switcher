import bpy

# “选择”菜单
class ACTION_OT_pose_select_constraint_target(bpy.types.Operator):
    bl_idname = "action.pose_select_constraint_target"
    bl_label = "约束目标"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.ops.pose.select_constraint_target()
        return {'FINISHED'}

# “姿态”菜单
class ACTION_OT_pose_select_constraint_target(bpy.types.Operator):
    bl_idname = "action.pose_select_constraint_target"
    bl_label = "约束目标"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.ops.pose.select_constraint_target()
        return {'FINISHED'}





classes = (
    ACTION_OT_pose_select_constraint_target,


)

def register():
    for cls in classes:
        bpy.utils.register_class(cls)

def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)