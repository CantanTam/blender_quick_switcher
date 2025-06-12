import bpy



# 套索选择——开始(备份用)
class ACTION_OT_global_select_lasso_set(bpy.types.Operator):
    bl_idname = "action.global_select_lasso_set"
    bl_label = "开始"
    bl_options = {'REGISTER', 'UNDO'}

    waiting_for_click: bpy.props.BoolProperty(default=False, options={'HIDDEN'})

    def invoke(self, context, event):
        if not self.waiting_for_click:
            self.waiting_for_click = True
            context.window_manager.modal_handler_add(self)
            return {'RUNNING_MODAL'}
        return self.execute(context)

    def modal(self, context, event):
        if event.type == 'LEFTMOUSE' and event.value == 'PRESS':
            return self.execute(context)
        return {'PASS_THROUGH'}

    def execute(self, context):
        typeandmode = bpy.context.active_object.type+bpy.context.active_object.mode

        if typeandmode == 'GPENCILEDIT_GPENCIL':
            bpy.ops.gpencil.select_lasso('INVOKE_DEFAULT', mode='SET')
        else:
            bpy.ops.view3d.select_lasso('INVOKE_DEFAULT', mode='SET')
        self.waiting_for_click = False
        return {'FINISHED'}










#网格编辑模式的选择选项





classes = (
    ACTION_OT_global_select_lasso_set,   #备份用，可以删除

)

def register():
    for cls in classes:
        bpy.utils.register_class(cls)

def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)