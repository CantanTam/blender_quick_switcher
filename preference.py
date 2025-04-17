import bpy
import webbrowser
from bpy.types import AddonPreferences, Operator
from bpy.props import BoolProperty, EnumProperty

class QuickSwitchAddonPreferences(AddonPreferences):
    bl_idname = __package__  # 使用当前包名作为标识符

    keys_combination_functions = [
        ('mode.menu_switch()', '弹出编辑模式菜单', '直接弹出编辑模式菜单'),
        ('switch.vertex_edge_face()', '快速切换点/线/面', '点←线←面方向快速切换'),
        ('mode.normal_up_to_down()', '上下方向快速切换编辑模式', '不弹出菜单，直接以从上到下的顺序切换编辑模式'), 
        ('mode.normal_down_to_up()', '下上方向快速切换编辑模式', '不弹出菜单，直接以从下到上的顺序切换编辑模式'), 
        ('mode.tab_switch()','切换最近两次编辑模式','比原生Tab键更合理的切换编辑模式方式'),
        ('wm.toolbar()','调用系统快捷菜单','调用Shift+Space快捷键'),
        ('NONE', '[ 无功能 ]', '如果快捷键和其它插件有键位冲突，可以选择[无功能]，重启Blender，注销组合键功能')
    ]
    
    ctrl_wheel_up: EnumProperty(
        name="Ctrl+鼠标上滚",
        description="选择Ctrl+鼠标上滚快捷键功能",
        items=keys_combination_functions,
        default='switch.vertex_edge_face()',
    )
    
    ctrl_wheel_down: EnumProperty(
        name="Ctrl+鼠标下滚", 
        description="选择Ctrl+鼠标下滚快捷键功能",
        items=keys_combination_functions,
        default='mode.tab_switch()'
    )

    ctrl_alt_wheel_up: EnumProperty(
        name="Ctrl+Alt+鼠标上滚", 
        description="选择Ctrl+Alt+鼠标上滚快捷键功能",
        items=keys_combination_functions,
        default='mode.menu_switch()'
    )

    ctrl_alt_wheel_down: EnumProperty(
        name="Ctrl+Alt+鼠标下滚", 
        description="选择Ctrl+Alt+鼠标下滚快捷键功能",
        items=keys_combination_functions,
        default='mode.menu_switch()'
    )

    shift_wheel_up: EnumProperty(
        name="Shift+鼠标上滚", 
        description="选择Shift+鼠标上滚快捷键功能",
        items=keys_combination_functions,
        default='mode.menu_switch()'
    )

    shift_wheel_down: EnumProperty(
        name="Shift+鼠标下滚", 
        description="选择Shift+鼠标下滚快捷键功能",
        items=keys_combination_functions,
        default='wm.toolbar()'
    )

    ctrl_shift_wheel_up: EnumProperty(
        name="Ctrl+Shift+鼠标上滚", 
        description="选择Ctrl+Shift+鼠标上滚快捷键功能",
        items=keys_combination_functions,
        default='mode.normal_down_to_up()'
    )

    ctrl_shift_wheel_down: EnumProperty(
        name="Ctrl+Shift+鼠标下滚", 
        description="选择Ctrl+Shift+鼠标下滚快捷键功能",
        items=keys_combination_functions,
        default='mode.normal_up_to_down()'
    )

    shift_alt_wheel_up: EnumProperty(
        name="Shift+Alt+鼠标上滚", 
        description="选择Shift+Alt+鼠标上滚快捷键功能",
        items=keys_combination_functions,
        default='mode.menu_switch()'
    )

    shift_alt_wheel_down: EnumProperty(
        name="Shift+Alt+鼠标下滚", 
        description="选择Shift+Alt+鼠标下滚快捷键功能",
        items=keys_combination_functions,
        default='mode.menu_switch()'
    )

    alt_mouse_right: EnumProperty(
        name="Alt+鼠标右键", 
        description="选择Alt+鼠标右键快捷键功能",
        items=keys_combination_functions,
        default='mode.menu_switch()'
    )

    ctrl_alt_mouse_right: EnumProperty(
        name="Ctrl+Alt+鼠标右键", 
        description="选择Ctrl+Alt+鼠标右键快捷键功能",
        items=keys_combination_functions,
        default='mode.menu_switch()'
    )

    shift_alt_mouse_right: EnumProperty(
        name="Shift+Alt+鼠标右键", 
        description="选择Shift+Alt+鼠标右键快捷键功能",
        items=keys_combination_functions,
        default='mode.menu_switch()'
    )

    show_shortcut_options: BoolProperty(
        name="显示快捷键选项",
        description="展开/折叠快捷键选项",
        default=True
    )

    def draw(self, context):
        layout = self.layout        
        # 可折叠的分组框
        box = layout.box()
        row = box.row()
        row.prop(self, "show_shortcut_options", 
                icon="TRIA_DOWN" if self.show_shortcut_options else "TRIA_RIGHT",
                icon_only=True, 
                emboss=False)
        row.label(text="选择快捷键功能：")
        
        if self.show_shortcut_options:
            # 选项内容区域
            content_box = box.box()
            row = content_box.row()
            row.prop(self, "ctrl_wheel_up")
            row = content_box.row() 
            row.prop(self, "ctrl_wheel_down")
            row = content_box.row() 
            row.prop(self, "ctrl_alt_wheel_up")
            row = content_box.row() 
            row.prop(self, "ctrl_alt_wheel_down")
            row = content_box.row() 
            row.prop(self, "shift_wheel_up")
            row = content_box.row() 
            row.prop(self, "shift_wheel_down")
            row = content_box.row() 
            row.prop(self, "ctrl_shift_wheel_up")
            row = content_box.row() 
            row.prop(self, "ctrl_shift_wheel_down")
            row = content_box.row() 
            row.prop(self, "shift_alt_wheel_up")
            row = content_box.row() 
            row.prop(self, "shift_alt_wheel_down")
            row = content_box.row() 
            row.prop(self, "alt_mouse_right")
            row = content_box.row() 
            row.prop(self, "ctrl_alt_mouse_right")
            row = content_box.row() 
            row.prop(self, "shift_alt_mouse_right")

def register():
    bpy.utils.register_class(QuickSwitchAddonPreferences)

def unregister():
    bpy.utils.unregister_class(QuickSwitchAddonPreferences)
