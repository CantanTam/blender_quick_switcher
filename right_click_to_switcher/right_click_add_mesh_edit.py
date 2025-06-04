import bpy
from .. import ADDON_NAME

def draw_add_to_switcher_meshedit(self, context):

    show_switcher = bpy.context.preferences.addons[ADDON_NAME].preferences.to_show_to_switcher
    if not show_switcher:
        return
    
    op = getattr(context, "operator", None) or getattr(context, "button_operator", None)

    if op and op.bl_rna.identifier == "MESH_OT_select_nth":
        layout = self.layout
        layout.separator()
        layout.operator("call.add_to_switcher_menu", text="\"间隔式弃选\"⟶Switcher", icon='PLUS').action = 'button.action_mesh_select_nth'

    elif op and op.bl_rna.identifier == "MESH_OT_edges_select_sharp":
        layout = self.layout
        layout.separator()
        layout.operator("call.add_to_switcher_menu", text="\"选择锐边\"⟶Switcher", icon='PLUS').action = 'button.action_mesh_edges_select_sharp'

    elif op and op.bl_rna.identifier == "MESH_OT_select_axis":
        layout = self.layout
        layout.separator()
        layout.operator("call.add_to_switcher_menu", text="\"活动项的同侧\"⟶Switcher", icon='RADIOBUT_OFF').action = 'button.action_mesh_select_axis'

    elif op and op.bl_rna.identifier == "TRANSFORM_OT_shrink_fatten":
        layout = self.layout
        layout.separator()
        layout.operator("call.add_to_switcher_menu", text="\"法向缩放\"⟶Switcher", icon='PLUS').action = 'button.action_meshedit_transform_shrink_fatten'

    elif op and op.bl_rna.identifier == "TRANSFORM_OT_skin_resize":
        layout = self.layout
        layout.separator()
        layout.operator("call.add_to_switcher_menu", text="\"重置蒙皮尺寸\"⟶Switcher", icon='PLUS').action = 'button.action_meshedit_transform_skin_resize'

    elif op and op.bl_rna.identifier == "MESH_OT_separate":
        layout = self.layout
        layout.separator()
        layout.operator("call.add_to_switcher_menu", text="\"分离\"⟶Switcher", icon='PRESET').action = 'button.action_meshedit_mesh_separate'

    elif op and op.bl_rna.identifier == "MESH_OT_bisect":
        layout = self.layout
        layout.separator()
        layout.operator("call.add_to_switcher_menu", text="\"切分\"⟶Switcher", icon='PLUS').action = 'button.action_meshedit_mesh_bisect'

    elif op and op.bl_rna.identifier == "MESH_OT_knife_project":
        layout = self.layout
        layout.separator()
        layout.operator("call.add_to_switcher_menu", text="\"投影切割\"⟶Switcher", icon='PLUS').action = 'button.action_meshedit_mesh_knife_project'

    elif op and op.bl_rna.identifier == "MESH_OT_knife_tool":
        layout = self.layout
        layout.separator()
        layout.operator("call.add_to_switcher_menu", text="\"裁刀拓扑工具\"⟶Switcher", icon='PLUS').action = 'button.action_meshedit_mesh_knife_tool'

    elif op and op.bl_rna.identifier == "MESH_OT_convex_hull":
        layout = self.layout
        layout.separator()
        layout.operator("call.add_to_switcher_menu", text="\"凸壳\"⟶Switcher", icon='PLUS').action = 'button.action_meshedit_mesh_convex_hull'

    elif op and op.bl_rna.identifier == "MESH_OT_symmetrize":
        layout = self.layout
        layout.separator()
        layout.operator("call.add_to_switcher_menu", text="\"对称\"⟶Switcher", icon='PLUS').action = 'button.action_meshedit_mesh_symmetrize'

    elif op and op.bl_rna.identifier == "MESH_OT_symmetry_snap":
        layout = self.layout
        layout.separator()
        layout.operator("call.add_to_switcher_menu", text="\"吸附到对称结构\"⟶Switcher", icon='PLUS').action = 'button.action_meshedit_mesh_symmetry_snap'

    elif op and op.bl_rna.identifier == "MESH_OT_flip_normals":
        layout = self.layout
        layout.separator()
        layout.operator("call.add_to_switcher_menu", text="\"翻转法向\"⟶Switcher", icon='PLUS').action = 'button.action_meshedit_flip_normals'

    elif op and op.bl_rna.identifier == "MESH_OT_normals_make_consistent":
        layout = self.layout
        layout.separator()
        layout.operator("call.add_to_switcher_menu", text="\"重新计算外/内侧\"⟶Switcher", icon='PLUS').action = 'button.action_meshedit_normals_make_consistent'

    elif op and op.bl_rna.identifier == "MESH_OT_set_normals_from_faces":
        layout = self.layout
        layout.separator()
        layout.operator("call.add_to_switcher_menu", text="\"从面设置法向\"⟶Switcher", icon='PLUS').action = 'button.action_meshedit_set_normals_from_faces'

    elif op and op.bl_rna.identifier == "TRANSFORM_OT_rotate_normal":
        layout = self.layout
        layout.separator()
        layout.operator("call.add_to_switcher_menu", text="\"旋转法向\"⟶Switcher", icon='PLUS').action = 'button.action_meshedit_transform_rotate_normal'

    elif op and op.bl_rna.identifier == "MESH_OT_point_normals":
        layout = self.layout
        layout.separator()
        layout.operator("call.add_to_switcher_menu", text="\"法向指向目标体\"⟶Switcher", icon='PLUS').action = 'button.action_meshedit_point_normals'

    elif op and op.bl_rna.identifier == "MESH_OT_merge_normals":
        layout = self.layout
        layout.separator()
        layout.operator("call.add_to_switcher_menu", text="\"合并法向\"⟶Switcher", icon='PLUS').action = 'button.action_meshedit_merge_normals'

    elif op and op.bl_rna.identifier == "MESH_OT_split_normals":
        layout = self.layout
        layout.separator()
        layout.operator("call.add_to_switcher_menu", text="\"拆分法向\"⟶Switcher", icon='PLUS').action = 'button.action_meshedit_split_normals'

    elif op and op.bl_rna.identifier == "MESH_OT_attribute_set":
        layout = self.layout
        layout.separator()
        layout.operator("call.add_to_switcher_menu", text="\"设置属性\"⟶Switcher", icon='PLUS').action = 'button.action_meshedit_attribute_set'

    elif op and op.bl_rna.identifier == "MESH_OT_sort_elements":
        layout = self.layout
        layout.separator()
        layout.operator("call.add_to_switcher_menu", text="\"网格元素排序(菜单)\"⟶Switcher", icon='PRESET').action = 'button.action_meshedit_sort_elements'

    elif op and op.bl_rna.identifier == "MESH_OT_extrude_vertices_move":
        layout = self.layout
        layout.separator()
        layout.operator("call.add_to_switcher_menu", text="\"挤出顶点\"⟶Switcher", icon='VERTEXSEL').action = 'button.action_meshedit_extrude_vertices_move'

    elif op and op.bl_rna.identifier == "MESH_OT_bevel":
        layout = self.layout
        layout.separator()
        layout.operator("call.add_to_switcher_menu", text="\"点倒角\"⟶Switcher", icon='MOD_BEVEL').action = 'button.action_meshedit_bevel_vertices'
        layout.operator("call.add_to_switcher_menu", text="\"边倒角\"⟶Switcher", icon='MOD_BEVEL').action = 'button.action_meshedit_bevel_edges'










