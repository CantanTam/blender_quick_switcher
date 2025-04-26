import bpy
# 全选
class BUTTON_ACTION_OT_select_select_all(bpy.types.Operator):
    bl_idname = "button.action_select_select_all"
    bl_label = "全选"
    bl_description = "快捷键 A"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        typeandmode = bpy.context.active_object.type+bpy.context.active_object.mode

        if bpy.context.mode == 'OBJECT':
            bpy.ops.object.select_all(action='SELECT')
        elif typeandmode in {"CURVEEDIT", "SURFACEEDIT"}:
            bpy.ops.curve.select_all(action='SELECT')
        elif typeandmode == "METAEDIT":
            bpy.ops.mball.select_all(action='SELECT')
        elif typeandmode ==  "FONTEDIT":
            bpy.ops.font.select_all()
        elif typeandmode == "LATTICEEDIT":
            bpy.ops.lattice.select_all(action='SELECT')
        elif typeandmode == "MESHEDIT":
            bpy.ops.mesh.select_all(action='SELECT')
        elif typeandmode in {"GPENCILEDIT_GPENCIL","GPENCILVERTEX_GPENCIL"}:
            bpy.ops.gpencil.select_all(action='SELECT') # 4.2 版本
        elif typeandmode in { "GREASEPENCILEDIT","GREASEPENCILVERTEX_GREASE_PENCIL"}:
            bpy.ops.grease_pencil.select_all(action='SELECT') # 4.3 版本
        elif typeandmode == "ARMATUREEDIT":
            bpy.ops.armature.select_all(action='SELECT')
        elif typeandmode == "ARMATUREPOSE":
            bpy.ops.pose.select_all(action='SELECT')
        else:
            return {'CANCELLED'}
        return {'FINISHED'}

# 反选
class BUTTON_ACTION_OT_select_select_invert(bpy.types.Operator):
    bl_idname = "button.action_select_select_invert"
    bl_label = "反选"
    bl_description = "快捷键 Ctrl I"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        typeandmode = bpy.context.active_object.type+bpy.context.active_object.mode

        if bpy.context.mode == 'OBJECT':
            bpy.ops.object.select_all(action='INVERT')
        elif typeandmode in {"CURVEEDIT", "SURFACEEDIT"}:
            bpy.ops.curve.select_all(action='INVERT')
        elif typeandmode == "METAEDIT":
            bpy.ops.mball.select_all(action='INVERT')
        elif typeandmode ==  "FONTEDIT":
            bpy.ops.font.select_all()
        elif typeandmode == "LATTICEEDIT":
            bpy.ops.lattice.select_all(action='INVERT')
        elif typeandmode == "MESHEDIT":
            bpy.ops.mesh.select_all(action='INVERT')
        elif typeandmode in {"GPENCILEDIT_GPENCIL","GPENCILVERTEX_GPENCIL"}:
            bpy.ops.gpencil.select_all(action='INVERT') # 4.2 版本
        elif typeandmode in { "GREASEPENCILEDIT","GREASEPENCILVERTEX_GREASE_PENCIL"}:
            bpy.ops.grease_pencil.select_all(action='INVERT') # 4.3 版本
        elif typeandmode == "ARMATUREEDIT":
            bpy.ops.armature.select_all(action='INVERT')
        elif typeandmode == "ARMATUREPOSE":
            bpy.ops.pose.select_all(action='INVERT')
        else:
            return {'CANCELLED'}
        return {'FINISHED'}
    
class VIEW3D_MT_select_select_by_type_menu(bpy.types.Menu):
    bl_label = ""
    bl_idname = "view3d.mt_select_select_by_type_menu"

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

# 弹出“按类型全选”菜单
class BUTTON_ACTION_OT_view3d_call_select_select_by_type_menu(bpy.types.Operator):
    bl_idname = "button.action_view3d_call_select_select_by_type_menu"
    bl_label = "按类型全选"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.ops.wm.call_menu(name="view3d.mt_select_select_by_type_menu")
        return {'FINISHED'}

