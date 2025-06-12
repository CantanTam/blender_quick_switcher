import bpy

# “骨架”菜单
class ACTION_OT_armatureedit_select_select_linked(bpy.types.Operator):
    bl_idname = "action.armatureedit_select_select_linked"
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
class ACTION_OT_armatureedit_select_similar(bpy.types.Operator):
    bl_idname = "action.armatureedit_select_similar"
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

class ACTION_OT_armatureedit_align(bpy.types.Operator):
    bl_idname = "action.armatureedit_align"
    bl_label = "对齐骨骼"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.ops.armature.align()
        return {'FINISHED'}

class ACTION_OT_armatureedit_armature_roll_menu(bpy.types.Operator):
    bl_idname = "action.armatureedit_armature_roll_menu"
    bl_label = "骨骼扭转"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.ops.wm.call_menu(name="VIEW3D_MT_edit_armature_roll")
        return {'FINISHED'}

class ACTION_OT_armatureedit_armature_calculate_roll_menu(bpy.types.Operator):
    bl_idname = "action.armatureedit_armature_calculate_roll_menu"
    bl_label = "重算扭转"
    bl_description = "快捷键 Shift N"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.ops.armature.calculate_roll('INVOKE_DEFAULT')
        return {'FINISHED'}

class ACTION_OT_armatureedit_transform_bone_roll(bpy.types.Operator):
    bl_idname = "action.armatureedit_transform_bone_roll"
    bl_label = "设置扭转"
    bl_description = "快捷键 Ctrl R"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.ops.transform.transform('INVOKE_DEFAULT',mode='BONE_ROLL')
        return {'FINISHED'}

class ACTION_OT_armatureedit_roll_clear(bpy.types.Operator):
    bl_idname = "action.armatureedit_roll_clear"
    bl_label = "清除扭转"
    bl_options = {'REGISTER', 'UNDO'}

    roll: bpy.props.FloatProperty(
        default=0,
        min=-6.28319,
        max=6.28319,
        subtype='ANGLE',
    )

    def invoke(self, context, event):
        return self.execute(context)

    def draw(self, context):
        layout = self.layout
        split = layout.row().split(factor=0.4)
        
        col_left = split.column()
        col_left.alignment = 'RIGHT'
        col_right = split.column()

        col_left.label(text="扭转(滚动)")
        col_right.prop(self, "roll", text="")

    def execute(self, context):    
        bpy.ops.armature.roll_clear(roll=self.roll)
        return {'FINISHED'}

class ACTION_OT_armatureedit_extrude_move(bpy.types.Operator):
    bl_idname = "action.armatureedit_extrude_move"
    bl_label = "挤出"
    bl_description = "快捷键 E"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):    
        bpy.ops.armature.extrude_move('INVOKE_DEFAULT')
        return {'FINISHED'}

class ACTION_OT_armatureedit_fill(bpy.types.Operator):
    bl_idname = "action.armatureedit_fill"
    bl_label = "在关节间填充骨骼"
    bl_description = "快捷键 F"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        selected_heads = [b for b in context.active_object.data.edit_bones if b.select_head]
        selected_tails = [b for b in context.active_object.data.edit_bones if b.select_tail]
        
        if not (selected_heads or selected_tails):
            return False
        
        head_bones = {b for b in selected_heads}
        tail_bones = {b for b in selected_tails}
        
        if head_bones & tail_bones:
            return False
        
        if len(selected_heads) + len(selected_tails) > 2:
            return False
        
        return True

    def execute(self, context):    
        bpy.ops.armature.fill()
        return {'FINISHED'}
    
class ACTION_OT_armatureedit_split(bpy.types.Operator):
    bl_idname = "action.armatureedit_split"
    bl_label = "拆分"
    bl_description = "快捷键 Y"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):    
        bpy.ops.armature.split()
        return {'FINISHED'}

class ACTION_OT_armatureedit_separate(bpy.types.Operator):
    bl_idname = "action.armatureedit_separate"
    bl_label = "分离骨骼"
    bl_description = "快捷键 P"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):    
        bpy.ops.armature.separate('INVOKE_DEFAULT')
        return {'FINISHED'}

