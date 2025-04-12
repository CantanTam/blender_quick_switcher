import bpy
from .operators import CSAWHEEL_OT_ModeSwitchOperator

wheel_shortcut_keymaps = []

def register():
    # 设置键映射
    csawheel_wm = bpy.context.window_manager
    ctrl_kc = csawheel_wm.keyconfigs.addon
    ctrl_km = ctrl_kc.keymaps.new(name='3D View', space_type='VIEW_3D')

    # 添加各种组合键映射
    key_combinations = [
        # (direction, key, ctrl, alt, shift)
        ('CTRL_WHEEL_UP', 'WHEELUPMOUSE', True, False, False),
        ('CTRL_WHEEL_DOWN', 'WHEELDOWNMOUSE', True, False, False),
        ('CTRL_ALT_WHEEL_UP', 'WHEELUPMOUSE', True, True, False),
        ('CTRL_ALT_WHEEL_DOWN', 'WHEELDOWNMOUSE', True, True, False),
        ('SHIFT_WHEEL_UP', 'WHEELUPMOUSE', False, False, True),
        ('SHIFT_WHEEL_DOWN', 'WHEELDOWNMOUSE', False, False, True),
        ('CTRL_SHIFT_WHEEL_UP', 'WHEELUPMOUSE', True, False, True),
        ('CTRL_SHIFT_WHEEL_DOWN', 'WHEELDOWNMOUSE', True, False, True),
        ('ALT_MOUSE_RIGHT', 'RIGHTMOUSE', False, True, False),
        ('CTRL_ALT_MOUSE_RIGHT', 'RIGHTMOUSE', True, True, False),
        ('SHIFT_ALT_MOUSE_RIGHT', 'RIGHTMOUSE', False, True, True)
    ]

    for direction, key, ctrl, alt, shift in key_combinations:
        kmi = ctrl_km.keymap_items.new(
            "csawheel.mode_switch",
            key,
            'PRESS',
            ctrl=ctrl,
            alt=alt,
            shift=shift
        )
        kmi.properties.direction = direction

    wheel_shortcut_keymaps.append(ctrl_km)

def unregister():
    for ctrl_km in wheel_shortcut_keymaps:
        bpy.context.window_manager.keyconfigs.addon.keymaps.remove(ctrl_km)
    wheel_shortcut_keymaps.clear()
