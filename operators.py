import bpy
from bpy.types import Operator
from bpy.props import EnumProperty
from .preference import QuickSwitchAddonPreferences

# 模式切换处理（添加物体检查）
def super_quick_switch(keys_combination, context):
    # 定义direction到prefs属性的映射
    direction_to_pref = {
        'CTRL_WHEEL_UP': 'ctrl_wheel_up',
        'CTRL_WHEEL_DOWN': 'ctrl_wheel_down',
        'CTRL_ALT_WHEEL_UP': 'ctrl_alt_wheel_up',
        'CTRL_ALT_WHEEL_DOWN': 'ctrl_alt_wheel_down',
        'SHIFT_WHEEL_UP': 'shift_wheel_up',
        'SHIFT_WHEEL_DOWN': 'shift_wheel_down',
        'CTRL_SHIFT_WHEEL_UP': 'ctrl_shift_wheel_up',
        'CTRL_SHIFT_WHEEL_DOWN': 'ctrl_shift_wheel_down',
        'ALT_MOUSE_RIGHT': 'alt_mouse_right',
        'CTRL_ALT_MOUSE_RIGHT': 'ctrl_alt_mouse_right',
        'SHIFT_ALT_MOUSE_RIGHT': 'shift_alt_mouse_right',
        'SHIFT_ALT_WHEEL_UP': 'shift_alt_wheel_up',
        'SHIFT_ALT_WHEEL_DOWN': 'shift_alt_wheel_down',
        'CTRL_SHIFT_ALT_MOUSE_RIGHT': 'ctrl_shift_alt_mouse_right'
    }

    prefs = context.preferences.addons[__package__].preferences
    pref_name = direction_to_pref.get(keys_combination)
    
    if pref_name:
        op = getattr(prefs, pref_name)
        if op != 'NONE':
            try:
                if op == 'mode.transfer()':
                    # 调用系统 alt q 传递模式功能
                    bpy.ops.mode.transfer('INVOKE_DEFAULT')
                elif op == 'mode.forced_select()':
                    bpy.ops.mode.to_object_and_select('INVOKE_DEFAULT')
                else:
                    exec(f'bpy.ops.{op}()')  # 自动添加bpy.ops.前缀和()后缀
            except Exception as e:
                print(f"执行操作失败: bpy.ops.{op}(), 错误: {e}")
    
    return True

# 主操作符（添加前置检查）
class CSAWHEEL_OT_ModeSwitchOperator(Operator):
    bl_idname = "csawheel.mode_switch"
    bl_label = "Advanced Mode Switch"
    bl_options = {'REGISTER', 'UNDO'}

    direction: EnumProperty(
        items=[
            ('CTRL_WHEEL_UP', 'CTRL_WHEEL_UP', ''),
            ('CTRL_WHEEL_DOWN', 'CTRL_WHEEL_DOWN', ''),
            ('CTRL_ALT_WHEEL_UP', 'CTRL_ALT_WHEEL_UP', ''),
            ('CTRL_ALT_WHEEL_DOWN', 'CTRL_ALT_WHEEL_DOWN', ''),
            ('SHIFT_WHEEL_UP', 'SHIFT_WHEEL_UP', ''),
            ('SHIFT_WHEEL_DOWN', 'SHIFT_WHEEL_DOWN', ''),
            ('CTRL_SHIFT_WHEEL_UP', 'CTRL_SHIFT_WHEEL_UP', ''),
            ('CTRL_SHIFT_WHEEL_DOWN', 'CTRL_SHIFT_WHEEL_DOWN', ''),
            ('ALT_MOUSE_RIGHT', 'ALT_MOUSE_RIGHT', ''),
            ('CTRL_ALT_MOUSE_RIGHT', 'CTRL_ALT_MOUSE_RIGHT', ''),
            ('SHIFT_ALT_MOUSE_RIGHT', 'SHIFT_ALT_MOUSE_RIGHT', ''),
            # 添加 shift alt 滚轮向上快捷键
            ('SHIFT_ALT_WHEEL_UP', 'SHIFT_ALT_WHEEL_UP', ''),
            ('SHIFT_ALT_WHEEL_DOWN', 'SHIFT_ALT_WHEEL_DOWN', ''),
            ('CTRL_SHIFT_ALT_MOUSE_RIGHT', 'CTRL_SHIFT_ALT_MOUSE_RIGHT', '')
        ],
        default='CTRL_WHEEL_UP'
    )

    @classmethod
    def poll(cls, context):
        return context.area.type == 'VIEW_3D'

    def invoke(self, context, event):
        if not self.poll(context):
            return {'PASS_THROUGH'}

        keys_combination = None

        # 检查各种组合键+滚轮
        if event.type in {'WHEELUPMOUSE', 'WHEELDOWNMOUSE'}:
            if event.ctrl and event.alt:
                keys_combination = 'CTRL_ALT_WHEEL_UP' if event.type == 'WHEELUPMOUSE' else 'CTRL_ALT_WHEEL_DOWN'
            elif event.ctrl and event.shift:
                keys_combination = 'CTRL_SHIFT_WHEEL_UP' if event.type == 'WHEELUPMOUSE' else 'CTRL_SHIFT_WHEEL_DOWN'
            elif event.shift and event.alt:
                keys_combination = 'SHIFT_ALT_WHEEL_UP' if event.type == 'WHEELUPMOUSE' else 'SHIFT_ALT_WHEEL_DOWN'
            elif event.shift:
                keys_combination = 'SHIFT_WHEEL_UP' if event.type == 'WHEELUPMOUSE' else 'SHIFT_WHEEL_DOWN'
            elif event.ctrl:
                keys_combination = 'CTRL_WHEEL_UP' if event.type == 'WHEELUPMOUSE' else 'CTRL_WHEEL_DOWN'

        # 检查鼠标右键组合键
        elif event.type == 'RIGHTMOUSE':
            if event.ctrl and event.shift and event.alt:
                keys_combination = 'CTRL_SHIFT_ALT_MOUSE_RIGHT'
            elif event.ctrl and event.alt:
                keys_combination = 'CTRL_ALT_MOUSE_RIGHT'
            elif event.alt and event.shift:
                keys_combination = 'SHIFT_ALT_MOUSE_RIGHT'
            elif event.alt:
                keys_combination = 'ALT_MOUSE_RIGHT'

        if not keys_combination:
            return {'PASS_THROUGH'}

        if context.area.type != 'VIEW_3D':
            return {'PASS_THROUGH'}

        if super_quick_switch(keys_combination, context):
            return {'FINISHED'}

        return {'PASS_THROUGH'}
