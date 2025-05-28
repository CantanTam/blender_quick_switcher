import bpy

# 以下是“物体”模式当中“物体”菜单特有的一些选项

# 变换——缩放纹理空间
class BUTTON_ACTION_OT_armatureedit_select_select_linked(bpy.types.Operator):
    bl_idname = "button.action_armatureedit_select_select_linked"
    bl_label = "选择相连"
    bl_options = {'REGISTER', 'UNDO'}

    all_forks: bpy.props.BoolProperty(
        name="全部分支",
        description="跟随父级链中的分支",
        default=False,
    )

    def invoke(self, context, event):
        return self.execute(context)

    def draw(self, context):
        layout = self.layout
        split = layout.row().split(factor=0.4)
        
        col_left = split.column()
        col_left.alignment = 'RIGHT'
        col_left.label(text="")
        
        col_right = split.column()
        col_right.prop(self, "all_forks")

    def execute(self, context):
        bpy.ops.armature.select_linked(all_forks=self.all_forks)
        return {'FINISHED'}
    






classes = (
    BUTTON_ACTION_OT_armatureedit_select_select_linked,

)

def register():
    for cls in classes:
        bpy.utils.register_class(cls)

def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)