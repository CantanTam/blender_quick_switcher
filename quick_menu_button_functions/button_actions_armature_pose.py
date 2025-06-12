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
class ACTION_OT_pose_pose_slide_menu(bpy.types.Operator):
    bl_idname = "action.pose_pose_slide_menu"
    bl_label = "间帧调整"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.ops.wm.call_menu(name="VIEW3D_MT_pose_slide")
        return {'FINISHED'}

class ACTION_OT_pose_push_rest(bpy.types.Operator):
    bl_idname = "action.pose_push_rest"
    bl_label = "从静置姿态推移姿态"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        try:
            bpy.ops.pose.push_rest('INVOKE_DEFAULT')
        except RuntimeError:
            self.report({'ERROR'}, "无法从静置姿态推移姿态")
            return {'CANCELLED'}
        return {'FINISHED'}

class ACTION_OT_pose_relax_rest(bpy.types.Operator):
    bl_idname = "action.pose_relax_rest"
    bl_label = "松弛姿态至静置姿态"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        try:
            bpy.ops.pose.relax_rest('INVOKE_DEFAULT')
        except RuntimeError:
            self.report({'ERROR'}, "无法松弛姿态至静置姿态")
            return {'CANCELLED'}
        return {'FINISHED'}

class ACTION_OT_pose_push(bpy.types.Operator):
    bl_idname = "action.pose_push"
    bl_label = "从补间姿态推移姿态"
    bl_description ="快捷键 Ctrl E"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        try:
            bpy.ops.pose.push('INVOKE_DEFAULT')
        except RuntimeError:
            self.report({'ERROR'}, "无法从补间姿态推移姿态")
            return {'CANCELLED'}
        return {'FINISHED'}

class ACTION_OT_pose_relax(bpy.types.Operator):
    bl_idname = "action.pose_relax"
    bl_label = "松弛姿态到补间姿态"
    bl_description ="快捷键 Alt E"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        try:
            bpy.ops.pose.relax('INVOKE_DEFAULT')
        except RuntimeError:
            self.report({'ERROR'}, "无法松弛姿态到补间姿态")
            return {'CANCELLED'}
        return {'FINISHED'}

class ACTION_OT_pose_breakdown(bpy.types.Operator):
    bl_idname = "action.pose_breakdown"
    bl_label = "姿态补间器"
    bl_description ="快捷键 Shift E"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        try:
            bpy.ops.pose.breakdown('INVOKE_DEFAULT')
        except RuntimeError:
            self.report({'ERROR'}, "无法姿态补间器")
            return {'CANCELLED'}
        return {'FINISHED'}

class ACTION_OT_pose_blend_to_neighbor(bpy.types.Operator):
    bl_idname = "action.pose_blend_to_neighbor"
    bl_label = "混合至邻帧"
    bl_description ="快捷键 Shift Alt E"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        try:
            bpy.ops.pose.blend_to_neighbor('INVOKE_DEFAULT')
        except RuntimeError:
            self.report({'ERROR'}, "无法混合至邻帧")
            return {'CANCELLED'}
        return {'FINISHED'}
# 4.3版本有效
class ACTION_OT_pose_blend_with_rest(bpy.types.Operator):
    bl_idname = "action.pose_blend_with_rest"
    bl_label = "将姿态与静置姿态混合"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        try:
            bpy.ops.pose.blend_with_rest('INVOKE_DEFAULT')
        except RuntimeError:
            self.report({'ERROR'}, "无法将姿态与静置姿态混合")
            return {'CANCELLED'}
        return {'FINISHED'}

class ACTION_OT_pose_propagate_menu(bpy.types.Operator):
    bl_idname = "action.pose_propagate_menu"
    bl_label = "传导"
    bl_description ="快捷键 Alt P"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.ops.wm.call_menu(name="VIEW3D_MT_pose_propagate")
        return {'FINISHED'}

class ACTION_OT_pose_motion_menu(bpy.types.Operator):
    bl_idname = "action.pose_motion_menu"
    bl_label = "运动路径"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.ops.wm.call_menu(name="VIEW3D_MT_pose_motion")
        return {'FINISHED'}

class ACTION_OT_pose_paths_calculate(bpy.types.Operator):
    bl_idname = "action.pose_paths_calculate"
    bl_label = "计算运动路径"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.ops.pose.paths_calculate('INVOKE_DEFAULT')
        return {'FINISHED'}

class ACTION_OT_pose_paths_clear(bpy.types.Operator):
    bl_idname = "action.pose_paths_clear"
    bl_label = "清空骨骼路径"
    bl_options = {'REGISTER', 'UNDO'}

    only_selected: bpy.props.BoolProperty(
        default=False,
    )

    def invoke(self, context, event):
        return self.execute(context)

    def draw(self, context):
        layout = self.layout
        split = layout.row().split(factor=0.4)
        
        col_left = split.column()
        col_left.alignment = 'RIGHT'
        col_right = split.column()

        col_left.label(text="")
        col_right.prop(self, "only_selected", text="仅选中")

    def execute(self, context):
        bpy.ops.pose.paths_clear(only_selected=self.only_selected)
        return {'FINISHED'}
