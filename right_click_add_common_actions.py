import bpy

def draw_add_to_switcher_common(self, context):
    ADDON_NAME = __package__.split('.')[0]

    show_switcher = bpy.context.preferences.addons[ADDON_NAME].preferences.to_show_to_switcher
    if not show_switcher:
        return
    
    op = getattr(context, "operator", None) or getattr(context, "button_operator", None)
    # 检查右键对象是否为 Transform → Translate (Move)
    if op and op.bl_rna.identifier == "TRANSFORM_OT_translate":
        layout = self.layout
        layout.separator()
        layout.operator("call.add_to_switcher_menu", text="\"移动\"添加到Switcher", icon='EVENT_G').action = 'button.action_global_grab'
        layout.operator("call.add_to_switcher_menu", text="添加分隔符到Switcher", icon='REMOVE').action = 'SEPARATOR'
    elif op and op.bl_rna.identifier == "TRANSFORM_OT_resize":
        layout = self.layout
        layout.separator()
        layout.operator("call.add_to_switcher_menu", text="\"缩放\"添加到Switcher", icon='EVENT_S').action = 'button.action_global_scale'
        layout.operator("call.add_to_switcher_menu", text="添加分隔符到Switcher", icon='REMOVE').action = 'SEPARATOR'
    elif op and op.bl_rna.identifier == "TRANSFORM_OT_rotate":
        layout = self.layout
        layout.separator()
        layout.operator("call.add_to_switcher_menu", text="\"旋转\"添加到Switcher", icon='EVENT_R').action = 'button.action_global_rotate'
        layout.operator("call.add_to_switcher_menu", text="添加分隔符到Switcher", icon='REMOVE').action = 'SEPARATOR'
    elif op and op.bl_rna.identifier in {
        "OBJECT_OT_duplicate_move",
        "CURVE_OT_duplicate_move",
        "MBALL_OT_duplicate_move",
        "GPENCIL_OT_duplicate_move", # 4.2 edition
        "GREASE_PENCIL_OT_duplicate_move", # 4.3 edition
        "MESH_OT_duplicate_move",
        "ARMATURE_OT_duplicate_move",
        }:
        layout = self.layout
        layout.separator()
        layout.operator("call.add_to_switcher_menu", text="\"复制\"添加到Switcher", icon='DUPLICATE').action = 'button.action_global_duplicate_move'
        layout.operator("call.add_to_switcher_menu", text="添加分隔符到Switcher", icon='REMOVE').action = 'SEPARATOR'
    elif op and op.bl_rna.identifier in {
        "VIEW3D_OT_copybuffer",
        "GPENCIL_OT_copy", # 4.2 edition
        "GREASE_PENCIL_OT_copy", # 4.3 edition
        "POSE_OT_copy",
        }:
        layout = self.layout
        layout.separator()
        layout.operator("call.add_to_switcher_menu", text="\"复制\"添加到Switcher", icon='COPYDOWN').action = 'button.action_global_copy'
        layout.operator("call.add_to_switcher_menu", text="添加分隔符到Switcher", icon='REMOVE').action = 'SEPARATOR'
    elif op and op.bl_rna.identifier in {
        "VIEW3D_OT_pastebuffer",
        "GPENCIL_OT_paste", # 4.2 edition
        "GREASE_PENCIL_OT_paste", # 4.3 edition
        "POSE_OT_paste",
        }:
        layout = self.layout
        layout.separator()
        layout.operator("call.add_to_switcher_menu", text="\"粘贴\"添加到Switcher", icon='PASTEDOWN').action = 'button.action_global_paste'
        layout.operator("call.add_to_switcher_menu", text="添加分隔符到Switcher", icon='REMOVE').action = 'SEPARATOR'
    elif op and op.bl_rna.identifier in {
        "OBJECT_OT_delete",
        "MBALL_OT_delete_metaelems",
        }:
        layout = self.layout
        layout.separator()
        layout.operator("call.add_to_switcher_menu", text="\"删除\"添加到Switcher", icon='EVENT_X').action = 'button.action_global_call_delete_menu'
        layout.operator("call.add_to_switcher_menu", text="添加分隔符到Switcher", icon='REMOVE').action = 'SEPARATOR'
    elif op and op.bl_rna.identifier in {
        "OBJECT_OT_hide_view_set",
        "CURVE_OT_hide",
        "MBALL_OT_hide_metaelems",
        "MESH_OT_hide",
        "GPENCIL_OT_hide",
        "GREASE_PENCIL_OT_layer_hide",
        "ARMATURE_OT_hide",
        "POSE_OT_hide",
        }:
        layout = self.layout
        layout.separator()
        layout.operator("call.add_to_switcher_menu", text="\"隐藏\"添加到Switcher", icon='EVENT_H').action = 'button.action_global_hide_view_set'
        layout.operator("call.add_to_switcher_menu", text="添加分隔符到Switcher", icon='REMOVE').action = 'SEPARATOR'
    elif op and op.bl_rna.identifier in {
        "OBJECT_OT_hide_view_clear",
        "CURVE_OT_reveal",
        "MBALL_OT_reveal_metaelems",
        "MESH_OT_reveal",
        "GPENCIL_OT_reveal",
        "GREASE_PENCIL_OT_layer_reveal",
        "ARMATURE_OT_reveal",
        "POSE_OT_reveal",
        }:
        layout = self.layout
        layout.separator()
        layout.operator("call.add_to_switcher_menu", text="\"显示隐藏项\"添加到Switcher", icon='HIDE_OFF').action = 'button.action_global_hide_view_clear'
        layout.operator("call.add_to_switcher_menu", text="添加分隔符到Switcher", icon='REMOVE').action = 'SEPARATOR'
    elif op and op.bl_rna.identifier == "TRANSFORM_OT_mirror":
        layout = self.layout
        layout.separator()
        layout.operator("call.add_to_switcher_menu", text="\"交互镜像\"添加到Switcher", icon='MOD_MIRROR').action = 'button.action_global_transform_mirror'
        layout.operator("call.add_to_switcher_menu", text="添加分隔符到Switcher", icon='REMOVE').action = 'SEPARATOR'
















































































