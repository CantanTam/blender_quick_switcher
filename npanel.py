import bpy
from .preference import update_enum_items

# 你的面板类
class QUICKPOPUP_PT_NPanel(bpy.types.Panel):
    bl_label = "极速菜单快捷键"
    bl_idname = "QUICKPOPUP_PT_npanel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "QuickPopup"

    @classmethod
    def poll(cls, context):
        prefs = context.preferences.addons[__package__].preferences
        return prefs.to_use_npanel

    def draw(self, context):
        prefs = context.preferences.addons[__package__].preferences
        layout = self.layout

        # 更新按钮box框
        box = layout.box()
        box.operator("quickpopup.update_enum", icon='PRESET')

        factor_value = 0.5
        
        if prefs.ctrl_wheel_up_on_panel:
            row = layout.row().split(factor=factor_value, align=True)
            row.label(text="Ctrl+鼠标上滚")
            row.prop(prefs, "ctrl_wheel_up", text="")

        if prefs.ctrl_wheel_down_on_panel:
            row = layout.row().split(factor=factor_value, align=True)
            row.label(text="Ctr+鼠标下滚")
            row.prop(prefs, "ctrl_wheel_down", text="")

        if prefs.ctrl_alt_wheel_up_on_panel:
            row = layout.row().split(factor=factor_value, align=True)
            row.label(text="Ctrl+Shift+鼠标上滚")
            row.prop(prefs, "ctrl_alt_wheel_up", text="")

        if prefs.ctrl_alt_wheel_down_on_panel:
            row = layout.row().split(factor=factor_value, align=True)
            row.label(text="Ctrl+Shift+鼠标下滚")
            row.prop(prefs, "ctrl_alt_wheel_down", text="")

        if prefs.shift_wheel_up_on_panel:
            row = layout.row().split(factor=factor_value, align=True)
            row.label(text="Shift+鼠标上滚")
            row.prop(prefs, "shift_wheel_up", text="")

        if prefs.shift_wheel_down_on_panel:
            row = layout.row().split(factor=factor_value, align=True)
            row.label(text="Shift+鼠标下滚")
            row.prop(prefs, "shift_wheel_down", text="")

        if prefs.ctrl_shift_wheel_up_on_panel:
            row = layout.row().split(factor=factor_value, align=True)
            row.label(text="Ctrl+Shift+鼠标上滚")
            row.prop(prefs, "ctrl_shift_wheel_up", text="")

        if prefs.ctrl_shift_wheel_down_on_panel:
            row = layout.row().split(factor=factor_value, align=True)
            row.label(text="Ctrl+Shift+鼠标下滚")
            row.prop(prefs, "ctrl_shift_wheel_down", text="")

        if prefs.shift_alt_wheel_up_on_panel:
            row = layout.row().split(factor=factor_value, align=True)
            row.label(text="Shift+Alt+鼠标上滚")
            row.prop(prefs, "shift_alt_wheel_up", text="")

        if prefs.shift_alt_wheel_down_on_panel:
            row = layout.row().split(factor=factor_value, align=True)
            row.label(text="Shift+Alt+鼠标下滚")
            row.prop(prefs, "shift_alt_wheel_down", text="")

        if prefs.alt_mouse_right_on_panel:
            row = layout.row().split(factor=factor_value, align=True)
            row.label(text="Alt+鼠标右键")
            row.prop(prefs, "alt_mouse_right", text="")

        if prefs.ctrl_alt_mouse_right_on_panel:
            row = layout.row().split(factor=factor_value, align=True)
            row.label(text="Ctrl+Alt+鼠标右键")
            row.prop(prefs, "ctrl_alt_mouse_right", text="")

        if prefs.shift_alt_mouse_right_on_panel:
            row = layout.row().split(factor=factor_value, align=True)
            row.label(text="Shift+Alt+鼠标右键")
            row.prop(prefs, "shift_alt_mouse_right", text="")

class QUICKPOPUP_OT_UpdateEnum(bpy.types.Operator):
    bl_idname = "quickpopup.update_enum"
    bl_label = "更新下拉菜单"
    bl_description = "手动刷新快捷键下拉菜单的枚举项"

    def execute(self, context):
        prefs = context.preferences.addons[__package__].preferences
        update_enum_items(prefs, context)
        self.report({'INFO'}, "已刷新快捷键下拉菜单")
        return {'FINISHED'}
