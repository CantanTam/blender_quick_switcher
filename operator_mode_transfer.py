import os
import bpy
from .show_switch_notice import show_notice

class MODE_OT_Transfer(bpy.types.Operator):
    bl_idname = "mode.transfer"
    bl_label = "传递模式"
    bl_description = "不经过物体模式，直接把当前模式传递给鼠标下的物体"
    bl_options = {'REGISTER', 'UNDO'}

    # 在 invoke 中捕获鼠标坐标
    def invoke(self, context, event):
        self.mx = event.mouse_region_x
        self.my = event.mouse_region_y
        return self.execute(context)

    def execute(self, context):
        # 遍历第一个 3D 视图区块
        for area in context.screen.areas:
            if area.type == 'VIEW_3D':
                override_ctx = {
                    'window': context.window,
                    'screen':  context.screen,
                    'area':    area,
                    'region':  area.regions[-1],
                    # 将捕获的鼠标坐标传给底层操作符
                    'mouse_region_x': self.mx,
                    'mouse_region_y': self.my,
                }
                # 临时重写上下文并以 INVOKE_DEFAULT 调用 transfer_mode
                with context.temp_override(**override_ctx):
                    bpy.ops.object.transfer_mode(
                        'INVOKE_DEFAULT',
                        use_flash_on_transfer=True
                    )
                break
            
        image_name = bpy.context.active_object.type+bpy.context.active_object.mode+".png"
        show_notice(image_name)
        
        return {'FINISHED'}


class MODE_OT_to_object_and_select(bpy.types.Operator):
    bl_idname = "mode.to_object_and_select"
    bl_label = "切换到对象模式并选择物体"
    bl_options = {'REGISTER', 'UNDO'}

    def invoke(self, context, event):
        # 捕获鼠标在当前区域内的坐标（使用相对区域坐标）
        self.mouse_x = event.mouse_region_x
        self.mouse_y = event.mouse_region_y
        return self.execute(context)

    def execute(self, context):
        # 切换到对象模式（如果不是对象模式）
        obj = context.object
        if obj is not None and obj.mode != 'OBJECT':
            bpy.ops.object.mode_set(mode='OBJECT')

        # 查找第一个 3D 视图区域和其窗口子区域
        view_area = None
        for area in context.window.screen.areas:
            if area.type == 'VIEW_3D':
                view_area = area
                break
        if view_area is None:
            self.report({'WARNING'}, "未找到 3D 视图区域")
            return {'CANCELLED'}

        view_region = None
        for region in view_area.regions:
            if region.type == 'WINDOW':
                view_region = region
                break
        if view_region is None:
            self.report({'WARNING'}, "未找到 3D 视图窗口区域")
            return {'CANCELLED'}

        # 构造上下文覆盖并调用 view3d.select
        override = {
            'window': context.window,
            'screen': context.window.screen,
            'area': view_area,
            'region': view_region
        }
        with context.temp_override(**override):
            bpy.ops.view3d.select(location=(self.mouse_x, self.mouse_y))

        image_name = bpy.context.active_object.type+bpy.context.active_object.mode+".png"
        show_notice(image_name)

        return {'FINISHED'}

