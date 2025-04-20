import bpy
import webbrowser
import json
import os
from bpy.types import AddonPreferences, Operator
from bpy.props import BoolProperty, EnumProperty
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

    keys_combination_functions = [
        ('mode.menu_switch()', '弹出编辑模式菜单', '直接弹出编辑模式菜单'),
        ('switch.vertex_edge_face()', '快速切换点/线/面', '点←线←面方向快速切换'),
        ('mode.normal_up_to_down()', '上下方向快速切换编辑模式', '不弹出菜单，直接以从上到下的顺序切换编辑模式'), 
        ('mode.normal_down_to_up()', '下上方向快速切换编辑模式', '不弹出菜单，直接以从下到上的顺序切换编辑模式'), 
        ('mode.tab_switch()','切换最近两次编辑模式','比原生Tab键更合理的切换编辑模式方式'),
        ('wm.toolbar()','调用系统快捷菜单','调用Shift+Space快捷键'),
        ('call.popup_menu_one()','极速菜单1','超级菜单1'),
        ('NONE', '[ 无功能 ]', '如果快捷键和其它插件有键位冲突，可以选择[无功能]，重启Blender，注销组合键功能')
    ]





    
    ctrl_wheel_up: EnumProperty(
        name="Ctrl+鼠标上滚",
        description="选择Ctrl+鼠标上滚快捷键功能",
        items=keys_combination_functions,
        default='call.popup_menu_one()',
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
        default='mode.menu_switch()',
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

    show_shortcut_options: BoolProperty(
        name="显示快捷键选项",
        description="展开/折叠快捷键选项",
        default=False,
        update=update_preferences
    )
    

# 设置一个空按钮，如果按钮功能不适用当前模式，变成一个空白按钮
# 这个选项不在 def draw 中显示
    blank_button: EnumProperty(
        name="菜单1列1按钮1",
        description="菜单1列1按钮1功能测试",
        items=button_options_list,
        default='NO_BUTTON',
        update=update_preferences
    )




# --------↓↓↓↓ panel one 相关设置 ↓↓↓↓---------
    expand_quick_panel_one:BoolProperty(
        name="极速菜单1",
        description="展开/折叠极速菜单1",
        default=True,
        update=update_preferences
    )
    
    panel_one_col1_title: bpy.props.StringProperty(
        name="第一列标题",
        description="留空不显示该列",
        default="第一列标题",
        update=update_preferences
    )

    panel_one_col1_width: bpy.props.IntProperty(
        name="面板宽度",
        description="第一列宽度",
        default=80,
        min=55,  # 最小值
        max=150,  # 最大值
        soft_min=55,  # 拖动时的最小限制
        soft_max=150,  # 拖动时的最大限制
        update=update_preferences
    )

    panel1_col1_button1: EnumProperty(
        name="菜单1列1按钮1",
        description="菜单1列1按钮1功能测试",
        items=button_options_list,
        default='NO_BUTTON',
        update=update_preferences
    )

    panel1_col1_button2: EnumProperty(
        name="菜单1列1按钮2",
        description="菜单1列1按钮2功能测试",
        items=button_options_list,
        default='NO_BUTTON',
        update=update_preferences
    )

    panel1_col1_button3: EnumProperty(
        name="菜单1列1按钮3",
        description="菜单1列1按钮3功能测试",
        items=button_options_list,
        default='NO_BUTTON',
        update=update_preferences
    )

    panel1_col1_button4: EnumProperty(
        name="菜单1列1按钮4",
        description="菜单1列1按钮4功能测试",
        items=button_options_list,
        default='NO_BUTTON',
        update=update_preferences
    )

    panel1_col1_button5: EnumProperty(
        name="菜单1列1按钮5",
        description="菜单1列1按钮5功能测试",
        items=button_options_list,
        default='NO_BUTTON',
        update=update_preferences
    )

    panel1_col1_button6: EnumProperty(
        name="菜单1列1按钮6",
        description="菜单1列1按钮6功能测试",
        items=button_options_list,
        default='NO_BUTTON',
        update=update_preferences
    )

    panel1_col1_button7: EnumProperty(
        name="菜单1列1按钮7",
        description="菜单1列1按钮7功能测试",
        items=button_options_list,
        default='NO_BUTTON',
        update=update_preferences
    )

    panel1_col1_button8: EnumProperty(
        name="菜单1列1按钮8",
        description="菜单1列1按钮8功能测试",
        items=button_options_list,
        default='NO_BUTTON',
        update=update_preferences
    )

    panel1_col1_button9: EnumProperty(
        name="菜单1列1按钮9",
        description="菜单1列1按钮9功能测试",
        items=button_options_list,
        default='NO_BUTTON',
        update=update_preferences
    )

    panel1_col1_button10: EnumProperty(
        name="菜单1列1按钮10",
        description="菜单1列1按钮10功能测试",
        items=button_options_list,
        default='NO_BUTTON',
        update=update_preferences
    )

    # 后期添加搜索框功能
    search_filter: bpy.props.StringProperty(
        name="搜索",
        description="输入搜索内容",
        default="搜索框测试",  # 设置默认值作为placeholder
        update=update_preferences
    )

    panel_one_col2_title: bpy.props.StringProperty(
        name="第二列标题",
        description="留空不显示该列",
        default="第二列标题",
        update=update_preferences
    )

    panel_one_col2_width: bpy.props.IntProperty(
        name="面板宽度",
        description="第二列宽度",
        default=80,
        min=55,  # 最小值
        max=150,  # 最大值
        soft_min=55,  # 拖动时的最小限制
        soft_max=150,  # 拖动时的最大限制
        update=update_preferences
    )

    panel1_col2_button1: EnumProperty(
        name="菜单1列2按钮1",
        description="菜单1列2按钮1功能测试",
        items=button_options_list,
        default='NO_BUTTON',
        update=update_preferences
    )

    panel1_col2_button2: EnumProperty(
        name="菜单1列2按钮2",
        description="菜单1列2按钮2功能测试",
        items=button_options_list,
        default='NO_BUTTON',
        update=update_preferences
    )

    panel_one_col3_title: bpy.props.StringProperty(
        name="第三列标题",
        description="留空不显示该列",
        default="第三列标题",
        update=update_preferences
    )

    panel_one_col3_width: bpy.props.IntProperty(
        name="面板宽度",
        description="第三列宽度",
        default=80,
        min=55,  # 最小值
        max=150,  # 最大值
        soft_min=55,  # 拖动时的最小限制
        soft_max=150,  # 拖动时的最大限制
        update=update_preferences
    )

    panel1_col3_button1: EnumProperty(
        name="菜单1列3按钮1",
        description="菜单1列3按钮1功能测试",
        items=button_options_list,
        default='NO_BUTTON',
        update=update_preferences
    )

    panel1_col3_button2: EnumProperty(
        name="菜单1列3按钮2",
        description="菜单1列3按钮2功能测试",
        items=button_options_list,
        default='NO_BUTTON',
        update=update_preferences
    )


# --------↑↑↑↑ panel one 相关设置 ↑↑↑↑---------



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
                icon="TRIA_DOWN" if self.show_shortcut_options else "TRIA_RIGHT",
                icon_only=True, 
                emboss=False)
        row.label(text="选择快捷键功能", icon="MODIFIER")
        
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
        row.label(text="极速菜单1",icon='COLLECTION_COLOR_01')
            
        if self.expand_quick_panel_one:

            # 第一列设置项：
            top_box = box.box()
            row = top_box.row()
            row.prop(self, "panel_one_col1_title", text="",icon="TOPBAR")
            row.prop(self, "panel_one_col1_width", text="第一列宽度")

            content_box = top_box.box()
            row = content_box.row()
            row.prop(self, "panel1_col1_button1")
            #row.prop(self, "search_filter", text="", icon="VIEWZOOM")  # 搜索功能后面再开发
            row = content_box.row()
            row.prop(self, "panel1_col1_button2")
            row = content_box.row()
            row.prop(self, "panel1_col1_button3")
            row = content_box.row()
            row.prop(self, "panel1_col1_button4")

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

            # 第三列设置项：
            top_box = box.box()
            row = top_box.row()
            row.prop(self, "panel_one_col3_title", text="",icon="TOPBAR")
            row.prop(self, "panel_one_col3_width", text="第三列宽度")
            
            content_box = top_box.box()
            row = content_box.row()
            row.prop(self, "panel1_col3_button1")
            row = content_box.row()
            row.prop(self, "panel1_col3_button2")







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
