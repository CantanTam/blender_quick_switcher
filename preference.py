import bpy
import webbrowser
import json
import os
from bpy.types import AddonPreferences, Operator
from bpy.props import BoolProperty, EnumProperty, FloatProperty, IntProperty, StringProperty
from .button_operator_dict import button_options_list

# 定义 JSON 配置文件路径，假设保存于当前 addon 文件夹下
def get_settings_file_path():
    addon_dir = os.path.dirname(__file__)
    return os.path.join(addon_dir, "settings.json")

# 加载 JSON 设置
def load_settings():
    path = get_settings_file_path()
    if os.path.exists(path):
        try:
            with open(path, 'r', encoding='utf-8') as f:
                return json.load(f)
        except Exception as e:
            print("加载设置失败：", e)
    return {}

# 保存设置到 JSON 文件
def save_settings(settings_dict):
    path = get_settings_file_path()
    try:
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(settings_dict, f, indent=4, ensure_ascii=False)
    except Exception as e:
        print("保存设置失败：", e)

# 用于 update 回调的公共函数，属性一旦更新就写入 JSON 文件
def update_preferences(self, context):
    self.save_to_file()

keys_combination_functions = [
    ('mode.menu_switch()', '弹出编辑模式菜单', '直接弹出编辑模式菜单'),
    ('switch.vertex_edge_face()', '快速切换点/线/面', '点←线←面方向快速切换'),
    ('mode.normal_up_to_down()', '上下方向快速切换编辑模式', '不弹出菜单，直接以从上到下的顺序切换编辑模式'), 
    ('mode.normal_down_to_up()', '下上方向快速切换编辑模式', '不弹出菜单，直接以从下到上的顺序切换编辑模式'), 
    ('mode.tab_switch()','切换最近两次编辑模式','比原生Tab键更合理的切换编辑模式方式'),
    ('wm.toolbar()','调用系统快捷菜单','调用Shift+Space快捷键'),
    ('mode.transfer()','传递编辑模式','不经过物体模式切换，直接把当前模式传递给鼠标下的物体'),
    ('mode.forced_select()','强行选中','把鼠标所在位置下的对象转为物体类型并选中'),

    ('call.popup_menu_one()','极速菜单1','超级菜单1'),
    ('call.popup_menu_two()','极速菜单2','超级菜单2'),
    ('NONE', '[ 无功能 ]', '如果快捷键和其它插件有键位冲突，可以选择[无功能]，重启Blender，注销组合键功能')
]

class QuickSwitchAddonPreferences(AddonPreferences):
    bl_idname = __package__  # 使用当前包名作为标识符
    
    def __init__(self):
        super().__init__()
        print("初始化插件首选项...")
        # 立即加载设置
        settings = load_settings()
        if settings:
            print("从settings.json加载初始设置...")
            for prop_name, value in settings.items():
                if hasattr(self, prop_name):
                    try:
                        # 直接设置属性值
                        setattr(self, prop_name, value)
                        print(f"初始设置 {prop_name} = {value}")
                    except Exception as e:
                        print(f"初始设置 {prop_name} 失败: {e}")

    to_show_to_switcher:BoolProperty(
        name="显示添加到Switcher",
        description="显示/隐藏右击\"添加到Switcher\"选项",
        default=False,
        update=update_preferences
    )

    ctrl_wheel_up: EnumProperty(
        name="Ctrl+鼠标上滚",
        description="选择Ctrl+鼠标上滚快捷键功能",
        items=keys_combination_functions,
        default='switch.vertex_edge_face()',
        update=update_preferences,
    )
    
    ctrl_wheel_down: EnumProperty(
        name="Ctrl+鼠标下滚", 
        description="选择Ctrl+鼠标下滚快捷键功能",
        items=keys_combination_functions,
        default='mode.tab_switch()',
        update=update_preferences,
    )

    ctrl_alt_wheel_up: EnumProperty(
        name="Ctrl+Alt+鼠标上滚", 
        description="选择Ctrl+Alt+鼠标上滚快捷键功能",
        items=keys_combination_functions,
        default='mode.menu_switch()',
        update=update_preferences
    )

    ctrl_alt_wheel_down: EnumProperty(
        name="Ctrl+Alt+鼠标下滚", 
        description="选择Ctrl+Alt+鼠标下滚快捷键功能",
        items=keys_combination_functions,
        default='mode.menu_switch()',
        update=update_preferences
    )

    shift_wheel_up: EnumProperty(
        name="Shift+鼠标上滚", 
        description="选择Shift+鼠标上滚快捷键功能",
        items=keys_combination_functions,
        default='mode.menu_switch()',
        update=update_preferences
    )

    shift_wheel_down: EnumProperty(
        name="Shift+鼠标下滚", 
        description="选择Shift+鼠标下滚快捷键功能",
        items=keys_combination_functions,
        default='wm.toolbar()',
        update=update_preferences
    )

    ctrl_shift_wheel_up: EnumProperty(
        name="Ctrl+Shift+鼠标上滚", 
        description="选择Ctrl+Shift+鼠标上滚快捷键功能",
        items=keys_combination_functions,
        default='mode.normal_down_to_up()',
        update=update_preferences
    )

    ctrl_shift_wheel_down: EnumProperty(
        name="Ctrl+Shift+鼠标下滚", 
        description="选择Ctrl+Shift+鼠标下滚快捷键功能",
        items=keys_combination_functions,
        default='mode.normal_up_to_down()',
        update=update_preferences
    )

    shift_alt_wheel_up: EnumProperty(
        name="Shift+Alt+鼠标上滚", 
        description="选择Shift+Alt+鼠标上滚快捷键功能",
        items=keys_combination_functions,
        default='mode.menu_switch()',
        update=update_preferences
    )

    shift_alt_wheel_down: EnumProperty(
        name="Shift+Alt+鼠标下滚", 
        description="选择Shift+Alt+鼠标下滚快捷键功能",
        items=keys_combination_functions,
        default='mode.menu_switch()',
        update=update_preferences
    )

    alt_mouse_right: EnumProperty(
        name="Alt+鼠标右键", 
        description="选择Alt+鼠标右键快捷键功能",
        items=keys_combination_functions,
        default='mode.transfer()',
        update=update_preferences
    )

    ctrl_alt_mouse_right: EnumProperty(
        name="Ctrl+Alt+鼠标右键", 
        description="选择Ctrl+Alt+鼠标右键快捷键功能",
        items=keys_combination_functions,
        default='mode.menu_switch()',
        update=update_preferences
    )

    shift_alt_mouse_right: EnumProperty(
        name="Shift+Alt+鼠标右键", 
        description="选择Shift+Alt+鼠标右键快捷键功能",
        items=keys_combination_functions,
        default='mode.menu_switch()',
        update=update_preferences
    )

    ctrl_shift_alt_mouse_right: EnumProperty(
        name="Ctrl_Shift+Alt+鼠标右键", 
        description="选择Ctrl+Shift+Alt+鼠标右键快捷键功能",
        items=keys_combination_functions,
        default='mode.forced_select()',
        update=update_preferences
    )

    show_shortcut_options: BoolProperty(
        name="显示快捷键选项",
        description="展开/折叠快捷键选项",
        default=False,
        update=update_preferences
    )
    

# 设置一个空按钮，如果按钮功能不适用当前模式，变成一个空白按钮
# 这个选项不在 def draw 中显示
    blank_button: EnumProperty(
        name="空白按钮",
        description="用于不显示按钮",
        items=button_options_list,
        default='NO_BUTTON',
        update=update_preferences
    )







    to_show_switch_notice:BoolProperty(
        name="显示切换提示",
        description="显示/隐藏切换提示",
        default=True,
        update=update_preferences
    )

# 编辑模式切换提示及缩放系数
    switch_notice_scale:FloatProperty(
        name="切换提示缩放系数",
        default=1.0,  
        min=0.5,     
        max=2.0,    
        precision=1,
        update=update_preferences
    )

    switch_notice_themes: bpy.props.EnumProperty(
        name="切换提示主题",
        items=[
            ('pale', "Pale", ""),
            ('white', "White", ""),
            ('whiteround', "White_Round", ""),
            ('dark', "Dark", ""),
            ('darkround', "Dark_round", ""),
        ],
        default='white',
        update=update_preferences
    )

    switch_notice_position: bpy.props.EnumProperty(
        name="切换提示位置",
        items=[
            ('top', "顶部", ""),
            ('center', "中心", ""),
            ('bottom', "底部", ""),
        ],
        default='bottom',
        update=update_preferences
    )

#极速菜单通用管理
    quick_menu_one:BoolProperty(
        name="极速菜单1",
        description="展开/折叠极速菜单1",
        default=True,
        update=update_preferences
    )

    quick_menu_two:BoolProperty(
        name="极速菜单2",
        description="展开/折叠极速菜单2",
        default=True,
        update=update_preferences
    )







# --------↓↓↓↓ panelone_mode1 相关设置 ↓↓↓↓---------
    panelone_mode1_visible: BoolProperty(
        name="",
        description="显示/隐藏超级面板",
        default=True,
        update=update_preferences
    )

    panelone_mode1_col1_title: StringProperty(
        name="一列标题",
        description="留空不显示该列",
        default="一列标题",
        update=update_preferences
    )

    panelone_mode1_col1_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode1_col1_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode1_col1_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode1_col1_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode1_col1_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode1_col1_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode1_col1_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode1_col1_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode1_col1_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode1_col1_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode1_col2_title: StringProperty(
        name="二列标题",
        description="留空不显示该列",
        default="二列标题",
        update=update_preferences
    )

    panelone_mode1_col2_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode1_col2_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode1_col2_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode1_col2_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode1_col2_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode1_col2_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode1_col2_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode1_col2_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode1_col2_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode1_col2_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode1_col3_title: StringProperty(
        name="三列标题",
        description="留空不显示该列",
        default="三列标题",
        update=update_preferences
    )

    panelone_mode1_col3_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode1_col3_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode1_col3_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode1_col3_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode1_col3_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode1_col3_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode1_col3_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode1_col3_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode1_col3_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode1_col3_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode1_col4_title: StringProperty(
        name="四列标题",
        description="留空不显示该列",
        default="四列标题",
        update=update_preferences
    )

    panelone_mode1_col4_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode1_col4_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode1_col4_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode1_col4_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode1_col4_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode1_col4_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode1_col4_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode1_col4_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode1_col4_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode1_col4_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode1_col5_title: StringProperty(
        name="五列标题",
        description="留空不显示该列",
        default="五列标题",
        update=update_preferences
    )

    panelone_mode1_col5_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode1_col5_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode1_col5_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode1_col5_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode1_col5_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode1_col5_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode1_col5_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode1_col5_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode1_col5_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode1_col5_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode1_col6_title: StringProperty(
        name="六列标题",
        description="留空不显示该列",
        default="六列标题",
        update=update_preferences
    )

    panelone_mode1_col6_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode1_col6_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode1_col6_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode1_col6_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode1_col6_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode1_col6_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode1_col6_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode1_col6_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode1_col6_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode1_col6_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode1_col7_title: StringProperty(
        name="七列标题",
        description="留空不显示该列",
        default="七列标题",
        update=update_preferences
    )

    panelone_mode1_col7_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode1_col7_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode1_col7_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode1_col7_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode1_col7_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode1_col7_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode1_col7_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode1_col7_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode1_col7_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode1_col7_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode1_col8_title: StringProperty(
        name="八列标题",
        description="留空不显示该列",
        default="八列标题",
        update=update_preferences
    )

    panelone_mode1_col8_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode1_col8_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode1_col8_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode1_col8_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode1_col8_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode1_col8_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode1_col8_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode1_col8_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode1_col8_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode1_col8_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

# --------↑↑↑↑ panelone_mode1 相关设置 ↑↑↑↑---------













# --------↓↓↓↓ panelone_mode2 相关设置 ↓↓↓↓---------
    panelone_mode2_visible: BoolProperty(
        name="",
        description="显示/隐藏超级面板",
        default=True,
        update=update_preferences
    )
    
    panelone_mode2_col1_title: StringProperty(
        name="一列标题",
        description="留空不显示该列",
        default="一列标题",
        update=update_preferences
    )

    panelone_mode2_col1_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode2_col1_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode2_col1_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode2_col1_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode2_col1_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode2_col1_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode2_col1_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode2_col1_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode2_col1_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode2_col1_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode2_col2_title: StringProperty(
        name="二列标题",
        description="留空不显示该列",
        default="二列标题",
        update=update_preferences
    )

    panelone_mode2_col2_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode2_col2_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode2_col2_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode2_col2_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode2_col2_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode2_col2_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode2_col2_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode2_col2_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode2_col2_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode2_col2_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode2_col3_title: StringProperty(
        name="三列标题",
        description="留空不显示该列",
        default="三列标题",
        update=update_preferences
    )

    panelone_mode2_col3_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode2_col3_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode2_col3_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode2_col3_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode2_col3_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode2_col3_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode2_col3_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode2_col3_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode2_col3_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode2_col3_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode2_col4_title: StringProperty(
        name="四列标题",
        description="留空不显示该列",
        default="四列标题",
        update=update_preferences
    )

    panelone_mode2_col4_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode2_col4_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode2_col4_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode2_col4_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode2_col4_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode2_col4_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode2_col4_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode2_col4_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode2_col4_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode2_col4_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode2_col5_title: StringProperty(
        name="五列标题",
        description="留空不显示该列",
        default="五列标题",
        update=update_preferences
    )

    panelone_mode2_col5_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode2_col5_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode2_col5_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode2_col5_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode2_col5_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode2_col5_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode2_col5_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode2_col5_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode2_col5_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode2_col5_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode2_col6_title: StringProperty(
        name="六列标题",
        description="留空不显示该列",
        default="六列标题",
        update=update_preferences
    )

    panelone_mode2_col6_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode2_col6_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode2_col6_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode2_col6_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode2_col6_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode2_col6_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode2_col6_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode2_col6_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode2_col6_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode2_col6_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode2_col7_title: StringProperty(
        name="七列标题",
        description="留空不显示该列",
        default="七列标题",
        update=update_preferences
    )

    panelone_mode2_col7_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode2_col7_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode2_col7_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode2_col7_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode2_col7_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode2_col7_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode2_col7_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode2_col7_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode2_col7_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode2_col7_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode2_col8_title: StringProperty(
        name="八列标题",
        description="留空不显示该列",
        default="八列标题",
        update=update_preferences
    )

    panelone_mode2_col8_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode2_col8_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode2_col8_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode2_col8_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode2_col8_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode2_col8_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode2_col8_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode2_col8_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode2_col8_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode2_col8_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )
# --------↑↑↑↑ panelone_mode2_ 相关设置 ↑↑↑↑---------










# --------↓↓↓↓ panelone_mode3_ 相关设置 ↓↓↓↓---------
    panelone_mode3_visible: BoolProperty(
        name="",
        description="显示/隐藏超级面板",
        default=True,
        update=update_preferences
    )
    
    panelone_mode3_col1_title: StringProperty(
        name="一列标题",
        description="留空不显示该列",
        default="一列标题",
        update=update_preferences
    )

    panelone_mode3_col1_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode3_col1_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode3_col1_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode3_col1_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode3_col1_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode3_col1_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode3_col1_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode3_col1_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode3_col1_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode3_col1_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode3_col2_title: StringProperty(
        name="二列标题",
        description="留空不显示该列",
        default="二列标题",
        update=update_preferences
    )

    panelone_mode3_col2_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode3_col2_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode3_col2_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode3_col2_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode3_col2_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode3_col2_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode3_col2_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode3_col2_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode3_col2_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode3_col2_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode3_col3_title: StringProperty(
        name="三列标题",
        description="留空不显示该列",
        default="三列标题",
        update=update_preferences
    )

    panelone_mode3_col3_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode3_col3_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode3_col3_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode3_col3_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode3_col3_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode3_col3_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode3_col3_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode3_col3_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode3_col3_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode3_col3_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode3_col4_title: StringProperty(
        name="四列标题",
        description="留空不显示该列",
        default="四列标题",
        update=update_preferences
    )

    panelone_mode3_col4_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode3_col4_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode3_col4_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode3_col4_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode3_col4_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode3_col4_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode3_col4_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode3_col4_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode3_col4_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode3_col4_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode3_col5_title: StringProperty(
        name="五列标题",
        description="留空不显示该列",
        default="五列标题",
        update=update_preferences
    )

    panelone_mode3_col5_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode3_col5_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode3_col5_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode3_col5_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode3_col5_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode3_col5_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode3_col5_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode3_col5_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode3_col5_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode3_col5_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode3_col6_title: StringProperty(
        name="六列标题",
        description="留空不显示该列",
        default="六列标题",
        update=update_preferences
    )

    panelone_mode3_col6_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode3_col6_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode3_col6_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode3_col6_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode3_col6_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode3_col6_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode3_col6_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode3_col6_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode3_col6_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode3_col6_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode3_col7_title: StringProperty(
        name="七列标题",
        description="留空不显示该列",
        default="七列标题",
        update=update_preferences
    )

    panelone_mode3_col7_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode3_col7_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode3_col7_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode3_col7_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode3_col7_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode3_col7_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode3_col7_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode3_col7_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode3_col7_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode3_col7_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode3_col8_title: StringProperty(
        name="八列标题",
        description="留空不显示该列",
        default="八列标题",
        update=update_preferences
    )

    panelone_mode3_col8_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode3_col8_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode3_col8_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode3_col8_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode3_col8_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode3_col8_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode3_col8_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode3_col8_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode3_col8_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode3_col8_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )
# --------↑↑↑↑ panelone_mode3_ 相关设置 ↑↑↑↑---------










# --------↓↓↓↓ panelone_mode4_ 相关设置 ↓↓↓↓---------
    panelone_mode4_visible: BoolProperty(
        name="",
        description="显示/隐藏超级面板",
        default=True,
        update=update_preferences
    )
    
    panelone_mode4_col1_title: StringProperty(
        name="一列标题",
        description="留空不显示该列",
        default="一列标题",
        update=update_preferences
    )

    panelone_mode4_col1_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode4_col1_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode4_col1_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode4_col1_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode4_col1_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode4_col1_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode4_col1_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode4_col1_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode4_col1_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode4_col1_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode4_col2_title: StringProperty(
        name="二列标题",
        description="留空不显示该列",
        default="二列标题",
        update=update_preferences
    )

    panelone_mode4_col2_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode4_col2_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode4_col2_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode4_col2_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode4_col2_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode4_col2_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode4_col2_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode4_col2_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode4_col2_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode4_col2_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode4_col3_title: StringProperty(
        name="三列标题",
        description="留空不显示该列",
        default="三列标题",
        update=update_preferences
    )

    panelone_mode4_col3_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode4_col3_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode4_col3_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode4_col3_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode4_col3_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode4_col3_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode4_col3_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode4_col3_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode4_col3_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode4_col3_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode4_col4_title: StringProperty(
        name="四列标题",
        description="留空不显示该列",
        default="四列标题",
        update=update_preferences
    )

    panelone_mode4_col4_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode4_col4_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode4_col4_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode4_col4_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode4_col4_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode4_col4_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode4_col4_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode4_col4_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode4_col4_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode4_col4_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode4_col5_title: StringProperty(
        name="五列标题",
        description="留空不显示该列",
        default="五列标题",
        update=update_preferences
    )

    panelone_mode4_col5_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode4_col5_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode4_col5_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode4_col5_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode4_col5_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode4_col5_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode4_col5_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode4_col5_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode4_col5_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode4_col5_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode4_col6_title: StringProperty(
        name="六列标题",
        description="留空不显示该列",
        default="六列标题",
        update=update_preferences
    )

    panelone_mode4_col6_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode4_col6_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode4_col6_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode4_col6_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode4_col6_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode4_col6_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode4_col6_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode4_col6_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode4_col6_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode4_col6_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode4_col7_title: StringProperty(
        name="七列标题",
        description="留空不显示该列",
        default="七列标题",
        update=update_preferences
    )

    panelone_mode4_col7_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode4_col7_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode4_col7_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode4_col7_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode4_col7_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode4_col7_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode4_col7_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode4_col7_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode4_col7_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode4_col7_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode4_col8_title: StringProperty(
        name="八列标题",
        description="留空不显示该列",
        default="八列标题",
        update=update_preferences
    )

    panelone_mode4_col8_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode4_col8_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode4_col8_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode4_col8_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode4_col8_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode4_col8_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode4_col8_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode4_col8_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode4_col8_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode4_col8_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )
