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

    elif op and op.bl_rna.identifier == "MESH_OT_edge_face_add":
        layout = self.layout
        layout.separator()
        layout.operator("call.add_to_switcher_menu", text="\"从顶点创建边/面\"⟶Switcher", icon='PLUS').action = 'button.action_meshedit_edge_face_add'

    elif op and op.bl_rna.identifier == "MESH_OT_vert_connect_path":
        layout = self.layout
        layout.separator()
        layout.operator("call.add_to_switcher_menu", text="\"连接顶点路径\"⟶Switcher", icon='PLUS').action = 'button.action_meshedit_vert_connect_path'

    elif op and op.bl_rna.identifier == "MESH_OT_vert_connect":
        layout = self.layout
        layout.separator()
        layout.operator("call.add_to_switcher_menu", text="\"连接顶点对\"⟶Switcher", icon='PLUS').action = 'button.action_meshedit_vert_connect'

    elif op and op.bl_rna.identifier == "MESH_OT_rip_move":
        layout = self.layout
        layout.separator()
        layout.operator("call.add_to_switcher_menu", text="\"断离顶点\"⟶Switcher", icon='PLUS').action = 'button.action_meshedit_rip_move'
        layout.operator("call.add_to_switcher_menu", text="\"断离顶点并填充\"⟶Switcher", icon='PLUS').action = 'button.action_meshedit_rip_move_fill'

    elif op and op.bl_rna.identifier == "MESH_OT_rip_edge_move":
        layout = self.layout
        layout.separator()
        layout.operator("call.add_to_switcher_menu", text="\"断离顶点并延长\"⟶Switcher", icon='PLUS').action = 'button.action_meshedit_rip_edge_move'

    elif op and op.bl_rna.identifier == "TRANSFORM_OT_vert_slide":
        layout = self.layout
        layout.separator()
        layout.operator("call.add_to_switcher_menu", text="\"滑移顶点\"⟶Switcher", icon='PLUS').action = 'button.action_meshedit_transform_vert_slide'

    elif op and op.bl_rna.identifier == "MESH_OT_vertices_smooth":
        layout = self.layout
        layout.separator()
        layout.operator("call.add_to_switcher_menu", text="\"平滑顶点\"⟶Switcher", icon='PLUS').action = 'button.action_meshedit_vertices_smooth'

    elif op and op.bl_rna.identifier == "MESH_OT_vertices_smooth_laplacian":
        layout = self.layout
        layout.separator()
        layout.operator("call.add_to_switcher_menu", text="\"平滑顶点(拉普拉斯)\"⟶Switcher", icon='PLUS').action = 'button.action_meshedit_vertices_smooth_laplacian'

    elif op and op.bl_rna.identifier == "TRANSFORM_OT_vert_crease":
        layout = self.layout
        layout.separator()
        layout.operator("call.add_to_switcher_menu", text="\"顶点折痕\"⟶Switcher", icon='PLUS').action = 'button.action_meshedit_transform_vert_crease'

    elif op and op.bl_rna.identifier == "MESH_OT_blend_from_shape":
        layout = self.layout
        layout.separator()
        layout.operator("call.add_to_switcher_menu", text="\"从形状混合\"⟶Switcher", icon='SHAPEKEY_DATA').action = 'button.action_meshedit_blend_from_shape'

    elif op and op.bl_rna.identifier == "MESH_OT_shape_propagate_to_all":
        layout = self.layout
        layout.separator()
        layout.operator("call.add_to_switcher_menu", text="\"传递到形状\"⟶Switcher", icon='SHAPEKEY_DATA').action = 'button.action_meshedit_shape_propagate_to_all'

    elif op and op.bl_rna.identifier == "OBJECT_OT_vertex_parent_set":
        layout = self.layout
        layout.separator()
        layout.operator("call.add_to_switcher_menu", text="\"创建父级顶点\"⟶Switcher", icon='PLUS').action = 'button.action_meshedit_vertex_parent_set'

    elif op and op.bl_rna.identifier == "MESH_OT_extrude_edges_move":
        layout = self.layout
        layout.separator()
        layout.operator("call.add_to_switcher_menu", text="\"挤出边线\"⟶Switcher", icon='EDGESEL').action = 'button.action_meshedit_extrude_edges_move'

    elif op and op.bl_rna.identifier == "MESH_OT_bridge_edge_loops":
        layout = self.layout
        layout.separator()
        layout.operator("call.add_to_switcher_menu", text="\"桥接循环边\"⟶Switcher", icon='PLUS').action = 'button.action_meshedit_bridge_edge_loops'

    elif op and op.bl_rna.identifier == "MESH_OT_subdivide_edgering":
        layout = self.layout
        layout.separator()
        layout.operator("call.add_to_switcher_menu", text="\"细分并排边\"⟶Switcher", icon='PLUS').action = 'button.action_meshedit_subdivide_edgering'

    elif op and op.bl_rna.identifier == "MESH_OT_unsubdivide":
        layout = self.layout
        layout.separator()
        layout.operator("call.add_to_switcher_menu", text="\"反细分\"⟶Switcher", icon='PLUS').action = 'button.action_meshedit_unsubdivide'

    elif op and op.bl_rna.identifier == "MESH_OT_edge_rotate":
        layout = self.layout
        layout.separator()
        layout.operator("call.add_to_switcher_menu", text="\"顺/逆时针旋转边\"⟶Switcher", icon='PLUS').action = 'button.action_meshedit_edge_rotate'

    elif op and op.bl_rna.identifier == "TRANSFORM_OT_edge_slide":
        layout = self.layout
        layout.separator()
        layout.operator("call.add_to_switcher_menu", text="\"滑移边线\"⟶Switcher", icon='PLUS').action = 'button.action_meshedit_transform_edge_slide'

    elif op and op.bl_rna.identifier == "MESH_OT_loopcut_slide":
        layout = self.layout
        layout.separator()
        layout.operator("call.add_to_switcher_menu", text="\"环切并滑移\"⟶Switcher", icon='PLUS').action = 'button.action_meshedit_loopcut_slide'

    elif op and op.bl_rna.identifier == "MESH_OT_offset_edge_loops_slide":
        layout = self.layout
        layout.separator()
        layout.operator("call.add_to_switcher_menu", text="\"偏移边线并滑移\"⟶Switcher", icon='PLUS').action = 'button.action_meshedit_offset_edge_loops_slide'

    elif op and op.bl_rna.identifier == "TRANSFORM_OT_edge_crease":
        layout = self.layout
        layout.separator()
        layout.operator("call.add_to_switcher_menu", text="\"边线折痕\"⟶Switcher", icon='PLUS').action = 'button.action_meshedit_transform_edge_crease'

    elif op and op.bl_rna.identifier == "TRANSFORM_OT_edge_bevelweight":
        layout = self.layout
        layout.separator()
        layout.operator("call.add_to_switcher_menu", text="\"倒角边权重\"⟶Switcher", icon='PLUS').action = 'button.action_meshedit_transform_edge_bevelweight'

    elif op and op.bl_rna.identifier == "MESH_OT_mark_seam":
        layout = self.layout
        layout.separator()
        layout.operator("call.add_to_switcher_menu", text="\"缝合边\"⟶Switcher", icon='PLUS').action = 'button.action_meshedit_mesh_mark_seam_toggle'

    elif op and op.bl_rna.identifier == "MESH_OT_mark_sharp":
        layout = self.layout
        layout.separator()
        layout.operator("call.add_to_switcher_menu", text="\"锐边\"⟶Switcher", icon='PLUS').action = 'button.action_meshedit_mesh_mark_sharp_toggle'

    elif op and op.bl_rna.identifier == "MESH_OT_set_sharpness_by_angle":
        layout = self.layout
        layout.separator()
        layout.operator("call.add_to_switcher_menu", text="\"按角度设置锐边\"⟶Switcher", icon='PLUS').action = 'button.action_meshedit_mesh_set_sharpness_by_angle'

    elif op and op.bl_rna.identifier == "MESH_OT_mark_freestyle_edge":
        layout = self.layout
        layout.separator()
        layout.operator("call.add_to_switcher_menu", text="\"标记Freestyle边\"⟶Switcher", icon='PLUS').action = 'button.action_meshedit_mesh_mark_freestyle_edge_clear_false'
        layout.operator("call.add_to_switcher_menu", text="\"清除Freestyle边\"⟶Switcher", icon='PLUS').action = 'button.action_meshedit_mesh_mark_freestyle_edge_clear_true'







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

