import bpy
from bpy.types import Operator
from bpy.props import StringProperty

class SEARCH_OT_quick_search(Operator):
    bl_idname = "wm.quick_search"
    bl_label = "快速搜索"
    bl_description = "在菜单中快速搜索功能"
    
    search_term: StringProperty(
        name="搜索词",
        description="输入要搜索的内容",
        default=""
    )
    
    def execute(self, context):
        # 获取当前偏好设置
        prefs = context.preferences.addons[__package__].preferences
        
        # 过滤按钮功能
        filtered = [
            btn for btn in prefs.button_press_function
            if self.search_term.lower() in btn[1].lower()
        ]
        
        # 显示结果（这里简化为打印到控制台）
        print(f"找到 {len(filtered)} 个匹配项:")
        for btn in filtered:
            print(f"- {btn[1]}")
            
        return {'FINISHED'}
    
    def invoke(self, context, event):
        return context.window_manager.invoke_props_dialog(self)
    
    def draw(self, context):
        layout = self.layout
        layout.prop(self, "search_term")

def register():
    bpy.utils.register_class(SEARCH_OT_quick_search)

def unregister():
    bpy.utils.unregister_class(SEARCH_OT_quick_search)
