import bpy
from .. import ADDON_NAME

def draw_add_to_switcher_gpenciledit(self, context):

    show_switcher = bpy.context.preferences.addons[ADDON_NAME].preferences.to_show_to_switcher
    if not show_switcher:
        return
    
    op = getattr(context, "operator", None) or getattr(context, "button_operator", None)

    if op and op.bl_rna.identifier == "GPENCIL_OT_layer_add":
        layout = self.layout
        layout.separator()
        layout.operator("call.add_to_switcher_menu", text="\"新建层\"⟶Switcher", icon='ADD').action = 'action.gpenciledit_layer_add'

    elif op and op.bl_rna.identifier == "GPENCIL_OT_blank_frame_add":
        layout = self.layout
        layout.separator()
        layout.operator("call.add_to_switcher_menu", text="\"在活动层播入空白帧\"⟶Switcher", icon='PLUS').action = 'action.gpenciledit_blank_frame_add_false'
        layout.operator("call.add_to_switcher_menu", text="\"在全部层插入空白帧\"⟶Switcher", icon='PLUS').action = 'action.gpenciledit_blank_frame_add_true'

    elif op and op.bl_rna.identifier == "GPENCIL_OT_frame_duplicate":
        layout = self.layout
        layout.separator()
        layout.operator("call.add_to_switcher_menu", text="\"复制活动层的活动帧\"⟶Switcher", icon='PLUS').action = 'action.gpenciledit_frame_duplicate_active'
        layout.operator("call.add_to_switcher_menu", text="\"复制全部层的活动帧\"⟶Switcher", icon='PLUS').action = 'action.gpenciledit_frame_duplicate_all'

    elif op and op.bl_rna.identifier == "GPENCIL_OT_interpolate_sequence":
        layout = self.layout
        layout.separator()
        layout.operator("call.add_to_switcher_menu", text="\"插值顺序\"⟶Switcher", icon='PLUS').action = 'action.gpenciledit_interpolate_sequence_modal'

    elif op and op.bl_rna.identifier == "GPENCIL_OT_stroke_separate":
        layout = self.layout
        layout.separator()
        layout.operator("call.add_to_switcher_menu", text="\"分离(菜单)\"⟶Switcher", icon='PRESET').action = 'action.call_gpenciledit_stroke_separate_menu'

    elif op and op.bl_rna.identifier == "GPENCIL_OT_stroke_split":
        layout = self.layout
        layout.separator()
        layout.operator("call.add_to_switcher_menu", text="\"拆分\"⟶Switcher", icon='PLUS').action = 'action.call_gpenciledit_stroke_split'

    elif op and op.bl_rna.identifier == "GPENCIL_OT_frame_clean_fill":
        layout = self.layout
        layout.separator()
        layout.operator("call.add_to_switcher_menu", text="\"清理边界笔画\"⟶Switcher", icon='PLUS').action = 'action.gpenciledit_frame_clean_fill_active'
        layout.operator("call.add_to_switcher_menu", text="\"清理所有帧的边界笔画\"⟶Switcher", icon='PLUS').action = 'action.gpenciledit_frame_clean_fill_all'

    elif op and op.bl_rna.identifier == "GPENCIL_OT_frame_clean_loose":
        layout = self.layout
        layout.separator()
        layout.operator("call.add_to_switcher_menu", text="\"删除松散点\"⟶Switcher", icon='PLUS').action = 'action.gpenciledit_frame_clean_loose'

    elif op and op.bl_rna.identifier == "GPENCIL_OT_stroke_merge_by_distance":
        layout = self.layout
        layout.separator()
        layout.operator("call.add_to_switcher_menu", text="\"按间距合并\"⟶Switcher", icon='PLUS').action = 'action.gpenciledit_stroke_merge_by_distance'

    elif op and op.bl_rna.identifier == "GPENCIL_OT_frame_clean_duplicate":
        layout = self.layout
        layout.separator()
        layout.operator("call.add_to_switcher_menu", text="\"清理重复帧\"⟶Switcher", icon='PLUS').action = 'action.gpenciledit_frame_clean_duplicate'

    elif op and op.bl_rna.identifier == "GPENCIL_OT_recalc_geometry":
        layout = self.layout
        layout.separator()
        layout.operator("call.add_to_switcher_menu", text="\"重新计算几何\"⟶Switcher", icon='PLUS').action = 'action.gpenciledit_recalc_geometry'

    elif op and op.bl_rna.identifier == "GPENCIL_OT_reproject":
        layout = self.layout
        layout.separator()
        layout.operator("call.add_to_switcher_menu", text="\"重投影笔画(菜单)\"⟶Switcher", icon='PRESET').action = 'action.call_gpenciledit_reproject_menu'

    elif op and op.bl_rna.identifier == "GPENCIL_OT_stroke_subdivide":
        layout = self.layout
        layout.separator()
        layout.operator("call.add_to_switcher_menu", text="\"细分笔画\"⟶Switcher", icon='PRESET').action = 'action.gpenciledit_stroke_subdivide'

    elif op and op.bl_rna.identifier == "GPENCIL_OT_stroke_trim":
        layout = self.layout
        layout.separator()
        layout.operator("call.add_to_switcher_menu", text="\"修剪笔画\"⟶Switcher", icon='PLUS').action = 'action.call_gpenciledit_stroke_trim'

    elif op and op.bl_rna.identifier == "GPENCIL_OT_stroke_outline":
        layout = self.layout
        layout.separator()
        layout.operator("call.add_to_switcher_menu", text="\"笔画轮廓\"⟶Switcher", icon='PLUS').action = 'action.gpenciledit_stroke_outline'

    elif op and op.bl_rna.identifier == "GPENCIL_OT_stroke_join":
        layout = self.layout
        layout.separator()
        layout.operator("call.add_to_switcher_menu", text="\"合并(菜单)\"⟶Switcher", icon='PRESET').action = 'action.call_gpenciledit_stroke_join_menu'
        layout.operator("call.add_to_switcher_menu", text="\"合并笔画\"⟶Switcher", icon='PLUS').action = 'action.gpenciledit_stroke_join_join'
        layout.operator("call.add_to_switcher_menu", text="\"合并&复制笔画\"⟶Switcher", icon='PLUS').action = 'action.gpenciledit_stroke_join_joincopy'

    elif op and op.bl_rna.identifier == "GPENCIL_OT_set_active_material":
        layout = self.layout
        layout.separator()
        layout.operator("call.add_to_switcher_menu", text="\"设为活动材质\"⟶Switcher", icon='PLUS').action = 'action.gpenciledit_set_active_material'

    elif op and op.bl_rna.identifier == "GPENCIL_OT_stroke_arrange":
        layout = self.layout
        layout.separator()
        layout.operator("call.add_to_switcher_menu", text="\"排列笔画(菜单)\"⟶Switcher", icon='PRESET').action = 'action.call_gpenciledit_stroke_arrange_menu'
        layout.operator("call.add_to_switcher_menu", text="\"笔画移到最前\"⟶Switcher", icon='PLUS').action = 'action.gpenciledit_stroke_arrange_top'
        layout.operator("call.add_to_switcher_menu", text="\"笔画前移\"⟶Switcher", icon='PLUS').action = 'action.gpenciledit_stroke_arrange_up'
        layout.operator("call.add_to_switcher_menu", text="\"笔画后送\"⟶Switcher", icon='PLUS').action = 'action.gpenciledit_stroke_arrange_down'
        layout.operator("call.add_to_switcher_menu", text="\"笔画移到最后\"⟶Switcher", icon='PLUS').action = 'action.gpenciledit_stroke_arrange_bottom'

    elif op and op.bl_rna.identifier == "GPENCIL_OT_stroke_cyclical_set":
        layout = self.layout
        layout.separator()
        layout.operator("call.add_to_switcher_menu", text="\"闭合笔画\"⟶Switcher", icon='PLUS').action = 'action.gpenciledit_stroke_cyclical_set'
        layout.operator("call.add_to_switcher_menu", text="\"切换笔画循环\"⟶Switcher", icon='PLUS').action = 'action.gpenciledit_stroke_cyclical_set_toggle'

    elif op and op.bl_rna.identifier == "GPENCIL_OT_stroke_caps_set":
        layout = self.layout
        layout.separator()
        layout.operator("call.add_to_switcher_menu", text="\"切换封顶类型(菜单)\"⟶Switcher", icon='PRESET').action = 'action.call_gpenciledit_stroke_caps_set_menu'

    elif op and op.bl_rna.identifier == "GPENCIL_OT_stroke_flip":
        layout = self.layout
        layout.separator()
        layout.operator("call.add_to_switcher_menu", text="\"切换笔画方向\"⟶Switcher", icon='PLUS').action = 'action.gpenciledit_stroke_flip'

    elif op and op.bl_rna.identifier == "GPENCIL_OT_stroke_start_set":
        layout = self.layout
        layout.separator()
        layout.operator("call.add_to_switcher_menu", text="\"设置笔画起始点\"⟶Switcher", icon='PLUS').action = 'action.gpenciledit_stroke_start_set'

    elif op and op.bl_rna.identifier == "GPENCIL_OT_stroke_normalize":
        layout = self.layout
        layout.separator()
        layout.operator("call.add_to_switcher_menu", text="\"规格化宽度\"⟶Switcher", icon='PLUS').action = 'action.gpenciledit_stroke_normalize_thickness'
        layout.operator("call.add_to_switcher_menu", text="\"规格化不透明度\"⟶Switcher", icon='PLUS').action = 'action.gpenciledit_stroke_normalize_opacity'

    elif op and op.bl_rna.identifier == "GPENCIL_OT_reset_transform_fill":
        layout = self.layout
        layout.separator()
        layout.operator("call.add_to_switcher_menu", text="\"重置填充变换\"⟶Switcher", icon='PLUS').action = 'action.gpenciledit_reset_transform_fill'

    elif op and op.bl_rna.identifier == "GPENCIL_OT_extrude_move":
        layout = self.layout
        layout.separator()
        layout.operator("call.add_to_switcher_menu", text="\"挤出\"⟶Switcher", icon='EVENT_E').action = 'action.gpenciledit_extrude_move'

    elif op and op.bl_rna.identifier == "GPENCIL_OT_stroke_smooth":
        layout = self.layout
        layout.separator()
        layout.operator("call.add_to_switcher_menu", text="\"光滑\"⟶Switcher", icon='PLUS').action = 'action.gpenciledit_stroke_smooth'

    elif op and op.bl_rna.identifier == "GPENCIL_OT_stroke_merge":
        layout = self.layout
        layout.separator()
        layout.operator("call.add_to_switcher_menu", text="\"合并点\"⟶Switcher", icon='PLUS').action = 'action.gpenciledit_stroke_merge'












