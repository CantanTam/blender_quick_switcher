import bpy
from ..show_switch_notice import show_notice

class BUTTON_ACTION_OT_switch_snap_menu(bpy.types.Operator):
    bl_idname = "button.action_switch_snap_menu"
    bl_label = "吸附"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.ops.wm.call_panel(name="VIEW3D_PT_snapping")
        return {'FINISHED'}

class BUTTON_ACTION_OT_switch_snap_toggle(bpy.types.Operator):
    bl_idname = "button.action_switch_snap_toggle"
    bl_label = "开/关吸附"
    bl_description = "快捷键 Shift Tab"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.context.scene.tool_settings.use_snap = not bpy.context.scene.tool_settings.use_snap
        if bpy.context.scene.tool_settings.use_snap == True:
            show_notice("SNAP_ON.png")
        else:
            show_notice("SNAP_OFF.png")
        return {'FINISHED'}

class BUTTON_ACTION_OT_switch_snap_increment(bpy.types.Operator):
    bl_idname = "button.action_switch_snap_increment"
    bl_label = ""
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.context.scene.tool_settings.snap_elements = {'INCREMENT'}
        return {'FINISHED'}

class BUTTON_ACTION_OT_switch_snap_vertex(bpy.types.Operator):
    bl_idname = "button.action_switch_snap_vertex"
    bl_label = ""
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.context.scene.tool_settings.snap_elements = {'VERTEX'}
        return {'FINISHED'}

class BUTTON_ACTION_OT_switch_snap_edge(bpy.types.Operator):
    bl_idname = "button.action_switch_snap_edge"
    bl_label = ""
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.context.scene.tool_settings.snap_elements = {'EDGE'}
        return {'FINISHED'}

class BUTTON_ACTION_OT_switch_snap_face(bpy.types.Operator):
    bl_idname = "button.action_switch_snap_face"
    bl_label = ""
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.context.scene.tool_settings.snap_elements = {'FACE'}
        return {'FINISHED'}

class BUTTON_ACTION_OT_switch_snap_face_nearest(bpy.types.Operator):
    bl_idname = "button.action_switch_snap_face_nearest"
    bl_label = ""
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.context.scene.tool_settings.snap_elements = {'FACE_NEAREST'}
        return {'FINISHED'}

class BUTTON_ACTION_OT_switch_snap_volume(bpy.types.Operator):
    bl_idname = "button.action_switch_snap_volume"
    bl_label = ""
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.context.scene.tool_settings.snap_elements = {'VOLUME'}
        return {'FINISHED'}
    
class BUTTON_ACTION_OT_switch_snap_edge_midpoint(bpy.types.Operator):
    bl_idname = "button.action_switch_snap_edge_midpoint"
    bl_label = ""
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.context.scene.tool_settings.snap_elements = {'EDGE_MIDPOINT'}
        return {'FINISHED'}

class BUTTON_ACTION_OT_switch_snap_edge_perpendicular(bpy.types.Operator):
    bl_idname = "button.action_switch_snap_edge_perpendicular"
    bl_label = ""
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.context.scene.tool_settings.snap_elements = {'EDGE_PERPENDICULAR'}
        return {'FINISHED'}

classes = (
    BUTTON_ACTION_OT_switch_snap_menu,
    BUTTON_ACTION_OT_switch_snap_toggle,
    BUTTON_ACTION_OT_switch_snap_increment,
    BUTTON_ACTION_OT_switch_snap_vertex,
    BUTTON_ACTION_OT_switch_snap_edge,
    BUTTON_ACTION_OT_switch_snap_face,
    BUTTON_ACTION_OT_switch_snap_face_nearest,
    BUTTON_ACTION_OT_switch_snap_volume,
    BUTTON_ACTION_OT_switch_snap_edge_midpoint,
    BUTTON_ACTION_OT_switch_snap_edge_perpendicular,
)

def register():
    for cls in classes:
        bpy.utils.register_class(cls)

def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)
