import bpy

def draw_add_to_switcher_global_select(self, context):
    show_switcher = bpy.context.preferences.addons[__package__].preferences.to_show_to_switcher
    if not show_switcher:
        return
    
    op = getattr(context, "operator", None) or getattr(context, "button_operator", None)
    # 检查右键对象是否为视图操作
    if op and op.bl_rna.identifier in {
        "OBJECT_OT_select_all",
        "CURVE_OT_select_all",
        "MBALL_OT_select_all",
        "FONT_OT_select_all",
        "LATTICE_OT_select_all",
        "MESH_OT_select_all",
        "GPENCIL_OT_select_all",    #4.2 版本或以下
        "GREASE_PENCIL_OT_select_all", #4.3 版本或以上
        "ARMATURE_OT_select_all",
        "POSE_OT_select_all",
        }:
        layout = self.layout
        layout.separator()
        layout.operator("call.add_to_switcher_menu", text="\"全选\"添加到Switcher", icon='EVENT_A').action = 'button.action_global_select_all'
        layout.operator("call.add_to_switcher_menu", text="\"反选\"添加到Switcher", icon='PLUS').action = 'button.action_global_select_invert'
        layout.operator("call.add_to_switcher_menu", text="添加分隔符到Switcher", icon='REMOVE').action = 'SEPARATOR'

    elif op and op.bl_rna.identifier in {
        "VIEW3D_OT_select_circle",
        "GPENCIL_OT_select_circle",
        }:
        layout = self.layout
        layout.separator()
        layout.operator("call.add_to_switcher_menu", text="\"刷选\"添加到Switcher", icon='EVENT_C').action = 'button.action_global_select_circle'
        layout.operator("call.add_to_switcher_menu", text="添加分隔符到Switcher", icon='REMOVE').action = 'SEPARATOR'

    elif op and op.bl_rna.identifier == "OBJECT_OT_select_by_type":
        layout = self.layout
        layout.separator()
        layout.operator("call.add_to_switcher_menu", text="\"按类型全选(菜单)\"添加到Switcher", icon='PRESET').action = 'button.action_call_select_select_by_type_menu'
        layout.operator("call.add_to_switcher_menu", text="添加分隔符到Switcher", icon='REMOVE').action = 'SEPARATOR'

    elif op and op.bl_rna.identifier == "OBJECT_OT_select_camera":
        layout = self.layout
        layout.separator()
        layout.operator("call.add_to_switcher_menu", text="\"选择活动摄像机\"添加到Switcher", icon='OUTLINER_OB_CAMERA').action = 'object.select_camera'
        layout.operator("call.add_to_switcher_menu", text="添加分隔符到Switcher", icon='REMOVE').action = 'SEPARATOR'

    elif op and op.bl_rna.identifier in {
        "OBJECT_OT_select_mirror",
        "LATTICE_OT_select_mirror",
        "MESH_OT_select_mirror",
        "ARMATURE_OT_select_mirror",
        "POSE_OT_select_mirror",
        }:
        layout = self.layout
        layout.separator()
        layout.operator("call.add_to_switcher_menu", text="\"选择镜像\"添加到Switcher", icon='MOD_MIRROR').action = 'button.action_select_select_mirror'
        layout.operator("call.add_to_switcher_menu", text="添加分隔符到Switcher", icon='REMOVE').action = 'SEPARATOR'

    elif op and op.bl_rna.identifier in {
        "OBJECT_OT_select_random",
        "MESH_OT_select_random",
        "CURVE_OT_select_random",
        "MBALL_OT_select_random_metaelems",
        "GPENCIL_OT_select_random",
        "GREASE_PENCIL_OT_select_random",
        "LATTICE_OT_select_random",
        }:
        layout = self.layout
        layout.separator()
        layout.operator("call.add_to_switcher_menu", text="\"随机选择\"添加到Switcher", icon='RADIOBUT_OFF').action = 'button.action_select_select_random'
        layout.operator("call.add_to_switcher_menu", text="添加分隔符到Switcher", icon='REMOVE').action = 'SEPARATOR'

    elif op and op.bl_rna.identifier in {
        "CURVE_OT_select_more",
        "CURVE_OT_select_less",
        "CURVE_OT_select_next",
        "CURVE_OT_select_previous",
        "GPENCIL_OT_select_more",
        "GPENCIL_OT_select_less",
        "GREASE_PENCIL_OT_select_more",
        "GREASE_PENCIL_OT_select_less",
        "ARMATURE_OT_select_more",
        "ARMATURE_OT_select_less",
        "LATTICE_OT_select_more",
        "LATTICE_OT_select_less",
        }:
        layout = self.layout
        layout.separator()
        layout.operator("call.add_to_switcher_menu", text="\"加选/减选(菜单)\"添加到Switcher", icon='FORCE_CHARGE').action = 'button.action_call_object_select_more_or_less_menu'
        layout.operator("call.add_to_switcher_menu", text="添加分隔符到Switcher", icon='REMOVE').action = 'SEPARATOR'

    elif op and op.bl_rna.identifier == "ARMATURE_OT_select_hierarchy":
        layout = self.layout
        layout.separator()
        layout.operator("call.add_to_switcher_menu", text="\"父级/子级(菜单)\"添加到Switcher", icon='ORIENTATION_PARENT').action = 'button.action_object_select_hierarchy_parent_child'
        layout.operator("call.add_to_switcher_menu", text="添加分隔符到Switcher", icon='REMOVE').action = 'SEPARATOR'

    elif op and op.bl_rna.identifier in {
        "GPENCIL_OT_select_grouped",
        "POSE_OT_select_grouped",
        "OBJECT_OT_select_grouped",
        }:
        layout = self.layout
        layout.separator()
        layout.operator("call.add_to_switcher_menu", text="\"按组选择(菜单)\"添加到Switcher", icon='PRESET').action = 'button.action_select_select_grouped'
        layout.operator("call.add_to_switcher_menu", text="添加分隔符到Switcher", icon='REMOVE').action = 'SEPARATOR'

    elif op and op.bl_rna.identifier in {
        "OBJECT_OT_select_linked",
        "GREASE_PENCIL_OT_select_linked",
        "GPENCIL_OT_select_linked",
        "CURVE_OT_select_linked",
        "ARMATURE_OT_select_linked",
        "POSE_OT_select_linked"
        }:
        layout = self.layout
        layout.separator()
        layout.operator("call.add_to_switcher_menu", text="\"选择相连(菜单)\"添加到Switcher", icon='LINK_BLEND').action = 'button.action_select_select_linked'
        layout.operator("call.add_to_switcher_menu", text="添加分隔符到Switcher", icon='REMOVE').action = 'SEPARATOR'

    elif op and op.bl_rna.identifier == "OBJECT_OT_select_pattern":
        layout = self.layout
        layout.separator()
        layout.operator("call.add_to_switcher_menu", text="\"按名称选择\"添加到Switcher", icon='PLUS').action = 'button.action_object_select_pattern'
        layout.operator("call.add_to_switcher_menu", text="添加分隔符到Switcher", icon='REMOVE').action = 'SEPARATOR'

    elif op and op.bl_rna.identifier == "MESH_OT_select_nth":
        layout = self.layout
        layout.separator()
        layout.operator("call.add_to_switcher_menu", text="\"间隔式弃选\"添加到Switcher", icon='PLUS').action = 'button.action_mesh_select_nth'
        layout.operator("call.add_to_switcher_menu", text="添加分隔符到Switcher", icon='REMOVE').action = 'SEPARATOR'

    elif op and op.bl_rna.identifier == "MESH_OT_edges_select_sharp":
        layout = self.layout
        layout.separator()
        layout.operator("call.add_to_switcher_menu", text="\"选择锐边\"添加到Switcher", icon='PLUS').action = 'button.action_mesh_edges_select_sharp'
        layout.operator("call.add_to_switcher_menu", text="添加分隔符到Switcher", icon='REMOVE').action = 'SEPARATOR'

    elif op and op.bl_rna.identifier in {
        "CURVE_OT_select_similar",
        "ARMATURE_OT_select_similar",
        "MBALL_OT_select_similar"
        }:
        layout = self.layout
        layout.separator()
        layout.operator("call.add_to_switcher_menu", text="\"选择相似(菜单)\"添加到Switcher", icon='PRESET').action = 'button.action_select_select_similar'
        layout.operator("call.add_to_switcher_menu", text="添加分隔符到Switcher", icon='REMOVE').action = 'SEPARATOR'



