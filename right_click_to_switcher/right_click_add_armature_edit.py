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
        layout.operator("call.add_to_switcher_menu", text="\"父级/子级(菜单)\"⟶Switcher", icon='ORIENTATION_PARENT').action = 'action.global_select_select_parent_or_child'

    elif op and op.bl_rna.identifier == "ARMATURE_OT_select_linked":
        layout = self.layout
        layout.separator()
        layout.operator("call.add_to_switcher_menu", text="\"选择相连(菜单)\"⟶Switcher", icon='LINK_BLEND').action = 'action.armatureedit_select_select_linked'

    elif op and op.bl_rna.identifier == "ARMATURE_OT_select_similar":
        layout = self.layout
        layout.separator()
        layout.operator("call.add_to_switcher_menu", text="\"选择相似(菜单)\"⟶Switcher", icon='PRESET').action = 'action.armatureedit_select_similar'

    elif op and op.bl_rna.identifier == "ARMATURE_OT_align":
        layout = self.layout
        layout.separator()
        layout.operator("call.add_to_switcher_menu", text="\"对齐骨骼\"⟶Switcher", icon='PLUS').action = 'action.armatureedit_align'

    elif op and op.bl_rna.identifier == "ARMATURE_OT_extrude_move":
        layout = self.layout
        layout.separator()
        layout.operator("call.add_to_switcher_menu", text="\"挤出\"⟶Switcher", icon='EVENT_E').action = 'action.armatureedit_extrude_move'

    elif op and op.bl_rna.identifier == "ARMATURE_OT_fill":
        layout = self.layout
        layout.separator()
        layout.operator("call.add_to_switcher_menu", text="\"在关节间填充骨骼\"⟶Switcher", icon='EVENT_F').action = 'action.armatureedit_fill'

    elif op and op.bl_rna.identifier == "ARMATURE_OT_split":
        layout = self.layout
        layout.separator()
        layout.operator("call.add_to_switcher_menu", text="\"拆分\"⟶Switcher", icon='EVENT_Y').action = 'action.armatureedit_split'

    elif op and op.bl_rna.identifier == "ARMATURE_OT_separate":
        layout = self.layout
        layout.separator()
        layout.operator("call.add_to_switcher_menu", text="\"分离骨骼\"⟶Switcher", icon='EVENT_P').action = 'action.armatureedit_separate'

    elif op and op.bl_rna.identifier == "ARMATURE_OT_subdivide":
        layout = self.layout
        layout.separator()
        layout.operator("call.add_to_switcher_menu", text="\"细分\"⟶Switcher", icon='PLUS').action = 'action.armatureedit_subdivide'

    elif op and op.bl_rna.identifier == "ARMATURE_OT_switch_direction":
        layout = self.layout
        layout.separator()
        layout.operator("call.add_to_switcher_menu", text="\"切换方向\"⟶Switcher", icon='PLUS').action = 'action.armatureedit_switch_direction'

    elif op and op.bl_rna.identifier == "ARMATURE_OT_symmetrize":
        layout = self.layout
        layout.separator()
        layout.operator("call.add_to_switcher_menu", text="\"对称\"⟶Switcher", icon='PLUS').action = 'action.armatureedit_symmetrize'

    elif op and op.bl_rna.identifier == "ARMATURE_OT_armature_layers":
        layout = self.layout
        layout.separator()
        layout.operator("call.add_to_switcher_menu", text="\"更改骨架层\"⟶Switcher", icon='PRESET').action = 'action.armatureedit_armature_layers'

    elif op and op.bl_rna.identifier == "ARMATURE_OT_bone_layers":
        layout = self.layout
        layout.separator()
        layout.operator("call.add_to_switcher_menu", text="\"更改骨骼层\"⟶Switcher", icon='PRESET').action = 'action.armatureedit_bone_layers'

    elif op and op.bl_rna.identifier == "ARMATURE_OT_parent_set":
        layout = self.layout
        layout.separator()
        layout.operator("call.add_to_switcher_menu", text="\"生成父级\"⟶Switcher", icon='PRESET').action = 'action.armatureedit_parent_set'

    elif op and op.bl_rna.identifier == "ARMATURE_OT_parent_clear":
        layout = self.layout
        layout.separator()
        layout.operator("call.add_to_switcher_menu", text="\"清空父级\"⟶Switcher", icon='PRESET').action = 'action.armatureedit_parent_clear'
    # 4.3 版本有效
    elif op and op.bl_rna.identifier == "ARMATURE_OT_move_to_collection":
        layout = self.layout
        layout.separator()
        layout.operator("call.add_to_switcher_menu", text="\"移动到集合\"⟶Switcher", icon='PRESET').action = 'action.armatureedit_move_to_collection'

    elif op and op.bl_rna.identifier == "ARMATURE_OT_assign_to_collection":
        layout = self.layout
        layout.separator()
        layout.operator("call.add_to_switcher_menu", text="\"指定到集合\"⟶Switcher", icon='PRESET').action = 'action.armatureedit_assign_to_collection'

    elif op and op.bl_rna.identifier == "ARMATURE_OT_collection_show_all":
        layout = self.layout
        layout.separator()
        layout.operator("call.add_to_switcher_menu", text="\"显示全部\"⟶Switcher", icon='HIDE_OFF').action = 'action.armatureedit_collection_show_all'

    elif op and op.bl_rna.identifier == "ARMATURE_OT_collection_create_and_assign":
        layout = self.layout
        layout.separator()
        layout.operator("call.add_to_switcher_menu", text="\"指定到新集合\"⟶Switcher", icon='PLUS').action = 'action.armatureedit_collection_create_and_assign'


