import bpy

# 全局“全选”功能
class BUTTON_ACTION_OT_global_select_all(bpy.types.Operator):
    bl_idname = "button.action_global_select_all"
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
    
# 全局“反选”功能
class BUTTON_ACTION_OT_global_select_invert(bpy.types.Operator):
    bl_idname = "button.action_global_select_invert"
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
    
# 全局“刷选”功能
class BUTTON_ACTION_OT_global_select_circle(bpy.types.Operator):
    bl_idname = "button.action_global_select_circle"
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

# “按类型选择”菜单
class VIEW3D_MT_select_select_by_type_menu(bpy.types.Operator):
    bl_label = ""
    bl_idname = "button.action_call_select_select_by_type_menu"

    @classmethod
    def poll(cls, context):
        # 不在OBJECT模式时直接返回False，菜单将不会显示
        return context.active_object is not None and context.active_object.mode == 'OBJECT'

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
        return self.execute(context)

    def draw(self, context):
        typeandmode = bpy.context.active_object.type + bpy.context.active_object.mode

        layout = self.layout
        #row = layout.row()
        split = layout.row().split(factor=0.4)
        
        # 左侧列 - 标签
        col_left = split.column()
        col_left.alignment = 'RIGHT'
        if typeandmode in {"MESHEDIT","LATTICEEDIT"}:
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

# 随机选择
class BUTTON_ACTION_OT_select_select_random(bpy.types.Operator):
    bl_idname = "button.action_select_select_random"
    bl_label = "随机选择"
    bl_options = {'REGISTER', 'UNDO'}

    ratio: bpy.props.FloatProperty(
        name="",
        description="用于随机选择的部分",
        default=0.5, 
        min=0.0,  
        max=1.0, 
        subtype='FACTOR',      
        precision=3,          
        update=lambda self, context: self.execute(context)  
    )

    seed: bpy.props.IntProperty(
        name="",
        description="随机数生成器的种值",
        default=0,
        min=0,
        soft_max=255, 
        update=lambda self, context: self.execute(context)  
    )

    action: bpy.props.EnumProperty(
        name="动作",
        items=[
            ('SELECT', "选择", "全选"),
            ('DESELECT', "弃选", "弃选全部元素"),
        ],
        default='SELECT',
        update=lambda self, context: self.execute(context) 
    )

    unselect_ends: bpy.props.BoolProperty(
        name="不选中末端",
        description="不选择笔画的起点和末点",
        default=False,
        update=lambda self, context: self.execute(context)
    )
    
    def invoke(self, context, event):
        return self.execute(context)

    def draw(self, context):
        typeandmode = bpy.context.active_object.type + bpy.context.active_object.mode

        layout = self.layout
        split = layout.row().split(factor=0.4)
        
        col_left = split.column()
        col_left.alignment = 'RIGHT'
        col_left.label(text="比率")
        col_left.label(text="随机种")
        col_left.label(text="动作")
        
        col_right = split.column()
        col_right.prop(self, "ratio")
        col_right.prop(self, "seed")
        col_right.prop(self, "action", expand=True)
        if typeandmode == "GPENCILEDIT_GPENCIL":
            col_right.prop(self, "unselect_ends")

    def execute(self, context):
        typeandmode = bpy.context.active_object.type + bpy.context.active_object.mode

        if bpy.context.mode == 'OBJECT':
            bpy.ops.object.select_random(ratio=self.ratio, seed=self.seed, action=self.action)
        elif typeandmode == "MESHEDIT":
            bpy.ops.mesh.select_random(ratio=self.ratio, seed=self.seed, action=self.action)
        elif typeandmode in {"CURVEEDIT","SURFACEEDIT"}:
            bpy.ops.curve.select_random(ratio=self.ratio, seed=self.seed, action=self.action)
        elif typeandmode == "METAEDIT":
            bpy.ops.mball.select_random_metaelems(ratio=self.ratio, seed=self.seed, action=self.action)
        elif typeandmode == "GPENCILEDIT_GPENCIL":
            bpy.ops.gpencil.select_random(ratio=self.ratio, seed=self.seed, action=self.action, unselect_ends=self.unselect_ends)
        elif typeandmode == "GREASEPENCILEDIT":
            bpy.ops.grease_pencil.select_random(ratio=self.ratio, seed=self.seed, action=self.action)
        elif typeandmode == "LATTICEEDIT":
            bpy.ops.lattice.select_random(ratio=self.ratio, seed=self.seed, action=self.action)
        else:
            return {'CANCELLED'}
        return {'FINISHED'}

