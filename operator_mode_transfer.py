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