# --------↑↑↑↑ panelone_mode4_ 相关设置 ↑↑↑↑---------










# --------↓↓↓↓ panelone_mode5_ 相关设置 ↓↓↓↓---------
    panelone_mode5_visible: BoolProperty(
        name="",
        description="显示/隐藏超级面板",
        default=True,
        update=update_preferences
    )
    
    panelone_mode5_col1_title: StringProperty(
        name="一列标题",
        description="留空不显示该列",
        default="一列标题",
        update=update_preferences
    )

    panelone_mode5_col1_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode5_col1_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode5_col1_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode5_col1_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode5_col1_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode5_col1_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode5_col1_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode5_col1_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode5_col1_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode5_col1_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode5_col2_title: StringProperty(
        name="二列标题",
        description="留空不显示该列",
        default="二列标题",
        update=update_preferences
    )

    panelone_mode5_col2_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode5_col2_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode5_col2_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode5_col2_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode5_col2_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode5_col2_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode5_col2_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode5_col2_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode5_col2_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode5_col2_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode5_col3_title: StringProperty(
        name="三列标题",
        description="留空不显示该列",
        default="三列标题",
        update=update_preferences
    )

    panelone_mode5_col3_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode5_col3_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode5_col3_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode5_col3_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode5_col3_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode5_col3_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode5_col3_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode5_col3_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode5_col3_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode5_col3_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode5_col4_title: StringProperty(
        name="四列标题",
        description="留空不显示该列",
        default="四列标题",
        update=update_preferences
    )

    panelone_mode5_col4_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode5_col4_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode5_col4_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode5_col4_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode5_col4_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode5_col4_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode5_col4_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode5_col4_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode5_col4_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode5_col4_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode5_col5_title: StringProperty(
        name="五列标题",
        description="留空不显示该列",
        default="五列标题",
        update=update_preferences
    )

    panelone_mode5_col5_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode5_col5_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode5_col5_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode5_col5_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode5_col5_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode5_col5_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode5_col5_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode5_col5_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode5_col5_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode5_col5_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode5_col6_title: StringProperty(
        name="六列标题",
        description="留空不显示该列",
        default="六列标题",
        update=update_preferences
    )

    panelone_mode5_col6_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode5_col6_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode5_col6_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode5_col6_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode5_col6_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode5_col6_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode5_col6_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode5_col6_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode5_col6_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode5_col6_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode5_col7_title: StringProperty(
        name="七列标题",
        description="留空不显示该列",
        default="七列标题",
        update=update_preferences
    )

    panelone_mode5_col7_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode5_col7_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode5_col7_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode5_col7_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode5_col7_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode5_col7_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode5_col7_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode5_col7_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode5_col7_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode5_col7_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode5_col8_title: StringProperty(
        name="八列标题",
        description="留空不显示该列",
        default="八列标题",
        update=update_preferences
    )

    panelone_mode5_col8_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode5_col8_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode5_col8_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode5_col8_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode5_col8_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode5_col8_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode5_col8_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode5_col8_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode5_col8_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode5_col8_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )
# --------↑↑↑↑ panelone mode5 相关设置 ↑↑↑↑---------










# --------↓↓↓↓ panelone_mode6_ 相关设置 ↓↓↓↓---------
    panelone_mode6_visible: BoolProperty(
        name="",
        description="显示/隐藏超级面板",
        default=True,
        update=update_preferences
    )
    
    panelone_mode6_col1_title: StringProperty(
        name="一列标题",
        description="留空不显示该列",
        default="一列标题",
        update=update_preferences
    )

    panelone_mode6_col1_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode6_col1_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode6_col1_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode6_col1_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode6_col1_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode6_col1_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode6_col1_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode6_col1_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode6_col1_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode6_col1_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode6_col2_title: StringProperty(
        name="二列标题",
        description="留空不显示该列",
        default="二列标题",
        update=update_preferences
    )

    panelone_mode6_col2_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode6_col2_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode6_col2_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode6_col2_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode6_col2_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode6_col2_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode6_col2_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode6_col2_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode6_col2_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode6_col2_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode6_col3_title: StringProperty(
        name="三列标题",
        description="留空不显示该列",
        default="三列标题",
        update=update_preferences
    )

    panelone_mode6_col3_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode6_col3_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode6_col3_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode6_col3_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode6_col3_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode6_col3_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode6_col3_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode6_col3_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode6_col3_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode6_col3_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode6_col4_title: StringProperty(
        name="四列标题",
        description="留空不显示该列",
        default="四列标题",
        update=update_preferences
    )

    panelone_mode6_col4_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode6_col4_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode6_col4_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode6_col4_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode6_col4_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode6_col4_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode6_col4_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode6_col4_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode6_col4_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode6_col4_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode6_col5_title: StringProperty(
        name="五列标题",
        description="留空不显示该列",
        default="五列标题",
        update=update_preferences
    )

    panelone_mode6_col5_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode6_col5_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode6_col5_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode6_col5_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode6_col5_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode6_col5_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode6_col5_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode6_col5_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode6_col5_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode6_col5_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode6_col6_title: StringProperty(
        name="六列标题",
        description="留空不显示该列",
        default="六列标题",
        update=update_preferences
    )

    panelone_mode6_col6_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode6_col6_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode6_col6_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode6_col6_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode6_col6_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode6_col6_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode6_col6_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode6_col6_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode6_col6_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode6_col6_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode6_col7_title: StringProperty(
        name="七列标题",
        description="留空不显示该列",
        default="七列标题",
        update=update_preferences
    )

    panelone_mode6_col7_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode6_col7_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode6_col7_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode6_col7_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode6_col7_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode6_col7_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode6_col7_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode6_col7_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode6_col7_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode6_col7_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode6_col8_title: StringProperty(
        name="八列标题",
        description="留空不显示该列",
        default="八列标题",
        update=update_preferences
    )

    panelone_mode6_col8_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode6_col8_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode6_col8_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode6_col8_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode6_col8_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode6_col8_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode6_col8_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode6_col8_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode6_col8_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode6_col8_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )
# --------↑↑↑↑ panelone_mode6_ 相关设置 ↑↑↑↑---------










# --------↓↓↓↓ panelone_mode7_ 相关设置 ↓↓↓↓---------
    panelone_mode7_visible: BoolProperty(
        name="",
        description="显示/隐藏超级面板",
        default=True,
        update=update_preferences
    )
    
    panelone_mode7_col1_title: StringProperty(
        name="一列标题",
        description="留空不显示该列",
        default="一列标题",
        update=update_preferences
    )

    panelone_mode7_col1_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode7_col1_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode7_col1_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode7_col1_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode7_col1_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode7_col1_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode7_col1_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode7_col1_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode7_col1_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode7_col1_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode7_col2_title: StringProperty(
        name="二列标题",
        description="留空不显示该列",
        default="二列标题",
        update=update_preferences
    )

    panelone_mode7_col2_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode7_col2_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode7_col2_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode7_col2_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode7_col2_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode7_col2_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode7_col2_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode7_col2_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode7_col2_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode7_col2_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode7_col3_title: StringProperty(
        name="三列标题",
        description="留空不显示该列",
        default="三列标题",
        update=update_preferences
    )

    panelone_mode7_col3_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode7_col3_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode7_col3_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode7_col3_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode7_col3_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode7_col3_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode7_col3_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode7_col3_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode7_col3_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode7_col3_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode7_col4_title: StringProperty(
        name="四列标题",
        description="留空不显示该列",
        default="四列标题",
        update=update_preferences
    )

    panelone_mode7_col4_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode7_col4_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode7_col4_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode7_col4_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode7_col4_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode7_col4_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode7_col4_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode7_col4_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode7_col4_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode7_col4_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode7_col5_title: StringProperty(
        name="五列标题",
        description="留空不显示该列",
        default="五列标题",
        update=update_preferences
    )

    panelone_mode7_col5_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode7_col5_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode7_col5_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode7_col5_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode7_col5_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode7_col5_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode7_col5_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode7_col5_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode7_col5_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode7_col5_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode7_col6_title: StringProperty(
        name="六列标题",
        description="留空不显示该列",
        default="六列标题",
        update=update_preferences
    )

    panelone_mode7_col6_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode7_col6_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode7_col6_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode7_col6_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode7_col6_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode7_col6_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode7_col6_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode7_col6_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode7_col6_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode7_col6_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode7_col7_title: StringProperty(
        name="七列标题",
        description="留空不显示该列",
        default="七列标题",
        update=update_preferences
    )

    panelone_mode7_col7_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode7_col7_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode7_col7_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode7_col7_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode7_col7_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode7_col7_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode7_col7_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode7_col7_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode7_col7_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode7_col7_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode7_col8_title: StringProperty(
        name="八列标题",
        description="留空不显示该列",
        default="八列标题",
        update=update_preferences
    )

    panelone_mode7_col8_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode7_col8_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode7_col8_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode7_col8_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode7_col8_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode7_col8_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode7_col8_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode7_col8_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode7_col8_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode7_col8_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )
# --------↑↑↑↑ panelone_mode7_ 相关设置 ↑↑↑↑---------










# --------↓↓↓↓ panelone_mode8_ 相关设置 ↓↓↓↓---------
    panelone_mode8_visible: BoolProperty(
        name="",
        description="显示/隐藏超级面板",
        default=True,
        update=update_preferences
    )
    
    panelone_mode8_col1_title: StringProperty(
        name="一列标题",
        description="留空不显示该列",
        default="一列标题",
        update=update_preferences
    )

    panelone_mode8_col1_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode8_col1_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode8_col1_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode8_col1_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode8_col1_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode8_col1_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode8_col1_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode8_col1_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode8_col1_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode8_col1_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode8_col2_title: StringProperty(
        name="二列标题",
        description="留空不显示该列",
        default="二列标题",
        update=update_preferences
    )

    panelone_mode8_col2_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode8_col2_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode8_col2_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode8_col2_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode8_col2_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode8_col2_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode8_col2_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode8_col2_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode8_col2_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode8_col2_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode8_col3_title: StringProperty(
        name="三列标题",
        description="留空不显示该列",
        default="三列标题",
        update=update_preferences
    )

    panelone_mode8_col3_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode8_col3_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode8_col3_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode8_col3_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode8_col3_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode8_col3_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode8_col3_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode8_col3_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode8_col3_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode8_col3_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode8_col4_title: StringProperty(
        name="四列标题",
        description="留空不显示该列",
        default="四列标题",
        update=update_preferences
    )

    panelone_mode8_col4_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode8_col4_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode8_col4_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode8_col4_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode8_col4_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode8_col4_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode8_col4_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode8_col4_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode8_col4_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode8_col4_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode8_col5_title: StringProperty(
        name="五列标题",
        description="留空不显示该列",
        default="五列标题",
        update=update_preferences
    )

    panelone_mode8_col5_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode8_col5_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode8_col5_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode8_col5_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode8_col5_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode8_col5_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode8_col5_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode8_col5_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode8_col5_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode8_col5_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode8_col6_title: StringProperty(
        name="六列标题",
        description="留空不显示该列",
        default="六列标题",
        update=update_preferences
    )

    panelone_mode8_col6_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode8_col6_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode8_col6_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode8_col6_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode8_col6_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode8_col6_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode8_col6_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode8_col6_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode8_col6_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode8_col6_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode8_col7_title: StringProperty(
        name="七列标题",
        description="留空不显示该列",
        default="七列标题",
        update=update_preferences
    )

    panelone_mode8_col7_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode8_col7_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode8_col7_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode8_col7_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode8_col7_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode8_col7_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode8_col7_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode8_col7_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode8_col7_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode8_col7_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode8_col8_title: StringProperty(
        name="八列标题",
        description="留空不显示该列",
        default="八列标题",
        update=update_preferences
    )

    panelone_mode8_col8_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode8_col8_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode8_col8_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode8_col8_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode8_col8_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode8_col8_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode8_col8_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode8_col8_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode8_col8_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode8_col8_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )
# --------↑↑↑↑ panelone_mode8_ 相关设置 ↑↑↑↑---------










# --------↓↓↓↓ panelone_mode9_ 相关设置 ↓↓↓↓---------
    panelone_mode9_visible: BoolProperty(
        name="",
        description="显示/隐藏超级面板",
        default=True,
        update=update_preferences
    )
    
    panelone_mode9_col1_title: StringProperty(
        name="一列标题",
        description="留空不显示该列",
        default="一列标题",
        update=update_preferences
    )

    panelone_mode9_col1_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode9_col1_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode9_col1_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode9_col1_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode9_col1_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode9_col1_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode9_col1_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode9_col1_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode9_col1_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode9_col1_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode9_col2_title: StringProperty(
        name="二列标题",
        description="留空不显示该列",
        default="二列标题",
        update=update_preferences
    )

    panelone_mode9_col2_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode9_col2_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode9_col2_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode9_col2_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode9_col2_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode9_col2_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode9_col2_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode9_col2_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode9_col2_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode9_col2_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode9_col3_title: StringProperty(
        name="三列标题",
        description="留空不显示该列",
        default="三列标题",
        update=update_preferences
    )

    panelone_mode9_col3_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode9_col3_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode9_col3_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode9_col3_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode9_col3_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode9_col3_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode9_col3_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode9_col3_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode9_col3_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode9_col3_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode9_col4_title: StringProperty(
        name="四列标题",
        description="留空不显示该列",
        default="四列标题",
        update=update_preferences
    )

    panelone_mode9_col4_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode9_col4_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode9_col4_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode9_col4_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode9_col4_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode9_col4_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode9_col4_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode9_col4_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode9_col4_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode9_col4_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode9_col5_title: StringProperty(
        name="五列标题",
        description="留空不显示该列",
        default="五列标题",
        update=update_preferences
    )

    panelone_mode9_col5_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode9_col5_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode9_col5_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode9_col5_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode9_col5_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode9_col5_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode9_col5_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode9_col5_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode9_col5_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode9_col5_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode9_col6_title: StringProperty(
        name="六列标题",
        description="留空不显示该列",
        default="六列标题",
        update=update_preferences
    )

    panelone_mode9_col6_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode9_col6_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode9_col6_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode9_col6_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode9_col6_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode9_col6_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode9_col6_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode9_col6_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode9_col6_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode9_col6_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode9_col7_title: StringProperty(
        name="七列标题",
        description="留空不显示该列",
        default="七列标题",
        update=update_preferences
    )

    panelone_mode9_col7_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode9_col7_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode9_col7_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode9_col7_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode9_col7_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode9_col7_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode9_col7_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode9_col7_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode9_col7_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode9_col7_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode9_col8_title: StringProperty(
        name="八列标题",
        description="留空不显示该列",
        default="八列标题",
        update=update_preferences
    )

    panelone_mode9_col8_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode9_col8_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode9_col8_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode9_col8_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode9_col8_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode9_col8_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode9_col8_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode9_col8_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode9_col8_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode9_col8_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )
# --------↑↑↑↑ panelone_mode9_ 相关设置 ↑↑↑↑---------










# --------↓↓↓↓ panelone_mode10_ 相关设置 ↓↓↓↓---------
    panelone_mode10_visible: BoolProperty(
        name="",
        description="显示/隐藏超级面板",
        default=True,
        update=update_preferences
    )
    
    panelone_mode10_col1_title: StringProperty(
        name="一列标题",
        description="留空不显示该列",
        default="一列标题",
        update=update_preferences
    )

    panelone_mode10_col1_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode10_col1_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode10_col1_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode10_col1_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode10_col1_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode10_col1_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode10_col1_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode10_col1_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode10_col1_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode10_col1_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode10_col2_title: StringProperty(
        name="二列标题",
        description="留空不显示该列",
        default="二列标题",
        update=update_preferences
    )

    panelone_mode10_col2_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode10_col2_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode10_col2_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode10_col2_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode10_col2_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode10_col2_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode10_col2_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode10_col2_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode10_col2_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode10_col2_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode10_col3_title: StringProperty(
        name="三列标题",
        description="留空不显示该列",
        default="三列标题",
        update=update_preferences
    )

    panelone_mode10_col3_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode10_col3_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode10_col3_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode10_col3_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode10_col3_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode10_col3_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode10_col3_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode10_col3_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode10_col3_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode10_col3_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode10_col4_title: StringProperty(
        name="四列标题",
        description="留空不显示该列",
        default="四列标题",
        update=update_preferences
    )

    panelone_mode10_col4_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode10_col4_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode10_col4_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode10_col4_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode10_col4_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode10_col4_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode10_col4_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode10_col4_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode10_col4_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode10_col4_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode10_col5_title: StringProperty(
        name="五列标题",
        description="留空不显示该列",
        default="五列标题",
        update=update_preferences
    )

    panelone_mode10_col5_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode10_col5_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode10_col5_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode10_col5_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode10_col5_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode10_col5_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode10_col5_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode10_col5_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode10_col5_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode10_col5_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode10_col6_title: StringProperty(
        name="六列标题",
        description="留空不显示该列",
        default="六列标题",
        update=update_preferences
    )

    panelone_mode10_col6_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode10_col6_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode10_col6_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode10_col6_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode10_col6_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode10_col6_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode10_col6_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode10_col6_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode10_col6_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode10_col6_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode10_col7_title: StringProperty(
        name="七列标题",
        description="留空不显示该列",
        default="七列标题",
        update=update_preferences
    )

    panelone_mode10_col7_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode10_col7_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode10_col7_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode10_col7_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode10_col7_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode10_col7_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode10_col7_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode10_col7_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode10_col7_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode10_col7_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode10_col8_title: StringProperty(
        name="八列标题",
        description="留空不显示该列",
        default="八列标题",
        update=update_preferences
    )

    panelone_mode10_col8_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode10_col8_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode10_col8_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode10_col8_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode10_col8_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode10_col8_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode10_col8_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode10_col8_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode10_col8_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode10_col8_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )
# --------↑↑↑↑ panelone_mode10_ 相关设置 ↑↑↑↑---------










