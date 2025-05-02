import bpy

# 唤出"视图“菜单类
class BUTTON_ACTION_OT_view3d_call_view_viewpoint_menu(bpy.types.Operator):
    bl_idname = "button.action_view3d_call_view_viewpoint_menu"
    bl_label = "视图"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.ops.wm.call_menu(name="VIEW3D_MT_view_viewpoint")
        return {'FINISHED'}

# 唤出“视图切换”菜单类
class BUTTON_ACTION_OT_view3d_call_view_navigation_menu(bpy.types.Operator):
    bl_idname = "button.action_view3d_call_view_navigation_menu"
    bl_label = "视图切换"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.ops.wm.call_menu(name="VIEW3D_MT_view_navigation")
        return {'FINISHED'}
    
# 自定义“框选放大”操作类
class BUTTON_ACTION_OT_view3d_zoom_border(bpy.types.Operator):
    bl_idname = "button.action_view3d_zoom_border"
    bl_label = "框选放大"
    bl_description = "快捷键 Shift B"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        bpy.ops.view3d.zoom_border('INVOKE_DEFAULT')
        return {'FINISHED'}
        
# 自定义“行走漫步”操作类
class BUTTON_ACTION_OT_view3d_walk(bpy.types.Operator):
    bl_idname = "button.action_view3d_walk"
    bl_label = "行走漫步"
    bl_description = "快捷键 Shift `"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        bpy.ops.view3d.view_lock_clear()
        bpy.ops.view3d.walk('INVOKE_DEFAULT')
        return {'FINISHED'}

# 平移视图操作类
class BUTTON_ACTION_OT_view_pan_left(bpy.types.Operator):
    bl_idname = "button.action_view_pan_left"
    bl_label = "左平移"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        return bpy.ops.view3d.view_pan('INVOKE_DEFAULT', type='PANLEFT')

class BUTTON_ACTION_OT_view_pan_right(bpy.types.Operator):
    bl_idname = "button.action_view_pan_right" 
    bl_label = "右平移"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        return bpy.ops.view3d.view_pan('INVOKE_DEFAULT', type='PANRIGHT')

class BUTTON_ACTION_OT_view_pan_up(bpy.types.Operator):
    bl_idname = "button.action_view_pan_up"
    bl_label = "上平移"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        return bpy.ops.view3d.view_pan('INVOKE_DEFAULT', type='PANUP')

class BUTTON_ACTION_OT_view_pan_down(bpy.types.Operator):
    bl_idname = "button.action_view_pan_down"
    bl_label = "下平移"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        return bpy.ops.view3d.view_pan('INVOKE_DEFAULT', type='PANDOWN')
    
# 自定义“锁定/解锁视图至活动物体”按钮类
class BUTTON_ACTION_OT_view3d_lock_to_active_or_lock_clear(bpy.types.Operator):
    bl_idname = "button.action_view3d_lock_to_active_or_lock_clear"
    bl_label = "锁定/解锁视图"
    bl_description = "锁定视图至活动物体/消除视图锁定"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        if bpy.context.space_data.lock_object is None:
            bpy.ops.view3d.view_lock_to_active()
        else:
            bpy.ops.view3d.view_lock_clear()
        return {'FINISHED'}

# 弹出“对齐视图”菜单
class BUTTON_ACTION_OT_view3d_call_view_align_menu(bpy.types.Operator):
    bl_idname = "button.action_view3d_call_view_align_menu"
    bl_label = "对齐视图"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.ops.wm.call_menu(name="VIEW3D_MT_view_align")
        return {'FINISHED'}
    
# 弹出“对齐视图”——游标居中并查看全部
class BUTTON_ACTION_OT_view3d_view_all_center_true(bpy.types.Operator):
    bl_idname = "button.action_view3d_view_all_center_true"
    bl_label = "游标居中并查看全部"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.ops.view3d.view_all(center=True)
        return {'FINISHED'}

# 自定义“视图框”菜单
class VIEW3D_MT_view_regions_menu(bpy.types.Menu):
    bl_label = ""
    bl_idname = "view3d.mt_view_regions_menu"

    def draw(self, context):
        layout = self.layout
        
        layout.operator("button.action_view3d_clip_border", text="裁剪框")
        layout.operator("button.action_view3d_render_border", text="渲染框")
        layout.separator()
        layout.operator("view3d.clear_render_border", text="清除渲染框")

# 弹出“视图框”菜单
class BUTTON_ACTION_OT_view3d_call_view_regions_menu(bpy.types.Operator):
    bl_idname = "button.action_view3d_call_view_regions_menu"
    bl_label = "视图框"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.ops.wm.call_menu(name="view3d.mt_view_regions_menu")
        return {'FINISHED'}

# 自定义“裁剪框”操作类
class BUTTON_ACTION_OT_view3d_clip_border(bpy.types.Operator):
    bl_idname = "button.action_view3d_clip_border"
    bl_label = "裁剪框"
    bl_description = "快捷键 Alt B"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        bpy.ops.view3d.clip_border('INVOKE_DEFAULT')
        return {'FINISHED'}
    
# 自定义“渲染框”操作类
class BUTTON_ACTION_OT_view3d_render_border(bpy.types.Operator):
    bl_idname = "button.action_view3d_render_border"
    bl_label = "渲染框"
    bl_description = "快捷键 Ctrl B"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        bpy.ops.view3d.render_border('INVOKE_DEFAULT')
        return {'FINISHED'}
    
# 自定义“区域”菜单
class BUTTON_ACTION_OT_view3d_area_menu(bpy.types.Operator):
    bl_idname = "button.action_view3d_area_menu"
    bl_label = "区域"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        bpy.ops.wm.call_menu(name="INFO_MT_area")
        return {'FINISHED'}
    
# 自定义“区域”——切换全屏模式
class BUTTON_ACTION_OT_view3d_screen_screen_full_area(bpy.types.Operator):
    bl_idname = "button.action_view3d_screen_screen_full_area"
    bl_label = "切换全屏模式"
    bl_description = "快捷键 Ctrl Alt 空格"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        bpy.ops.screen.screen_full_area(use_hide_panels=True)
        return {'FINISHED'}
    


