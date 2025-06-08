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
        layout.operator("call.add_to_switcher_menu", text="\"新建层\"⟶Switcher", icon='ADD').action = 'button.action_greasepenciledit_layer_add'

    elif op and op.bl_rna.identifier == "GREASE_PENCIL_OT_insert_blank_frame":
        layout = self.layout
        layout.separator()
        layout.operator("call.add_to_switcher_menu", text="\"在活动层插入空白帧\"⟶Switcher", icon='PLUS').action = 'button.action_greasepenciledit_insert_blank_frame_false'
        layout.operator("call.add_to_switcher_menu", text="\"在所有层插入空白帧\"⟶Switcher", icon='PLUS').action = 'button.action_greasepenciledit_insert_blank_frame_true'

    elif op and op.bl_rna.identifier == "GREASE_PENCIL_OT_frame_duplicate":
        layout = self.layout
        layout.separator()
        layout.operator("call.add_to_switcher_menu", text="\"复制活动层的活动关键帧\"⟶Switcher", icon='PLUS').action = 'button.action_greasepenciledit_frame_duplicate_false'
        layout.operator("call.add_to_switcher_menu", text="\"复制所有层的活动关键帧\"⟶Switcher", icon='PLUS').action = 'button.action_greasepenciledit_frame_duplicate_true'

    elif op and op.bl_rna.identifier == "GREASE_PENCIL_OT_separate":
        layout = self.layout
        layout.separator()
        layout.operator("call.add_to_switcher_menu", text="\"分离(菜单)\"⟶Switcher", icon='PRESET').action = 'button.action_call_greasepenciledit_separate_menu'

    elif op and op.bl_rna.identifier == "GREASE_PENCIL_OT_clean_loose":
        layout = self.layout
        layout.separator()
        layout.operator("call.add_to_switcher_menu", text="\"清除松散点\"⟶Switcher", icon='PLUS').action = 'button.action_greasepenciledit_clean_loose'

    elif op and op.bl_rna.identifier == "GREASE_PENCIL_OT_frame_clean_duplicate":
        layout = self.layout
        layout.separator()
        layout.operator("call.add_to_switcher_menu", text="\"清理重复帧\"⟶Switcher", icon='PLUS').action = 'button.action_greasepenciledit_frame_clean_duplicate'

    elif op and op.bl_rna.identifier == "GREASE_PENCIL_OT_stroke_merge_by_distance":
        layout = self.layout
        layout.separator()
        layout.operator("call.add_to_switcher_menu", text="\"按间距合并\"⟶Switcher", icon='PLUS').action = 'button.action_greasepenciledit_stroke_merge_by_distance'

    elif op and op.bl_rna.identifier == "GREASE_PENCIL_OT_reproject":
        layout = self.layout
        layout.separator()
        layout.operator("call.add_to_switcher_menu", text="\"重投影笔画\"⟶Switcher", icon='PRESET').action = 'button.action_greasepenciledit_reproject_menu'
    # “点”菜单
    elif op and op.bl_rna.identifier == "GREASE_PENCIL_OT_extrude_move":
        layout = self.layout
        layout.separator()
        layout.operator("call.add_to_switcher_menu", text="\"挤出\"⟶Switcher", icon='EVENT_E').action = 'button.action_greasepenciledit_extrude_move'










def greasepenciledit_layer_add_menu_to_switcher(self, context):
    show_switcher = bpy.context.preferences.addons[ADDON_NAME].preferences.to_show_to_switcher
    if not show_switcher:
        return
    self.layout.separator()
    self.layout.operator("call.add_to_switcher_menu", text="\"活动层(菜单)\"⟶Switcher", icon='PRESET').action = 'button.action_greasepenciledit_layer_active_menu'

def greasepenciledit_animation_menu_to_switcher(self, context):
    show_switcher = bpy.context.preferences.addons[ADDON_NAME].preferences.to_show_to_switcher
    if not show_switcher:
        return
    self.layout.separator()
    self.layout.operator("call.add_to_switcher_menu", text="\"动画(菜单)\"⟶Switcher", icon='PRESET').action = 'button.action_greasepenciledit_animation_menu'

def greasepenciledit_cleanup_menu_to_switcher(self, context):
    show_switcher = bpy.context.preferences.addons[ADDON_NAME].preferences.to_show_to_switcher
    if not show_switcher:
        return
    self.layout.separator()
    self.layout.operator("call.add_to_switcher_menu", text="\"清理(菜单)\"⟶Switcher", icon='PRESET').action = 'button.action_greasepenciledit_cleanup_menu'


def register():
    bpy.types.UI_MT_button_context_menu.append(draw_add_to_switcher_greasepenciledit)
    if bpy.app.version >= (4, 3, 0):
        bpy.types.GREASE_PENCIL_MT_layer_active.append(greasepenciledit_layer_add_menu_to_switcher)
        bpy.types.VIEW3D_MT_edit_greasepencil_animation.append(greasepenciledit_animation_menu_to_switcher)
        bpy.types.VIEW3D_MT_edit_greasepencil_cleanup.append(greasepenciledit_cleanup_menu_to_switcher)

def unregister():
    if bpy.app.version >= (4, 3, 0):
        bpy.types.VIEW3D_MT_edit_greasepencil_cleanup.remove(greasepenciledit_cleanup_menu_to_switcher)
        bpy.types.VIEW3D_MT_edit_greasepencil_animation.remove(greasepenciledit_animation_menu_to_switcher)
        bpy.types.GREASE_PENCIL_MT_layer_active.remove(greasepenciledit_layer_add_menu_to_switcher)
    bpy.types.UI_MT_button_context_menu.remove(draw_add_to_switcher_greasepenciledit)
