import bpy

# "选择"菜单——按类型全选
class BUTTON_ACTION_OT_object_select_select_by_type_menu(bpy.types.Operator):
    bl_label = ""
    bl_idname = "button.action_object_select_select_by_type_menu"

    def execute(self, context):
        def draw(self, context):
            layout = self.layout
            
            layout.operator("object.select_by_type", text="网格", icon="OUTLINER_OB_MESH").type='MESH'
            layout.operator("object.select_by_type", text="曲线", icon="OUTLINER_OB_CURVE").type='CURVE'
            layout.operator("object.select_by_type", text="表面", icon="OUTLINER_OB_SURFACE").type='SURFACE'
            layout.operator("object.select_by_type", text="元球", icon="OUTLINER_OB_META").type='META'
            layout.operator("object.select_by_type", text="文本", icon="OUTLINER_OB_FONT").type='FONT'
            layout.operator("object.select_by_type", text="毛发曲线", icon="OUTLINER_OB_CURVES").type='CURVES'
            layout.operator("object.select_by_type", text="点云", icon="OUTLINER_OB_POINTCLOUD").type='POINTCLOUD'
            layout.operator("object.select_by_type", text="体积", icon="OUTLINER_OB_VOLUME").type='VOLUME'
            if bpy.app.version >= (4,3,0):
                layout.operator("object.select_by_type", text="蜡笔", icon="OUTLINER_OB_GREASEPENCIL").type='GPENCIL'
                layout.operator("object.select_by_type", text="蜡笔V3版", icon="OUTLINER_OB_GREASEPENCIL").type='GREASEPENCIL'
            else:
                layout.operator("object.select_by_type", text="蜡笔", icon="OUTLINER_OB_GREASEPENCIL").type='GPENCIL'
            layout.separator()
            layout.operator("object.select_by_type", text="骨骼", icon="OUTLINER_OB_ARMATURE").type='ARMATURE'
            layout.operator("object.select_by_type", text="晶格", icon="OUTLINER_OB_LATTICE").type='LATTICE'
            layout.separator()
            layout.operator("object.select_by_type", text="空物体", icon="OUTLINER_OB_EMPTY").type='EMPTY'
            layout.separator()
            layout.operator("object.select_by_type", text="灯光", icon="OUTLINER_OB_LIGHT").type='LIGHT'
            layout.operator("object.select_by_type", text="光照探头", icon="OUTLINER_OB_LIGHTPROBE").type='LIGHT_PROBE'
            layout.separator()
            layout.operator("object.select_by_type", text="摄像机", icon="OUTLINER_OB_CAMERA").type='CAMERA'
            layout.separator()
            layout.operator("object.select_by_type", text="扬声器", icon="OUTLINER_OB_SPEAKER").type='SPEAKER'
        context.window_manager.popup_menu(draw, title="按类型全选")
        return {'FINISHED'}