#不能使用 draw_add_to_switcher_common 的添加到 Switcher 方法：
def add_menu_to_switcher(self, context):
    show_switcher = bpy.context.preferences.addons[__package__].preferences.to_show_to_switcher
    if not show_switcher:
        return
    self.layout.separator()
    self.layout.operator("call.add_to_switcher_menu", text="\"添加(菜单)\"添加到Switcher", icon='PRESET').action = 'button.action_global_add'
    self.layout.operator("call.add_to_switcher_menu", text="添加分隔符到Switcher", icon='REMOVE').action = 'SEPARATOR'

def delete_menu_to_switcher(self, context):
    show_switcher = bpy.context.preferences.addons[__package__].preferences.to_show_to_switcher
    if not show_switcher:
        return
    self.layout.separator()
    self.layout.operator("call.add_to_switcher_menu", text="\"删除(菜单)\"添加到Switcher", icon='EVENT_X').action = 'button.action_global_call_delete_menu'
    self.layout.operator("call.add_to_switcher_menu", text="添加分隔符到Switcher", icon='REMOVE').action = 'SEPARATOR'

def apply_menu_to_switcher(self, context):
    show_switcher = bpy.context.preferences.addons[__package__].preferences.to_show_to_switcher
    if not show_switcher:
        return
    self.layout.separator()
    self.layout.operator("call.add_to_switcher_menu", text="\"应用(菜单)\"添加到Switcher", icon='PRESET').action = 'button.action_global_apply'
    self.layout.operator("call.add_to_switcher_menu", text="添加分隔符到Switcher", icon='REMOVE').action = 'SEPARATOR'

def cleartransform_menu_to_switcher(self, context):
    show_switcher = bpy.context.preferences.addons[__package__].preferences.to_show_to_switcher
    if not show_switcher:
        return
    self.layout.separator()
    self.layout.operator("call.add_to_switcher_menu", text="\"清空变换(菜单)\"添加到Switcher", icon='PRESET').action = 'button.action_global_object_pose_clear'
    self.layout.operator("call.add_to_switcher_menu", text="添加分隔符到Switcher", icon='REMOVE').action = 'SEPARATOR'

def transformorientation_menu_to_switcher(self, context):
    show_switcher = bpy.context.preferences.addons[__package__].preferences.to_show_to_switcher
    if not show_switcher:
        return
    self.layout.separator()
    self.layout.operator("call.add_to_switcher_menu", text="\"切换坐标系(菜单)\"添加到Switcher", icon='PRESET').action = 'button.action_switch_orientation_menu'
    self.layout.operator("call.add_to_switcher_menu", text="\"全局\"添加到Switcher", icon='ORIENTATION_GLOBAL').action = 'button.action_orientation_to_global'
    self.layout.operator("call.add_to_switcher_menu", text="\"局部\"添加到Switcher", icon='ORIENTATION_LOCAL').action = 'button.action_orientation_to_local'
    self.layout.operator("call.add_to_switcher_menu", text="\"法向\"添加到Switcher", icon='ORIENTATION_NORMAL').action = 'button.action_orientation_to_normal'
    self.layout.operator("call.add_to_switcher_menu", text="\"万向\"添加到Switcher", icon='ORIENTATION_GIMBAL').action = 'button.action_orientation_to_gimbal'
    self.layout.operator("call.add_to_switcher_menu", text="\"视图\"添加到Switcher", icon='ORIENTATION_VIEW').action = 'button.action_orientation_to_view'
    self.layout.operator("call.add_to_switcher_menu", text="\"游标\"添加到Switcher", icon='ORIENTATION_CURSOR').action = 'button.action_orientation_to_cursor'
    self.layout.operator("call.add_to_switcher_menu", text="\"父级\"添加到Switcher", icon='ORIENTATION_PARENT').action = 'button.action_orientation_to_parent'
    self.layout.operator("call.add_to_switcher_menu", text="添加分隔符到Switcher", icon='REMOVE').action = 'SEPARATOR'

