import bpy

class BUTTON_ACTION_OT_greasepencilweight_vertex_group_normalize_all(bpy.types.Operator):
    bl_idname = "button.action_greasepencilweight_vertex_group_normalize_all"
    bl_label = "规格化全部顶点组"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        if hasattr(context.active_object, "vertex_groups") and len(context.active_object.vertex_groups) > 0:
            return True

    lock_active: bpy.props.BoolProperty(
        name="锁定活动项",
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
        col_right.prop(self, "lock_active")

    def execute(self, context):
        bpy.ops.grease_pencil.vertex_group_normalize_all(lock_active=self.lock_active)
        return {'FINISHED'}

class BUTTON_ACTION_OT_greasepencilweight_vertex_group_normalize(bpy.types.Operator):
    bl_idname = "button.action_greasepencilweight_vertex_group_normalize"
    bl_label = "规格化"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        if hasattr(context.active_object, "vertex_groups") and len(context.active_object.vertex_groups) > 0:
            return True

    def execute(self, context):
        bpy.ops.grease_pencil.vertex_group_normalize()
        return {'FINISHED'}

class BUTTON_ACTION_OT_greasepencilweight_vertex_group_invert(bpy.types.Operator):
    bl_idname = "button.action_greasepencilweight_vertex_group_invert"
    bl_label = "反转"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        if hasattr(context.active_object, "vertex_groups") and len(context.active_object.vertex_groups) > 0:
            return True

    def execute(self, context):
        bpy.ops.grease_pencil.weight_invert()
        return {'FINISHED'}

class BUTTON_ACTION_OT_greasepencilweight_vertex_group_smooth(bpy.types.Operator):
    bl_idname = "button.action_greasepencilweight_vertex_group_smooth"
    bl_label = "平滑顶点组"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        if hasattr(context.active_object, "vertex_groups") and len(context.active_object.vertex_groups) > 0:
            return True

    factor: bpy.props.FloatProperty(
        name="",
        default=0.5,
        min=0.0,
        max=1.0,
        subtype='FACTOR',
    )

    repeat: bpy.props.IntProperty(
        name="",
        default=1,
        min=1,
        max=10000,
        soft_max=200,
    )
    def invoke(self, context, event):
        return self.execute(context)

    def draw(self, context):
        layout = self.layout
        split = layout.row().split(factor=0.4)

        col_left = split.column()
        col_left.alignment = 'RIGHT'
        col_right = split.column()

        col_left.label(text="系数")
        col_right.prop(self, "factor")

        col_left.label(text="迭代")
        col_right.prop(self, "repeat")

    def execute(self, context):
        bpy.ops.grease_pencil.vertex_group_smooth(factor=self.factor, repeat=self.repeat)
        return {'FINISHED'}

class BUTTON_ACTION_OT_greasepencilweight_weight_sample(bpy.types.Operator):
    bl_idname = "button.action_greasepencilweight_weight_sample"
    bl_label = "采样权重"
    bl_description = "快捷键 Shift X"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.ops.grease_pencil.weight_sample('INVOKE_DEFAULT')
        return {'FINISHED'}

classes = (
    BUTTON_ACTION_OT_greasepencilweight_vertex_group_normalize_all,
    BUTTON_ACTION_OT_greasepencilweight_vertex_group_normalize,
    BUTTON_ACTION_OT_greasepencilweight_vertex_group_invert,
    BUTTON_ACTION_OT_greasepencilweight_vertex_group_smooth,
    BUTTON_ACTION_OT_greasepencilweight_weight_sample,

)

def register():
    for cls in classes:
        bpy.utils.register_class(cls)

def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)