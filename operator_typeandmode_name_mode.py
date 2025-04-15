import bpy

# 定义全局变量用于存储定时器引用
_timer = None

def _check_active_object_type():
    obj = bpy.context.active_object
    if obj:
        # 使用更可靠的方式显示信息
        try:
            bpy.ops.object.mode_set(mode='OBJECT')
            bpy.context.window_manager.popup_menu(lambda self, context: self.layout.label(text="测试"), title=f"{obj.type}", icon='INFO')
        except:
            print(f"对象类型: {obj.type}")
    else:
        print("没有活动对象")

    # 返回时间间隔（秒），以继续调用
    return 50.0

def register_mode_handler():
    global _timer
    if _timer is None:
        _timer = bpy.app.timers.register(_check_active_object_type)
        print("Mode handler registered.")

def unregister_mode_handler():
    global _timer
    if _timer is not None:
        bpy.app.timers.unregister(_check_active_object_type)
        _timer = None
        print("Mode handler unregistered.")
