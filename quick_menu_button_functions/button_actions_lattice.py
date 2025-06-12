import bpy

class VIEW3D_MT_latticeedit_flip_menu(bpy.types.Operator):
    bl_label = ""
    bl_idname = "popup.latticeedit_flip_menu"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        return {'FINISHED'}

    def invoke(self, context, event):
        return context.window_manager.invoke_popup(self, width=80)

    def draw(self, context):
        layout = self.layout
        col = layout.column(align=True)
        col.label(text="反转(免畸变)")
        col.operator("lattice.flip", text="U(X)轴", icon="RADIOBUT_OFF").axis='U'
        col.operator("lattice.flip", text="V(Y)轴", icon="RADIOBUT_OFF").axis='V'
        col.operator("lattice.flip", text="W(Z)轴", icon="RADIOBUT_OFF").axis='W'

class ACTION_OT_call_latticeedit_flip_menu(bpy.types.Operator):
    bl_idname = "action.call_latticeedit_flip_menu"
    bl_label = "反转(免畸变)"
    bl_description = "快捷键 Alt F"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.ops.popup.latticeedit_flip_menu('INVOKE_DEFAULT')
        return {'FINISHED'}

class ACTION_OT_call_latticeedit_make_regular(bpy.types.Operator):
    bl_idname = "action.latticeedit_make_regular"
    bl_label = "均匀分布"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.ops.lattice.make_regular()
        return {'FINISHED'}


classes = (
    VIEW3D_MT_latticeedit_flip_menu,
    ACTION_OT_call_latticeedit_flip_menu,
    ACTION_OT_call_latticeedit_make_regular,

)    

def register():
    for cls in classes:
        bpy.utils.register_class(cls)

def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)