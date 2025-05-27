import bpy
from .. import ADDON_NAME

def draw_add_to_switcher_global_select(self, context):

    show_switcher = bpy.context.preferences.addons[ADDON_NAME].preferences.to_show_to_switcher
    if not show_switcher:
        return
    
    op = getattr(context, "operator", None) or getattr(context, "button_operator", None)

    if op and op.bl_rna.identifier in {
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

    elif op and op.bl_rna.identifier == "MESH_OT_select_axis":
        layout = self.layout
        layout.separator()
        layout.operator("call.add_to_switcher_menu", text="\"活动项的同侧\"添加到Switcher", icon='RADIOBUT_OFF').action = 'button.action_mesh_select_axis'
        layout.operator("call.add_to_switcher_menu", text="添加分隔符到Switcher", icon='REMOVE').action = 'SEPARATOR'




def global_select_meshedit_select_linked_menu_to_switcher(self, context):
    show_switcher = bpy.context.preferences.addons[ADDON_NAME].preferences.to_show_to_switcher
    if not show_switcher:
        return
    self.layout.separator()
    self.layout.operator("call.add_to_switcher_menu", text="\"选择相连(菜单)\"添加到Switcher", icon='LINK_BLEND').action = 'button.action_select_select_linked'
    self.layout.operator("call.add_to_switcher_menu", text="添加分隔符到Switcher", icon='REMOVE').action = 'SEPARATOR'

def global_select_select_similar_menu_to_switcher(self, context):
    show_switcher = bpy.context.preferences.addons[ADDON_NAME].preferences.to_show_to_switcher
    if not show_switcher:
        return
    self.layout.separator()
    self.layout.operator("call.add_to_switcher_menu", text="\"选择相似(菜单)\"添加到Switcher", icon='PRESET').action = 'button.action_select_select_similar'
    self.layout.operator("call.add_to_switcher_menu", text="添加分隔符到Switcher", icon='REMOVE').action = 'SEPARATOR'

def global_select_mesh_select_by_trait_menu_to_switcher(self, context):
    show_switcher = bpy.context.preferences.addons[ADDON_NAME].preferences.to_show_to_switcher
    if not show_switcher:
        return
    self.layout.separator()
    self.layout.operator("call.add_to_switcher_menu", text="\"按特征全选(菜单)\"添加到Switcher", icon='PRESET').action = 'button.action_mesh_call_select_by_trait'
    self.layout.operator("call.add_to_switcher_menu", text="添加分隔符到Switcher", icon='REMOVE').action = 'SEPARATOR'

def global_select_mesh_select_loops_menu_to_switcher(self, context):
    show_switcher = bpy.context.preferences.addons[ADDON_NAME].preferences.to_show_to_switcher
    if not show_switcher:
        return
    self.layout.separator()
    self.layout.operator("call.add_to_switcher_menu", text="\"选择循环(菜单)\"添加到Switcher", icon='PRESET').action = 'button.action_call_mesh_select_loops'
    self.layout.operator("call.add_to_switcher_menu", text="添加分隔符到Switcher", icon='REMOVE').action = 'SEPARATOR'



def register():
    bpy.types.UI_MT_button_context_menu.append(draw_add_to_switcher_global_select)
    bpy.types.VIEW3D_MT_edit_mesh_select_linked.append(global_select_meshedit_select_linked_menu_to_switcher)
    bpy.types.VIEW3D_MT_edit_mesh_select_similar.append(global_select_select_similar_menu_to_switcher)
    bpy.types.VIEW3D_MT_edit_mesh_select_by_trait.append(global_select_mesh_select_by_trait_menu_to_switcher)
    bpy.types.VIEW3D_MT_edit_mesh_select_loops.append(global_select_mesh_select_loops_menu_to_switcher)


def unregister():
    bpy.types.VIEW3D_MT_edit_mesh_select_loops.remove(global_select_mesh_select_loops_menu_to_switcher)
    bpy.types.VIEW3D_MT_edit_mesh_select_by_trait.remove(global_select_mesh_select_by_trait_menu_to_switcher)
    bpy.types.VIEW3D_MT_edit_mesh_select_similar.remove(global_select_select_similar_menu_to_switcher)
    bpy.types.VIEW3D_MT_edit_mesh_select_linked.remove(global_select_meshedit_select_linked_menu_to_switcher)
    bpy.types.UI_MT_button_context_menu.remove(draw_add_to_switcher_global_select)
