# 这里只包含使用快捷键的功能：
import bpy

# 全局“移动”功能
class BUTTON_ACTION_OT_grab(bpy.types.Operator):
    bl_idname = "button.action_global_grab"
    bl_label = "移动"
    bl_description = "快捷键 G"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.ops.transform.translate('INVOKE_DEFAULT')
        return {'FINISHED'}
    
# 全局“缩放”功能
class BUTTON_ACTION_OT_scale(bpy.types.Operator):
    bl_idname = "button.action_global_scale"
    bl_label = "缩放"
    bl_description = "快捷键 S"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.ops.transform.resize('INVOKE_DEFAULT')
        return {'FINISHED'}

# 全局“旋转”功能    
class BUTTON_ACTION_OT_rotate(bpy.types.Operator):
    bl_idname = "button.action_global_rotate"
    bl_label = "旋转(R)"
    bl_description = "快捷键 R"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.ops.transform.rotate('INVOKE_DEFAULT')
        return {'FINISHED'}
    
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

# 全局“添加”菜单功能
class BUTTON_ACTION_OT_global_add(bpy.types.Operator):
    bl_idname = "button.action_global_add"
    bl_label = "添加"
    bl_description = "快捷键 Shift A"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        typeandmode = bpy.context.active_object.type+bpy.context.active_object.mode

        if bpy.context.mode == 'OBJECT':
            bpy.ops.wm.call_menu(name="VIEW3D_MT_add")
        if typeandmode == "CURVEEDIT":
            bpy.ops.wm.call_menu(name="VIEW3D_MT_curve_add")
        if typeandmode == 'SURFACEEDIT':
            bpy.ops.wm.call_menu(name="VIEW3D_MT_surface_add")
        if typeandmode == 'METAEDIT':
            bpy.ops.wm.call_menu(name="VIEW3D_MT_metaball_add")
        if typeandmode == 'MESHEDIT':
            bpy.ops.wm.call_menu(name="VIEW3D_MT_mesh_add")
        if typeandmode == 'ARMATUREEDIT':
            bpy.ops.wm.call_menu(name="TOPBAR_MT_edit_armature_add")
        return {'FINISHED'}

# 全局“复制 Shift D”按钮功能
class BUTTON_ACTION_OT_global_duplicate_move(bpy.types.Operator):
    bl_idname = "button.action_global_duplicate_move"
    bl_label = "复制"
    bl_description = "快捷键 Shift D"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        typeandmode = bpy.context.active_object.type+bpy.context.active_object.mode
        if bpy.context.mode == "OBJECT":
            bpy.ops.object.duplicate_move('INVOKE_DEFAULT')
        elif typeandmode in {"CURVEEDIT","SURFACEEDIT"}:
            bpy.ops.curve.duplicate_move('INVOKE_DEFAULT')
        elif typeandmode == "METAEDIT":
            bpy.ops.mball.duplicate_move('INVOKE_DEFAULT')
        elif typeandmode == "GPENCILEDIT_GPENCIL":
            bpy.ops.gpencil.duplicate_move('INVOKE_DEFAULT')
        elif typeandmode == "GREASEPENCILEDIT":
            bpy.ops.grease_pencil.duplicate_move('INVOKE_DEFAULT')
        elif typeandmode == "MESHEDIT":
            bpy.ops.mesh.duplicate_move('INVOKE_DEFAULT')
        elif typeandmode == "ARMATUREEDIT":
            bpy.ops.armature.duplicate_move('INVOKE_DEFAULT')
        return {'FINISHED'}
    
