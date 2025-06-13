import bpy
from .. import ADDON_NAME

def draw_add_to_switcher_global(self, context):

    show_switcher = bpy.context.preferences.addons[ADDON_NAME].preferences.to_show_to_switcher
    if not show_switcher:
        return
    
    op = getattr(context, "operator", None) or getattr(context, "button_operator", None)

    if op and op.bl_rna.identifier in {
        "OBJECT_OT_select_all",
        "CURVE_OT_select_all",
        "MBALL_OT_select_all",
        "LATTICE_OT_select_all",
        "MESH_OT_select_all",
        "PAINT_OT_face_select_all",
        "GPENCIL_OT_select_all",    #4.2 版本或以下
        "GREASE_PENCIL_OT_select_all", #4.3 版本或以上
        "ARMATURE_OT_select_all",
        "POSE_OT_select_all",
        }:
        layout = self.layout
        layout.separator()
        layout.operator("call.add_to_switcher_menu", text="\"全选\"⟶Switcher", icon='EVENT_A').action = 'action.global_select_all'
        layout.operator("call.add_to_switcher_menu", text="\"反选\"⟶Switcher", icon='PLUS').action = 'action.global_select_invert'

    elif op and op.bl_rna.identifier == "FONT_OT_select_all":
        layout = self.layout
        layout.separator()
        layout.operator("call.add_to_switcher_menu", text="\"全选\"⟶Switcher", icon='EVENT_A').action = 'action.global_select_all'

    elif op and op.bl_rna.identifier in {
        "VIEW3D_OT_select_circle",
        "GPENCIL_OT_select_circle",
        }:
        layout = self.layout
        layout.separator()
        layout.operator("call.add_to_switcher_menu", text="\"刷选\"⟶Switcher", icon='EVENT_C').action = 'action.global_select_circle'

    elif op and op.bl_rna.identifier in {
        "OBJECT_OT_select_mirror",
        "LATTICE_OT_select_mirror",
        "MESH_OT_select_mirror",
        "ARMATURE_OT_select_mirror",
        "POSE_OT_select_mirror",
        }:
        layout = self.layout
        layout.separator()
        layout.operator("call.add_to_switcher_menu", text="\"选择镜像\"⟶Switcher", icon='MOD_MIRROR').action = 'action.global_select_select_mirror'

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
        layout.operator("call.add_to_switcher_menu", text="\"随机选择\"⟶Switcher", icon='PLUS').action = 'action.global_select_select_random'

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
        "PAINT_OT_face_select_more",
        "PAINT_OT_face_select_less",
        }:
        layout = self.layout
        layout.separator()
        layout.operator("call.add_to_switcher_menu", text="\"加选/减选(菜单)\"⟶Switcher", icon='FORCE_CHARGE').action = 'action.call_global_select_more_or_less_menu'

    elif op and op.bl_rna.identifier in {
        "GPENCIL_OT_select_grouped",
        "POSE_OT_select_grouped",
        "OBJECT_OT_select_grouped",
        }:
        layout = self.layout
        layout.separator()
        layout.operator("call.add_to_switcher_menu", text="\"按组选择(菜单)\"⟶Switcher", icon='PRESET').action = 'action.select_select_grouped'

    elif op and op.bl_rna.identifier in {
        "OBJECT_OT_select_linked",
        "GREASE_PENCIL_OT_select_linked",
        "GPENCIL_OT_select_linked",
        "CURVE_OT_select_linked",
        "POSE_OT_select_linked",
        "PAINT_OT_face_select_linked",
        "PAINT_OT_vert_select_linked",
        }:
        layout = self.layout
        layout.separator()
        layout.operator("call.add_to_switcher_menu", text="\"选择相连(菜单)\"⟶Switcher", icon='LINK_BLEND').action = 'action.global_select_select_linked'

    elif op and op.bl_rna.identifier == "OBJECT_OT_select_pattern":
        layout = self.layout
        layout.separator()
        layout.operator("call.add_to_switcher_menu", text="\"按名称选择\"⟶Switcher", icon='PLUS').action = 'action.object_select_pattern'

    elif op and op.bl_rna.identifier in {
        "CURVE_OT_select_similar",
        "MBALL_OT_select_similar",
        "GREASE_PENCIL_OT_select_similar",
        }:
        layout = self.layout
        layout.separator()
        layout.operator("call.add_to_switcher_menu", text="\"选择相似(菜单)\"⟶Switcher", icon='PRESET').action = 'action.global_select_select_similar'

    elif op and op.bl_rna.identifier in {
        "PAINT_OT_vert_select_ungrouped",
        "LATTICE_OT_select_ungrouped",
        }:
        layout = self.layout
        layout.separator()
        layout.operator("call.add_to_switcher_menu", text="\"未归组顶点\"⟶Switcher", icon='PLUS').action = 'action.global_selectt_select_ungrouped'

    elif op and op.bl_rna.identifier == "GPENCIL_OT_select_first":
        layout = self.layout
        layout.separator()
        layout.operator("call.add_to_switcher_menu", text="\"选择首点\"⟶Switcher", icon='PLUS').action = 'action.global_gpencil_select_select_first'

    elif op and op.bl_rna.identifier == "GPENCIL_OT_select_last":
        layout = self.layout
        layout.separator()
        layout.operator("call.add_to_switcher_menu", text="\"选择末点\"⟶Switcher", icon='PLUS').action = 'action.global_gpencil_select_select_last'

    elif op and op.bl_rna.identifier == "GREASE_PENCIL_OT_select_ends":
        layout = self.layout
        layout.separator()
        layout.operator("call.add_to_switcher_menu", text="\"起始点\"⟶Switcher", icon='PLUS').action = 'action.global_greasepencil_select_select_first'
        layout.operator("call.add_to_switcher_menu", text="\"结束点\"⟶Switcher", icon='PLUS').action = 'action.global_greasepencil_select_select_last'

    elif op and op.bl_rna.identifier in {
        "GPENCIL_OT_select_alternate",
        "GREASE_PENCIL_OT_select_alternate",
        }:
        layout = self.layout
        layout.separator()
        layout.operator("call.add_to_switcher_menu", text="\"选择交替\"⟶Switcher", icon='PLUS').action = 'action.global_select_select_alternate'

    elif op and op.bl_rna.identifier == "TRANSFORM_OT_tosphere":
        layout = self.layout
        layout.separator()
        layout.operator("call.add_to_switcher_menu", text="\"球形化\"⟶Switcher", icon='SPHERE').action = 'action.global_transform_tosphere'

    elif op and op.bl_rna.identifier == "TRANSFORM_OT_shear":
        layout = self.layout
        layout.separator()
        layout.operator("call.add_to_switcher_menu", text="\"切变\"⟶Switcher", icon='PLUS').action = 'action.global_transform_shear'

    elif op and op.bl_rna.identifier == "TRANSFORM_OT_bend":
        layout = self.layout
        layout.separator()
        layout.operator("call.add_to_switcher_menu", text="\"弯曲\"⟶Switcher", icon='PLUS').action = 'action.global_transform_bend'

    elif op and op.bl_rna.identifier == "TRANSFORM_OT_push_pull":
        layout = self.layout
        layout.separator()
        layout.operator("call.add_to_switcher_menu", text="\"推/拉\"⟶Switcher", icon='PLUS').action = 'action.global_transform_push_pull'

    elif op and op.bl_rna.identifier == "TRANSFORM_OT_translate":
        layout = self.layout
        layout.separator()
        layout.operator("call.add_to_switcher_menu", text="\"移动纹理空间\"⟶Switcher", icon='PLUS').action = 'action.global_transform_translate_texturespace_true'

    elif op and op.bl_rna.identifier == "TRANSFORM_OT_resize":
        layout = self.layout
        layout.separator()
        layout.operator("call.add_to_switcher_menu", text="\"缩放纹理空间\"⟶Switcher", icon='PLUS').action = 'action.global_transform_resize_texturespace_true'

    elif op and op.bl_rna.identifier == "TRANSFORM_OT_vertex_warp":
        layout = self.layout
        layout.separator()
        layout.operator("call.add_to_switcher_menu", text="\"弯绕\"⟶Switcher", icon='PLUS').action = 'action.global_transform_vertex_warp'

    elif op and op.bl_rna.identifier == "TRANSFORM_OT_vertex_random":
        layout = self.layout
        layout.separator()
        layout.operator("call.add_to_switcher_menu", text="\"随机\"⟶Switcher", icon='PLUS').action = 'action.global_transform_vertex_random'

    elif op and op.bl_rna.identifier == "TRANSFORM_OT_mirror":
        layout = self.layout
        layout.separator()
        layout.operator("call.add_to_switcher_menu", text="\"交互镜像\"⟶Switcher", icon='MOD_MIRROR').action = 'action.global_transform_mirror'

    elif op and op.bl_rna.identifier in {
        "OBJECT_OT_duplicate_move",
        "CURVE_OT_duplicate_move",
        "MBALL_OT_duplicate_metaelems",
        "GPENCIL_OT_duplicate_move", # 4.2 edition
        "GREASE_PENCIL_OT_duplicate_move", # 4.3 edition
        "MESH_OT_duplicate_move",
        "ARMATURE_OT_duplicate_move",
        }:
        layout = self.layout
        layout.separator()
        layout.operator("call.add_to_switcher_menu", text="\"复制\"⟶Switcher", icon='DUPLICATE').action = 'action.global_duplicate_move'
    
    elif op and op.bl_rna.identifier in {
        "VIEW3D_OT_copybuffer",
        "GPENCIL_OT_copy", # 4.2 edition
        "GREASE_PENCIL_OT_copy", # 4.3 edition
        "POSE_OT_copy",
        }:
        layout = self.layout
        layout.separator()
        layout.operator("call.add_to_switcher_menu", text="\"复制\"⟶Switcher", icon='COPYDOWN').action = 'action.global_copy'

    elif op and op.bl_rna.identifier in {
        "VIEW3D_OT_pastebuffer",
        "GPENCIL_OT_paste", # 4.2 edition
        "GREASE_PENCIL_OT_paste", # 4.3 edition
        "POSE_OT_paste",
        }:
        layout = self.layout
        layout.separator()
        layout.operator("call.add_to_switcher_menu", text="\"粘贴\"⟶Switcher", icon='PASTEDOWN').action = 'action.global_paste'

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
        layout.operator("call.add_to_switcher_menu", text="\"隐藏选中项\"⟶Switcher", icon='EVENT_H').action = 'action.global_hide_view_set'
        layout.operator("call.add_to_switcher_menu", text="\"隐藏未选项\"⟶Switcher", icon='HIDE_ON').action = 'action.global_hide_view_set_unselected'

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
        layout.operator("call.add_to_switcher_menu", text="\"显示隐藏项\"⟶Switcher", icon='HIDE_OFF').action = 'action.global_hide_view_clear'

    elif op and op.bl_rna.identifier in {
        "OBJECT_OT_delete",
        "MBALL_OT_delete_metaelems",
        "GPENCIL_OT_delete",
        "GPENCIL_OT_active_frames_delete_all",
        "GREASE_PENCIL_OT_active_frame_delete",
        }:
        layout = self.layout
        layout.separator()
        layout.operator("call.add_to_switcher_menu", text="\"删除\"⟶Switcher", icon='EVENT_X').action = 'action.global_call_delete_menu'
        if bpy.context.mode == "OBJECT":
            layout.operator("call.add_to_switcher_menu", text="\"全局删除\"⟶Switcher", icon='PLUS').action = 'action.object_delete_global_true'

    elif op and op.bl_rna.identifier in {
        "GPENCIL_OT_snap_to_grid",
        "GREASE_PENCIL_OT_snap_to_grid",
        "VIEW3D_OT_snap_selected_to_grid",
        }:
        layout = self.layout
        layout.separator()
        layout.operator("call.add_to_switcher_menu", text="\"选中项->栅格点\"⟶Switcher", icon='PLUS').action = 'action.global_selected_to_grid'

    elif op and op.bl_rna.identifier in {
        "GPENCIL_OT_snap_to_cursor",
        "GREASE_PENCIL_OT_snap_to_cursor",
        "VIEW3D_OT_snap_selected_to_cursor",
        }:
        layout = self.layout
        layout.separator()
        layout.operator("call.add_to_switcher_menu", text="\"选中项->游标\"⟶Switcher", icon='PLUS').action = 'action.global_snap_selected_to_cursor_offset_false'
        layout.operator("call.add_to_switcher_menu", text="\"选中项->游标(保持偏移)\"⟶Switcher", icon='PLUS').action = 'action.global_snap_selected_to_cursor_offset_true'

    elif op and op.bl_rna.identifier == "VIEW3D_OT_snap_selected_to_active":
        layout = self.layout
        layout.separator()
        layout.operator("call.add_to_switcher_menu", text="\"选中项->活动项\"⟶Switcher", icon='PLUS').action = 'action.global_snap_selected_to_active'

    elif op and op.bl_rna.identifier in {
        "GPENCIL_OT_snap_cursor_to_selected",
        "GREASE_PENCIL_OT_snap_cursor_to_selected",
        "VIEW3D_OT_snap_cursor_to_selected",
        }:
        layout = self.layout
        layout.separator()
        layout.operator("call.add_to_switcher_menu", text="\"游标->选中项\"⟶Switcher", icon='PLUS').action = 'action.global_snap_cursor_to_selected'

    elif op and op.bl_rna.identifier == "VIEW3D_OT_snap_cursor_to_center":
        layout = self.layout
        layout.separator()
        layout.operator("call.add_to_switcher_menu", text="\"游标->世界原点\"⟶Switcher", icon='PLUS').action = 'action.global_snap_cursor_to_center'

    elif op and op.bl_rna.identifier == "VIEW3D_OT_snap_cursor_to_grid":
        layout = self.layout
        layout.separator()
        layout.operator("call.add_to_switcher_menu", text="\"游标->栅格点\"⟶Switcher", icon='PLUS').action = 'action.global_snap_cursor_to_grid'

    elif op and op.bl_rna.identifier == "VIEW3D_OT_snap_cursor_to_active":
        layout = self.layout
        layout.separator()
        layout.operator("call.add_to_switcher_menu", text="\"游标->活动项\"⟶Switcher", icon='PLUS').action = 'action.global_snap_cursor_to_active'

    elif op and op.bl_rna.identifier == "OBJECT_OT_parent_set":
        layout = self.layout
        layout.separator()
        layout.operator("call.add_to_switcher_menu", text="\"设置父级目标(菜单)\"⟶Switcher", icon='PRESET').action = 'action.global_set_parent_menu'

    elif op and op.bl_rna.identifier == "OBJECT_OT_parent_clear":
        layout = self.layout
        layout.separator()
        layout.operator("call.add_to_switcher_menu", text="\"清空父级(菜单)\"⟶Switcher", icon='PRESET').action = 'action.global_parent_clear_menu'























































