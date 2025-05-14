import bpy

class BUTTON_ACTION_OT_view3d_view_selected(bpy.types.Operator):
    bl_idname = "button.action_view3d_view_selected"
    bl_label = "框选所选"
    bl_description = "快捷键 ."
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.ops.view3d.view_selected('INVOKE_DEFAULT')
        return {'FINISHED'}
    
class BUTTON_ACTION_OT_view3d_view_all(bpy.types.Operator):
    bl_idname = "button.action_view3d_view_all"
    bl_label = "框选全部"
    bl_description = "快捷键 Home"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.ops.view3d.view_all('INVOKE_DEFAULT')
        return {'FINISHED'}
    
class BUTTON_ACTION_OT_view3d_localview(bpy.types.Operator):
    bl_idname = "button.action_view3d_localview"
    bl_label = "切换局部视图"
    bl_description = "快捷键 /"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.ops.view3d.localview('INVOKE_DEFAULT')
        return {'FINISHED'}
    
class BUTTON_ACTION_OT_view3d_object_as_camera(bpy.types.Operator):
    bl_idname = "button.action_view3d_object_as_camera"
    bl_label = "设置活动物体为摄像机"
    bl_description = "快捷键 Ctrl Num_0"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.ops.view3d.object_as_camera('INVOKE_DEFAULT')
        return {'FINISHED'}
    
class BUTTON_ACTION_OT_view3d_view_center_camera(bpy.types.Operator):
    bl_idname = "button.action_view3d_view_center_camera"
    bl_label = "摄像机边界框"
    bl_description = "快捷键 Home"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.ops.view3d.view_center_camera('INVOKE_DEFAULT')
        return {'FINISHED'}
    
class BUTTON_ACTION_OT_view3d_view_viewpoint_menu(bpy.types.Operator):
    bl_idname = "button.action_view3d_view_viewpoint_menu"
    bl_label = "视图"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        return {'FINISHED'}

    def invoke(self, context, event):
        return context.window_manager.invoke_popup(self, width=80)

    def draw(self, context):
        layout = self.layout
        row = layout.row()
        col = row.column(align=True)
        col.label(text="视图", icon='PRESET')
        col.operator("view3d.view_camera", text="摄像机", icon="OUTLINER_DATA_CAMERA")
        col.separator()
        col.operator("view3d.view_axis", text="顶视图", icon="RADIOBUT_OFF").type='TOP'
        col.operator("view3d.view_axis", text="底视图", icon="RADIOBUT_OFF").type='BOTTOM'
        col.separator()
        col.operator("view3d.view_axis", text="前视图", icon="RADIOBUT_OFF").type='FRONT'
        col.operator("view3d.view_axis", text="后视图", icon="RADIOBUT_OFF").type='BACK'
        col.separator()
        col.operator("view3d.view_axis", text="右视图", icon="RADIOBUT_OFF").type='RIGHT'
        col.operator("view3d.view_axis", text="左视图", icon="RADIOBUT_OFF").type='LEFT'

# 唤出"视图“菜单类
class BUTTON_ACTION_OT_view3d_call_view_viewpoint_menu(bpy.types.Operator):
    bl_idname = "button.action_view3d_call_view_viewpoint_menu"
    bl_label = "视图"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.ops.button.action_view3d_view_viewpoint_menu('INVOKE_DEFAULT')
        return {'FINISHED'}

class BUTTON_ACTION_OT_view3d_view_navigation_menu(bpy.types.Operator):
    bl_idname = "button.action_view3d_view_navigation_menu"
    bl_label = "视图切换"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        return {'FINISHED'}

    def invoke(self, context, event):
        return context.window_manager.invoke_popup(self, width=100)

    def draw(self, context):
        layout = self.layout
        row = layout.row()
        col = row.column(align=True)
        col.label(text="视图切换", icon='PRESET')
        col.operator("view3d.view_orbit", text="视轨左滚", icon="RADIOBUT_OFF").type='ORBITLEFT'
        col.operator("view3d.view_orbit", text="视轨右滚", icon="RADIOBUT_OFF").type='ORBITRIGHT'
        col.operator("view3d.view_orbit", text="视轨上滚", icon="RADIOBUT_OFF").type='ORBITUP'
        col.operator("view3d.view_orbit", text="视轨下滚", icon="RADIOBUT_OFF").type='ORBITDOWN'
        op = col.operator("view3d.view_orbit", text="相对视轨", icon="RADIOBUT_OFF")
        op.angle=3.14159
        op.type='ORBITRIGHT'
        col.separator()
        col.operator("view3d.view_roll", text="左倾", icon="RADIOBUT_OFF").type='LEFT'
        col.operator("view3d.view_roll", text="右倾", icon="RADIOBUT_OFF").type='RIGHT'
        col.separator()
        col.operator("view3d.view_pan", text="左平移", icon="RADIOBUT_OFF").type='PANLEFT'
        col.operator("view3d.view_pan", text="右平移", icon="RADIOBUT_OFF").type='PANRIGHT'
        col.operator("view3d.view_pan", text="上平移", icon="RADIOBUT_OFF").type='PANUP'
        col.operator("view3d.view_pan", text="下平移", icon="RADIOBUT_OFF").type='PANDOWN'
        col.separator()
        col.operator("view3d.zoom", text="视图放大", icon="RADIOBUT_OFF").delta=1
        col.operator("view3d.zoom", text="视图缩小", icon="RADIOBUT_OFF").delta=-1
        col.operator("view3d.zoom_border", text="框选放大", icon="RADIOBUT_OFF")
        col.operator("view3d.dolly", text="滑动视图", icon="RADIOBUT_OFF")
        col.operator("view3d.zoom_camera_1_to_1", text="1:1缩放摄像机视图", icon="RADIOBUT_OFF")
        col.separator()
        col.operator("view3d.fly", text="飞行漫游模式", icon="RADIOBUT_OFF")
        col.operator("view3d.walk", text="行走漫游", icon="RADIOBUT_OFF")

