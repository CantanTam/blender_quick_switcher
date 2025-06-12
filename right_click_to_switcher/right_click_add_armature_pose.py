import bpy
from .. import ADDON_NAME

def draw_add_to_switcher_armaturepose(self, context):
    show_switcher = bpy.context.preferences.addons[ADDON_NAME].preferences.to_show_to_switcher
    if not show_switcher:
        return
    
    op = getattr(context, "operator", None) or getattr(context, "button_operator", None)

    if op and op.bl_rna.identifier == "POSE_OT_select_constraint_target":
        layout = self.layout
        layout.separator()
        layout.operator("call.add_to_switcher_menu", text="\"约束目标\"⟶Switcher", icon='PLUS').action = 'action.pose_select_constraint_target'

    elif op and op.bl_rna.identifier == "POSE_OT_push_rest":
        layout = self.layout
        layout.separator()
        layout.operator("call.add_to_switcher_menu", text="\"从静置姿态推移姿态\"⟶Switcher", icon='PLUS').action = 'action.pose_push_rest'

    elif op and op.bl_rna.identifier == "POSE_OT_relax_rest":
        layout = self.layout
        layout.separator()
        layout.operator("call.add_to_switcher_menu", text="\"松弛姿态至静置姿态\"⟶Switcher", icon='PLUS').action = 'action.pose_relax_rest'

    elif op and op.bl_rna.identifier == "POSE_OT_push":
        layout = self.layout
        layout.separator()
        layout.operator("call.add_to_switcher_menu", text="\"从补间姿态推移姿态\"⟶Switcher", icon='PLUS').action = 'action.pose_push'

    elif op and op.bl_rna.identifier == "POSE_OT_relax":
        layout = self.layout
        layout.separator()
        layout.operator("call.add_to_switcher_menu", text="\"松弛姿态到补间姿态\"⟶Switcher", icon='PLUS').action = 'action.pose_relax'

    elif op and op.bl_rna.identifier == "POSE_OT_breakdown":
        layout = self.layout
        layout.separator()
        layout.operator("call.add_to_switcher_menu", text="\"姿态补间器\"⟶Switcher", icon='PLUS').action = 'action.pose_breakdown'

    elif op and op.bl_rna.identifier == "POSE_OT_blend_to_neighbor":
        layout = self.layout
        layout.separator()
        layout.operator("call.add_to_switcher_menu", text="\"混合至邻帧\"⟶Switcher", icon='PLUS').action = 'action.pose_blend_to_neighbor'

    elif op and op.bl_rna.identifier == "POSE_OT_blend_with_rest":
        layout = self.layout
        layout.separator()
        layout.operator("call.add_to_switcher_menu", text="\"将姿态与静置姿态混合\"⟶Switcher", icon='PLUS').action = 'action.pose_blend_with_rest'

    elif op and op.bl_rna.identifier == "POSE_OT_paths_calculate":
        layout = self.layout
        layout.separator()
        layout.operator("call.add_to_switcher_menu", text="\"计算运动路径\"⟶Switcher", icon='PLUS').action = 'action.pose_paths_calculate'

    elif op and op.bl_rna.identifier == "POSE_OT_paths_clear":
        layout = self.layout
        layout.separator()
        layout.operator("call.add_to_switcher_menu", text="\"清空运动路径\"⟶Switcher", icon='PLUS').action = 'action.pose_paths_clear'

    elif op and op.bl_rna.identifier == "POSE_OT_ik_add":
        layout = self.layout
        layout.separator()
        layout.operator("call.add_to_switcher_menu", text="\"为骨骼添加IK\"⟶Switcher", icon='PLUS').action = 'action.pose_ik_add'

    elif op and op.bl_rna.identifier == "POSE_OT_ik_clear":
        layout = self.layout
        layout.separator()
        layout.operator("call.add_to_switcher_menu", text="\"移除IK\"⟶Switcher", icon='PLUS').action = 'action.pose_ik_clear'

    elif op and op.bl_rna.identifier == "POSE_OT_constraint_add_with_targets":
        layout = self.layout
        layout.separator()
        layout.operator("call.add_to_switcher_menu", text="\"添加约束(带目标)(菜单)\"⟶Switcher", icon='PRESET').action = 'action.pose_constraint_add_with_targets'

    elif op and op.bl_rna.identifier == "POSE_OT_constraints_copy":
        layout = self.layout
        layout.separator()
        layout.operator("call.add_to_switcher_menu", text="\"将约束复制到当前所选骨骼\"⟶Switcher", icon='PLUS').action = 'action.pose_constraints_copy'

    elif op and op.bl_rna.identifier == "POSE_OT_constraints_clear":
        layout = self.layout
        layout.separator()
        layout.operator("call.add_to_switcher_menu", text="\"清除姿态约束\"⟶Switcher", icon='PLUS').action = 'action.pose_constraints_clear'





