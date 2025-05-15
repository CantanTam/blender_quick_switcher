import bpy
from ..show_switch_notice import show_notice

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
            show_notice("ACTIVE_LOCK.png")
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
        show_notice("ACTIVE_LOCK.png")
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
        layout = self.layout

        typeandmode = bpy.context.active_object.type+bpy.context.active_object.mode

        layout = self.layout
        row = layout.row()
        col = row.column(align=True)
        col.label(text="加选/减选", icon='FORCE_CHARGE')

        if bpy.context.mode == "OBJECT":
        # 调用 view_axis 操作符，并传入对应的 type 参数
            col.operator("object.select_more", text="扩展选区", icon="ADD")
            col.operator("object.select_less", text="缩减选区", icon="REMOVE")
        elif typeandmode in {"CURVEEDIT","SURFACEEDIT"}:
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

class BUTTON_ACTION_OT_call_object_select_more_or_less_menu(bpy.types.Operator):
    bl_idname = "button.action_call_object_select_more_or_less_menu"
    bl_label = "加选/减选"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.ops.popup.more_or_less_menu('INVOKE_DEFAULT')
        return {'FINISHED'}
    
# 加选    
class BUTTON_ACTION_OT_object_select_more(bpy.types.Operator):
    bl_idname = "button.action_object_select_more"
    bl_label = "加选"
    bl_description = "快捷键 Ctrl Num_+"
    bl_options = {'REGISTER', 'UNDO'}

    use_face_step: bpy.props.BoolProperty(
        name="面步长",            
        description="相连的面(而非边)", 
        default=True,
        update=lambda self, context: self.execute(context)
    )    

    def invoke(self, context, event):
        return self.execute(context)
    
    def draw(self, context):
        typeandmode = bpy.context.active_object.type + bpy.context.active_object.mode

        if typeandmode == "MESHEDIT":

            layout = self.layout
            #row = layout.row()
            split = layout.row().split(factor=0.4)
            
            # 左侧列 - 标签
            col_left = split.column()
            col_left.label(text="")
            
            # 右侧列 - 垂直排列的单选按钮
            col_right = split.column()
            col_right.prop(self, "use_face_step")

    def execute(self, context):
        typeandmode = bpy.context.active_object.type+bpy.context.active_object.mode

        if bpy.context.mode == 'OBJECT':
            bpy.ops.object.select_more()
        elif typeandmode in {"CURVEEDIT","SURFACEEDIT",}:
            bpy.ops.curve.select_more()
        elif typeandmode == "MESHEDIT":
            bpy.ops.mesh.select_more(use_face_step=self.use_face_step)
        elif typeandmode == "GPENCILEDIT_GPENCIL": # 4.2 版本
            bpy.ops.gpencil.select_more()
        elif typeandmode == "GREASEPENCILEDIT": # 4.3 版本
            bpy.ops.grease_pencil.select_more()
        elif typeandmode == "ARMATUREEDIT":
            bpy.ops.armature.select_more()
        elif typeandmode == "LATTICEEDIT":
            bpy.ops.lattice.select_more()
        else:
            return {'CANCELLED'}
        return {'FINISHED'}
    
# 减选    
class BUTTON_ACTION_OT_object_select_less(bpy.types.Operator):
    bl_idname = "button.action_object_select_less"
    bl_label = "减选"
    bl_description = "快捷键 Ctrl Num_-"
    bl_options = {'REGISTER', 'UNDO'}

    use_face_step: bpy.props.BoolProperty(
        name="面步长",            
        description="相连的面(而非边)", 
        default=True,
        update=lambda self, context: self.execute(context)
    )    

    def invoke(self, context, event):
        return self.execute(context)
    
    def draw(self, context):
        typeandmode = bpy.context.active_object.type + bpy.context.active_object.mode

        if typeandmode == "MESHEDIT":

            layout = self.layout
            #row = layout.row()
            split = layout.row().split(factor=0.4)
            
            # 左侧列 - 标签
            col_left = split.column()
            col_left.label(text="")
            
            # 右侧列 - 垂直排列的单选按钮
            col_right = split.column()
            col_right.prop(self, "use_face_step")

    def execute(self, context):
        typeandmode = bpy.context.active_object.type+bpy.context.active_object.mode

        if bpy.context.mode == 'OBJECT':
            bpy.ops.object.select_less()
        elif typeandmode in {"CURVEEDIT","SURFACEEDIT",}:
            bpy.ops.curve.select_less()
        elif typeandmode == "MESHEDIT":
            bpy.ops.mesh.select_less(use_face_step=self.use_face_step)
        elif typeandmode == "GPENCILEDIT_GPENCIL": # 4.2 版本
            bpy.ops.gpencil.select_less()
        elif typeandmode == "GREASEPENCILEDIT": # 4.3 版本
            bpy.ops.grease_pencil.select_less()
        elif typeandmode == "ARMATUREEDIT":
            bpy.ops.armature.select_less()
        elif typeandmode == "LATTICEEDIT":
            bpy.ops.lattice.select_less()
        else:
            return {'CANCELLED'}
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
        #default='PARENT',
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

