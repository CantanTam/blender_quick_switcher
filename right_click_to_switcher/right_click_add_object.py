import bpy
from .. import ADDON_NAME

def draw_add_to_switcher_object(self, context):
    show_switcher = bpy.context.preferences.addons[ADDON_NAME].preferences.to_show_to_switcher
    if not show_switcher:
        return
    
    op = getattr(context, "operator", None) or getattr(context, "button_operator", None)

    if op and op.bl_rna.identifier == "OBJECT_OT_select_by_type":
        layout = self.layout
        layout.separator()
        layout.operator("call.add_to_switcher_menu", text="\"按类型全选(菜单)\"⟶Switcher", icon='PRESET').action = 'button.action_object_select_select_by_type_menu'

    elif op and op.bl_rna.identifier == "OBJECT_OT_select_camera":
        layout = self.layout
        layout.separator()
        layout.operator("call.add_to_switcher_menu", text="\"选择活动摄像机\"⟶Switcher", icon='OUTLINER_OB_CAMERA').action = 'object.select_camera'
    
    elif op and op.bl_rna.identifier == "OBJECT_OT_randomize_transform":
        layout = self.layout
        layout.separator()
        layout.operator("call.add_to_switcher_menu", text="\"随机变换\"⟶Switcher", icon='PLUS').action = 'button.action_object_randomize_transform'
    
    elif op and op.bl_rna.identifier == "OBJECT_OT_align":
        layout = self.layout
        layout.separator()
        layout.operator("call.add_to_switcher_menu", text="\"对齐物体\"⟶Switcher", icon='PLUS').action = 'button.action_object_transform_object_align'
    
    elif op and op.bl_rna.identifier == "OBJECT_OT_origin_set":
        layout = self.layout
        layout.separator()
        layout.operator("call.add_to_switcher_menu", text="\"设置原点(菜单)\"⟶Switcher", icon='PRESET').action = 'button.action_call_object_origin_set_menu'
        layout.separator()
        layout.operator("call.add_to_switcher_menu", text="\"几何中心->原点\"⟶Switcher", icon='PLUS').action = 'button.action_object_origin_set_geometry_origin'
        layout.operator("call.add_to_switcher_menu", text="\"原点->几何中心\"⟶Switcher", icon='PLUS').action = 'button.action_object_origin_set_origin_geometry'
        layout.operator("call.add_to_switcher_menu", text="\"原点->3D 游标\"⟶Switcher", icon='PLUS').action = 'button.action_object_origin_set_origin_cursor'
        layout.operator("call.add_to_switcher_menu", text="\"原点->质心(表面)\"⟶Switcher", icon='PLUS').action = 'button.action_object_origin_set_origin_center_of_mass'
        layout.operator("call.add_to_switcher_menu", text="\"原点->质心(体积)\"⟶Switcher", icon='PLUS').action = 'button.action_object_origin_set_origin_center_of_volume'

    elif op and op.bl_rna.identifier == "OBJECT_OT_duplicate_move_linked":
        layout = self.layout
        layout.separator()
        layout.operator("call.add_to_switcher_menu", text="\"关联复制\"⟶Switcher", icon='DUPLICATE').action = 'button.action_object_duplicate_move_linked'
    
    elif op and op.bl_rna.identifier == "OBJECT_OT_join":
        layout = self.layout
        layout.separator()
        layout.operator("call.add_to_switcher_menu", text="\"合并\"⟶Switcher", icon='PLUS').action = 'button.action_object_join'
    
    elif op and op.bl_rna.identifier == "ASSET_OT_mark":
        layout = self.layout
        layout.separator()
        layout.operator("call.add_to_switcher_menu", text="\"标记为资产\"⟶Switcher", icon='PLUS').action = 'button.action_object_asset_mark'
    
    elif op and op.bl_rna.identifier == "ASSET_OT_clear":
        layout = self.layout
        layout.separator()
        layout.operator("call.add_to_switcher_menu", text="\"清理资产\"⟶Switcher", icon='PLUS').action = 'button.action_object_asset_clear_fake_user_false'
        layout.operator("call.add_to_switcher_menu", text="\"清理资产(设置伪用户)\"⟶Switcher", icon='PLUS').action = 'button.action_object_asset_clear_fake_user_true'

    elif op and op.bl_rna.identifier == "OBJECT_OT_move_to_collection":
        layout = self.layout
        layout.separator()
        layout.operator("call.add_to_switcher_menu", text="\"移动到集合\"⟶Switcher", icon='PLUS').action = 'button.action_object_move_to_collection'

    elif op and op.bl_rna.identifier == "OBJECT_OT_link_to_collection":
        layout = self.layout
        layout.separator()
        layout.operator("call.add_to_switcher_menu", text="\"关联至集合\"⟶Switcher", icon='PLUS').action = 'button.action_object_link_to_collection'

    elif op and op.bl_rna.identifier == "COLLECTION_OT_create":
        layout = self.layout
        layout.separator()
        layout.operator("call.add_to_switcher_menu", text="\"创建新集合\"⟶Switcher", icon='PLUS').action = 'button.action_object_collection_create'

    elif op and op.bl_rna.identifier == "COLLECTION_OT_objects_remove":
        layout = self.layout
        layout.separator()
        layout.operator("call.add_to_switcher_menu", text="\"从集合中移除\"⟶Switcher", icon='PLUS').action = 'button.action_object_collection_objects_remove'

    elif op and op.bl_rna.identifier == "COLLECTION_OT_objects_remove_all":
        layout = self.layout
        layout.separator()
        layout.operator("call.add_to_switcher_menu", text="\"从所有集合中移除\"⟶Switcher", icon='PLUS').action = 'button.action_object_collection_objects_remove_all'

    elif op and op.bl_rna.identifier == "COLLECTION_OT_objects_add_active":
        layout = self.layout
        layout.separator()
        layout.operator("call.add_to_switcher_menu", text="\"将选中项添加到活动集合中\"⟶Switcher", icon='PLUS').action = 'button.action_object_collection_objects_add_active'

    elif op and op.bl_rna.identifier == "COLLECTION_OT_objects_remove_active":
        layout = self.layout
        layout.separator()
        layout.operator("call.add_to_switcher_menu", text="\"从活动集合中移除所选\"⟶Switcher", icon='PLUS').action = 'button.action_object_collection_objects_remove_active'

    elif op and op.bl_rna.identifier == "OBJECT_OT_constraint_add_with_targets":
        layout = self.layout
        layout.separator()
        layout.operator("call.add_to_switcher_menu", text="\"添加约束(预指定目标物体)\"⟶Switcher", icon='PLUS').action = 'button.action_object_constraint_add_with_targets'

    elif op and op.bl_rna.identifier == "OBJECT_OT_constraints_copy":
        layout = self.layout
        layout.separator()
        layout.operator("call.add_to_switcher_menu", text="\"将约束复制到当前所选\"⟶Switcher", icon='PLUS').action = 'button.action_object_constraint_copy'

    elif op and op.bl_rna.identifier == "OBJECT_OT_constraints_clear":
        layout = self.layout
        layout.separator()
        layout.operator("call.add_to_switcher_menu", text="\"清除物体约束\"⟶Switcher", icon='PLUS').action = 'button.action_object_constraint_clear'





