def global_select_select_similar_menu_to_switcher(self, context):
    show_switcher = bpy.context.preferences.addons[ADDON_NAME].preferences.to_show_to_switcher
    if not show_switcher:
        return
    self.layout.separator()
    self.layout.operator("call.add_to_switcher_menu", text="\"选择相似(菜单)\"⟶Switcher", icon='PRESET').action = 'action.global_select_select_similar'

def global_transform_menu_to_switcher(self, context):
    show_switcher = bpy.context.preferences.addons[ADDON_NAME].preferences.to_show_to_switcher
    if not show_switcher:
        return
    self.layout.separator()
    self.layout.operator("call.add_to_switcher_menu", text="\"变换(菜单)\"⟶Switcher", icon='PRESET').action = 'action.global_transform'
    if context.mode == "EDIT_GPENCIL":
        self.layout.operator("call.add_to_switcher_menu", text="\"法向缩放\"⟶Switcher", icon='PLUS').action = 'action.gpenciledit_transform_shrink_fatten'

def global_hide_show_menu_to_switcher(self, context):
    show_switcher = bpy.context.preferences.addons[ADDON_NAME].preferences.to_show_to_switcher
    if not show_switcher:
        return
    self.layout.separator()
    self.layout.operator("call.add_to_switcher_menu", text="\"显示/隐藏(菜单)\"⟶Switcher", icon='PRESET').action = 'action.global_hide_show_menu'