# --------↓↓↓↓ panelone_mode11_ 相关设置 ↓↓↓↓---------
    panelone_mode11_visible: BoolProperty(
        name="",
        description="显示/隐藏超级面板",
        default=True,
        update=update_preferences
    )
    
    panelone_mode11_col1_title: StringProperty(
        name="一列标题",
        description="留空不显示该列",
        default="一列标题",
        update=update_preferences
    )

    panelone_mode11_col1_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode11_col1_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode11_col1_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode11_col1_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode11_col1_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode11_col1_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode11_col1_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode11_col1_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode11_col1_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode11_col1_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode11_col2_title: StringProperty(
        name="二列标题",
        description="留空不显示该列",
        default="二列标题",
        update=update_preferences
    )

    panelone_mode11_col2_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode11_col2_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode11_col2_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode11_col2_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode11_col2_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode11_col2_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode11_col2_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode11_col2_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode11_col2_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode11_col2_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode11_col3_title: StringProperty(
        name="三列标题",
        description="留空不显示该列",
        default="三列标题",
        update=update_preferences
    )

    panelone_mode11_col3_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode11_col3_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode11_col3_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode11_col3_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode11_col3_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode11_col3_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode11_col3_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode11_col3_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode11_col3_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode11_col3_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode11_col4_title: StringProperty(
        name="四列标题",
        description="留空不显示该列",
        default="四列标题",
        update=update_preferences
    )

    panelone_mode11_col4_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode11_col4_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode11_col4_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode11_col4_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode11_col4_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode11_col4_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode11_col4_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode11_col4_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode11_col4_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode11_col4_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode11_col5_title: StringProperty(
        name="五列标题",
        description="留空不显示该列",
        default="五列标题",
        update=update_preferences
    )

    panelone_mode11_col5_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode11_col5_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode11_col5_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode11_col5_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode11_col5_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode11_col5_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode11_col5_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode11_col5_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode11_col5_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode11_col5_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode11_col6_title: StringProperty(
        name="六列标题",
        description="留空不显示该列",
        default="六列标题",
        update=update_preferences
    )

    panelone_mode11_col6_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode11_col6_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode11_col6_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode11_col6_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode11_col6_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode11_col6_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode11_col6_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode11_col6_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode11_col6_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode11_col6_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode11_col7_title: StringProperty(
        name="七列标题",
        description="留空不显示该列",
        default="七列标题",
        update=update_preferences
    )

    panelone_mode11_col7_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode11_col7_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode11_col7_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode11_col7_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode11_col7_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode11_col7_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode11_col7_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode11_col7_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode11_col7_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode11_col7_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode11_col8_title: StringProperty(
        name="八列标题",
        description="留空不显示该列",
        default="八列标题",
        update=update_preferences
    )

    panelone_mode11_col8_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode11_col8_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode11_col8_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode11_col8_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode11_col8_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode11_col8_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode11_col8_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode11_col8_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode11_col8_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode11_col8_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )
# --------↑↑↑↑ panelone_mode11_ 相关设置 ↑↑↑↑---------










# --------↓↓↓↓ panelone_mode12_ 相关设置 ↓↓↓↓---------
    panelone_mode12_visible: BoolProperty(
        name="",
        description="显示/隐藏超级面板",
        default=True,
        update=update_preferences
    )
    
    panelone_mode12_col1_title: StringProperty(
        name="一列标题",
        description="留空不显示该列",
        default="一列标题",
        update=update_preferences
    )

    panelone_mode12_col1_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode12_col1_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode12_col1_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode12_col1_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode12_col1_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode12_col1_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode12_col1_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode12_col1_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode12_col1_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode12_col1_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode12_col2_title: StringProperty(
        name="二列标题",
        description="留空不显示该列",
        default="二列标题",
        update=update_preferences
    )

    panelone_mode12_col2_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode12_col2_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode12_col2_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode12_col2_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode12_col2_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode12_col2_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode12_col2_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode12_col2_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode12_col2_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode12_col2_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode12_col3_title: StringProperty(
        name="三列标题",
        description="留空不显示该列",
        default="三列标题",
        update=update_preferences
    )

    panelone_mode12_col3_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode12_col3_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode12_col3_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode12_col3_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode12_col3_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode12_col3_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode12_col3_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode12_col3_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode12_col3_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode12_col3_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode12_col4_title: StringProperty(
        name="四列标题",
        description="留空不显示该列",
        default="四列标题",
        update=update_preferences
    )

    panelone_mode12_col4_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode12_col4_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode12_col4_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode12_col4_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode12_col4_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode12_col4_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode12_col4_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode12_col4_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode12_col4_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode12_col4_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode12_col5_title: StringProperty(
        name="五列标题",
        description="留空不显示该列",
        default="五列标题",
        update=update_preferences
    )

    panelone_mode12_col5_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode12_col5_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode12_col5_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode12_col5_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode12_col5_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode12_col5_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode12_col5_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode12_col5_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode12_col5_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode12_col5_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode12_col6_title: StringProperty(
        name="六列标题",
        description="留空不显示该列",
        default="六列标题",
        update=update_preferences
    )

    panelone_mode12_col6_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode12_col6_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode12_col6_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode12_col6_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode12_col6_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode12_col6_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode12_col6_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode12_col6_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode12_col6_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode12_col6_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode12_col7_title: StringProperty(
        name="七列标题",
        description="留空不显示该列",
        default="七列标题",
        update=update_preferences
    )

    panelone_mode12_col7_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode12_col7_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode12_col7_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode12_col7_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode12_col7_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode12_col7_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode12_col7_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode12_col7_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode12_col7_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode12_col7_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode12_col8_title: StringProperty(
        name="八列标题",
        description="留空不显示该列",
        default="八列标题",
        update=update_preferences
    )

    panelone_mode12_col8_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode12_col8_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode12_col8_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode12_col8_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode12_col8_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode12_col8_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode12_col8_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode12_col8_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode12_col8_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode12_col8_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )
# --------↑↑↑↑ panelone_mode12_ 相关设置 ↑↑↑↑---------










# --------↓↓↓↓ panelone_mode13_ 相关设置 ↓↓↓↓---------
    panelone_mode13_visible: BoolProperty(
        name="",
        description="显示/隐藏超级面板",
        default=True,
        update=update_preferences
    )
    
    panelone_mode13_col1_title: StringProperty(
        name="一列标题",
        description="留空不显示该列",
        default="一列标题",
        update=update_preferences
    )

    panelone_mode13_col1_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode13_col1_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode13_col1_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode13_col1_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode13_col1_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode13_col1_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode13_col1_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode13_col1_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode13_col1_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode13_col1_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode13_col2_title: StringProperty(
        name="二列标题",
        description="留空不显示该列",
        default="二列标题",
        update=update_preferences
    )

    panelone_mode13_col2_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode13_col2_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode13_col2_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode13_col2_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode13_col2_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode13_col2_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode13_col2_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode13_col2_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode13_col2_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode13_col2_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode13_col3_title: StringProperty(
        name="三列标题",
        description="留空不显示该列",
        default="三列标题",
        update=update_preferences
    )

    panelone_mode13_col3_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode13_col3_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode13_col3_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode13_col3_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode13_col3_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode13_col3_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode13_col3_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode13_col3_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode13_col3_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode13_col3_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode13_col4_title: StringProperty(
        name="四列标题",
        description="留空不显示该列",
        default="四列标题",
        update=update_preferences
    )

    panelone_mode13_col4_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode13_col4_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode13_col4_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode13_col4_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode13_col4_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode13_col4_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode13_col4_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode13_col4_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode13_col4_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode13_col4_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode13_col5_title: StringProperty(
        name="五列标题",
        description="留空不显示该列",
        default="五列标题",
        update=update_preferences
    )

    panelone_mode13_col5_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode13_col5_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode13_col5_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode13_col5_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode13_col5_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode13_col5_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode13_col5_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode13_col5_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode13_col5_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode13_col5_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode13_col6_title: StringProperty(
        name="六列标题",
        description="留空不显示该列",
        default="六列标题",
        update=update_preferences
    )

    panelone_mode13_col6_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode13_col6_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode13_col6_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode13_col6_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode13_col6_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode13_col6_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode13_col6_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode13_col6_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode13_col6_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode13_col6_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode13_col7_title: StringProperty(
        name="七列标题",
        description="留空不显示该列",
        default="七列标题",
        update=update_preferences
    )

    panelone_mode13_col7_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode13_col7_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode13_col7_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode13_col7_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode13_col7_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode13_col7_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode13_col7_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode13_col7_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode13_col7_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode13_col7_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode13_col8_title: StringProperty(
        name="八列标题",
        description="留空不显示该列",
        default="八列标题",
        update=update_preferences
    )

    panelone_mode13_col8_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode13_col8_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode13_col8_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode13_col8_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode13_col8_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode13_col8_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode13_col8_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode13_col8_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode13_col8_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode13_col8_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )
# --------↑↑↑↑ panelone_mode13_ 相关设置 ↑↑↑↑---------










# --------↓↓↓↓ panelone_mode14_ 相关设置 ↓↓↓↓---------
    panelone_mode14_visible: BoolProperty(
        name="",
        description="显示/隐藏超级面板",
        default=True,
        update=update_preferences
    )
    
    panelone_mode14_col1_title: StringProperty(
        name="一列标题",
        description="留空不显示该列",
        default="一列标题",
        update=update_preferences
    )

    panelone_mode14_col1_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode14_col1_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode14_col1_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode14_col1_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode14_col1_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode14_col1_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode14_col1_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode14_col1_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode14_col1_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode14_col1_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode14_col2_title: StringProperty(
        name="二列标题",
        description="留空不显示该列",
        default="二列标题",
        update=update_preferences
    )

    panelone_mode14_col2_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode14_col2_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode14_col2_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode14_col2_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode14_col2_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode14_col2_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode14_col2_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode14_col2_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode14_col2_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode14_col2_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode14_col3_title: StringProperty(
        name="三列标题",
        description="留空不显示该列",
        default="三列标题",
        update=update_preferences
    )

    panelone_mode14_col3_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode14_col3_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode14_col3_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode14_col3_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode14_col3_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode14_col3_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode14_col3_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode14_col3_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode14_col3_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode14_col3_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode14_col4_title: StringProperty(
        name="四列标题",
        description="留空不显示该列",
        default="四列标题",
        update=update_preferences
    )

    panelone_mode14_col4_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode14_col4_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode14_col4_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode14_col4_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode14_col4_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode14_col4_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode14_col4_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode14_col4_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode14_col4_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode14_col4_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode14_col5_title: StringProperty(
        name="五列标题",
        description="留空不显示该列",
        default="五列标题",
        update=update_preferences
    )

    panelone_mode14_col5_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode14_col5_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode14_col5_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode14_col5_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode14_col5_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode14_col5_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode14_col5_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode14_col5_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode14_col5_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode14_col5_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode14_col6_title: StringProperty(
        name="六列标题",
        description="留空不显示该列",
        default="六列标题",
        update=update_preferences
    )

    panelone_mode14_col6_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode14_col6_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode14_col6_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode14_col6_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode14_col6_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode14_col6_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode14_col6_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode14_col6_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode14_col6_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode14_col6_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode14_col7_title: StringProperty(
        name="七列标题",
        description="留空不显示该列",
        default="七列标题",
        update=update_preferences
    )

    panelone_mode14_col7_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode14_col7_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode14_col7_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode14_col7_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode14_col7_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode14_col7_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode14_col7_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode14_col7_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode14_col7_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode14_col7_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode14_col8_title: StringProperty(
        name="八列标题",
        description="留空不显示该列",
        default="八列标题",
        update=update_preferences
    )

    panelone_mode14_col8_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode14_col8_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode14_col8_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode14_col8_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode14_col8_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode14_col8_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode14_col8_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode14_col8_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode14_col8_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode14_col8_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )
# --------↑↑↑↑ panelone_mode14_ 相关设置 ↑↑↑↑---------










# --------↓↓↓↓ panelone_mode15_ 相关设置 ↓↓↓↓---------
    panelone_mode15_visible: BoolProperty(
        name="",
        description="显示/隐藏超级面板",
        default=True,
        update=update_preferences
    )
    
    panelone_mode15_col1_title: StringProperty(
        name="一列标题",
        description="留空不显示该列",
        default="一列标题",
        update=update_preferences
    )

    panelone_mode15_col1_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode15_col1_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode15_col1_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode15_col1_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode15_col1_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode15_col1_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode15_col1_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode15_col1_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode15_col1_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode15_col1_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode15_col2_title: StringProperty(
        name="二列标题",
        description="留空不显示该列",
        default="二列标题",
        update=update_preferences
    )

    panelone_mode15_col2_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode15_col2_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode15_col2_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode15_col2_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode15_col2_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode15_col2_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode15_col2_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode15_col2_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode15_col2_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode15_col2_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode15_col3_title: StringProperty(
        name="三列标题",
        description="留空不显示该列",
        default="三列标题",
        update=update_preferences
    )

    panelone_mode15_col3_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode15_col3_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode15_col3_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode15_col3_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode15_col3_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode15_col3_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode15_col3_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode15_col3_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode15_col3_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode15_col3_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode15_col4_title: StringProperty(
        name="四列标题",
        description="留空不显示该列",
        default="四列标题",
        update=update_preferences
    )

    panelone_mode15_col4_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode15_col4_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode15_col4_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode15_col4_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode15_col4_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode15_col4_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode15_col4_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode15_col4_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode15_col4_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode15_col4_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode15_col5_title: StringProperty(
        name="五列标题",
        description="留空不显示该列",
        default="五列标题",
        update=update_preferences
    )

    panelone_mode15_col5_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode15_col5_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode15_col5_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode15_col5_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode15_col5_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode15_col5_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode15_col5_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode15_col5_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode15_col5_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode15_col5_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode15_col6_title: StringProperty(
        name="六列标题",
        description="留空不显示该列",
        default="六列标题",
        update=update_preferences
    )

    panelone_mode15_col6_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode15_col6_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode15_col6_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode15_col6_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode15_col6_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode15_col6_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode15_col6_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode15_col6_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode15_col6_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode15_col6_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode15_col7_title: StringProperty(
        name="七列标题",
        description="留空不显示该列",
        default="七列标题",
        update=update_preferences
    )

    panelone_mode15_col7_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode15_col7_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode15_col7_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode15_col7_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode15_col7_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode15_col7_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode15_col7_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode15_col7_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode15_col7_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode15_col7_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode15_col8_title: StringProperty(
        name="八列标题",
        description="留空不显示该列",
        default="八列标题",
        update=update_preferences
    )

    panelone_mode15_col8_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode15_col8_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode15_col8_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode15_col8_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode15_col8_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode15_col8_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode15_col8_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode15_col8_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode15_col8_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode15_col8_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )
# --------↑↑↑↑ panelone_mode15_ 相关设置 ↑↑↑↑---------










# --------↓↓↓↓ panelone_mode16_ 相关设置 ↓↓↓↓---------
    panelone_mode16_visible: BoolProperty(
        name="",
        description="显示/隐藏超级面板",
        default=True,
        update=update_preferences
    )
    
    panelone_mode16_col1_title: StringProperty(
        name="一列标题",
        description="留空不显示该列",
        default="一列标题",
        update=update_preferences
    )

    panelone_mode16_col1_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode16_col1_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode16_col1_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode16_col1_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode16_col1_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode16_col1_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode16_col1_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode16_col1_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode16_col1_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode16_col1_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode16_col2_title: StringProperty(
        name="二列标题",
        description="留空不显示该列",
        default="二列标题",
        update=update_preferences
    )

    panelone_mode16_col2_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode16_col2_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode16_col2_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode16_col2_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode16_col2_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode16_col2_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode16_col2_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode16_col2_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode16_col2_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode16_col2_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode16_col3_title: StringProperty(
        name="三列标题",
        description="留空不显示该列",
        default="三列标题",
        update=update_preferences
    )

    panelone_mode16_col3_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode16_col3_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode16_col3_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode16_col3_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode16_col3_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode16_col3_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode16_col3_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode16_col3_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode16_col3_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode16_col3_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode16_col4_title: StringProperty(
        name="四列标题",
        description="留空不显示该列",
        default="四列标题",
        update=update_preferences
    )

    panelone_mode16_col4_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode16_col4_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode16_col4_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode16_col4_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode16_col4_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode16_col4_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode16_col4_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode16_col4_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode16_col4_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode16_col4_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode16_col5_title: StringProperty(
        name="五列标题",
        description="留空不显示该列",
        default="五列标题",
        update=update_preferences
    )

    panelone_mode16_col5_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode16_col5_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode16_col5_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode16_col5_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode16_col5_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode16_col5_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode16_col5_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode16_col5_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode16_col5_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode16_col5_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode16_col6_title: StringProperty(
        name="六列标题",
        description="留空不显示该列",
        default="六列标题",
        update=update_preferences
    )

    panelone_mode16_col6_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode16_col6_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode16_col6_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode16_col6_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode16_col6_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode16_col6_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode16_col6_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode16_col6_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode16_col6_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode16_col6_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode16_col7_title: StringProperty(
        name="七列标题",
        description="留空不显示该列",
        default="七列标题",
        update=update_preferences
    )

    panelone_mode16_col7_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode16_col7_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode16_col7_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode16_col7_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode16_col7_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode16_col7_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode16_col7_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode16_col7_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode16_col7_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode16_col7_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode16_col8_title: StringProperty(
        name="八列标题",
        description="留空不显示该列",
        default="八列标题",
        update=update_preferences
    )

    panelone_mode16_col8_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode16_col8_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode16_col8_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode16_col8_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode16_col8_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode16_col8_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode16_col8_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode16_col8_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode16_col8_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode16_col8_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )
# --------↑↑↑↑ panelone_mode16_ 相关设置 ↑↑↑↑---------










# --------↓↓↓↓ panelone_mode17_ 相关设置 ↓↓↓↓---------
    panelone_mode17_visible: BoolProperty(
        name="",
        description="显示/隐藏超级面板",
        default=True,
        update=update_preferences
    )
    
    panelone_mode17_col1_title: StringProperty(
        name="一列标题",
        description="留空不显示该列",
        default="一列标题",
        update=update_preferences
    )

    panelone_mode17_col1_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode17_col1_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode17_col1_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode17_col1_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode17_col1_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode17_col1_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode17_col1_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode17_col1_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode17_col1_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode17_col1_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode17_col2_title: StringProperty(
        name="二列标题",
        description="留空不显示该列",
        default="二列标题",
        update=update_preferences
    )

    panelone_mode17_col2_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode17_col2_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode17_col2_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode17_col2_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode17_col2_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode17_col2_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode17_col2_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode17_col2_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode17_col2_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode17_col2_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode17_col3_title: StringProperty(
        name="三列标题",
        description="留空不显示该列",
        default="三列标题",
        update=update_preferences
    )

    panelone_mode17_col3_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode17_col3_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode17_col3_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode17_col3_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode17_col3_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode17_col3_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode17_col3_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode17_col3_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode17_col3_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode17_col3_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode17_col4_title: StringProperty(
        name="四列标题",
        description="留空不显示该列",
        default="四列标题",
        update=update_preferences
    )

    panelone_mode17_col4_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode17_col4_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode17_col4_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode17_col4_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode17_col4_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode17_col4_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode17_col4_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode17_col4_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode17_col4_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode17_col4_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode17_col5_title: StringProperty(
        name="五列标题",
        description="留空不显示该列",
        default="五列标题",
        update=update_preferences
    )

    panelone_mode17_col5_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode17_col5_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode17_col5_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode17_col5_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode17_col5_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode17_col5_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode17_col5_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode17_col5_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode17_col5_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode17_col5_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode17_col6_title: StringProperty(
        name="六列标题",
        description="留空不显示该列",
        default="六列标题",
        update=update_preferences
    )

    panelone_mode17_col6_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode17_col6_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode17_col6_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode17_col6_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode17_col6_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode17_col6_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode17_col6_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode17_col6_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode17_col6_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode17_col6_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode17_col7_title: StringProperty(
        name="七列标题",
        description="留空不显示该列",
        default="七列标题",
        update=update_preferences
    )

    panelone_mode17_col7_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode17_col7_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode17_col7_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode17_col7_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode17_col7_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode17_col7_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode17_col7_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode17_col7_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode17_col7_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode17_col7_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode17_col8_title: StringProperty(
        name="八列标题",
        description="留空不显示该列",
        default="八列标题",
        update=update_preferences
    )

    panelone_mode17_col8_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode17_col8_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode17_col8_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode17_col8_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode17_col8_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode17_col8_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode17_col8_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode17_col8_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode17_col8_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode17_col8_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )
# --------↑↑↑↑ panelone_mode17_ 相关设置 ↑↑↑↑---------










# --------↓↓↓↓ panelone_mode18_ 相关设置 ↓↓↓↓---------
    panelone_mode18_visible: BoolProperty(
        name="",
        description="显示/隐藏超级面板",
        default=True,
        update=update_preferences
    )
    
    panelone_mode18_col1_title: StringProperty(
        name="一列标题",
        description="留空不显示该列",
        default="一列标题",
        update=update_preferences
    )

    panelone_mode18_col1_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode18_col1_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode18_col1_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode18_col1_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode18_col1_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode18_col1_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode18_col1_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode18_col1_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode18_col1_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode18_col1_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode18_col2_title: StringProperty(
        name="二列标题",
        description="留空不显示该列",
        default="二列标题",
        update=update_preferences
    )

    panelone_mode18_col2_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode18_col2_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode18_col2_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode18_col2_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode18_col2_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode18_col2_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode18_col2_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode18_col2_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode18_col2_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode18_col2_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode18_col3_title: StringProperty(
        name="三列标题",
        description="留空不显示该列",
        default="三列标题",
        update=update_preferences
    )

    panelone_mode18_col3_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode18_col3_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode18_col3_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode18_col3_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode18_col3_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode18_col3_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode18_col3_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode18_col3_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode18_col3_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode18_col3_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode18_col4_title: StringProperty(
        name="四列标题",
        description="留空不显示该列",
        default="四列标题",
        update=update_preferences
    )

    panelone_mode18_col4_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode18_col4_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode18_col4_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode18_col4_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode18_col4_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode18_col4_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode18_col4_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode18_col4_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode18_col4_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode18_col4_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode18_col5_title: StringProperty(
        name="五列标题",
        description="留空不显示该列",
        default="五列标题",
        update=update_preferences
    )

    panelone_mode18_col5_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode18_col5_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode18_col5_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode18_col5_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode18_col5_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode18_col5_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode18_col5_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode18_col5_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode18_col5_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode18_col5_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode18_col6_title: StringProperty(
        name="六列标题",
        description="留空不显示该列",
        default="六列标题",
        update=update_preferences
    )

    panelone_mode18_col6_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode18_col6_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode18_col6_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode18_col6_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode18_col6_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode18_col6_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode18_col6_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode18_col6_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode18_col6_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode18_col6_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode18_col7_title: StringProperty(
        name="七列标题",
        description="留空不显示该列",
        default="七列标题",
        update=update_preferences
    )

    panelone_mode18_col7_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode18_col7_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode18_col7_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode18_col7_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode18_col7_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode18_col7_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode18_col7_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode18_col7_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode18_col7_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode18_col7_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode18_col8_title: StringProperty(
        name="八列标题",
        description="留空不显示该列",
        default="八列标题",
        update=update_preferences
    )

    panelone_mode18_col8_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode18_col8_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode18_col8_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode18_col8_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode18_col8_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode18_col8_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode18_col8_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode18_col8_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode18_col8_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode18_col8_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )
# --------↑↑↑↑ panelone_mode18_ 相关设置 ↑↑↑↑---------










# --------↓↓↓↓ panelone_mode19_ 相关设置 ↓↓↓↓---------
    panelone_mode19_visible: BoolProperty(
        name="",
        description="显示/隐藏超级面板",
        default=True,
        update=update_preferences
    )
    
    panelone_mode19_col1_title: StringProperty(
        name="一列标题",
        description="留空不显示该列",
        default="一列标题",
        update=update_preferences
    )

    panelone_mode19_col1_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode19_col1_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode19_col1_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode19_col1_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode19_col1_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode19_col1_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode19_col1_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode19_col1_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode19_col1_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode19_col1_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode19_col2_title: StringProperty(
        name="二列标题",
        description="留空不显示该列",
        default="二列标题",
        update=update_preferences
    )

    panelone_mode19_col2_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode19_col2_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode19_col2_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode19_col2_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode19_col2_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode19_col2_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode19_col2_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode19_col2_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode19_col2_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode19_col2_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode19_col3_title: StringProperty(
        name="三列标题",
        description="留空不显示该列",
        default="三列标题",
        update=update_preferences
    )

    panelone_mode19_col3_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode19_col3_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode19_col3_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode19_col3_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode19_col3_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode19_col3_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode19_col3_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode19_col3_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode19_col3_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode19_col3_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode19_col4_title: StringProperty(
        name="四列标题",
        description="留空不显示该列",
        default="四列标题",
        update=update_preferences
    )

    panelone_mode19_col4_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode19_col4_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode19_col4_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode19_col4_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode19_col4_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode19_col4_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode19_col4_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode19_col4_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode19_col4_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode19_col4_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode19_col5_title: StringProperty(
        name="五列标题",
        description="留空不显示该列",
        default="五列标题",
        update=update_preferences
    )

    panelone_mode19_col5_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode19_col5_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode19_col5_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode19_col5_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode19_col5_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode19_col5_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode19_col5_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode19_col5_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode19_col5_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode19_col5_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode19_col6_title: StringProperty(
        name="六列标题",
        description="留空不显示该列",
        default="六列标题",
        update=update_preferences
    )

    panelone_mode19_col6_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode19_col6_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode19_col6_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode19_col6_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode19_col6_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode19_col6_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode19_col6_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode19_col6_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode19_col6_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode19_col6_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode19_col7_title: StringProperty(
        name="七列标题",
        description="留空不显示该列",
        default="七列标题",
        update=update_preferences
    )

    panelone_mode19_col7_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode19_col7_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode19_col7_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode19_col7_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode19_col7_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode19_col7_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode19_col7_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode19_col7_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode19_col7_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode19_col7_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode19_col8_title: StringProperty(
        name="八列标题",
        description="留空不显示该列",
        default="八列标题",
        update=update_preferences
    )

    panelone_mode19_col8_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode19_col8_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode19_col8_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode19_col8_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode19_col8_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode19_col8_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode19_col8_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode19_col8_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode19_col8_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode19_col8_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )
# --------↑↑↑↑ panelone_mode19_ 相关设置 ↑↑↑↑---------










# --------↓↓↓↓ panelone_mode20_ 相关设置 ↓↓↓↓---------
    panelone_mode20_visible: BoolProperty(
        name="",
        description="显示/隐藏超级面板",
        default=True,
        update=update_preferences
    )
    
    panelone_mode20_col1_title: StringProperty(
        name="一列标题",
        description="留空不显示该列",
        default="一列标题",
        update=update_preferences
    )

    panelone_mode20_col1_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode20_col1_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode20_col1_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode20_col1_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode20_col1_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode20_col1_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode20_col1_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode20_col1_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode20_col1_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode20_col1_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode20_col2_title: StringProperty(
        name="二列标题",
        description="留空不显示该列",
        default="二列标题",
        update=update_preferences
    )

    panelone_mode20_col2_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode20_col2_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode20_col2_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode20_col2_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode20_col2_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode20_col2_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode20_col2_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode20_col2_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode20_col2_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode20_col2_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode20_col3_title: StringProperty(
        name="三列标题",
        description="留空不显示该列",
        default="三列标题",
        update=update_preferences
    )

    panelone_mode20_col3_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode20_col3_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode20_col3_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode20_col3_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode20_col3_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode20_col3_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode20_col3_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode20_col3_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode20_col3_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode20_col3_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode20_col4_title: StringProperty(
        name="四列标题",
        description="留空不显示该列",
        default="四列标题",
        update=update_preferences
    )

    panelone_mode20_col4_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode20_col4_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode20_col4_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode20_col4_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode20_col4_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode20_col4_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode20_col4_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode20_col4_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode20_col4_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode20_col4_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode20_col5_title: StringProperty(
        name="五列标题",
        description="留空不显示该列",
        default="五列标题",
        update=update_preferences
    )

    panelone_mode20_col5_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode20_col5_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode20_col5_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode20_col5_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode20_col5_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode20_col5_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode20_col5_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode20_col5_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode20_col5_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode20_col5_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode20_col6_title: StringProperty(
        name="六列标题",
        description="留空不显示该列",
        default="六列标题",
        update=update_preferences
    )

    panelone_mode20_col6_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode20_col6_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode20_col6_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode20_col6_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode20_col6_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode20_col6_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode20_col6_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode20_col6_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode20_col6_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode20_col6_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode20_col7_title: StringProperty(
        name="七列标题",
        description="留空不显示该列",
        default="七列标题",
        update=update_preferences
    )

    panelone_mode20_col7_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode20_col7_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode20_col7_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode20_col7_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode20_col7_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode20_col7_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode20_col7_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode20_col7_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode20_col7_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode20_col7_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode20_col8_title: StringProperty(
        name="八列标题",
        description="留空不显示该列",
        default="八列标题",
        update=update_preferences
    )

    panelone_mode20_col8_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode20_col8_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode20_col8_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode20_col8_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode20_col8_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode20_col8_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode20_col8_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode20_col8_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode20_col8_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode20_col8_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )
# --------↑↑↑↑ panelone_mode20_ 相关设置 ↑↑↑↑---------










# --------↓↓↓↓ panelone_mode21_ 相关设置 ↓↓↓↓---------
    panelone_mode21_visible: BoolProperty(
        name="",
        description="显示/隐藏超级面板",
        default=True,
        update=update_preferences
    )
    
    panelone_mode21_col1_title: StringProperty(
        name="一列标题",
        description="留空不显示该列",
        default="一列标题",
        update=update_preferences
    )

    panelone_mode21_col1_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode21_col1_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode21_col1_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode21_col1_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode21_col1_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode21_col1_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode21_col1_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode21_col1_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode21_col1_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode21_col1_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode21_col2_title: StringProperty(
        name="二列标题",
        description="留空不显示该列",
        default="二列标题",
        update=update_preferences
    )

    panelone_mode21_col2_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode21_col2_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode21_col2_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode21_col2_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode21_col2_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode21_col2_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode21_col2_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode21_col2_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode21_col2_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode21_col2_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode21_col3_title: StringProperty(
        name="三列标题",
        description="留空不显示该列",
        default="三列标题",
        update=update_preferences
    )

    panelone_mode21_col3_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode21_col3_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode21_col3_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode21_col3_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode21_col3_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode21_col3_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode21_col3_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode21_col3_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode21_col3_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode21_col3_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode21_col4_title: StringProperty(
        name="四列标题",
        description="留空不显示该列",
        default="四列标题",
        update=update_preferences
    )

    panelone_mode21_col4_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode21_col4_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode21_col4_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode21_col4_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode21_col4_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode21_col4_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode21_col4_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode21_col4_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode21_col4_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode21_col4_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode21_col5_title: StringProperty(
        name="五列标题",
        description="留空不显示该列",
        default="五列标题",
        update=update_preferences
    )

    panelone_mode21_col5_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode21_col5_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode21_col5_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode21_col5_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode21_col5_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode21_col5_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode21_col5_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode21_col5_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode21_col5_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode21_col5_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode21_col6_title: StringProperty(
        name="六列标题",
        description="留空不显示该列",
        default="六列标题",
        update=update_preferences
    )

    panelone_mode21_col6_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode21_col6_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode21_col6_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode21_col6_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode21_col6_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode21_col6_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode21_col6_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode21_col6_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode21_col6_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode21_col6_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode21_col7_title: StringProperty(
        name="七列标题",
        description="留空不显示该列",
        default="七列标题",
        update=update_preferences
    )

    panelone_mode21_col7_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode21_col7_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode21_col7_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode21_col7_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode21_col7_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode21_col7_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode21_col7_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode21_col7_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode21_col7_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode21_col7_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode21_col8_title: StringProperty(
        name="八列标题",
        description="留空不显示该列",
        default="八列标题",
        update=update_preferences
    )

    panelone_mode21_col8_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode21_col8_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode21_col8_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode21_col8_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode21_col8_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode21_col8_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode21_col8_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode21_col8_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode21_col8_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode21_col8_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )
# --------↑↑↑↑ panelone_mode21_ 相关设置 ↑↑↑↑---------










# --------↓↓↓↓ panelone_mode22_ 相关设置 ↓↓↓↓---------
    panelone_mode22_visible: BoolProperty(
        name="",
        description="显示/隐藏超级面板",
        default=True,
        update=update_preferences
    )
    
    panelone_mode22_col1_title: StringProperty(
        name="一列标题",
        description="留空不显示该列",
        default="一列标题",
        update=update_preferences
    )

    panelone_mode22_col1_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode22_col1_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode22_col1_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode22_col1_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode22_col1_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode22_col1_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode22_col1_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode22_col1_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode22_col1_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode22_col1_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode22_col2_title: StringProperty(
        name="二列标题",
        description="留空不显示该列",
        default="二列标题",
        update=update_preferences
    )

    panelone_mode22_col2_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode22_col2_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode22_col2_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode22_col2_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode22_col2_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode22_col2_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode22_col2_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode22_col2_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode22_col2_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode22_col2_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode22_col3_title: StringProperty(
        name="三列标题",
        description="留空不显示该列",
        default="三列标题",
        update=update_preferences
    )

    panelone_mode22_col3_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode22_col3_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode22_col3_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode22_col3_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode22_col3_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode22_col3_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode22_col3_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode22_col3_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode22_col3_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode22_col3_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode22_col4_title: StringProperty(
        name="四列标题",
        description="留空不显示该列",
        default="四列标题",
        update=update_preferences
    )

    panelone_mode22_col4_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode22_col4_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode22_col4_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode22_col4_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode22_col4_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode22_col4_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode22_col4_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode22_col4_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode22_col4_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode22_col4_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode22_col5_title: StringProperty(
        name="五列标题",
        description="留空不显示该列",
        default="五列标题",
        update=update_preferences
    )

    panelone_mode22_col5_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode22_col5_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode22_col5_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode22_col5_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode22_col5_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode22_col5_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode22_col5_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode22_col5_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode22_col5_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode22_col5_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode22_col6_title: StringProperty(
        name="六列标题",
        description="留空不显示该列",
        default="六列标题",
        update=update_preferences
    )

    panelone_mode22_col6_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode22_col6_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode22_col6_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode22_col6_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode22_col6_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode22_col6_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode22_col6_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode22_col6_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode22_col6_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode22_col6_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode22_col7_title: StringProperty(
        name="七列标题",
        description="留空不显示该列",
        default="七列标题",
        update=update_preferences
    )

    panelone_mode22_col7_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode22_col7_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode22_col7_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode22_col7_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode22_col7_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode22_col7_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode22_col7_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode22_col7_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode22_col7_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode22_col7_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode22_col8_title: StringProperty(
        name="八列标题",
        description="留空不显示该列",
        default="八列标题",
        update=update_preferences
    )

    panelone_mode22_col8_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode22_col8_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode22_col8_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode22_col8_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode22_col8_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode22_col8_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode22_col8_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode22_col8_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode22_col8_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode22_col8_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )
# --------↑↑↑↑ panelone_mode22_ 相关设置 ↑↑↑↑---------










# --------↓↓↓↓ panelone_mode23_ 相关设置 ↓↓↓↓---------
    panelone_mode23_visible: BoolProperty(
        name="",
        description="显示/隐藏超级面板",
        default=True,
        update=update_preferences
    )
    
    panelone_mode23_col1_title: StringProperty(
        name="一列标题",
        description="留空不显示该列",
        default="一列标题",
        update=update_preferences
    )

    panelone_mode23_col1_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode23_col1_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode23_col1_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode23_col1_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode23_col1_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode23_col1_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode23_col1_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode23_col1_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode23_col1_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode23_col1_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode23_col2_title: StringProperty(
        name="二列标题",
        description="留空不显示该列",
        default="二列标题",
        update=update_preferences
    )

    panelone_mode23_col2_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode23_col2_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode23_col2_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode23_col2_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode23_col2_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode23_col2_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode23_col2_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode23_col2_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode23_col2_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode23_col2_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode23_col3_title: StringProperty(
        name="三列标题",
        description="留空不显示该列",
        default="三列标题",
        update=update_preferences
    )

    panelone_mode23_col3_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode23_col3_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode23_col3_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode23_col3_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode23_col3_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode23_col3_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode23_col3_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode23_col3_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode23_col3_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode23_col3_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode23_col4_title: StringProperty(
        name="四列标题",
        description="留空不显示该列",
        default="四列标题",
        update=update_preferences
    )

    panelone_mode23_col4_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode23_col4_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode23_col4_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode23_col4_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode23_col4_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode23_col4_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode23_col4_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode23_col4_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode23_col4_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode23_col4_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode23_col5_title: StringProperty(
        name="五列标题",
        description="留空不显示该列",
        default="五列标题",
        update=update_preferences
    )

    panelone_mode23_col5_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode23_col5_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode23_col5_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode23_col5_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode23_col5_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode23_col5_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode23_col5_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode23_col5_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode23_col5_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode23_col5_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode23_col6_title: StringProperty(
        name="六列标题",
        description="留空不显示该列",
        default="六列标题",
        update=update_preferences
    )

    panelone_mode23_col6_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode23_col6_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode23_col6_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode23_col6_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode23_col6_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode23_col6_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode23_col6_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode23_col6_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode23_col6_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode23_col6_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode23_col7_title: StringProperty(
        name="七列标题",
        description="留空不显示该列",
        default="七列标题",
        update=update_preferences
    )

    panelone_mode23_col7_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode23_col7_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode23_col7_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode23_col7_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode23_col7_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode23_col7_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode23_col7_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode23_col7_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode23_col7_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode23_col7_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode23_col8_title: StringProperty(
        name="八列标题",
        description="留空不显示该列",
        default="八列标题",
        update=update_preferences
    )

    panelone_mode23_col8_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode23_col8_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode23_col8_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode23_col8_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode23_col8_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode23_col8_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode23_col8_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode23_col8_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode23_col8_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    panelone_mode23_col8_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )
# --------↑↑↑↑ panelone_mode23_ 相关设置 ↑↑↑↑---------


#============================================================









# --------↓↓↓↓ paneltwo_mode1 相关设置 ↓↓↓↓---------
    paneltwo_mode1_visible: BoolProperty(
        name="",
        description="显示/隐藏超级面板",
        default=True,
        update=update_preferences
    )

    paneltwo_mode1_col1_title: StringProperty(
        name="一列标题",
        description="留空不显示该列",
        default="一列标题",
        update=update_preferences
    )

    paneltwo_mode1_col1_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode1_col1_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode1_col1_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode1_col1_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode1_col1_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode1_col1_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode1_col1_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode1_col1_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode1_col1_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode1_col1_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode1_col2_title: StringProperty(
        name="二列标题",
        description="留空不显示该列",
        default="二列标题",
        update=update_preferences
    )

    paneltwo_mode1_col2_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode1_col2_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode1_col2_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode1_col2_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode1_col2_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode1_col2_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode1_col2_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode1_col2_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode1_col2_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode1_col2_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode1_col3_title: StringProperty(
        name="三列标题",
        description="留空不显示该列",
        default="三列标题",
        update=update_preferences
    )

    paneltwo_mode1_col3_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode1_col3_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode1_col3_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode1_col3_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode1_col3_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode1_col3_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode1_col3_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode1_col3_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode1_col3_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode1_col3_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode1_col4_title: StringProperty(
        name="四列标题",
        description="留空不显示该列",
        default="四列标题",
        update=update_preferences
    )

    paneltwo_mode1_col4_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode1_col4_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode1_col4_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode1_col4_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode1_col4_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode1_col4_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode1_col4_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode1_col4_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode1_col4_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode1_col4_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode1_col5_title: StringProperty(
        name="五列标题",
        description="留空不显示该列",
        default="五列标题",
        update=update_preferences
    )

    paneltwo_mode1_col5_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode1_col5_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode1_col5_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode1_col5_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode1_col5_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode1_col5_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode1_col5_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode1_col5_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode1_col5_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode1_col5_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode1_col6_title: StringProperty(
        name="六列标题",
        description="留空不显示该列",
        default="六列标题",
        update=update_preferences
    )

    paneltwo_mode1_col6_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode1_col6_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode1_col6_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode1_col6_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode1_col6_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode1_col6_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode1_col6_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode1_col6_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode1_col6_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode1_col6_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode1_col7_title: StringProperty(
        name="七列标题",
        description="留空不显示该列",
        default="七列标题",
        update=update_preferences
    )

    paneltwo_mode1_col7_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode1_col7_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode1_col7_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode1_col7_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode1_col7_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode1_col7_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode1_col7_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode1_col7_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode1_col7_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode1_col7_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode1_col8_title: StringProperty(
        name="八列标题",
        description="留空不显示该列",
        default="八列标题",
        update=update_preferences
    )

    paneltwo_mode1_col8_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode1_col8_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode1_col8_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode1_col8_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode1_col8_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode1_col8_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode1_col8_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode1_col8_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode1_col8_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode1_col8_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

# --------↑↑↑↑ paneltwo_mode1 相关设置 ↑↑↑↑---------













# --------↓↓↓↓ paneltwo_mode2 相关设置 ↓↓↓↓---------
    paneltwo_mode2_visible: BoolProperty(
        name="",
        description="显示/隐藏超级面板",
        default=True,
        update=update_preferences
    )
    
    paneltwo_mode2_col1_title: StringProperty(
        name="一列标题",
        description="留空不显示该列",
        default="一列标题",
        update=update_preferences
    )

    paneltwo_mode2_col1_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode2_col1_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode2_col1_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode2_col1_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode2_col1_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode2_col1_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode2_col1_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode2_col1_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode2_col1_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode2_col1_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode2_col2_title: StringProperty(
        name="二列标题",
        description="留空不显示该列",
        default="二列标题",
        update=update_preferences
    )

    paneltwo_mode2_col2_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode2_col2_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode2_col2_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode2_col2_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode2_col2_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode2_col2_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode2_col2_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode2_col2_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode2_col2_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode2_col2_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode2_col3_title: StringProperty(
        name="三列标题",
        description="留空不显示该列",
        default="三列标题",
        update=update_preferences
    )

    paneltwo_mode2_col3_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode2_col3_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode2_col3_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode2_col3_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode2_col3_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode2_col3_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode2_col3_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode2_col3_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode2_col3_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode2_col3_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode2_col4_title: StringProperty(
        name="四列标题",
        description="留空不显示该列",
        default="四列标题",
        update=update_preferences
    )

    paneltwo_mode2_col4_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode2_col4_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode2_col4_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode2_col4_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode2_col4_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode2_col4_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode2_col4_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode2_col4_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode2_col4_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode2_col4_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode2_col5_title: StringProperty(
        name="五列标题",
        description="留空不显示该列",
        default="五列标题",
        update=update_preferences
    )

    paneltwo_mode2_col5_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode2_col5_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode2_col5_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode2_col5_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode2_col5_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode2_col5_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode2_col5_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode2_col5_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode2_col5_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode2_col5_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode2_col6_title: StringProperty(
        name="六列标题",
        description="留空不显示该列",
        default="六列标题",
        update=update_preferences
    )

    paneltwo_mode2_col6_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode2_col6_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode2_col6_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode2_col6_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode2_col6_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode2_col6_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode2_col6_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode2_col6_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode2_col6_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode2_col6_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode2_col7_title: StringProperty(
        name="七列标题",
        description="留空不显示该列",
        default="七列标题",
        update=update_preferences
    )

    paneltwo_mode2_col7_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode2_col7_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode2_col7_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode2_col7_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode2_col7_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode2_col7_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode2_col7_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode2_col7_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode2_col7_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode2_col7_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode2_col8_title: StringProperty(
        name="八列标题",
        description="留空不显示该列",
        default="八列标题",
        update=update_preferences
    )

    paneltwo_mode2_col8_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode2_col8_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode2_col8_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode2_col8_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode2_col8_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode2_col8_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode2_col8_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode2_col8_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode2_col8_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode2_col8_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )
# --------↑↑↑↑ paneltwo_mode2_ 相关设置 ↑↑↑↑---------










# --------↓↓↓↓ paneltwo_mode3_ 相关设置 ↓↓↓↓---------
    paneltwo_mode3_visible: BoolProperty(
        name="",
        description="显示/隐藏超级面板",
        default=True,
        update=update_preferences
    )
    
    paneltwo_mode3_col1_title: StringProperty(
        name="一列标题",
        description="留空不显示该列",
        default="一列标题",
        update=update_preferences
    )

    paneltwo_mode3_col1_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode3_col1_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode3_col1_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode3_col1_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode3_col1_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode3_col1_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode3_col1_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode3_col1_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode3_col1_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode3_col1_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode3_col2_title: StringProperty(
        name="二列标题",
        description="留空不显示该列",
        default="二列标题",
        update=update_preferences
    )

    paneltwo_mode3_col2_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode3_col2_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode3_col2_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode3_col2_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode3_col2_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode3_col2_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode3_col2_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode3_col2_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode3_col2_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode3_col2_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode3_col3_title: StringProperty(
        name="三列标题",
        description="留空不显示该列",
        default="三列标题",
        update=update_preferences
    )

    paneltwo_mode3_col3_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode3_col3_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode3_col3_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode3_col3_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode3_col3_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode3_col3_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode3_col3_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode3_col3_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode3_col3_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode3_col3_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode3_col4_title: StringProperty(
        name="四列标题",
        description="留空不显示该列",
        default="四列标题",
        update=update_preferences
    )

    paneltwo_mode3_col4_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode3_col4_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode3_col4_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode3_col4_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode3_col4_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode3_col4_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode3_col4_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode3_col4_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode3_col4_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode3_col4_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode3_col5_title: StringProperty(
        name="五列标题",
        description="留空不显示该列",
        default="五列标题",
        update=update_preferences
    )

    paneltwo_mode3_col5_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode3_col5_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode3_col5_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode3_col5_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode3_col5_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode3_col5_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode3_col5_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode3_col5_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode3_col5_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode3_col5_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode3_col6_title: StringProperty(
        name="六列标题",
        description="留空不显示该列",
        default="六列标题",
        update=update_preferences
    )

    paneltwo_mode3_col6_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode3_col6_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode3_col6_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode3_col6_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode3_col6_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode3_col6_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode3_col6_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode3_col6_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode3_col6_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode3_col6_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode3_col7_title: StringProperty(
        name="七列标题",
        description="留空不显示该列",
        default="七列标题",
        update=update_preferences
    )

    paneltwo_mode3_col7_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode3_col7_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode3_col7_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode3_col7_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode3_col7_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode3_col7_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode3_col7_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode3_col7_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode3_col7_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode3_col7_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode3_col8_title: StringProperty(
        name="八列标题",
        description="留空不显示该列",
        default="八列标题",
        update=update_preferences
    )

    paneltwo_mode3_col8_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode3_col8_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode3_col8_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode3_col8_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode3_col8_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode3_col8_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode3_col8_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode3_col8_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode3_col8_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode3_col8_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )
# --------↑↑↑↑ paneltwo_mode3_ 相关设置 ↑↑↑↑---------










# --------↓↓↓↓ paneltwo_mode4_ 相关设置 ↓↓↓↓---------
    paneltwo_mode4_visible: BoolProperty(
        name="",
        description="显示/隐藏超级面板",
        default=True,
        update=update_preferences
    )
    
    paneltwo_mode4_col1_title: StringProperty(
        name="一列标题",
        description="留空不显示该列",
        default="一列标题",
        update=update_preferences
    )

    paneltwo_mode4_col1_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode4_col1_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode4_col1_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode4_col1_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode4_col1_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode4_col1_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode4_col1_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode4_col1_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode4_col1_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode4_col1_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode4_col2_title: StringProperty(
        name="二列标题",
        description="留空不显示该列",
        default="二列标题",
        update=update_preferences
    )

    paneltwo_mode4_col2_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode4_col2_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode4_col2_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode4_col2_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode4_col2_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode4_col2_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode4_col2_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode4_col2_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode4_col2_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode4_col2_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode4_col3_title: StringProperty(
        name="三列标题",
        description="留空不显示该列",
        default="三列标题",
        update=update_preferences
    )

    paneltwo_mode4_col3_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode4_col3_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode4_col3_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode4_col3_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode4_col3_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode4_col3_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode4_col3_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode4_col3_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode4_col3_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode4_col3_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode4_col4_title: StringProperty(
        name="四列标题",
        description="留空不显示该列",
        default="四列标题",
        update=update_preferences
    )

    paneltwo_mode4_col4_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode4_col4_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode4_col4_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode4_col4_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode4_col4_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode4_col4_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode4_col4_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode4_col4_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode4_col4_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode4_col4_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode4_col5_title: StringProperty(
        name="五列标题",
        description="留空不显示该列",
        default="五列标题",
        update=update_preferences
    )

    paneltwo_mode4_col5_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode4_col5_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode4_col5_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode4_col5_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode4_col5_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode4_col5_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode4_col5_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode4_col5_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode4_col5_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode4_col5_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode4_col6_title: StringProperty(
        name="六列标题",
        description="留空不显示该列",
        default="六列标题",
        update=update_preferences
    )

    paneltwo_mode4_col6_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode4_col6_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode4_col6_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode4_col6_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode4_col6_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode4_col6_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode4_col6_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode4_col6_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode4_col6_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode4_col6_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode4_col7_title: StringProperty(
        name="七列标题",
        description="留空不显示该列",
        default="七列标题",
        update=update_preferences
    )

    paneltwo_mode4_col7_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode4_col7_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode4_col7_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode4_col7_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode4_col7_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode4_col7_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode4_col7_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode4_col7_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode4_col7_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode4_col7_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode4_col8_title: StringProperty(
        name="八列标题",
        description="留空不显示该列",
        default="八列标题",
        update=update_preferences
    )

    paneltwo_mode4_col8_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode4_col8_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode4_col8_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode4_col8_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode4_col8_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode4_col8_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode4_col8_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode4_col8_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode4_col8_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode4_col8_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )
# --------↑↑↑↑ paneltwo_mode4_ 相关设置 ↑↑↑↑---------










# --------↓↓↓↓ paneltwo_mode5_ 相关设置 ↓↓↓↓---------
    paneltwo_mode5_visible: BoolProperty(
        name="",
        description="显示/隐藏超级面板",
        default=True,
        update=update_preferences
    )
    
    paneltwo_mode5_col1_title: StringProperty(
        name="一列标题",
        description="留空不显示该列",
        default="一列标题",
        update=update_preferences
    )

    paneltwo_mode5_col1_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode5_col1_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode5_col1_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode5_col1_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode5_col1_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode5_col1_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode5_col1_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode5_col1_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode5_col1_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode5_col1_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode5_col2_title: StringProperty(
        name="二列标题",
        description="留空不显示该列",
        default="二列标题",
        update=update_preferences
    )

    paneltwo_mode5_col2_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode5_col2_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode5_col2_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode5_col2_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode5_col2_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode5_col2_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode5_col2_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode5_col2_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode5_col2_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode5_col2_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode5_col3_title: StringProperty(
        name="三列标题",
        description="留空不显示该列",
        default="三列标题",
        update=update_preferences
    )

    paneltwo_mode5_col3_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode5_col3_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode5_col3_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode5_col3_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode5_col3_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode5_col3_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode5_col3_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode5_col3_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode5_col3_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode5_col3_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode5_col4_title: StringProperty(
        name="四列标题",
        description="留空不显示该列",
        default="四列标题",
        update=update_preferences
    )

    paneltwo_mode5_col4_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode5_col4_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode5_col4_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode5_col4_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode5_col4_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode5_col4_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode5_col4_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode5_col4_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode5_col4_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode5_col4_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode5_col5_title: StringProperty(
        name="五列标题",
        description="留空不显示该列",
        default="五列标题",
        update=update_preferences
    )

    paneltwo_mode5_col5_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode5_col5_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode5_col5_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode5_col5_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode5_col5_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode5_col5_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode5_col5_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode5_col5_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode5_col5_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode5_col5_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode5_col6_title: StringProperty(
        name="六列标题",
        description="留空不显示该列",
        default="六列标题",
        update=update_preferences
    )

    paneltwo_mode5_col6_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode5_col6_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode5_col6_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode5_col6_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode5_col6_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode5_col6_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode5_col6_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode5_col6_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode5_col6_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode5_col6_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode5_col7_title: StringProperty(
        name="七列标题",
        description="留空不显示该列",
        default="七列标题",
        update=update_preferences
    )

    paneltwo_mode5_col7_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode5_col7_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode5_col7_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode5_col7_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode5_col7_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode5_col7_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode5_col7_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode5_col7_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode5_col7_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode5_col7_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode5_col8_title: StringProperty(
        name="八列标题",
        description="留空不显示该列",
        default="八列标题",
        update=update_preferences
    )

    paneltwo_mode5_col8_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode5_col8_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode5_col8_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode5_col8_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode5_col8_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode5_col8_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode5_col8_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode5_col8_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode5_col8_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode5_col8_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )
# --------↑↑↑↑ panelone mode5 相关设置 ↑↑↑↑---------










# --------↓↓↓↓ paneltwo_mode6_ 相关设置 ↓↓↓↓---------
    paneltwo_mode6_visible: BoolProperty(
        name="",
        description="显示/隐藏超级面板",
        default=True,
        update=update_preferences
    )
    
    paneltwo_mode6_col1_title: StringProperty(
        name="一列标题",
        description="留空不显示该列",
        default="一列标题",
        update=update_preferences
    )

    paneltwo_mode6_col1_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode6_col1_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode6_col1_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode6_col1_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode6_col1_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode6_col1_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode6_col1_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode6_col1_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode6_col1_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode6_col1_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode6_col2_title: StringProperty(
        name="二列标题",
        description="留空不显示该列",
        default="二列标题",
        update=update_preferences
    )

    paneltwo_mode6_col2_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode6_col2_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode6_col2_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode6_col2_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode6_col2_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode6_col2_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode6_col2_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode6_col2_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode6_col2_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode6_col2_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode6_col3_title: StringProperty(
        name="三列标题",
        description="留空不显示该列",
        default="三列标题",
        update=update_preferences
    )

    paneltwo_mode6_col3_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode6_col3_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode6_col3_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode6_col3_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode6_col3_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode6_col3_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode6_col3_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode6_col3_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode6_col3_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode6_col3_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode6_col4_title: StringProperty(
        name="四列标题",
        description="留空不显示该列",
        default="四列标题",
        update=update_preferences
    )

    paneltwo_mode6_col4_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode6_col4_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode6_col4_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode6_col4_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode6_col4_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode6_col4_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode6_col4_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode6_col4_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode6_col4_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode6_col4_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode6_col5_title: StringProperty(
        name="五列标题",
        description="留空不显示该列",
        default="五列标题",
        update=update_preferences
    )

    paneltwo_mode6_col5_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode6_col5_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode6_col5_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode6_col5_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode6_col5_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode6_col5_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode6_col5_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode6_col5_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode6_col5_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode6_col5_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode6_col6_title: StringProperty(
        name="六列标题",
        description="留空不显示该列",
        default="六列标题",
        update=update_preferences
    )

    paneltwo_mode6_col6_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode6_col6_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode6_col6_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode6_col6_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode6_col6_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode6_col6_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode6_col6_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode6_col6_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode6_col6_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode6_col6_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode6_col7_title: StringProperty(
        name="七列标题",
        description="留空不显示该列",
        default="七列标题",
        update=update_preferences
    )

    paneltwo_mode6_col7_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode6_col7_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode6_col7_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode6_col7_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode6_col7_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode6_col7_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode6_col7_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode6_col7_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode6_col7_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode6_col7_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode6_col8_title: StringProperty(
        name="八列标题",
        description="留空不显示该列",
        default="八列标题",
        update=update_preferences
    )

    paneltwo_mode6_col8_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode6_col8_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode6_col8_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode6_col8_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode6_col8_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode6_col8_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode6_col8_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode6_col8_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode6_col8_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode6_col8_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )
# --------↑↑↑↑ paneltwo_mode6_ 相关设置 ↑↑↑↑---------