def global_select_object_moreless_menu_to_switcher(self, context):
    show_switcher = bpy.context.preferences.addons[__package__].preferences.to_show_to_switcher
    if not show_switcher:
        return
    self.layout.separator()
    self.layout.operator("call.add_to_switcher_menu", text="\"加选/减选(菜单)\"添加到Switcher", icon='FORCE_CHARGE').action = 'button.action_call_object_select_more_or_less_menu'
    self.layout.operator("call.add_to_switcher_menu", text="\"父级/子级(菜单)\"添加到Switcher", icon='ORIENTATION_PARENT').action = 'button.action_object_select_hierarchy_parent_child'
    self.layout.operator("call.add_to_switcher_menu", text="添加分隔符到Switcher", icon='REMOVE').action = 'SEPARATOR'

def global_select_pose_moreless_menu_to_switcher(self, context):
    show_switcher = bpy.context.preferences.addons[__package__].preferences.to_show_to_switcher
    if not show_switcher:
        return
    self.layout.separator()
    self.layout.operator("call.add_to_switcher_menu", text="\"父级/子级(菜单)\"添加到Switcher", icon='ORIENTATION_PARENT').action = 'button.action_object_select_hierarchy_parent_child'
    self.layout.operator("call.add_to_switcher_menu", text="添加分隔符到Switcher", icon='REMOVE').action = 'SEPARATOR'