def add_menu_to_switcher(self, context):
    show_switcher = bpy.context.preferences.addons[ADDON_NAME].preferences.to_show_to_switcher
    if not show_switcher:
        return
    self.layout.separator()
    self.layout.operator("call.add_to_switcher_menu", text="\"添加(菜单)\"⟶Switcher", icon='PRESET').action = 'action.global_add'


def delete_menu_to_switcher(self, context):
    show_switcher = bpy.context.preferences.addons[ADDON_NAME].preferences.to_show_to_switcher
    if not show_switcher:
        return
    self.layout.separator()
    self.layout.operator("call.add_to_switcher_menu", text="\"删除(菜单)\"⟶Switcher", icon='EVENT_X').action = 'action.global_call_delete_menu'


def apply_menu_to_switcher(self, context):
    show_switcher = bpy.context.preferences.addons[ADDON_NAME].preferences.to_show_to_switcher
    if not show_switcher:
        return
    self.layout.separator()
    self.layout.operator("call.add_to_switcher_menu", text="\"应用(菜单)\"⟶Switcher", icon='PRESET').action = 'action.global_apply'


def cleartransform_menu_to_switcher(self, context):
    show_switcher = bpy.context.preferences.addons[ADDON_NAME].preferences.to_show_to_switcher
    if not show_switcher:
        return
    self.layout.separator()
    self.layout.operator("call.add_to_switcher_menu", text="\"清空(菜单)\"⟶Switcher", icon='PRESET').action = 'action.global_object_pose_clear'