# “变换”菜单——随机变换
class BUTTON_ACTION_OT_object_transform_randomize_transform(bpy.types.Operator):
    bl_idname = "button.action_object_randomize_transform"
    bl_label = "随机变换"
    bl_options = {'REGISTER', 'UNDO'}

    random_seed: bpy.props.IntProperty(
        name="",
        description="随机生成器的种数量",
        default=0,
        min=0,
        max=10000
    )

    use_delta: bpy.props.BoolProperty(
        name="变换增量",
        description="使用随机变换增量值代替规则变换",
        default=False
    )

    use_loc: bpy.props.BoolProperty(
        name="坐标随机化",
        description="坐标值随机化.",
        default=True
    )

    loc: bpy.props.FloatVectorProperty(
        name="",
        description="物体在各轴向上的最大位移距离",
        size=3,
        default=(0.0, 0.0, 0.0),
        min=-100.0,
        max=100.0,
        subtype='TRANSLATION'
    )

    use_rot: bpy.props.BoolProperty(
        name="旋转随机化",
        description="旋转值随机化",
        default=True
    )

    rot: bpy.props.FloatVectorProperty(
        name="",
        description="各轴向上的最大旋转角度",
        size=3,
        default=(0.0, 0.0, 0.0),
        min=-3.14159,
        max=3.14159,
        subtype='EULER'
    )

    use_scale: bpy.props.BoolProperty(
        name="缩放随机化",
        description="缩放值随机化",
        default=True
    )

    scale_even: bpy.props.BoolProperty(
        name="等比例缩放",
        description="各轴向等比例缩放",
        default=False
    )

    scale: bpy.props.FloatVectorProperty(
        name="",
        description="各轴向上的最大随机缩放值",
        size=3,
        default=(1.0, 1.0, 1.0),
        min=-100.0,
        max=100.0,
        subtype='XYZ'
    )

    def invoke(self, context, event):
        return self.execute(context)

    def draw(self, context):
        layout = self.layout
        split = layout.row().split(factor=0.4)

        col_left = split.column()
        col_left.alignment = "RIGHT"
        col_right = split.column()

        # 随机种子、变换增量
        col_left.label(text="随机种")
        col_right.prop(self, "random_seed", text="")

        col_left.label(text="")
        col_right.prop(self, "use_delta", text="变换增量")

        # 坐标随机化
        col_left.label(text="")
        col_right.prop(self, "use_loc", text="坐标随机化")

        # 位置 XYZ（左三行对右三行）
        col_l = col_left.column(align=True)
        col_l.alignment = "RIGHT"
        col_l.label(text="位置 X")
        col_l.label(text="Y")
        col_l.label(text="Z")

        col_r = col_right.column(align=True)
        col_r.prop(self, "loc", index=0, text="")
        col_r.prop(self, "loc", index=1, text="")
        col_r.prop(self, "loc", index=2, text="")

        # 旋转随机化
        col_left.label(text="")
        col_right.prop(self, "use_rot", text="旋转随机化")

        # 旋转 XYZ
        col_l = col_left.column(align=True)
        col_l.alignment = "RIGHT"
        col_l.label(text="旋转 X")
        col_l.label(text="Y")
        col_l.label(text="Z")

        col_r = col_right.column(align=True)
        col_r.prop(self, "rot", index=0, text="")
        col_r.prop(self, "rot", index=1, text="")
        col_r.prop(self, "rot", index=2, text="")

        # 缩放随机化
        col_left.label(text="")
        col_right.prop(self, "use_scale", text="缩放随机化")

        # 等比例缩放
        col_left.label(text="")
        col_right.prop(self, "scale_even", text="等比例缩放")

        # 缩放 XYZ
        col_l = col_left.column(align=True)
        col_l.alignment = "RIGHT"
        col_l.label(text="缩放 ")
        col_l.label(text="")
        col_l.label(text="")

        col_r = col_right.column(align=True)
        col_r.prop(self, "scale", index=0, text="")
        col_r.prop(self, "scale", index=1, text="")
        col_r.prop(self, "scale", index=2, text="")

    def execute(self, context):
        bpy.ops.object.randomize_transform(
            random_seed=self.random_seed,
            use_delta=self.use_delta,
            use_loc=self.use_loc,
            loc=self.loc,
            use_rot=self.use_rot,
            rot=self.rot,
            use_scale=self.use_scale,
            scale_even=self.scale_even,
            scale=self.scale
        )
        return {'FINISHED'}

# “变换”菜单——对齐物体
class BUTTON_ACTION_OT_object_transform_object_align(bpy.types.Operator):
    bl_idname = "button.action_object_transform_object_align"
    bl_label = "对齐物体"
    bl_options = {'REGISTER', 'UNDO'}

    bb_quality: bpy.props.BoolProperty(
        name="",
        description="",
        default=True
    )

    align_mode: bpy.props.EnumProperty(
        name="",
        description="",
        items=[
            ('OPT_1', "反面", ""),
            ('OPT_2', "中心", ""),
            ('OPT_3', "正面", "")
        ],
        default='OPT_2'
    )

    relative_to: bpy.props.EnumProperty(
        name="",
        description="",
        items=[
            ('OPT_1', "场景原点", ""),
            ('OPT_2', "3D 游标", ""),
            ('OPT_3', "选中项", ""),
            ('OPT_4', "活动项", "")
        ],
        default='OPT_4'
    )

    align_axis: bpy.props.EnumProperty(
        name="",
        description="",
        options={'ENUM_FLAG'},
        items=[
            ('X', "X", ""),
            ('Y', "Y", ""),
            ('Z', "Z", "")
        ],
        default=set() 
    )

    def invoke(self, context, event):
        return self.execute(context)
    
    def draw(self, context):
        layout = self.layout
        split = layout.row().split(factor=0.4)

        col_left = split.column()
        col_left.alignment = "RIGHT"
        col_right = split.column()

        col_left.label(text="")
        col_right.prop(self, "bb_quality", text="高品质")

        col_left.label(text="对齐模式")
        col_right.prop(self, "align_mode", text="")

        col_left.label(text="相对于")
        col_right.prop(self, "relative_to", text="")

        col_left.label(text="对齐")
        col_right.prop(self, "align_axis", text="XYZ")

    def execute(self, context):
        bpy.ops.object.align(
            bb_quality=self.bb_quality,
            align_mode=self.align_mode,
            relative_to=self.relative_to,
            align_axis=self.align_axis
        )
        return {'FINISHED'}