def object_select_moreless_menu_to_switcher(self, context):
    show_switcher = bpy.context.preferences.addons[ADDON_NAME].preferences.to_show_to_switcher
    if not show_switcher:
        return
    self.layout.separator()
    self.layout.operator("call.add_to_switcher_menu", text="\"加选/减选(菜单)\"⟶Switcher", icon='FORCE_CHARGE').action = 'button.action_call_global_select_more_or_less_menu'
    self.layout.operator("call.add_to_switcher_menu", text="\"父级/子级(菜单)\"⟶Switcher", icon='ORIENTATION_PARENT').action = 'button.action_global_select_select_parent_or_child'

def object_asset_menu_to_switcher(self, context):
    show_switcher = bpy.context.preferences.addons[ADDON_NAME].preferences.to_show_to_switcher
    if not show_switcher:
        return
    self.layout.separator()
    self.layout.operator("call.add_to_switcher_menu", text="\"资源(菜单)\"⟶Switcher", icon='PRESET').action = 'button.action_object_asset_menu'

def object_collection_menu_to_switcher(self, context):
    show_switcher = bpy.context.preferences.addons[ADDON_NAME].preferences.to_show_to_switcher
    if not show_switcher:
        return
    self.layout.separator()
    self.layout.operator("call.add_to_switcher_menu", text="\"集合(菜单)\"⟶Switcher", icon='PRESET').action = 'button.action_object_collection_menu'

def object_relations_menu_to_switcher(self, context):
    show_switcher = bpy.context.preferences.addons[ADDON_NAME].preferences.to_show_to_switcher
    if not show_switcher:
        return
    self.layout.separator()
    self.layout.operator("call.add_to_switcher_menu", text="\"关系(菜单)\"⟶Switcher", icon='PRESET').action = 'button.action_object_relations_menu'

def object_liboverride_menu_to_switcher(self, context):
    show_switcher = bpy.context.preferences.addons[ADDON_NAME].preferences.to_show_to_switcher
    if not show_switcher:
        return
    self.layout.separator()
    self.layout.operator("call.add_to_switcher_menu", text="\"库重写(菜单)\"⟶Switcher", icon='PRESET').action = 'button.action_object_liboverride'

def object_constraints_menu_to_switcher(self, context):
    show_switcher = bpy.context.preferences.addons[ADDON_NAME].preferences.to_show_to_switcher
    if not show_switcher:
        return
    self.layout.separator()
    self.layout.operator("call.add_to_switcher_menu", text="\"约束(菜单)\"⟶Switcher", icon='PRESET').action = 'button.action_call_object_constraints_menu'


def register():
    bpy.types.UI_MT_button_context_menu.append(draw_add_to_switcher_object)
    bpy.types.VIEW3D_MT_select_object_more_less.append(object_select_moreless_menu_to_switcher)
    bpy.types.VIEW3D_MT_object_asset.append(object_asset_menu_to_switcher)
    bpy.types.VIEW3D_MT_object_collection.append(object_collection_menu_to_switcher)
    bpy.types.VIEW3D_MT_object_relations.append(object_relations_menu_to_switcher)
    bpy.types.VIEW3D_MT_object_liboverride.append(object_liboverride_menu_to_switcher)
    bpy.types.VIEW3D_MT_object_constraints.append(object_constraints_menu_to_switcher)

def unregister():
    bpy.types.VIEW3D_MT_object_constraints.remove(object_constraints_menu_to_switcher)
    bpy.types.VIEW3D_MT_object_liboverride.remove(object_liboverride_menu_to_switcher)
    bpy.types.VIEW3D_MT_object_relations.remove(object_relations_menu_to_switcher)
    bpy.types.VIEW3D_MT_object_collection.remove(object_collection_menu_to_switcher)
    bpy.types.VIEW3D_MT_object_asset.remove(object_asset_menu_to_switcher)
    bpy.types.VIEW3D_MT_select_object_more_less.remove(object_select_moreless_menu_to_switcher)
    bpy.types.UI_MT_button_context_menu.remove(draw_add_to_switcher_object)