# ”加选/减选“菜单
class VIEW3D_MT_object_select_more_or_less_menu(bpy.types.Operator):
    bl_label = ""
    bl_idname = "popup.more_or_less_menu"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        return {'FINISHED'}

    def invoke(self, context, event):
        return context.window_manager.invoke_popup(self, width=100)

    def draw(self, context):
        typeandmode = bpy.context.active_object.type+bpy.context.active_object.mode

        layout = self.layout
        row = layout.row()
        col = row.column(align=True)
        col.label(text="加选/减选", icon='FORCE_CHARGE')

        if bpy.context.mode == "OBJECT":
        # 调用 view_axis 操作符，并传入对应的 type 参数
            col.operator("object.select_more", text="扩展选区", icon="ADD")
            col.operator("object.select_less", text="缩减选区", icon="REMOVE")
        elif typeandmode == "CURVEEDIT":
            col.operator("curve.select_more", text="扩展选择", icon="ADD")
            col.operator("curve.select_less", text="缩减选择", icon="REMOVE")
            col.separator()
            col.operator("curve.select_next", text="选择下一项", icon="FRAME_NEXT")
            col.operator("curve.select_previous", text="选择上一项", icon="FRAME_PREV")
        elif typeandmode == "SURFACEEDIT":
            col.operator("curve.select_more", text="扩展选择", icon="ADD")
            col.operator("curve.select_less", text="缩减选择", icon="REMOVE")
        elif typeandmode == "MESHEDIT":
            col.operator("mesh.select_more", text="扩展选区", icon="ADD")
            col.operator("mesh.select_less", text="缩减选区", icon="REMOVE")
            col.separator()
            col.operator("mesh.select_next_item", text="下一个活动元素", icon="FRAME_NEXT")
            col.operator("mesh.select_prev_item", text="上一个活动元素", icon="FRAME_PREV")
        elif typeandmode == "ARMATUREEDIT":
            col.operator("armature.select_more", text="扩展选区", icon="ADD")
            col.operator("armature.select_less", text="缩减选区", icon="REMOVE")
        elif typeandmode == "LATTICEEDIT":
            col.operator("lattice.select_more", text="扩展选区", icon="ADD")
            col.operator("lattice.select_less", text="缩减选区", icon="REMOVE")
        elif typeandmode == "GPENCILEDIT_GPENCIL":
            col.operator("gpencil.select_more", text="扩展选区", icon="ADD")
            col.operator("gpencil.select_less", text="缩减选区", icon="REMOVE")
        elif typeandmode == "GREASEPENCILEDIT":
            col.operator("grease_pencil.select_more", text="扩展选区", icon="ADD")
            col.operator("grease_pencil.select_less", text="缩减选区", icon="REMOVE")

class BUTTON_ACTION_OT_call_object_select_more_or_less_menu(bpy.types.Operator):
    bl_idname = "button.action_call_object_select_more_or_less_menu"
    bl_label = "加选/减选"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.ops.popup.more_or_less_menu('INVOKE_DEFAULT')
        return {'FINISHED'}
    
# 父级/子级/扩展父级/扩展子级 功能四合一   
class BUTTON_ACTION_OT_object_select_hierarchy_parent_child(bpy.types.Operator):
    bl_idname = "button.action_object_select_hierarchy_parent_child"
    bl_label = "父级/子级/扩展父级/扩展子级"
    bl_description = "父级/子级/扩展父级/扩展子级功能集合"
    bl_options = {'REGISTER', 'UNDO'}

    direction: bpy.props.EnumProperty(
        name="选择动作",  # 显示在UI中的标签名称
        items=[
            ('PARENT', "父级", ""),
            ('CHILD', "子级", ""), 
        ],
        default='PARENT',
        update=lambda self, context: self.execute(context)
    )

    extend: bpy.props.BoolProperty(
        name="扩展",            
        description="", 
        default=False,
        update=lambda self, context: self.execute(context)
    ) 

    def invoke(self, context, event):
        return self.execute(context)

    def draw(self, context):
        layout = self.layout
        #row = layout.row()
        split = layout.row().split(factor=0.4)
        
        # 左侧列 - 标签
        col_left = split.column()
        col_left.alignment = 'RIGHT'
        col_left.label(text="方向")
        
        # 右侧列 - 垂直排列的单选按钮
        col_right = split.column()
        col_right.prop(self, "direction", expand=True)
        col_right.prop(self, "extend")

    def execute(self, context):
        typeandmode = bpy.context.active_object.type+bpy.context.active_object.mode

        if bpy.context.mode == 'OBJECT':
            bpy.ops.object.select_hierarchy(direction=self.direction, extend=self.extend)
        elif typeandmode == "ARMATUREEDIT":
            bpy.ops.armature.select_hierarchy(direction=self.direction, extend=self.extend)
        elif typeandmode == "ARMATUREPOSE":
            bpy.ops.pose.select_hierarchy(direction=self.direction, extend=self.extend)
        else:
            return {'CANCELLED'}
        return {'FINISHED'}

# 调出“按组选择”菜单
class BUTTON_ACTION_OT_select_select_grouped(bpy.types.Operator):
    bl_idname = "button.action_select_select_grouped"
    bl_label = "按组选择"
    bl_description = "快捷键 Shift G"
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



classes = (
    BUTTON_ACTION_OT_global_select_all,
    BUTTON_ACTION_OT_global_select_invert,
    BUTTON_ACTION_OT_global_select_circle,
    BUTTON_ACTION_OT_global_select_lasso_set,   #备份用，可以删除
    BUTTON_ACTION_OT_select_select_random,
    BUTTON_ACTION_OT_select_select_mirror,
    VIEW3D_MT_select_select_by_type_menu,
    VIEW3D_MT_object_select_more_or_less_menu,
    BUTTON_ACTION_OT_call_object_select_more_or_less_menu,
    BUTTON_ACTION_OT_object_select_hierarchy_parent_child,
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
)

def register():
    for cls in classes:
        bpy.utils.register_class(cls)

def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)