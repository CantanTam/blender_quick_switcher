import bpy

class BUTTON_ACTION_OT_meshvertex_vertex_color_set(bpy.types.Operator):
    bl_idname = "button.action_meshvertex_vertex_color_set"
    bl_label = "设置顶点色"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.ops.paint.vertex_color_set()
        return {'FINISHED'}

class BUTTON_ACTION_OT_meshvertex_vertex_color_smooth(bpy.types.Operator):
    bl_idname = "button.action_meshvertex_vertex_color_smooth"
    bl_label = "平滑顶点色"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.ops.paint.vertex_color_smooth()
        return {'FINISHED'}

class BUTTON_ACTION_OT_meshvertex_vertex_color_dirt(bpy.types.Operator):
    bl_idname = "button.action_meshvertex_vertex_color_dirt"
    bl_label = "脏旧顶点色"
    bl_options = {'REGISTER', 'UNDO'}

    blur_strength: bpy.props.FloatProperty(
        default=1.0,
        min=0.01,
        max=1.0,
        precision=2,
        subtype='FACTOR'
    )

    blur_iterations: bpy.props.IntProperty(
        default=1,
        min=0,
        max=40,
    )

    clean_angle: bpy.props.FloatProperty(
        default=3.14159,
        min=0.0,
        max=3.14159,
        subtype='ANGLE'
    )

    dirt_angle: bpy.props.FloatProperty(
        default=0.0,
        min=0.0,
        max=3.14159,
        subtype='ANGLE'
    )

    dirt_only: bpy.props.BoolProperty(
        default=False
    )

    normalize: bpy.props.BoolProperty(
        default=True
    )

    def invoke(self, context, event):
        return self.execute(context)

    def draw(self, context):
        layout = self.layout
        split = layout.row().split(factor=0.4)

        col_left = split.column()
        col_left.alignment = 'RIGHT'
        col_right = split.column()

        col_left.label(text="模糊强度")
        col_right.prop(self, "blur_strength", text="")

        col_left.label(text="模糊迭代")
        col_right.prop(self, "blur_iterations", text="")

        col_left.label(text="高亮角度")
        col_right.prop(self, "clean_angle", text="")

        col_left.label(text="脏旧角度")
        col_right.prop(self, "dirt_angle", text="")

        col_left.label(text="")
        col_right.prop(self, "dirt_only", text="仅脏旧")

        col_left.label(text="")
        col_right.prop(self, "normalize", text="规格化")

    def execute(self, context):
        bpy.ops.paint.vertex_color_dirt(
            blur_strength=self.blur_strength,
            blur_iterations=self.blur_iterations,
            clean_angle=self.clean_angle,
            dirt_angle=self.dirt_angle,
            dirt_only=self.dirt_only,
            normalize=self.normalize)
        return {'FINISHED'}

class BUTTON_ACTION_OT_meshvertex_vertex_color_from_weight(bpy.types.Operator):
    bl_idname = "button.action_meshvertex_vertex_color_from_weight"
    bl_label = "来自权重的顶点色"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        return (
            context.active_object.vertex_groups and
            context.active_object.data and 
            context.active_object.data.vertices
        )

    def execute(self, context):
        bpy.ops.paint.vertex_color_from_weight()
        return {'FINISHED'}

class BUTTON_ACTION_OT_meshvertex_vertex_color_invert(bpy.types.Operator):
    bl_idname = "button.action_meshvertex_vertex_color_invert"
    bl_label = "反转"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.ops.paint.vertex_color_invert()
        return {'FINISHED'}