# 刷选
class BUTTON_ACTION_OT_select_select_circle(bpy.types.Operator):
    bl_idname = "button.action_select_select_circle"
    bl_label = "刷选"
    bl_description = "快捷键 C"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        typeandmode = bpy.context.active_object.type+bpy.context.active_object.mode

        if bpy.context.mode == 'OBJECT':
            bpy.ops.view3d.select_circle('INVOKE_DEFAULT')
        elif typeandmode in {
            "CURVEEDIT", 
            "SURFACEEDIT",
            "METAEDIT",
            "LATTICEEDIT",
            "MESHEDIT",
            "GREASEPENCILEDIT",
            "ARMATUREEDIT",
            "ARMATUREPOSE",
            }:
            bpy.ops.view3d.select_circle('INVOKE_DEFAULT')
        elif typeandmode == "GPENCILEDIT_GPENCIL":
            bpy.ops.gpencil.select_circle('INVOKE_DEFAULT') # 4.2 版本
        else:
            return {'CANCELLED'}
        return {'FINISHED'}
    
# 选择“镜像”
class BUTTON_ACTION_OT_select_select_mirror(bpy.types.Operator):
    bl_idname = "button.action_select_select_mirror"
    bl_label = "选择镜像"
    bl_description = "快捷键 Ctrl Shift M"
    bl_options = {'REGISTER', 'UNDO'}

    axis: bpy.props.EnumProperty(
        name="镜像轴",
        items=[
            ('X', "X轴", ""),
            ('Y', "Y轴", ""),
            ('Z', "Z轴", ""),
        ],
        default='X',
        update=lambda self, context: self.execute(context) #if bpy.context.mode == 'EDIT_MESH' else None
    )
    
    extend: bpy.props.BoolProperty(
        name="扩展",
        default=False,
        description="扩展选择，而不是先取消选择",
        update=lambda self, context: self.execute(context) #if bpy.context.mode == 'EDIT_MESH' else None
    )

    # 针对骨骼的选项
    only_active: bpy.props.BoolProperty(
        name="仅激活",
        default=False,
        description="仅操作活动的骨骼",
        update=lambda self, context: self.execute(context) #if bpy.context.mode == 'EDIT_MESH' else None
    )

    def invoke(self, context, event):
        if bpy.context.mode == 'EDIT_MESH':
            # 在编辑模式下，返回FINISHED直接让update回调调用execute
            return {'FINISHED'}
        return self.execute(context)

    def draw(self, context):
        typeandmode = bpy.context.active_object.type + bpy.context.active_object.mode

        layout = self.layout
        #row = layout.row()
        split = layout.row().split(factor=0.4)
        
        # 左侧列 - 标签
        col_left = split.column()
        col_left.alignment = 'RIGHT'
        if typeandmode == "MESHEDIT":
            col_left.label(text="轴向")
        
        # 右侧列 - 垂直排列的单选按钮
        col_right = split.column()
        if typeandmode in {"MESHEDIT","LATTICEEDIT"}:
            col_right.prop(self, "axis", expand=True)
        if typeandmode in {"ARMATUREEDIT","ARMATUREPOSE"}:
            col_right.prop(self, "only_active")
        col_right.prop(self, "extend")

    def execute(self, context):
        typeandmode = bpy.context.active_object.type + bpy.context.active_object.mode

        if bpy.context.mode == 'OBJECT':
            bpy.ops.object.select_mirror(extend=self.extend)
        elif typeandmode == "LATTICEEDIT":
            bpy.ops.lattice.select_mirror(axis={self.axis}, extend=self.extend)
        elif typeandmode == "MESHEDIT":
            # 在编辑模式下直接将轴参数传给操作符
            bpy.ops.mesh.select_mirror(axis={self.axis}, extend=self.extend)
        elif typeandmode == "ARMATUREEDIT":
            bpy.ops.armature.select_mirror(only_active=self.only_active, extend=self.extend)
        elif typeandmode == "ARMATUREPOSE":
            bpy.ops.pose.select_mirror(only_active=self.only_active, extend=self.extend)
        else:
            return {'CANCELLED'}
        return {'FINISHED'}
