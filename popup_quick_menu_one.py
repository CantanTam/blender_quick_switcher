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
        if all(getattr(prefs, f"panel1_col1_button{i}") in ["NO_BUTTON", "SEPARATOR"] for i in range(1, 11)):
            bybutton_show_col1 = 0
        else:
            bybutton_show_col1 = 1

        typeandmode = bpy.context.active_object.type+bpy.context.active_object.mode

        # 获取 col1 所有按钮对应的设置值（也就是“键”）的对应的元组，单个元组是指这个按钮可以作用的 typeandmode
        # ，当 col1 所有按钮的所有元组的所有元素，也就是所有支持的 typeandmode ，都不和当前的 typeandmode 对应
        # ，则直接隐藏这一行，下面一样。
        col1_tuples = (
            button_press_function.get(prefs.panel1_col1_button1, ()) +
            button_press_function.get(prefs.panel1_col1_button2, ()) +
            button_press_function.get(prefs.panel1_col1_button3, ()) +
            button_press_function.get(prefs.panel1_col1_button4, ()) +
            button_press_function.get(prefs.panel1_col1_button5, ()) +
            button_press_function.get(prefs.panel1_col1_button6, ()) +
            button_press_function.get(prefs.panel1_col1_button7, ()) +
            button_press_function.get(prefs.panel1_col1_button8, ()) +
            button_press_function.get(prefs.panel1_col1_button9, ()) +
            button_press_function.get(prefs.panel1_col1_button10, ())
        )

        col1_width = prefs.panel_one_col1_width+10 if prefs.panel_one_col1_title.strip() != "" and bybutton_show_col1 != 0 and typeandmode in col1_tuples else 0
        # ---------------↑↑↑↑ 计算第 col1 的宽度 ↑↑↑↑-----------------------


        col2_width = prefs.panel_one_col2_width+10 if prefs.panel_one_col2_title.strip() != "" else 0
        col3_width = prefs.panel_one_col3_width+10 if prefs.panel_one_col3_title.strip() != "" else 0

        total_col_width = col1_width + col2_width + col3_width
        
        return context.window_manager.invoke_popup(self, width=total_col_width)

    def draw(self, context):
        layout = self.layout


        prefs = context.preferences.addons[__package__].preferences

        # 利用typeandmode 和
        typeandmode = bpy.context.active_object.type+bpy.context.active_object.mode

        col1_tuples = (
            button_press_function.get(prefs.panel1_col1_button1, ()) +
            button_press_function.get(prefs.panel1_col1_button2, ()) +
            button_press_function.get(prefs.panel1_col1_button3, ()) +
            button_press_function.get(prefs.panel1_col1_button4, ()) +
            button_press_function.get(prefs.panel1_col1_button5, ()) +
            button_press_function.get(prefs.panel1_col1_button6, ()) +
            button_press_function.get(prefs.panel1_col1_button7, ()) +
            button_press_function.get(prefs.panel1_col1_button8, ()) +
            button_press_function.get(prefs.panel1_col1_button9, ()) +
            button_press_function.get(prefs.panel1_col1_button10, ())
        )

        # 创建十列布局
        row = layout.row()

        col1_width = prefs.panel_one_col1_width if prefs.panel_one_col1_title.strip() != "" else 0
        col2_width = prefs.panel_one_col2_width if prefs.panel_one_col2_title.strip() != "" else 0
        col3_width = prefs.panel_one_col3_width if prefs.panel_one_col3_title.strip() != "" else 0

        # range(1, 4) 表示从 1 开始到 4 之前。如果 col1 列全部按钮
        if all(getattr(prefs, f"panel1_col1_button{i}") in ["NO_BUTTON", "SEPARATOR"] for i in range(1, 11)):
            bybutton_show_col1 = 0
        else:
            bybutton_show_col1 = 1


        total_col_width = col1_width * bybutton_show_col1 + col2_width + col3_width

        if prefs.panel_one_col1_title.strip() != "" and bybutton_show_col1 != 0:
            col1 = row.column(align=True)
            col1.scale_x = col1_width  / total_col_width  # 设置第一列宽度比例
        col2 = row.column(align=True)
        col2.scale_x = col2_width / total_col_width  # 设置第二列宽度比例
        col3 = row.column(align=True)
        col3.scale_x = col3_width / total_col_width  # 设置第三列宽度比例

        

        if prefs.panel_one_col1_title.strip() != "" and bybutton_show_col1 != 0 and typeandmode in col1_tuples:
            col1.label(text=prefs.panel_one_col1_title, icon='PRESET')
            col1.separator()
            # 第一列菜单项
            
            # 我在设置preference的时候，已经为 panel1_col1_button1 在下拉菜单选定了值，例如
            # teston，现在是需要用用 'testone' 这个值在 button_press_function 当中寻找
            # ("mode.tab_switch","智能切换","CUBE","MESH") 这个元组当中的 'mode.tab_switch'
            # "智能切换","CUBE"这些值
            temp_col1_button1 = button_press_function.get(prefs.panel1_col1_button1)
            if prefs.panel1_col1_button1 != 'NO_BUTTON' and typeandmode in temp_col1_button1:
                if prefs.panel1_col1_button1 != 'SEPARATOR':
                    col1.operator(temp_col1_button1[0], text=temp_col1_button1[1], icon=temp_col1_button1[2])
                else: 
                    col1.separator()

            temp_col1_button2 = button_press_function.get(prefs.panel1_col1_button2)
            if prefs.panel1_col1_button2 != 'NO_BUTTON' and typeandmode in temp_col1_button2:
                if prefs.panel1_col1_button2 != 'SEPARATOR':
                    col1.operator(temp_col1_button2[0], text=temp_col1_button2[1], icon=temp_col1_button2[2])
                else:
                    col1.separator()
            
            temp_col1_button3 = button_press_function.get(prefs.panel1_col1_button3)
            if prefs.panel1_col1_button3 != 'NO_BUTTON' and typeandmode in temp_col1_button3:
                if prefs.panel1_col1_button3 != 'SEPARATOR':
                    col1.operator(temp_col1_button3[0], text=temp_col1_button3[1], icon=temp_col1_button3[2])
                else: 
                    col1.separator()

            temp_col1_button4 = button_press_function.get(prefs.panel1_col1_button4)
            if prefs.panel1_col1_button4 != 'NO_BUTTON' and typeandmode in temp_col1_button4:
                if prefs.panel1_col1_button4 != 'SEPARATOR':
                    col1.operator(temp_col1_button4[0], text=temp_col1_button4[1], icon=temp_col1_button4[2])
                else: 
                    col1.separator()

            #col1.operator("mode.menu_switch", text="模式切换2", icon='EDITMODE_HLT')
            #col1.operator("mode.menu_switch", text="模式切换3", icon='MODIFIER')

        if prefs.panel_one_col2_title and prefs.panel_one_col2_title.strip():
            col2.label(text=prefs.panel_one_col2_title, icon='PRESET')
            col2.separator()
            # 第二列菜单项
            col2.operator("mode.menu_switch", text="模式切换4", icon='RESTRICT_SELECT_OFF')
            col2.operator("mode.menu_switch", text="模式切换5", icon='RESTRICT_VIEW_OFF')
            col2.operator("mode.menu_switch", text="模式切换6", icon='HIDE_OFF')

        if prefs.panel_one_col3_title and prefs.panel_one_col3_title.strip():
            col3.label(text=prefs.panel_one_col3_title, icon='PRESET')
            col3.separator()
            # 第三列菜单项
            col3.operator("switch.vertex_edge_face", text="模式切换7", icon='MODIFIER_DATA')
            col3.operator("mode.menu_switch", text="")
            col3.operator("mode.menu_switch", text="模式切换9", icon='MODIFIER_OFF')


# 需要另外写一个 call.popup_menu_one 函数来调用这个类函数
