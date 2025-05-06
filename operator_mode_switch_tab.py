import bpy

from .operator_mode_switch_menu_downtoup import MODE_MENU_OT_Switch
from .operator_typeandmode_name_mode import typeandmode_name # 导入字典用于比较 typeandmode 变化
from .show_switch_notice import show_notice

# 模拟原生 tab 切换编辑模式
class MODE_TAB_OT_Switch(bpy.types.Operator):
    bl_idname = "mode.tab_switch"
    bl_label = "tab模式切换编辑模式"
    bl_description = "在最近的两种编辑模式之间进行切换"
    bl_options = {"REGISTER",'UNDO'}

    def execute(self, context):
        # 为保证 4.2 版本与 4.3 版本同时可用，利用 bpy.context.active_object.type+bpy.active_object.mode，生成唯一键的字典，然后再调用 值 作为切换模式
        type_mode_maps = {
            # Mesh 类型（两个版本保持一致）
            'MESHOBJECT': 'OBJECT',
            'MESHEDIT': 'EDIT',
            'MESHSCULPT': 'SCULPT',
            'MESHVERTEX_PAINT': 'VERTEX_PAINT',
            'MESHWEIGHT_PAINT': 'WEIGHT_PAINT',
            'MESHTEXTURE_PAINT': 'TEXTURE_PAINT',

            # Grease Pencil 类型（4.2 版本）
            'GPENCILOBJECT': 'OBJECT',
            'GPENCILEDIT_GPENCIL': 'EDIT_GPENCIL',
            'GPENCILSCULPT_GPENCIL': 'SCULPT_GPENCIL',
            'GPENCILPAINT_GPENCIL': 'PAINT_GPENCIL',
            'GPENCILWEIGHT_GPENCIL': 'WEIGHT_GPENCIL',
            'GPENCILVERTEX_GPENCIL': 'VERTEX_GPENCIL',

            # Grease Pencil 类型（4.3 版本）
            'GREASEPENCILOBJECT': 'OBJECT',
            'GREASEPENCILEDIT': 'EDIT',
            'GREASEPENCILSCULPT_GREASE_PENCIL': 'SCULPT_GREASE_PENCIL',
            'GREASEPENCILPAINT_GREASE_PENCIL': 'PAINT_GREASE_PENCIL',
            'GREASEPENCILWEIGHT_GREASE_PENCIL': 'WEIGHT_GREASE_PENCIL',
            'GREASEPENCILVERTEX_GREASE_PENCIL': 'VERTEX_GREASE_PENCIL',

            # Armature 类型（两个版本保持一致）
            'ARMATUREOBJECT': 'OBJECT',
            'ARMATUREEDIT': 'EDIT',
            'ARMATUREPOSE': 'POSE'
        }

        if not bpy.context.active_object:
            return {'CANCELLED'}
        
        else:
            if bpy.context.active_object.type in {'CURVE','SURFACE','META','FONT','LATTICE'}:
                bpy.ops.object.editmode_toggle()
                image_path = bpy.context.active_object.type+bpy.context.active_object.mode + ".png"
                show_notice(image_path)

            elif bpy.context.active_object.type+bpy.context.active_object.mode in type_mode_maps:
                if typeandmode_name["object_prev_name"] == "NONE" or \
                    typeandmode_name["object_prev_name"] != bpy.context.active_object.name or \
                    typeandmode_name["object_prev_type"] != bpy.context.active_object.type:
    
                    bpy.ops.mode.menu_switch()
                else:
                    # 先用 typeandmode_name 字典 获得原来的 object_prev_typeandmode 状态，例如 MESHEDIT_MESH
                    # 再用字典 types_mode_maps 把 MESHEDIT_MESH 转换为 EDIT 的切换模式。
                    bpy.ops.object.mode_set(mode=type_mode_maps[typeandmode_name["object_prev_typeandmode"]])
                    image_path = bpy.context.active_object.type+bpy.context.active_object.mode + ".png"
                    show_notice(image_path)

            else:
                return {'CANCELLED'}

        return {'FINISHED'}

