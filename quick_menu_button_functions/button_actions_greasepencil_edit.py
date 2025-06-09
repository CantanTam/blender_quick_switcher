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

class BUTTON_ACTION_OT_greasepenciledit_stroke_smooth(bpy.types.Operator):
    bl_idname = "button.action_greasepenciledit_stroke_smooth"
    bl_label = "平滑笔画"
    bl_options = {'REGISTER', 'UNDO'}

    iterations: bpy.props.IntProperty(
        default=10,
        min=1,
        max=100,
        soft_max=30,
    )

    factor: bpy.props.FloatProperty(
        default=1.0,
        min=0.0,
        max=1.0,
        precision=3,
        subtype='FACTOR',
    )

    smooth_ends: bpy.props.BoolProperty(
        default=False
    )

    keep_shape: bpy.props.BoolProperty(
        default=False
    )

    smooth_position: bpy.props.BoolProperty(
        default=True
    )

    smooth_radius: bpy.props.BoolProperty(
        default=True
    )

    smooth_opacity: bpy.props.BoolProperty(
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

        col_left.label(text="迭代")
        col_right.prop(self, "iterations", text="")

        col_left.label(text="系数")
        col_right.prop(self, "factor", text="")

        col_left.label(text="")
        col_right.prop(self, "smooth_ends", text="平滑末尾点")

        col_left.label(text="")
        col_right.prop(self, "keep_shape", text="保持形态")

        col_left.label(text="")
        col_right.prop(self, "smooth_position", text="位置")

        col_left.label(text="")
        col_right.prop(self, "smooth_radius", text="半径")

        col_left.label(text="")
        col_right.prop(self, "smooth_opacity", text="不透明度")

    def execute(self, context):
        bpy.ops.grease_pencil.stroke_smooth(
            iterations=self.iterations,
            factor=self.factor,
            smooth_ends=self.smooth_ends,
            keep_shape=self.keep_shape,
            smooth_position=self.smooth_position,
            smooth_radius=self.smooth_radius,
            smooth_opacity=self.smooth_opacity)        
        return {'FINISHED'}

class BUTTON_ACTION_OT_greasepenciledit_vertex_group_menu(bpy.types.Operator):
    bl_idname = "button.action_greasepenciledit_vertex_group_menu"
    bl_label = "顶点组"
    bl_description = "快捷键 Ctrl G"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.ops.wm.call_menu(name="VIEW3D_MT_greasepencil_vertex_group")
        return {'FINISHED'}

class BUTTON_ACTION_OT_greasepenciledit_set_handle_type(bpy.types.Operator):
    bl_idname = "button.action_greasepenciledit_set_handle_type"
    bl_label = "设置控制柄类型"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.ops.grease_pencil.set_handle_type('INVOKE_DEFAULT')
        return {'FINISHED'}
# “笔画”菜单
class BUTTON_ACTION_OT_greasepenciledit_stroke_subdivide(bpy.types.Operator):
    bl_idname = "button.action_greasepenciledit_stroke_subdivide"
    bl_label = "细分笔画"
    bl_options = {'REGISTER', 'UNDO'}

    number_cuts: bpy.props.IntProperty(
        default=1,
        min=1,
        max=32,
        soft_max=5,
    )

    only_selected: bpy.props.BoolProperty(
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

        col_left.label(text="切割次数")
        col_right.prop(self, "number_cuts", text="")

        col_left.label(text="")
        col_right.prop(self, "only_selected", text="选中控制点")

    def execute(self, context):
        bpy.ops.grease_pencil.stroke_subdivide(number_cuts=self.number_cuts, only_selected=self.only_selected)
        return {'FINISHED'}

class BUTTON_ACTION_OT_greasepenciledit_stroke_subdivide_smooth(bpy.types.Operator):
    bl_idname = "button.action_greasepenciledit_stroke_subdivide_smooth"
    bl_label = "细分并平滑笔画"
    bl_options = {'REGISTER', 'UNDO'}

    number_cuts: bpy.props.IntProperty(
        default=1,
        min=1,
        max=32,
        soft_max=5,
    )

    only_selected: bpy.props.BoolProperty(
        default=True
    )

    iterations: bpy.props.IntProperty(
        default=10,
        min=1,
        max=100,
        soft_max=30,
    )

    factor: bpy.props.FloatProperty(
        default=1.0,
        min=0.0,
        max=1.0,
        precision=3,
        subtype='FACTOR',
    )

    smooth_ends: bpy.props.BoolProperty(
        default=False
    )

    keep_shape: bpy.props.BoolProperty(
        default=False
    )

    smooth_position: bpy.props.BoolProperty(
        default=True
    )

    smooth_radius: bpy.props.BoolProperty(
        default=True
    )

    smooth_opacity: bpy.props.BoolProperty(
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

        col_left.label(text="切割次数")
        col_right.prop(self, "number_cuts", text="")

        col_left.label(text="")
        col_right.prop(self, "only_selected", text="选中控制点")

        col_left.label(text="迭代")
        col_right.prop(self, "iterations", text="")

        col_left.label(text="系数")
        col_right.prop(self, "factor", text="")

        col_left.label(text="")
        col_right.prop(self, "smooth_ends", text="平滑末尾点")

        col_left.label(text="")
        col_right.prop(self, "keep_shape", text="保持形态")

        col_left.label(text="")
        col_right.prop(self, "smooth_position", text="位置")

        col_left.label(text="")
        col_right.prop(self, "smooth_radius", text="半径")

        col_left.label(text="")
        col_right.prop(self, "smooth_opacity", text="不透明度")

    def execute(self, context):
        bpy.ops.grease_pencil.stroke_subdivide_smooth(
            GREASE_PENCIL_OT_stroke_subdivide={
                "number_cuts": self.number_cuts,
                "only_selected": self.only_selected
            },
            GREASE_PENCIL_OT_stroke_smooth={
                "iterations": self.iterations,
                "factor": self.factor,
                "smooth_ends": self.smooth_ends,
                "keep_shape": self.keep_shape,
                "smooth_position": self.smooth_position,
                "smooth_radius": self.smooth_radius,
                "smooth_opacity": self.smooth_opacity
            }
        )
        return {'FINISHED'}

class BUTTON_ACTION_OT_greasepenciledit_stroke_simplify(bpy.types.Operator):
    bl_idname = "button.action_greasepenciledit_stroke_simplify"
    bl_label = "简化笔画"
    bl_options = {'REGISTER', 'UNDO'}

    factor: bpy.props.FloatProperty(
        default=0.01,
        min=0.0,
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

        col_left.label(text="系数")
        col_right.prop(self, "factor", text="")

    def execute(self, context):
        bpy.ops.grease_pencil.stroke_simplify(factor=self.factor)
        return {'FINISHED'}

class BUTTON_ACTION_OT_greasepenciledit_join_selection(bpy.types.Operator):
    bl_idname = "button.action_greasepenciledit_join_selection"
    bl_label = "合并笔画"
    bl_description = "快捷键 Ctrl J"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.ops.grease_pencil.join_selection('INVOKE_DEFAULT')
        return {'FINISHED'}

class BUTTON_ACTION_OT_greasepenciledit_join_selection_join(bpy.types.Operator):
    bl_idname = "button.action_greasepenciledit_join_selection_join"
    bl_label = "并入选区"
    bl_description = "快捷键 Ctrl J"
    bl_options = {'REGISTER', 'UNDO'}

    type: bpy.props.EnumProperty(
        items=[
            ('JOIN', "合并", ""),
            ('JOINCOPY', "合并并复制", "")
        ],
        default='JOIN'
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
        col_right.prop(self, "type",text="abc", expand=True)

    def execute(self, context):
        bpy.ops.grease_pencil.join_selection(type=self.type)
        return {'FINISHED'}

class BUTTON_ACTION_OT_greasepenciledit_join_selection_joincopy(bpy.types.Operator):
    bl_idname = "button.action_greasepenciledit_join_selection_joincopy"
    bl_label = "并入选区"
    bl_description = "快捷键 Ctrl Shift J"
    bl_options = {'REGISTER', 'UNDO'}

    type: bpy.props.EnumProperty(
        items=[
            ('JOIN', "合并", ""),
            ('JOINCOPY', "合并并复制", "")
        ],
        default='JOINCOPY'
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
        col_right.prop(self, "type",text="abc", expand=True)

    def execute(self, context):
        bpy.ops.grease_pencil.join_selection(type=self.type)
        return {'FINISHED'}

class BUTTON_ACTION_OT_greasepenciledit_move_to_layer_menu(bpy.types.Operator):
    bl_idname = "button.action_greasepenciledit_move_to_layer_menu"
    bl_label = "移动到层"
    bl_description = "快捷键 M"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.ops.wm.call_menu(name="GREASE_PENCIL_MT_move_to_layer")
        return {'FINISHED'}

class BUTTON_ACTION_OT_greasepenciledit_assign_material_menu(bpy.types.Operator):
    bl_idname = "button.action_greasepenciledit_assign_material_menu"
    bl_label = "指定材质"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.ops.wm.call_menu(name="VIEW3D_MT_grease_pencil_assign_material")
        return {'FINISHED'}

class BUTTON_ACTION_OT_greasepenciledit_set_active_material(bpy.types.Operator):
    bl_idname = "button.action_greasepenciledit_set_active_material"
    bl_label = "设置活动的材质"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.ops.grease_pencil.set_active_material()
        return {'FINISHED'}

class VIEW3D_MT_greasepenciledit_reorder_menu(bpy.types.Menu):
    bl_label = "排列笔画"
    bl_idname = "popup.greasepenciledit_reorder_menu"
    bl_options = {'SEARCH_ON_KEY_PRESS'}

    def draw(self, context):
        layout = self.layout
        layout.operator("grease_pencil.reorder", text="移到最前").direction='TOP'
        layout.operator("grease_pencil.reorder", text="前移").direction='UP'
        layout.separator()
        layout.operator("grease_pencil.reorder", text="后送").direction='DOWN'
        layout.operator("grease_pencil.reorder", text="移到最后").direction='BOTTOM'

class BUTTON_ACTION_OT_call_greasepenciledit_reorder_menu(bpy.types.Operator):
    bl_idname = "button.action_call_greasepenciledit_reorder_menu"
    bl_label = "排列笔画"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.ops.wm.call_menu(name="popup.greasepenciledit_reorder_menu")
        return {'FINISHED'}

class BUTTON_ACTION_OT_gpenciledit_reorder_top(bpy.types.Operator):
    bl_idname = "button.action_gpenciledit_reorder_top"
    bl_label = "重新排序"
    bl_options = {'REGISTER', 'UNDO'}

    direction: bpy.props.EnumProperty(
        items=[
            ('TOP', "移到最前", ""),
            ('UP', "前移", ""),
            ('DOWN', "后送", ""),
            ('BOTTOM', "移到最后", "")
        ],
        default='TOP'
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
        bpy.ops.grease_pencil.reorder(direction=self.direction)
        return {'FINISHED'}

class BUTTON_ACTION_OT_gpenciledit_reorder_up(bpy.types.Operator):
    bl_idname = "button.action_gpenciledit_reorder_up"
    bl_label = "重新排序"
    bl_options = {'REGISTER', 'UNDO'}

    direction: bpy.props.EnumProperty(
        items=[
            ('TOP', "移到最前", ""),
            ('UP', "前移", ""),
            ('DOWN', "后送", ""),
            ('BOTTOM', "移到最后", "")
        ],
        default='UP'
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
        bpy.ops.grease_pencil.reorder(direction=self.direction)
        return {'FINISHED'}

class BUTTON_ACTION_OT_gpenciledit_reorder_down(bpy.types.Operator):
    bl_idname = "button.action_gpenciledit_reorder_down"
    bl_label = "重新排序"
    bl_options = {'REGISTER', 'UNDO'}

    direction: bpy.props.EnumProperty(
        items=[
            ('TOP', "移到最前", ""),
            ('UP', "前移", ""),
            ('DOWN', "后送", ""),
            ('BOTTOM', "移到最后", "")
        ],
        default='DOWN'
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
        bpy.ops.grease_pencil.reorder(direction=self.direction)
        return {'FINISHED'}

class BUTTON_ACTION_OT_gpenciledit_reorder_bottom(bpy.types.Operator):
    bl_idname = "button.action_gpenciledit_reorder_bottom"
    bl_label = "重新排序"
    bl_options = {'REGISTER', 'UNDO'}

    direction: bpy.props.EnumProperty(
        items=[
            ('TOP', "移到最前", ""),
            ('UP', "前移", ""),
            ('DOWN', "后送", ""),
            ('BOTTOM', "移到最后", "")
        ],
        default='BOTTOM'
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
        bpy.ops.grease_pencil.reorder(direction=self.direction)
        return {'FINISHED'}

class BUTTON_ACTION_OT_greasepenciledit_cyclical_set_close(bpy.types.Operator):
    bl_idname = "button.action_greasepenciledit_cyclical_set_close"
    bl_label = "设置闭合状态"
    bl_description ="快捷键 F"
    bl_options = {'REGISTER', 'UNDO'}

    type: bpy.props.EnumProperty(
        items=[
            ('CLOSE', "闭合全部", ""),
            ('OPEN', "敞开全部", ""),
            ('TOGGLE', "切换", "")
        ],
        default='CLOSE'
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
        bpy.ops.grease_pencil.cyclical_set(type=self.type)
        return {'FINISHED'}

class BUTTON_ACTION_OT_greasepenciledit_cyclical_set_toggle(bpy.types.Operator):
    bl_idname = "button.action_greasepenciledit_cyclical_set_toggle"
    bl_label = "设置闭合状态"
    bl_description ="快捷键 Alt C"
    bl_options = {'REGISTER', 'UNDO'}

    type: bpy.props.EnumProperty(
        items=[
            ('CLOSE', "闭合全部", ""),
            ('OPEN', "敞开全部", ""),
            ('TOGGLE', "切换", "")
        ],
        default='TOGGLE'
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
        bpy.ops.grease_pencil.cyclical_set(type=self.type)
        return {'FINISHED'}

class BUTTON_ACTION_OT_greasepenciledit_caps_set(bpy.types.Operator):
    bl_idname = "button.action_greasepenciledit_caps_set"
    bl_label = "设置端点"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.ops.grease_pencil.caps_set('INVOKE_DEFAULT')
        return {'FINISHED'}

class BUTTON_ACTION_OT_greasepenciledit_stroke_switch_direction(bpy.types.Operator):
    bl_idname = "button.action_greasepenciledit_stroke_switch_direction"
    bl_label = "切换方向"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.ops.grease_pencil.stroke_switch_direction()
        return {'FINISHED'}

class BUTTON_ACTION_OT_greasepenciledit_set_uniform_thickness(bpy.types.Operator):
    bl_idname = "button.action_greasepenciledit_set_uniform_thickness"
    bl_label = "设置统一粗细"
    bl_options = {'REGISTER', 'UNDO'}

    thickness: bpy.props.FloatProperty(
        default=0.1,
        min=0,
        max=1000,
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

        col_left.label(text="厚(宽)度")
        col_right.prop(self, "thickness", text="")

    def execute(self, context):
        bpy.ops.grease_pencil.set_uniform_thickness(thickness=self.thickness)
        return {'FINISHED'}

class BUTTON_ACTION_OT_greasepenciledit_set_uniform_opacity(bpy.types.Operator):
    bl_idname = "button.action_greasepenciledit_set_uniform_opacity"
    bl_label = "设置统一不透明度"
    bl_options = {'REGISTER', 'UNDO'}

    opacity: bpy.props.FloatProperty(
        default=1.0,
        min=0.0,
        max=1.0,
        subtype='FACTOR',
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

        col_left.label(text="不透明度")
        col_right.prop(self, "opacity", text="")

    def execute(self, context):
        bpy.ops.grease_pencil.set_uniform_opacity(opacity=self.opacity)
        return {'FINISHED'}

class BUTTON_ACTION_OT_greasepenciledit_set_curve_type(bpy.types.Operator):
    bl_idname = "button.action_greasepenciledit_set_curve_type"
    bl_label = "设置曲线类型"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.ops.grease_pencil.set_curve_type('INVOKE_DEFAULT')
        return {'FINISHED'}

class BUTTON_ACTION_OT_greasepenciledit_set_curve_resolution(bpy.types.Operator):
    bl_idname = "button.action_greasepenciledit_set_curve_resolution"
    bl_label = "设置曲线分辨率"
    bl_options = {'REGISTER', 'UNDO'}

    resolution: bpy.props.IntProperty(
        default=12,
        min=1,
        max=10000,
        soft_max=64,
    )

    def invoke(self, context, event):
        return self.execute(context)

    def draw(self, context):
        layout = self.layout
        split = layout.row().split(factor=0.4)

        col_left = split.column()
        col_left.alignment = 'RIGHT'
        col_right = split.column()

        col_left.label(text="分辨率")
        col_right.prop(self, "resolution", text="")

    def execute(self, context):
        bpy.ops.grease_pencil.set_curve_resolution(resolution=self.resolution)
        return {'FINISHED'}

class BUTTON_ACTION_OT_greasepenciledit_reset_uvs(bpy.types.Operator):
    bl_idname = "button.action_greasepenciledit_reset_uvs"
    bl_label = "重置UV"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.ops.grease_pencil.reset_uvs()
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
    BUTTON_ACTION_OT_greasepenciledit_stroke_smooth,
    BUTTON_ACTION_OT_greasepenciledit_vertex_group_menu,
    BUTTON_ACTION_OT_greasepenciledit_set_handle_type,

    BUTTON_ACTION_OT_greasepenciledit_stroke_subdivide,
    BUTTON_ACTION_OT_greasepenciledit_stroke_subdivide_smooth,
    BUTTON_ACTION_OT_greasepenciledit_stroke_simplify,
    BUTTON_ACTION_OT_greasepenciledit_join_selection,
    BUTTON_ACTION_OT_greasepenciledit_join_selection_join,
    BUTTON_ACTION_OT_greasepenciledit_join_selection_joincopy,
    BUTTON_ACTION_OT_greasepenciledit_move_to_layer_menu,
    BUTTON_ACTION_OT_greasepenciledit_assign_material_menu,
    BUTTON_ACTION_OT_greasepenciledit_set_active_material,
    VIEW3D_MT_greasepenciledit_reorder_menu,
    BUTTON_ACTION_OT_call_greasepenciledit_reorder_menu,
    BUTTON_ACTION_OT_gpenciledit_reorder_top,
    BUTTON_ACTION_OT_gpenciledit_reorder_up,
    BUTTON_ACTION_OT_gpenciledit_reorder_down,
    BUTTON_ACTION_OT_gpenciledit_reorder_bottom,
    BUTTON_ACTION_OT_greasepenciledit_cyclical_set_close,
    BUTTON_ACTION_OT_greasepenciledit_cyclical_set_toggle,
    BUTTON_ACTION_OT_greasepenciledit_caps_set,
    BUTTON_ACTION_OT_greasepenciledit_stroke_switch_direction,
    BUTTON_ACTION_OT_greasepenciledit_set_uniform_thickness,
    BUTTON_ACTION_OT_greasepenciledit_set_uniform_opacity,
    BUTTON_ACTION_OT_greasepenciledit_set_curve_type,
    BUTTON_ACTION_OT_greasepenciledit_set_curve_resolution,
    BUTTON_ACTION_OT_greasepenciledit_reset_uvs,

)

def register():
    for cls in classes:
        bpy.utils.register_class(cls)

def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)