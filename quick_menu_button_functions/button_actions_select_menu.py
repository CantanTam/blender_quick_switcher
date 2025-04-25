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
        update=lambda self, context: self.execute(context) if bpy.context.mode == 'EDIT_MESH' else None
    )
    
    extend: bpy.props.BoolProperty(
        name="扩展",
        default=False,
        description="扩展而不是替换当前选择",
        update=lambda self, context: self.execute(context) if bpy.context.mode == 'EDIT_MESH' else None
    )

    def invoke(self, context, event):
        if bpy.context.mode == 'EDIT_MESH':
            # 在编辑模式下，返回FINISHED直接让update回调调用execute
            return {'FINISHED'}
        return self.execute(context)

    def draw(self, context):
        layout = self.layout
        #row = layout.row()
        split = layout.row().split(factor=0.4)
        
        # 左侧列 - 标签
        #col_left = row.column()
        col_left = split.column()
        col_left.alignment = 'RIGHT'
        col_left.label(text="轴向")
        
        # 右侧列 - 垂直排列的单选按钮
        #col_right = row.column()
        col_right = split.column()
        col_right.prop(self, "axis", expand=True)
        #layout.separator()
        col_right.prop(self, "extend")

    def execute(self, context):
        typeandmode = bpy.context.active_object.type + bpy.context.active_object.mode

        if bpy.context.mode == 'OBJECT':
            # 对象模式下通过 tool_settings 设置参数
            context.scene.tool_settings.mirror_axis = self.axis
            bpy.ops.object.select_mirror()
        elif typeandmode in {"CURVEEDIT", "SURFACEEDIT"}:
            bpy.ops.curve.select_all(action='INVERT')
        elif typeandmode == "METAEDIT":
            bpy.ops.mball.select_all(action='INVERT')
        elif typeandmode == "FONTEDIT":
            bpy.ops.font.select_all()
        elif typeandmode == "LATTICEEDIT":
            bpy.ops.lattice.select_all(action='INVERT')
        elif typeandmode == "MESHEDIT":
            # 在编辑模式下直接将轴参数传给操作符
            bpy.ops.mesh.select_mirror(axis={self.axis}, extend=self.extend)
        elif typeandmode in {"GPENCILEDIT_GPENCIL", "GPENCILVERTEX_GPENCIL"}:
            bpy.ops.gpencil.select_all(action='INVERT')
        elif typeandmode in {"GREASEPENCILEDIT", "GREASEPENCILVERTEX_GREASE_PENCIL"}:
            bpy.ops.grease_pencil.select_all(action='INVERT')
        elif typeandmode == "ARMATUREEDIT":
            bpy.ops.armature.select_all(action='INVERT')
        elif typeandmode == "ARMATUREPOSE":
            bpy.ops.pose.select_all(action='INVERT')
        else:
            return {'CANCELLED'}
        return {'FINISHED'}
