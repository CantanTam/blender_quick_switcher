import bpy
from .. import ADDON_NAME

def draw_add_to_switcher_global_view(self, context):

    show_switcher = bpy.context.preferences.addons[ADDON_NAME].preferences.to_show_to_switcher
    if not show_switcher:
        return
    
    op = getattr(context, "operator", None) or getattr(context, "button_operator", None)
    # 检查右键对象是否为视图操作
    if op and op.bl_rna.identifier == "VIEW3D_OT_view_selected":
        layout = self.layout
        layout.separator()
        layout.operator("call.add_to_switcher_menu", text="\"框显所选\"添加到Switcher", icon='DOT').action = 'button.action_global_view_selected'
        
    elif op and op.bl_rna.identifier == "VIEW3D_OT_view_all":
        layout = self.layout
        layout.separator()
        layout.operator("call.add_to_switcher_menu", text="\"框显全部\"添加到Switcher", icon='HOME').action = 'button.action_global_view_all'
        
    elif op and op.bl_rna.identifier == "VIEW3D_OT_localview":
        layout = self.layout
        layout.separator()
        layout.operator("call.add_to_switcher_menu", text="\"局部视图\"添加到Switcher", icon='PLUS').action = 'button.action_global_localview'
        
    elif op and op.bl_rna.identifier == "VIEW3D_OT_localview_remove_from":
        layout = self.layout
        layout.separator()
        layout.operator("call.add_to_switcher_menu", text="\"从局部视图中移除\"添加到Switcher", icon='PLUS').action = 'view3d.localview_remove_from'
        
    elif op and op.bl_rna.identifier == "VIEW3D_OT_object_as_camera":
        layout = self.layout
        layout.separator()
        layout.operator("call.add_to_switcher_menu", text="\"设置活动物体为摄像机\"添加到Switcher", icon='OUTLINER_OB_CAMERA').action = 'button.action_global_object_as_camera'
        
    elif op and op.bl_rna.identifier == "VIEW3D_OT_view_center_camera":
        layout = self.layout
        layout.separator()
        layout.operator("call.add_to_switcher_menu", text="\"摄像机边界框\"添加到Switcher", icon='SELECT_SET').action = 'button.action_global_view_center_camera'

    elif op and op.bl_rna.identifier == "VIEW3D_OT_zoom_border":
        layout = self.layout
        layout.separator()
        layout.operator("call.add_to_switcher_menu", text="\"框选放大\"添加到Switcher", icon='SELECT_SET').action = 'button.action_global_zoom_border'

    elif op and op.bl_rna.identifier == "VIEW3D_OT_zoom_camera_1_to_1":
        layout = self.layout
        layout.separator()
        layout.operator("call.add_to_switcher_menu", text="\"1:1缩放摄像机视图\"添加到Switcher", icon='PLUS').action = 'button.action_zoom_camera_1_to_1'

    elif op and op.bl_rna.identifier == "VIEW3D_OT_fly":
        layout = self.layout
        layout.separator()
        layout.operator("call.add_to_switcher_menu", text="\"飞行漫游模式\"添加到Switcher", icon='PLUS').action = 'button.action_global_fly'

    elif op and op.bl_rna.identifier == "VIEW3D_OT_walk":
        layout = self.layout
        layout.separator()
        layout.operator("call.add_to_switcher_menu", text="\"行走漫步\"添加到Switcher", icon='PLUS').action = 'button.action_global_walk'

    elif op and op.bl_rna.identifier == "RENDER_OT_opengl":
        layout = self.layout
        layout.separator()
        layout.operator("call.add_to_switcher_menu", text="\"视图渲染图像\"添加到Switcher", icon='RENDER_STILL').action = 'button.action_global_render_opengl'
        layout.operator("call.add_to_switcher_menu", text="\"视图渲染动画\"添加到Switcher", icon='RENDER_ANIMATION').action = 'button.action_global_render_opengl_animation'
        layout.operator("call.add_to_switcher_menu", text="\"视图渲染关键帧\"添加到Switcher", icon='RENDER_ANIMATION').action = 'button.action_global_render_opengl_keyframe'


def global_view_viewpoint_menu_to_switcher(self, context):
    show_switcher = bpy.context.preferences.addons[ADDON_NAME].preferences.to_show_to_switcher
    if not show_switcher:
        return
    self.layout.separator()
    self.layout.operator("call.add_to_switcher_menu", text="\"视图(菜单)\"添加到Switcher", icon='PRESET').action = 'button.action_global_call_view_viewpoint_menu'

def global_view_navigation_menu_to_switcher(self, context):
    show_switcher = bpy.context.preferences.addons[ADDON_NAME].preferences.to_show_to_switcher
    if not show_switcher:
        return
    self.layout.separator()
    self.layout.operator("call.add_to_switcher_menu", text="\"视图切换(菜单)\"添加到Switcher", icon='PRESET').action = 'button.action_global_call_view_navigation_menu'