# 按组选择类（菜单）
class VIEW3D_MT_select_select_grouped_menu(bpy.types.Menu):
    bl_label = ""
    bl_idname = "view3d.mt_select_select_grouped_menu"

    def draw(self, context):
        layout = self.layout

        typeandmode = bpy.context.active_object.type+bpy.context.active_object.mode

        if bpy.context.mode == "OBJECT":
            layout.operator("object.select_grouped", text="子级").type='CHILDREN_RECURSIVE'
            layout.operator("object.select_grouped", text="直接子级").type='CHILDREN'
            layout.operator("object.select_grouped", text="父级").type='PARENT'
            layout.operator("object.select_grouped", text="平级").type='SIBLINGS'
            layout.operator("object.select_grouped", text="类型").type='TYPE'
            layout.operator("object.select_grouped", text="集合").type='COLLECTION'
            layout.operator("object.select_grouped", text="钩挂").type='HOOK'
            layout.operator("object.select_grouped", text="通道层").type='PASS'
            layout.operator("object.select_grouped", text="颜色").type='COLOR'
            layout.operator("object.select_grouped", text="插帧集").type='KEYINGSET'
            layout.operator("object.select_grouped", text="灯光类型").type='LIGHT_TYPE'
        elif typeandmode == "MESHEDIT" and bpy.app.version < (4, 2, 0) :
            layout.operator("mesh.select_similar", text="法向").type='NORMAL'
            layout.operator("mesh.select_similar", text="相邻面数量").type='FACE'
            layout.operator("mesh.select_similar", text="顶点组").type='VGROUP'
            layout.operator("mesh.select_similar", text="连接边数量").type='EDGE'
            layout.operator("mesh.select_similar", text="顶点折痕").type='VCREASE'
            layout.separator()
            layout.operator("mesh.select_similar_region", text="面区域")
        elif typeandmode == "MESHEDIT" and bpy.app.version >= (4, 2, 0) :
            layout.operator("mesh.select_similar", text="法向").type='VERT_NORMAL'
            layout.operator("mesh.select_similar", text="相邻面数量").type='VERT_FACES'
            layout.operator("mesh.select_similar", text="顶点组").type='VERT_GROUPS'
            layout.operator("mesh.select_similar", text="连接边数量").type='VERT_EDGES'
            layout.operator("mesh.select_similar", text="顶点折痕").type='VERT_CREASE'
            layout.separator()
            layout.operator("mesh.select_similar_region", text="面区域")         
        elif typeandmode in {"GPENCILEDIT_GPENCIL","GPENCILVERTEX_GPENCIL"}:
            layout.operator("gpencil.select_grouped", text="层").type='LAYER'
            layout.operator("gpencil.select_grouped", text="材质").type='MATERIAL'
        elif typeandmode in {"GREASEPENCILEDIT","GREASEPENCILVERTEX_GREASE_PENCIL"}:
            layout.operator("grease_pencil.select_similar", text="层").mode='LAYER'
            layout.operator("grease_pencil.select_similar", text="材质").mode='MATERIAL'
            layout.operator("grease_pencil.select_similar", text="顶点颜色").mode='VERTEX_COLOR'
            layout.operator("grease_pencil.select_similar", text="半径").mode='RADIUS'
            layout.operator("grease_pencil.select_similar", text="不透明度").mode='OPACITY'
        elif typeandmode == "ARMATUREEDIT" and bpy.app.version < (4, 2, 0) :
            layout.operator("armature.select_similar", text="子级").type='CHILDREN'
            layout.operator("armature.select_similar", text="直接子级").type='CHILDREN_IMMEDIATE'
            layout.operator("armature.select_similar", text="平级").type='SIBLINGS'
            layout.operator("armature.select_similar", text="长度").type='LENGTH'
            layout.operator("armature.select_similar", text="方向(Y轴)").type='DIRECTION'
            layout.operator("armature.select_similar", text="前缀").type='PREFIX'
            layout.operator("armature.select_similar", text="后缀").type='SUFFIX'
            layout.operator("armature.select_similar", text="层").type='LAYER'
            layout.operator("armature.select_similar", text="群组").type='GROUP'
            layout.operator("armature.select_similar", text="形状").type='SHAPE'
        elif typeandmode == "ARMATUREEDIT" and bpy.app.version >= (4, 2, 0) :
            layout.operator("armature.select_similar", text="子级").type='CHILDREN'
            layout.operator("armature.select_similar", text="直接子级").type='CHILDREN_IMMEDIATE'
            layout.operator("armature.select_similar", text="平级").type='SIBLINGS'
            layout.operator("armature.select_similar", text="长度").type='LENGTH'
            layout.operator("armature.select_similar", text="方向(Y轴)").type='DIRECTION'
            layout.operator("armature.select_similar", text="前缀").type='PREFIX'
            layout.operator("armature.select_similar", text="后缀").type='SUFFIX'
            layout.operator("armature.select_similar", text="骨骼集合").type='BONE_COLLECTION'
            layout.operator("armature.select_similar", text="颜色").type='COLOR'
            layout.operator("armature.select_similar", text="形状").type='SHAPE'
        elif typeandmode == "ARMATUREPOSE" and bpy.app.version < (4, 2, 0) :
            layout.operator("pose.select_grouped", text="层").type='LAYER'
            layout.operator("pose.select_grouped", text="群组").type='GROUP'
            layout.operator("pose.select_grouped", text="插帧集").type='KEYINGSET'
        elif typeandmode == "ARMATUREPOSE" and bpy.app.version >= (4, 2, 0) :
            layout.operator("pose.select_grouped", text="集合").type='COLLECTION'
            layout.operator("pose.select_grouped", text="颜色").type='COLOR'
            layout.operator("pose.select_grouped", text="插帧集").type='KEYINGSET'
        elif typeandmode == "METAEDIT":
            layout.operator("mball.select_similar", text="类型").type='TYPE'
            layout.operator("mball.select_similar", text="半径").type='RADIUS'
            layout.operator("mball.select_similar", text="硬度").type='STIFFNESS'
            layout.operator("mball.select_similar", text="旋转").type='ROTATION'