def transformorientation_menu_to_switcher(self, context):
    show_switcher = bpy.context.preferences.addons[ADDON_NAME].preferences.to_show_to_switcher
    if not show_switcher:
        return
    self.layout.separator()
    self.layout.operator("call.add_to_switcher_menu", text="\"切换坐标系(菜单)\"⟶Switcher", icon='PRESET').action = 'action.switch_orientation_menu'
    self.layout.operator("call.add_to_switcher_menu", text="\"全局\"⟶Switcher", icon='ORIENTATION_GLOBAL').action = 'action.orientation_to_global'
    self.layout.operator("call.add_to_switcher_menu", text="\"局部\"⟶Switcher", icon='ORIENTATION_LOCAL').action = 'action.orientation_to_local'
    self.layout.operator("call.add_to_switcher_menu", text="\"法向\"⟶Switcher", icon='ORIENTATION_NORMAL').action = 'action.orientation_to_normal'
    self.layout.operator("call.add_to_switcher_menu", text="\"万向\"⟶Switcher", icon='ORIENTATION_GIMBAL').action = 'action.orientation_to_gimbal'
    self.layout.operator("call.add_to_switcher_menu", text="\"视图\"⟶Switcher", icon='ORIENTATION_VIEW').action = 'action.orientation_to_view'
    self.layout.operator("call.add_to_switcher_menu", text="\"游标\"⟶Switcher", icon='ORIENTATION_CURSOR').action = 'action.orientation_to_cursor'
    self.layout.operator("call.add_to_switcher_menu", text="\"父级\"⟶Switcher", icon='ORIENTATION_PARENT').action = 'action.orientation_to_parent'

