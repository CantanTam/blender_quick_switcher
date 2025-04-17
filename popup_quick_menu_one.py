import bpy

class QUICK_POPUP_MENU_OT_one(bpy.types.Operator):
    bl_idname = "popup.quick_menu_one"
    bl_label = "两列菜单"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        return {'FINISHED'}

    def invoke(self, context, event):
        # 使用invoke_popup正确方式
        return context.window_manager.invoke_popup(self, width=300)

    def draw(self, context):
        layout = self.layout

        # 创建两列布局
        row = layout.row()
        col1 = row.column(align=True)
        col2 = row.column(align=True)

        # 第一列标题和分隔符
        col1.label(text="工具列1", icon='TOOL_SETTINGS')
        col1.separator()
        # 第一列菜单项
        col1.operator("mode.menu_switch", text="模式切换1", icon='OBJECT_DATA')
        col1.operator("mode.menu_switch", text="模式切换2", icon='EDITMODE_HLT')
        col1.operator("mode.menu_switch", text="模式切换3", icon='MODIFIER')

        # 第二列标题和分隔符
        col2.label(text="工具列2", icon='PREFERENCES')
        col2.separator()
        # 第二列菜单项
        col2.operator("mode.menu_switch", text="模式切换4", icon='RESTRICT_SELECT_OFF')
        col2.operator("mode.menu_switch", text="模式切换5", icon='RESTRICT_VIEW_OFF')
        col2.operator("mode.menu_switch", text="模式切换6", icon='HIDE_OFF')

# 需要另外写一个 call.popup_menu_one 函数来调用这个类函数
