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
        ('call.popup_menu_one()','超级菜单1','超级菜单1'),
        ('NONE', '[ 无功能 ]', '如果快捷键和其它插件有键位冲突，可以选择[无功能]，重启Blender，注销组合键功能')
    ]

    button_press_function = [
        ('wm.toolbar()','菜单功能1','测试菜单功能1'),
        ('mode.menu_switch()', '菜单功能2', '测试菜单功能2'),
        ('SEPARATOR', '[ 分隔符 ]', '测试分隔符功能'),
        ('NONE', '[ 无功能 ]', '测试按钮留空功能')
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
        default=False
    )
    

# --------↓↓↓↓ panel one 相关设置 ↓↓↓↓---------
    expand_quick_panel_one:BoolProperty(
        name="极速菜单1",
        description="展开/折叠极速菜单1",
        default=True
    )
    
    panel_one_col1_title: bpy.props.StringProperty(
        name="第一列标题",
        description="留空不显示该列",
        default="第一列标题"
    )

    panel_one_col1_width: bpy.props.IntProperty(
        name="面板宽度",
        description="第一列宽度",
        default=80,
        min=55,  # 最小值
        max=150,  # 最大值
        soft_min=55,  # 拖动时的最小限制
        soft_max=150  # 拖动时的最大限制
    )

    panel1_col1_button1: EnumProperty(
        name="菜单1列1按钮1",
        description="菜单1列1按钮1功能测试",
        items=button_press_function,
        default='wm.toolbar()',
    )

    panel1_col1_button2: EnumProperty(
        name="菜单1列1按钮2",
        description="菜单1列1按钮2功能测试",
        items=button_press_function,
        default='wm.toolbar()',
    )

    panel_one_col2_title: bpy.props.StringProperty(
        name="第二列标题",
        description="留空不显示该列",
        default="第二列标题"
    )

    panel_one_col2_width: bpy.props.IntProperty(
        name="面板宽度",
        description="第二列宽度",
        default=80,
        min=55,  # 最小值
        max=150,  # 最大值
        soft_min=55,  # 拖动时的最小限制
        soft_max=150  # 拖动时的最大限制
    )

    panel1_col2_button1: EnumProperty(
        name="菜单1列2按钮1",
        description="菜单1列2按钮1功能测试",
        items=button_press_function,
        default='wm.toolbar()',
    )

    panel1_col2_button2: EnumProperty(
        name="菜单1列2按钮2",
        description="菜单1列2按钮2功能测试",
        items=button_press_function,
        default='wm.toolbar()',
    )

    panel_one_col3_title: bpy.props.StringProperty(
        name="第三列标题",
        description="留空不显示该列",
        default="第三列标题"
    )

    panel_one_col3_width: bpy.props.IntProperty(
        name="面板宽度",
        description="第三列宽度",
        default=80,
        min=55,  # 最小值
        max=150,  # 最大值
        soft_min=55,  # 拖动时的最小限制
        soft_max=150  # 拖动时的最大限制
    )

    panel1_col3_button1: EnumProperty(
        name="菜单1列3按钮1",
        description="菜单1列3按钮1功能测试",
        items=button_press_function,
        default='wm.toolbar()',
    )

    panel1_col3_button2: EnumProperty(
        name="菜单1列3按钮2",
        description="菜单1列3按钮2功能测试",
        items=button_press_function,
        default='wm.toolbar()',
    )


# --------↑↑↑↑ panel one 相关设置 ↑↑↑↑---------



    # 绘制插件设置页选项菜单函数
    def draw(self, context):
        layout = self.layout

        # “选择快捷键” BOX框
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


        # -----------------------------------------------
        # 极速菜单1 设置项 BOX框
        box = layout.box()
        row = box.row()
        row.prop(self, "expand_quick_panel_one", 
                icon="TRIA_DOWN" if self.expand_quick_panel_one else "TRIA_RIGHT",
                icon_only=True, 
                emboss=False)
        row.label(text="极速菜单1：")
            
        if self.expand_quick_panel_one:

            # 第一列设置项：
            top_box = box.box()
            row = top_box.row()
            row.prop(self, "panel_one_col1_title", text="",icon="TOPBAR")
            row.prop(self, "panel_one_col1_width", text="第一列宽度")

            row = top_box.row()
            row.prop(self, "panel1_col1_button1")
            row = top_box.row()
            row.prop(self, "panel1_col1_button2")

            # 第二列设置项：
            top_box = box.box()
            row = top_box.row()
            row.prop(self, "panel_one_col2_title", text="",icon="TOPBAR")
            row.prop(self, "panel_one_col2_width", text="第二列宽度")
            
            content_box = top_box.box()
            row = content_box.row()
            row.prop(self, "panel1_col2_button1")
            row = content_box.row()
            row.prop(self, "panel1_col2_button2")

            # 第二列设置项：
            top_box = box.box()
            row = top_box.row()
            row.prop(self, "panel_one_col3_title", text="",icon="TOPBAR")
            row.prop(self, "panel_one_col3_width", text="第三列宽度")
            
            content_box = top_box.box()
            row = content_box.row()
            row.prop(self, "panel1_col3_button1")
            row = content_box.row()
            row.prop(self, "panel1_col3_button2")






def register():
    bpy.utils.register_class(QuickSwitchAddonPreferences)

def unregister():
    bpy.utils.unregister_class(QuickSwitchAddonPreferences)
