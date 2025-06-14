import bpy
from .. import ADDON_NAME

def draw_add_to_switcher_greasepenciledit(self, context):

    show_switcher = bpy.context.preferences.addons[ADDON_NAME].preferences.to_show_to_switcher
    if not show_switcher:
        return
    
    op = getattr(context, "operator", None) or getattr(context, "button_operator", None)

    if op and op.bl_rna.identifier == "GREASE_PENCIL_OT_layer_add":
        layout = self.layout
        layout.separator()
        layout.operator("call.add_to_switcher_menu", text="\"新建层\"⟶Switcher", icon='ADD').action = 'action.greasepenciledit_layer_add'

    elif op and op.bl_rna.identifier == "GREASE_PENCIL_OT_insert_blank_frame":
        layout = self.layout
        layout.separator()
        layout.operator("call.add_to_switcher_menu", text="\"在活动层插入空白帧\"⟶Switcher", icon='PLUS').action = 'action.greasepenciledit_insert_blank_frame_false'
        layout.operator("call.add_to_switcher_menu", text="\"在所有层插入空白帧\"⟶Switcher", icon='PLUS').action = 'action.greasepenciledit_insert_blank_frame_true'

    elif op and op.bl_rna.identifier == "GREASE_PENCIL_OT_frame_duplicate":
        layout = self.layout
        layout.separator()
        layout.operator("call.add_to_switcher_menu", text="\"复制活动层的活动关键帧\"⟶Switcher", icon='PLUS').action = 'action.greasepenciledit_frame_duplicate_false'
        layout.operator("call.add_to_switcher_menu", text="\"复制所有层的活动关键帧\"⟶Switcher", icon='PLUS').action = 'action.greasepenciledit_frame_duplicate_true'

    elif op and op.bl_rna.identifier == "GREASE_PENCIL_OT_interpolate_sequence":
        layout = self.layout
        layout.separator()
        layout.operator("call.add_to_switcher_menu", text="\"插值顺序\"⟶Switcher", icon='PLUS').action = 'action.greasepenciledit_interpolate_sequence_modal'

    elif op and op.bl_rna.identifier == "GREASE_PENCIL_OT_separate":
        layout = self.layout
        layout.separator()
        layout.operator("call.add_to_switcher_menu", text="\"分离(菜单)\"⟶Switcher", icon='PRESET').action = 'action.call_greasepenciledit_separate_menu'

    elif op and op.bl_rna.identifier == "GREASE_PENCIL_OT_clean_loose":
        layout = self.layout
        layout.separator()
        layout.operator("call.add_to_switcher_menu", text="\"清除松散点\"⟶Switcher", icon='PLUS').action = 'action.greasepenciledit_clean_loose'

    elif op and op.bl_rna.identifier == "GREASE_PENCIL_OT_frame_clean_duplicate":
        layout = self.layout
        layout.separator()
        layout.operator("call.add_to_switcher_menu", text="\"清理重复帧\"⟶Switcher", icon='PLUS').action = 'action.greasepenciledit_frame_clean_duplicate'

    elif op and op.bl_rna.identifier == "GREASE_PENCIL_OT_stroke_merge_by_distance":
        layout = self.layout
        layout.separator()
        layout.operator("call.add_to_switcher_menu", text="\"按间距合并\"⟶Switcher", icon='PLUS').action = 'action.greasepenciledit_stroke_merge_by_distance'

    elif op and op.bl_rna.identifier == "GREASE_PENCIL_OT_reproject":
        layout = self.layout
        layout.separator()
        layout.operator("call.add_to_switcher_menu", text="\"重投影笔画\"⟶Switcher", icon='PRESET').action = 'action.greasepenciledit_reproject_menu'
    # “点”菜单
    elif op and op.bl_rna.identifier == "GREASE_PENCIL_OT_extrude_move":
        layout = self.layout
        layout.separator()
        layout.operator("call.add_to_switcher_menu", text="\"挤出\"⟶Switcher", icon='EVENT_E').action = 'action.greasepenciledit_extrude_move'

    elif op and op.bl_rna.identifier == "GREASE_PENCIL_OT_stroke_smooth":
        layout = self.layout
        layout.separator()
        layout.operator("call.add_to_switcher_menu", text="\"光滑\"⟶Switcher", icon='PLUS').action = 'action.greasepenciledit_stroke_smooth'

    elif op and op.bl_rna.identifier == "GREASE_PENCIL_OT_set_handle_type":
        layout = self.layout
        layout.separator()
        layout.operator("call.add_to_switcher_menu", text="\"设置控制柄类型\"⟶Switcher", icon='PRESET').action = 'action.greasepenciledit_set_handle_type'

    elif op and op.bl_rna.identifier == "GREASE_PENCIL_OT_stroke_subdivide":
        layout = self.layout
        layout.separator()
        layout.operator("call.add_to_switcher_menu", text="\"细分笔画\"⟶Switcher", icon='PLUS').action = 'action.greasepenciledit_stroke_subdivide'

    elif op and op.bl_rna.identifier == "GREASE_PENCIL_OT_stroke_subdivide_smooth":
        layout = self.layout
        layout.separator()
        layout.operator("call.add_to_switcher_menu", text="\"细分并平滑笔画\"⟶Switcher", icon='PLUS').action = 'action.greasepenciledit_stroke_subdivide_smooth'

    elif op and op.bl_rna.identifier == "GREASE_PENCIL_OT_stroke_simplify":
        layout = self.layout
        layout.separator()
        layout.operator("call.add_to_switcher_menu", text="\"简化笔画\"⟶Switcher", icon='PLUS').action = 'action.greasepenciledit_stroke_simplify'

    elif op and op.bl_rna.identifier == "GREASE_PENCIL_OT_join_selection":
        layout = self.layout
        layout.separator()
        layout.operator("call.add_to_switcher_menu", text="\"合并笔画\"⟶Switcher", icon='PRESET').action = 'action.greasepenciledit_join_selection'
        layout.operator("call.add_to_switcher_menu", text="\"合并笔画\"⟶Switcher", icon='PLUS').action = 'action.greasepenciledit_join_selection_join'
        layout.operator("call.add_to_switcher_menu", text="\"合并并复制笔画\"⟶Switcher", icon='PLUS').action = 'action.greasepenciledit_join_selection_joincopy'

    elif op and op.bl_rna.identifier == "GREASE_PENCIL_OT_set_active_material":
        layout = self.layout
        layout.separator()
        layout.operator("call.add_to_switcher_menu", text="\"设置活动的材质\"⟶Switcher", icon='PLUS').action = 'action.greasepenciledit_set_active_material'

    elif op and op.bl_rna.identifier == "GREASE_PENCIL_OT_reorder":
        layout = self.layout
        layout.separator()
        layout.operator("call.add_to_switcher_menu", text="\"排列笔画\"⟶Switcher", icon='PRESET').action = 'action.call_greasepenciledit_reorder_menu'
        layout.operator("call.add_to_switcher_menu", text="\"笔画移到最前\"⟶Switcher", icon='PLUS').action = 'action.gpenciledit_reorder_top'
        layout.operator("call.add_to_switcher_menu", text="\"笔画前移\"⟶Switcher", icon='PLUS').action = 'action.gpenciledit_reorder_up'
        layout.operator("call.add_to_switcher_menu", text="\"笔画后送\"⟶Switcher", icon='PLUS').action = 'action.gpenciledit_reorder_down'
        layout.operator("call.add_to_switcher_menu", text="\"笔画移到最后\"⟶Switcher", icon='PLUS').action = 'action.gpenciledit_reorder_bottom'

    elif op and op.bl_rna.identifier == "GREASE_PENCIL_OT_cyclical_set":
        layout = self.layout
        layout.separator()
        layout.operator("call.add_to_switcher_menu", text="\"闭合笔画\"⟶Switcher", icon='PLUS').action = 'action.greasepenciledit_cyclical_set_close'
        layout.operator("call.add_to_switcher_menu", text="\"切换闭合笔画\"⟶Switcher", icon='PLUS').action = 'action.greasepenciledit_cyclical_set_toggle'

    elif op and op.bl_rna.identifier == "GREASE_PENCIL_OT_caps_set":
        layout = self.layout
        layout.separator()
        layout.operator("call.add_to_switcher_menu", text="\"设置端点\"⟶Switcher", icon='PRESET').action = 'action.greasepenciledit_caps_set'

    elif op and op.bl_rna.identifier == "GREASE_PENCIL_OT_stroke_switch_direction":
        layout = self.layout
        layout.separator()
        layout.operator("call.add_to_switcher_menu", text="\"切换方向\"⟶Switcher", icon='PLUS').action = 'action.greasepenciledit_stroke_switch_direction'

    elif op and op.bl_rna.identifier == "GREASE_PENCIL_OT_set_uniform_thickness":
        layout = self.layout
        layout.separator()
        layout.operator("call.add_to_switcher_menu", text="\"设置统一粗细\"⟶Switcher", icon='PLUS').action = 'action.greasepenciledit_set_uniform_thickness'

    elif op and op.bl_rna.identifier == "GREASE_PENCIL_OT_set_uniform_opacity":
        layout = self.layout
        layout.separator()
        layout.operator("call.add_to_switcher_menu", text="\"设置统一不透明度\"⟶Switcher", icon='PLUS').action = 'action.greasepenciledit_set_uniform_opacity'

    elif op and op.bl_rna.identifier == "GREASE_PENCIL_OT_set_curve_type":
        layout = self.layout
        layout.separator()
        layout.operator("call.add_to_switcher_menu", text="\"设置曲线类型\"⟶Switcher", icon='PRESET').action = 'action.greasepenciledit_set_curve_type'

    elif op and op.bl_rna.identifier == "GREASE_PENCIL_OT_set_curve_resolution":
        layout = self.layout
        layout.separator()
        layout.operator("call.add_to_switcher_menu", text="\"设置曲线分辨率\"⟶Switcher", icon='PLUS').action = 'action.greasepenciledit_set_curve_resolution'

    elif op and op.bl_rna.identifier == "GREASE_PENCIL_OT_reset_uvs":
        layout = self.layout
        layout.separator()
        layout.operator("call.add_to_switcher_menu", text="\"重置UV\"⟶Switcher", icon='PLUS').action = 'action.greasepenciledit_reset_uvs'


