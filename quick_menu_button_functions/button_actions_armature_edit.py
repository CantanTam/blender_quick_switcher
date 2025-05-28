import bpy

# 以下是“物体”模式当中“物体”菜单特有的一些选项

# “选择”菜单——选择相连
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

# “选择”菜单——相似项 
class BUTTON_ACTION_OT_armatureedit_select_similar(bpy.types.Operator):
    bl_idname = "button.action_armatureedit_select_similar"
    bl_label = "选择相似元素"
    bl_options = {'REGISTER', 'UNDO'}

    type: bpy.props.EnumProperty(
        name="",
        items=[
            ('CHILDREN',            "子级",               ""),
            ('CHILDREN_IMMEDIATE',  "直接子级",     ""),
            ('SIBLINGS',            "平级",               ""),
            ('LENGTH',              "长度",                 ""),
            ('DIRECTION',           "方向(Y轴)",              ""),
            ('PREFIX',              "前缀",                 ""),
            ('SUFFIX',              "后缀",                 ""),
            ('LAYER',               "层",                  ""),
            ('GROUP',               "群组",                  ""),
            ('SHAPE',               "形状",                  ""),
        ],
        default='LENGTH',
    )

    threshold: bpy.props.FloatProperty(
        name="",
        description="阈值",
        default=0.1,
        min=0.0,
        max=1.0,
        precision=3,
        subtype='FACTOR',
    )

    def invoke(self, context, event):
        return self.execute(context)

    def draw(self, context):
        if bpy.context.active_object.type+bpy.context.active_object.mode == "ARMATUREEDIT":

            layout = self.layout
            split = layout.row().split(factor=0.4)
            
            col_left = split.column()
            col_left.alignment = 'RIGHT'
            col_left.label(text="类型")
            col_left.label(text="阈值")
            
            col_right = split.column()
            col_right.prop(self, "type")
            col_right.prop(self, "threshold")

    def execute(self, context):    
        bpy.ops.armature.select_similar(type=self.type, threshold=self.threshold)
        return {'FINISHED'}





classes = (
    BUTTON_ACTION_OT_armatureedit_select_select_linked,
    BUTTON_ACTION_OT_armatureedit_select_similar,

)

def register():
    for cls in classes:
        bpy.utils.register_class(cls)

def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)