def switchsnap_menu_to_switcher(self, context):
    show_switcher = bpy.context.preferences.addons[ADDON_NAME].preferences.to_show_to_switcher
    if not show_switcher:
        return
    self.layout.separator()
    self.layout.operator("call.add_to_switcher_menu", text="\"切换吸附(菜单)\"⟶Switcher", icon='PRESET').action = 'action.switch_snap_menu'
    self.layout.operator("call.add_to_switcher_menu", text="\"开/关吸附\"⟶Switcher", icon='SNAP_ON').action = 'action.switch_snap_toggle'
    self.layout.operator("call.add_to_switcher_menu", text="\"增量\"⟶Switcher", icon='SNAP_INCREMENT').action = 'action.switch_snap_increment'
    self.layout.operator("call.add_to_switcher_menu", text="\"顶点\"⟶Switcher", icon='SNAP_VERTEX').action = 'action.switch_snap_vertex'
    self.layout.operator("call.add_to_switcher_menu", text="\"边\"⟶Switcher", icon='SNAP_EDGE').action = 'action.switch_snap_edge'
    self.layout.operator("call.add_to_switcher_menu", text="\"面投射\"⟶Switcher", icon='SNAP_FACE').action = 'action.switch_snap_face'
    self.layout.operator("call.add_to_switcher_menu", text="\"面最近\"⟶Switcher", icon='SNAP_FACE_NEAREST').action = 'action.switch_snap_face_nearest'
    self.layout.operator("call.add_to_switcher_menu", text="\"体积\"⟶Switcher", icon='SNAP_VOLUME').action = 'action.switch_snap_volume'
    self.layout.operator("call.add_to_switcher_menu", text="\"边中点\"⟶Switcher", icon='SNAP_MIDPOINT').action = 'action.switch_snap_edge_midpoint'
    self.layout.operator("call.add_to_switcher_menu", text="\"垂直交线\"⟶Switcher", icon='SNAP_PERPENDICULAR').action = 'action.switch_snap_edge_perpendicular'

