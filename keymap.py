import bpy
from .operators import CSAWHEEL_OT_ModeSwitchOperator
from .preference import QuickSwitchAddonPreferences

wheel_shortcut_keymaps = []

def register():
    # 设置键映射
    csawheel_wm = bpy.context.window_manager
    shortcut_kc = csawheel_wm.keyconfigs.addon
    shortcut_km = shortcut_kc.keymaps.new(name='3D View', space_type='VIEW_3D')

    # 添加各种组合键映射
    key_combinations = [
        # (direction, key, ctrl, alt, shift)
        ('CTRL_WHEEL_UP', 'WHEELUPMOUSE', True, False, False) ,
        ('CTRL_WHEEL_DOWN', 'WHEELDOWNMOUSE', True, False, False),
        ('CTRL_ALT_WHEEL_UP', 'WHEELUPMOUSE', True, True, False),
        ('CTRL_ALT_WHEEL_DOWN', 'WHEELDOWNMOUSE', True, True, False),
        ('SHIFT_WHEEL_UP', 'WHEELUPMOUSE', False, False, True),
        ('SHIFT_WHEEL_DOWN', 'WHEELDOWNMOUSE', False, False, True),
        ('CTRL_SHIFT_WHEEL_UP', 'WHEELUPMOUSE', True, False, True),
        ('CTRL_SHIFT_WHEEL_DOWN', 'WHEELDOWNMOUSE', True, False, True),
        ('ALT_MOUSE_RIGHT', 'RIGHTMOUSE', False, True, False),
        ('CTRL_ALT_MOUSE_RIGHT', 'RIGHTMOUSE', True, True, False),
        ('SHIFT_ALT_MOUSE_RIGHT', 'RIGHTMOUSE', False, True, True),
        #添加 shift alt 滚轮向上
        ('SHIFT_ALT_WHEEL_UP', 'WHEELUPMOUSE', False, True, True),
        ('SHIFT_ALT_WHEEL_DOWN', 'WHEELDOWNMOUSE', False, True, True),
        ('CTRL_SHIFT_ALT_MOUSE_RIGHT', 'RIGHTMOUSE', True, True, True)

    ]

    prefs = bpy.context.preferences.addons[__package__].preferences

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

    for direction, key, ctrl, alt, shift in key_combinations:
        pref_name = direction_to_pref.get(direction)
        if pref_name and getattr(prefs, pref_name, None) == 'NONE':
            continue

        kmi = shortcut_km.keymap_items.new(
            "csawheel.mode_switch",
            key,
            'PRESS',
            ctrl=ctrl,
            alt=alt,
            shift=shift
        )
        kmi.properties.direction = direction

    wheel_shortcut_keymaps.append(shortcut_km)

def unregister():
    for shortcut_km in wheel_shortcut_keymaps:
        bpy.context.window_manager.keyconfigs.addon.keymaps.remove(shortcut_km)
    wheel_shortcut_keymaps.clear()
