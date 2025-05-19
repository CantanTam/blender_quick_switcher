import bpy

from .button_operator_dict import button_press_function

# 以原来的 oopup menu two 作为基础的样式备份
class QUICK_POPUP_MENU_OT_one_meshedit(bpy.types.Menu):
    bl_idname = "popup.quick_menu_one_meshedit"
    bl_label = ""
    bl_options = {'SEARCH_ON_KEY_PRESS'}

    # 通用的插件名称引用
    ADDON_NAME = __package__.split('.')[0]

    def draw(self, context):
        prefs = context.preferences.addons[self.ADDON_NAME].preferences

        layout = self.layout

        # 利用typeandmode 和
        typeandmode = bpy.context.active_object.type+bpy.context.active_object.mode

        col1_tuples = ()
        for i in range(1, 11):
            col1_tuples += button_press_function.get(getattr(prefs, f"panelone_mode2_col1_button{i}"), ())

        col2_tuples = ()
        for i in range(1, 11):
            col2_tuples += button_press_function.get(getattr(prefs, f"panelone_mode2_col2_button{i}"), ())

        col3_tuples = ()
        for i in range(1, 11):
            col3_tuples += button_press_function.get(getattr(prefs, f"panelone_mode2_col3_button{i}"), ())

        col4_tuples = ()
        for i in range(1, 11):
            col4_tuples += button_press_function.get(getattr(prefs, f"panelone_mode2_col4_button{i}"), ())

        col5_tuples = ()
        for i in range(1, 11):
            col5_tuples += button_press_function.get(getattr(prefs, f"panelone_mode2_col5_button{i}"), ())

        col6_tuples = ()
        for i in range(1, 11):
            col6_tuples += button_press_function.get(getattr(prefs, f"panelone_mode2_col6_button{i}"), ())

        col7_tuples = ()
        for i in range(1, 11):
            col7_tuples += button_press_function.get(getattr(prefs, f"panelone_mode2_col7_button{i}"), ())

        col8_tuples = ()
        for i in range(1, 11):
            col8_tuples += button_press_function.get(getattr(prefs, f"panelone_mode2_col8_button{i}"), ())

        row = layout.row()

        if prefs.panelone_mode2_col1_title.strip() != "" and (typeandmode in col1_tuples or "all" in col1_tuples):
            col1 = row.column(align=True)
        if prefs.panelone_mode2_col2_title.strip() != "" and (typeandmode in col2_tuples or "all" in col2_tuples):
            col2 = row.column(align=True)
        if prefs.panelone_mode2_col3_title.strip() != "" and (typeandmode in col3_tuples or "all" in col3_tuples):
            col3 = row.column(align=True)
        if prefs.panelone_mode2_col4_title.strip() != "" and (typeandmode in col4_tuples or "all" in col4_tuples):
            col4 = row.column(align=True)
        if prefs.panelone_mode2_col5_title.strip() != "" and (typeandmode in col5_tuples or "all" in col5_tuples):
            col5 = row.column(align=True)
        if prefs.panelone_mode2_col6_title.strip() != "" and (typeandmode in col6_tuples or "all" in col6_tuples):
            col6 = row.column(align=True)
        if prefs.panelone_mode2_col7_title.strip() != "" and (typeandmode in col7_tuples or "all" in col7_tuples):
            col7 = row.column(align=True)
        if prefs.panelone_mode2_col8_title.strip() != "" and (typeandmode in col8_tuples or "all" in col8_tuples):
            col8 = row.column(align=True)

        # 第一列菜单项
        if prefs.panelone_mode2_col1_title.strip() != "" and (typeandmode in col1_tuples or "all" in col1_tuples) :
            col1.label(text=prefs.panelone_mode2_col1_title, icon='PRESET')
            col1.separator()
            # 我在设置preference的时候，已经为 panelone_mode2_col1_button1 在下拉菜单选定了值，例如
            # teston，现在是需要用用 'testone' 这个值在 button_press_function 当中寻找
            # ("mode.tab_switch","智能切换","CUBE","MESH") 这个元组当中的 'mode.tab_switch'
            # "智能切换","CUBE"这些值
            for i in range(1, 11):
                col1_button_value = getattr(prefs, f"panelone_mode2_col1_button{i}")
                temp_col1_button = button_press_function.get(col1_button_value)
                if col1_button_value == 'SEPARATOR':
                    col1.separator()
                elif temp_col1_button and typeandmode in temp_col1_button:
                    col1.operator(temp_col1_button[0], text=temp_col1_button[1], icon=temp_col1_button[2])
                elif temp_col1_button and "all" in temp_col1_button: # "all" 在所有场景都显示
                    col1.operator(temp_col1_button[0], text=temp_col1_button[1], icon=temp_col1_button[2])

        # 第二列菜单项
        if prefs.panelone_mode2_col2_title.strip() != "" and (typeandmode in col2_tuples or "all" in col2_tuples):
            col2.label(text=prefs.panelone_mode2_col2_title, icon='PRESET')
            col2.separator()

            for i in range(1, 11):
                col2_button_value = getattr(prefs, f"panelone_mode2_col2_button{i}")
                temp_col2_button = button_press_function.get(col2_button_value)
                if col2_button_value == 'SEPARATOR':
                    col2.separator()
                elif temp_col2_button and typeandmode in temp_col2_button:
                    col2.operator(temp_col2_button[0], text=temp_col2_button[1], icon=temp_col2_button[2])
                elif temp_col2_button and "all" in temp_col2_button: # "all" 在所有场景都显示
                    col2.operator(temp_col2_button[0], text=temp_col2_button[1], icon=temp_col2_button[2])

        # 第三列菜单项
        if prefs.panelone_mode2_col3_title.strip() != "" and (typeandmode in col3_tuples or "all" in col3_tuples):
            col3.label(text=prefs.panelone_mode2_col3_title, icon='PRESET')
            col3.separator()

            for i in range(1, 11):
                col3_button_value = getattr(prefs, f"panelone_mode2_col3_button{i}")
                temp_col3_button = button_press_function.get(col3_button_value)
                if col3_button_value == 'SEPARATOR':
                    col3.separator()
                elif temp_col3_button and typeandmode in temp_col3_button:
                    col3.operator(temp_col3_button[0], text=temp_col3_button[1], icon=temp_col3_button[2])
                elif temp_col3_button and "all" in temp_col3_button: # "all" 在所有场景都显示
                    col3.operator(temp_col3_button[0], text=temp_col3_button[1], icon=temp_col3_button[2])

        # 第四列菜单项
        if prefs.panelone_mode2_col4_title.strip() != "" and (typeandmode in col4_tuples or "all" in col4_tuples):
            col4.label(text=prefs.panelone_mode2_col4_title, icon='PRESET')
            col4.separator()

            for i in range(1, 11):
                col4_button_value = getattr(prefs, f"panelone_mode2_col4_button{i}")
                temp_col4_button = button_press_function.get(col4_button_value)
                if col4_button_value == 'SEPARATOR':
                    col4.separator()
                elif temp_col4_button and typeandmode in temp_col4_button:
                    col4.operator(temp_col4_button[0], text=temp_col4_button[1], icon=temp_col4_button[2])
                elif temp_col4_button and "all" in temp_col4_button: # "all" 在所有场景都显示
                    col4.operator(temp_col4_button[0], text=temp_col4_button[1], icon=temp_col4_button[2])

        # 第五列菜单项
        if prefs.panelone_mode2_col5_title.strip() != "" and (typeandmode in col5_tuples or "all" in col5_tuples):
            col5.label(text=prefs.panelone_mode2_col5_title, icon='PRESET')
            col5.separator()

            for i in range(1, 11):
                col5_button_value = getattr(prefs, f"panelone_mode2_col5_button{i}")
                temp_col5_button = button_press_function.get(col5_button_value)
                if col5_button_value == 'SEPARATOR':
                    col5.separator()
                elif temp_col5_button and typeandmode in temp_col5_button:
                    col5.operator(temp_col5_button[0], text=temp_col5_button[1], icon=temp_col5_button[2])
                elif temp_col5_button and "all" in temp_col5_button: # "all" 在所有场景都显示
                    col5.operator(temp_col5_button[0], text=temp_col5_button[1], icon=temp_col5_button[2])

        # 第六列菜单项
        if prefs.panelone_mode2_col6_title.strip() != "" and (typeandmode in col6_tuples or "all" in col6_tuples):
            col6.label(text=prefs.panelone_mode2_col6_title, icon='PRESET')
            col6.separator()

            for i in range(1, 11):
                col6_button_value = getattr(prefs, f"panelone_mode2_col6_button{i}")
                temp_col6_button = button_press_function.get(col6_button_value)
                if col6_button_value == 'SEPARATOR':
                    col6.separator()
                elif temp_col6_button and typeandmode in temp_col6_button:
                    col6.operator(temp_col6_button[0], text=temp_col6_button[1], icon=temp_col6_button[2])
                elif temp_col6_button and "all" in temp_col6_button: # "all" 在所有场景都显示
                    col6.operator(temp_col6_button[0], text=temp_col6_button[1], icon=temp_col6_button[2])

        # 第七列菜单项
        if prefs.panelone_mode2_col7_title.strip() != "" and (typeandmode in col7_tuples or "all" in col7_tuples):
            col7.label(text=prefs.panelone_mode2_col7_title, icon='PRESET')
            col7.separator()

            for i in range(1, 11):
                col7_button_value = getattr(prefs, f"panelone_mode2_col7_button{i}")
                temp_col7_button = button_press_function.get(col7_button_value)
                if col7_button_value == 'SEPARATOR':
                    col7.separator()
                elif temp_col7_button and typeandmode in temp_col7_button:
                    col7.operator(temp_col7_button[0], text=temp_col7_button[1], icon=temp_col7_button[2])
                elif temp_col7_button and "all" in temp_col7_button: # "all" 在所有场景都显示
                    col7.operator(temp_col7_button[0], text=temp_col7_button[1], icon=temp_col7_button[2])

        # 第八列菜单项
        if prefs.panelone_mode2_col8_title.strip() != "" and (typeandmode in col8_tuples or "all" in col8_tuples):
            col8.label(text=prefs.panelone_mode2_col8_title, icon='PRESET')
            col8.separator()

            for i in range(1, 11):
                col8_button_value = getattr(prefs, f"panelone_mode2_col8_button{i}")
                temp_col8_button = button_press_function.get(col8_button_value)
                if col8_button_value == 'SEPARATOR':
                    col8.separator()
                elif temp_col8_button and typeandmode in temp_col8_button:
                    col8.operator(temp_col8_button[0], text=temp_col8_button[1], icon=temp_col8_button[2])
                elif temp_col8_button and "all" in temp_col8_button: # "all" 在所有场景都显示
                    col8.operator(temp_col8_button[0], text=temp_col8_button[1], icon=temp_col8_button[2])

# 需要另外写一个 call.popup_menu_two 函数来调用这个类函数
