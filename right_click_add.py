import bpy

class OBJECT_OT_test_move_context(bpy.types.Operator):
    bl_idname = "object.test_move_context"
    bl_label = "测试选项?"
    bl_description = "自定义右键菜单选项示例"
    bl_options = {'REGISTER'}

    @classmethod
    def poll(cls, context):
        # 只在对象模式下可用
        return context.mode == 'OBJECT' and context.area.type == 'VIEW_3D'

    def execute(self, context):
        prefs = bpy.context.preferences.addons[__package__].preferences
        prefs.panel2_col3_button3 = 'button.action_global_grab'
        self.report({'INFO'}, "点击了 测试选项?")
        return {'FINISHED'}

def draw_move_context(self, context):
    op = getattr(context, "button_operator", None)
    # 检查右键对象是否为 Transform → Translate (Move)
    if op and op.bl_rna.identifier == "TRANSFORM_OT_translate":
        layout = self.layout
        layout.separator()
        layout.operator(OBJECT_OT_test_move_context.bl_idname, icon='PLUGIN')

def register():
    bpy.utils.register_class(OBJECT_OT_test_move_context)
    # 将自定义绘制函数附加到按钮上下文菜单
    bpy.types.UI_MT_button_context_menu.append(draw_move_context)

def unregister():
    bpy.types.UI_MT_button_context_menu.remove(draw_move_context)
    bpy.utils.unregister_class(OBJECT_OT_test_move_context)

if __name__ == "__main__":
    register()