# --------↓↓↓↓ paneltwo_mode7_ 相关设置 ↓↓↓↓---------
    paneltwo_mode7_visible: BoolProperty(
        name="",
        description="显示/隐藏超级面板",
        default=True,
        update=update_preferences
    )
    
    paneltwo_mode7_col1_title: StringProperty(
        name="一列标题",
        description="留空不显示该列",
        default="一列标题",
        update=update_preferences
    )

    paneltwo_mode7_col1_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode7_col1_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode7_col1_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode7_col1_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode7_col1_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode7_col1_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode7_col1_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode7_col1_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode7_col1_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode7_col1_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode7_col2_title: StringProperty(
        name="二列标题",
        description="留空不显示该列",
        default="二列标题",
        update=update_preferences
    )

    paneltwo_mode7_col2_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode7_col2_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode7_col2_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode7_col2_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode7_col2_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode7_col2_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode7_col2_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode7_col2_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode7_col2_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode7_col2_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode7_col3_title: StringProperty(
        name="三列标题",
        description="留空不显示该列",
        default="三列标题",
        update=update_preferences
    )

    paneltwo_mode7_col3_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode7_col3_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode7_col3_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode7_col3_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode7_col3_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode7_col3_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode7_col3_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode7_col3_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode7_col3_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode7_col3_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode7_col4_title: StringProperty(
        name="四列标题",
        description="留空不显示该列",
        default="四列标题",
        update=update_preferences
    )

    paneltwo_mode7_col4_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode7_col4_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode7_col4_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode7_col4_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode7_col4_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode7_col4_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode7_col4_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode7_col4_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode7_col4_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode7_col4_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode7_col5_title: StringProperty(
        name="五列标题",
        description="留空不显示该列",
        default="五列标题",
        update=update_preferences
    )

    paneltwo_mode7_col5_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode7_col5_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode7_col5_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode7_col5_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode7_col5_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode7_col5_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode7_col5_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode7_col5_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode7_col5_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode7_col5_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode7_col6_title: StringProperty(
        name="六列标题",
        description="留空不显示该列",
        default="六列标题",
        update=update_preferences
    )

    paneltwo_mode7_col6_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode7_col6_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode7_col6_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode7_col6_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode7_col6_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode7_col6_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode7_col6_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode7_col6_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode7_col6_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode7_col6_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode7_col7_title: StringProperty(
        name="七列标题",
        description="留空不显示该列",
        default="七列标题",
        update=update_preferences
    )

    paneltwo_mode7_col7_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode7_col7_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode7_col7_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode7_col7_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode7_col7_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode7_col7_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode7_col7_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode7_col7_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode7_col7_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode7_col7_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode7_col8_title: StringProperty(
        name="八列标题",
        description="留空不显示该列",
        default="八列标题",
        update=update_preferences
    )

    paneltwo_mode7_col8_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode7_col8_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode7_col8_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode7_col8_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode7_col8_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode7_col8_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode7_col8_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode7_col8_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode7_col8_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode7_col8_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )
# --------↑↑↑↑ paneltwo_mode7_ 相关设置 ↑↑↑↑---------










# --------↓↓↓↓ paneltwo_mode8_ 相关设置 ↓↓↓↓---------
    paneltwo_mode8_visible: BoolProperty(
        name="",
        description="显示/隐藏超级面板",
        default=True,
        update=update_preferences
    )
    
    paneltwo_mode8_col1_title: StringProperty(
        name="一列标题",
        description="留空不显示该列",
        default="一列标题",
        update=update_preferences
    )

    paneltwo_mode8_col1_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode8_col1_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode8_col1_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode8_col1_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode8_col1_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode8_col1_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode8_col1_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode8_col1_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode8_col1_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode8_col1_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode8_col2_title: StringProperty(
        name="二列标题",
        description="留空不显示该列",
        default="二列标题",
        update=update_preferences
    )

    paneltwo_mode8_col2_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode8_col2_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode8_col2_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode8_col2_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode8_col2_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode8_col2_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode8_col2_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode8_col2_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode8_col2_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode8_col2_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode8_col3_title: StringProperty(
        name="三列标题",
        description="留空不显示该列",
        default="三列标题",
        update=update_preferences
    )

    paneltwo_mode8_col3_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode8_col3_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode8_col3_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode8_col3_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode8_col3_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode8_col3_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode8_col3_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode8_col3_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode8_col3_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode8_col3_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode8_col4_title: StringProperty(
        name="四列标题",
        description="留空不显示该列",
        default="四列标题",
        update=update_preferences
    )

    paneltwo_mode8_col4_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode8_col4_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode8_col4_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode8_col4_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode8_col4_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode8_col4_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode8_col4_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode8_col4_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode8_col4_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode8_col4_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode8_col5_title: StringProperty(
        name="五列标题",
        description="留空不显示该列",
        default="五列标题",
        update=update_preferences
    )

    paneltwo_mode8_col5_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode8_col5_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode8_col5_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode8_col5_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode8_col5_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode8_col5_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode8_col5_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode8_col5_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode8_col5_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode8_col5_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode8_col6_title: StringProperty(
        name="六列标题",
        description="留空不显示该列",
        default="六列标题",
        update=update_preferences
    )

    paneltwo_mode8_col6_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode8_col6_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode8_col6_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode8_col6_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode8_col6_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode8_col6_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode8_col6_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode8_col6_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode8_col6_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode8_col6_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode8_col7_title: StringProperty(
        name="七列标题",
        description="留空不显示该列",
        default="七列标题",
        update=update_preferences
    )

    paneltwo_mode8_col7_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode8_col7_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode8_col7_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode8_col7_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode8_col7_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode8_col7_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode8_col7_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode8_col7_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode8_col7_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode8_col7_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode8_col8_title: StringProperty(
        name="八列标题",
        description="留空不显示该列",
        default="八列标题",
        update=update_preferences
    )

    paneltwo_mode8_col8_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode8_col8_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode8_col8_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode8_col8_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode8_col8_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode8_col8_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode8_col8_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode8_col8_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode8_col8_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode8_col8_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )
# --------↑↑↑↑ paneltwo_mode8_ 相关设置 ↑↑↑↑---------










# --------↓↓↓↓ paneltwo_mode9_ 相关设置 ↓↓↓↓---------
    paneltwo_mode9_visible: BoolProperty(
        name="",
        description="显示/隐藏超级面板",
        default=True,
        update=update_preferences
    )
    
    paneltwo_mode9_col1_title: StringProperty(
        name="一列标题",
        description="留空不显示该列",
        default="一列标题",
        update=update_preferences
    )

    paneltwo_mode9_col1_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode9_col1_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode9_col1_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode9_col1_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode9_col1_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode9_col1_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode9_col1_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode9_col1_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode9_col1_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode9_col1_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode9_col2_title: StringProperty(
        name="二列标题",
        description="留空不显示该列",
        default="二列标题",
        update=update_preferences
    )

    paneltwo_mode9_col2_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode9_col2_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode9_col2_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode9_col2_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode9_col2_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode9_col2_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode9_col2_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode9_col2_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode9_col2_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode9_col2_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode9_col3_title: StringProperty(
        name="三列标题",
        description="留空不显示该列",
        default="三列标题",
        update=update_preferences
    )

    paneltwo_mode9_col3_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode9_col3_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode9_col3_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode9_col3_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode9_col3_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode9_col3_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode9_col3_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode9_col3_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode9_col3_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode9_col3_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode9_col4_title: StringProperty(
        name="四列标题",
        description="留空不显示该列",
        default="四列标题",
        update=update_preferences
    )

    paneltwo_mode9_col4_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode9_col4_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode9_col4_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode9_col4_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode9_col4_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode9_col4_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode9_col4_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode9_col4_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode9_col4_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode9_col4_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode9_col5_title: StringProperty(
        name="五列标题",
        description="留空不显示该列",
        default="五列标题",
        update=update_preferences
    )

    paneltwo_mode9_col5_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode9_col5_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode9_col5_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode9_col5_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode9_col5_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode9_col5_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode9_col5_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode9_col5_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode9_col5_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode9_col5_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode9_col6_title: StringProperty(
        name="六列标题",
        description="留空不显示该列",
        default="六列标题",
        update=update_preferences
    )

    paneltwo_mode9_col6_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode9_col6_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode9_col6_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode9_col6_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode9_col6_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode9_col6_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode9_col6_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode9_col6_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode9_col6_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode9_col6_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode9_col7_title: StringProperty(
        name="七列标题",
        description="留空不显示该列",
        default="七列标题",
        update=update_preferences
    )

    paneltwo_mode9_col7_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode9_col7_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode9_col7_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode9_col7_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode9_col7_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode9_col7_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode9_col7_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode9_col7_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode9_col7_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode9_col7_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode9_col8_title: StringProperty(
        name="八列标题",
        description="留空不显示该列",
        default="八列标题",
        update=update_preferences
    )

    paneltwo_mode9_col8_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode9_col8_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode9_col8_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode9_col8_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode9_col8_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode9_col8_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode9_col8_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode9_col8_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode9_col8_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode9_col8_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )
# --------↑↑↑↑ paneltwo_mode9_ 相关设置 ↑↑↑↑---------










# --------↓↓↓↓ paneltwo_mode10_ 相关设置 ↓↓↓↓---------
    paneltwo_mode10_visible: BoolProperty(
        name="",
        description="显示/隐藏超级面板",
        default=True,
        update=update_preferences
    )
    
    paneltwo_mode10_col1_title: StringProperty(
        name="一列标题",
        description="留空不显示该列",
        default="一列标题",
        update=update_preferences
    )

    paneltwo_mode10_col1_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode10_col1_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode10_col1_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode10_col1_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode10_col1_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode10_col1_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode10_col1_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode10_col1_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode10_col1_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode10_col1_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode10_col2_title: StringProperty(
        name="二列标题",
        description="留空不显示该列",
        default="二列标题",
        update=update_preferences
    )

    paneltwo_mode10_col2_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode10_col2_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode10_col2_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode10_col2_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode10_col2_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode10_col2_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode10_col2_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode10_col2_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode10_col2_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode10_col2_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode10_col3_title: StringProperty(
        name="三列标题",
        description="留空不显示该列",
        default="三列标题",
        update=update_preferences
    )

    paneltwo_mode10_col3_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode10_col3_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode10_col3_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode10_col3_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode10_col3_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode10_col3_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode10_col3_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode10_col3_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode10_col3_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode10_col3_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode10_col4_title: StringProperty(
        name="四列标题",
        description="留空不显示该列",
        default="四列标题",
        update=update_preferences
    )

    paneltwo_mode10_col4_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode10_col4_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode10_col4_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode10_col4_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode10_col4_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode10_col4_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode10_col4_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode10_col4_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode10_col4_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode10_col4_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode10_col5_title: StringProperty(
        name="五列标题",
        description="留空不显示该列",
        default="五列标题",
        update=update_preferences
    )

    paneltwo_mode10_col5_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode10_col5_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode10_col5_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode10_col5_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode10_col5_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode10_col5_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode10_col5_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode10_col5_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode10_col5_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode10_col5_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode10_col6_title: StringProperty(
        name="六列标题",
        description="留空不显示该列",
        default="六列标题",
        update=update_preferences
    )

    paneltwo_mode10_col6_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode10_col6_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode10_col6_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode10_col6_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode10_col6_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode10_col6_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode10_col6_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode10_col6_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode10_col6_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode10_col6_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode10_col7_title: StringProperty(
        name="七列标题",
        description="留空不显示该列",
        default="七列标题",
        update=update_preferences
    )

    paneltwo_mode10_col7_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode10_col7_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode10_col7_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode10_col7_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode10_col7_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode10_col7_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode10_col7_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode10_col7_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode10_col7_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode10_col7_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode10_col8_title: StringProperty(
        name="八列标题",
        description="留空不显示该列",
        default="八列标题",
        update=update_preferences
    )

    paneltwo_mode10_col8_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode10_col8_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode10_col8_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode10_col8_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode10_col8_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode10_col8_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode10_col8_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode10_col8_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode10_col8_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode10_col8_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )
# --------↑↑↑↑ paneltwo_mode10_ 相关设置 ↑↑↑↑---------










# --------↓↓↓↓ paneltwo_mode11_ 相关设置 ↓↓↓↓---------
    paneltwo_mode11_visible: BoolProperty(
        name="",
        description="显示/隐藏超级面板",
        default=True,
        update=update_preferences
    )
    
    paneltwo_mode11_col1_title: StringProperty(
        name="一列标题",
        description="留空不显示该列",
        default="一列标题",
        update=update_preferences
    )

    paneltwo_mode11_col1_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode11_col1_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode11_col1_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode11_col1_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode11_col1_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode11_col1_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode11_col1_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode11_col1_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode11_col1_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode11_col1_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode11_col2_title: StringProperty(
        name="二列标题",
        description="留空不显示该列",
        default="二列标题",
        update=update_preferences
    )

    paneltwo_mode11_col2_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode11_col2_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode11_col2_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode11_col2_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode11_col2_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode11_col2_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode11_col2_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode11_col2_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode11_col2_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode11_col2_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode11_col3_title: StringProperty(
        name="三列标题",
        description="留空不显示该列",
        default="三列标题",
        update=update_preferences
    )

    paneltwo_mode11_col3_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode11_col3_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode11_col3_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode11_col3_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode11_col3_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode11_col3_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode11_col3_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode11_col3_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode11_col3_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode11_col3_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode11_col4_title: StringProperty(
        name="四列标题",
        description="留空不显示该列",
        default="四列标题",
        update=update_preferences
    )

    paneltwo_mode11_col4_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode11_col4_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode11_col4_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode11_col4_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode11_col4_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode11_col4_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode11_col4_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode11_col4_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode11_col4_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode11_col4_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode11_col5_title: StringProperty(
        name="五列标题",
        description="留空不显示该列",
        default="五列标题",
        update=update_preferences
    )

    paneltwo_mode11_col5_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode11_col5_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode11_col5_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode11_col5_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode11_col5_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode11_col5_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode11_col5_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode11_col5_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode11_col5_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode11_col5_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode11_col6_title: StringProperty(
        name="六列标题",
        description="留空不显示该列",
        default="六列标题",
        update=update_preferences
    )

    paneltwo_mode11_col6_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode11_col6_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode11_col6_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode11_col6_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode11_col6_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode11_col6_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode11_col6_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode11_col6_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode11_col6_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode11_col6_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode11_col7_title: StringProperty(
        name="七列标题",
        description="留空不显示该列",
        default="七列标题",
        update=update_preferences
    )

    paneltwo_mode11_col7_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode11_col7_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode11_col7_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode11_col7_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode11_col7_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode11_col7_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode11_col7_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode11_col7_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode11_col7_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode11_col7_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode11_col8_title: StringProperty(
        name="八列标题",
        description="留空不显示该列",
        default="八列标题",
        update=update_preferences
    )

    paneltwo_mode11_col8_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode11_col8_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode11_col8_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode11_col8_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode11_col8_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode11_col8_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode11_col8_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode11_col8_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode11_col8_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode11_col8_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )
# --------↑↑↑↑ paneltwo_mode11_ 相关设置 ↑↑↑↑---------










# --------↓↓↓↓ paneltwo_mode12_ 相关设置 ↓↓↓↓---------
    paneltwo_mode12_visible: BoolProperty(
        name="",
        description="显示/隐藏超级面板",
        default=True,
        update=update_preferences
    )
    
    paneltwo_mode12_col1_title: StringProperty(
        name="一列标题",
        description="留空不显示该列",
        default="一列标题",
        update=update_preferences
    )

    paneltwo_mode12_col1_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode12_col1_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode12_col1_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode12_col1_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode12_col1_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode12_col1_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode12_col1_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode12_col1_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode12_col1_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode12_col1_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode12_col2_title: StringProperty(
        name="二列标题",
        description="留空不显示该列",
        default="二列标题",
        update=update_preferences
    )

    paneltwo_mode12_col2_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode12_col2_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode12_col2_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode12_col2_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode12_col2_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode12_col2_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode12_col2_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode12_col2_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode12_col2_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode12_col2_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode12_col3_title: StringProperty(
        name="三列标题",
        description="留空不显示该列",
        default="三列标题",
        update=update_preferences
    )

    paneltwo_mode12_col3_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode12_col3_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode12_col3_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode12_col3_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode12_col3_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode12_col3_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode12_col3_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode12_col3_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode12_col3_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode12_col3_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode12_col4_title: StringProperty(
        name="四列标题",
        description="留空不显示该列",
        default="四列标题",
        update=update_preferences
    )

    paneltwo_mode12_col4_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode12_col4_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode12_col4_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode12_col4_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode12_col4_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode12_col4_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode12_col4_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode12_col4_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode12_col4_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode12_col4_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode12_col5_title: StringProperty(
        name="五列标题",
        description="留空不显示该列",
        default="五列标题",
        update=update_preferences
    )

    paneltwo_mode12_col5_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode12_col5_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode12_col5_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode12_col5_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode12_col5_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode12_col5_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode12_col5_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode12_col5_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode12_col5_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode12_col5_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode12_col6_title: StringProperty(
        name="六列标题",
        description="留空不显示该列",
        default="六列标题",
        update=update_preferences
    )

    paneltwo_mode12_col6_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode12_col6_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode12_col6_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode12_col6_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode12_col6_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode12_col6_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode12_col6_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode12_col6_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode12_col6_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode12_col6_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode12_col7_title: StringProperty(
        name="七列标题",
        description="留空不显示该列",
        default="七列标题",
        update=update_preferences
    )

    paneltwo_mode12_col7_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode12_col7_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode12_col7_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode12_col7_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode12_col7_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode12_col7_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode12_col7_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode12_col7_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode12_col7_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode12_col7_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode12_col8_title: StringProperty(
        name="八列标题",
        description="留空不显示该列",
        default="八列标题",
        update=update_preferences
    )

    paneltwo_mode12_col8_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode12_col8_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode12_col8_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode12_col8_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode12_col8_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode12_col8_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode12_col8_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode12_col8_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode12_col8_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode12_col8_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )
# --------↑↑↑↑ paneltwo_mode12_ 相关设置 ↑↑↑↑---------










# --------↓↓↓↓ paneltwo_mode13_ 相关设置 ↓↓↓↓---------
    paneltwo_mode13_visible: BoolProperty(
        name="",
        description="显示/隐藏超级面板",
        default=True,
        update=update_preferences
    )
    
    paneltwo_mode13_col1_title: StringProperty(
        name="一列标题",
        description="留空不显示该列",
        default="一列标题",
        update=update_preferences
    )

    paneltwo_mode13_col1_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode13_col1_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode13_col1_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode13_col1_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode13_col1_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode13_col1_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode13_col1_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode13_col1_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode13_col1_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode13_col1_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode13_col2_title: StringProperty(
        name="二列标题",
        description="留空不显示该列",
        default="二列标题",
        update=update_preferences
    )

    paneltwo_mode13_col2_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode13_col2_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode13_col2_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode13_col2_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode13_col2_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode13_col2_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode13_col2_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode13_col2_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode13_col2_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode13_col2_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode13_col3_title: StringProperty(
        name="三列标题",
        description="留空不显示该列",
        default="三列标题",
        update=update_preferences
    )

    paneltwo_mode13_col3_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode13_col3_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode13_col3_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode13_col3_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode13_col3_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode13_col3_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode13_col3_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode13_col3_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode13_col3_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode13_col3_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode13_col4_title: StringProperty(
        name="四列标题",
        description="留空不显示该列",
        default="四列标题",
        update=update_preferences
    )

    paneltwo_mode13_col4_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode13_col4_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode13_col4_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode13_col4_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode13_col4_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode13_col4_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode13_col4_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode13_col4_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode13_col4_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode13_col4_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode13_col5_title: StringProperty(
        name="五列标题",
        description="留空不显示该列",
        default="五列标题",
        update=update_preferences
    )

    paneltwo_mode13_col5_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode13_col5_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode13_col5_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode13_col5_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode13_col5_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode13_col5_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode13_col5_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode13_col5_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode13_col5_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode13_col5_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode13_col6_title: StringProperty(
        name="六列标题",
        description="留空不显示该列",
        default="六列标题",
        update=update_preferences
    )

    paneltwo_mode13_col6_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode13_col6_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode13_col6_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode13_col6_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode13_col6_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode13_col6_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode13_col6_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode13_col6_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode13_col6_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode13_col6_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode13_col7_title: StringProperty(
        name="七列标题",
        description="留空不显示该列",
        default="七列标题",
        update=update_preferences
    )

    paneltwo_mode13_col7_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode13_col7_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode13_col7_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode13_col7_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode13_col7_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode13_col7_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode13_col7_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode13_col7_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode13_col7_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode13_col7_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode13_col8_title: StringProperty(
        name="八列标题",
        description="留空不显示该列",
        default="八列标题",
        update=update_preferences
    )

    paneltwo_mode13_col8_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode13_col8_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode13_col8_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode13_col8_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode13_col8_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode13_col8_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode13_col8_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode13_col8_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode13_col8_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode13_col8_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )
