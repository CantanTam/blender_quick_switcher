import bpy

from ..button_dicts.button_dict_all import button_press_function

class QUICK_POPUP_MENU_OT_one_greasepencilvertex(bpy.types.Menu):
    bl_idname = "popup.quick_menu_one_greasepencilvertex"
    bl_label = "蜡笔顶点绘制模式"
    bl_options = {'SEARCH_ON_KEY_PRESS'}

    # 通用的插件名称引用
    ADDON_NAME = __package__.split('.')[0]

    @classmethod
    def poll(cls, context):
        return context.preferences.addons[cls.ADDON_NAME].preferences.panelone_mode16_visible

    def draw(self, context):
        prefs = context.preferences.addons[self.ADDON_NAME].preferences
        layout = self.layout
        row = layout.row()

        if prefs.panelone_mode16_col1_title.strip() != "" :
            col1 = row.column()
        if prefs.panelone_mode16_col2_title.strip() != "":
            col2 = row.column()
        if prefs.panelone_mode16_col3_title.strip() != "":
            col3 = row.column()
        if prefs.panelone_mode16_col4_title.strip() != "":
            col4 = row.column()
        if prefs.panelone_mode16_col5_title.strip() != "":
            col5 = row.column()
        if prefs.panelone_mode16_col6_title.strip() != "":
            col6 = row.column()
        if prefs.panelone_mode16_col7_title.strip() != "":
            col7 = row.column()
        if prefs.panelone_mode16_col8_title.strip() != "":
            col8 = row.column()

        # 第一列菜单项
        if prefs.panelone_mode16_col1_title.strip() != "":
            col1.label(text=prefs.panelone_mode16_col1_title, icon='PRESET')
            col1.separator()
            for i in range(1, 11):
                col1_button_value = getattr(prefs, f"panelone_mode16_col1_button{i}")
                temp_col1_button = button_press_function.get(col1_button_value)
                if col1_button_value == 'SEPARATOR':
                    col1.separator()
                elif temp_col1_button:
                    col1.operator(temp_col1_button[0], text=temp_col1_button[1], icon=temp_col1_button[2])
                    #break


        # 第二列菜单项
        if prefs.panelone_mode16_col2_title.strip() != "":
            col2.label(text=prefs.panelone_mode16_col2_title, icon='PRESET')
            col2.separator()
            for i in range(1, 11):
                col2_button_value = getattr(prefs, f"panelone_mode16_col2_button{i}")
                temp_col2_button = button_press_function.get(col2_button_value)
                if col2_button_value == 'SEPARATOR':
                    col2.separator()
                elif temp_col2_button:
                    col2.operator(temp_col2_button[0], text=temp_col2_button[1], icon=temp_col2_button[2])


        # 第三列菜单项
        if prefs.panelone_mode16_col3_title.strip() != "":
            col3.label(text=prefs.panelone_mode16_col3_title, icon='PRESET')
            col3.separator()
            for i in range(1, 11):
                col3_button_value = getattr(prefs, f"panelone_mode16_col3_button{i}")
                temp_col3_button = button_press_function.get(col3_button_value)
                if col3_button_value == 'SEPARATOR':
                    col3.separator()
                elif temp_col3_button:
                    col3.operator(temp_col3_button[0], text=temp_col3_button[1], icon=temp_col3_button[2])


        # 第四列菜单项
        if prefs.panelone_mode16_col4_title.strip() != "":
            col4.label(text=prefs.panelone_mode16_col4_title, icon='PRESET')
            col4.separator()
            for i in range(1, 11):
                col4_button_value = getattr(prefs, f"panelone_mode16_col4_button{i}")
                temp_col4_button = button_press_function.get(col4_button_value)
                if col4_button_value == 'SEPARATOR':
                    col4.separator()
                elif temp_col4_button:
                    col4.operator(temp_col4_button[0], text=temp_col4_button[1], icon=temp_col4_button[2])


        # 第五列菜单项
        if prefs.panelone_mode16_col5_title.strip() != "":
            col5.label(text=prefs.panelone_mode16_col5_title, icon='PRESET')
            col5.separator()
            for i in range(1, 11):
                col5_button_value = getattr(prefs, f"panelone_mode16_col5_button{i}")
                temp_col5_button = button_press_function.get(col5_button_value)
                if col5_button_value == 'SEPARATOR':
                    col5.separator()
                elif temp_col5_button:
                    col5.operator(temp_col5_button[0], text=temp_col5_button[1], icon=temp_col5_button[2])


        # 第六列菜单项
        if prefs.panelone_mode16_col6_title.strip() != "":
            col6.label(text=prefs.panelone_mode16_col6_title, icon='PRESET')
            col6.separator()
            for i in range(1, 11):
                col6_button_value = getattr(prefs, f"panelone_mode16_col6_button{i}")
                temp_col6_button = button_press_function.get(col6_button_value)
                if col6_button_value == 'SEPARATOR':
                    col6.separator()
                elif temp_col6_button:
                    col6.operator(temp_col6_button[0], text=temp_col6_button[1], icon=temp_col6_button[2])


        # 第七列菜单项
        if prefs.panelone_mode16_col7_title.strip() != "":
            col7.label(text=prefs.panelone_mode16_col7_title, icon='PRESET')
            col7.separator()
            for i in range(1, 11):
                col7_button_value = getattr(prefs, f"panelone_mode16_col7_button{i}")
                temp_col7_button = button_press_function.get(col7_button_value)
                if col7_button_value == 'SEPARATOR':
                    col7.separator()
                elif temp_col7_button:
                    col7.operator(temp_col7_button[0], text=temp_col7_button[1], icon=temp_col7_button[2])


        # 第八列菜单项
        if prefs.panelone_mode16_col8_title.strip() != "":
            col8.label(text=prefs.panelone_mode16_col8_title, icon='PRESET')
            col8.separator()
            for i in range(1, 11):
                col8_button_value = getattr(prefs, f"panelone_mode16_col8_button{i}")
                temp_col8_button = button_press_function.get(col8_button_value)
                if col8_button_value == 'SEPARATOR':
                    col8.separator()
                elif temp_col8_button:
                    col8.operator(temp_col8_button[0], text=temp_col8_button[1], icon=temp_col8_button[2])