# 4.2 版本有效
class ACTION_OT_pose_group_menu(bpy.types.Operator):
    bl_idname = "action.pose_group_menu"
    bl_label = "骨骼组"
    bl_description = "快捷键 Ctrl G"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.ops.wm.call_menu(name="VIEW3D_MT_pose_group")
        return {'FINISHED'}

class ACTION_OT_pose_group_menu(bpy.types.Operator):
    bl_idname = "action.pose_group_menu"
    bl_label = "骨骼组"
    bl_description = "快捷键 Ctrl G"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.ops.wm.call_menu(name="VIEW3D_MT_pose_group")
        return {'FINISHED'}

class ACTION_OT_pose_ik_menu(bpy.types.Operator):
    bl_idname = "action.pose_ik_menu"
    bl_label = "反向运动学"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.ops.wm.call_menu(name="VIEW3D_MT_pose_ik")
        return {'FINISHED'}

class ACTION_OT_pose_ik_add(bpy.types.Operator):
    bl_idname = "action.pose_ik_add"
    bl_label = "为骨骼添加IK"
    bl_description = "快捷键 Shift I"
    bl_options = {'REGISTER', 'UNDO'}

    with_targets: bpy.props.BoolProperty(
        default=True,
    )

    def invoke(self, context, event):
        return self.execute(context)

    def draw(self, context):
        layout = self.layout
        split = layout.row().split(factor=0.4)
        
        col_left = split.column()
        col_left.alignment = 'RIGHT'
        col_right = split.column()

        col_left.label(text="")
        col_right.prop(self, "with_targets", text="附带目标")

    def execute(self, context):
        bpy.ops.pose.ik_add(with_targets=self.with_targets)
        return {'FINISHED'}

class ACTION_OT_pose_ik_clear(bpy.types.Operator):
    bl_idname = "action.pose_ik_clear"
    bl_label = "移除IK"
    bl_description = "快捷键 Ctrl Alt I"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.ops.pose.ik_clear()
        return {'FINISHED'}

class ACTION_OT_pose_constraints_menu(bpy.types.Operator):
    bl_idname = "action.pose_constraints_menu"
    bl_label = "约束"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.ops.wm.call_menu(name="VIEW3D_MT_pose_constraints")
        return {'FINISHED'}

class ACTION_OT_pose_constraint_add_with_targets(bpy.types.Operator):
    bl_idname = "action.pose_constraint_add_with_targets"
    bl_label = "添加约束(带目标)"
    bl_description = "快捷键 Ctrl Shift C"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.ops.pose.constraint_add_with_targets('INVOKE_DEFAULT')
        return {'FINISHED'}

class ACTION_OT_pose_constraints_copy(bpy.types.Operator):
    bl_idname = "action.pose_constraints_copy"
    bl_label = "将约束复制到当前所选骨骼"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        try:
            bpy.ops.pose.constraints_copy()
        except RuntimeError:
            self.report({'ERROR'}, "无法将约束复制到当前所选骨骼")
            return {'CANCELLED'}
        return {'FINISHED'}

class ACTION_OT_pose_constraints_clear(bpy.types.Operator):
    bl_idname = "action.pose_constraints_clear"
    bl_label = "清除姿态约束"
    bl_description = "快捷键 Ctrl Alt C"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.ops.pose.constraints_clear()
        return {'FINISHED'}






classes = (
    ACTION_OT_pose_select_constraint_target,
    ACTION_OT_pose_pose_slide_menu,
    ACTION_OT_pose_push_rest,
    ACTION_OT_pose_relax_rest,
    ACTION_OT_pose_push,
    ACTION_OT_pose_relax,
    ACTION_OT_pose_breakdown,
    ACTION_OT_pose_blend_to_neighbor,
    ACTION_OT_pose_blend_with_rest,
    ACTION_OT_pose_propagate_menu,
    ACTION_OT_pose_motion_menu,
    ACTION_OT_pose_paths_calculate,
    ACTION_OT_pose_paths_clear,
    ACTION_OT_pose_group_menu,
    ACTION_OT_pose_ik_menu,
    ACTION_OT_pose_ik_add,
    ACTION_OT_pose_ik_clear,
    ACTION_OT_pose_constraints_menu,
    ACTION_OT_pose_constraint_add_with_targets,
    ACTION_OT_pose_constraints_copy,
    ACTION_OT_pose_constraints_clear,


)

def register():
    for cls in classes:
        bpy.utils.register_class(cls)

def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)