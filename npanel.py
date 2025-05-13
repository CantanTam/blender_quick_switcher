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

        # 在这里统一设置：
        layout.use_property_split = True     # 开启“属性名/控件”拆分
        #layout.prop_split        = 0.7      # 左侧占 70%，右侧占 30%
        layout.use_property_decorate = False

        # 更新按钮box框
        box = layout.box()
        box.operator("quickpopup.update_enum", icon='PRESET')

        factor_value = 0.5
        
        if prefs.ctrl_wheel_up_on_panel:
            layout.row().prop(prefs, "ctrl_wheel_up", text="Ctrl+鼠标上滚",)

        if prefs.ctrl_wheel_down_on_panel:
            layout.row().prop(prefs, "ctrl_wheel_down", text="Ctrl+鼠标下滚")

        if prefs.ctrl_alt_wheel_up_on_panel:
            layout.row().prop(prefs, "ctrl_alt_wheel_up", text="Ctrl+Alt+鼠标上滚")

        if prefs.ctrl_alt_wheel_down_on_panel:
            layout.row().prop(prefs, "ctrl_alt_wheel_down", text="Ctrl+Alt+鼠标下滚")

        if prefs.shift_wheel_up_on_panel:
            layout.row().prop(prefs, "shift_wheel_up", text="Shift+鼠标上滚")

        if prefs.shift_wheel_down_on_panel:
            layout.row().prop(prefs, "shift_wheel_down", text="Shift+鼠标下滚")

        if prefs.ctrl_shift_wheel_up_on_panel:
            layout.row().prop(prefs, "ctrl_shift_wheel_up", text="Ctrl+Shift+鼠标上滚")

        if prefs.ctrl_shift_wheel_down_on_panel:
            layout.row().prop(prefs, "ctrl_shift_wheel_down", text="Ctrl+Shift+鼠标下滚")

        if prefs.shift_alt_wheel_up_on_panel:
            layout.row().prop(prefs, "shift_alt_wheel_up", text="Shift+Alt+鼠标上滚")

        if prefs.shift_alt_wheel_down_on_panel:
            layout.row().prop(prefs, "shift_alt_wheel_down", text="Shift+Alt+鼠标下滚")

        if prefs.alt_mouse_right_on_panel:
            layout.row().prop(prefs, "alt_mouse_right", text="Alt+鼠标右键")

        if prefs.ctrl_alt_mouse_right_on_panel:
            layout.row().prop(prefs, "ctrl_alt_mouse_right", text="Ctrl+Alt+鼠标右键")

        if prefs.shift_alt_mouse_right_on_panel:
            layout.row().prop(prefs, "shift_alt_mouse_right", text="Shift+Alt+鼠标右键")

        if prefs.ctrl_shift_alt_mouse_right_on_panel:
            layout.row().prop(prefs, "ctrl_shift_alt_mouse_right", text="Ctrl+Shift+Alt+鼠标右键")

class QUICKPOPUP_OT_UpdateEnum(bpy.types.Operator):
    bl_idname = "quickpopup.update_enum"
    bl_label = "更新下拉菜单"
    bl_description = "手动刷新快捷键下拉菜单的枚举项"

    def execute(self, context):
        prefs = context.preferences.addons[__package__].preferences
        update_enum_items(prefs, context)
        self.report({'INFO'}, "已刷新快捷键下拉菜单")
        return {'FINISHED'}

def register():
    bpy.utils.register_class(QUICKPOPUP_PT_NPanel)
    bpy.utils.register_class(QUICKPOPUP_OT_UpdateEnum)

def unregister():
    bpy.utils.unregister_class(QUICKPOPUP_PT_NPanel)
    bpy.utils.unregister_class(QUICKPOPUP_OT_UpdateEnum)
