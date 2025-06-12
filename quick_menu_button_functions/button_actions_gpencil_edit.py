import bpy

class ACTION_OT_gpenciledit_transform_shrink_fatten(bpy.types.Operator):
    bl_idname = "action.gpenciledit_transform_shrink_fatten"
    bl_label = "法向缩放"
    bl_description = "快捷键 Alt S"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.ops.transform.transform('INVOKE_DEFAULT',mode='GPENCIL_SHRINKFATTEN')
        return {'FINISHED'}

class ACTION_OT_gpenciledit_layer_active_menu(bpy.types.Operator):
    bl_idname = "action.gpenciledit_layer_active_menu"
    bl_label = "活动层"
    bl_description = "快捷键 Y"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.ops.wm.call_menu(name="GPENCIL_MT_layer_active")
        return {'FINISHED'}
    
class ACTION_OT_gpenciledit_layer_add(bpy.types.Operator):
    bl_idname = "action.gpenciledit_layer_add"
    bl_label = "新建层"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.ops.gpencil.layer_add('INVOKE_DEFAULT', layer=-1)
        return {'FINISHED'}
    
class ACTION_OT_gpenciledit_animation_menu(bpy.types.Operator):
    bl_idname = "action.gpenciledit_animation_menu"
    bl_label = "动画"
    bl_description = "快捷键 I"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.ops.wm.call_menu(name="VIEW3D_MT_gpencil_animation")
        return {'FINISHED'}

