import bpy
from bpy.types import Operator
from bpy.props import EnumProperty

# 模式切换处理（添加物体检查）
def super_quick_switch(keys_combination, context):
    # Ctrl + 鼠标滚轮向下的操作
    if keys_combination == 'CTRL_WHEEL_DOWN':
        bpy.ops.mode.menu_switch()

    # Ctrl + 鼠标滚轮向上的操作
    elif keys_combination == 'CTRL_WHEEL_UP':
        bpy.ops.mode.normal_down_to_up()

    elif keys_combination == 'CTRL_SHIFT_WHEEL_UP':
        bpy.ops.switch.vertex_edge_face()

    #测试命令：
    elif keys_combination == 'ALT_MOUSE_RIGHT':
        bpy.ops.wm.toolbar()

    return False

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
            ('SHIFT_ALT_MOUSE_RIGHT', 'SHIFT_ALT_MOUSE_RIGHT', '')
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
            elif event.shift:
                keys_combination = 'SHIFT_WHEEL_UP' if event.type == 'WHEELUPMOUSE' else 'SHIFT_WHEEL_DOWN'
            elif event.ctrl:
                keys_combination = 'CTRL_WHEEL_UP' if event.type == 'WHEELUPMOUSE' else 'CTRL_WHEEL_DOWN'

        # 检查鼠标右键组合键
        elif event.type == 'RIGHTMOUSE':
            if event.ctrl and event.alt:
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