def switchproportional_menu_to_switcher(self, context):
    show_switcher = bpy.context.preferences.addons[ADDON_NAME].preferences.to_show_to_switcher
    if not show_switcher:
        return
    self.layout.separator()
    self.layout.operator("call.add_to_switcher_menu", text="\"切换衰减编辑(菜单)\"⟶Switcher", icon='PRESET').action = 'action.switch_proportional_menu'
    self.layout.operator("call.add_to_switcher_menu", text="\"开/关衰减编辑\"⟶Switcher", icon='PROP_ON').action = 'action.switch_proportional_toggle'
    self.layout.operator("call.add_to_switcher_menu", text="\"平滑\"⟶Switcher", icon='SMOOTHCURVE').action = 'action.switch_proportional_smooth'
    self.layout.operator("call.add_to_switcher_menu", text="\"球体\"⟶Switcher", icon='SPHERECURVE').action = 'action.switch_proportional_sphere'
    self.layout.operator("call.add_to_switcher_menu", text="\"根凸\"⟶Switcher", icon='ROOTCURVE').action = 'action.switch_proportional_root'
    self.layout.operator("call.add_to_switcher_menu", text="\"平方反比\"⟶Switcher", icon='INVERSESQUARECURVE').action = 'action.switch_proportional_inverse_square'
    self.layout.operator("call.add_to_switcher_menu", text="\"锐利\"⟶Switcher", icon='SHARPCURVE').action = 'action.switch_proportional_sharp'
    self.layout.operator("call.add_to_switcher_menu", text="\"线性\"⟶Switcher", icon='LINCURVE').action = 'action.switch_proportional_linear'
    self.layout.operator("call.add_to_switcher_menu", text="\"常值\"⟶Switcher", icon='NOCURVE').action = 'action.switch_proportional_constant'
    self.layout.operator("call.add_to_switcher_menu", text="\"随机\"⟶Switcher", icon='RNDCURVE').action = 'action.switch_proportional_random'