def greasepenciledit_layer_add_menu_to_switcher(self, context):
    show_switcher = bpy.context.preferences.addons[ADDON_NAME].preferences.to_show_to_switcher
    if not show_switcher:
        return
    self.layout.separator()
    self.layout.operator("call.add_to_switcher_menu", text="\"活动层(菜单)\"⟶Switcher", icon='PRESET').action = 'action.greasepenciledit_layer_active_menu'

def greasepenciledit_animation_menu_to_switcher(self, context):
    show_switcher = bpy.context.preferences.addons[ADDON_NAME].preferences.to_show_to_switcher
    if not show_switcher:
        return
    self.layout.separator()
    self.layout.operator("call.add_to_switcher_menu", text="\"动画(菜单)\"⟶Switcher", icon='PRESET').action = 'action.greasepenciledit_animation_menu'

def greasepenciledit_weight_menu_to_switcher(self, context):
    show_switcher = bpy.context.preferences.addons[ADDON_NAME].preferences.to_show_to_switcher
    if not show_switcher:
        return
    self.layout.separator()
    self.layout.operator("call.add_to_switcher_menu", text="\"权重(菜单)\"⟶Switcher", icon='PRESET').action = 'action.greasepenciledit_weight_greasepencil'

def greasepenciledit_cleanup_menu_to_switcher(self, context):
    show_switcher = bpy.context.preferences.addons[ADDON_NAME].preferences.to_show_to_switcher
    if not show_switcher:
        return
    self.layout.separator()
    self.layout.operator("call.add_to_switcher_menu", text="\"清理(菜单)\"⟶Switcher", icon='PRESET').action = 'action.greasepenciledit_cleanup_menu'