# 物体模式/蜡笔“复制 Ctrl C”按钮功能
class BUTTON_ACTION_OT_global_copy(bpy.types.Operator):
    bl_idname = "button.action_global_copy"
    bl_label = "复制"
    bl_description = "快捷键 Ctrl C"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        typeandmode = bpy.context.active_object.type+bpy.context.active_object.mode
        if bpy.context.mode == "OBJECT":
            bpy.ops.view3d.copybuffer()
        elif typeandmode == "ARMATUREPOSE":
            bpy.ops.pose.copy()
        elif typeandmode == "GPENCILEDIT_GPENCIL":
            bpy.ops.gpencil.copy()
        elif typeandmode == "GREASEPENCILEDIT":
            bpy.ops.grease_pencil.copy()
        return {'FINISHED'}
    
# 物体模式/蜡笔“复制 Ctrl C”按钮功能
class BUTTON_ACTION_OT_global_paste(bpy.types.Operator):
    bl_idname = "button.action_global_paste"
    bl_label = "粘贴"
    bl_description = "快捷键 Ctrl V"
    bl_options = {'REGISTER', 'UNDO'}

    autoselect: bpy.props.BoolProperty( # 粘贴“物体”用
        name="选择",
        default=True,
        description="扩展选择，而不是先取消选择",
        update=lambda self, context: self.execute(context) #if bpy.context.mode == 'EDIT_MESH' else None
    )

    active_collection: bpy.props.BoolProperty(  # 粘贴“物体”用
        name="活动集合",
        default=True,
        description="扩展选择，而不是先取消选择",
        update=lambda self, context: self.execute(context) #if bpy.context.mode == 'EDIT_MESH' else None
    )

    type: bpy.props.EnumProperty(   # 4.2 版本粘贴蜡笔用
        name="类型",
        items=[
            ('ACTIVE', "粘贴到活动项", ""),
            ('LAYER', "按层粘贴", ""),
        ],
        default='ACTIVE',
        update=lambda self, context: self.execute(context) #if bpy.context.mode == 'EDIT_MESH' else None
    )

    paste_back: bpy.props.BoolProperty(  # 4.2 4.3 两个版本共用粘贴蜡笔用
        name="粘贴到最后",
        default=False,
        description="将画笔粘贴到所有画笔之后",
        update=lambda self, context: self.execute(context) #if bpy.context.mode == 'EDIT_MESH' else None
    )

    keep_world_transform: bpy.props.BoolProperty(  # 4.3 版本粘贴蜡笔用
        name="保持世界变换",
        default=False,
        description="保持剪贴板中笔画的世界变换不变",
        update=lambda self, context: self.execute(context) #if bpy.context.mode == 'EDIT_MESH' else None
    )

    flipped: bpy.props.BoolProperty( # 粘贴“物体”用
        name="没X轴翻转",
        default=False,
        description="将存储的翻转姿态粘贴到当前姿态",
        update=lambda self, context: self.execute(context) 
    )

    selected_mask: bpy.props.BoolProperty( # 粘贴“物体”用
        name="只考虑所选部分",
        default=False,
        description="只将存储的姿态粘贴到当前姿态中的所选骨骼上",
        update=lambda self, context: self.execute(context) 
    )

    def invoke(self, context, event):
        return self.execute(context)
    
    def draw(self, context):
        typeandmode = bpy.context.active_object.type + bpy.context.active_object.mode

        layout = self.layout
        split = layout.row().split(factor=0.4)
        
        # 左侧列 - 标签
        col_left = split.column()
        col_left.alignment = 'RIGHT'
        if bpy.context.mode == "OBJECT":
            col_left.label(text="")
            col_left.label(text="")
        elif typeandmode == "GPENCILEDIT_GPENCIL":
            col_left.label(text="类型")
            col_left.label(text="") 
            col_left.label(text="")    
        elif typeandmode == "GREASEPENCILEDIT":
            col_left.label(text="") 
            col_left.label(text="")
        elif typeandmode == "ARMATUREPOSE":
            col_left.label(text="") 
            col_left.label(text="")
        
        # 右侧列 - 垂直排列的单选按钮
        col_right = split.column()
        if bpy.context.mode == "OBJECT":
            col_right.prop(self, "autoselect")
            col_right.prop(self, "active_collection")
        elif typeandmode == "GPENCILEDIT_GPENCIL":
            col_right.prop(self, "type", expand=True)
            col_right.prop(self, "paste_back")    
        elif typeandmode == "GREASEPENCILEDIT":
            col_right.prop(self, "paste_back") 
            col_right.prop(self, "keep_world_transform")
        elif typeandmode == "ARMATUREPOSE":
            col_right.prop(self, "flipped")
            col_right.prop(self, "selected_mask")

    def execute(self, context):
        typeandmode = bpy.context.active_object.type+bpy.context.active_object.mode
        if bpy.context.mode == "OBJECT":
            bpy.ops.view3d.pastebuffer(autoselect=self.autoselect, active_collection=self.active_collection)
        elif typeandmode == "GPENCILEDIT_GPENCIL":
            bpy.ops.gpencil.paste(type=self.type, paste_back=self.paste_back)
        elif typeandmode == "GREASEPENCILEDIT":
            bpy.ops.grease_pencil.paste(paste_back=self.paste_back, keep_world_transform=self.keep_world_transform)
        elif typeandmode == "ARMATUREPOSE":
            bpy.ops.pose.paste(flipped=self.flipped, selected_mask=self.selected_mask)
        return {'FINISHED'}