class ACTION_OT_armatureedit_subdivide(bpy.types.Operator):
    bl_idname = "action.armatureedit_subdivide"
    bl_label = "细分"
    bl_options = {'REGISTER', 'UNDO'}

    number_cuts: bpy.props.IntProperty(
        default=1,
        min=1,
        max=1000,
        soft_max=10,
    )

    def invoke(self, context, event):
        return self.execute(context)

    def draw(self, context):
        layout = self.layout
        split = layout.row().split(factor=0.4)
        
        col_left = split.column()
        col_left.alignment = 'RIGHT'
        col_right = split.column()

        col_left.label(text="切割次数")
        col_right.prop(self, "number_cuts", text="")

    def execute(self, context):    
        bpy.ops.armature.subdivide(number_cuts=self.number_cuts)
        return {'FINISHED'}

class ACTION_OT_armatureedit_switch_direction(bpy.types.Operator):
    bl_idname = "action.armatureedit_switch_direction"
    bl_label = "切换方向"
    bl_description = "快捷键 Alt F"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):    
        bpy.ops.armature.switch_direction()
        return {'FINISHED'}

class ACTION_OT_armatureedit_symmetrize(bpy.types.Operator):
    bl_idname = "action.armatureedit_symmetrize"
    bl_label = "对称"
    bl_options = {'REGISTER', 'UNDO'}

    direction: bpy.props.EnumProperty(
        items=[
            ('NEGATIVE_X', "-X 到 +X", ""),
            ('POSITIVE_X', "+X 到 -X", ""),
        ],
        default='NEGATIVE_X'
    )

    def invoke(self, context, event):
        return self.execute(context)

    def draw(self, context):
        layout = self.layout
        split = layout.row().split(factor=0.4)
        
        col_left = split.column()
        col_left.alignment = 'RIGHT'
        col_right = split.column()

        col_left.label(text="方向")
        col_right.prop(self, "direction", text="abc", expand=True)

    def execute(self, context):    
        bpy.ops.armature.symmetrize(direction=self.direction)
        return {'FINISHED'}

class ACTION_OT_armatureedit_name_menu(bpy.types.Operator):
    bl_idname = "action.armatureedit_name_menu"
    bl_label = "名称"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):    
        bpy.ops.wm.call_menu(name="VIEW3D_MT_edit_armature_names")
        return {'FINISHED'}
    
class ACTION_OT_armatureedit_armature_layers(bpy.types.Operator):
    bl_idname = "action.armatureedit_armature_layers"
    bl_label = "更改骨架层"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):    
        bpy.ops.armature.armature_layers('INVOKE_DEFAULT')
        return {'FINISHED'}

class ACTION_OT_armatureedit_bone_layers(bpy.types.Operator):
    bl_idname = "action.armatureedit_bone_layers"
    bl_label = "更改骨骼层"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):    
        bpy.ops.armature.bone_layers('INVOKE_DEFAULT')
        return {'FINISHED'}

class ACTION_OT_armatureedit_edit_armature_parent(bpy.types.Operator):
    bl_idname = "action.armatureedit_edit_armature_parent"
    bl_label = "父级"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):    
        bpy.ops.wm.call_menu(name="VIEW3D_MT_edit_armature_parent")
        return {'FINISHED'}

class ACTION_OT_armatureedit_parent_set(bpy.types.Operator):
    bl_idname = "action.armatureedit_parent_set"
    bl_label = "生成父级"
    bl_description = "快捷键 Ctrl P"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):    
        bpy.ops.armature.parent_set('INVOKE_DEFAULT')
        return {'FINISHED'}
    
class ACTION_OT_armatureedit_parent_clear(bpy.types.Operator):
    bl_idname = "action.armatureedit_parent_clear"
    bl_label = "清空父级"
    bl_description = "快捷键 Alt P"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):    
        bpy.ops.armature.parent_clear('INVOKE_DEFAULT')
        return {'FINISHED'}
    