class POPUP_MT_object_origin_set_menu(bpy.types.Operator):
    bl_idname = "popup.object_origin_set_menu"
    bl_label = "设置原点"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        return {'FINISHED'}

    def invoke(self, context, event):
        return context.window_manager.invoke_popup(self, width=120)

    def draw(self, context):
        layout = self.layout
        row = layout.row()
        col = row.column(align=True)
        col.label(text="设置原点", icon='PRESET')
        col.operator("object.origin_set", text="几何中心 -> 原点", icon="RADIOBUT_OFF").type='GEOMETRY_ORIGIN'
        col.operator("object.origin_set", text="原点 -> 几何中心", icon="RADIOBUT_OFF").type='ORIGIN_GEOMETRY'
        col.operator("object.origin_set", text="原点 -> 3D 游标", icon="RADIOBUT_OFF").type='ORIGIN_CURSOR'
        col.operator("object.origin_set", text="原点 -> 质心(表面)", icon="RADIOBUT_OFF").type='ORIGIN_CENTER_OF_MASS'
        col.operator("object.origin_set", text="原点 -> 质心(体积)", icon="RADIOBUT_OFF").type='ORIGIN_CENTER_OF_VOLUME'
        col.separator()
        col.operator("ed.undo", text="撤销", icon="LOOP_BACK")
        col.operator("ed.redo", text="重做", icon="LOOP_FORWARDS")

class BUTTON_ACTION_OT_call_object_origin_set_menu(bpy.types.Operator):
    bl_idname = "button.action_call_object_origin_set_menu"
    bl_label = "设置原点"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.ops.popup.object_origin_set_menu('INVOKE_DEFAULT')
        return {'FINISHED'}

class BUTTON_ACTION_OT_object_origin_set_geometry_origin(bpy.types.Operator):
    bl_idname = "button.action_object_origin_set_geometry_origin"
    bl_label = "几何中心 -> 原点"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.ops.object.origin_set(type='GEOMETRY_ORIGIN')
        return {'FINISHED'}
    
class BUTTON_ACTION_OT_object_origin_set_origin_geometry(bpy.types.Operator):
    bl_idname = "button.action_object_origin_set_origin_geometry"
    bl_label = "原点 -> 几何中心"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY')
        return {'FINISHED'}
    
class BUTTON_ACTION_OT_object_origin_set_origin_cursor(bpy.types.Operator):
    bl_idname = "button.action_object_origin_set_origin_cursor"
    bl_label = "原点 -> 3D 游标"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.ops.object.origin_set(type='ORIGIN_CURSOR')
        return {'FINISHED'}
    
class BUTTON_ACTION_OT_object_origin_set_origin_center_of_mass(bpy.types.Operator):
    bl_idname = "button.action_object_origin_set_origin_center_of_mass"
    bl_label = "原点 -> 质心(表面)"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.ops.object.origin_set(type='ORIGIN_CENTER_OF_MASS')
        return {'FINISHED'}
    
class BUTTON_ACTION_OT_object_origin_set_origin_center_of_volume(bpy.types.Operator):
    bl_idname = "button.action_object_origin_set_origin_center_of_volume"
    bl_label = "原点 -> 质心(体积)"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.ops.object.origin_set(type='ORIGIN_CENTER_OF_VOLUME')
        return {'FINISHED'}












class BUTTON_ACTION_OT_global_duplicate_move_linked(bpy.types.Operator):
    bl_idname = "button.action_global_duplicate_move_linked"
    bl_label = "关联复制"
    bl_description = "快捷键 Alt D"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.ops.object.duplicate_move_linked('INVOKE_DEFAULT')
        return {'FINISHED'}







classes = (
    BUTTON_ACTION_OT_object_select_select_by_type_menu,
    BUTTON_ACTION_OT_object_transform_randomize_transform,
    BUTTON_ACTION_OT_object_transform_object_align,
    POPUP_MT_object_origin_set_menu,
    BUTTON_ACTION_OT_call_object_origin_set_menu,
    BUTTON_ACTION_OT_object_origin_set_geometry_origin,
    BUTTON_ACTION_OT_object_origin_set_origin_geometry,
    BUTTON_ACTION_OT_object_origin_set_origin_cursor,
    BUTTON_ACTION_OT_object_origin_set_origin_center_of_mass,
    BUTTON_ACTION_OT_object_origin_set_origin_center_of_volume,

    BUTTON_ACTION_OT_global_duplicate_move_linked,

)

def register():
    for cls in classes:
        bpy.utils.register_class(cls)

def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)