class ACTION_OT_gpenciledit_blank_frame_add_false(bpy.types.Operator):
    bl_idname = "action.gpenciledit_blank_frame_add_false"
    bl_label = "插入空白帧"
    bl_options = {'REGISTER', 'UNDO'}

    all_layers: bpy.props.BoolProperty(
        name="全部层",
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
        col_right.prop(self, "all_layers")

    def execute(self, context):
        bpy.ops.gpencil.blank_frame_add(all_layers=self.all_layers)
        return {'FINISHED'}
    
class ACTION_OT_gpenciledit_blank_frame_add_true(bpy.types.Operator):
    bl_idname = "action.gpenciledit_blank_frame_add_true"
    bl_label = "插入空白帧"
    bl_options = {'REGISTER', 'UNDO'}

    all_layers: bpy.props.BoolProperty(
        name="全部层",
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
        col_right.prop(self, "all_layers")

    def execute(self, context):
        bpy.ops.gpencil.blank_frame_add(all_layers=self.all_layers)
        return {'FINISHED'}

class ACTION_OT_gpenciledit_frame_duplicate_active(bpy.types.Operator):
    bl_idname = "action.gpenciledit_frame_duplicate_active"
    bl_label = "复制帧"
    bl_options = {'REGISTER', 'UNDO'}

    mode: bpy.props.EnumProperty(
        name="",
        items=[
            ('ACTIVE', "活动项", ""),
            ('ALL', "全部", ""),
        ],
        default='ACTIVE'
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
        bpy.ops.gpencil.frame_duplicate(mode=self.mode)
        return {'FINISHED'}

class ACTION_OT_gpenciledit_frame_duplicate_all(bpy.types.Operator):
    bl_idname = "action.gpenciledit_frame_duplicate_all"
    bl_label = "复制帧"
    bl_options = {'REGISTER', 'UNDO'}

    mode: bpy.props.EnumProperty(
        name="",
        items=[
            ('ACTIVE', "活动项", ""),
            ('ALL', "全部", ""),
        ],
        default='ALL'
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
        bpy.ops.gpencil.frame_duplicate(mode=self.mode)
        return {'FINISHED'}

class VIEW3D_MT_gpenciledit_stroke_separate_menu(bpy.types.Menu):
    bl_label = "分离笔画"
    bl_idname = "popup.gpenciledit_stroke_separate_menu"
    bl_options = {'SEARCH_ON_KEY_PRESS'}

    def draw(self, context):
        layout = self.layout
        layout.operator("gpencil.stroke_separate", text="选中控制点").mode='POINT'
        layout.operator("gpencil.stroke_separate", text="选中笔画").mode='STROKE'
        layout.operator("gpencil.stroke_separate", text="活动层").mode='LAYER'

class ACTION_OT_call_gpenciledit_stroke_separate_menu(bpy.types.Operator):
    bl_idname = "action.call_gpenciledit_stroke_separate_menu"
    bl_label = "分离"
    bl_description = "快捷键 P"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.ops.wm.call_menu(name="popup.gpenciledit_stroke_separate_menu")
        return {'FINISHED'}
    
class ACTION_OT_call_gpenciledit_stroke_split(bpy.types.Operator):
    bl_idname = "action.call_gpenciledit_stroke_split"
    bl_label = "拆分"
    bl_description = "快捷键 V"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.ops.gpencil.stroke_split()
        return {'FINISHED'}
    
class ACTION_OT_gpenciledit_cleanup_menu(bpy.types.Operator):
    bl_idname = "action.gpenciledit_cleanup_menu"
    bl_label = "清理"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.ops.wm.call_menu(name="GPENCIL_MT_cleanup")
        return {'FINISHED'}

class ACTION_OT_gpenciledit_frame_clean_fill_active(bpy.types.Operator):
    bl_idname = "action.gpenciledit_frame_clean_fill_active"
    bl_label = "清除填充边界"
    bl_options = {'REGISTER', 'UNDO'}

    mode: bpy.props.EnumProperty(
        name="模式",
        items=[
            ('ACTIVE', "仅活动帧", ""),
            ('ALL', "全部帧", ""),
        ],
        default='ACTIVE'
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
        bpy.ops.gpencil.frame_clean_fill(mode=self.mode)
        return {'FINISHED'}
    
class ACTION_OT_gpenciledit_frame_clean_fill_all(bpy.types.Operator):
    bl_idname = "action.gpenciledit_frame_clean_fill_all"
    bl_label = "清除填充边界"
    bl_options = {'REGISTER', 'UNDO'}

    mode: bpy.props.EnumProperty(
        name="模式",
        items=[
            ('ACTIVE', "仅活动帧", ""),
            ('ALL', "全部帧", ""),
        ],
        default='ALL'
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
        bpy.ops.gpencil.frame_clean_fill(mode=self.mode)
        return {'FINISHED'}
    
class ACTION_OT_gpenciledit_frame_clean_loose(bpy.types.Operator):
    bl_idname = "action.gpenciledit_frame_clean_loose"
    bl_label = "清除松散点"
    bl_options = {'REGISTER', 'UNDO'}

    limit: bpy.props.IntProperty(
        name="",
        default=1,
        min=1
    )

    def invoke(self, context, event):
        return self.execute(context)
    
    def draw(self, context):
        layout = self.layout
        split = layout.row().split(factor=0.4)

        col_left = split.column()
        col_left.alignment = 'RIGHT'
        col_right = split.column()

        col_left.label(text="限制")
        col_right.prop(self, "limit")

    def execute(self, context):
        bpy.ops.gpencil.frame_clean_loose(limit=self.limit)
        return {'FINISHED'}
    
class ACTION_OT_gpenciledit_stroke_merge_by_distance(bpy.types.Operator):
    bl_idname = "action.gpenciledit_stroke_merge_by_distance"
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
        bpy.ops.gpencil.stroke_merge_by_distance(threshold=self.threshold, use_unselected=self.use_unselected)
        return {'FINISHED'}
    
class ACTION_OT_gpenciledit_frame_clean_duplicate(bpy.types.Operator):
    bl_idname = "action.gpenciledit_frame_clean_duplicate"
    bl_label = "清理重复帧"
    bl_options = {'REGISTER', 'UNDO'}

    type: bpy.props.EnumProperty(
        name="",
        items=[
            ('ALL', "全部帧", ""),
            ('SELECTED', "所选帧", "")
        ],
        default='ALL'
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
        bpy.ops.gpencil.frame_clean_duplicate(type=self.type)
        return {'FINISHED'}

class ACTION_OT_gpenciledit_recalc_geometry(bpy.types.Operator):
    bl_idname = "action.gpenciledit_recalc_geometry"
    bl_label = "重新计算几何"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.ops.gpencil.recalc_geometry()
        return {'FINISHED'}
    
class VIEW3D_MT_gpenciledit_reproject_menu(bpy.types.Menu):
    bl_label = "重投影笔画"
    bl_idname = "popup.gpenciledit_reproject_menu"
    bl_options = {'SEARCH_ON_KEY_PRESS'}

    def draw(self, context):
        layout = self.layout
        layout.operator("gpencil.reproject", text="前").type='FRONT'
        layout.operator("gpencil.reproject", text="边").type='SIDE'
        layout.operator("gpencil.reproject", text="顶").type='TOP'
        layout.operator("gpencil.reproject", text="视图").type='VIEW'
        layout.operator("gpencil.reproject", text="表(曲)面").type='SURFACE'
        layout.operator("gpencil.reproject", text="游标").type='CURSOR'

class ACTION_OT_call_gpenciledit_reproject_menu(bpy.types.Operator):
    bl_idname = "action.call_gpenciledit_reproject_menu"
    bl_label = "重投影笔画"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.ops.wm.call_menu(name="popup.gpenciledit_reproject_menu")
        return {'FINISHED'}

class ACTION_OT_gpenciledit_stroke_subdivide(bpy.types.Operator):
    bl_idname = "action.gpenciledit_stroke_subdivide"
    bl_label = "细分笔画"
    bl_options = {'REGISTER', 'UNDO'}

    number_cuts: bpy.props.IntProperty(
        default=1,
        min=1,
        max=10
    )

    factor: bpy.props.FloatProperty(
        default=0.0,
        min=0.0,
        max=2.0
    )

    repeat: bpy.props.IntProperty(
        default=1,
        min=1,
        max=10
    )

    only_selected: bpy.props.BoolProperty(
        default=True
    )

    smooth_position: bpy.props.BoolProperty(
        default=True
    )

    smooth_thickness: bpy.props.BoolProperty(
        default=True
    )

    smooth_strength: bpy.props.BoolProperty(
        default=False
    )

    smooth_uv: bpy.props.BoolProperty(
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

        col_left.label(text="平滑")
        col_right.prop(self, "factor", text="")

        col_left.label(text="重复")
        col_right.prop(self, "repeat", text="")

        col_left.label(text="")
        col_right.prop(self, "only_selected",text="选中控制点")

        col_left.label(text="")
        col_right.prop(self, "smooth_position",text="位置")

        col_left.label(text="")
        col_right.prop(self, "smooth_thickness",text="厚(宽)度")

        col_left.label(text="")
        col_right.prop(self, "smooth_strength",text="强度/力度")

        col_left.label(text="")
        col_right.prop(self, "smooth_uv",text="UV")

    def execute(self, context):
        bpy.ops.gpencil.stroke_subdivide(
            number_cuts=self.number_cuts,
            factor=self.factor,
            repeat=self.repeat,
            only_selected=self.only_selected,
            smooth_position=self.smooth_position,
            smooth_thickness=self.smooth_thickness,
            smooth_strength=self.smooth_strength,
            smooth_uv=self.smooth_uv
        )
        return {'FINISHED'}

class ACTION_OT_call_gpenciledit_simplify_menu(bpy.types.Operator):
    bl_idname = "action.call_gpenciledit_simplify_menu"
    bl_label = "简化笔画"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.ops.wm.call_menu(name="VIEW3D_MT_gpencil_simplify")
        return {'FINISHED'}

class ACTION_OT_call_gpenciledit_stroke_trim(bpy.types.Operator):
    bl_idname = "action.call_gpenciledit_stroke_trim"
    bl_label = "修剪笔画"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.ops.gpencil.stroke_trim()
        return {'FINISHED'}

class ACTION_OT_gpenciledit_stroke_outline(bpy.types.Operator):
    bl_idname = "action.gpenciledit_stroke_outline"
    bl_label = "将笔画转换为轮廓"
    bl_options = {'REGISTER', 'UNDO'}

    view_mode: bpy.props.EnumProperty(
        items=[
            ('VIEW', "视图", ""),
            ('FRONT', "前", ""),
            ('SIDE', "边", ""),
            ('TOP', "顶", ""),
            ('CAMERA', "摄像机", "")
        ],
        default='VIEW'
    )

    material_mode: bpy.props.EnumProperty(
        items=[
            ('ACTIVE', "活动材质", ""),
            ('KEEP', "保留材质", ""),
            ('NEW', "新材质", "")
        ],
        default='ACTIVE'
    )

    thickness: bpy.props.IntProperty(
        default=1,
        min=1,
        max=1000
    )

    keep: bpy.props.BoolProperty(
        default=True
    )

    subdivisions: bpy.props.IntProperty(
        default=3,
        min=0,
        max=10
    )

    length: bpy.props.FloatProperty(
        default=0.0,
        min=0.0,
        max=100.0,
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

        col_left.label(text="视图")
        col_right.prop(self, "view_mode", text="")

        col_left.label(text="材质模式")
        col_right.prop(self, "material_mode", text="")

        col_left.label(text="厚(宽)度")
        col_right.prop(self, "thickness", text="")

        col_left.label(text="")
        col_right.prop(self, "keep",text="保持形态")

        col_left.label(text="细分")
        col_right.prop(self, "subdivisions",text="")

        col_left.label(text="采样长度")
        col_right.prop(self, "length",text="")

    def execute(self, context):
        bpy.ops.gpencil.stroke_outline(
            view_mode=self.view_mode,
            material_mode=self.material_mode,
            thickness=self.thickness,
            keep=self.keep,
            subdivisions=self.subdivisions,
            length=self.length
        )
        return {'FINISHED'}

class VIEW3D_MT_gpenciledit_stroke_join_menu(bpy.types.Menu):
    bl_label = "合并菜单"
    bl_idname = "popup.gpenciledit_stroke_join_menu"
    bl_options = {'SEARCH_ON_KEY_PRESS'}

    def draw(self, context):
        layout = self.layout
        layout.operator("gpencil.stroke_join", text="合并").type='JOIN'
        layout.operator("gpencil.stroke_join", text="合并 & 复制").type='JOINCOPY'

class ACTION_OT_call_gpenciledit_stroke_join_menu(bpy.types.Operator):
    bl_idname = "action.call_gpenciledit_stroke_join_menu"
    bl_label = "合并菜单"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.ops.wm.call_menu(name="popup.gpenciledit_stroke_join_menu")
        return {'FINISHED'}

class ACTION_OT_gpenciledit_stroke_join_join(bpy.types.Operator):
    bl_idname = "action.gpenciledit_stroke_join_join"
    bl_label = "合并笔画"
    bl_description = "快捷键 Ctrl J"
    bl_options = {'REGISTER', 'UNDO'}

    type: bpy.props.EnumProperty(
        items=[
            ('JOIN', "合并", ""),
            ('JOINCOPY', "合并&复制", "")
        ],
        default='JOIN'
    )

    leave_gaps: bpy.props.BoolProperty(
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

        col_left.label(text="类型")
        col_right.prop(self, "type",text="abc", expand=True)

        col_left.label(text="")
        col_right.prop(self, "leave_gaps",text="保留缺口")

    def execute(self, context):
        bpy.ops.gpencil.stroke_join(type=self.type, leave_gaps=self.leave_gaps)
        return {'FINISHED'}

class ACTION_OT_gpenciledit_stroke_join_joincopy(bpy.types.Operator):
    bl_idname = "action.gpenciledit_stroke_join_joincopy"
    bl_label = "合并笔画"
    bl_description = "快捷键 Ctrl Shift J"
    bl_options = {'REGISTER', 'UNDO'}

    type: bpy.props.EnumProperty(
        items=[
            ('JOIN', "合并", ""),
            ('JOINCOPY', "合并&复制", "")
        ],
        default='JOINCOPY'
    )

    leave_gaps: bpy.props.BoolProperty(
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

        col_left.label(text="类型")
        col_right.prop(self, "type",text="abc", expand=True)

        col_left.label(text="")
        col_right.prop(self, "leave_gaps",text="保留缺口")

    def execute(self, context):
        bpy.ops.gpencil.stroke_join(type=self.type, leave_gaps=self.leave_gaps)
        return {'FINISHED'}

class ACTION_OT_call_gpenciledit_move_to_layer_menu(bpy.types.Operator):
    bl_idname = "action.call_gpenciledit_move_to_layer_menu"
    bl_label = "移动到层"
    bl_description = "快捷键 M"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.ops.wm.call_menu(name="GPENCIL_MT_move_to_layer")
        return {'FINISHED'}
    
class ACTION_OT_call_gpenciledit_assign_material_menu(bpy.types.Operator):
    bl_idname = "action.call_gpenciledit_assign_material_menu"
    bl_label = "指定材质"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.ops.wm.call_menu(name="VIEW3D_MT_assign_material")
        return {'FINISHED'}

class ACTION_OT_gpenciledit_set_active_material(bpy.types.Operator):
    bl_idname = "action.gpenciledit_set_active_material"
    bl_label = "设为活动材质"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.ops.gpencil.set_active_material()
        return {'FINISHED'}

class VIEW3D_MT_gpenciledit_stroke_arrange_menu(bpy.types.Menu):
    bl_label = "排列笔画"
    bl_idname = "popup.gpenciledit_stroke_arrange_menu"
    bl_options = {'SEARCH_ON_KEY_PRESS'}

    def draw(self, context):
        layout = self.layout
        layout.operator("gpencil.stroke_arrange", text="移到最前").direction='TOP'
        layout.operator("gpencil.stroke_arrange", text="前移").direction='UP'
        layout.operator("gpencil.stroke_arrange", text="后送").direction='DOWN'
        layout.operator("gpencil.stroke_arrange", text="移到最后").direction='BOTTOM'

class ACTION_OT_call_gpenciledit_stroke_arrange_menu(bpy.types.Operator):
    bl_idname = "action.call_gpenciledit_stroke_arrange_menu"
    bl_label = "排列笔画"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.ops.wm.call_menu(name="popup.gpenciledit_stroke_arrange_menu")
        return {'FINISHED'}
    
class ACTION_OT_gpenciledit_stroke_arrange_top(bpy.types.Operator):
    bl_idname = "action.gpenciledit_stroke_arrange_top"
    bl_label = "整理笔画"
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
        bpy.ops.gpencil.stroke_arrange(direction=self.direction)
        return {'FINISHED'}

class ACTION_OT_gpenciledit_stroke_arrange_up(bpy.types.Operator):
    bl_idname = "action.gpenciledit_stroke_arrange_up"
    bl_label = "整理笔画"
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
        bpy.ops.gpencil.stroke_arrange(direction=self.direction)
        return {'FINISHED'}

class ACTION_OT_gpenciledit_stroke_arrange_down(bpy.types.Operator):
    bl_idname = "action.gpenciledit_stroke_arrange_down"
    bl_label = "整理笔画"
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
        bpy.ops.gpencil.stroke_arrange(direction=self.direction)
        return {'FINISHED'}

class ACTION_OT_gpenciledit_stroke_arrange_bottom(bpy.types.Operator):
    bl_idname = "action.gpenciledit_stroke_arrange_bottom"
    bl_label = "整理笔画"
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
        bpy.ops.gpencil.stroke_arrange(direction=self.direction)
        return {'FINISHED'}

class ACTION_OT_gpenciledit_stroke_cyclical_set(bpy.types.Operator):
    bl_idname = "action.gpenciledit_stroke_cyclical_set"
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

    geometry: bpy.props.BoolProperty(
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

        col_left.label(text="类型")
        col_right.prop(self, "type", text="abc", expand=True)

        col_left.label(text="")
        col_right.prop(self, "geometry", text="创建几何体")

    def execute(self, context):
        bpy.ops.gpencil.stroke_cyclical_set(type=self.type, geometry=self.geometry)
        return {'FINISHED'}

class ACTION_OT_gpenciledit_stroke_cyclical_set_toggle(bpy.types.Operator):
    bl_idname = "action.gpenciledit_stroke_cyclical_set_toggle"
    bl_label = "设置闭合状态"
    bl_options = {'REGISTER', 'UNDO'}

    type: bpy.props.EnumProperty(
        items=[
            ('CLOSE', "闭合全部", ""),
            ('OPEN', "敞开全部", ""),
            ('TOGGLE', "切换", "")
        ],
        default='TOGGLE'
    )

    geometry: bpy.props.BoolProperty(
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

        col_left.label(text="类型")
        col_right.prop(self, "type", text="abc", expand=True)

        col_left.label(text="")
        col_right.prop(self, "geometry", text="创建几何体")

    def execute(self, context):
        bpy.ops.gpencil.stroke_cyclical_set(type=self.type, geometry=self.geometry)
        return {'FINISHED'}
    
class VIEW3D_MT_gpenciledit_stroke_caps_set_menu(bpy.types.Menu):
    bl_label = "切换封顶类型"
    bl_idname = "popup.gpenciledit_stroke_caps_set_menu"
    bl_options = {'SEARCH_ON_KEY_PRESS'}

    def draw(self, context):
        layout = self.layout
        layout.operator("gpencil.stroke_caps_set", text="两者").type='TOGGLE'
        layout.operator("gpencil.stroke_caps_set", text="起始").type='START'
        layout.operator("gpencil.stroke_caps_set", text="结束点").type='END'
        layout.operator("gpencil.stroke_caps_set", text="默认").type='DEFAULT'

class ACTION_OT_call_gpenciledit_stroke_caps_set_menu(bpy.types.Operator):
    bl_idname = "action.call_gpenciledit_stroke_caps_set_menu"
    bl_label = "切换封顶类型"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.ops.wm.call_menu(name="popup.gpenciledit_stroke_caps_set_menu")
        return {'FINISHED'}

class ACTION_OT_gpenciledit_stroke_flip(bpy.types.Operator):
    bl_idname = "action.gpenciledit_stroke_flip"
    bl_label = "切换方向"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.ops.gpencil.stroke_flip()
        return {'FINISHED'}
    
class ACTION_OT_gpenciledit_stroke_start_set(bpy.types.Operator):
    bl_idname = "action.gpenciledit_stroke_start_set"
    bl_label = "设置起始点"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.ops.gpencil.stroke_start_set()
        return {'FINISHED'}

class ACTION_OT_gpenciledit_stroke_normalize_thickness(bpy.types.Operator):
    bl_idname = "action.gpenciledit_stroke_normalize_thickness"
    bl_label = "规格化笔画"
    bl_options = {'REGISTER', 'UNDO'}

    mode: bpy.props.EnumProperty(
        items=[
            ('THICKNESS', "厚(宽)度", ""),
            ('OPACITY', "不透明度", "")
        ],
        default='THICKNESS'
    )

    factor: bpy.props.FloatProperty(
        default=1.0,
        min=0.0,
        max=1.0,
        subtype='FACTOR',
    )

    value: bpy.props.IntProperty(
        default=10,
        min=0,
        max=1000,
    )

    def invoke(self, context, event):
        return self.execute(context)

    def draw(self, context):
        layout = self.layout
        split = layout.row().split(factor=0.4)

        col_left = split.column(align=True)
        col_left.alignment = 'RIGHT'
        col_left.label(text="模式")
        col_left.label(text="")
        if self.mode == 'THICKNESS':
            col_left.label(text="值(明度)")
        if self.mode == 'OPACITY':
            col_left.label(text="系数")

        col_right = split.column()
        col_right.prop(self, "mode", text="abc", expand=True)
        if self.mode == 'THICKNESS':
            col_right.prop(self, "value", text="")
        if self.mode == 'OPACITY':
            col_right.prop(self, "factor", text="")

    def execute(self, context):
        bpy.ops.gpencil.stroke_normalize(mode=self.mode, factor=self.factor, value=self.value)
        return {'FINISHED'}
    
class ACTION_OT_gpenciledit_stroke_normalize_opacity(bpy.types.Operator):
    bl_idname = "action.gpenciledit_stroke_normalize_opacity"
    bl_label = "规格化笔画"
    bl_options = {'REGISTER', 'UNDO'}

    mode: bpy.props.EnumProperty(
        items=[
            ('THICKNESS', "厚(宽)度", ""),
            ('OPACITY', "不透明度", "")
        ],
        default='OPACITY'
    )

    factor: bpy.props.FloatProperty(
        default=1.0,
        min=0.0,
        max=1.0,
        subtype='FACTOR',
    )

    value: bpy.props.IntProperty(
        default=10,
        min=0,
        max=1000,
    )

    def invoke(self, context, event):
        return self.execute(context)

    def draw(self, context):
        layout = self.layout
        split = layout.row().split(factor=0.4)

        col_left = split.column(align=True)
        col_left.alignment = 'RIGHT'
        col_left.label(text="模式")
        col_left.label(text="")
        if self.mode == 'THICKNESS':
            col_left.label(text="值(明度)")
        if self.mode == 'OPACITY':
            col_left.label(text="系数")

        col_right = split.column()
        col_right.prop(self, "mode", text="abc", expand=True)
        if self.mode == 'THICKNESS':
            col_right.prop(self, "value", text="")
        if self.mode == 'OPACITY':
            col_right.prop(self, "factor", text="")

    def execute(self, context):
        bpy.ops.gpencil.stroke_normalize(mode=self.mode, factor=self.factor, value=self.value)
        return {'FINISHED'}

class ACTION_OT_gpenciledit_reset_transform_fill(bpy.types.Operator):
    bl_idname = "action.gpenciledit_reset_transform_fill"
    bl_label = "重置填充变换"
    bl_options = {'REGISTER', 'UNDO'}

    mode: bpy.props.EnumProperty(
        items=[
            ('ALL', "全部", ""),
            ('TRANSLATE', "移动", ""),
            ('ROTATE', "旋转", ""),
            ('SCALE', "缩放", "")
        ],
        default='ALL'
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
        bpy.ops.gpencil.reset_transform_fill(mode=self.mode)
        return {'FINISHED'}

class ACTION_OT_gpenciledit_extrude_move(bpy.types.Operator):
    bl_idname = "action.gpenciledit_extrude_move"
    bl_label = "挤出"
    bl_description = "快捷键 E"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.ops.gpencil.extrude_move('INVOKE_DEFAULT')
        return {'FINISHED'}

class ACTION_OT_gpenciledit_stroke_smooth(bpy.types.Operator):
    bl_idname = "action.gpenciledit_stroke_smooth"
    bl_label = "平滑笔画"
    bl_options = {'REGISTER', 'UNDO'}

    repeat: bpy.props.IntProperty(
        default=2,
        min=1,
        max=1000
    )

    factor: bpy.props.FloatProperty(
        default=1.0,
        min=0.0,
        max=2.0,
        precision=3
    )

    only_selected: bpy.props.BoolProperty(
        default=True
    )

    smooth_position: bpy.props.BoolProperty(
        default=True
    )

    smooth_thickness: bpy.props.BoolProperty(
        default=True
    )

    smooth_strength: bpy.props.BoolProperty(
        default=False
    )

    smooth_uv: bpy.props.BoolProperty(
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

        col_left.label(text="重复")
        col_right.prop(self, "repeat", text="")

        col_left.label(text="系数")
        col_right.prop(self, "factor", text="")

        col_left.label(text="")
        col_right.prop(self, "only_selected", text="选中控制点")

        col_left.label(text="")
        col_right.prop(self, "smooth_position", text="位置")

        col_left.label(text="")
        col_right.prop(self, "smooth_thickness", text="厚(宽)度")

        col_left.label(text="")
        col_right.prop(self, "smooth_strength", text="强度/力度")

        col_left.label(text="")
        col_right.prop(self, "smooth_uv", text="UV")

    def execute(self, context):
        bpy.ops.gpencil.stroke_smooth(
            repeat=self.repeat,
            factor=self.factor,
            only_selected=self.only_selected,
            smooth_position=self.smooth_position,
            smooth_thickness=self.smooth_thickness,
            smooth_strength=self.smooth_strength,
            smooth_uv=self.smooth_uv)
        return {'FINISHED'}

class ACTION_OT_gpenciledit_stroke_merge(bpy.types.Operator):
    bl_idname = "action.gpenciledit_stroke_merge"
    bl_label = "合并笔画"
    bl_options = {'REGISTER', 'UNDO'}

    mode: bpy.props.EnumProperty(
        items=[
            ('STROKE', "笔画", ""),
            ('POINT', "点", "")
        ],
        default='STROKE'
    )

    back: bpy.props.BoolProperty(
        default=False
    )

    additive: bpy.props.BoolProperty(
        default=False
    )

    cyclic: bpy.props.BoolProperty(
        default=False
    )

    clear_point: bpy.props.BoolProperty(
        default=False
    )

    clear_stroke: bpy.props.BoolProperty(
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

        col_left.label(text="模式")
        col_right.prop(self, "mode", text="abc", expand=True)

        col_left.label(text="")
        col_right.prop(self, "back", text="在后方绘制")

        col_left.label(text="")
        col_right.prop(self, "additive", text="累加绘制")

        col_left.label(text="")
        col_right.prop(self, "cyclic", text="循环")

        col_left.label(text="")
        col_right.prop(self, "clear_point", text="融并控制点")

        col_left.label(text="")
        col_right.prop(self, "clear_stroke", text="删除笔画")

    def execute(self, context):
        bpy.ops.gpencil.stroke_merge(
            mode=self.mode,
            back=self.back,
            additive=self.additive,
            cyclic=self.cyclic,
            clear_point=self.clear_point,
            clear_stroke=self.clear_stroke)
        return {'FINISHED'}

class ACTION_OT_gpenciledit_gpencil_vertex_group_menu(bpy.types.Operator):
    bl_idname = "action.gpenciledit_gpencil_vertex_group_menu"
    bl_label = "顶点组"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.ops.wm.call_menu(name="VIEW3D_MT_gpencil_vertex_group")
        return {'FINISHED'}

classes = (
    ACTION_OT_gpenciledit_transform_shrink_fatten,
    ACTION_OT_gpenciledit_layer_active_menu,
    ACTION_OT_gpenciledit_layer_add,
    ACTION_OT_gpenciledit_animation_menu,
    ACTION_OT_gpenciledit_blank_frame_add_false,
    ACTION_OT_gpenciledit_blank_frame_add_true,
    ACTION_OT_gpenciledit_frame_duplicate_active,
    ACTION_OT_gpenciledit_frame_duplicate_all,
    VIEW3D_MT_gpenciledit_stroke_separate_menu,
    ACTION_OT_call_gpenciledit_stroke_separate_menu,
    ACTION_OT_call_gpenciledit_stroke_split,

    ACTION_OT_gpenciledit_cleanup_menu,
    ACTION_OT_gpenciledit_frame_clean_fill_active,
    ACTION_OT_gpenciledit_frame_clean_fill_all,
    ACTION_OT_gpenciledit_frame_clean_loose,
    ACTION_OT_gpenciledit_stroke_merge_by_distance,
    ACTION_OT_gpenciledit_frame_clean_duplicate,
    ACTION_OT_gpenciledit_recalc_geometry,
    VIEW3D_MT_gpenciledit_reproject_menu,
    ACTION_OT_call_gpenciledit_reproject_menu,

    ACTION_OT_gpenciledit_stroke_subdivide,
    ACTION_OT_call_gpenciledit_simplify_menu,
    ACTION_OT_call_gpenciledit_stroke_trim,
    ACTION_OT_gpenciledit_stroke_outline,
    VIEW3D_MT_gpenciledit_stroke_join_menu,
    ACTION_OT_call_gpenciledit_stroke_join_menu,
    ACTION_OT_gpenciledit_stroke_join_join,
    ACTION_OT_gpenciledit_stroke_join_joincopy,
    ACTION_OT_call_gpenciledit_move_to_layer_menu,
    ACTION_OT_call_gpenciledit_assign_material_menu,
    ACTION_OT_gpenciledit_set_active_material,
    VIEW3D_MT_gpenciledit_stroke_arrange_menu,
    ACTION_OT_call_gpenciledit_stroke_arrange_menu,
    ACTION_OT_gpenciledit_stroke_arrange_top,
    ACTION_OT_gpenciledit_stroke_arrange_up,
    ACTION_OT_gpenciledit_stroke_arrange_down,
    ACTION_OT_gpenciledit_stroke_arrange_bottom,
    ACTION_OT_gpenciledit_stroke_cyclical_set,
    ACTION_OT_gpenciledit_stroke_cyclical_set_toggle,
    VIEW3D_MT_gpenciledit_stroke_caps_set_menu,
    ACTION_OT_call_gpenciledit_stroke_caps_set_menu,
    ACTION_OT_gpenciledit_stroke_flip,
    ACTION_OT_gpenciledit_stroke_start_set,
    ACTION_OT_gpenciledit_stroke_normalize_thickness,
    ACTION_OT_gpenciledit_stroke_normalize_opacity,
    ACTION_OT_gpenciledit_reset_transform_fill,

    ACTION_OT_gpenciledit_extrude_move,
    ACTION_OT_gpenciledit_stroke_smooth,
    ACTION_OT_gpenciledit_stroke_merge,
    ACTION_OT_gpenciledit_gpencil_vertex_group_menu,


)

def register():
    for cls in classes:
        bpy.utils.register_class(cls)

def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)