def gpenciledit_layer_add_menu_to_switcher(self, context):
    show_switcher = bpy.context.preferences.addons[ADDON_NAME].preferences.to_show_to_switcher
    if not show_switcher:
        return
    self.layout.separator()
    self.layout.operator("call.add_to_switcher_menu", text="\"活动层(菜单)\"⟶Switcher", icon='PRESET').action = 'action.gpenciledit_layer_active_menu'

def gpenciledit_animation_menu_to_switcher(self, context):
    show_switcher = bpy.context.preferences.addons[ADDON_NAME].preferences.to_show_to_switcher
    if not show_switcher:
        return
    self.layout.separator()
    self.layout.operator("call.add_to_switcher_menu", text="\"动画(菜单)\"⟶Switcher", icon='PRESET').action = 'action.gpenciledit_animation_menu'

def gpenciledit_weight_menu_to_switcher(self, context):
    show_switcher = bpy.context.preferences.addons[ADDON_NAME].preferences.to_show_to_switcher
    if not show_switcher or not bpy.context.mode == 'EDIT_GPENCIL':
        return
    self.layout.separator()
    self.layout.operator("call.add_to_switcher_menu", text="\"权重(菜单)\"⟶Switcher", icon='PRESET').action = 'action.gpenciledit_weight_gpencil'