def greasepenciledit_vertex_group_menu_to_switcher(self, context):
    show_switcher = bpy.context.preferences.addons[ADDON_NAME].preferences.to_show_to_switcher
    if not show_switcher:
        return
    self.layout.separator()
    self.layout.operator("call.add_to_switcher_menu", text="\"顶点组(菜单)\"⟶Switcher", icon='PRESET').action = 'action.greasepenciledit_vertex_group_menu'

def greasepenciledit_move_to_layer_menu_to_switcher(self, context):
    show_switcher = bpy.context.preferences.addons[ADDON_NAME].preferences.to_show_to_switcher
    if not show_switcher:
        return
    self.layout.separator()
    self.layout.operator("call.add_to_switcher_menu", text="\"移动到层(菜单)\"⟶Switcher", icon='PRESET').action = 'action.greasepenciledit_move_to_layer_menu'

def greasepenciledit_assign_material_menu_to_switcher(self, context):
    show_switcher = bpy.context.preferences.addons[ADDON_NAME].preferences.to_show_to_switcher
    if not show_switcher:
        return
    self.layout.separator()
    self.layout.operator("call.add_to_switcher_menu", text="\"指定材质(菜单)\"⟶Switcher", icon='PRESET').action = 'action.greasepenciledit_assign_material_menu'

