import bpy

# 定义全局变量用于存储定时器引用
_record_typeandmode_name_timer = None

# 记录当前的 typeandmode、name，被 operator_mode_switch_tab.py 调用
typeandmode_name = {
    "object_prev_typeandmode":"NONE",
    "object_current_typeandmode":"NONE",
    "object_prev_name":"NONE",
    "object_current_name":"NONE"
}

def record_name_typeandmode():
    # 有活动物体，&& ( object_current_name 与当前活动物体的 bpy.context.active_object.name 不同
    # ，||  object_current_typeandmode 与当前活动物体的 bpy.context.active_object.type+
    # bpy.context.active_object.mode不同 )，才会进行下一步操作
    if bpy.context.active_object \
        and (typeandmode_name["object_current_name"] != bpy.context.active_object.name \
        or typeandmode_name["object_current_typeandmode"] != bpy.context.active_object.type+bpy.context.active_object.mode) :
        
        typeandmode_name["object_prev_typeandmode"] = typeandmode_name["object_current_typeandmode"]
        typeandmode_name["object_prev_name"] = typeandmode_name["object_current_name"]

        typeandmode_name["object_current_typeandmode"] = bpy.context.active_object.type+bpy.context.active_object.mode
        typeandmode_name["object_current_name"] = bpy.context.active_object.name

        #bpy.context.window_manager.popup_menu(lambda self, context: self.layout.label(text="测试"), title="发生改变，记录", icon='INFO')
        return 0.1
    else:
        #bpy.context.window_manager.popup_menu(lambda self, context: self.layout.label(text="测试"), title="没改变，不记录", icon='INFO')
        return 0.1

def register_mode_handler():
    global _record_typeandmode_name_timer
    if _record_typeandmode_name_timer is None:
        _record_typeandmode_name_timer = bpy.app.timers.register(record_name_typeandmode)

def unregister_mode_handler():
    global _record_typeandmode_name_timer
    if _record_typeandmode_name_timer is not None:
        bpy.app.timers.unregister(_record_typeandmode_name_timer)
        _record_typeandmode_name_timer = None