# 这个功能暂时不可用
class BUTTON_ACTION_OT_meshvertex_vertex_color_levels(bpy.types.Operator):
    bl_idname = "button.action_meshvertex_vertex_color_levels"
    bl_label = "顶点绘制层级"
    bl_options = {'REGISTER', 'UNDO'}

    offset: bpy.props.FloatProperty(
        default=0.0,
        min=-1.0,
        max=1.0,
        precision=3,
        subtype='FACTOR'
    )

    gain: bpy.props.FloatProperty(
        default=1.0,
        min=0.0,
        soft_max=10,
        precision=3,
    )

    def invoke(self, context, event):
        return self.execute(context)

    def draw(self, context):
        layout = self.layout
        split = layout.row().split(factor=0.4)

        col_left = split.column()
        col_left.alignment = 'RIGHT'
        col_right = split.column()

        col_left.label(text="偏移量")
        col_right.prop(self, "offset", text="")

        col_left.label(text="增益")
        col_right.prop(self, "gain", text="")

    def execute(self, context):
        bpy.ops.paint.vertex_color_levels(offset=self.offset, gain=self.gain)
        return {'FINISHED'}

class BUTTON_ACTION_OT_meshvertex_vertex_color_hsv(bpy.types.Operator):
    bl_idname = "button.action_meshvertex_vertex_color_hsv"
    bl_label = "顶点绘制色相/饱和度/明度"
    bl_options = {'REGISTER', 'UNDO'}

    h: bpy.props.FloatProperty(
        default=0.5,
        min=0.0,
        max=1.0,
        precision=3,
        subtype='FACTOR'
    )

    s: bpy.props.FloatProperty(
        default=1.0,
        min=0.0,
        max=2.0,
        precision=3,
        subtype='FACTOR'
    )

    v: bpy.props.FloatProperty(
        default=1.0,
        min=0.0,
        max=2.0,
        precision=3,
        subtype='FACTOR'
    )

    def invoke(self, context, event):
        return self.execute(context)

    def draw(self, context):
        layout = self.layout
        split = layout.row().split(factor=0.4)

        col_left = split.column()
        col_left.alignment = 'RIGHT'
        col_right = split.column()

        col_left.label(text="色相")
        col_right.prop(self, "h", text="")

        col_left.label(text="饱和度")
        col_right.prop(self, "s", text="")

        col_left.label(text="值(明度)")
        col_right.prop(self, "v", text="")

    def execute(self, context):
        bpy.ops.paint.vertex_color_hsv(h=self.h, s=self.s, v=self.v)
        return {'FINISHED'}
    
class BUTTON_ACTION_OT_meshvertex_vertex_color_brightness_contrast(bpy.types.Operator):
    bl_idname = "button.action_meshvertex_vertex_color_brightness_contrast"
    bl_label = "顶点绘制亮度/对比度"
    bl_options = {'REGISTER', 'UNDO'}

    brightness: bpy.props.FloatProperty(
        default=0.0,
        min=-100.0,
        max=100.0,
        precision=3,
        subtype='FACTOR'
    )

    contrast: bpy.props.FloatProperty(
        default=0.0,
        min=-100.0,
        max=100.0,
        precision=3,
        subtype='FACTOR'
    )

    def invoke(self, context, event):
        return self.execute(context)

    def draw(self, context):
        layout = self.layout
        split = layout.row().split(factor=0.4)

        col_left = split.column()
        col_left.alignment = 'RIGHT'
        col_right = split.column()

        col_left.label(text="亮度")
        col_right.prop(self, "brightness", text="")

        col_left.label(text="对比度")
        col_right.prop(self, "contrast", text="")

    def execute(self, context):
        bpy.ops.paint.vertex_color_invert()
        #bpy.ops.paint.vertex_color_brightness_contrast(brightness=self.brightness, contrast=self.contrast)
        return {'FINISHED'}



classes = (
    BUTTON_ACTION_OT_meshvertex_vertex_color_set,
    BUTTON_ACTION_OT_meshvertex_vertex_color_smooth,
    BUTTON_ACTION_OT_meshvertex_vertex_color_dirt,
    BUTTON_ACTION_OT_meshvertex_vertex_color_from_weight,
    BUTTON_ACTION_OT_meshvertex_vertex_color_invert,
    BUTTON_ACTION_OT_meshvertex_vertex_color_levels,
    BUTTON_ACTION_OT_meshvertex_vertex_color_hsv,
    BUTTON_ACTION_OT_meshvertex_vertex_color_brightness_contrast,

)

def register():
    for cls in classes:
        bpy.utils.register_class(cls)

def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)