def greasepenciledit_scale_thickness_to_switcher(self, context):
    show_switcher = bpy.context.preferences.addons[ADDON_NAME].preferences.to_show_to_switcher
    if not show_switcher:
        return
    self.layout.separator()
    self.layout.operator("call.add_to_switcher_menu", text="\"缩放厚度\"⟶Switcher", icon='PLUS').action = 'action.greasepenciledit_scale_thickness'




def register():
    bpy.types.UI_MT_button_context_menu.append(draw_add_to_switcher_greasepenciledit)
    if bpy.app.version >= (4, 3, 0):
        bpy.types.GREASE_PENCIL_MT_layer_active.append(greasepenciledit_layer_add_menu_to_switcher)
        bpy.types.VIEW3D_MT_edit_greasepencil_animation.append(greasepenciledit_animation_menu_to_switcher)
        bpy.types.VIEW3D_MT_weight_grease_pencil.append(greasepenciledit_weight_menu_to_switcher)
        bpy.types.VIEW3D_MT_edit_greasepencil_cleanup.append(greasepenciledit_cleanup_menu_to_switcher)
        bpy.types.VIEW3D_MT_greasepencil_vertex_group.append(greasepenciledit_vertex_group_menu_to_switcher)
        bpy.types.GREASE_PENCIL_MT_move_to_layer.append(greasepenciledit_move_to_layer_menu_to_switcher)
        bpy.types.VIEW3D_MT_grease_pencil_assign_material.append(greasepenciledit_assign_material_menu_to_switcher)
        bpy.types.VIEW3D_MT_edit_greasepencil_stroke.append(greasepenciledit_scale_thickness_to_switcher)

def unregister():
    if bpy.app.version >= (4, 3, 0):
        bpy.types.VIEW3D_MT_edit_greasepencil_stroke.remove(greasepenciledit_scale_thickness_to_switcher)
        bpy.types.VIEW3D_MT_grease_pencil_assign_material.remove(greasepenciledit_assign_material_menu_to_switcher)
        bpy.types.GREASE_PENCIL_MT_move_to_layer.remove(greasepenciledit_move_to_layer_menu_to_switcher)
        bpy.types.VIEW3D_MT_greasepencil_vertex_group.remove(greasepenciledit_vertex_group_menu_to_switcher)
        bpy.types.VIEW3D_MT_edit_greasepencil_cleanup.remove(greasepenciledit_cleanup_menu_to_switcher)
        bpy.types.VIEW3D_MT_weight_grease_pencil.remove(greasepenciledit_weight_menu_to_switcher)
        bpy.types.VIEW3D_MT_edit_greasepencil_animation.remove(greasepenciledit_animation_menu_to_switcher)
        bpy.types.GREASE_PENCIL_MT_layer_active.remove(greasepenciledit_layer_add_menu_to_switcher)
    bpy.types.UI_MT_button_context_menu.remove(draw_add_to_switcher_greasepenciledit)