def meshedit_mesh_select_by_trait_menu_to_switcher(self, context):
    show_switcher = bpy.context.preferences.addons[ADDON_NAME].preferences.to_show_to_switcher
    if not show_switcher:
        return
    self.layout.separator()
    self.layout.operator("call.add_to_switcher_menu", text="\"按特征全选(菜单)\"⟶Switcher", icon='PRESET').action = 'button.action_mesh_call_select_by_trait'

def meshedit_select_more_or_less_menu_to_switcher(self, context):
    show_switcher = bpy.context.preferences.addons[ADDON_NAME].preferences.to_show_to_switcher
    if not show_switcher:
        return
    self.layout.separator()
    self.layout.operator("call.add_to_switcher_menu", text="\"加选/减选(菜单)\"⟶Switcher", icon='FORCE_CHARGE').action = 'button.action_call_global_select_more_or_less_menu'

def meshedit_select_mesh_select_loops_menu_to_switcher(self, context):
    show_switcher = bpy.context.preferences.addons[ADDON_NAME].preferences.to_show_to_switcher
    if not show_switcher:
        return
    self.layout.separator()
    self.layout.operator("call.add_to_switcher_menu", text="\"选择循环(菜单)\"⟶Switcher", icon='PRESET').action = 'button.action_call_mesh_select_loops'