def switchsnap_menu_to_switcher(self, context):
    show_switcher = bpy.context.preferences.addons[__package__].preferences.to_show_to_switcher
    if not show_switcher:
        return
    self.layout.separator()
    self.layout.operator("call.add_to_switcher_menu", text="\"切换吸附(菜单)\"添加到Switcher", icon='PRESET').action = 'button.action_switch_snap_menu'
    self.layout.operator("call.add_to_switcher_menu", text="\"开/关吸附\"添加到Switcher", icon='SNAP_ON').action = 'button.action_switch_snap_toggle'
    self.layout.operator("call.add_to_switcher_menu", text="\"增量\"添加到Switcher", icon='SNAP_INCREMENT').action = 'button.action_switch_snap_increment'
    self.layout.operator("call.add_to_switcher_menu", text="\"顶点\"添加到Switcher", icon='SNAP_VERTEX').action = 'button.action_switch_snap_vertex'
    self.layout.operator("call.add_to_switcher_menu", text="\"边\"添加到Switcher", icon='SNAP_EDGE').action = 'button.action_switch_snap_edge'
    self.layout.operator("call.add_to_switcher_menu", text="\"面投射\"添加到Switcher", icon='SNAP_FACE').action = 'button.action_switch_snap_face'
    self.layout.operator("call.add_to_switcher_menu", text="\"面最近\"添加到Switcher", icon='SNAP_FACE_NEAREST').action = 'button.action_switch_snap_face_nearest'
    self.layout.operator("call.add_to_switcher_menu", text="\"体积\"添加到Switcher", icon='SNAP_VOLUME').action = 'button.action_switch_snap_volume'
    self.layout.operator("call.add_to_switcher_menu", text="\"边中点\"添加到Switcher", icon='SNAP_MIDPOINT').action = 'button.action_switch_snap_edge_midpoint'
    self.layout.operator("call.add_to_switcher_menu", text="\"垂直交线\"添加到Switcher", icon='SNAP_PERPENDICULAR').action = 'button.action_switch_snap_edge_perpendicular'
    self.layout.operator("call.add_to_switcher_menu", text="添加分隔符到Switcher", icon='REMOVE').action = 'SEPARATOR'

def switchproportional_menu_to_switcher(self, context):
    show_switcher = bpy.context.preferences.addons[__package__].preferences.to_show_to_switcher
    if not show_switcher:
        return
    self.layout.separator()
    self.layout.operator("call.add_to_switcher_menu", text="\"切换衰减编辑(菜单)\"添加到Switcher", icon='PRESET').action = 'button.action_switch_proportional_menu'
    self.layout.operator("call.add_to_switcher_menu", text="\"开/关衰减编辑\"添加到Switcher", icon='PROP_ON').action = 'button.action_switch_proportional_toggle'
    self.layout.operator("call.add_to_switcher_menu", text="\"平滑\"添加到Switcher", icon='SMOOTHCURVE').action = 'button.action_switch_proportional_smooth'
    self.layout.operator("call.add_to_switcher_menu", text="\"球体\"添加到Switcher", icon='SPHERECURVE').action = 'button.action_switch_proportional_sphere'
    self.layout.operator("call.add_to_switcher_menu", text="\"根凸\"添加到Switcher", icon='ROOTCURVE').action = 'button.action_switch_proportional_root'
    self.layout.operator("call.add_to_switcher_menu", text="\"平方反比\"添加到Switcher", icon='INVERSESQUARECURVE').action = 'button.action_switch_proportional_inverse_square'
    self.layout.operator("call.add_to_switcher_menu", text="\"锐利\"添加到Switcher", icon='SHARPCURVE').action = 'button.action_switch_proportional_sharp'
    self.layout.operator("call.add_to_switcher_menu", text="\"线性\"添加到Switcher", icon='LINCURVE').action = 'button.action_switch_proportional_linear'
    self.layout.operator("call.add_to_switcher_menu", text="\"常值\"添加到Switcher", icon='NOCURVE').action = 'button.action_switch_proportional_constant'
    self.layout.operator("call.add_to_switcher_menu", text="\"随机\"添加到Switcher", icon='RNDCURVE').action = 'button.action_switch_proportional_random'
    self.layout.operator("call.add_to_switcher_menu", text="添加分隔符到Switcher", icon='REMOVE').action = 'SEPARATOR'


