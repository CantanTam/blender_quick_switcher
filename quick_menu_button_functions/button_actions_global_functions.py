# 这里只包含使用快捷键的功能：
import bpy

# 全局“移动”功能
class BUTTON_ACTION_OT_grab(bpy.types.Operator):
    bl_idname = "button.action_global_grab"
    bl_label = "移动"
    bl_description = "快捷键 G"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.ops.transform.translate('INVOKE_DEFAULT')
        return {'FINISHED'}
    
# 全局“缩放”功能
class BUTTON_ACTION_OT_scale(bpy.types.Operator):
    bl_idname = "button.action_global_scale"
    bl_label = "缩放"
    bl_description = "快捷键 S"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.ops.transform.resize('INVOKE_DEFAULT')
        return {'FINISHED'}

# 全局“旋转”功能    
class BUTTON_ACTION_OT_rotate(bpy.types.Operator):
    bl_idname = "button.action_global_rotate"
    bl_label = "旋转(R)"
    bl_description = "快捷键 R"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.ops.transform.rotate('INVOKE_DEFAULT')
        return {'FINISHED'}
    
# 全局“全选”功能
class BUTTON_ACTION_OT_global_select_all(bpy.types.Operator):
    bl_idname = "button.action_global_select_all"
    bl_label = "全选"
    bl_description = "快捷键 A"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        typeandmode = bpy.context.active_object.type+bpy.context.active_object.mode

        if bpy.context.mode == 'OBJECT':
            bpy.ops.object.select_all(action='SELECT')
        elif typeandmode in {"CURVEEDIT", "SURFACEEDIT"}:
            bpy.ops.curve.select_all(action='SELECT')
        elif typeandmode == "METAEDIT":
            bpy.ops.mball.select_all(action='SELECT')
        elif typeandmode ==  "FONTEDIT":
            bpy.ops.font.select_all()
        elif typeandmode == "LATTICEEDIT":
            bpy.ops.lattice.select_all(action='SELECT')
        elif typeandmode == "MESHEDIT":
            bpy.ops.mesh.select_all(action='SELECT')
        elif typeandmode in {"GPENCILEDIT_GPENCIL","GPENCILVERTEX_GPENCIL"}:
            bpy.ops.gpencil.select_all(action='SELECT') # 4.2 版本
        elif typeandmode in { "GREASEPENCILEDIT","GREASEPENCILVERTEX_GREASE_PENCIL"}:
            bpy.ops.grease_pencil.select_all(action='SELECT') # 4.3 版本
        elif typeandmode == "ARMATUREEDIT":
            bpy.ops.armature.select_all(action='SELECT')
        elif typeandmode == "ARMATUREPOSE":
            bpy.ops.pose.select_all(action='SELECT')
        else:
            return {'CANCELLED'}
        return {'FINISHED'}
    
# 全局“反选”功能
class BUTTON_ACTION_OT_global_select_invert(bpy.types.Operator):
    bl_idname = "button.action_global_select_invert"
    bl_label = "反选"
    bl_description = "快捷键 Ctrl I"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        typeandmode = bpy.context.active_object.type+bpy.context.active_object.mode

        if bpy.context.mode == 'OBJECT':
            bpy.ops.object.select_all(action='INVERT')
        elif typeandmode in {"CURVEEDIT", "SURFACEEDIT"}:
            bpy.ops.curve.select_all(action='INVERT')
        elif typeandmode == "METAEDIT":
            bpy.ops.mball.select_all(action='INVERT')
        elif typeandmode ==  "FONTEDIT":
            bpy.ops.font.select_all()
        elif typeandmode == "LATTICEEDIT":
            bpy.ops.lattice.select_all(action='INVERT')
        elif typeandmode == "MESHEDIT":
            bpy.ops.mesh.select_all(action='INVERT')
        elif typeandmode in {"GPENCILEDIT_GPENCIL","GPENCILVERTEX_GPENCIL"}:
            bpy.ops.gpencil.select_all(action='INVERT') # 4.2 版本
        elif typeandmode in { "GREASEPENCILEDIT","GREASEPENCILVERTEX_GREASE_PENCIL"}:
            bpy.ops.grease_pencil.select_all(action='INVERT') # 4.3 版本
        elif typeandmode == "ARMATUREEDIT":
            bpy.ops.armature.select_all(action='INVERT')
        elif typeandmode == "ARMATUREPOSE":
            bpy.ops.pose.select_all(action='INVERT')
        else:
            return {'CANCELLED'}
        return {'FINISHED'}
    
# 全局“刷选”功能
class BUTTON_ACTION_OT_global_select_circle(bpy.types.Operator):
    bl_idname = "button.action_global_select_circle"
    bl_label = "刷选"
    bl_description = "快捷键 C"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        typeandmode = bpy.context.active_object.type+bpy.context.active_object.mode

        if bpy.context.mode == 'OBJECT':
            bpy.ops.view3d.select_circle('INVOKE_DEFAULT')
        elif typeandmode in {
            "CURVEEDIT", 
            "SURFACEEDIT",
            "METAEDIT",
            "LATTICEEDIT",
            "MESHEDIT",
            "GREASEPENCILEDIT",
            "ARMATUREEDIT",
            "ARMATUREPOSE",
            }:
            bpy.ops.view3d.select_circle('INVOKE_DEFAULT')
        elif typeandmode == "GPENCILEDIT_GPENCIL":
            bpy.ops.gpencil.select_circle('INVOKE_DEFAULT') # 4.2 版本
        else:
            return {'CANCELLED'}
        return {'FINISHED'}

# 全局“添加”菜单功能
class BUTTON_ACTION_OT_global_add(bpy.types.Operator):
    bl_idname = "button.action_global_add"
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
            bpy.ops.wm.call_menu(name="TOPBAR_MT_edit_armature_add")
        return {'FINISHED'}

# 全局“复制”按钮功能
class BUTTON_ACTION_OT_global_duplicate_move(bpy.types.Operator):
    bl_idname = "button.action_global_duplicate_move"
    bl_label = "复制"
    bl_description = "快捷键 Shift D"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        typeandmode = bpy.context.active_object.type+bpy.context.active_object.mode
        if bpy.context.mode == "OBJECT":
            bpy.ops.object.duplicate_move('INVOKE_DEFAULT')
        elif typeandmode in {"CURVEEDIT","SURFACEEDIT"}:
            bpy.ops.curve.duplicate_move('INVOKE_DEFAULT')
        elif typeandmode == "METAEDIT":
            bpy.ops.mball.duplicate_move('INVOKE_DEFAULT')
        elif typeandmode == "GPENCILEDIT_GPENCIL":
            bpy.ops.gpencil.duplicate_move('INVOKE_DEFAULT')
        elif typeandmode == "GREASEPENCILEDIT":
            bpy.ops.grease_pencil.duplicate_move('INVOKE_DEFAULT')
        elif typeandmode == "MESHEDIT":
            bpy.ops.mesh.duplicate_move('INVOKE_DEFAULT')
        elif typeandmode == "ARMATUREEDIT":
            bpy.ops.armature.duplicate_move('INVOKE_DEFAULT')
        return {'FINISHED'}
