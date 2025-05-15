import bpy

def draw_add_to_switcher_global_view(self, context):
    show_switcher = bpy.context.preferences.addons[__package__].preferences.to_show_to_switcher
    if not show_switcher:
        return
    
    op = getattr(context, "operator", None) or getattr(context, "button_operator", None)
    # 检查右键对象是否为视图操作
    if op and op.bl_rna.identifier == "VIEW3D_OT_view_selected":
        layout = self.layout
        layout.separator()
        layout.operator("call.add_to_switcher_menu", text="\"框显所选\"添加到Switcher", icon='DOT').action = 'button.action_view3d_view_selected'
        layout.operator("call.add_to_switcher_menu", text="添加分隔符到Switcher", icon='REMOVE').action = 'SEPARATOR'
        
    elif op and op.bl_rna.identifier == "VIEW3D_OT_view_all":
        layout = self.layout
        layout.separator()
        layout.operator("call.add_to_switcher_menu", text="\"框显全部\"添加到Switcher", icon='HOME').action = 'button.action_view3d_view_all'
        layout.operator("call.add_to_switcher_menu", text="添加分隔符到Switcher", icon='REMOVE').action = 'SEPARATOR'
        
    elif op and op.bl_rna.identifier == "VIEW3D_OT_localview":
        layout = self.layout
        layout.separator()
        layout.operator("call.add_to_switcher_menu", text="\"局部视图\"添加到Switcher", icon='PLUS').action = 'button.action_view3d_localview'
        layout.operator("call.add_to_switcher_menu", text="添加分隔符到Switcher", icon='REMOVE').action = 'SEPARATOR'
        
    elif op and op.bl_rna.identifier == "VIEW3D_OT_localview_remove_from":
        layout = self.layout
        layout.separator()
        layout.operator("call.add_to_switcher_menu", text="\"从局部视图中移除\"添加到Switcher", icon='PLUS').action = 'view3d.localview_remove_from'
        layout.operator("call.add_to_switcher_menu", text="添加分隔符到Switcher", icon='REMOVE').action = 'SEPARATOR'
        
    elif op and op.bl_rna.identifier == "VIEW3D_OT_object_as_camera":
        layout = self.layout
        layout.separator()
        layout.operator("call.add_to_switcher_menu", text="\"设置活动物体为摄像机\"添加到Switcher", icon='OUTLINER_OB_CAMERA').action = 'button.action_view3d_object_as_camera'
        layout.operator("call.add_to_switcher_menu", text="添加分隔符到Switcher", icon='REMOVE').action = 'SEPARATOR'
        
    elif op and op.bl_rna.identifier == "VIEW3D_OT_view_center_camera":
        layout = self.layout
        layout.separator()
        layout.operator("call.add_to_switcher_menu", text="\"摄像机边界框\"添加到Switcher", icon='SELECT_SET').action = 'button.action_view3d_view_center_camera'
        layout.operator("call.add_to_switcher_menu", text="添加分隔符到Switcher", icon='REMOVE').action = 'SEPARATOR'

    elif op and op.bl_rna.identifier == "VIEW3D_OT_zoom_border":
        layout = self.layout
        layout.separator()
        layout.operator("call.add_to_switcher_menu", text="\"框选放大\"添加到Switcher", icon='SELECT_SET').action = 'button.action_view3d_zoom_border'
        layout.operator("call.add_to_switcher_menu", text="添加分隔符到Switcher", icon='REMOVE').action = 'SEPARATOR'

    elif op and op.bl_rna.identifier == "VIEW3D_OT_zoom_camera_1_to_1":
        layout = self.layout
        layout.separator()
        layout.operator("call.add_to_switcher_menu", text="\"1:1缩放摄像机视图\"添加到Switcher", icon='PLUS').action = 'button.action_zoom_camera_1_to_1'
        layout.operator("call.add_to_switcher_menu", text="添加分隔符到Switcher", icon='REMOVE').action = 'SEPARATOR'

    elif op and op.bl_rna.identifier == "VIEW3D_OT_fly":
        layout = self.layout
        layout.separator()
        layout.operator("call.add_to_switcher_menu", text="\"飞行漫游模式\"添加到Switcher", icon='PLUS').action = 'button.action_view3d_fly'
        layout.operator("call.add_to_switcher_menu", text="添加分隔符到Switcher", icon='REMOVE').action = 'SEPARATOR'

    elif op and op.bl_rna.identifier == "VIEW3D_OT_walk":
        layout = self.layout
        layout.separator()
        layout.operator("call.add_to_switcher_menu", text="\"行走漫步\"添加到Switcher", icon='PLUS').action = 'button.action_view3d_walk'
        layout.operator("call.add_to_switcher_menu", text="添加分隔符到Switcher", icon='REMOVE').action = 'SEPARATOR'




