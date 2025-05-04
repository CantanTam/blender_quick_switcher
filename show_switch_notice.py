import bpy
import gpu
from gpu_extras.batch import batch_for_shader
import os

# Define your SwitchNotice class here
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
        
        # Check and load the image
        if not os.path.exists(self.image_path):
            raise FileNotFoundError(f"Image file not found: {self.image_path}")
        self.image = bpy.data.images.load(self.image_path)
        self.texture = gpu.texture.from_image(self.image)

        # Create shader and batch
        # 4.3 版本之后，着色器名称发生了改变
        if bpy.app.version < (4, 3, 0):
            self.shader = gpu.shader.from_builtin('2D_IMAGE')
        else:
            self.shader = gpu.shader.from_builtin('IMAGE')
        #self.shader = gpu.shader.from_builtin('2D_IMAGE')


        self.vertices = {
            "pos": [(100, 100), (300, 100), (300, 300), (100, 300)],
            "texCoord": [(0, 0), (1, 0), (1, 1), (0, 1)],
        }
        self.batch = batch_for_shader(self.shader, 'TRI_FAN', self.vertices)

        # Register draw handler
        self.draw_handler = bpy.types.SpaceView3D.draw_handler_add(
            self.view3d_draw_callback, (), 'WINDOW', 'POST_PIXEL')

        # Start timer
        bpy.app.timers.register(self.check_redraw, persistent=True)

        # Initial display
        self.show()

    def draw(self):
        gpu.state.blend_set('ALPHA')
        self.shader.bind()
        self.shader.uniform_sampler("image", self.texture)
        self.batch.draw(self.shader)
        gpu.state.blend_set('NONE')

    def show(self):
        if self.handler is None:
            self.handler = bpy.types.SpaceView3D.draw_handler_add(
                self.draw, (), 'WINDOW', 'POST_PIXEL')

    def hide(self):
        if self.handler is not None:
            bpy.types.SpaceView3D.draw_handler_remove(self.handler, 'WINDOW')
            self.handler = None

    def view3d_draw_callback(self):
        self.needs_redraw = True

    def check_redraw(self):
        if self.needs_redraw:
            self.hide()
            self.needs_redraw = False
        return 1.0

    def cleanup(self):
        # 确保所有handler都被移除
        self.hide()
        if self.draw_handler:
            try:
                bpy.types.SpaceView3D.draw_handler_remove(self.draw_handler, 'WINDOW')
            except:
                pass
            self.draw_handler = None
        
        # 确保定时器被移除
        try:
            bpy.app.timers.unregister(self.check_redraw)
        except:
            pass
        
        # 释放纹理资源
        if hasattr(self, 'texture'):
            del self.texture
        if hasattr(self, 'image'):
            del self.image

# Global variable to store the current notice
current_notice = None

def show_notice(image_path):
    prefs = bpy.context.preferences.addons.get(__package__).preferences
    if not prefs or not prefs.to_show_switch_notice:
        return
    
    global current_notice
    # 强制完全清理
    if current_notice:
        current_notice.cleanup()
        current_notice = None
        # 给Blender一个事件循环周期来完成清理
        # 这个空定时器确保资源释放完成后再创建新实例
        bpy.app.timers.register(lambda: None, first_interval=0.1)
    
    # 创建全新实例
    current_notice = SwitchNotice(image_path)

# Define register and unregister functions
def register():
    pass  # Add registration logic here if needed

def unregister():
    global current_notice
    if current_notice:
        current_notice.cleanup()
        current_notice = None