def armatureedit_armature_roll_menu_to_switcher(self, context):
    show_switcher = bpy.context.preferences.addons[ADDON_NAME].preferences.to_show_to_switcher
    if not show_switcher:
        return
    self.layout.separator()
    self.layout.operator("call.add_to_switcher_menu", text="\"骨骼扭转(菜单)\"⟶Switcher", icon='PRESET').action = 'action.armatureedit_armature_roll_menu'
    self.layout.operator("call.add_to_switcher_menu", text="\"重算扭转\"⟶Switcher", icon='PRESET').action = 'action.armatureedit_armature_calculate_roll_menu'
    self.layout.operator("call.add_to_switcher_menu", text="\"设置扭转\"⟶Switcher", icon='PLUS').action = 'action.armatureedit_transform_bone_roll'
    self.layout.operator("call.add_to_switcher_menu", text="\"清除扭转\"⟶Switcher", icon='PLUS').action = 'action.armatureedit_roll_clear'

def armatureedit_name_roll_menu_to_switcher(self, context):
    show_switcher = bpy.context.preferences.addons[ADDON_NAME].preferences.to_show_to_switcher
    if not show_switcher:
        return
    self.layout.separator()
    self.layout.operator("call.add_to_switcher_menu", text="\"名称(菜单)\"⟶Switcher", icon='PRESET').action = 'action.armatureedit_name_menu'

def armatureedit_armature_parent_menu_to_switcher(self, context):
    show_switcher = bpy.context.preferences.addons[ADDON_NAME].preferences.to_show_to_switcher
    if not show_switcher:
        return
    self.layout.separator()
    self.layout.operator("call.add_to_switcher_menu", text="\"父级(菜单)\"⟶Switcher", icon='PRESET').action = 'action.armatureedit_edit_armature_parent'

def armatureedit_bone_options_toggle_menu_to_switcher(self, context):
    show_switcher = bpy.context.preferences.addons[ADDON_NAME].preferences.to_show_to_switcher
    if not show_switcher:
        return
    self.layout.separator()
    self.layout.operator("call.add_to_switcher_menu", text="\"骨骼设置(菜单)\"⟶Switcher", icon='PRESET').action = 'action.armatureedit_bone_options_toggle'

def armatureedit_bone_collections_menu_to_switcher(self, context):
    show_switcher = bpy.context.preferences.addons[ADDON_NAME].preferences.to_show_to_switcher
    if not show_switcher:
        return
    self.layout.separator()
    self.layout.operator("call.add_to_switcher_menu", text="\"骨骼集合(菜单)\"⟶Switcher", icon='PRESET').action = 'action.armatureedit_bone_collections'




def register():
    bpy.types.UI_MT_button_context_menu.append(draw_add_to_switcher_armature_edit)
    bpy.types.VIEW3D_MT_edit_armature_roll.append(armatureedit_armature_roll_menu_to_switcher)
    bpy.types.VIEW3D_MT_edit_armature_names.append(armatureedit_name_roll_menu_to_switcher)
    bpy.types.VIEW3D_MT_edit_armature_parent.append(armatureedit_armature_parent_menu_to_switcher)
    bpy.types.VIEW3D_MT_bone_options_toggle.append(armatureedit_bone_options_toggle_menu_to_switcher)
    if bpy.app.version >= (4, 3, 0):
        bpy.types.VIEW3D_MT_bone_collections.append(armatureedit_bone_collections_menu_to_switcher)

def unregister():
    if bpy.app.version >= (4, 3, 0):
        bpy.types.VIEW3D_MT_bone_collections.remove(armatureedit_bone_collections_menu_to_switcher)
    bpy.types.VIEW3D_MT_bone_options_toggle.remove(armatureedit_bone_options_toggle_menu_to_switcher)
    bpy.types.VIEW3D_MT_edit_armature_parent.remove(armatureedit_armature_parent_menu_to_switcher)
    bpy.types.VIEW3D_MT_edit_armature_names.remove(armatureedit_name_roll_menu_to_switcher)
    bpy.types.VIEW3D_MT_edit_armature_roll.remove(armatureedit_armature_roll_menu_to_switcher)
    bpy.types.UI_MT_button_context_menu.remove(draw_add_to_switcher_armature_edit)