def register():
    bpy.types.UI_MT_button_context_menu.append(draw_add_to_switcher_common)
    #“添加”菜单
    bpy.types.VIEW3D_MT_add.append(add_menu_to_switcher)
    bpy.types.VIEW3D_MT_mesh_add.append(add_menu_to_switcher)
    bpy.types.VIEW3D_MT_curve_add.append(add_menu_to_switcher)
    bpy.types.VIEW3D_MT_surface_add.append(add_menu_to_switcher)
    bpy.types.VIEW3D_MT_metaball_add.append(add_menu_to_switcher)
    bpy.types.TOPBAR_MT_edit_armature_add.append(add_menu_to_switcher)

    #“删除”菜单
    bpy.types.VIEW3D_MT_edit_mesh_delete.append(delete_menu_to_switcher)
    if bpy.app.version <= (4, 2, 0):
        bpy.types.VIEW3D_MT_edit_gpencil_delete.append(delete_menu_to_switcher)    
    elif bpy.app.version >= (4, 3, 0):
        bpy.types.VIEW3D_MT_edit_greasepencil_delete.append(delete_menu_to_switcher)
    bpy.types.VIEW3D_MT_edit_armature_delete.append(delete_menu_to_switcher)
    bpy.types.VIEW3D_MT_edit_curve_delete.append(delete_menu_to_switcher)
    
    #“应用”菜单
    bpy.types.VIEW3D_MT_object_apply.append(apply_menu_to_switcher)
    bpy.types.VIEW3D_MT_pose_apply.append(apply_menu_to_switcher)

    #"清空变换"菜单
    bpy.types.VIEW3D_MT_object_clear.append(cleartransform_menu_to_switcher)
    bpy.types.VIEW3D_MT_pose_transform.append(cleartransform_menu_to_switcher)

    #切换坐标系
    bpy.types.VIEW3D_PT_transform_orientations.append(transformorientation_menu_to_switcher)

    #切换吸附菜单
    bpy.types.VIEW3D_PT_snapping.append(switchsnap_menu_to_switcher)

    #切换衰减编辑
    bpy.types.VIEW3D_PT_proportional_edit.append(switchproportional_menu_to_switcher)

def unregister():
    #切换衰减编辑
    bpy.types.VIEW3D_PT_proportional_edit.remove(switchproportional_menu_to_switcher)

    #切换吸附菜单
    bpy.types.VIEW3D_PT_snapping.remove(switchsnap_menu_to_switcher)

    #切换坐标系
    bpy.types.VIEW3D_PT_transform_orientations.remove(transformorientation_menu_to_switcher)

    #"清空变换"菜单
    bpy.types.VIEW3D_MT_pose_transform.remove(cleartransform_menu_to_switcher)
    bpy.types.VIEW3D_MT_object_clear.remove(cleartransform_menu_to_switcher)

    #“应用”菜单
    bpy.types.VIEW3D_MT_pose_apply.remove(apply_menu_to_switcher)
    bpy.types.VIEW3D_MT_object_apply.remove(apply_menu_to_switcher)

    #“删除”菜单
    bpy.types.VIEW3D_MT_edit_mesh_delete.remove(delete_menu_to_switcher)
    bpy.types.VIEW3D_MT_edit_armature_delete.remove(delete_menu_to_switcher)
    bpy.types.VIEW3D_MT_edit_curve_delete.remove(delete_menu_to_switcher)
    if bpy.app.version <= (4, 2, 0):
        bpy.types.VIEW3D_MT_edit_gpencil_delete.remove(delete_menu_to_switcher)
    elif bpy.app.version >= (4, 3, 0):
        bpy.types.VIEW3D_MT_edit_greasepencil_delete.remove(delete_menu_to_switcher)

    #“添加”菜单
    bpy.types.TOPBAR_MT_edit_armature_add.remove(add_menu_to_switcher)
    bpy.types.VIEW3D_MT_metaball_add.remove(add_menu_to_switcher)
    bpy.types.VIEW3D_MT_surface_add.remove(add_menu_to_switcher)
    bpy.types.VIEW3D_MT_curve_add.remove(add_menu_to_switcher)
    bpy.types.VIEW3D_MT_mesh_add.remove(add_menu_to_switcher)
    bpy.types.VIEW3D_MT_add.remove(add_menu_to_switcher)

    bpy.types.UI_MT_button_context_menu.remove(draw_add_to_switcher_common)

