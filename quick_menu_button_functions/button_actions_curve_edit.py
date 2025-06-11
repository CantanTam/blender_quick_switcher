import bpy

class BUTTON_ACTION_OT_transform_transform_mode_curve_shrinkfatten(bpy.types.Operator):
    bl_idname = "button.action_transform_transform_mode_curve_shrinkfatten"
    bl_label = "半径"
    bl_description = "快捷键 Alt S"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.ops.transform.transform('INVOKE_DEFAULT',mode='CURVE_SHRINKFATTEN')
        return {'FINISHED'}

class BUTTON_ACTION_OT_curveedit_select_nth(bpy.types.Operator):
    bl_idname = "button.action_curveedit_select_nth"
    bl_label = "间隔式弃选"
    bl_options = {'REGISTER', 'UNDO'}

    skip: bpy.props.IntProperty(
        default=1,
        min=1,
        soft_max=100,
    )

    nth: bpy.props.IntProperty(
        default=1,
        min=1,
        soft_max=100,
    )

    offset: bpy.props.IntProperty(
        default=0,
        soft_min=-100,
        soft_max=100,
    )

    def invoke(self, context, event):
        return self.execute(context)

    def draw(self, context):
        layout = self.layout
        split = layout.row().split(factor=0.4)
        
        col_left = split.column()
        col_left.alignment = 'RIGHT'
        col_right = split.column()

        col_left.label(text="弃选项")
        col_right.prop(self, "skip", text="")

        col_left.label(text="选中项")
        col_right.prop(self, "nth", text="")

        col_left.label(text="偏移量")
        col_right.prop(self, "offset", text="")

    def execute(self, context):
        try:
            bpy.ops.curve.select_nth(skip=self.skip, nth=self.nth, offset=self.offset)
        except RuntimeError:
            self.report({'ERROR'}, "曲线没有活动点")
            return {'CANCELLED'}
        return {'FINISHED'}

class BUTTON_ACTION_OT_curveedit_select_first(bpy.types.Operator):
    bl_idname = "button.action_curveedit_select_first"
    bl_label = "选中/弃选首点"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.ops.curve.de_select_first()
        return {'FINISHED'}

class BUTTON_ACTION_OT_curveedit_select_last(bpy.types.Operator):
    bl_idname = "button.action_curveedit_select_last"
    bl_label = "选中/弃选末点"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.ops.curve.de_select_last()
        return {'FINISHED'}
    
class BUTTON_ACTION_OT_curveedit_select_row(bpy.types.Operator):
    bl_idname = "button.action_curveedit_select_row"
    bl_label = "控制点行"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.ops.curve.select_row()
        return {'FINISHED'}

class BUTTON_ACTION_OT_curveedit_spin(bpy.types.Operator):
    bl_idname = "button.action_curveedit_spin"
    bl_label = "旋绕"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        return bpy.context.mode == 'EDIT_SURFACE'

    center: bpy.props.FloatVectorProperty(
        default=(0.0, 0.0, 0.0),
        subtype='TRANSLATION',
    )

    axis: bpy.props.FloatVectorProperty(
        default=(0.0, 0.0, 0.0),
        subtype='DIRECTION',
        min=-1.0,
        max=1.0,
        precision=3,
    )

    def invoke(self, context, event):
        return self.execute(context)
    
    def draw(self, context):
        layout = self.layout
        split = layout.row().split(factor=0.4)

        col_left = split.column()
        col_left.alignment = "RIGHT"
        col_right = split.column()

        col_l = col_left.column(align=True)
        col_l.alignment = "RIGHT"
        col_l.label(text="中心 X")
        col_l.label(text="Y")
        col_l.label(text="Z")

        col_r = col_right.column(align=True)
        col_r.prop(self, "center", index=0, text="")
        col_r.prop(self, "center", index=1, text="")
        col_r.prop(self, "center", index=2, text="")

        col_l = col_left.column(align=True)
        col_l.alignment = "RIGHT"
        col_l.label(text="轴向 X")
        col_l.label(text="Y")
        col_l.label(text="Z")

        col_r = col_right.column(align=True)
        col_r.prop(self, "axis", index=0, text="")
        col_r.prop(self, "axis", index=1, text="")
        col_r.prop(self, "axis", index=2, text="")

    def execute(self, context):
        bpy.ops.curve.spin(center=self.center, axis=self.axis)
        return {'FINISHED'}