# 调出“按组选择”菜单
class BUTTON_ACTION_OT_call_select_select_grouped_menu(bpy.types.Operator):
    bl_idname = "button.action_call_select_select_grouped_menu"
    bl_label = "按组选择"
    bl_description = "快捷键 Shift G"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        typeandmode = context.active_object.type + context.active_object.mode
        
        if typeandmode in {"CURVEEDIT","SURFACEEDIT"}:
            #bpy.ops.button.action_curveedit_surfaceedit_select_similar()
            bpy.ops.curve.select_similar('INVOKE_DEFAULT')
        else:
            bpy.ops.wm.call_menu(name="view3d.mt_select_select_grouped_menu")
        return {'FINISHED'}

# 选择相连项（菜单）
class VIEW3D_MT_select_select_linked_menu(bpy.types.Menu):
    bl_label = ""
    bl_idname = "view3d.mt_select_select_linked_menu"

    def draw(self, context):
        layout = self.layout

        typeandmode = bpy.context.active_object.type+bpy.context.active_object.mode

        if bpy.context.mode == "OBJECT":
            layout.operator("object.select_linked", text="物体数据").type='OBDATA'
            layout.operator("object.select_linked", text="材质").type='MATERIAL'
            layout.operator("object.select_linked", text="实例集合").type='DUPGROUP'
            layout.operator("object.select_linked", text="粒子系统").type='PARTICLE'
            layout.operator("object.select_linked", text="库").type='LIBRARY'
            layout.operator("object.select_linked", text="库(物体数据)").type='LIBRARY_OBDATA'
        elif typeandmode == "MESHEDIT":
            layout.operator("mesh.select_linked", text="关联项")
            layout.operator("mesh.shortest_path_select", text="最短路径")
            layout.operator("mesh.faces_select_linked_flat", text="相连的平民面")

# 调出“选择相连项”菜单
class BUTTON_ACTION_OT_call_select_select_linked_menu(bpy.types.Operator):
    bl_idname = "button.action_call_select_select_linked_menu"
    bl_label = "选择相连元素"
    bl_description = "不同编辑模式有不同功能"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        typeandmode = bpy.context.active_object.type+bpy.context.active_object.mode

        if typeandmode in {"CURVEEDIT","SURFACEEDIT"}:
            bpy.ops.curve.select_linked()
            return {'FINISHED'}
        elif typeandmode == "GPENCILEDIT_GPENCIL":
            bpy.ops.gpencil.select_linked()
            return {'FINISHED'}
        elif typeandmode == "GREASEPENCILEDIT":
            bpy.ops.grease_pencil.select_linked()
            return {'FINISHED'}
        elif typeandmode == "ARMATUREEDIT":
            bpy.ops.armature.select_linked()
        elif typeandmode == "ARMATUREPOSE":
            bpy.ops.pose.select_linked()
        elif bpy.context.mode == "OBJECT" or typeandmode == "MESHEDIT":
            bpy.ops.wm.call_menu(name="view3d.mt_select_select_linked_menu")
        return {'FINISHED'}


classes = (
    BUTTON_ACTION_OT_global_select_lasso_set,
    BUTTON_ACTION_OT_select_select_mirror,
    VIEW3D_MT_select_select_by_type_menu,
    VIEW3D_MT_object_select_more_or_less_menu,
    BUTTON_ACTION_OT_call_object_select_more_or_less_menu,
    BUTTON_ACTION_OT_object_select_more,
    BUTTON_ACTION_OT_object_select_less,
    BUTTON_ACTION_OT_object_select_hierarchy_parent_child,
    VIEW3D_MT_select_select_grouped_menu,
    BUTTON_ACTION_OT_call_select_select_grouped_menu,
    VIEW3D_MT_select_select_linked_menu,
    BUTTON_ACTION_OT_call_select_select_linked_menu,
)

def register():
    for cls in classes:
        bpy.utils.register_class(cls)

def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)