# 定义“删除”菜单
class VIEW3D_MT_global_delete_menu(bpy.types.Menu):
    bl_label = "删除"
    bl_idname = "view3d.mt_global_delete_menu"

    def draw(self, context):
        layout = self.layout

        typeandmode = bpy.context.active_object.type+bpy.context.active_object.mode

        if bpy.context.mode == "OBJECT":
            layout.operator("object.delete", text="删除", icon="QUESTION").use_global=False
        elif typeandmode == "MESHEDIT":
            layout.operator("mesh.dissolve_mode", text="融并删除" ,icon="CANCEL")
            layout.separator()
            layout.operator("mesh.delete", text="顶点").type='VERT'
            layout.operator("mesh.delete", text="边").type='EDGE'
            layout.operator("mesh.delete", text="面").type='FACE'
            layout.operator("mesh.delete", text="仅边和面").type='EDGE_FACE'
            layout.operator("mesh.delete", text="仅面").type='ONLY_FACE'
            layout.separator()
            layout.operator("mesh.dissolve_verts", text="融并顶点")
            layout.operator("mesh.dissolve_edges", text="融并边")
            layout.operator("mesh.dissolve_faces", text="融并面")
            layout.separator()
            layout.operator("mesh.dissolve_limited", text="有限融并")
            layout.separator()
            layout.operator("mesh.edge_collapse", text="塌陷边和面")
            layout.operator("mesh.delete_edgeloop", text="循环边")
        elif typeandmode == "METAEDIT":
            layout.operator("mball.delete_metaelems", text="删除", icon="QUESTION")
        elif typeandmode == "GPENCILEDIT_GPENCIL":
            layout.operator("gpencil.delete", text="点").type='POINTS'
            layout.operator("gpencil.delete", text="笔画").type='STROKES'
            layout.operator("gpencil.delete", text="帧").type='FRAME'
            layout.separator()
            layout.operator("gpencil.dissolve", text="消融").type='POINTS'
            layout.operator("gpencil.dissolve", text="融并期间").type='BETWEEN'
            layout.operator("gpencil.dissolve", text="融并未选中").type='UNSELECT'
            layout.separator()
            layout.operator("gpencil.delete", text="删除活动层的活动帧").type='FRAME'
            layout.operator("gpencil.active_frames_delete_all", text="删除全部层的活动帧")
        elif typeandmode == "GPENCILPAINT_GPENCIL":
            layout.operator("gpencil.delete", text="删除活动层的活动帧").type='FRAME'
            layout.operator("gpencil.active_frames_delete_all", text="删除全部层的活动帧")
        elif typeandmode == "GREASEPENCILEDIT":        
            layout.operator("grease_pencil.delete", text="删除")
            layout.separator()
            layout.operator("grease_pencil.dissolve", text="消融").type='POINTS'
            layout.operator("grease_pencil.dissolve", text="融并其间").type='BETWEEN'
            layout.operator("grease_pencil.dissolve", text="融并未选中").type='UNSELECT'
            layout.separator()
            layout.operator("grease_pencil.delete_frame", text="删除活动层的活动关键帧").type='ACTIVE_FRAME'
            layout.operator("grease_pencil.delete_frame", text="删除所有层的活动关键帧").type='ALL_FRAMES'
        elif typeandmode == "ARMATUREEDIT":
            layout.operator("armature.delete", text="骨骼")
            layout.separator()
            layout.operator("armature.dissolve", text="融并骨骼")
        elif typeandmode in {"CURVEEDIT","SURFACEEDIT"}:
            layout.operator("curve.delete", text="顶点").type='VERT'
            layout.operator("curve.delete", text="段数").type='SEGMENT'
            layout.separator()
            layout.operator("curve.dissolve_verts", text="融并顶点")