class BUTTON_ACTION_OT_curveedit_split(bpy.types.Operator):
    bl_idname = "button.action_curveedit_split"
    bl_label = "拆分"
    bl_description = "快捷键 Y"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.ops.curve.split()
        return {'FINISHED'}

class BUTTON_ACTION_OT_curveedit_separate(bpy.types.Operator):
    bl_idname = "button.action_curveedit_separate"
    bl_label = "分离"
    bl_description = "快捷键 P"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.ops.curve.separate('INVOKE_DEFAULT')
        return {'FINISHED'}
    
class BUTTON_ACTION_OT_curveedit_cyclic_toggle(bpy.types.Operator):
    bl_idname = "button.action_curveedit_cyclic_toggle"
    bl_label = "切换循环"
    bl_description = "快捷键 Alt C"
    bl_options = {'REGISTER', 'UNDO'}

    direction: bpy.props.EnumProperty(
        items=[
            ('CYCLIC_U', "U 向循环", ""),
            ('CYCLIC_V', "V 向循环", ""),
        ],
        default='CYCLIC_U'
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
        bpy.ops.curve.cyclic_toggle(direction=self.direction)
        return {'FINISHED'}
    
class BUTTON_ACTION_OT_curveedit_spline_type_set(bpy.types.Operator):
    bl_idname = "button.action_curveedit_spline_type_set"
    bl_label = "设置样条类型"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        return bpy.context.mode == 'EDIT_CURVE'
    
    def execute(self, context):
        bpy.ops.curve.spline_type_set('INVOKE_DEFAULT')
        return {'FINISHED'}
    
class BUTTON_ACTION_OT_curveedit_curve_clean_menu(bpy.types.Operator):
    bl_idname = "button.action_curveedit_curve_clean_menu"
    bl_label = "清理"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        return bpy.context.mode == 'EDIT_CURVE'
    
    def execute(self, context):
        bpy.ops.wm.call_menu(name="VIEW3D_MT_edit_curve_clean")
        return {'FINISHED'}

class BUTTON_ACTION_OT_curveedit_decimate(bpy.types.Operator):
    bl_idname = "button.action_curveedit_decimate"
    bl_label = "精简曲线"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        return bpy.context.mode == 'EDIT_CURVE'

    ratio: bpy.props.FloatProperty(
        default=1,
        min=0,
        max=1,
        subtype='FACTOR',
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

        col_left.label(text="比率")
        col_right.prop(self, "ratio", text="")

    def execute(self, context):
        bpy.ops.curve.decimate(ratio=self.ratio)
        return {'FINISHED'}


classes = (
    BUTTON_ACTION_OT_transform_transform_mode_curve_shrinkfatten,
    BUTTON_ACTION_OT_curveedit_select_nth,
    BUTTON_ACTION_OT_curveedit_select_first,
    BUTTON_ACTION_OT_curveedit_select_last,
    BUTTON_ACTION_OT_curveedit_select_row,

    BUTTON_ACTION_OT_curveedit_spin,
    BUTTON_ACTION_OT_curveedit_split,
    BUTTON_ACTION_OT_curveedit_separate,
    BUTTON_ACTION_OT_curveedit_cyclic_toggle,
    BUTTON_ACTION_OT_curveedit_spline_type_set,
    BUTTON_ACTION_OT_curveedit_curve_clean_menu,
    BUTTON_ACTION_OT_curveedit_decimate,





)

def register():
    for cls in classes:
        bpy.utils.register_class(cls)

def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)