def meshedit_select_linked_menu_to_switcher(self, context):
    show_switcher = bpy.context.preferences.addons[ADDON_NAME].preferences.to_show_to_switcher
    if not show_switcher:
        return
    self.layout.separator()
    self.layout.operator("call.add_to_switcher_menu", text="\"选择相连(菜单)\"⟶Switcher", icon='LINK_BLEND').action = 'button.action_global_select_select_linked'

def meshedit_edit_mesh_extrude_menu_to_switcher(self, context):
    show_switcher = bpy.context.preferences.addons[ADDON_NAME].preferences.to_show_to_switcher
    if not show_switcher:
        return
    self.layout.separator()
    self.layout.operator("call.add_to_switcher_menu", text="\"挤出(菜单)\"⟶Switcher", icon='PRESET').action = 'button.action_meshedit_edit_mesh_extrude_menu'

def meshedit_edit_mesh_merge_menu_to_switcher(self, context):
    show_switcher = bpy.context.preferences.addons[ADDON_NAME].preferences.to_show_to_switcher
    if not show_switcher:
        return
    self.layout.separator()
    self.layout.operator("call.add_to_switcher_menu", text="\"合并(菜单)\"⟶Switcher", icon='PRESET').action = 'button.action_meshedit_edit_mesh_merge_menu'

def meshedit_edit_mesh_split_menu_to_switcher(self, context):
    show_switcher = bpy.context.preferences.addons[ADDON_NAME].preferences.to_show_to_switcher
    if not show_switcher:
        return
    self.layout.separator()
    self.layout.operator("call.add_to_switcher_menu", text="\"拆分(菜单)\"⟶Switcher", icon='PRESET').action = 'button.action_meshedit_edit_mesh_split_menu'

def meshedit_edit_mesh_normals_menu_to_switcher(self, context):
    show_switcher = bpy.context.preferences.addons[ADDON_NAME].preferences.to_show_to_switcher
    if not show_switcher:
        return
    self.layout.separator()
    self.layout.operator("call.add_to_switcher_menu", text="\"法向(菜单)\"⟶Switcher", icon='PRESET').action = 'button.action_meshedit_edit_mesh_normals_menu'

def meshedit_edit_mesh_normals_average_menu_to_switcher(self, context):
    show_switcher = bpy.context.preferences.addons[ADDON_NAME].preferences.to_show_to_switcher
    if not show_switcher:
        return
    self.layout.separator()
    self.layout.operator("call.add_to_switcher_menu", text="\"平均法向(菜单)\"⟶Switcher", icon='PRESET').action = 'button.action_meshedit_edit_mesh_normals_average'

def meshedit_edit_mesh_shading_menu_to_switcher(self, context):
    show_switcher = bpy.context.preferences.addons[ADDON_NAME].preferences.to_show_to_switcher
    if not show_switcher:
        return
    self.layout.separator()
    self.layout.operator("call.add_to_switcher_menu", text="\"着色方式(菜单)\"⟶Switcher", icon='PRESET').action = 'button.action_meshedit_edit_mesh_shading'

def meshedit_edit_mesh_weights_menu_to_switcher(self, context):
    show_switcher = bpy.context.preferences.addons[ADDON_NAME].preferences.to_show_to_switcher
    if not show_switcher:
        return
    self.layout.separator()
    self.layout.operator("call.add_to_switcher_menu", text="\"权重(菜单)\"⟶Switcher", icon='PRESET').action = 'button.action_meshedit_edit_mesh_weights'

