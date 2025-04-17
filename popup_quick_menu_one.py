import bpy

class QUICK_POPUP_MENU_OT_one(bpy.types.Operator):
    bl_idname = "popup.quick_menu_one"
    bl_label = "两列菜单"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        return {'FINISHED'}

    def invoke(self, context, event):
        # 使用invoke_popup并设置动态宽度
        prefs = context.preferences.addons[__package__].preferences

        col1_width = prefs.panel_one_col1_width+10 if prefs.panel_one_col1_title.strip() != "" else 0
        col2_width = prefs.panel_one_col2_width+10 if prefs.panel_one_col2_title.strip() != "" else 0
        col3_width = prefs.panel_one_col3_width+10 if prefs.panel_one_col3_title.strip() != "" else 0

        total_col_width = col1_width + col2_width + col3_width
        
        return context.window_manager.invoke_popup(self, width=total_col_width)

    def draw(self, context):
        layout = self.layout

        # 创建两列布局
        row = layout.row()
        prefs = context.preferences.addons[__package__].preferences

        col1_width = prefs.panel_one_col1_width if prefs.panel_one_col1_title.strip() != "" else 0
        col2_width = prefs.panel_one_col2_width if prefs.panel_one_col2_title.strip() != "" else 0
        col3_width = prefs.panel_one_col3_width if prefs.panel_one_col3_title.strip() != "" else 0

        total_col_width = col1_width + col2_width + col3_width

        col1 = row.column(align=True)
        col1.scale_x = col1_width / total_col_width  # 设置第一列宽度比例
        col2 = row.column(align=True)
        col2.scale_x = col2_width / total_col_width  # 设置第二列宽度比例
        col3 = row.column(align=True)
        col3.scale_x = col3_width / total_col_width  # 设置第三列宽度比例

        if prefs.panel_one_col1_title.strip() != "":
            col1.label(text=prefs.panel_one_col1_title, icon='PRESET')
            col1.separator()
            # 第一列菜单项
            col1.operator("mode.menu_switch", text="模式切换1", icon='OBJECT_DATA')
            col1.operator("mode.menu_switch", text="模式切换2", icon='EDITMODE_HLT')
            col1.operator("mode.menu_switch", text="模式切换3", icon='MODIFIER')

        if prefs.panel_one_col2_title and prefs.panel_one_col2_title.strip():
            col2.label(text=prefs.panel_one_col2_title, icon='MENU_PANEL')
            col2.separator()
            # 第二列菜单项
            col2.operator("mode.menu_switch", text="模式切换4", icon='RESTRICT_SELECT_OFF')
            col2.operator("mode.menu_switch", text="模式切换5", icon='RESTRICT_VIEW_OFF')
            col2.operator("mode.menu_switch", text="模式切换6", icon='HIDE_OFF')

        if prefs.panel_one_col3_title and prefs.panel_one_col3_title.strip():
            col3.label(text=prefs.panel_one_col3_title, icon='MENU_PANEL')
            col3.separator()
            # 第三列菜单项
            col3.operator("mode.menu_switch", text="模式切换7", icon='MODIFIER_DATA')
            col3.operator("mode.menu_switch", text="模式切换8", icon='MODIFIER_ON')
            col3.operator("mode.menu_switch", text="模式切换9", icon='MODIFIER_OFF')

# 需要另外写一个 call.popup_menu_one 函数来调用这个类函数
