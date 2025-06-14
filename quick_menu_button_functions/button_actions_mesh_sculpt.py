import bpy
from ..show_switch_notice import show_notice


class ACTION_OT_meshsculpt_mesh_filter_sphere(bpy.types.Operator):
    bl_idname = "action.meshsculpt_mesh_filter_sphere"
    bl_label = "球形化"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        #current_mode_idname = bpy.context.workspace.tools.from_space_view3d_mode(mode='SCULPT', create=True).idname
        #bpy.context.workspace.tools.from_space_view3d_mode(mode='SCULPT', create=True).idname = "builtin.mesh_filter"
        bpy.ops.sculpt.mesh_filter('INVOKE_DEFAULT', type='SPHERE')
        #bpy.context.workspace.tools.from_space_view3d_mode(mode='SCULPT', create=True).idname = current_mode_idname
        return {'FINISHED'}

class ACTION_OT_meshsculpt_paint_hide_show_hide(bpy.types.Operator):
    bl_idname = "action.meshsculpt_paint_hide_show_hide"
    bl_label = "框选隐藏"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.ops.paint.hide_show('INVOKE_DEFAULT',action='HIDE')
        return {'FINISHED'}

class ACTION_OT_meshsculpt_paint_hide_show_show(bpy.types.Operator):
    bl_idname = "action.meshsculpt_paint_hide_show_show"
    bl_label = "框选显示"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.ops.paint.hide_show('INVOKE_DEFAULT',action='SHOW')
        return {'FINISHED'}

class ACTION_OT_meshsculpt_paint_hide_show_all(bpy.types.Operator):
    bl_idname = "action.meshsculpt_paint_hide_show_all"
    bl_label = "显示全部"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.ops.paint.hide_show('INVOKE_DEFAULT',action='SHOW', area='ALL') # 4.2版本
        return {'FINISHED'}

class ACTION_OT_meshsculpt_face_set_change_visibility_toggle(bpy.types.Operator):
    bl_idname = "action.meshsculpt_face_set_change_visibility_toggle"
    bl_label = "切换可见性"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        return {'FINISHED'}

    def invoke(self, context, event):
        return context.window_manager.invoke_popup(self, width=80)

    def draw(self, context):
        layout = self.layout
        layout.operator("sculpt.face_set_change_visibility", text="切换可见性", icon="RADIOBUT_OFF").mode='TOGGLE'

class ACTION_OT_meshsculpt_face_set_change_visibility_toggle_modal(bpy.types.Operator):
    bl_idname = "action.meshsculpt_face_set_change_visibility_toggle_modal"
    bl_label = "切换可见性"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        show_notice("LEFT_CLICK.png")
        bpy.ops.action.meshsculpt_face_set_change_visibility_toggle('INVOKE_DEFAULT')
        return {'FINISHED'}

class ACTION_OT_meshsculpt_face_set_change_visibility_hide(bpy.types.Operator):
    bl_idname = "action.meshsculpt_face_set_change_visibility_hide"
    bl_label = "隐藏活动面组"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        return {'FINISHED'}

    def invoke(self, context, event):
        return context.window_manager.invoke_popup(self, width=100)

    def draw(self, context):
        layout = self.layout
        layout.operator("sculpt.face_set_change_visibility", text="隐藏活动面组", icon="RADIOBUT_OFF").mode='HIDE_ACTIVE'

class ACTION_OT_meshsculpt_face_set_change_visibility_hide_modal(bpy.types.Operator):
    bl_idname = "action.meshsculpt_face_set_change_visibility_hide_modal"
    bl_label = "隐藏活动面组"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        show_notice("LEFT_CLICK.png")
        bpy.ops.action.meshsculpt_face_set_change_visibility_hide('INVOKE_DEFAULT')
        return {'FINISHED'}

class ACTION_OT_meshsculpt_face_set_invert_visibility(bpy.types.Operator):
    bl_idname = "action.meshsculpt_face_set_invert_visibility"
    bl_label = "反转可见"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.ops.sculpt.face_set_invert_visibility()
        return {'FINISHED'}

class ACTION_OT_meshsculpt_paint_hide_show_hide_masked(bpy.types.Operator):
    bl_idname = "action.meshsculpt_paint_hide_show_hide_masked"
    bl_label = "隐藏遮罩作用项"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.ops.paint.hide_show(action='HIDE', area='MASKED')
        return {'FINISHED'}

class ACTION_OT_meshsculpt_trim_box_gesture_difference(bpy.types.Operator):
    bl_idname = "action.meshsculpt_trim_box_gesture_difference"
    bl_label = "框选修剪"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.ops.sculpt.trim_box_gesture('INVOKE_DEFAULT', trim_mode='DIFFERENCE')
        return {'FINISHED'}

class ACTION_OT_meshsculpt_trim_box_gesture_join(bpy.types.Operator):
    bl_idname = "action.meshsculpt_trim_box_gesture_join"
    bl_label = "框选添加"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.ops.sculpt.trim_box_gesture('INVOKE_DEFAULT', trim_mode='JOIN')
        return {'FINISHED'}
    
