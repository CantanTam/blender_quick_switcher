import bpy

from .button_operator_dict import button_press_function

class QUICK_POPUP_MENU_OT_one(bpy.types.Operator):
    bl_idname = "popup.quick_menu_one"
    bl_label = "极速菜单1"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        return {'FINISHED'}

    def invoke(self, context, event):
        # 使用invoke_popup并设置动态宽度
        prefs = context.preferences.addons[__package__].preferences


        # ---------------↓↓↓↓ 计算第 col1 的宽度 ↓↓↓↓-----------------------
        # range(1, 4) 表示从 1 开始到 4 之前。如果 col? 列全部按钮全部为 NO_BUTTON 则直接隐藏这一列
        typeandmode = bpy.context.active_object.type+bpy.context.active_object.mode

        # 获取 col1 所有按钮对应的设置值（也就是“键”）的对应的元组，单个元组是指这个按钮可以作用的 typeandmode
        # ，当 col1 所有按钮的所有元组的所有元素，也就是所有支持的 typeandmode ，都不和当前的 typeandmode 对应
        # ，则直接隐藏这一行，下面一样。
        col1_tuples = ()
        for i in range(1, 11):
            col1_tuples += button_press_function.get(getattr(prefs, f"panel1_col1_button{i}"), ())

        col2_tuples = ()
        for i in range(1, 11):
            col2_tuples += button_press_function.get(getattr(prefs, f"panel1_col2_button{i}"), ())

        col3_tuples = ()
        for i in range(1, 11):
            col3_tuples += button_press_function.get(getattr(prefs, f"panel1_col3_button{i}"), ())

        col4_tuples = ()
        for i in range(1, 11):
            col4_tuples += button_press_function.get(getattr(prefs, f"panel1_col4_button{i}"), ())

        col5_tuples = ()
        for i in range(1, 11):
            col5_tuples += button_press_function.get(getattr(prefs, f"panel1_col5_button{i}"), ())

        col6_tuples = ()
        for i in range(1, 11):
            col6_tuples += button_press_function.get(getattr(prefs, f"panel1_col6_button{i}"), ())

        # 计算各列宽度
        col_widths = []
        for i in range(1, 7):
            col_title = getattr(prefs, f"panel_one_col{i}_title").strip()
            col_tuples = locals()[f"col{i}_tuples"]
            if col_title != "" and typeandmode in col_tuples:
                col_widths.append(getattr(prefs, f"panel_one_col{i}_width") )
            else:
                col_widths.append(0)
        
        # 计算总宽度
        total_col_width = sum(col_widths)
        
        return context.window_manager.invoke_popup(self, width=total_col_width)



    def draw(self, context):
        layout = self.layout

        prefs = context.preferences.addons[__package__].preferences

        # 利用typeandmode 和
        typeandmode = bpy.context.active_object.type+bpy.context.active_object.mode

        col1_tuples = ()
        for i in range(1, 11):
            col1_tuples += button_press_function.get(getattr(prefs, f"panel1_col1_button{i}"), ())

        col2_tuples = ()
        for i in range(1, 11):
            col2_tuples += button_press_function.get(getattr(prefs, f"panel1_col2_button{i}"), ())

        col3_tuples = ()
        for i in range(1, 11):
            col3_tuples += button_press_function.get(getattr(prefs, f"panel1_col3_button{i}"), ())

        col4_tuples = ()
        for i in range(1, 11):
            col4_tuples += button_press_function.get(getattr(prefs, f"panel1_col4_button{i}"), ())

        col5_tuples = ()
        for i in range(1, 11):
            col5_tuples += button_press_function.get(getattr(prefs, f"panel1_col5_button{i}"), ())

        col6_tuples = ()
        for i in range(1, 11):
            col6_tuples += button_press_function.get(getattr(prefs, f"panel1_col6_button{i}"), ())

        col1_width = prefs.panel_one_col1_width if prefs.panel_one_col1_title.strip() != "" and typeandmode in col1_tuples else 0
        col2_width = prefs.panel_one_col2_width if prefs.panel_one_col2_title.strip() != "" and typeandmode in col2_tuples else 0
        col3_width = prefs.panel_one_col3_width if prefs.panel_one_col3_title.strip() != "" and typeandmode in col3_tuples else 0
        col4_width = prefs.panel_one_col4_width if prefs.panel_one_col4_title.strip() != "" and typeandmode in col4_tuples else 0
        col5_width = prefs.panel_one_col5_width if prefs.panel_one_col5_title.strip() != "" and typeandmode in col5_tuples else 0
        col6_width = prefs.panel_one_col6_width if prefs.panel_one_col6_title.strip() != "" and typeandmode in col6_tuples else 0

        # ---------------↑↑↑↑ 再计算一次第 col1 的宽度 ↑↑↑↑-----------------------


        total_col_width = col1_width + col2_width + col3_width + col4_width + col5_width + col6_width


        # ------------创建十列布局-------------------------
        row = layout.row()



        if prefs.panel_one_col1_title.strip() != "" and typeandmode in col1_tuples:
            col1 = row.column(align=True)
            col1.scale_x = col1_width  / total_col_width  # 设置第一列宽度比例
        if prefs.panel_one_col2_title.strip() != "" and typeandmode in col2_tuples:
            col2 = row.column(align=True)
            col2.scale_x = col2_width  / total_col_width  # 设置第二列宽度比例
        if prefs.panel_one_col3_title.strip() != "" and typeandmode in col3_tuples:
            col3 = row.column(align=True)
            col3.scale_x = col3_width  / total_col_width  # 设置第三列宽度比例
        if prefs.panel_one_col4_title.strip() != "" and typeandmode in col4_tuples:
            col4 = row.column(align=True)
            col4.scale_x = col4_width  / total_col_width  # 设置第四列宽度比例
        if prefs.panel_one_col5_title.strip() != "" and typeandmode in col5_tuples:
            col5 = row.column(align=True)
            col5.scale_x = col5_width  / total_col_width  # 设置第五列宽度比例
        if prefs.panel_one_col6_title.strip() != "" and typeandmode in col6_tuples:
            col6 = row.column(align=True)
            col6.scale_x = col6_width  / total_col_width  # 设置第六列宽度比例

        # 第一列菜单项
        if prefs.panel_one_col1_title.strip() != "" and typeandmode in col1_tuples:
            col1.label(text=prefs.panel_one_col1_title, icon='PRESET')
            col1.separator()
            # 我在设置preference的时候，已经为 panel1_col1_button1 在下拉菜单选定了值，例如
            # teston，现在是需要用用 'testone' 这个值在 button_press_function 当中寻找
            # ("mode.tab_switch","智能切换","CUBE","MESH") 这个元组当中的 'mode.tab_switch'
            # "智能切换","CUBE"这些值
            for i in range(1, 11):
                col1_button_value = getattr(prefs, f"panel1_col1_button{i}")
                temp_col1_button = button_press_function.get(col1_button_value)
                if col1_button_value == 'SEPARATOR':
                    col1.separator()
                elif temp_col1_button and typeandmode in temp_col1_button:
                    col1.operator(temp_col1_button[0], text=temp_col1_button[1], icon=temp_col1_button[2])

        # 第二列菜单项
        if prefs.panel_one_col2_title.strip() != "" and typeandmode in col2_tuples:
            col2.label(text=prefs.panel_one_col2_title, icon='PRESET')
            col2.separator()

            for i in range(1, 11):
                col2_button_value = getattr(prefs, f"panel1_col2_button{i}")
                temp_col2_button = button_press_function.get(col2_button_value)
                if col2_button_value == 'SEPARATOR':
                    col2.separator()
                elif temp_col2_button and typeandmode in temp_col2_button:
                    col2.operator(temp_col2_button[0], text=temp_col2_button[1], icon=temp_col2_button[2])

        # 第三列菜单项
        if prefs.panel_one_col3_title.strip() != "" and typeandmode in col3_tuples:
            col3.label(text=prefs.panel_one_col3_title, icon='PRESET')
            col3.separator()

            for i in range(1, 11):
                col3_button_value = getattr(prefs, f"panel1_col3_button{i}")
                temp_col3_button = button_press_function.get(col3_button_value)
                if col3_button_value == 'SEPARATOR':
                    col3.separator()
                elif temp_col3_button and typeandmode in temp_col3_button:
                    col3.operator(temp_col3_button[0], text=temp_col3_button[1], icon=temp_col3_button[2])

        # 第四列菜单项
        if prefs.panel_one_col4_title.strip() != "" and typeandmode in col4_tuples:
            col4.label(text=prefs.panel_one_col4_title, icon='PRESET')
            col4.separator()

            for i in range(1, 11):
                col4_button_value = getattr(prefs, f"panel1_col4_button{i}")
                temp_col4_button = button_press_function.get(col4_button_value)
                if col4_button_value == 'SEPARATOR':
                    col4.separator()
                elif temp_col4_button and typeandmode in temp_col4_button:
                    col4.operator(temp_col4_button[0], text=temp_col4_button[1], icon=temp_col4_button[2])

        # 第五列菜单项
        if prefs.panel_one_col5_title.strip() != "" and typeandmode in col5_tuples:
            col5.label(text=prefs.panel_one_col5_title, icon='PRESET')
            col5.separator()

            for i in range(1, 11):
                col5_button_value = getattr(prefs, f"panel1_col5_button{i}")
                temp_col5_button = button_press_function.get(col5_button_value)
                if col5_button_value == 'SEPARATOR':
                    col5.separator()
                elif temp_col5_button and typeandmode in temp_col5_button:
                    col5.operator(temp_col5_button[0], text=temp_col5_button[1], icon=temp_col5_button[2])

        # 第六列菜单项
        if prefs.panel_one_col6_title.strip() != "" and typeandmode in col6_tuples:
            col6.label(text=prefs.panel_one_col6_title, icon='PRESET')
            col6.separator()

            for i in range(1, 11):
                col6_button_value = getattr(prefs, f"panel1_col6_button{i}")
                temp_col6_button = button_press_function.get(col6_button_value)
                if col6_button_value == 'SEPARATOR':
                    col6.separator()
                elif temp_col6_button and typeandmode in temp_col6_button:
                    col6.operator(temp_col6_button[0], text=temp_col6_button[1], icon=temp_col6_button[2])

# 需要另外写一个 call.popup_menu_one 函数来调用这个类函数
