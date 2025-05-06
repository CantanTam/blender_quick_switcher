import bpy
import gpu
from gpu_extras.batch import batch_for_shader
import os

class SwitchNotice:
    def __init__(self, image_path):
        self.image_path = image_path
        self.handler = None
        self.needs_redraw = False
        self.draw_handler = None

        # Convert relative path to absolute path (Windows compatible)
        if not os.path.isabs(self.image_path):
            # Get directory of this script
            script_dir = os.path.dirname(os.path.realpath(__file__))
            # Normalize path for Windows (convert / to \ if needed)
            script_dir = os.path.normpath(script_dir)
            # Join with notice_images subdirectory
            self.image_path = os.path.normpath(
                os.path.join(script_dir, "notice_images", self.image_path)
            )
        
        if not os.path.exists(self.image_path):
            raise FileNotFoundError(f"Image file not found: {self.image_path}")
        self.image = bpy.data.images.load(self.image_path)
        self.texture = gpu.texture.from_image(self.image)

        # 4.3版本之后着色器名称改变
        if bpy.app.version < (4, 3, 0):
            self.shader = gpu.shader.from_builtin('2D_IMAGE')
        else:
            self.shader = gpu.shader.from_builtin('IMAGE')

        # 获取 3D 视图区域宽度
        area_width = bpy.context.area.width

        prefs = bpy.context.preferences.addons.get(__package__).preferences
        self.scale_factor = prefs.to_show_switch_notice

        # 计算居中位置（保持底部距离不变，仅水平居中）
        self.left = (area_width - 480 * self.scale_factor) // 2  
        self.right = self.left + 480 * self.scale_factor

        # 初次计算资产栏高度
        asset_shelf_height = self.get_asset_shelf_height()
        height = asset_shelf_height + 15

        # 定义顶点数据（位置和纹理坐标）
        self.vertices = {
            "pos": [
                (self.left, height),
                (self.right, height),
                (self.right, 80 * self.scale_factor + height),
                (self.left, 80 * self.scale_factor + height)
            ],
            "texCoord": [(0, 0), (1, 0), (1, 1), (0, 1)],
        }
        self.batch = batch_for_shader(self.shader, 'TRI_FAN', self.vertices)

        # 注册绘制处理器 (draw_handler 用于记录重绘请求)
        self.draw_handler = bpy.types.SpaceView3D.draw_handler_add(
            self.view3d_draw_callback, (), 'WINDOW', 'POST_PIXEL'
        )

        bpy.app.timers.register(self.check_redraw, persistent=True)

        # 初次显示
        self.show()

    def get_asset_shelf_height(self):
        """遍历当前屏幕中所有 VIEW_3D 区域，返回第一个找到的 ASSET_SHELF 高度"""
        asset_shelf_height = 0
        for area in bpy.context.screen.areas:
            if area.type == 'VIEW_3D':
                for region in area.regions:
                    if region.type == "ASSET_SHELF":
                        asset_shelf_height = region.height
                        break
        return asset_shelf_height

    def update_asset_shelf_height(self):
        """在每次绘制前动态更新资产栏高度，并重置顶点数据"""
        asset_shelf_height = self.get_asset_shelf_height()
        height = asset_shelf_height + 15
        new_pos = [
            (self.left, height),
            (self.right, height),
            (self.right, 80 * self.scale_factor + height),
            (self.left, 80 * self.scale_factor + height),
        ]
        self.vertices["pos"] = new_pos
        # 重新构建 batch，这样绘制时就会使用新的顶点数据
        self.batch = batch_for_shader(self.shader, 'TRI_FAN', self.vertices)

    def draw(self):
        """在每次绘制前更新高度，然后绘制提示图像"""
        self.update_asset_shelf_height()
        gpu.state.blend_set('ALPHA')
        self.shader.bind()
        self.shader.uniform_sampler("image", self.texture)
        self.batch.draw(self.shader)
        gpu.state.blend_set('NONE')

    def show(self):
        if self.handler is None:
            self.handler = bpy.types.SpaceView3D.draw_handler_add(
                self.draw, (), 'WINDOW', 'POST_PIXEL'
            )

    def hide(self):
        if self.handler is not None:
            bpy.types.SpaceView3D.draw_handler_remove(self.handler, 'WINDOW')
            self.handler = None

    def view3d_draw_callback(self):
        self.needs_redraw = True

    def check_redraw(self):
        if self.needs_redraw:
            # 可根据需要调用 self.hide() 或其他刷新逻辑
            self.hide()
            self.needs_redraw = False
        return 1.0

    def cleanup(self):
        # 清理所有注册的处理器和定时器，并释放纹理资源
        self.hide()
        if self.draw_handler:
            try:
                bpy.types.SpaceView3D.draw_handler_remove(self.draw_handler, 'WINDOW')
            except Exception:
                pass
            self.draw_handler = None
        
        try:
            bpy.app.timers.unregister(self.check_redraw)
        except Exception:
            pass
        
        if hasattr(self, 'texture'):
            del self.texture
        if hasattr(self, 'image'):
            del self.image

# 全局变量存储当前的 SwitchNotice 实例
current_notice = None

def show_notice(image_path):
    prefs = bpy.context.preferences.addons.get(__package__).preferences
    if not prefs or prefs.to_show_switch_notice < 0.5:
        return
    
    global current_notice
    if current_notice:
        current_notice.cleanup()
        current_notice = None
        bpy.app.timers.register(lambda: None, first_interval=0.1)
    
    current_notice = SwitchNotice(image_path)

def register():
    pass

def unregister():
    global current_notice
    if current_notice:
        current_notice.cleanup()
        current_notice = None