class ACTION_OT_armatureedit_bone_options_toggle(bpy.types.Operator):
    bl_idname = "action.armatureedit_bone_options_toggle"
    bl_label = "骨骼设置"
    bl_description = "快捷键 Shift W"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):    
        bpy.ops.wm.call_menu(name="VIEW3D_MT_bone_options_toggle")
        return {'FINISHED'}
# 4.3版本以后的功能
class ACTION_OT_armatureedit_bone_collections(bpy.types.Operator):
    bl_idname = "action.armatureedit_bone_collections"
    bl_label = "骨骼集合"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):    
        bpy.ops.wm.call_menu(name="VIEW3D_MT_bone_collections")
        return {'FINISHED'}

class ACTION_OT_armatureedit_move_to_collection(bpy.types.Operator):
    bl_idname = "action.armatureedit_move_to_collection"
    bl_label = "移动到集合"
    bl_description = "快捷键 M"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):    
        bpy.ops.armature.move_to_collection('INVOKE_DEFAULT')
        return {'FINISHED'}
    
class ACTION_OT_armatureedit_assign_to_collection(bpy.types.Operator):
    bl_idname = "action.armatureedit_assign_to_collection"
    bl_label = "指定到集合"
    bl_description = "快捷键 Shift M"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):    
        bpy.ops.armature.assign_to_collection('INVOKE_DEFAULT')
        return {'FINISHED'}

class ACTION_OT_armatureedit_collection_show_all(bpy.types.Operator):
    bl_idname = "action.armatureedit_collection_show_all"
    bl_label = "显示全部"
    bl_description = "快捷键 Ctrl `"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):    
        bpy.ops.armature.collection_show_all()
        return {'FINISHED'}

class ACTION_OT_armatureedit_collection_create_and_assign(bpy.types.Operator):
    bl_idname = "action.armatureedit_collection_create_and_assign"
    bl_label = "添加选中的骨骼到新集合"
    bl_options = {'REGISTER', 'UNDO'}

    name: bpy.props.StringProperty(
        default='New Collection',
    )

    def invoke(self, context, event):
        return self.execute(context)

    def draw(self, context):
        layout = self.layout
        split = layout.row().split(factor=0.4)
        
        col_left = split.column()
        col_left.alignment = 'RIGHT'
        col_right = split.column()

        col_left.label(text="骨骼集合")
        col_right.prop(self, "name", text="")

    def execute(self, context):    
        bpy.ops.armature.collection_create_and_assign(name=self.name)
        return {'FINISHED'}





classes = (
    ACTION_OT_armatureedit_select_select_linked,
    ACTION_OT_armatureedit_select_similar,
    ACTION_OT_armatureedit_align,
    ACTION_OT_armatureedit_armature_roll_menu,
    ACTION_OT_armatureedit_armature_calculate_roll_menu,
    ACTION_OT_armatureedit_transform_bone_roll,
    ACTION_OT_armatureedit_roll_clear,
    ACTION_OT_armatureedit_extrude_move,
    ACTION_OT_armatureedit_fill,
    ACTION_OT_armatureedit_split,
    ACTION_OT_armatureedit_separate,
    ACTION_OT_armatureedit_subdivide,
    ACTION_OT_armatureedit_switch_direction,
    ACTION_OT_armatureedit_symmetrize,
    ACTION_OT_armatureedit_name_menu,
    ACTION_OT_armatureedit_armature_layers,
    ACTION_OT_armatureedit_bone_layers,
    ACTION_OT_armatureedit_edit_armature_parent,
    ACTION_OT_armatureedit_parent_set,
    ACTION_OT_armatureedit_parent_clear,
    ACTION_OT_armatureedit_bone_options_toggle,

    ACTION_OT_armatureedit_bone_collections,
    ACTION_OT_armatureedit_move_to_collection,
    ACTION_OT_armatureedit_assign_to_collection,
    ACTION_OT_armatureedit_collection_show_all,
    ACTION_OT_armatureedit_collection_create_and_assign,

)

def register():
    for cls in classes:
        bpy.utils.register_class(cls)

def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)