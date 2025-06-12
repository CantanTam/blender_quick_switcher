import bpy

class ACTION_OT_meshweight_weight_from_bones_auto(bpy.types.Operator):
    bl_idname = "action.meshweight_weight_from_bones_auto"
    bl_label = "根据骨骼定义权重"
    bl_options = {'REGISTER', 'UNDO'}

    type: bpy.props.EnumProperty(
        items=[
            ('AUTOMATIC', "自动", ""),
            ('ENVELOPES', "按封套分配权重", ""),
        ],
        default='AUTOMATIC'
    )

    def invoke(self, context, event):
        return self.execute(context)

    def draw(self, context):
        layout = self.layout
        split = layout.row().split(factor=0.4)
        
        col_left = split.column()
        col_left.alignment = 'RIGHT'
        col_right = split.column()

        col_left.label(text="类型")
        col_right.prop(self, "type", text="abc", expand=True)

    def execute(self, context):
        try:
            bpy.ops.paint.weight_from_bones(type=self.type)
        except RuntimeError:
            self.report({'ERROR'}, "无法自动按骨骼指定")
            return {'CANCELLED'}
        return {'FINISHED'}
    
class ACTION_OT_meshweight_weight_from_bones_envelope(bpy.types.Operator):
    bl_idname = "action.meshweight_weight_from_bones_envelope"
    bl_label = "根据骨骼定义权重"
    bl_options = {'REGISTER', 'UNDO'}

    type: bpy.props.EnumProperty(
        items=[
            ('AUTOMATIC', "自动", ""),
            ('ENVELOPES', "按封套分配权重", ""),
        ],
        default='ENVELOPES'
    )

    def invoke(self, context, event):
        return self.execute(context)

    def draw(self, context):
        layout = self.layout
        split = layout.row().split(factor=0.4)
        
        col_left = split.column()
        col_left.alignment = 'RIGHT'
        col_right = split.column()

        col_left.label(text="类型")
        col_right.prop(self, "type", text="abc", expand=True)

    def execute(self, context):
        try:
            bpy.ops.paint.weight_from_bones(type=self.type)
        except RuntimeError:
            self.report({'ERROR'}, "无法按骨骼封套指定")
            return {'CANCELLED'}
        return {'FINISHED'}
    
class ACTION_OT_meshweight_object_vertex_group_normalize(bpy.types.Operator):
    bl_idname = "action.meshweight_object_vertex_group_normalize"
    bl_label = "规格化"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        try:
            bpy.ops.object.vertex_group_normalize()
        except RuntimeError:
            self.report({'ERROR'}, "无法规格化")
            return {'CANCELLED'}
        return {'FINISHED'}

class ACTION_OT_meshweight_object_vertex_group_mirror(bpy.types.Operator):
    bl_idname = "action.meshweight_object_vertex_group_mirror"
    bl_label = "镜像顶点组"
    bl_options = {'REGISTER', 'UNDO'}

    mirror_weights: bpy.props.BoolProperty(default=True)
    flip_group_names: bpy.props.BoolProperty(default=True)
    all_groups: bpy.props.BoolProperty(default=False)
    use_topology: bpy.props.BoolProperty(default=False)

    def invoke(self, context, event):
        return self.execute(context)

    def draw(self, context):
        layout = self.layout
        split = layout.row().split(factor=0.4)
        
        col_left = split.column()
        col_left.alignment = 'RIGHT'
        col_right = split.column()

        col_left.label(text="")
        col_right.prop(self, "mirror_weights", text="镜像权重")

        col_left.label(text="")
        col_right.prop(self, "flip_group_names", text="翻转组名称")

        col_left.label(text="")
        col_right.prop(self, "all_groups", text="全部组")

        col_left.label(text="")
        col_right.prop(self, "use_topology", text="拓扑镜像")

    def execute(self, context):
        try:
            bpy.ops.object.vertex_group_mirror(
                mirror_weights=self.mirror_weights,
                flip_group_names=self.flip_group_names,
                all_groups=self.all_groups,
                use_topology=self.use_topology
            )
        except RuntimeError:
            self.report({'ERROR'}, "无法镜像顶点组")
            return {'CANCELLED'}
        return {'FINISHED'}




classes = (
    ACTION_OT_meshweight_weight_from_bones_auto,
    ACTION_OT_meshweight_weight_from_bones_envelope,
    ACTION_OT_meshweight_object_vertex_group_normalize,
    ACTION_OT_meshweight_object_vertex_group_mirror,

)

def register():
    for cls in classes:
        bpy.utils.register_class(cls)

def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)