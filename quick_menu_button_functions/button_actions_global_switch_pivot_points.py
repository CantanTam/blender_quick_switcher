import bpy

class BUTTON_ACTION_OT_pivot_to_bounding_box_center(bpy.types.Operator):
    bl_idname = "button.action_pivot_to_bounding_box_center"
    bl_label = "边界框中心"
    bl_description = "边界框中心"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.context.scene.tool_settings.transform_pivot_point = 'BOUNDING_BOX_CENTER'
        return {'FINISHED'}

class BUTTON_ACTION_OT_pivot_to_cursor(bpy.types.Operator):
    bl_idname = "button.action_pivot_to_cursor"
    bl_label = "3D 游标"
    bl_description = "3D 游标"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.context.scene.tool_settings.transform_pivot_point = 'CURSOR'
        return {'FINISHED'}

class BUTTON_ACTION_OT_pivot_to_individual_origins(bpy.types.Operator):
    bl_idname = "button.action_pivot_to_individual_origins"
    bl_label = "各自的原点"
    bl_description = "各自的原点"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.context.scene.tool_settings.transform_pivot_point = 'INDIVIDUAL_ORIGINS'
        return {'FINISHED'}

class BUTTON_ACTION_OT_pivot_to_median_point(bpy.types.Operator):
    bl_idname = "button.action_pivot_to_median_point"
    bl_label = "质心点"
    bl_description = "质心点"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.context.scene.tool_settings.transform_pivot_point = 'MEDIAN_POINT'
        return {'FINISHED'}

class BUTTON_ACTION_OT_pivot_to_active_element(bpy.types.Operator):
    bl_idname = "button.action_pivot_to_active_element"
    bl_label = "活动元素"
    bl_description = "活动元素"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.context.scene.tool_settings.transform_pivot_point = 'ACTIVE_ELEMENT'
        return {'FINISHED'}
