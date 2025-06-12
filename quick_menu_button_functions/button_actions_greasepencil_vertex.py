import bpy

class ACTION_OT_greasepencilvertex_vertex_color_set(bpy.types.Operator):
    bl_idname = "action.greasepencilvertex_vertex_color_set"
    bl_label = "顶点绘制设置颜色"
    bl_options = {'REGISTER', 'UNDO'}

    mode: bpy.props.EnumProperty(
        items=[
            ('STROKE', "笔画", ""),
            ('FILL', "填充", ""),
            ('BOTH', "笔画与填充", ""),
        ],
        default='BOTH'
    )

    factor: bpy.props.FloatProperty(
        default=1.0,
        min=0.001,
        max=1.0,
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

        col_left.label(text="模式")
        col_right.prop(self, "mode", text="abc", expand=True)

        col_left.label(text="系数")
        col_right.prop(self, "factor", text="")

    def execute(self, context):
        bpy.ops.grease_pencil.vertex_color_set(mode=self.mode, factor=self.factor)
        return {'FINISHED'}

class ACTION_OT_greasepencilvertex_stroke_reset_vertex_color(bpy.types.Operator):
    bl_idname = "action.greasepencilvertex_stroke_reset_vertex_color"
    bl_label = "重置顶点色"
    bl_options = {'REGISTER', 'UNDO'}

    mode: bpy.props.EnumProperty(
        items=[
            ('STROKE', "笔画", ""),
            ('FILL', "填充", ""),
            ('BOTH', "笔画与填充", ""),
        ],
        default='BOTH'
    )

    def invoke(self, context, event):
        return self.execute(context)

    def draw(self, context):
        layout = self.layout
        split = layout.row().split(factor=0.4)

        col_left = split.column()
        col_left.alignment = 'RIGHT'
        col_right = split.column()

        col_left.label(text="模式")
        col_right.prop(self, "mode", text="abc", expand=True)

    def execute(self, context):
        bpy.ops.grease_pencil.stroke_reset_vertex_color(mode=self.mode)
        return {'FINISHED'}

class ACTION_OT_greasepencilvertex_vertex_color_invert(bpy.types.Operator):
    bl_idname = "action.greasepencilvertex_vertex_color_invert"
    bl_label = "顶点绘制反相"
    bl_options = {'REGISTER', 'UNDO'}

    mode: bpy.props.EnumProperty(
        items=[
            ('STROKE', "笔画", ""),
            ('FILL', "填充", ""),
            ('BOTH', "笔画与填充", ""),
        ],
        default='BOTH'
    )

    def invoke(self, context, event):
        return self.execute(context)

    def draw(self, context):
        layout = self.layout
        split = layout.row().split(factor=0.4)

        col_left = split.column()
        col_left.alignment = 'RIGHT'
        col_right = split.column()

        col_left.label(text="模式")
        col_right.prop(self, "mode", text="abc", expand=True)

    def execute(self, context):
        bpy.ops.grease_pencil.vertex_color_invert(mode=self.mode)
        return {'FINISHED'}
    
class ACTION_OT_greasepencilvertex_vertex_color_levels(bpy.types.Operator):
    bl_idname = "action.greasepencilvertex_vertex_color_levels"
    bl_label = "顶点绘制层级"
    bl_options = {'REGISTER', 'UNDO'}

    mode: bpy.props.EnumProperty(
        items=[
            ('STROKE', "笔画", ""),
            ('FILL', "填充", ""),
            ('BOTH', "笔画与填充", ""),
        ],
        default='BOTH'
    )

    offset: bpy.props.FloatProperty(
        default=0,
        min=-1,
        max=1,
        precision=3,
        subtype='FACTOR'
    )

    gain: bpy.props.FloatProperty(
        default=1,
        min=0,
        soft_max=10,
        precision=3
    )

    def invoke(self, context, event):
        return self.execute(context)

    def draw(self, context):
        layout = self.layout
        split = layout.row().split(factor=0.4)

        col_left = split.column()
        col_left.alignment = 'RIGHT'
        col_right = split.column()

        col_left.label(text="模式")
        col_right.prop(self, "mode", text="")

        col_left.label(text="偏移量")
        col_right.prop(self, "offset", text="")

        col_left.label(text="增益")
        col_right.prop(self, "gain", text="")

    def execute(self, context):
        bpy.ops.grease_pencil.vertex_color_levels(mode=self.mode, offset=self.offset, gain=self.gain)
        return {'FINISHED'}

class ACTION_OT_greasepencilvertex_vertex_color_hsv(bpy.types.Operator):
    bl_idname = "action.greasepencilvertex_vertex_color_hsv"
    bl_label = "顶点绘制色相/饱和度/明度"
    bl_options = {'REGISTER', 'UNDO'}

    mode: bpy.props.EnumProperty(
        items=[
            ('STROKE', "笔画", ""),
            ('FILL', "填充", ""),
            ('BOTH', "笔画与填充", ""),
        ],
        default='BOTH'
    )

    h: bpy.props.FloatProperty(
        default=0.5,
        min=0,
        max=1,
        precision=3,
        subtype='FACTOR'
    )

    s: bpy.props.FloatProperty(
        default=1,
        min=0,
        max=2,
        precision=3,
        subtype='FACTOR'
    )

    v: bpy.props.FloatProperty(
        default=1,
        min=0,
        max=2,
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

        col_left.label(text="模式")
        col_right.prop(self, "mode", text="")

        col_left.label(text="色相")
        col_right.prop(self, "h", text="")

        col_left.label(text="饱和度")
        col_right.prop(self, "s", text="")

        col_left.label(text="值(明度)")
        col_right.prop(self, "v", text="")

    def execute(self, context):
        bpy.ops.grease_pencil.vertex_color_hsv(
            mode=self.mode, 
            h=self.h,
            s=self.s,
            v=self.v)
        return {'FINISHED'}

class ACTION_OT_greasepencilvertex_brightness_contrast(bpy.types.Operator):
    bl_idname = "action.greasepencilvertex_brightness_contrast"
    bl_label = "顶点绘制亮度/对比度"
    bl_options = {'REGISTER', 'UNDO'}

    mode: bpy.props.EnumProperty(
        items=[
            ('STROKE', "笔画", ""),
            ('FILL', "填充", ""),
            ('BOTH', "笔画与填充", ""),
        ],
        default='BOTH'
    )

    brightness: bpy.props.FloatProperty(
        default=0,
        min=-100,
        max=100,
        precision=3,
    )

    contrast: bpy.props.FloatProperty(
        default=0,
        min=-100,
        max=100,
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

        col_left.label(text="模式")
        col_right.prop(self, "mode", text="")

        col_left.label(text="亮度")
        col_right.prop(self, "brightness", text="")

        col_left.label(text="对比度")
        col_right.prop(self, "contrast", text="")

    def execute(self, context):
        bpy.ops.grease_pencil.vertex_color_brightness_contrast(
            mode=self.mode, 
            brightness=self.brightness,
            contrast=self.contrast,)
        return {'FINISHED'}


classes = (
    ACTION_OT_greasepencilvertex_vertex_color_set,
    ACTION_OT_greasepencilvertex_stroke_reset_vertex_color,
    ACTION_OT_greasepencilvertex_vertex_color_invert,
    ACTION_OT_greasepencilvertex_vertex_color_levels,
    ACTION_OT_greasepencilvertex_vertex_color_hsv,
    ACTION_OT_greasepencilvertex_brightness_contrast,


)

def register():
    for cls in classes:
        bpy.utils.register_class(cls)

def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)