def meshedit_edit_mesh_clean_menu_to_switcher(self, context):
    show_switcher = bpy.context.preferences.addons[ADDON_NAME].preferences.to_show_to_switcher
    if not show_switcher:
        return
    self.layout.separator()
    self.layout.operator("call.add_to_switcher_menu", text="\"清理(菜单)\"⟶Switcher", icon='PRESET').action = 'button.action_meshedit_edit_mesh_clean'














def register():
    bpy.types.UI_MT_button_context_menu.append(draw_add_to_switcher_meshedit)
    bpy.types.VIEW3D_MT_edit_mesh_select_by_trait.append(meshedit_mesh_select_by_trait_menu_to_switcher)
    bpy.types.VIEW3D_MT_edit_mesh_select_more_less.append(meshedit_select_more_or_less_menu_to_switcher)
    bpy.types.VIEW3D_MT_edit_mesh_select_loops.append(meshedit_select_mesh_select_loops_menu_to_switcher)
    bpy.types.VIEW3D_MT_edit_mesh_select_linked.append(meshedit_select_linked_menu_to_switcher)
    bpy.types.VIEW3D_MT_edit_mesh_extrude.append(meshedit_edit_mesh_extrude_menu_to_switcher)
    bpy.types.VIEW3D_MT_edit_mesh_merge.append(meshedit_edit_mesh_merge_menu_to_switcher)
    bpy.types.VIEW3D_MT_edit_mesh_split.append(meshedit_edit_mesh_split_menu_to_switcher)
    bpy.types.VIEW3D_MT_edit_mesh_normals.append(meshedit_edit_mesh_normals_menu_to_switcher)
    bpy.types.VIEW3D_MT_edit_mesh_normals_average.append(meshedit_edit_mesh_normals_average_menu_to_switcher)
    bpy.types.VIEW3D_MT_edit_mesh_shading.append(meshedit_edit_mesh_shading_menu_to_switcher)
    bpy.types.VIEW3D_MT_edit_mesh_weights.append(meshedit_edit_mesh_weights_menu_to_switcher)
    bpy.types.VIEW3D_MT_edit_mesh_clean.append(meshedit_edit_mesh_clean_menu_to_switcher)

def unregister():
    bpy.types.VIEW3D_MT_edit_mesh_clean.remove(meshedit_edit_mesh_clean_menu_to_switcher)
    bpy.types.VIEW3D_MT_edit_mesh_weights.remove(meshedit_edit_mesh_weights_menu_to_switcher)
    bpy.types.VIEW3D_MT_edit_mesh_shading.remove(meshedit_edit_mesh_shading_menu_to_switcher)
    bpy.types.VIEW3D_MT_edit_mesh_normals_average.remove(meshedit_edit_mesh_normals_average_menu_to_switcher)
    bpy.types.VIEW3D_MT_edit_mesh_normals.remove(meshedit_edit_mesh_normals_menu_to_switcher)
    bpy.types.VIEW3D_MT_edit_mesh_split.remove(meshedit_edit_mesh_split_menu_to_switcher)
    bpy.types.VIEW3D_MT_edit_mesh_merge.remove(meshedit_edit_mesh_merge_menu_to_switcher)
    bpy.types.VIEW3D_MT_edit_mesh_extrude.remove(meshedit_edit_mesh_extrude_menu_to_switcher)
    bpy.types.VIEW3D_MT_edit_mesh_select_linked.remove(meshedit_select_linked_menu_to_switcher)
    bpy.types.VIEW3D_MT_edit_mesh_select_loops.remove(meshedit_select_mesh_select_loops_menu_to_switcher)
    bpy.types.VIEW3D_MT_edit_mesh_select_more_less.remove(meshedit_select_more_or_less_menu_to_switcher)
    bpy.types.VIEW3D_MT_edit_mesh_select_by_trait.remove(meshedit_mesh_select_by_trait_menu_to_switcher)
    bpy.types.UI_MT_button_context_menu.remove(draw_add_to_switcher_meshedit)