# 定义调用“删除”菜单操作
class BUTTON_ACTION_OT_call_global_delete_menu(bpy.types.Operator):
    bl_idname = "button.action_global_call_delete_menu"
    bl_label = "删除"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.ops.wm.call_menu(name="view3d.mt_global_delete_menu")
        return {'FINISHED'}

# 多种编辑模式“隐藏”/"隐藏未选项"
class BUTTON_ACTION_OT_global_hide_view_set(bpy.types.Operator):
    bl_idname = "button.action_global_hide_view_set"
    bl_label = "隐藏"
    bl_description = "快捷键 H"
    bl_options = {'REGISTER', 'UNDO'}

    unselected: bpy.props.BoolProperty(
        name="未选中项",
        default=False,
        description="隐藏未选中项而不是选择项",
        update=lambda self, context: self.execute(context) 
    )

    def invoke(self, context, event):
        return self.execute(context)

    def draw(self, context):

        layout = self.layout
        split = layout.row().split(factor=0.4)
        
        # 左侧列 - 标签
        col_left = split.column()
        col_left.alignment = 'RIGHT'
        col_left.label(text="")
        
        # 右侧列 - 垂直排列的单选按钮
        col_right = split.column()
        col_right.prop(self, "unselected")

    def execute(self, context):
        typeandmode = bpy.context.active_object.type+bpy.context.active_object.mode
        
        if bpy.context.mode == "OBJECT":
            bpy.ops.object.hide_view_set(unselected=self.unselected)
        if typeandmode in {"CURVEEDIT","SURFACEEDIT"}:
            bpy.ops.curve.hide(unselected=self.unselected)
        if typeandmode == "METAEDIT":
            bpy.ops.mball.hide_metaelems(unselected=self.unselected)
        if typeandmode == "MESHEDIT":
            bpy.ops.mesh.hide(unselected=self.unselected)
        if typeandmode in {"GPENCILEDIT_GPENCIL","GPENCILPAINT_GPENCIL"}:
            bpy.ops.gpencil.hide(unselected=self.unselected)
        if typeandmode in {"GREASEPENCILEDIT","GREASEPENCILPAINT_GREASE_PENCIL"}:
            bpy.ops.grease_pencil.layer_hide(unselected=self.unselected)
        if typeandmode == "ARMATUREEDIT":
            bpy.ops.armature.hide(unselected=self.unselected)
        if typeandmode == "ARMATUREPOSE":
            bpy.ops.pose.hide(unselected=self.unselected)
        return {'FINISHED'}
    