def meshedit_vertex_group_menu_to_switcher(self, context):
    show_switcher = bpy.context.preferences.addons[ADDON_NAME].preferences.to_show_to_switcher
    if not show_switcher:
        return
    self.layout.separator()
    self.layout.operator("call.add_to_switcher_menu", text="\"顶点组(菜单)\"⟶Switcher", icon='GROUP_VERTEX').action = 'button.action_meshedit_vertex_group_menu'

def meshedit_hook_menu_to_switcher(self, context):
    show_switcher = bpy.context.preferences.addons[ADDON_NAME].preferences.to_show_to_switcher
    if not show_switcher:
        return
    self.layout.separator()
    self.layout.operator("call.add_to_switcher_menu", text="\"钩挂(菜单)\"⟶Switcher", icon='PRESET').action = 'button.action_meshedit_hook_menu'














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
    bpy.types.VIEW3D_MT_vertex_group.append(meshedit_vertex_group_menu_to_switcher)
    bpy.types.VIEW3D_MT_hook.append(meshedit_hook_menu_to_switcher)

def unregister():
    bpy.types.VIEW3D_MT_hook.remove(meshedit_hook_menu_to_switcher)
    bpy.types.VIEW3D_MT_vertex_group.remove(meshedit_vertex_group_menu_to_switcher)
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