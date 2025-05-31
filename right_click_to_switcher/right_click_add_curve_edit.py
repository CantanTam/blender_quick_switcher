import bpy
from .. import ADDON_NAME



def curveedit_transform_mode_curve_shrinkfatten_to_switcher(self, context):
    show_switcher = bpy.context.preferences.addons[ADDON_NAME].preferences.to_show_to_switcher
    if not show_switcher or bpy.context.mode not in {"EDIT_CURVE","EDIT_GREASE_PENCIL"}:
        return
    self.layout.separator()
    self.layout.operator("call.add_to_switcher_menu", text="\"半径\"添加到Switcher", icon='PLUS').action = 'button.action_transform_transform_mode_curve_shrinkfatten'






def register():
    bpy.types.VIEW3D_MT_transform.append(curveedit_transform_mode_curve_shrinkfatten_to_switcher)

def unregister():
    bpy.types.VIEW3D_MT_transform.remove(curveedit_transform_mode_curve_shrinkfatten_to_switcher)