# 多种编辑模式"显示隐藏项"
class BUTTON_ACTION_OT_global_hide_view_clear(bpy.types.Operator):
    bl_idname = "button.action_global_hide_view_clear"
    bl_label = "显示隐藏项"
    bl_description = "快捷键 Alt H"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        typeandmode = bpy.context.active_object.type+bpy.context.active_object.mode
        
        if bpy.context.mode == "OBJECT":
            bpy.ops.object.hide_view_clear()
        if typeandmode in {"CURVEEDIT","SURFACEEDIT"}:
            bpy.ops.curve.reveal()
        if typeandmode == "METAEDIT":
            bpy.ops.mball.reveal_metaelems()
        if typeandmode == "MESHEDIT":
            bpy.ops.mesh.reveal()
        if typeandmode in {"GPENCILEDIT_GPENCIL","GPENCILPAINT_GPENCIL"}:
            bpy.ops.gpencil.reveal()
        if typeandmode in {"GREASEPENCILEDIT","GREASEPENCILPAINT_GREASE_PENCIL"}:
            bpy.ops.grease_pencil.layer_reveal()
        if typeandmode == "ARMATUREEDIT":
            bpy.ops.armature.reveal()
        if typeandmode == "ARMATUREPOSE":
            bpy.ops.pose.reveal()
        return {'FINISHED'}
    
# 物体模式/骨骼姿态模式——“应用 Ctrl A”操作
class BUTTON_ACTION_OT_global_apply(bpy.types.Operator):
    bl_idname = "button.action_global_apply"
    bl_label = "应用"
    bl_description = "快捷键 Ctrl A"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        typeandmode = bpy.context.active_object.type+bpy.context.active_object.mode
        
        if bpy.context.mode == "OBJECT":
            bpy.ops.wm.call_menu(name="VIEW3D_MT_object_apply")
        elif typeandmode == "ARMATUREPOSE":
            bpy.ops.wm.call_menu(name="VIEW3D_MT_pose_apply")
        return {'FINISHED'}
    
# 物体模式/网格模式/骨骼姿态模式——“交互镜像 Ctrl M”操作
class BUTTON_ACTION_OT_global_transform_mirror(bpy.types.Operator):
    bl_idname = "button.action_global_transform_mirror"
    bl_label = "交互镜像"
    bl_description = "快捷键 Ctrl M"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.ops.transform.mirror('INVOKE_DEFAULT')    
        return {'FINISHED'}

# 物体模式/骨骼姿态“清空变换(菜单)”操作
class BUTTON_ACTION_OT_global_object_pose_clear(bpy.types.Operator):
    bl_idname = "button.action_global_object_pose_clear"
    bl_label = "清空变换"
    bl_description = "物体模式/骨骼姿态模式“清空变换”菜单"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        typeandmode = bpy.context.active_object.type+bpy.context.active_object.mode
        
        if bpy.context.mode == "OBJECT":
            bpy.ops.wm.call_menu(name="VIEW3D_MT_object_clear")
        elif typeandmode == "ARMATUREPOSE":
            bpy.ops.wm.call_menu(name="VIEW3D_MT_pose_transform")
        return {'FINISHED'}


classes = (
    BUTTON_ACTION_OT_grab,
    BUTTON_ACTION_OT_scale,
    BUTTON_ACTION_OT_rotate,
    BUTTON_ACTION_OT_global_select_all,
    BUTTON_ACTION_OT_global_select_invert,
    BUTTON_ACTION_OT_global_select_circle,
    BUTTON_ACTION_OT_global_duplicate_move,
    BUTTON_ACTION_OT_global_add,
    BUTTON_ACTION_OT_global_copy,
    BUTTON_ACTION_OT_global_paste,
    BUTTON_ACTION_OT_call_global_delete_menu,
    VIEW3D_MT_global_delete_menu,
    BUTTON_ACTION_OT_global_hide_view_set,
    BUTTON_ACTION_OT_global_hide_view_clear,
    BUTTON_ACTION_OT_global_apply,
    BUTTON_ACTION_OT_global_transform_mirror,
    BUTTON_ACTION_OT_global_object_pose_clear,
)

def register():
    for cls in classes:
        bpy.utils.register_class(cls)

def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)