def global_view_viewpoint_menu_to_switcher(self, context):
    show_switcher = bpy.context.preferences.addons[__package__].preferences.to_show_to_switcher
    if not show_switcher:
        return
    self.layout.separator()
    self.layout.operator("call.add_to_switcher_menu", text="\"视图(菜单)\"添加到Switcher", icon='PRESET').action = 'button.action_view3d_call_view_viewpoint_menu'
    self.layout.operator("call.add_to_switcher_menu", text="添加分隔符到Switcher", icon='REMOVE').action = 'SEPARATOR'

def global_view_navigation_menu_to_switcher(self, context):
    show_switcher = bpy.context.preferences.addons[__package__].preferences.to_show_to_switcher
    if not show_switcher:
        return
    self.layout.separator()
    self.layout.operator("call.add_to_switcher_menu", text="\"视图切换(菜单)\"添加到Switcher", icon='PRESET').action = 'button.action_view3d_call_view_navigation_menu'
    self.layout.operator("call.add_to_switcher_menu", text="添加分隔符到Switcher", icon='REMOVE').action = 'SEPARATOR'

def global_view_viewalign_menu_to_switcher(self, context):
    show_switcher = bpy.context.preferences.addons[__package__].preferences.to_show_to_switcher
    if not show_switcher:
        return
    self.layout.separator()
    self.layout.operator("call.add_to_switcher_menu", text="\"对齐视图(菜单)\"添加到Switcher", icon='PRESET').action = 'button.action_view3d_call_view_align_menu'
    self.layout.operator("call.add_to_switcher_menu", text="\"活动摄像机对齐当前视角\"添加到Switcher", icon='OUTLINER_DATA_CAMERA').action = 'button.action_view3d_camera_to_view'
    self.layout.operator("call.add_to_switcher_menu", text="\"活动摄像机对齐选中的物体\"添加到Switcher", icon='OUTLINER_OB_CAMERA').action = 'button.action_view3d_camera_to_view_selected'
    self.layout.operator("call.add_to_switcher_menu", text="\"游标居中并查看全部\"添加到Switcher", icon='CURSOR').action = 'button.action_view3d_view_all_center_true'
    self.layout.operator("call.add_to_switcher_menu", text="\"视图中心对齐游标\"添加到Switcher", icon='PIVOT_CURSOR').action = 'button.action_view3d_view_center_cursor'
    self.layout.operator("call.add_to_switcher_menu", text="\"锁定/解锁视图\"添加到Switcher", icon='CON_CAMERASOLVER').action = 'button.action_view3d_lock_to_active_or_lock_clear'

    self.layout.operator("call.add_to_switcher_menu", text="添加分隔符到Switcher", icon='REMOVE').action = 'SEPARATOR'

def global_view_alignselected_menu_to_switcher(self, context):
    show_switcher = bpy.context.preferences.addons[__package__].preferences.to_show_to_switcher
    if not show_switcher:
        return
    self.layout.separator()
    self.layout.operator("call.add_to_switcher_menu", text="\"视图对齐活动项(菜单)\"添加到Switcher", icon='PRESET').action = 'button.action_view3d_call_view_align_selected_menu'
    self.layout.operator("call.add_to_switcher_menu", text="添加分隔符到Switcher", icon='REMOVE').action = 'SEPARATOR'



def register():
    bpy.types.UI_MT_button_context_menu.append(draw_add_to_switcher_global_view)
    bpy.types.VIEW3D_MT_view_viewpoint.append(global_view_viewpoint_menu_to_switcher)
    bpy.types.VIEW3D_MT_view_navigation.append(global_view_navigation_menu_to_switcher)
    bpy.types.VIEW3D_MT_view_align.append(global_view_viewalign_menu_to_switcher)
    bpy.types.VIEW3D_MT_view_align_selected.append(global_view_alignselected_menu_to_switcher)



def unregister():
    bpy.types.VIEW3D_MT_view_align_selected.remove(global_view_alignselected_menu_to_switcher)
    bpy.types.VIEW3D_MT_view_align.remove(global_view_viewalign_menu_to_switcher)
    bpy.types.VIEW3D_MT_view_navigation.remove(global_view_navigation_menu_to_switcher)
    bpy.types.VIEW3D_MT_view_viewpoint.remove(global_view_viewpoint_menu_to_switcher)
    bpy.types.UI_MT_button_context_menu.remove(draw_add_to_switcher_global_view)
