import bpy

class ACTION_OT_gpencilweight_vertex_group_normalize_all(bpy.types.Operator):
    bl_idname = "action.gpencilweight_vertex_group_normalize_all"
    bl_label = "规格化全部顶点组"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        if not context.active_object.vertex_groups:
            return False

        if not hasattr(context.active_object.data, "layers") or not context.active_object.data.layers:
            return False

        for layer in context.active_object.data.layers:
            for frame in layer.frames:
                for stroke in frame.strokes:
                    for point in stroke.points:
                        if point.vertex_group:
                            return True
        return False

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
        bpy.ops.gpencil.vertex_group_normalize_all(lock_active=self.lock_active)
        return {'FINISHED'}

class ACTION_OT_gpencilweight_vertex_group_normalize(bpy.types.Operator):
    bl_idname = "action.gpencilweight_vertex_group_normalize"
    bl_label = "规格化"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        if not context.active_object.vertex_groups:
            return False

        if not hasattr(context.active_object.data, "layers") or not context.active_object.data.layers:
            return False

        for layer in context.active_object.data.layers:
            for frame in layer.frames:
                for stroke in frame.strokes:
                    for point in stroke.points:
                        if point.vertex_group:
                            return True
        return False

    def execute(self, context):
        bpy.ops.gpencil.vertex_group_normalize()
        return {'FINISHED'}

class ACTION_OT_gpencilweight_vertex_group_invert(bpy.types.Operator):
    bl_idname = "action.gpencilweight_vertex_group_invert"
    bl_label = "反转"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        if not context.active_object.vertex_groups:
            return False

        if not hasattr(context.active_object.data, "layers") or not context.active_object.data.layers:
            return False

        for layer in context.active_object.data.layers:
            for frame in layer.frames:
                for stroke in frame.strokes:
                    for point in stroke.points:
                        if point.vertex_group:
                            return True
        return False

    def execute(self, context):
        bpy.ops.gpencil.vertex_group_invert()
        return {'FINISHED'}
    
class ACTION_OT_gpencilweight_vertex_group_smooth(bpy.types.Operator):
    bl_idname = "action.gpencilweight_vertex_group_smooth"
    bl_label = "平滑顶点组"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        if not context.active_object.vertex_groups:
            return False

        if not hasattr(context.active_object.data, "layers") or not context.active_object.data.layers:
            return False

        for layer in context.active_object.data.layers:
            for frame in layer.frames:
                for stroke in frame.strokes:
                    for point in stroke.points:
                        if point.vertex_group:
                            return True
        return False

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
        bpy.ops.gpencil.vertex_group_smooth(factor=self.factor, repeat=self.repeat)
        return {'FINISHED'}
    
class ACTION_OT_gpencilweight_gpencil_autoweights_menu(bpy.types.Operator):
    bl_idname = "action.gpencilweight_gpencil_autoweights_menu"
    bl_label = "生成权重"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.ops.wm.call_menu(name="VIEW3D_MT_gpencil_autoweights")
        return {'FINISHED'}

classes = (
    ACTION_OT_gpencilweight_vertex_group_normalize_all,
    ACTION_OT_gpencilweight_vertex_group_normalize,
    ACTION_OT_gpencilweight_vertex_group_invert,
    ACTION_OT_gpencilweight_vertex_group_smooth,
    ACTION_OT_gpencilweight_gpencil_autoweights_menu,

)

def register():
    for cls in classes:
        bpy.utils.register_class(cls)

def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)