class ACTION_OT_meshsculpt_trim_lasso_gesture_difference(bpy.types.Operator):
    bl_idname = "action.meshsculpt_trim_lasso_gesture_difference"
    bl_label = "套索修剪"
    bl_options = {'REGISTER', 'UNDO'}

    def modal(self, context, event):
        if event.type == 'LEFTMOUSE' and event.value == 'PRESS':
            bpy.ops.sculpt.trim_lasso_gesture('INVOKE_DEFAULT', trim_mode='DIFFERENCE')
            return {'FINISHED'}
        
        elif event.type in {'ESC','RIGHTMOUSE'}:
            return {'CANCELLED'}

        return {'RUNNING_MODAL'}

    def invoke(self, context, event):
        context.window_manager.modal_handler_add(self)
        return {'RUNNING_MODAL'}

class ACTION_OT_meshsculpt_trim_lasso_gesture_difference_modal(bpy.types.Operator):
    bl_idname = "action.meshsculpt_trim_lasso_gesture_difference_modal"
    bl_label = "套索修剪"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        show_notice("LEFT_CLICK.png")
        bpy.ops.action.meshsculpt_trim_lasso_gesture_difference('INVOKE_DEFAULT')
        return {'FINISHED'}

class ACTION_OT_meshsculpt_trim_lasso_gesture_join(bpy.types.Operator):
    bl_idname = "action.meshsculpt_trim_lasso_gesture_join"
    bl_label = "套索添加"
    bl_options = {'REGISTER', 'UNDO'}

    def modal(self, context, event):
        if event.type == 'LEFTMOUSE' and event.value == 'PRESS':
            bpy.ops.sculpt.trim_lasso_gesture('INVOKE_DEFAULT', trim_mode='JOIN')
            return {'FINISHED'}
        
        elif event.type in {'ESC','RIGHTMOUSE'}:
            return {'CANCELLED'}

        return {'RUNNING_MODAL'}

    def invoke(self, context, event):
        context.window_manager.modal_handler_add(self)
        return {'RUNNING_MODAL'}

class ACTION_OT_meshsculpt_trim_lasso_gesture_join_modal(bpy.types.Operator):
    bl_idname = "action.meshsculpt_trim_lasso_gesture_join_modal"
    bl_label = "套索添加"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        show_notice("LEFT_CLICK.png")
        bpy.ops.action.meshsculpt_trim_lasso_gesture_join('INVOKE_DEFAULT')
        return {'FINISHED'}

class ACTION_OT_meshsculpt_project_line_gesture(bpy.types.Operator):
    bl_idname = "action.meshsculpt_project_line_gesture"
    bl_label = "划线投影"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        show_notice("LEFT_CLICK.png")
        bpy.ops.sculpt.project_line_gesture('INVOKE_DEFAULT')
        return {'FINISHED'}








class ACTION_OT_meshsculpt_face_set_edit_position(bpy.types.Operator):
    bl_idname = "action.meshsculpt_face_set_edit_position"
    bl_label = "平顺位置"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        return {'FINISHED'}

    def invoke(self, context, event):
        return context.window_manager.invoke_popup(self, width=80)

    def draw(self, context):
        layout = self.layout
        layout.operator("sculpt.face_set_edit", text="平顺位置", icon="RADIOBUT_OFF").mode='FAIR_POSITIONS'

class ACTION_OT_meshsculpt_face_set_edit_position_modal(bpy.types.Operator):
    bl_idname = "action.meshsculpt_face_set_edit_position_modal"
    bl_label = "平顺位置"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        show_notice("LEFT_CLICK.png")
        bpy.ops.action.meshsculpt_face_set_edit_position('INVOKE_DEFAULT')
        return {'FINISHED'}
    






classes = (
    ACTION_OT_meshsculpt_mesh_filter_sphere,
    ACTION_OT_meshsculpt_paint_hide_show_hide,
    ACTION_OT_meshsculpt_paint_hide_show_show,
    ACTION_OT_meshsculpt_paint_hide_show_all,
    ACTION_OT_meshsculpt_face_set_change_visibility_toggle,
    ACTION_OT_meshsculpt_face_set_change_visibility_toggle_modal,
    ACTION_OT_meshsculpt_face_set_change_visibility_hide,
    ACTION_OT_meshsculpt_face_set_change_visibility_hide_modal,
    ACTION_OT_meshsculpt_face_set_invert_visibility,
    ACTION_OT_meshsculpt_paint_hide_show_hide_masked,
    ACTION_OT_meshsculpt_trim_box_gesture_difference,
    ACTION_OT_meshsculpt_trim_box_gesture_join,
    ACTION_OT_meshsculpt_trim_lasso_gesture_difference,
    ACTION_OT_meshsculpt_trim_lasso_gesture_difference_modal,
    ACTION_OT_meshsculpt_trim_lasso_gesture_join,
    ACTION_OT_meshsculpt_trim_lasso_gesture_join_modal,
    ACTION_OT_meshsculpt_project_line_gesture,
    ACTION_OT_meshsculpt_face_set_edit_position,
    ACTION_OT_meshsculpt_face_set_edit_position_modal,

)

def register():
    for cls in classes:
        bpy.utils.register_class(cls)

def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)