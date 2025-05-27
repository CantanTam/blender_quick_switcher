import bpy



# 套索选择——开始(备份用)
class BUTTON_ACTION_OT_global_select_lasso_set(bpy.types.Operator):
    bl_idname = "button.action_global_select_lasso_set"
    bl_label = "开始"
    bl_options = {'REGISTER', 'UNDO'}

    waiting_for_click: bpy.props.BoolProperty(default=False, options={'HIDDEN'})

    def invoke(self, context, event):
        if not self.waiting_for_click:
            self.waiting_for_click = True
            context.window_manager.modal_handler_add(self)
            return {'RUNNING_MODAL'}
        return self.execute(context)

    def modal(self, context, event):
        if event.type == 'LEFTMOUSE' and event.value == 'PRESS':
            return self.execute(context)
        return {'PASS_THROUGH'}

    def execute(self, context):
        typeandmode = bpy.context.active_object.type+bpy.context.active_object.mode

        if typeandmode == 'GPENCILEDIT_GPENCIL':
            bpy.ops.gpencil.select_lasso('INVOKE_DEFAULT', mode='SET')
        else:
            bpy.ops.view3d.select_lasso('INVOKE_DEFAULT', mode='SET')
        self.waiting_for_click = False
        return {'FINISHED'}



# 调出“按组选择”菜单
class BUTTON_ACTION_OT_select_select_grouped(bpy.types.Operator):
    bl_idname = "button.action_select_select_grouped"
    bl_label = "按组选择"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):        
        if bpy.context.mode == "OBJECT":
            bpy.ops.object.select_grouped('INVOKE_DEFAULT')
        elif bpy.context.mode == "EDIT_GPENCIL":
            bpy.ops.gpencil.select_grouped('INVOKE_DEFAULT')
        elif bpy.context.mode == "POSE":
            bpy.ops.pose.select_grouped('INVOKE_DEFAULT')
        return {'FINISHED'}

# ”加选/减选“菜单
class VIEW3D_MT_mesh_select_linked_menu(bpy.types.Operator):
    bl_label = "选择相连元素"
    bl_idname = "popup.mesh_select_linked_menu"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        return {'FINISHED'}

    def invoke(self, context, event):
        return context.window_manager.invoke_popup(self, width=100)

    def draw(self, context):
        layout = self.layout
        row = layout.row()
        col = row.column(align=True)
        col.label(text="选择相连元素", icon='LINK_BLEND')
        col.operator("mesh.select_linked", text="关联项", icon="RADIOBUT_OFF")
        col.operator("mesh.shortest_path_select", text="最短路径", icon="RADIOBUT_OFF")
        col.operator("mesh.faces_select_linked_flat", text="相连的平展面", icon="RADIOBUT_OFF")

# 调出“选择相连”菜单
class BUTTON_ACTION_OT_select_select_linked(bpy.types.Operator):
    bl_idname = "button.action_select_select_linked"
    bl_label = "选择相连"
    bl_description = "选择相连元素/关联项"
    bl_options = {'REGISTER', 'UNDO'}

    all_forks: bpy.props.BoolProperty(
        name="全部分支",
        description="跟随父级链中的分支",
        default=False,
        update=lambda self, context: self.execute(context)
    )

    def invoke(self, context, event):
        return self.execute(context)

    def draw(self, context):
        if bpy.context.active_object.type + bpy.context.active_object.mode == "ARMATUREEDIT":
            layout = self.layout
            split = layout.row().split(factor=0.4)
            
            col_left = split.column()
            col_left.alignment = 'RIGHT'
            col_left.label(text="")
            
            col_right = split.column()
            col_right.prop(self, "all_forks")

    def execute(self, context):        
        typeandmode = bpy.context.active_object.type + bpy.context.active_object.mode
        
        if bpy.context.mode == "OBJECT":
            bpy.ops.object.select_linked('INVOKE_DEFAULT')
        elif typeandmode == "GREASEPENCILEDIT":
            bpy.ops.grease_pencil.select_linked('INVOKE_DEFAULT')
        elif typeandmode == "GPENCILEDIT_GPENCIL":
            bpy.ops.gpencil.select_linked('INVOKE_DEFAULT')
        elif typeandmode in {"CURVEEDIT", "SURFACEEDIT"}:
            bpy.ops.curve.select_linked('INVOKE_DEFAULT')
        elif typeandmode == "MESHEDIT":
            bpy.ops.popup.mesh_select_linked_menu('INVOKE_DEFAULT')
        elif typeandmode == "ARMATUREEDIT":
            bpy.ops.armature.select_linked(all_forks=self.all_forks)
        elif typeandmode == "ARMATUREPOSE":
            bpy.ops.pose.select_linked('INVOKE_DEFAULT')
        return {'FINISHED'}

class BUTTON_ACTION_OT_object_select_pattern(bpy.types.Operator):
    bl_idname = "button.action_object_select_pattern"
    bl_label = "按名称选择"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.ops.object.select_pattern('INVOKE_DEFAULT')
        return {'FINISHED'}

#网格编辑模式的选择选项

