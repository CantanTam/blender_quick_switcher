# npanel.py
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

        if prefs.ctrl_wheel_up_on_panel:
            row = layout.row()
            row.split(factor=0.3, align=True)
            row.label(text="Ctrl+鼠标上滚")
            row.prop(prefs, "ctrl_wheel_up", text="")

        row = layout.row()
        row.split(factor=0.3, align=True)
        row.label(text="Ctr+鼠标下滚")
        row.prop(prefs, "ctrl_wheel_down", text="")

# 集中管理此模块要注册的类
classes = (
    QUICKPOPUP_PT_NPanel,
)

def register():
    """Blender 启用插件时自动调用"""
    for cls in classes:
        bpy.utils.register_class(cls)

def unregister():
    """Blender 禁用插件时自动调用"""
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)