def gpenciledit_cleanup_menu_to_switcher(self, context):
    show_switcher = bpy.context.preferences.addons[ADDON_NAME].preferences.to_show_to_switcher
    if not show_switcher:
        return
    self.layout.separator()
    self.layout.operator("call.add_to_switcher_menu", text="\"清理(菜单)\"⟶Switcher", icon='PRESET').action = 'action.gpenciledit_cleanup_menu'

def gpenciledit_simplify_menu_to_switcher(self, context):
    show_switcher = bpy.context.preferences.addons[ADDON_NAME].preferences.to_show_to_switcher
    if not show_switcher:
        return
    self.layout.separator()
    self.layout.operator("call.add_to_switcher_menu", text="\"简化笔画(菜单)\"⟶Switcher", icon='PRESET').action = 'action.call_gpenciledit_simplify_menu'

def gpenciledit_move_to_layer_menu_to_switcher(self, context):
    show_switcher = bpy.context.preferences.addons[ADDON_NAME].preferences.to_show_to_switcher
    if not show_switcher:
        return
    self.layout.separator()
    self.layout.operator("call.add_to_switcher_menu", text="\"移动到层(菜单)\"⟶Switcher", icon='PRESET').action = 'action.call_gpenciledit_move_to_layer_menu'

def gpenciledit_assign_material_menu_to_switcher(self, context):
    show_switcher = bpy.context.preferences.addons[ADDON_NAME].preferences.to_show_to_switcher
    if not show_switcher:
        return
    self.layout.separator()
    self.layout.operator("call.add_to_switcher_menu", text="\"指定材质(菜单)\"⟶Switcher", icon='PRESET').action = 'action.call_gpenciledit_assign_material_menu'