def snap_menu_to_switcher(self, context):
    show_switcher = bpy.context.preferences.addons[ADDON_NAME].preferences.to_show_to_switcher
    if not show_switcher:
        return
    self.layout.separator()
    self.layout.operator("call.add_to_switcher_menu", text="\"吸附(菜单)\"⟶Switcher", icon='PRESET').action = 'action.global_snap_menu'

def global_parent_menu_to_switcher(self, context):
    show_switcher = bpy.context.preferences.addons[ADDON_NAME].preferences.to_show_to_switcher
    if not show_switcher:
        return
    self.layout.separator()
    self.layout.operator("call.add_to_switcher_menu", text="\"父级(菜单)\"⟶Switcher", icon='PRESET').action = 'action.global_parent_menu'

def global_show_face_orientation_to_switcher(self, context):
    show_switcher = bpy.context.preferences.addons[ADDON_NAME].preferences.to_show_to_switcher
    if not show_switcher:
        return
    self.layout.separator()
    self.layout.operator("call.add_to_switcher_menu", text="\"面朝向\"⟶Switcher", icon='PLUS').action = 'action.meshedit_edit_show_face_orientation'



def register():
    bpy.types.UI_MT_button_context_menu.append(draw_add_to_switcher_global)
    #“添加”菜单

    # "选择"菜单
    bpy.types.VIEW3D_MT_edit_mesh_select_similar.append(global_select_select_similar_menu_to_switcher)

    bpy.types.VIEW3D_MT_add.append(add_menu_to_switcher)
    bpy.types.VIEW3D_MT_mesh_add.append(add_menu_to_switcher)
    bpy.types.VIEW3D_MT_curve_add.append(add_menu_to_switcher)
    bpy.types.VIEW3D_MT_surface_add.append(add_menu_to_switcher)
    bpy.types.VIEW3D_MT_metaball_add.append(add_menu_to_switcher)
    bpy.types.TOPBAR_MT_edit_armature_add.append(add_menu_to_switcher)

    # "变换"菜单
    bpy.types.VIEW3D_MT_transform_object.append(global_transform_menu_to_switcher)
    bpy.types.VIEW3D_MT_transform.append(global_transform_menu_to_switcher)
    if bpy.app.version > (4, 2, 0):
        bpy.types.VIEW3D_MT_sculpt_transform.append(global_transform_menu_to_switcher)
    if bpy.app.version < (4, 3, 0):
        bpy.types.VIEW3D_MT_edit_gpencil_transform.append(global_transform_menu_to_switcher) 
    bpy.types.VIEW3D_MT_transform_armature.append(global_transform_menu_to_switcher)

    #“删除”菜单
    bpy.types.VIEW3D_MT_edit_mesh_delete.append(delete_menu_to_switcher)
    if bpy.app.version <= (4, 2, 0):
        bpy.types.VIEW3D_MT_edit_gpencil_delete.append(delete_menu_to_switcher)    
    if bpy.app.version >= (4, 3, 0):
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

    bpy.types.VIEW3D_MT_object_showhide.append(global_hide_show_menu_to_switcher)
    bpy.types.VIEW3D_MT_edit_curve_showhide.append(global_hide_show_menu_to_switcher)
    bpy.types.VIEW3D_MT_edit_meta_showhide.append(global_hide_show_menu_to_switcher)
    bpy.types.VIEW3D_MT_edit_mesh_showhide.append(global_hide_show_menu_to_switcher)
    if bpy.app.version <= (4, 2, 0):
        bpy.types.VIEW3D_MT_edit_gpencil_showhide.append(global_hide_show_menu_to_switcher)
    if bpy.app.version >= (4, 3, 0):
        bpy.types.VIEW3D_MT_edit_greasepencil_showhide.append(global_hide_show_menu_to_switcher)
    if bpy.app.version <= (4, 2, 0):
        bpy.types.GPENCIL_MT_snap.append(snap_menu_to_switcher)
    if bpy.app.version >= (4, 3, 0):
        bpy.types.GREASE_PENCIL_MT_snap.append(snap_menu_to_switcher)
    bpy.types.VIEW3D_MT_snap.append(snap_menu_to_switcher)
    bpy.types.VIEW3D_MT_object_parent.append(global_parent_menu_to_switcher)
    bpy.types.VIEW3D_MT_view.append(global_show_face_orientation_to_switcher)


