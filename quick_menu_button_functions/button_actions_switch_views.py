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
        
# 定义视图菜单
class VIEW3D_MT_view_axis_menu(bpy.types.Menu):
    bl_label = ""
    bl_idname = "VIEW3D_MT_view_axis_menu"

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

# 定义唤出菜单类
class BUTTON_ACTION_OT_view3d_call_menu_view_axis(bpy.types.Operator):
    bl_idname = "button.action_view3d_call_menu_view_axis"
    bl_label = "切换视图"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        # 只在3D视图中可用
        return context.area.type == 'VIEW_3D'

    def execute(self, context):
        bpy.ops.wm.call_menu(name="VIEW3D_MT_view_axis_menu")
        return {'CANCELLED'}
