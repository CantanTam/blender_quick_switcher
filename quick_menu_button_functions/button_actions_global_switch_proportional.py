import bpy
from ..show_switch_notice import show_notice

class ACTION_OT_switch_proportional_menu(bpy.types.Operator):
    bl_idname = "action.switch_proportional_menu"
    bl_label = "衰减编辑(菜单)"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.ops.wm.call_panel(name="VIEW3D_PT_proportional_edit")
        return {'FINISHED'}

class ACTION_OT_switch_proportional_toggle(bpy.types.Operator):
    bl_idname = "action.switch_proportional_toggle"
    bl_label = "开/关衰减编辑"
    bl_description = "快捷键 O"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        if bpy.context.active_object.mode == "OBJECT":
            bpy.context.scene.tool_settings.use_proportional_edit_objects = not bpy.context.scene.tool_settings.use_proportional_edit_objects
            if bpy.context.scene.tool_settings.use_proportional_edit_objects == True:
                show_notice("PROPORTIONAL_ON.png")
            else:
                show_notice("PROPORTIONAL_OFF.png")
        else:
            bpy.context.scene.tool_settings.use_proportional_edit = not bpy.context.scene.tool_settings.use_proportional_edit
            if bpy.context.scene.tool_settings.use_proportional_edit == True:
                show_notice("PROPORTIONAL_ON.png")
            else:
                show_notice("PROPORTIONAL_OFF.png")
        return {'FINISHED'}

class ACTION_OT_switch_proportional_smooth(bpy.types.Operator):
    bl_idname = "action.switch_proportional_smooth"
    bl_label = ""
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.context.scene.tool_settings.proportional_edit_falloff = 'SMOOTH'
        return {'FINISHED'}

class ACTION_OT_switch_proportional_sphere(bpy.types.Operator):
    bl_idname = "action.switch_proportional_sphere"
    bl_label = ""
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.context.scene.tool_settings.proportional_edit_falloff = 'SPHERE'
        return {'FINISHED'}

class ACTION_OT_switch_proportional_root(bpy.types.Operator):
    bl_idname = "action.switch_proportional_root"
    bl_label = ""
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.context.scene.tool_settings.proportional_edit_falloff = 'ROOT'
        return {'FINISHED'}

class ACTION_OT_switch_proportional_inverse_square(bpy.types.Operator):
    bl_idname = "action.switch_proportional_inverse_square"
    bl_label = ""
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.context.scene.tool_settings.proportional_edit_falloff = 'INVERSE_SQUARE'
        return {'FINISHED'}

class ACTION_OT_switch_proportional_sharp(bpy.types.Operator):
    bl_idname = "action.switch_proportional_sharp"
    bl_label = ""
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.context.scene.tool_settings.proportional_edit_falloff = 'SHARP'
        return {'FINISHED'}

class ACTION_OT_switch_proportional_linear(bpy.types.Operator):
    bl_idname = "action.switch_proportional_linear"
    bl_label = ""
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.context.scene.tool_settings.proportional_edit_falloff = 'LINEAR'
        return {'FINISHED'}

class ACTION_OT_switch_proportional_constant(bpy.types.Operator):
    bl_idname = "action.switch_proportional_constant"
    bl_label = ""
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.context.scene.tool_settings.proportional_edit_falloff = 'CONSTANT'
        return {'FINISHED'}

class ACTION_OT_switch_proportional_random(bpy.types.Operator):
    bl_idname = "action.switch_proportional_random"
    bl_label = ""
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.context.scene.tool_settings.proportional_edit_falloff = 'RANDOM'
        return {'FINISHED'}

classes = (
    ACTION_OT_switch_proportional_menu,
    ACTION_OT_switch_proportional_toggle,
    ACTION_OT_switch_proportional_smooth,
    ACTION_OT_switch_proportional_sphere,
    ACTION_OT_switch_proportional_root,
    ACTION_OT_switch_proportional_inverse_square,
    ACTION_OT_switch_proportional_sharp,
    ACTION_OT_switch_proportional_linear,
    ACTION_OT_switch_proportional_constant,
    ACTION_OT_switch_proportional_random,
)

def register():
    for cls in classes:
        bpy.utils.register_class(cls)

def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)