# --------↑↑↑↑ paneltwo_mode13_ 相关设置 ↑↑↑↑---------










# --------↓↓↓↓ paneltwo_mode14_ 相关设置 ↓↓↓↓---------
    paneltwo_mode14_visible: BoolProperty(
        name="",
        description="显示/隐藏超级面板",
        default=True,
        update=update_preferences
    )
    
    paneltwo_mode14_col1_title: StringProperty(
        name="一列标题",
        description="留空不显示该列",
        default="一列标题",
        update=update_preferences
    )

    paneltwo_mode14_col1_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode14_col1_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode14_col1_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode14_col1_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode14_col1_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode14_col1_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode14_col1_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode14_col1_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode14_col1_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode14_col1_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode14_col2_title: StringProperty(
        name="二列标题",
        description="留空不显示该列",
        default="二列标题",
        update=update_preferences
    )

    paneltwo_mode14_col2_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode14_col2_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode14_col2_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode14_col2_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode14_col2_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode14_col2_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode14_col2_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode14_col2_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode14_col2_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode14_col2_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode14_col3_title: StringProperty(
        name="三列标题",
        description="留空不显示该列",
        default="三列标题",
        update=update_preferences
    )

    paneltwo_mode14_col3_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode14_col3_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode14_col3_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode14_col3_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode14_col3_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode14_col3_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode14_col3_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode14_col3_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode14_col3_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode14_col3_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode14_col4_title: StringProperty(
        name="四列标题",
        description="留空不显示该列",
        default="四列标题",
        update=update_preferences
    )

    paneltwo_mode14_col4_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode14_col4_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode14_col4_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode14_col4_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode14_col4_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode14_col4_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode14_col4_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode14_col4_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode14_col4_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode14_col4_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode14_col5_title: StringProperty(
        name="五列标题",
        description="留空不显示该列",
        default="五列标题",
        update=update_preferences
    )

    paneltwo_mode14_col5_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode14_col5_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode14_col5_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode14_col5_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode14_col5_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode14_col5_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode14_col5_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode14_col5_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode14_col5_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode14_col5_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode14_col6_title: StringProperty(
        name="六列标题",
        description="留空不显示该列",
        default="六列标题",
        update=update_preferences
    )

    paneltwo_mode14_col6_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode14_col6_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode14_col6_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode14_col6_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode14_col6_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode14_col6_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode14_col6_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode14_col6_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode14_col6_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode14_col6_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode14_col7_title: StringProperty(
        name="七列标题",
        description="留空不显示该列",
        default="七列标题",
        update=update_preferences
    )

    paneltwo_mode14_col7_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode14_col7_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode14_col7_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode14_col7_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode14_col7_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode14_col7_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode14_col7_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode14_col7_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode14_col7_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode14_col7_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode14_col8_title: StringProperty(
        name="八列标题",
        description="留空不显示该列",
        default="八列标题",
        update=update_preferences
    )

    paneltwo_mode14_col8_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode14_col8_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode14_col8_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode14_col8_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode14_col8_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode14_col8_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode14_col8_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode14_col8_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode14_col8_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode14_col8_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )
# --------↑↑↑↑ paneltwo_mode14_ 相关设置 ↑↑↑↑---------










# --------↓↓↓↓ paneltwo_mode15_ 相关设置 ↓↓↓↓---------
    paneltwo_mode15_visible: BoolProperty(
        name="",
        description="显示/隐藏超级面板",
        default=True,
        update=update_preferences
    )
    
    paneltwo_mode15_col1_title: StringProperty(
        name="一列标题",
        description="留空不显示该列",
        default="一列标题",
        update=update_preferences
    )

    paneltwo_mode15_col1_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode15_col1_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode15_col1_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode15_col1_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode15_col1_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode15_col1_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode15_col1_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode15_col1_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode15_col1_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode15_col1_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode15_col2_title: StringProperty(
        name="二列标题",
        description="留空不显示该列",
        default="二列标题",
        update=update_preferences
    )

    paneltwo_mode15_col2_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode15_col2_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode15_col2_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode15_col2_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode15_col2_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode15_col2_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode15_col2_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode15_col2_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode15_col2_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode15_col2_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode15_col3_title: StringProperty(
        name="三列标题",
        description="留空不显示该列",
        default="三列标题",
        update=update_preferences
    )

    paneltwo_mode15_col3_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode15_col3_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode15_col3_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode15_col3_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode15_col3_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode15_col3_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode15_col3_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode15_col3_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode15_col3_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode15_col3_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode15_col4_title: StringProperty(
        name="四列标题",
        description="留空不显示该列",
        default="四列标题",
        update=update_preferences
    )

    paneltwo_mode15_col4_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode15_col4_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode15_col4_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode15_col4_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode15_col4_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode15_col4_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode15_col4_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode15_col4_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode15_col4_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode15_col4_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode15_col5_title: StringProperty(
        name="五列标题",
        description="留空不显示该列",
        default="五列标题",
        update=update_preferences
    )

    paneltwo_mode15_col5_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode15_col5_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode15_col5_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode15_col5_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode15_col5_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode15_col5_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode15_col5_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode15_col5_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode15_col5_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode15_col5_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode15_col6_title: StringProperty(
        name="六列标题",
        description="留空不显示该列",
        default="六列标题",
        update=update_preferences
    )

    paneltwo_mode15_col6_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode15_col6_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode15_col6_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode15_col6_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode15_col6_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode15_col6_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode15_col6_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode15_col6_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode15_col6_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode15_col6_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode15_col7_title: StringProperty(
        name="七列标题",
        description="留空不显示该列",
        default="七列标题",
        update=update_preferences
    )

    paneltwo_mode15_col7_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode15_col7_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode15_col7_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode15_col7_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode15_col7_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode15_col7_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode15_col7_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode15_col7_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode15_col7_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode15_col7_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode15_col8_title: StringProperty(
        name="八列标题",
        description="留空不显示该列",
        default="八列标题",
        update=update_preferences
    )

    paneltwo_mode15_col8_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode15_col8_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode15_col8_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode15_col8_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode15_col8_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode15_col8_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode15_col8_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode15_col8_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode15_col8_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode15_col8_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )
# --------↑↑↑↑ paneltwo_mode15_ 相关设置 ↑↑↑↑---------










# --------↓↓↓↓ paneltwo_mode16_ 相关设置 ↓↓↓↓---------
    paneltwo_mode16_visible: BoolProperty(
        name="",
        description="显示/隐藏超级面板",
        default=True,
        update=update_preferences
    )
    
    paneltwo_mode16_col1_title: StringProperty(
        name="一列标题",
        description="留空不显示该列",
        default="一列标题",
        update=update_preferences
    )

    paneltwo_mode16_col1_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode16_col1_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode16_col1_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode16_col1_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode16_col1_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode16_col1_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode16_col1_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode16_col1_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode16_col1_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode16_col1_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode16_col2_title: StringProperty(
        name="二列标题",
        description="留空不显示该列",
        default="二列标题",
        update=update_preferences
    )

    paneltwo_mode16_col2_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode16_col2_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode16_col2_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode16_col2_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode16_col2_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode16_col2_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode16_col2_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode16_col2_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode16_col2_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode16_col2_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode16_col3_title: StringProperty(
        name="三列标题",
        description="留空不显示该列",
        default="三列标题",
        update=update_preferences
    )

    paneltwo_mode16_col3_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode16_col3_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode16_col3_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode16_col3_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode16_col3_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode16_col3_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode16_col3_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode16_col3_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode16_col3_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode16_col3_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode16_col4_title: StringProperty(
        name="四列标题",
        description="留空不显示该列",
        default="四列标题",
        update=update_preferences
    )

    paneltwo_mode16_col4_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode16_col4_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode16_col4_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode16_col4_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode16_col4_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode16_col4_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode16_col4_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode16_col4_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode16_col4_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode16_col4_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode16_col5_title: StringProperty(
        name="五列标题",
        description="留空不显示该列",
        default="五列标题",
        update=update_preferences
    )

    paneltwo_mode16_col5_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode16_col5_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode16_col5_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode16_col5_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode16_col5_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode16_col5_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode16_col5_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode16_col5_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode16_col5_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode16_col5_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode16_col6_title: StringProperty(
        name="六列标题",
        description="留空不显示该列",
        default="六列标题",
        update=update_preferences
    )

    paneltwo_mode16_col6_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode16_col6_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode16_col6_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode16_col6_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode16_col6_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode16_col6_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode16_col6_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode16_col6_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode16_col6_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode16_col6_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode16_col7_title: StringProperty(
        name="七列标题",
        description="留空不显示该列",
        default="七列标题",
        update=update_preferences
    )

    paneltwo_mode16_col7_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode16_col7_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode16_col7_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode16_col7_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode16_col7_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode16_col7_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode16_col7_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode16_col7_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode16_col7_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode16_col7_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode16_col8_title: StringProperty(
        name="八列标题",
        description="留空不显示该列",
        default="八列标题",
        update=update_preferences
    )

    paneltwo_mode16_col8_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode16_col8_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode16_col8_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode16_col8_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode16_col8_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode16_col8_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode16_col8_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode16_col8_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode16_col8_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode16_col8_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )
# --------↑↑↑↑ paneltwo_mode16_ 相关设置 ↑↑↑↑---------










# --------↓↓↓↓ paneltwo_mode17_ 相关设置 ↓↓↓↓---------
    paneltwo_mode17_visible: BoolProperty(
        name="",
        description="显示/隐藏超级面板",
        default=True,
        update=update_preferences
    )
    
    paneltwo_mode17_col1_title: StringProperty(
        name="一列标题",
        description="留空不显示该列",
        default="一列标题",
        update=update_preferences
    )

    paneltwo_mode17_col1_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode17_col1_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode17_col1_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode17_col1_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode17_col1_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode17_col1_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode17_col1_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode17_col1_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode17_col1_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode17_col1_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode17_col2_title: StringProperty(
        name="二列标题",
        description="留空不显示该列",
        default="二列标题",
        update=update_preferences
    )

    paneltwo_mode17_col2_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode17_col2_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode17_col2_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode17_col2_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode17_col2_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode17_col2_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode17_col2_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode17_col2_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode17_col2_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode17_col2_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode17_col3_title: StringProperty(
        name="三列标题",
        description="留空不显示该列",
        default="三列标题",
        update=update_preferences
    )

    paneltwo_mode17_col3_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode17_col3_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode17_col3_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode17_col3_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode17_col3_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode17_col3_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode17_col3_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode17_col3_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode17_col3_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode17_col3_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode17_col4_title: StringProperty(
        name="四列标题",
        description="留空不显示该列",
        default="四列标题",
        update=update_preferences
    )

    paneltwo_mode17_col4_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode17_col4_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode17_col4_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode17_col4_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode17_col4_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode17_col4_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode17_col4_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode17_col4_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode17_col4_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode17_col4_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode17_col5_title: StringProperty(
        name="五列标题",
        description="留空不显示该列",
        default="五列标题",
        update=update_preferences
    )

    paneltwo_mode17_col5_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode17_col5_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode17_col5_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode17_col5_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode17_col5_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode17_col5_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode17_col5_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode17_col5_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode17_col5_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode17_col5_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode17_col6_title: StringProperty(
        name="六列标题",
        description="留空不显示该列",
        default="六列标题",
        update=update_preferences
    )

    paneltwo_mode17_col6_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode17_col6_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode17_col6_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode17_col6_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode17_col6_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode17_col6_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode17_col6_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode17_col6_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode17_col6_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode17_col6_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode17_col7_title: StringProperty(
        name="七列标题",
        description="留空不显示该列",
        default="七列标题",
        update=update_preferences
    )

    paneltwo_mode17_col7_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode17_col7_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode17_col7_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode17_col7_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode17_col7_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode17_col7_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode17_col7_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode17_col7_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode17_col7_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode17_col7_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode17_col8_title: StringProperty(
        name="八列标题",
        description="留空不显示该列",
        default="八列标题",
        update=update_preferences
    )

    paneltwo_mode17_col8_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode17_col8_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode17_col8_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode17_col8_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode17_col8_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode17_col8_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode17_col8_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode17_col8_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode17_col8_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode17_col8_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )
# --------↑↑↑↑ paneltwo_mode17_ 相关设置 ↑↑↑↑---------










# --------↓↓↓↓ paneltwo_mode18_ 相关设置 ↓↓↓↓---------
    paneltwo_mode18_visible: BoolProperty(
        name="",
        description="显示/隐藏超级面板",
        default=True,
        update=update_preferences
    )
    
    paneltwo_mode18_col1_title: StringProperty(
        name="一列标题",
        description="留空不显示该列",
        default="一列标题",
        update=update_preferences
    )

    paneltwo_mode18_col1_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode18_col1_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode18_col1_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode18_col1_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode18_col1_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode18_col1_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode18_col1_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode18_col1_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode18_col1_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode18_col1_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode18_col2_title: StringProperty(
        name="二列标题",
        description="留空不显示该列",
        default="二列标题",
        update=update_preferences
    )

    paneltwo_mode18_col2_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode18_col2_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode18_col2_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode18_col2_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode18_col2_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode18_col2_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode18_col2_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode18_col2_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode18_col2_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode18_col2_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode18_col3_title: StringProperty(
        name="三列标题",
        description="留空不显示该列",
        default="三列标题",
        update=update_preferences
    )

    paneltwo_mode18_col3_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode18_col3_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode18_col3_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode18_col3_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode18_col3_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode18_col3_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode18_col3_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode18_col3_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode18_col3_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode18_col3_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode18_col4_title: StringProperty(
        name="四列标题",
        description="留空不显示该列",
        default="四列标题",
        update=update_preferences
    )

    paneltwo_mode18_col4_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode18_col4_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode18_col4_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode18_col4_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode18_col4_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode18_col4_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode18_col4_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode18_col4_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode18_col4_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode18_col4_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode18_col5_title: StringProperty(
        name="五列标题",
        description="留空不显示该列",
        default="五列标题",
        update=update_preferences
    )

    paneltwo_mode18_col5_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode18_col5_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode18_col5_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode18_col5_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode18_col5_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode18_col5_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode18_col5_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode18_col5_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode18_col5_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode18_col5_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode18_col6_title: StringProperty(
        name="六列标题",
        description="留空不显示该列",
        default="六列标题",
        update=update_preferences
    )

    paneltwo_mode18_col6_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode18_col6_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode18_col6_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode18_col6_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode18_col6_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode18_col6_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode18_col6_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode18_col6_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode18_col6_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode18_col6_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode18_col7_title: StringProperty(
        name="七列标题",
        description="留空不显示该列",
        default="七列标题",
        update=update_preferences
    )

    paneltwo_mode18_col7_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode18_col7_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode18_col7_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode18_col7_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode18_col7_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode18_col7_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode18_col7_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode18_col7_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode18_col7_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode18_col7_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode18_col8_title: StringProperty(
        name="八列标题",
        description="留空不显示该列",
        default="八列标题",
        update=update_preferences
    )

    paneltwo_mode18_col8_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode18_col8_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode18_col8_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode18_col8_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode18_col8_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode18_col8_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode18_col8_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode18_col8_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode18_col8_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode18_col8_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )
# --------↑↑↑↑ paneltwo_mode18_ 相关设置 ↑↑↑↑---------










# --------↓↓↓↓ paneltwo_mode19_ 相关设置 ↓↓↓↓---------
    paneltwo_mode19_visible: BoolProperty(
        name="",
        description="显示/隐藏超级面板",
        default=True,
        update=update_preferences
    )
    
    paneltwo_mode19_col1_title: StringProperty(
        name="一列标题",
        description="留空不显示该列",
        default="一列标题",
        update=update_preferences
    )

    paneltwo_mode19_col1_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode19_col1_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode19_col1_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode19_col1_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode19_col1_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode19_col1_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode19_col1_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode19_col1_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode19_col1_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode19_col1_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode19_col2_title: StringProperty(
        name="二列标题",
        description="留空不显示该列",
        default="二列标题",
        update=update_preferences
    )

    paneltwo_mode19_col2_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode19_col2_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode19_col2_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode19_col2_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode19_col2_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode19_col2_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode19_col2_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode19_col2_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode19_col2_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode19_col2_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode19_col3_title: StringProperty(
        name="三列标题",
        description="留空不显示该列",
        default="三列标题",
        update=update_preferences
    )

    paneltwo_mode19_col3_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode19_col3_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode19_col3_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode19_col3_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode19_col3_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode19_col3_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode19_col3_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode19_col3_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode19_col3_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode19_col3_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode19_col4_title: StringProperty(
        name="四列标题",
        description="留空不显示该列",
        default="四列标题",
        update=update_preferences
    )

    paneltwo_mode19_col4_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode19_col4_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode19_col4_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode19_col4_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode19_col4_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode19_col4_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode19_col4_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode19_col4_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode19_col4_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode19_col4_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode19_col5_title: StringProperty(
        name="五列标题",
        description="留空不显示该列",
        default="五列标题",
        update=update_preferences
    )

    paneltwo_mode19_col5_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode19_col5_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode19_col5_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode19_col5_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode19_col5_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode19_col5_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode19_col5_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode19_col5_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode19_col5_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode19_col5_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode19_col6_title: StringProperty(
        name="六列标题",
        description="留空不显示该列",
        default="六列标题",
        update=update_preferences
    )

    paneltwo_mode19_col6_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode19_col6_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode19_col6_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode19_col6_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode19_col6_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode19_col6_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode19_col6_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode19_col6_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode19_col6_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode19_col6_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode19_col7_title: StringProperty(
        name="七列标题",
        description="留空不显示该列",
        default="七列标题",
        update=update_preferences
    )

    paneltwo_mode19_col7_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode19_col7_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode19_col7_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode19_col7_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode19_col7_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode19_col7_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode19_col7_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode19_col7_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode19_col7_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode19_col7_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode19_col8_title: StringProperty(
        name="八列标题",
        description="留空不显示该列",
        default="八列标题",
        update=update_preferences
    )

    paneltwo_mode19_col8_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode19_col8_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode19_col8_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode19_col8_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode19_col8_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode19_col8_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode19_col8_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode19_col8_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode19_col8_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode19_col8_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )
