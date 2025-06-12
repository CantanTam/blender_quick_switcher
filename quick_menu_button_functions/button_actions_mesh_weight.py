import bpy

class BUTTON_ACTION_OT_meshweight_weight_from_bones_auto(bpy.types.Operator):
    bl_idname = "button.action_meshweight_weight_from_bones_auto"
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
    
class BUTTON_ACTION_OT_meshweight_weight_from_bones_envelope(bpy.types.Operator):
    bl_idname = "button.action_meshweight_weight_from_bones_envelope"
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
    






classes = (
    BUTTON_ACTION_OT_meshweight_weight_from_bones_auto,
    BUTTON_ACTION_OT_meshweight_weight_from_bones_envelope,

)

def register():
    for cls in classes:
        bpy.utils.register_class(cls)

def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)