# 唤出“视图切换”菜单类
class BUTTON_ACTION_OT_view3d_call_view_navigation_menu(bpy.types.Operator):
    bl_idname = "button.action_view3d_call_view_navigation_menu"
    bl_label = "视图切换"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.ops.button.action_view3d_view_navigation_menu('INVOKE_DEFAULT')
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
    
class BUTTON_ACTION_OT_view3d_fly(bpy.types.Operator):
    bl_idname = "button.action_view3d_fly"
    bl_label = "飞行漫游模式"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        bpy.ops.view3d.view_lock_clear()
        bpy.ops.view3d.fly('INVOKE_DEFAULT')
        return {'FINISHED'}
    
class BUTTON_ACTION_OT_view3d_view_align_selected_menu(bpy.types.Operator):
    bl_idname = "button.action_view_align_selected_menu"
    bl_label = "视图对齐活动项"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        return {'FINISHED'}

    def invoke(self, context, event):
        return context.window_manager.invoke_popup(self, width=80)

    def draw(self, context):
        layout = self.layout
        row = layout.row()
        col = row.column(align=True)
        col.label(text="视图对齐活动项", icon='PRESET')
        op = col.operator("view3d.view_axis", text="顶视图", icon="RADIOBUT_OFF")
        op.type = 'TOP'
        op.align_active=True
        op = col.operator("view3d.view_axis", text="底视图", icon="RADIOBUT_OFF")
        op.type = 'BOTTOM'
        op.align_active=True
        col.separator()
        op = col.operator("view3d.view_axis", text="前视图", icon="RADIOBUT_OFF")
        op.type = 'FRONT'
        op.align_active=True
        op = col.operator("view3d.view_axis", text="后视图", icon="RADIOBUT_OFF")
        op.type = 'BACK'
        op.align_active=True
        col.separator()
        op = col.operator("view3d.view_axis", text="左视图", icon="RADIOBUT_OFF")
        op.type = 'RIGHT'
        op.align_active=True
        op = col.operator("view3d.view_axis", text="右视图", icon="RADIOBUT_OFF")
        op.type = 'LEFT'
        op.align_active=True











class BUTTON_ACTION_OT_view3d_call_view_align_selected_menu(bpy.types.Operator):
    bl_idname = "button.action_view3d_call_view_align_selected_menu"
    bl_label = "视图对齐活动项"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.ops.button.action_view_align_selected_menu('INVOKE_DEFAULT')
        return {'FINISHED'}

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
    

classes = (
    BUTTON_ACTION_OT_view3d_view_align_selected_menu,
    BUTTON_ACTION_OT_view3d_call_view_align_selected_menu,
    BUTTON_ACTION_OT_view3d_view_selected,
    BUTTON_ACTION_OT_view3d_view_all,
    BUTTON_ACTION_OT_view3d_localview,
    BUTTON_ACTION_OT_view3d_object_as_camera,
    BUTTON_ACTION_OT_view3d_view_center_camera,
    BUTTON_ACTION_OT_view3d_view_viewpoint_menu,
    BUTTON_ACTION_OT_view3d_call_view_viewpoint_menu,
    BUTTON_ACTION_OT_view3d_view_navigation_menu,
    BUTTON_ACTION_OT_view3d_call_view_navigation_menu,
    BUTTON_ACTION_OT_view3d_zoom_border,
    BUTTON_ACTION_OT_view3d_walk,
    BUTTON_ACTION_OT_view3d_fly,
    BUTTON_ACTION_OT_view3d_call_view_align_menu,
    VIEW3D_MT_view_regions_menu,
    BUTTON_ACTION_OT_view3d_call_view_regions_menu,
    BUTTON_ACTION_OT_view3d_clip_border,
    BUTTON_ACTION_OT_view3d_render_border,
    BUTTON_ACTION_OT_view3d_lock_to_active_or_lock_clear,
    BUTTON_ACTION_OT_view3d_view_all_center_true,
    BUTTON_ACTION_OT_view3d_area_menu,
    BUTTON_ACTION_OT_view3d_screen_screen_full_area,
)

def register():
    for cls in classes:
        bpy.utils.register_class(cls)

def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)