def global_select_meshedit_moreless_menu_to_switcher(self, context):
    show_switcher = bpy.context.preferences.addons[__package__].preferences.to_show_to_switcher
    if not show_switcher:
        return
    self.layout.separator()
    self.layout.operator("call.add_to_switcher_menu", text="\"加选/减选(菜单)\"添加到Switcher", icon='FORCE_CHARGE').action = 'button.action_call_object_select_more_or_less_menu'
    self.layout.operator("call.add_to_switcher_menu", text="添加分隔符到Switcher", icon='REMOVE').action = 'SEPARATOR'

def global_select_meshedit_select_linked_menu_to_switcher(self, context):
    show_switcher = bpy.context.preferences.addons[__package__].preferences.to_show_to_switcher
    if not show_switcher:
        return
    self.layout.separator()
    self.layout.operator("call.add_to_switcher_menu", text="\"选择相连(菜单)\"添加到Switcher", icon='LINK_BLEND').action = 'button.action_select_select_linked'
    self.layout.operator("call.add_to_switcher_menu", text="添加分隔符到Switcher", icon='REMOVE').action = 'SEPARATOR'

def global_select_select_similar_menu_to_switcher(self, context):
    show_switcher = bpy.context.preferences.addons[__package__].preferences.to_show_to_switcher
    if not show_switcher:
        return
    self.layout.separator()
    self.layout.operator("call.add_to_switcher_menu", text="\"选择相似(菜单)\"添加到Switcher", icon='PRESET').action = 'button.action_select_select_similar'
    self.layout.operator("call.add_to_switcher_menu", text="添加分隔符到Switcher", icon='REMOVE').action = 'SEPARATOR'

def global_select_mesh_select_by_trait_menu_to_switcher(self, context):
    show_switcher = bpy.context.preferences.addons[__package__].preferences.to_show_to_switcher
    if not show_switcher:
        return
    self.layout.separator()
    self.layout.operator("call.add_to_switcher_menu", text="\"按特征全选(菜单)\"添加到Switcher", icon='PRESET').action = 'button.action_mesh_call_select_by_trait'
    self.layout.operator("call.add_to_switcher_menu", text="添加分隔符到Switcher", icon='REMOVE').action = 'SEPARATOR'

def global_select_mesh_select_loops_menu_to_switcher(self, context):
    show_switcher = bpy.context.preferences.addons[__package__].preferences.to_show_to_switcher
    if not show_switcher:
        return
    self.layout.separator()
    self.layout.operator("call.add_to_switcher_menu", text="\"选择循环(菜单)\"添加到Switcher", icon='PRESET').action = 'button.action_call_mesh_select_loops'
    self.layout.operator("call.add_to_switcher_menu", text="添加分隔符到Switcher", icon='REMOVE').action = 'SEPARATOR'



def register():
    bpy.types.UI_MT_button_context_menu.append(draw_add_to_switcher_global_select)
    bpy.types.VIEW3D_MT_select_object_more_less.append(global_select_object_moreless_menu_to_switcher)
    bpy.types.VIEW3D_MT_select_pose_more_less.append(global_select_pose_moreless_menu_to_switcher)
    bpy.types.VIEW3D_MT_edit_mesh_select_more_less.append(global_select_meshedit_moreless_menu_to_switcher)
    bpy.types.VIEW3D_MT_edit_mesh_select_linked.append(global_select_meshedit_select_linked_menu_to_switcher)
    bpy.types.VIEW3D_MT_edit_mesh_select_similar.append(global_select_select_similar_menu_to_switcher)
    bpy.types.VIEW3D_MT_edit_mesh_select_by_trait.append(global_select_mesh_select_by_trait_menu_to_switcher)
    bpy.types.VIEW3D_MT_edit_mesh_select_loops.append(global_select_mesh_select_loops_menu_to_switcher)


def unregister():
    bpy.types.VIEW3D_MT_edit_mesh_select_loops.remove(global_select_mesh_select_loops_menu_to_switcher)
    bpy.types.VIEW3D_MT_edit_mesh_select_by_trait.remove(global_select_mesh_select_by_trait_menu_to_switcher)
    bpy.types.VIEW3D_MT_edit_mesh_select_similar.remove(global_select_select_similar_menu_to_switcher)
    bpy.types.VIEW3D_MT_edit_mesh_select_linked.remove(global_select_meshedit_select_linked_menu_to_switcher)
    bpy.types.VIEW3D_MT_edit_mesh_select_more_less.remove(global_select_meshedit_moreless_menu_to_switcher)
    bpy.types.VIEW3D_MT_select_pose_more_less.remove(global_select_pose_moreless_menu_to_switcher)
    bpy.types.VIEW3D_MT_select_object_more_less.remove(global_select_object_moreless_menu_to_switcher)
    bpy.types.UI_MT_button_context_menu.remove(draw_add_to_switcher_global_select)