def armaturepose_select_moreless_menu_to_switcher(self, context):
    show_switcher = bpy.context.preferences.addons[ADDON_NAME].preferences.to_show_to_switcher
    if not show_switcher:
        return
    self.layout.separator()
    self.layout.operator("call.add_to_switcher_menu", text="\"父级/子级(菜单)\"⟶Switcher", icon='ORIENTATION_PARENT').action = 'action.global_select_select_parent_or_child'

def armaturepose_pose_slide_menu_to_switcher(self, context):
    show_switcher = bpy.context.preferences.addons[ADDON_NAME].preferences.to_show_to_switcher
    if not show_switcher:
        return
    self.layout.separator()
    self.layout.operator("call.add_to_switcher_menu", text="\"间帧调整(菜单)\"⟶Switcher", icon='PRESET').action = 'action.pose_pose_slide_menu'

def armaturepose_propagate_menu_to_switcher(self, context):
    show_switcher = bpy.context.preferences.addons[ADDON_NAME].preferences.to_show_to_switcher
    if not show_switcher:
        return
    self.layout.separator()
    self.layout.operator("call.add_to_switcher_menu", text="\"传导(菜单)\"⟶Switcher", icon='PRESET').action = 'action.pose_propagate_menu'

def armaturepose_motion_menu_to_switcher(self, context):
    show_switcher = bpy.context.preferences.addons[ADDON_NAME].preferences.to_show_to_switcher
    if not show_switcher:
        return
    self.layout.separator()
    self.layout.operator("call.add_to_switcher_menu", text="\"运动路径(菜单)\"⟶Switcher", icon='PRESET').action = 'action.pose_motion_menu'

def armaturepose_group_menu_to_switcher(self, context):
    show_switcher = bpy.context.preferences.addons[ADDON_NAME].preferences.to_show_to_switcher
    if not show_switcher:
        return
    self.layout.separator()
    self.layout.operator("call.add_to_switcher_menu", text="\"骨骼组(菜单)\"⟶Switcher", icon='PRESET').action = 'action.pose_group_menu'

def armaturepose_pose_ik_menu_to_switcher(self, context):
    show_switcher = bpy.context.preferences.addons[ADDON_NAME].preferences.to_show_to_switcher
    if not show_switcher:
        return
    self.layout.separator()
    self.layout.operator("call.add_to_switcher_menu", text="\"反向运动学(菜单)\"⟶Switcher", icon='PRESET').action = 'action.pose_ik_menu'

def armaturepose_constraints_menu_to_switcher(self, context):
    show_switcher = bpy.context.preferences.addons[ADDON_NAME].preferences.to_show_to_switcher
    if not show_switcher:
        return
    self.layout.separator()
    self.layout.operator("call.add_to_switcher_menu", text="\"约束(菜单)\"⟶Switcher", icon='PRESET').action = 'action.pose_constraints_menu'












def register():
    bpy.types.UI_MT_button_context_menu.append(draw_add_to_switcher_armaturepose)
    bpy.types.VIEW3D_MT_select_pose_more_less.append(armaturepose_select_moreless_menu_to_switcher)
    bpy.types.VIEW3D_MT_pose_slide.append(armaturepose_pose_slide_menu_to_switcher)
    bpy.types.VIEW3D_MT_pose_propagate.append(armaturepose_propagate_menu_to_switcher)
    bpy.types.VIEW3D_MT_pose_motion.append(armaturepose_motion_menu_to_switcher)
    bpy.types.VIEW3D_MT_pose_ik.append(armaturepose_pose_ik_menu_to_switcher)
    bpy.types.VIEW3D_MT_pose_constraints.append(armaturepose_constraints_menu_to_switcher)
    if bpy.app.version <= (4, 2, 0):
        bpy.types.VIEW3D_MT_pose_group.append(armaturepose_group_menu_to_switcher)

def unregister():
    if bpy.app.version <= (4, 2, 0):
        bpy.types.VIEW3D_MT_pose_group.remove(armaturepose_group_menu_to_switcher)
    bpy.types.VIEW3D_MT_pose_constraints.remove(armaturepose_constraints_menu_to_switcher)
    bpy.types.VIEW3D_MT_pose_ik.remove(armaturepose_pose_ik_menu_to_switcher)
    bpy.types.VIEW3D_MT_pose_motion.remove(armaturepose_motion_menu_to_switcher)
    bpy.types.VIEW3D_MT_pose_propagate.remove(armaturepose_propagate_menu_to_switcher)
    bpy.types.VIEW3D_MT_pose_slide.remove(armaturepose_pose_slide_menu_to_switcher)
    bpy.types.VIEW3D_MT_select_pose_more_less.remove(armaturepose_select_moreless_menu_to_switcher)
    bpy.types.UI_MT_button_context_menu.remove(draw_add_to_switcher_armaturepose)