class BUTTON_ACTION_OT_mesh_select_nth(bpy.types.Operator):
    bl_idname = "button.action_mesh_select_nth"
    bl_label = "间隔式弃选"
    bl_options = {'REGISTER', 'UNDO'}

    skip: bpy.props.IntProperty(
        name="",
        description="重复次序中跳过的元素数量",
        default=1,
        min=1,
        soft_max=100, 
        update=lambda self, context: self.execute(context)  
    )

    nth: bpy.props.IntProperty(
        name="",
        description="重复次序中选择的元素数量",
        default=1,
        min=1,
        soft_max=100, 
        update=lambda self, context: self.execute(context)  
    )

    offset: bpy.props.IntProperty(
        name="",
        description="从起始点偏移",
        default=0,
        soft_min=-100,
        soft_max=100, 
        update=lambda self, context: self.execute(context)  
    )

    def invoke(self, context, event):
        return self.execute(context)

    def draw(self, context):
        layout = self.layout
        split = layout.row().split(factor=0.4)
        
        col_left = split.column()
        col_left.alignment = 'RIGHT'
        col_left.label(text="弃选项")
        col_left.label(text="选中项")
        col_left.label(text="偏移量")
        
        col_right = split.column()
        col_right.prop(self, "skip")
        col_right.prop(self, "nth")
        col_right.prop(self, "offset")

    def execute(self, context):
        bpy.ops.mesh.select_nth(skip=self.skip, nth=self.nth, offset=self.offset)
        return {'FINISHED'}

class BUTTON_ACTION_OT_mesh_edges_select_sharp(bpy.types.Operator):
    bl_idname = "button.action_mesh_edges_select_sharp"
    bl_label = "选择锐边"
    bl_options = {'REGISTER', 'UNDO'}

    sharpness: bpy.props.FloatProperty(
        name="",
        default=0.523599,
        min=0.000174533,
        max=3.14159,
        soft_min=0.0174533,
        soft_max=3.14159,
        subtype='ANGLE',
        update=lambda self, context: self.execute(context)
    )

    def invoke(self, context, event):
        return self.execute(context)

    def draw(self, context):
        layout = self.layout
        split = layout.row().split(factor=0.4)
        
        col_left = split.column()
        col_left.alignment = 'RIGHT'
        col_left.label(text="锐度")
        
        col_right = split.column()
        col_right.prop(self, "sharpness")

    def execute(self, context):
        bpy.ops.mesh.edges_select_sharp(sharpness=self.sharpness)
        return {'FINISHED'}