def global_view_viewalign_menu_to_switcher(self, context):
    show_switcher = bpy.context.preferences.addons[ADDON_NAME].preferences.to_show_to_switcher
    if not show_switcher:
        return
    self.layout.separator()
    self.layout.operator("call.add_to_switcher_menu", text="\"对齐视图(菜单)\"添加到Switcher", icon='PRESET').action = 'button.action_global_call_view_align_menu'
    self.layout.operator("call.add_to_switcher_menu", text="\"活动摄像机对齐当前视角\"添加到Switcher", icon='OUTLINER_DATA_CAMERA').action = 'button.action_global_camera_to_view'
    self.layout.operator("call.add_to_switcher_menu", text="\"活动摄像机对齐选中的物体\"添加到Switcher", icon='OUTLINER_OB_CAMERA').action = 'button.action_global_camera_to_view_selected'
    self.layout.operator("call.add_to_switcher_menu", text="\"游标居中并查看全部\"添加到Switcher", icon='CURSOR').action = 'button.action_global_view_all_center_true'
    self.layout.operator("call.add_to_switcher_menu", text="\"视图中心对齐游标\"添加到Switcher", icon='PIVOT_CURSOR').action = 'button.action_global_view_center_cursor'
    self.layout.operator("call.add_to_switcher_menu", text="\"锁定/解锁视图\"添加到Switcher", icon='CON_CAMERASOLVER').action = 'button.action_global_lock_to_active_or_lock_clear'

def global_view_alignselected_menu_to_switcher(self, context):
    show_switcher = bpy.context.preferences.addons[ADDON_NAME].preferences.to_show_to_switcher
    if not show_switcher:
        return
    self.layout.separator()
    self.layout.operator("call.add_to_switcher_menu", text="\"视图对齐活动项(菜单)\"添加到Switcher", icon='PRESET').action = 'button.action_global_call_view_align_selected_menu'

def global_view_viewregions_menu_to_switcher(self, context):
    show_switcher = bpy.context.preferences.addons[ADDON_NAME].preferences.to_show_to_switcher
    if not show_switcher:
        return
    self.layout.separator()
    self.layout.operator("call.add_to_switcher_menu", text="\"视图框(菜单)\"添加到Switcher", icon='PRESET').action = 'button.action_global_call_view_regions_menu'
    self.layout.operator("call.add_to_switcher_menu", text="\"裁剪框\"添加到Switcher", icon='PLUS').action = 'button.action_global_clip_border'
    self.layout.operator("call.add_to_switcher_menu", text="\"开/关渲染框\"添加到Switcher", icon='PLUS').action = 'button.action_global_render_border'

def global_view_area_menu_to_switcher(self, context):
    show_switcher = bpy.context.preferences.addons[ADDON_NAME].preferences.to_show_to_switcher
    if not show_switcher:
        return
    self.layout.separator()
    self.layout.operator("call.add_to_switcher_menu", text="\"区域(菜单)\"添加到Switcher", icon='PRESET').action = 'button.action_global_area_menu'
    self.layout.operator("call.add_to_switcher_menu", text="\"四格视图\"添加到Switcher", icon='IMGDISPLAY').action = 'screen.region_quadview'
    self.layout.operator("call.add_to_switcher_menu", text="\"区域最大化\"添加到Switcher", icon='MOD_LENGTH').action = 'screen.screen_full_area'
    self.layout.operator("call.add_to_switcher_menu", text="\"全屏模式\"添加到Switcher", icon='FULLSCREEN_ENTER').action = 'button.action_global_screen_screen_full_area'

def register():
    bpy.types.UI_MT_button_context_menu.append(draw_add_to_switcher_global_view)
    bpy.types.VIEW3D_MT_view_viewpoint.append(global_view_viewpoint_menu_to_switcher)
    bpy.types.VIEW3D_MT_view_navigation.append(global_view_navigation_menu_to_switcher)
    bpy.types.VIEW3D_MT_view_align.append(global_view_viewalign_menu_to_switcher)
    bpy.types.VIEW3D_MT_view_align_selected.append(global_view_alignselected_menu_to_switcher)
    bpy.types.VIEW3D_MT_view_regions.append(global_view_viewregions_menu_to_switcher)
    bpy.types.INFO_MT_area.append(global_view_area_menu_to_switcher)


def unregister():
    bpy.types.INFO_MT_area.remove(global_view_area_menu_to_switcher)
    bpy.types.VIEW3D_MT_view_regions.remove(global_view_viewregions_menu_to_switcher)
    bpy.types.VIEW3D_MT_view_align_selected.remove(global_view_alignselected_menu_to_switcher)
    bpy.types.VIEW3D_MT_view_align.remove(global_view_viewalign_menu_to_switcher)
    bpy.types.VIEW3D_MT_view_navigation.remove(global_view_navigation_menu_to_switcher)
    bpy.types.VIEW3D_MT_view_viewpoint.remove(global_view_viewpoint_menu_to_switcher)
    bpy.types.UI_MT_button_context_menu.remove(draw_add_to_switcher_global_view)
