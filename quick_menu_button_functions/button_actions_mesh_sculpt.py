import bpy

class ACTION_OT_meshsculpt_mesh_filter_sphere(bpy.types.Operator):
    bl_idname = "action.meshsculpt_mesh_filter_sphere"
    bl_label = "球形化"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        current_mode_idname = bpy.context.workspace.tools.from_space_view3d_mode(mode='SCULPT', create=True).idname
        bpy.context.workspace.tools.from_space_view3d_mode(mode='SCULPT', create=True).idname = "builtin.mesh_filter"
        bpy.ops.sculpt.mesh_filter('INVOKE_DEFAULT', type='SPHERE')
        bpy.context.workspace.tools.from_space_view3d_mode(mode='SCULPT', create=True).idname = current_mode_idname
        return {'FINISHED'}







classes = (
    ACTION_OT_meshsculpt_mesh_filter_sphere,

)

def register():
    for cls in classes:
        bpy.utils.register_class(cls)

def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)