class BUTTON_ACTION_OT_select_select_similar(bpy.types.Operator):
    bl_idname = "button.action_select_select_similar"
    bl_label = "选择相似"
    bl_description = "快捷键 Shift G"
    bl_options = {'REGISTER', 'UNDO'}

    type: bpy.props.EnumProperty(
        name="",
        description="Property type to compare for similarity",
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
        update=lambda self, context: self.execute(context)
    )

    threshold: bpy.props.FloatProperty(
        name="",
        description="Similarity threshold (0–1)",
        default=0.1,
        min=0.0,
        max=1.0,
        precision=3,
        subtype='FACTOR',
        update=lambda self, context: self.execute(context)
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
        typeandmode = bpy.context.active_object.type+bpy.context.active_object.mode    
        if typeandmode in {"CURVEEDIT","SURFACEEDIT"}:
            bpy.ops.curve.select_similar('INVOKE_DEFAULT')
        elif typeandmode == "MESHEDIT":
            bpy.ops.wm.call_menu(name="VIEW3D_MT_edit_mesh_select_similar")
        elif bpy.context.mode == "ARMATUREEDIT":
            bpy.ops.armature.select_similar(type=self.type, threshold=self.threshold)
        elif typeandmode == "METAEDIT":
            bpy.ops.mball.select_similar('INVOKE_DEFAULT')
        return {'FINISHED'}

class BUTTON_ACTION_OT_mesh_select_by_trait(bpy.types.Operator):
    bl_idname = "popup.mesh_select_by_trait"
    bl_label = "按特征全选"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        return {'FINISHED'}

    def invoke(self, context, event):
        return context.window_manager.invoke_popup(self, width=100)

    def draw(self, context):
        layout = self.layout
        row = layout.row()
        col = row.column(align=True)
        col.label(text="按特征全选", icon='PRESET')
        col.operator("mesh.select_non_manifold", text="非流形", icon="RADIOBUT_OFF")
        col.operator("mesh.select_loose", text="松散几何元素", icon="RADIOBUT_OFF")
        col.operator("mesh.select_interior_faces", text="内侧面", icon="RADIOBUT_OFF")
        col.operator("mesh.select_face_by_sides", text="按侧选面", icon="RADIOBUT_OFF")

class BUTTON_ACTION_OT_mesh_call_select_by_trait(bpy.types.Operator):
    bl_idname = "button.action_mesh_call_select_by_trait"
    bl_label = "按特征全选"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.ops.popup.mesh_select_by_trait('INVOKE_DEFAULT')
        return {'FINISHED'}

class BUTTON_ACTION_OT_mesh_select_loops(bpy.types.Operator):
    bl_idname = "popup.mesh_select_loops"
    bl_label = "选择循环"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        return {'FINISHED'}

    def invoke(self, context, event):
        return context.window_manager.invoke_popup(self, width=100)

    def draw(self, context):
        layout = self.layout
        row = layout.row()
        col = row.column(align=True)
        col.label(text="选择循环", icon='PRESET')
        col.operator("mesh.loop_multi_select", text="循环边", icon="RADIOBUT_OFF").ring=False
        col.operator("mesh.loop_multi_select", text="并排边", icon="RADIOBUT_OFF").ring=True
        col.separator()
        col.operator("mesh.loop_to_region", text="选择循环线内侧区域", icon="RADIOBUT_OFF")
        col.operator("mesh.region_to_loop", text="选择区域轮廓线", icon="RADIOBUT_OFF")
        col.separator()
        col.operator("ed.undo", text="撤销", icon="LOOP_BACK")
        col.operator("ed.redo", text="重做", icon="LOOP_FORWARDS")

class BUTTON_ACTION_OT_call_mesh_select_loops(bpy.types.Operator):
    bl_idname = "button.action_call_mesh_select_loops"
    bl_label = "选择循环"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.ops.popup.mesh_select_loops('INVOKE_DEFAULT')
        return {'FINISHED'}

class BUTTON_ACTION_OT_mesh_select_axis(bpy.types.Operator):
    bl_idname = "button.action_mesh_select_axis"
    bl_label = "活动项的同侧"
    bl_options = {'REGISTER', 'UNDO'}

    orientation: bpy.props.EnumProperty(
        name="",
        description="轴朝向",
        items=[
            ('GLOBAL', "全局",    "", 'ORIENTATION_GLOBAL',   0),
            ('LOCAL',  "局部",     "", 'ORIENTATION_LOCAL', 1),
            ('NORMAL', "法向",    "", 'ORIENTATION_NORMAL',   2),
            ('GIMBAL', "万向",    "", 'ORIENTATION_GIMBAL',    3),
            ('VIEW',   "视图",      "", 'ORIENTATION_VIEW',      4),
            ('CURSOR', "游标",    "", 'ORIENTATION_CURSOR',        5),
            ('PARENT', "父级",    "", 'ORIENTATION_PARENT',     6),
        ],
        default='LOCAL',
        update=lambda self, context: self.execute(context)
    )

    sign: bpy.props.EnumProperty(
        name="",
        description="选择的一侧",
        items=[
            ('POS',   "正轴向",   ""),
            ('NEG',   "负轴向",   ""),
            ('ALIGN', "对齐轴",   ""),
        ],
        default='POS',
        update=lambda self, context: self.execute(context)
    )

    axis: bpy.props.EnumProperty(
        name="",
        description="选择各点用来比较的轴向",
        items=[
            ('X', "X", ""),
            ('Y', "Y", ""),
            ('Z', "Z", ""),
        ],
        default='X',
        update=lambda self, context: self.execute(context)
    )

    threshold: bpy.props.FloatProperty(
        name="",
        description="Threshold for selecting (in Blender units)",
        default=0,
        min=0,
        max=50.0,
        soft_max=10.0,
        precision=3,
        update=lambda self, context: self.execute(context)
    )

    def invoke(self, context, event):
        return self.execute(context)

    def draw(self, context):
        layout = self.layout
        split = layout.row().split(factor=0.4)
        
        col_left = split.column()
        col_left.alignment = 'RIGHT'
        col_left.label(text="轴向模式")
        col_left.label(text="轴向记号")
        col_left.label(text="轴向")
        col_left.label(text="阈值")

        col_right = split.column()
        col_right.prop(self, "orientation")
        col_right.prop(self, "sign")
        col_right.prop(self, "axis")
        col_right.prop(self, "threshold")

    def execute(self, context):
        bpy.ops.mesh.select_axis(orientation=self.orientation, sign=self.sign, axis=self.axis, threshold=self.threshold)
        return {'FINISHED'}





classes = (
    BUTTON_ACTION_OT_global_select_lasso_set,   #备份用，可以删除
    BUTTON_ACTION_OT_select_select_grouped,
    VIEW3D_MT_mesh_select_linked_menu,
    BUTTON_ACTION_OT_select_select_linked,
    BUTTON_ACTION_OT_object_select_pattern,
    BUTTON_ACTION_OT_mesh_select_nth,
    BUTTON_ACTION_OT_mesh_edges_select_sharp,
    BUTTON_ACTION_OT_select_select_similar,
    BUTTON_ACTION_OT_mesh_select_by_trait,
    BUTTON_ACTION_OT_mesh_call_select_by_trait,
    BUTTON_ACTION_OT_mesh_select_loops,
    BUTTON_ACTION_OT_call_mesh_select_loops,
    BUTTON_ACTION_OT_mesh_select_axis,
)

def register():
    for cls in classes:
        bpy.utils.register_class(cls)

def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)