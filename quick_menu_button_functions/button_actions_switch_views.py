import bpy
# 框显所选
class BUTTON_ACTION_OT_view_selected_use_all_regions_false(bpy.types.Operator):
    bl_idname = "button.action_view_selected_use_all_regions_false"
    bl_label = "框显所选"
    bl_description = "快捷键."
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        if bpy.context.selected_objects:
            bpy.ops.view3d.view_selected(use_all_regions=False)
            return {'FINISHED'}
        else:
            return {'CANCELLED'}

# 框显全部
class BUTTON_ACTION_OT_view_all_center_false(bpy.types.Operator):
    bl_idname = "button.action_view_all_center_false"
    bl_label = "框显全部"
    bl_description = "快捷键home"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.ops.view3d.view_all(center=False)
        return {'FINISHED'}
    
# 透视/正交
class BUTTON_ACTION_OT_view_persportho(bpy.types.Operator):
    bl_idname = "button.action_view_persportho"
    bl_label = "透视/正交"
    bl_description = "快捷键Num_5"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.ops.view3d.view_persportho()
        return {'FINISHED'}

# 局部视图
class BUTTON_ACTION_OT_view3d_localview(bpy.types.Operator):
    bl_idname = "button.action_view3d_localview"
    bl_label = "局部视图"
    bl_description = "快捷键/"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        if bpy.context.selected_objects:
            bpy.ops.view3d.localview(frame_selected=True)
            return {'FINISHED'}
        else:
            return {'CANCELLED'}
        
# 从局部视图中移除
class BUTTON_ACTION_OT_view3d_localview_remove_from(bpy.types.Operator):
    bl_idname = "button.action_view3d_localview_remove_from"
    bl_label = "从局部视图中移除"
    bl_description = "快捷键Alt+/"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        # 检查是否有选中对象且当前处于局部视图
        return (context.selected_objects and 
                context.space_data.local_view is not None)

    def execute(self, context):
        try:
            bpy.ops.view3d.localview_remove_from()
            return {'FINISHED'}
        except RuntimeError as e:
            self.report({'ERROR'}, str(e))
            return {'CANCELLED'}

# 设置活动物体为摄像机
class BUTTON_ACTION_OT_view3d_object_as_camera(bpy.types.Operator):
    bl_idname = "button.action_view3d_object_as_camera"
    bl_label = "设置活动物体为摄像机"
    bl_description = "快捷键Ctrl Num_0"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        if bpy.context.active_object:
            bpy.ops.view3d.object_as_camera()
            return {'FINISHED'}
        else:
            return {'CANCELLED'}

# 活动摄像机
class BUTTON_ACTION_OT_view3d_view_camera(bpy.types.Operator):
    bl_idname = "button.action_view3d_view_camera"
    bl_label = "活动摄像机"
    bl_description = "快捷键Num_0"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        if bpy.context.active_object:
            bpy.ops.view3d.view_camera()
            return {'FINISHED'}
        else:
            return {'CANCELLED'}
        
# 摄像机边界框
class BUTTON_ACTION_OT_view3d_view_center_camera(bpy.types.Operator):
    bl_idname = "button.action_view3d_view_center_camera"
    bl_label = "摄像机边界框"
    bl_description = "快捷键Home"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        # 检查当前是否有活动摄像机且处于摄像机视图
        return (context.scene.camera is not None and
                context.region_data.view_perspective == 'CAMERA')

    def execute(self, context):
        try:
            bpy.ops.view3d.view_center_camera()
            return {'FINISHED'}
        except RuntimeError as e:
            self.report({'ERROR'}, str(e))
            return {'CANCELLED'}
        
# 定义”视图“菜单
class VIEW3D_MT_view_axis_menu(bpy.types.Menu):
    bl_label = ""
    bl_idname = "view3d.mt_view_axis_menu"

    def draw(self, context):
        layout = self.layout
        
        # 调用 view_axis 操作符，并传入对应的 type 参数
        layout.operator("view3d.view_axis", text="顶视图").type='TOP'
        layout.operator("view3d.view_axis", text="底视图").type='BOTTOM'
        layout.separator()
        layout.operator("view3d.view_axis", text="前视图").type='FRONT'
        layout.operator("view3d.view_axis", text="后视图").type='BACK'
        layout.separator()
        layout.operator("view3d.view_axis", text="右视图").type='RIGHT'
        layout.operator("view3d.view_axis", text="左视图").type='LEFT'

