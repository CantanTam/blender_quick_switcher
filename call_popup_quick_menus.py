import bpy

class CALLOUT_QUICK_MENU_OT_one(bpy.types.Operator):
    bl_idname = "call.popup_menu_one"
    bl_label = "调用极速菜单1"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.ops.wm.call_menu(name="popup.quick_menu_object")
        return {'FINISHED'}
    
# 因为 operators.py 当中 限过了快捷键功能的运行方式是 exec(f'bpy.ops.{op}()') 
# ，无法在函数内部添加参数，而 bpy.ops.popup.quick_menu_object() 是无法调出自定义菜单的
# ，所以需要再构建一个函数，调用 bpy.ops.popup.quick_menu_object('INVOKE_DEFAULT')

class CALLOUT_QUICK_MENU_OT_two(bpy.types.Operator):
    bl_idname = "call.popup_menu_two"
    bl_label = "调用极速菜单2"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.ops.wm.call_menu(name="popup.quick_menu_two")
        return {'FINISHED'}
    
    