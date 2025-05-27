import bpy
from .. import ADDON_NAME

def draw_add_to_switcher_armature_pose(self, context):
    show_switcher = bpy.context.preferences.addons[ADDON_NAME].preferences.to_show_to_switcher
    if not show_switcher:
        return
    
    op = getattr(context, "operator", None) or getattr(context, "button_operator", None)

    if op and op.bl_rna.identifier == "POSE_OT_select_hierarchy":   #添加其它选项后删除
        layout = self.layout
        layout.separator()
        layout.operator("call.add_to_switcher_menu", text="\"父级/子级(菜单)\"添加到Switcher", icon='ORIENTATION_PARENT').action = 'button.action_global_select_select_parent_or_child'






def global_select_pose_moreless_menu_to_switcher(self, context):
    show_switcher = bpy.context.preferences.addons[ADDON_NAME].preferences.to_show_to_switcher
    if not show_switcher:
        return
    self.layout.separator()
    self.layout.operator("call.add_to_switcher_menu", text="\"父级/子级(菜单)\"添加到Switcher", icon='ORIENTATION_PARENT').action = 'button.action_global_select_select_parent_or_child'




def register():
    bpy.types.UI_MT_button_context_menu.append(draw_add_to_switcher_armature_pose)
    bpy.types.VIEW3D_MT_select_pose_more_less.append(global_select_pose_moreless_menu_to_switcher)

def unregister():
    bpy.types.VIEW3D_MT_select_pose_more_less.remove(global_select_pose_moreless_menu_to_switcher)
    bpy.types.UI_MT_button_context_menu.remove(draw_add_to_switcher_armature_pose)