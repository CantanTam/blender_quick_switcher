import bpy

class BUTTON_ACTION_OT_greasepenciledit_layer_active_menu(bpy.types.Operator):
    bl_idname = "button.action_greasepenciledit_layer_active_menu"
    bl_label = "活动层"
    bl_description = "快捷键 Y"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.ops.wm.call_menu(name="GREASE_PENCIL_MT_layer_active")
        return {'FINISHED'}

class BUTTON_ACTION_OT_greasepenciledit_layer_add(bpy.types.Operator):
    bl_idname = "button.action_greasepenciledit_layer_add"
    bl_label = "新建层"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.ops.grease_pencil.layer_add('INVOKE_DEFAULT', new_layer_name="Layer")
        return {'FINISHED'}

class BUTTON_ACTION_OT_greasepenciledit_animation_menu(bpy.types.Operator):
    bl_idname = "button.action_greasepenciledit_animation_menu"
    bl_label = "动画"
    bl_description = "快捷键 I"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.ops.wm.call_menu(name="VIEW3D_MT_edit_greasepencil_animation")
        return {'FINISHED'}

class BUTTON_ACTION_OT_greasepenciledit_insert_blank_frame_false(bpy.types.Operator):
    bl_idname = "button.action_greasepenciledit_insert_blank_frame_false"
    bl_label = "插入空白帧"
    bl_description = "快捷键 Shift I"
    bl_options = {'REGISTER', 'UNDO'}

    all_layers: bpy.props.BoolProperty(
        default=False,
    )

    duration: bpy.props.IntProperty(
        default=0,
        min=0,
        soft_min=100,
        max=1048574,
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
        col_right.prop(self, "all_layers", text="全部层")

        col_left.label(text="持续时间")
        col_right.prop(self, "duration" , text="")

    def execute(self, context):
        bpy.ops.grease_pencil.insert_blank_frame(all_layers=self.all_layers, duration=self.duration)
        return {'FINISHED'}

class BUTTON_ACTION_OT_greasepenciledit_insert_blank_frame_true(bpy.types.Operator):
    bl_idname = "button.action_greasepenciledit_insert_blank_frame_true"
    bl_label = "插入空白帧"
    bl_options = {'REGISTER', 'UNDO'}

    all_layers: bpy.props.BoolProperty(
        default=True,
    )

    duration: bpy.props.IntProperty(
        default=0,
        min=0,
        soft_min=100,
        max=1048574,
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
        col_right.prop(self, "all_layers", text="全部层")

        col_left.label(text="持续时间")
        col_right.prop(self, "duration" , text="")

    def execute(self, context):
        bpy.ops.grease_pencil.insert_blank_frame(all_layers=self.all_layers, duration=self.duration)
        return {'FINISHED'}

class BUTTON_ACTION_OT_greasepenciledit_frame_duplicate_false(bpy.types.Operator):
    bl_idname = "button.action_greasepenciledit_frame_duplicate_false"
    bl_label = "复制活动帧"
    bl_options = {'REGISTER', 'UNDO'}

    all: bpy.props.BoolProperty(
        default=False,
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
        col_right.prop(self, "all", text="复制全部")

    def execute(self, context):
        bpy.ops.grease_pencil.frame_duplicate(all=self.all)
        return {'FINISHED'}

class BUTTON_ACTION_OT_greasepenciledit_frame_duplicate_true(bpy.types.Operator):
    bl_idname = "button.action_greasepenciledit_frame_duplicate_true"
    bl_label = "复制活动帧"
    bl_options = {'REGISTER', 'UNDO'}

    all: bpy.props.BoolProperty(
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
        col_right.prop(self, "all", text="复制全部")

    def execute(self, context):
        bpy.ops.grease_pencil.frame_duplicate(all=self.all)
        return {'FINISHED'}

class VIEW3D_MT_greasepenciledit_separate_menu(bpy.types.Menu):
    bl_label = "分离笔画"
    bl_idname = "popup.greasepenciledit_separate_menu"
    bl_options = {'SEARCH_ON_KEY_PRESS'}

    def draw(self, context):
        layout = self.layout
        layout.operator("grease_pencil.separate", text="选中项").mode='SELECTED'
        layout.operator("grease_pencil.separate", text="按材质").mode='MATERIAL'
        layout.operator("grease_pencil.separate", text="按层").mode='LAYER'

class BUTTON_ACTION_OT_call_greasepenciledit_separate_menu(bpy.types.Operator):
    bl_idname = "button.action_call_greasepenciledit_separate_menu"
    bl_label = "分离"
    bl_description = "快捷键 P"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.ops.wm.call_menu(name="popup.greasepenciledit_separate_menu")
        return {'FINISHED'}

class BUTTON_ACTION_OT_greasepenciledit_cleanup_menu(bpy.types.Operator):
    bl_idname = "button.action_greasepenciledit_cleanup_menu"
    bl_label = "清理"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.ops.wm.call_menu(name="VIEW3D_MT_edit_greasepencil_cleanup")
        return {'FINISHED'}

class BUTTON_ACTION_OT_greasepenciledit_clean_loose(bpy.types.Operator):
    bl_idname = "button.action_greasepenciledit_clean_loose"
    bl_label = "清除松散点"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.ops.grease_pencil.clean_loose('INVOKE_DEFAULT')
        return {'FINISHED'}
    
class BUTTON_ACTION_OT_greasepenciledit_frame_clean_duplicate(bpy.types.Operator):
    bl_idname = "button.action_greasepenciledit_frame_clean_duplicate"
    bl_label = "清理重复帧"
    bl_options = {'REGISTER', 'UNDO'}

    selected: bpy.props.BoolProperty(
        default=False
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
        col_right.prop(self, "selected",text="选中项")

    def execute(self, context):
        bpy.ops.grease_pencil.frame_clean_duplicate(selected=self.selected)
        return {'FINISHED'}

class BUTTON_ACTION_OT_greasepenciledit_stroke_merge_by_distance(bpy.types.Operator):
    bl_idname = "button.action_greasepenciledit_stroke_merge_by_distance"
    bl_label = "按间距合并"
    bl_options = {'REGISTER', 'UNDO'}

    threshold: bpy.props.FloatProperty(
        name="",
        default=0.001,
        min=0.0,
        max=100.0,
        step=0.1,
        precision=3,
    )

    use_unselected: bpy.props.BoolProperty(
        name="未选中项",
        default=False,
    )

    def invoke(self, context, event):
        return self.execute(context)
    
    def draw(self, context):
        layout = self.layout
        split = layout.row().split(factor=0.4)

        col_left = split.column()
        col_left.alignment = 'RIGHT'
        col_right = split.column()

        col_left.label(text="阈值")
        col_right.prop(self, "threshold")

        col_left.label(text="")
        col_right.prop(self, "use_unselected")

    def execute(self, context):
        bpy.ops.grease_pencil.stroke_merge_by_distance(threshold=self.threshold, use_unselected=self.use_unselected)
        return {'FINISHED'}

class BUTTON_ACTION_OT_greasepenciledit_reproject_menu(bpy.types.Operator):
    bl_idname = "button.action_greasepenciledit_reproject_menu"
    bl_label = "重投影笔画"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.ops.grease_pencil.reproject('INVOKE_DEFAULT')
        return {'FINISHED'}
    
class BUTTON_ACTION_OT_greasepenciledit_extrude_move(bpy.types.Operator):
    bl_idname = "button.action_greasepenciledit_extrude_move"
    bl_label = "挤出"
    bl_description = "快捷键 E"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.ops.grease_pencil.extrude_move('INVOKE_DEFAULT')
        return {'FINISHED'}





classes = (
    BUTTON_ACTION_OT_greasepenciledit_layer_active_menu,
    BUTTON_ACTION_OT_greasepenciledit_layer_add,
    BUTTON_ACTION_OT_greasepenciledit_animation_menu,
    BUTTON_ACTION_OT_greasepenciledit_insert_blank_frame_false,
    BUTTON_ACTION_OT_greasepenciledit_insert_blank_frame_true,
    BUTTON_ACTION_OT_greasepenciledit_frame_duplicate_false,
    BUTTON_ACTION_OT_greasepenciledit_frame_duplicate_true,
    VIEW3D_MT_greasepenciledit_separate_menu,
    BUTTON_ACTION_OT_call_greasepenciledit_separate_menu,
    BUTTON_ACTION_OT_greasepenciledit_cleanup_menu,
    BUTTON_ACTION_OT_greasepenciledit_clean_loose,
    BUTTON_ACTION_OT_greasepenciledit_frame_clean_duplicate,
    BUTTON_ACTION_OT_greasepenciledit_stroke_merge_by_distance,
    BUTTON_ACTION_OT_greasepenciledit_reproject_menu,

    BUTTON_ACTION_OT_greasepenciledit_extrude_move,




)

def register():
    for cls in classes:
        bpy.utils.register_class(cls)

def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)