import bpy

from .operator_mode_switch_menu_downtoup import MODE_MENU_OT_Switch

# 模拟原生 tab 切换编辑模式
class MODE_TAB_OT_Switch(bpy.types.Operator):
    bl_idname = "mode.tab_switch"
    bl_label = "tab模式切换编辑模式"
    bl_options = {"REGISTER",'UNDO'}

    def execute(self, context):
        # 为保证 4.2 版本与 4.3 版本同时可用，利用 bpy.context.active_object.type+bpy.context.mode，生成唯一键的字典，然后再调用 值 作为切换模式
        type_mode_maps = {
            'MESHOBJECT': 'OBJECT',
            'MESHEDIT_MESH': 'EDIT',
            'MESHSCULPT': 'SCULPT',
            'MESHPAINT_VERTEX': 'VERTEX_PAINT',
            'MESHPAINT_WEIGHT': 'WEIGHT_PAINT',
            'MESHPAINT_TEXTURE': 'TEXTURE_PAINT',
            'MESHEDIT': 'EDIT',
            'MESHVERTEX_PAINT': 'VERTEX_PAINT',
            'MESHWEIGHT_PAINT': 'WEIGHT_PAINT',
            'MESHTEXTURE_PAINT': 'TEXTURE_PAINT',
            'GPENCILOBJECT': 'OBJECT',
            'GPENCILEDIT_GPENCIL': 'EDIT_GPENCIL',
            'GPENCILSCULPT_GPENCIL': 'SCULPT_GPENCIL',
            'GPENCILPAINT_GPENCIL': 'PAINT_GPENCIL',
            'GPENCILWEIGHT_GPENCIL': 'WEIGHT_GPENCIL',
            'GPENCILVERTEX_GPENCIL': 'VERTEX_GPENCIL',
            'GREASEPENCILOBJECT': 'OBJECT',
            'GREASEPENCILEDIT_GREASE_PENCIL': 'EDIT',
            'GREASEPENCILSCULPT_GREASE_PENCIL': 'SCULPT_GREASE_PENCIL',
            'GREASEPENCILPAINT_GREASE_PENCIL': 'PAINT_GREASE_PENCIL',
            'GREASEPENCILWEIGHT_GREASE_PENCIL': 'WEIGHT_GREASE_PENCIL',
            'GREASEPENCILVERTEX_GREASE_PENCIL': 'VERTEX_GREASE_PENCIL',
            'ARMATUREOBJECT': 'OBJECT',
            'ARMATUREEDIT_ARMATURE': 'EDIT',
            'ARMATUREPOSE': 'POSE'
        }

        if not bpy.context.active_object:
            return {'CANCELLED'}
        
        else:
            if bpy.context.active_object.type in {'CURVE','SURFACE','META','FONT'}:
                bpy.ops.object.editmode_toggle()

            elif bpy.context.active_object.type+bpy.context.mode in type_mode_maps:
                bpy.ops.mode.menu_switch()

            else:
                return {'CANCELLED'}

        return {'FINISHED'}