def gpenciledit_vertex_group_menu_to_switcher(self, context):
    show_switcher = bpy.context.preferences.addons[ADDON_NAME].preferences.to_show_to_switcher
    if not show_switcher:
        return
    self.layout.separator()
    self.layout.operator("call.add_to_switcher_menu", text="\"顶点组(菜单)\"⟶Switcher", icon='PRESET').action = 'action.gpenciledit_gpencil_vertex_group_menu'

def gpenciledit_scale_thickness_to_switcher(self, context):
    show_switcher = bpy.context.preferences.addons[ADDON_NAME].preferences.to_show_to_switcher
    if not show_switcher:
        return
    self.layout.separator()
    self.layout.operator("call.add_to_switcher_menu", text="\"缩放厚度\"⟶Switcher", icon='PLUS').action = 'action.gpenciledit_scale_thickness'

def register():
    bpy.types.UI_MT_button_context_menu.append(draw_add_to_switcher_gpenciledit)
    if bpy.app.version <= (4, 2, 0):
        bpy.types.GPENCIL_MT_layer_active.append(gpenciledit_layer_add_menu_to_switcher)
        bpy.types.VIEW3D_MT_gpencil_animation.append(gpenciledit_animation_menu_to_switcher)
        bpy.types.VIEW3D_MT_weight_gpencil.append(gpenciledit_weight_menu_to_switcher)
        bpy.types.GPENCIL_MT_cleanup.append(gpenciledit_cleanup_menu_to_switcher)
        bpy.types.VIEW3D_MT_gpencil_simplify.append(gpenciledit_simplify_menu_to_switcher)
        bpy.types.GPENCIL_MT_move_to_layer.append(gpenciledit_move_to_layer_menu_to_switcher)
        bpy.types.VIEW3D_MT_assign_material.append(gpenciledit_assign_material_menu_to_switcher)
        bpy.types.VIEW3D_MT_gpencil_vertex_group.append(gpenciledit_vertex_group_menu_to_switcher)
        bpy.types.VIEW3D_MT_edit_gpencil_stroke.append(gpenciledit_scale_thickness_to_switcher)

def unregister():
    if bpy.app.version <= (4, 2, 0):
        bpy.types.VIEW3D_MT_edit_gpencil_stroke.remove(gpenciledit_scale_thickness_to_switcher)
        bpy.types.VIEW3D_MT_gpencil_vertex_group.remove(gpenciledit_vertex_group_menu_to_switcher)
        bpy.types.VIEW3D_MT_assign_material.remove(gpenciledit_assign_material_menu_to_switcher)
        bpy.types.GPENCIL_MT_move_to_layer.remove(gpenciledit_move_to_layer_menu_to_switcher)
        bpy.types.VIEW3D_MT_gpencil_simplify.remove(gpenciledit_simplify_menu_to_switcher)
        bpy.types.GPENCIL_MT_cleanup.remove(gpenciledit_cleanup_menu_to_switcher)
        bpy.types.VIEW3D_MT_weight_gpencil.remove(gpenciledit_weight_menu_to_switcher)
        bpy.types.VIEW3D_MT_gpencil_animation.remove(gpenciledit_animation_menu_to_switcher)
        bpy.types.GPENCIL_MT_layer_active.remove(gpenciledit_layer_add_menu_to_switcher)
    bpy.types.UI_MT_button_context_menu.remove(draw_add_to_switcher_gpenciledit)
