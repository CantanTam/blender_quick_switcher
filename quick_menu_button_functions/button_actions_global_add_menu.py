import bpy
# 添加
class BUTTON_ACTION_OT_add(bpy.types.Operator):
    bl_idname = "button.action_add"
    bl_label = "添加"
    bl_description = "快捷键 Shift A"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        typeandmode = bpy.context.active_object.type+bpy.context.active_object.mode

        if bpy.context.mode == 'OBJECT':
            bpy.ops.wm.call_menu(name="VIEW3D_MT_add")
        if typeandmode == "CURVEEDIT":
            bpy.ops.wm.call_menu(name="VIEW3D_MT_curve_add")
        if typeandmode == 'SURFACEEDIT':
            bpy.ops.wm.call_menu(name="VIEW3D_MT_surface_add")
        if typeandmode == 'METAEDIT':
            bpy.ops.wm.call_menu(name="VIEW3D_MT_metaball_add")
        if typeandmode == 'MESHEDIT':
            bpy.ops.wm.call_menu(name="VIEW3D_MT_mesh_add")
        if typeandmode == 'ARMATUREEDIT':
            bpy.ops.armature.bone_primitive_add(name='Bone')
        return {'FINISHED'}
    