# 唤出"视图“菜单类
class BUTTON_ACTION_OT_view3d_call_menu_view_axis(bpy.types.Operator):
    bl_idname = "button.action_view3d_call_menu_view_axis"
    bl_label = "视图"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.ops.wm.call_menu(name="view3d.mt_view_axis_menu")
        return {'CANCELLED'}

# 定语”视图切换“菜单
class VIEW3D_MT_view_switch_axis_menu(bpy.types.Menu):
    bl_label = ""
    bl_idname = "view3d.mt_view_switch_axis_menu"

    def draw(self, context):
        layout = self.layout
        
        # 调用 view_axis 操作符，并传入对应的 type 参数
        layout.operator("view3d.view_orbit", text="视轨左滚").type='ORBITLEFT'
        layout.operator("view3d.view_orbit", text="视轨右滚").type='ORBITRIGHT'
        layout.operator("view3d.view_orbit", text="视轨上滚").type='ORBITUP'
        layout.operator("view3d.view_orbit", text="视轨下滚").type='ORBITDOWN'
        op = layout.operator("view3d.view_orbit", text="相对视轨")
        op.type='ORBITRIGHT'
        op.angle=3.14159
        layout.separator()
        layout.operator("view3d.view_roll", text="左倾").type='LEFT'
        layout.operator("view3d.view_roll", text="右倾").type='RIGHT'
        layout.separator()
        layout.operator("button.action_view_pan_left", text="左平移")
        layout.operator("button.action_view_pan_right", text="右平移") 
        layout.operator("button.action_view_pan_up", text="上平移")
        layout.operator("button.action_view_pan_down", text="下平移")
        layout.separator()
        layout.operator("view3d.zoom", text="视图放大", icon="ZOOM_IN").delta=1
        layout.operator("view3d.zoom", text="视图缩小", icon = "ZOOM_OUT").delta=-1
        layout.operator("button.action_view3d_zoom_border", text="框选放大", icon = "SELECT_SET")
        if context.scene.camera is not None and context.region_data.view_perspective == 'CAMERA':
            layout.operator("view3d.zoom_camera_1_to_1", text="1:1缩放摄像机视图", icon = "CAMERA_DATA")
        layout.separator()
        layout.operator("button.action_view3d_fly", text="飞行漫步")
        layout.operator("button.action_view3d_walk", text="行走漫步")

class BUTTON_ACTION_OT_view3d_call_menu_view_switch_axis(bpy.types.Operator):
    bl_idname = "button.action_view3d_call_menu_view_switch_axis"
    bl_label = "视图切换"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.ops.wm.call_menu(name="view3d.mt_view_switch_axis_menu")
        return {'CANCELLED'}
    
# 自定义“框选放大”操作类
class BUTTON_ACTION_OT_view3d_zoom_border(bpy.types.Operator):
    bl_idname = "button.action_view3d_zoom_border"
    bl_label = "框选放大"
    bl_description = "快捷键 Shift B"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        bpy.ops.view3d.zoom_border('INVOKE_DEFAULT')
        return {'FINISHED'}
    
# 自定义“飞行漫步”操作类
class BUTTON_ACTION_OT_view3d_fly(bpy.types.Operator):
    bl_idname = "button.action_view3d_fly"
    bl_label = "飞行漫步"
    bl_description = ""
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        bpy.ops.view3d.fly('INVOKE_DEFAULT')
        return {'FINISHED'}
    
# 自定义“行走漫步”操作类
class BUTTON_ACTION_OT_view3d_walk(bpy.types.Operator):
    bl_idname = "button.action_view3d_walk"
    bl_label = "行走漫步"
    bl_description = "快捷键 Shift `"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
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
