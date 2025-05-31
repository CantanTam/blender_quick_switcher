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
        layout.operator("call.add_to_switcher_menu", text="\"按类型全选(菜单)\"添加到Switcher", icon='PRESET').action = 'button.action_object_select_select_by_type_menu'

    elif op and op.bl_rna.identifier == "OBJECT_OT_select_camera":
        layout = self.layout
        layout.separator()
        layout.operator("call.add_to_switcher_menu", text="\"选择活动摄像机\"添加到Switcher", icon='OUTLINER_OB_CAMERA').action = 'object.select_camera'
    
    elif op and op.bl_rna.identifier == "OBJECT_OT_randomize_transform":
        layout = self.layout
        layout.separator()
        layout.operator("call.add_to_switcher_menu", text="\"随机变换\"添加到Switcher", icon='PLUS').action = 'button.action_object_randomize_transform'
    
    elif op and op.bl_rna.identifier == "OBJECT_OT_align":
        layout = self.layout
        layout.separator()
        layout.operator("call.add_to_switcher_menu", text="\"对齐物体\"添加到Switcher", icon='PLUS').action = 'button.action_object_transform_object_align'
    
    elif op and op.bl_rna.identifier == "OBJECT_OT_origin_set":
        layout = self.layout
        layout.separator()
        layout.operator("call.add_to_switcher_menu", text="\"设置原点(菜单)\"添加到Switcher", icon='PRESET').action = 'button.action_call_object_origin_set_menu'
        layout.separator()
        layout.operator("call.add_to_switcher_menu", text="\"几何中心->原点\"添加到Switcher", icon='PLUS').action = 'button.action_object_origin_set_geometry_origin'
        layout.operator("call.add_to_switcher_menu", text="\"原点->几何中心\"添加到Switcher", icon='PLUS').action = 'button.action_object_origin_set_origin_geometry'
        layout.operator("call.add_to_switcher_menu", text="\"原点->3D 游标\"添加到Switcher", icon='PLUS').action = 'button.action_object_origin_set_origin_cursor'
        layout.operator("call.add_to_switcher_menu", text="\"原点->质心(表面)\"添加到Switcher", icon='PLUS').action = 'button.action_object_origin_set_origin_center_of_mass'
        layout.operator("call.add_to_switcher_menu", text="\"原点->质心(体积)\"添加到Switcher", icon='PLUS').action = 'button.action_object_origin_set_origin_center_of_volume'

    elif op and op.bl_rna.identifier == "OBJECT_OT_duplicate_move_linked":
        layout = self.layout
        layout.separator()
        layout.operator("call.add_to_switcher_menu", text="\"关联复制\"添加到Switcher", icon='DUPLICATE').action = 'button.action_global_duplicate_move_linked'
    


def object_select_moreless_menu_to_switcher(self, context):
    show_switcher = bpy.context.preferences.addons[ADDON_NAME].preferences.to_show_to_switcher
    if not show_switcher:
        return
    self.layout.separator()
    self.layout.operator("call.add_to_switcher_menu", text="\"加选/减选(菜单)\"添加到Switcher", icon='FORCE_CHARGE').action = 'button.action_call_global_select_more_or_less_menu'
    self.layout.operator("call.add_to_switcher_menu", text="\"父级/子级(菜单)\"添加到Switcher", icon='ORIENTATION_PARENT').action = 'button.action_global_select_select_parent_or_child'



def register():
    bpy.types.UI_MT_button_context_menu.append(draw_add_to_switcher_object)
    bpy.types.VIEW3D_MT_select_object_more_less.append(object_select_moreless_menu_to_switcher)

def unregister():
    bpy.types.VIEW3D_MT_select_object_more_less.remove(object_select_moreless_menu_to_switcher)
    bpy.types.UI_MT_button_context_menu.remove(draw_add_to_switcher_object)