# --------↑↑↑↑ paneltwo_mode19_ 相关设置 ↑↑↑↑---------










# --------↓↓↓↓ paneltwo_mode20_ 相关设置 ↓↓↓↓---------
    paneltwo_mode20_visible: BoolProperty(
        name="",
        description="显示/隐藏超级面板",
        default=True,
        update=update_preferences
    )
    
    paneltwo_mode20_col1_title: StringProperty(
        name="一列标题",
        description="留空不显示该列",
        default="一列标题",
        update=update_preferences
    )

    paneltwo_mode20_col1_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode20_col1_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode20_col1_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode20_col1_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode20_col1_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode20_col1_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode20_col1_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode20_col1_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode20_col1_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode20_col1_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode20_col2_title: StringProperty(
        name="二列标题",
        description="留空不显示该列",
        default="二列标题",
        update=update_preferences
    )

    paneltwo_mode20_col2_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode20_col2_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode20_col2_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode20_col2_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode20_col2_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode20_col2_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode20_col2_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode20_col2_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode20_col2_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode20_col2_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode20_col3_title: StringProperty(
        name="三列标题",
        description="留空不显示该列",
        default="三列标题",
        update=update_preferences
    )

    paneltwo_mode20_col3_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode20_col3_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode20_col3_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode20_col3_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode20_col3_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode20_col3_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode20_col3_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode20_col3_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode20_col3_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode20_col3_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode20_col4_title: StringProperty(
        name="四列标题",
        description="留空不显示该列",
        default="四列标题",
        update=update_preferences
    )

    paneltwo_mode20_col4_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode20_col4_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode20_col4_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode20_col4_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode20_col4_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode20_col4_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode20_col4_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode20_col4_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode20_col4_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode20_col4_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode20_col5_title: StringProperty(
        name="五列标题",
        description="留空不显示该列",
        default="五列标题",
        update=update_preferences
    )

    paneltwo_mode20_col5_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode20_col5_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode20_col5_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode20_col5_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode20_col5_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode20_col5_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode20_col5_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode20_col5_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode20_col5_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode20_col5_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode20_col6_title: StringProperty(
        name="六列标题",
        description="留空不显示该列",
        default="六列标题",
        update=update_preferences
    )

    paneltwo_mode20_col6_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode20_col6_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode20_col6_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode20_col6_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode20_col6_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode20_col6_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode20_col6_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode20_col6_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode20_col6_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode20_col6_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode20_col7_title: StringProperty(
        name="七列标题",
        description="留空不显示该列",
        default="七列标题",
        update=update_preferences
    )

    paneltwo_mode20_col7_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode20_col7_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode20_col7_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode20_col7_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode20_col7_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode20_col7_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode20_col7_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode20_col7_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode20_col7_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode20_col7_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode20_col8_title: StringProperty(
        name="八列标题",
        description="留空不显示该列",
        default="八列标题",
        update=update_preferences
    )

    paneltwo_mode20_col8_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode20_col8_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode20_col8_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode20_col8_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode20_col8_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode20_col8_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode20_col8_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode20_col8_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode20_col8_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode20_col8_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )
# --------↑↑↑↑ paneltwo_mode20_ 相关设置 ↑↑↑↑---------










# --------↓↓↓↓ paneltwo_mode21_ 相关设置 ↓↓↓↓---------
    paneltwo_mode21_visible: BoolProperty(
        name="",
        description="显示/隐藏超级面板",
        default=True,
        update=update_preferences
    )
    
    paneltwo_mode21_col1_title: StringProperty(
        name="一列标题",
        description="留空不显示该列",
        default="一列标题",
        update=update_preferences
    )

    paneltwo_mode21_col1_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode21_col1_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode21_col1_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode21_col1_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode21_col1_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode21_col1_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode21_col1_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode21_col1_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode21_col1_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode21_col1_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode21_col2_title: StringProperty(
        name="二列标题",
        description="留空不显示该列",
        default="二列标题",
        update=update_preferences
    )

    paneltwo_mode21_col2_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode21_col2_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode21_col2_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode21_col2_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode21_col2_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode21_col2_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode21_col2_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode21_col2_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode21_col2_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode21_col2_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode21_col3_title: StringProperty(
        name="三列标题",
        description="留空不显示该列",
        default="三列标题",
        update=update_preferences
    )

    paneltwo_mode21_col3_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode21_col3_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode21_col3_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode21_col3_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode21_col3_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode21_col3_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode21_col3_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode21_col3_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode21_col3_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode21_col3_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode21_col4_title: StringProperty(
        name="四列标题",
        description="留空不显示该列",
        default="四列标题",
        update=update_preferences
    )

    paneltwo_mode21_col4_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode21_col4_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode21_col4_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode21_col4_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode21_col4_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode21_col4_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode21_col4_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode21_col4_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode21_col4_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode21_col4_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode21_col5_title: StringProperty(
        name="五列标题",
        description="留空不显示该列",
        default="五列标题",
        update=update_preferences
    )

    paneltwo_mode21_col5_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode21_col5_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode21_col5_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode21_col5_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode21_col5_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode21_col5_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode21_col5_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode21_col5_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode21_col5_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode21_col5_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode21_col6_title: StringProperty(
        name="六列标题",
        description="留空不显示该列",
        default="六列标题",
        update=update_preferences
    )

    paneltwo_mode21_col6_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode21_col6_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode21_col6_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode21_col6_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode21_col6_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode21_col6_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode21_col6_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode21_col6_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode21_col6_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode21_col6_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode21_col7_title: StringProperty(
        name="七列标题",
        description="留空不显示该列",
        default="七列标题",
        update=update_preferences
    )

    paneltwo_mode21_col7_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode21_col7_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode21_col7_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode21_col7_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode21_col7_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode21_col7_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode21_col7_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode21_col7_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode21_col7_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode21_col7_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode21_col8_title: StringProperty(
        name="八列标题",
        description="留空不显示该列",
        default="八列标题",
        update=update_preferences
    )

    paneltwo_mode21_col8_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode21_col8_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode21_col8_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode21_col8_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode21_col8_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode21_col8_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode21_col8_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode21_col8_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode21_col8_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode21_col8_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )
# --------↑↑↑↑ paneltwo_mode21_ 相关设置 ↑↑↑↑---------










# --------↓↓↓↓ paneltwo_mode22_ 相关设置 ↓↓↓↓---------
    paneltwo_mode22_visible: BoolProperty(
        name="",
        description="显示/隐藏超级面板",
        default=True,
        update=update_preferences
    )
    
    paneltwo_mode22_col1_title: StringProperty(
        name="一列标题",
        description="留空不显示该列",
        default="一列标题",
        update=update_preferences
    )

    paneltwo_mode22_col1_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode22_col1_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode22_col1_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode22_col1_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode22_col1_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode22_col1_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode22_col1_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode22_col1_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode22_col1_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode22_col1_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode22_col2_title: StringProperty(
        name="二列标题",
        description="留空不显示该列",
        default="二列标题",
        update=update_preferences
    )

    paneltwo_mode22_col2_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode22_col2_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode22_col2_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode22_col2_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode22_col2_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode22_col2_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode22_col2_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode22_col2_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode22_col2_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode22_col2_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode22_col3_title: StringProperty(
        name="三列标题",
        description="留空不显示该列",
        default="三列标题",
        update=update_preferences
    )

    paneltwo_mode22_col3_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode22_col3_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode22_col3_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode22_col3_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode22_col3_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode22_col3_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode22_col3_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode22_col3_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode22_col3_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode22_col3_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode22_col4_title: StringProperty(
        name="四列标题",
        description="留空不显示该列",
        default="四列标题",
        update=update_preferences
    )

    paneltwo_mode22_col4_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode22_col4_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode22_col4_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode22_col4_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode22_col4_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode22_col4_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode22_col4_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode22_col4_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode22_col4_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode22_col4_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode22_col5_title: StringProperty(
        name="五列标题",
        description="留空不显示该列",
        default="五列标题",
        update=update_preferences
    )

    paneltwo_mode22_col5_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode22_col5_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode22_col5_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode22_col5_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode22_col5_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode22_col5_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode22_col5_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode22_col5_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode22_col5_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode22_col5_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode22_col6_title: StringProperty(
        name="六列标题",
        description="留空不显示该列",
        default="六列标题",
        update=update_preferences
    )

    paneltwo_mode22_col6_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode22_col6_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode22_col6_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode22_col6_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode22_col6_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode22_col6_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode22_col6_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode22_col6_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode22_col6_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode22_col6_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode22_col7_title: StringProperty(
        name="七列标题",
        description="留空不显示该列",
        default="七列标题",
        update=update_preferences
    )

    paneltwo_mode22_col7_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode22_col7_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode22_col7_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode22_col7_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode22_col7_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode22_col7_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode22_col7_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode22_col7_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode22_col7_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode22_col7_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode22_col8_title: StringProperty(
        name="八列标题",
        description="留空不显示该列",
        default="八列标题",
        update=update_preferences
    )

    paneltwo_mode22_col8_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode22_col8_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode22_col8_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode22_col8_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode22_col8_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode22_col8_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode22_col8_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode22_col8_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode22_col8_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode22_col8_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )
# --------↑↑↑↑ paneltwo_mode22_ 相关设置 ↑↑↑↑---------










# --------↓↓↓↓ paneltwo_mode23_ 相关设置 ↓↓↓↓---------
    paneltwo_mode23_visible: BoolProperty(
        name="",
        description="显示/隐藏超级面板",
        default=True,
        update=update_preferences
    )
    
    paneltwo_mode23_col1_title: StringProperty(
        name="一列标题",
        description="留空不显示该列",
        default="一列标题",
        update=update_preferences
    )

    paneltwo_mode23_col1_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode23_col1_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode23_col1_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode23_col1_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode23_col1_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode23_col1_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode23_col1_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode23_col1_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode23_col1_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode23_col1_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode23_col2_title: StringProperty(
        name="二列标题",
        description="留空不显示该列",
        default="二列标题",
        update=update_preferences
    )

    paneltwo_mode23_col2_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode23_col2_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode23_col2_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode23_col2_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode23_col2_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode23_col2_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode23_col2_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode23_col2_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode23_col2_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode23_col2_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode23_col3_title: StringProperty(
        name="三列标题",
        description="留空不显示该列",
        default="三列标题",
        update=update_preferences
    )

    paneltwo_mode23_col3_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode23_col3_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode23_col3_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode23_col3_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode23_col3_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode23_col3_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode23_col3_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode23_col3_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode23_col3_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode23_col3_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode23_col4_title: StringProperty(
        name="四列标题",
        description="留空不显示该列",
        default="四列标题",
        update=update_preferences
    )

    paneltwo_mode23_col4_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode23_col4_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode23_col4_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode23_col4_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode23_col4_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode23_col4_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode23_col4_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode23_col4_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode23_col4_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode23_col4_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode23_col5_title: StringProperty(
        name="五列标题",
        description="留空不显示该列",
        default="五列标题",
        update=update_preferences
    )

    paneltwo_mode23_col5_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode23_col5_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode23_col5_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode23_col5_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode23_col5_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode23_col5_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode23_col5_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode23_col5_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode23_col5_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode23_col5_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode23_col6_title: StringProperty(
        name="六列标题",
        description="留空不显示该列",
        default="六列标题",
        update=update_preferences
    )

    paneltwo_mode23_col6_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode23_col6_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode23_col6_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode23_col6_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode23_col6_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode23_col6_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode23_col6_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode23_col6_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode23_col6_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode23_col6_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode23_col7_title: StringProperty(
        name="七列标题",
        description="留空不显示该列",
        default="七列标题",
        update=update_preferences
    )

    paneltwo_mode23_col7_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode23_col7_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode23_col7_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode23_col7_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode23_col7_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode23_col7_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode23_col7_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode23_col7_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode23_col7_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode23_col7_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode23_col8_title: StringProperty(
        name="八列标题",
        description="留空不显示该列",
        default="八列标题",
        update=update_preferences
    )

    paneltwo_mode23_col8_button1: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode23_col8_button2: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode23_col8_button3: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode23_col8_button4: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode23_col8_button5: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode23_col8_button6: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode23_col8_button7: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode23_col8_button8: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode23_col8_button9: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )

    paneltwo_mode23_col8_button10: StringProperty(
        name="",
        default='NO_BUTTON',
        update=update_preferences
    )
# --------↑↑↑↑ paneltwo_mode23_ 相关设置 ↑↑↑↑---------



    # 绘制插件设置页选项菜单函数
    def draw(self, context):
        # 每次绘制时强制检查设置
        settings = load_settings()
        if settings:
            for prop_name, value in settings.items():
                if hasattr(self, prop_name) and getattr(self, prop_name) != value:
                    print(f"修正设置: {prop_name} (当前:{getattr(self, prop_name)}, 应设为:{value})")
                    setattr(self, prop_name, value)
        
        layout = self.layout

        # “选择快捷键” BOX框
        box = layout.box()
        row = box.row()
        row.prop(self, "show_shortcut_options", 
                icon="DOWNARROW_HLT" if self.show_shortcut_options else "RIGHTARROW",
                icon_only=True, 
                emboss=False)
        row.label(text="选择快捷键功能", icon="MODIFIER")
        row.prop(self, "to_show_switch_notice")
        row.prop(self, "to_show_to_switcher")

        if self.show_shortcut_options:
            # 选项内容区域
            if self.to_show_switch_notice:
                content_box = box.box()

            #row = content_box.row()
            
            
                row = content_box.row()
                row.prop(self, "switch_notice_scale", slider=True , text="切换提示大小")
                row = content_box.row()
                row.prop(self, "switch_notice_themes")
                row = content_box.row()
                row.prop(self, "switch_notice_position")

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
            row = content_box.row() 
            row.prop(self, "ctrl_shift_alt_mouse_right")

        # -----------------------------------------------
        # 极速菜单1 设置项 BOX框
        box = layout.box()
        row = box.row()
        row.prop(self, "quick_menu_one", 
                icon="DOWNARROW_HLT" if self.quick_menu_one else "RIGHTARROW",
                icon_only=True, 
                emboss=False)
        row.label(text="极速菜单1", icon="COLLECTION_COLOR_01")
            
        if self.quick_menu_one:

            top_box = box.box()
            top_box.label(text="物体模式", icon="OBJECT_DATA")
            row = top_box.row()
            row.prop(self, "panelone_mode1_visible",
                    icon="HIDE_OFF" if self.panelone_mode1_visible else "HIDE_ON")
            row.prop(self, "panelone_mode1_col1_title", text="")
            row.prop(self, "panelone_mode1_col2_title", text="")
            row.prop(self, "panelone_mode1_col3_title", text="")
            row.prop(self, "panelone_mode1_col4_title", text="")
            row.prop(self, "panelone_mode1_col5_title", text="")
            row.prop(self, "panelone_mode1_col6_title", text="")
            row.prop(self, "panelone_mode1_col7_title", text="")
            row.prop(self, "panelone_mode1_col8_title", text="")
        
            top_box.label(text="网络编辑模式", icon="EDITMODE_HLT")
            row = top_box.row()
            row.prop(self, "panelone_mode2_visible",
                    icon="HIDE_OFF" if self.panelone_mode2_visible else "HIDE_ON")
            row.prop(self, "panelone_mode2_col1_title", text="")
            row.prop(self, "panelone_mode2_col2_title", text="")
            row.prop(self, "panelone_mode2_col3_title", text="")
            row.prop(self, "panelone_mode2_col4_title", text="")
            row.prop(self, "panelone_mode2_col5_title", text="")
            row.prop(self, "panelone_mode2_col6_title", text="")
            row.prop(self, "panelone_mode2_col7_title", text="")
            row.prop(self, "panelone_mode2_col8_title", text="")





        # -----------------------------------------------
        # 极速菜单2 设置项 BOX框
        box = layout.box()
        row = box.row()
        row.prop(self, "quick_menu_two", 
                icon="DOWNARROW_HLT" if self.quick_menu_two else "RIGHTARROW",
                icon_only=True, 
                emboss=False)
        row.label(text="极速菜单2", icon="COLLECTION_COLOR_02")            
        
        if self.quick_menu_two:

            # 第一列设置项：
            top_box = box.box()
            top_box.label(text="lj fdljf dlf jl")
            row = top_box.row()
            row.prop(self, "panelone_mode2_col1_title", text="")
            row.prop(self, "panelone_mode2_col2_title", text="")
            row.prop(self, "panelone_mode2_col3_title", text="")
            row.prop(self, "panelone_mode2_col4_title", text="")
            row.prop(self, "panelone_mode2_col5_title", text="")
            row.prop(self, "panelone_mode2_col6_title", text="")
            row.prop(self, "panelone_mode2_col7_title", text="")
            row.prop(self, "panelone_mode2_col8_title", text="")




    def load_from_file(self):
        """加载 JSON 文件中的设置，并依次写入 AddonPreferences 属性"""
        settings = load_settings()
        if settings:
            # 假设所有设置均以属性名称为 key 存储
            for prop_name, value in settings.items():
                if hasattr(self, prop_name):
                    try:
                        setattr(self, prop_name, value)
                    except Exception as e:
                        print(f"为 {prop_name} 赋值时出错: {e}")

    def save_to_file(self):
        """遍历所有属性，将其保存到 JSON 文件"""
        settings = {}
        # 遍历所有在 bl_rna.properties 中注册的属性
        for prop in self.bl_rna.properties:
            if prop.is_readonly:
                continue  # 跳过只读属性
            prop_name = prop.identifier
            settings[prop_name] = getattr(self, prop_name)
        save_settings(settings)

    # 为所有属性添加update回调

def register():
    # 注册插件类
    bpy.utils.register_class(QuickSwitchAddonPreferences)
    
    # 创建新的首选项实例并强制加载设置
    def force_load_settings():
        try:
            # 创建新的首选项实例
            prefs = QuickSwitchAddonPreferences()
            
            # 加载settings.json
            settings = load_settings()
            if not settings:
                print("settings.json为空或不存在")
                return
                
            print("强制加载设置...")
            
            # 遍历所有可写属性
            for prop in prefs.bl_rna.properties:
                if prop.is_readonly:
                    continue
                    
                prop_name = prop.identifier
                if prop_name in settings:
                    try:
                        # 强制设置属性值
                        setattr(prefs, prop_name, settings[prop_name])
                        print(f"强制设置: {prop_name} = {settings[prop_name]}")
                    except Exception as e:
                        print(f"设置属性 {prop_name} 失败: {str(e)}")
                else:
                    print(f"settings.json中缺少属性: {prop_name}")
                    
            # 保存回Blender首选项
            addon = bpy.context.preferences.addons.get(__package__)
            if addon:
                addon.preferences = prefs
                print("首选项已强制更新")
            else:
                print("无法获取插件首选项实例")
                
        except Exception as e:
            print(f"强制加载设置失败: {str(e)}")
            import traceback
            traceback.print_exc()
    
    # 立即执行强制加载
    force_load_settings()

def unregister():
    # 卸载前保存当前设置
    try:
        prefs = bpy.context.preferences.addons[__package__].preferences
        prefs.save_to_file()
    except:
        pass  # 防止卸载时出错
    bpy.utils.unregister_class(QuickSwitchAddonPreferences)
