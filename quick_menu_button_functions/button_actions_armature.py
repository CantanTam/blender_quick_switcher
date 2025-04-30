import bpy

class BUTTON_ACTION_OT_armature_bone_primitive_add(bpy.types.Operator):
    bl_idname = "button.action_armature_bone_primitive_add"
    bl_label = "添加骨骼"
    bl_description = "快捷键 Shift A"
    bl_options = {'REGISTER', 'UNDO'}

    # 针对"添加骨骼“的选项
    name: bpy.props.StringProperty(
        name="",
        default="Bone",
        update=lambda self, context: self.execute(context) #if bpy.context.mode == 'EDIT_MESH' else None
    )

    def invoke(self, context, event):
        return self.execute(context)

    def draw(self, context):

        layout = self.layout
        split = layout.row().split(factor=0.4)
        
        # 左侧列 - 标签
        col_left = split.column()
        col_left.alignment = 'RIGHT'
        col_left.label(text="名称")
        
        # 右侧列 - 垂直排列的单选按钮
        col_right = split.column()
        col_right.prop(self, "name")

    def execute(self, context):
        bpy.ops.armature.bone_primitive_add('INVOKE_DEFAULT', name=self.name)
        return {'FINISHED'}