def unregister():

    bpy.types.VIEW3D_MT_view.remove(global_show_face_orientation_to_switcher)
    bpy.types.VIEW3D_MT_object_parent.remove(global_parent_menu_to_switcher)
    bpy.types.VIEW3D_MT_snap.remove(snap_menu_to_switcher)
    if bpy.app.version >= (4, 3, 0):
        bpy.types.GREASE_PENCIL_MT_snap.remove(snap_menu_to_switcher)
    if bpy.app.version <= (4, 2, 0):
        bpy.types.GPENCIL_MT_snap.remove(snap_menu_to_switcher)


    if bpy.app.version <= (4, 2, 0):
        bpy.types.VIEW3D_MT_edit_gpencil_showhide.remove(global_hide_show_menu_to_switcher)
    if bpy.app.version >= (4, 3, 0):
        bpy.types.VIEW3D_MT_edit_greasepencil_showhide.remove(global_hide_show_menu_to_switcher)
    bpy.types.VIEW3D_MT_edit_mesh_showhide.remove(global_hide_show_menu_to_switcher)
    bpy.types.VIEW3D_MT_edit_meta_showhide.remove(global_hide_show_menu_to_switcher)
    bpy.types.VIEW3D_MT_edit_curve_showhide.remove(global_hide_show_menu_to_switcher)
    bpy.types.VIEW3D_MT_object_showhide.remove(global_hide_show_menu_to_switcher)
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

    # “变换”菜单
    bpy.types.VIEW3D_MT_transform_armature.remove(global_transform_menu_to_switcher)
    if bpy.app.version < (4, 3, 0):
        bpy.types.VIEW3D_MT_edit_gpencil_transform.remove(global_transform_menu_to_switcher)
    if bpy.app.version > (4, 2, 0):
        bpy.types.VIEW3D_MT_sculpt_transform.remove(global_transform_menu_to_switcher)
    bpy.types.VIEW3D_MT_transform.remove(global_transform_menu_to_switcher)
    bpy.types.VIEW3D_MT_transform_object.remove(global_transform_menu_to_switcher)

    #“添加”菜单
    bpy.types.TOPBAR_MT_edit_armature_add.remove(add_menu_to_switcher)
    bpy.types.VIEW3D_MT_metaball_add.remove(add_menu_to_switcher)
    bpy.types.VIEW3D_MT_surface_add.remove(add_menu_to_switcher)
    bpy.types.VIEW3D_MT_curve_add.remove(add_menu_to_switcher)
    bpy.types.VIEW3D_MT_mesh_add.remove(add_menu_to_switcher)
    bpy.types.VIEW3D_MT_add.remove(add_menu_to_switcher)

    # “选择”菜单
    bpy.types.VIEW3D_MT_edit_mesh_select_similar.remove(global_select_select_similar_menu_to_switcher)

    bpy.types.UI_MT_button_context_menu.remove(draw_add_to_switcher_global)

