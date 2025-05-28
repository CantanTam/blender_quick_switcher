import bpy
from .. import ADDON_NAME

def draw_add_to_switcher_armature_edit(self, context):
    show_switcher = bpy.context.preferences.addons[ADDON_NAME].preferences.to_show_to_switcher
    if not show_switcher:
        return
    
    op = getattr(context, "operator", None) or getattr(context, "button_operator", None)

    if op and op.bl_rna.identifier == "ARMATURE_OT_select_hierarchy":
        layout = self.layout
        layout.separator()
        layout.operator("call.add_to_switcher_menu", text="\"父级/子级(菜单)\"添加到Switcher", icon='ORIENTATION_PARENT').action = 'button.action_global_select_select_parent_or_child'

    elif op and op.bl_rna.identifier == "ARMATURE_OT_select_linked":
        layout = self.layout
        layout.separator()
        layout.operator("call.add_to_switcher_menu", text="\"选择相连(菜单)\"添加到Switcher", icon='LINK_BLEND').action = 'button.action_armatureedit_select_select_linked'







def register():
    bpy.types.UI_MT_button_context_menu.append(draw_add_to_switcher_armature_edit)

def unregister():
    bpy.types.UI_MT_button_context_menu.remove(draw_add_to_switcher_armature_edit)