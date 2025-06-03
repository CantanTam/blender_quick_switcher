import bpy
import bmesh
from . show_switch_notice import show_notice

gsr_mode: int = 0

def is_object_selected(context):
    obj = context.active_object
    if not obj:
        is_selected = False

    if context.mode == "OBJECT":
        is_selected = obj.select_get()

    if obj.type == 'MESH' and context.mode == "EDIT_MESH":
        bm = bmesh.from_edit_mesh(obj.data)
        is_selected = (
            any(e.select for e in bm.verts) or
            any(e.select for e in bm.edges) or
            any(e.select for e in bm.faces)
        )

    elif obj.type == 'ARMATURE' and context.mode == "EDIT_ARMATURE":
        is_selected = any(
            b.select_head or b.select_tail or b.select
            for b in obj.data.edit_bones
        )

    elif obj.type == 'ARMATURE' and context.mode == "POSE":
        is_selected = any(bone.bone.select for bone in obj.pose.bones)

    elif obj.type == 'CURVE' and context.mode == "EDIT_CURVE":
        is_selected = any(
            (
                p.select_control_point or p.select_left_handle or p.select_right_handle
                if spl.type == 'BEZIER'
                else p.select
            )
            for spl in obj.data.splines
            for p in (spl.bezier_points if spl.type == 'BEZIER' else spl.points)
        )

    elif obj.type == 'CURVES' and context.mode == 'EDIT_CURVES':
        selection_attr = obj.data.attributes.get(".selection")
        is_selected = any(p.value > 0.5 for p in selection_attr.data)

    elif obj.type == 'SURFACE' and context.mode == "EDIT_SURFACE":
        is_selected = any(p.select for spl in obj.data.splines for p in spl.points )

    elif obj.type == 'LATTICE' and context.mode == "EDIT_LATTICE":
        is_selected = any(p.select for p in obj.data.points)

    elif obj.type == 'META' and context.mode == "EDIT_METABALL":
        is_selected = any(e.select for e in obj.data.elements)

    elif obj.type == 'GPENCIL' and context.mode == "EDIT_GPENCIL":
        # Blender api 不支持检测开启曲线状态下的选中检测，所以：关闭→检测→开启
        if getattr(obj.data, "use_curve_edit", True):
            bpy.context.active_object.data.use_curve_edit = False

            try:
                is_selected = any(
                    p.select
                    for l in obj.data.layers
                    for f in l.frames
                    for s in f.strokes
                    for p in s.points
                )
                
            except AttributeError:
                is_selected = False

            bpy.context.active_object.data.use_curve_edit = True
        else:
            try:
                is_selected = any(
                    p.select
                    for l in obj.data.layers
                    for f in l.frames
                    for s in f.strokes
                    for p in s.points
                )
            except AttributeError:
                is_selected = False
        
    elif obj.type == 'GREASEPENCIL' and context.mode == "EDIT_GREASE_PENCIL":
        try:
            is_selected = any(
                p.select
                for l in obj.data.layers
                for f in l.frames
                if f.drawing  # 确保 drawing 存在
                for s in f.drawing.strokes
                for p in s.points
            )
        except AttributeError:
            is_selected = False

    elif obj.type == 'MESH' and context.mode == "SCULPT":
        is_selected = True

    return is_selected

class GRAB_SCALE_ROTATE_OT_Switch(bpy.types.Operator):
    bl_idname = "switch.grab_scale_rotate"
    bl_label = "切换移动/缩放/旋转"
    bl_description = ""
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self,context):
        global gsr_mode

        if not is_object_selected(context):
            return {'CANCELLED'}
        
        typeandmode = bpy.context.active_object.type+bpy.context.active_object.mode

        if bpy.context.mode == "OBJECT" or typeandmode in {
            "GPENCILEDIT_GPENCIL",
            "MESHSCULPT",
            "GREASEPENCILEDIT",
            "ARMATUREEDIT",
            "ARMATUREPOSE",
            "CURVEEDIT",
            "CURVESEDIT",
            "SURFACEEDIT",
            "METAEDIT",
            "LATTICEEDIT",
        }:
            if gsr_mode % 4 == 0:
                show_notice("GSR2R_G.png")
            elif gsr_mode % 4 == 1:
                show_notice("GSR2R_S.png")
            elif gsr_mode % 4 == 2:
                show_notice("GSR2R_R.png")
            elif gsr_mode % 4 == 3:
                show_notice("GSR2R_2R.png")

        elif typeandmode == "MESHEDIT":
            if gsr_mode % 5 == 0:
                show_notice("G2GSR2R_G.png")
            elif gsr_mode % 5 == 1:
                show_notice("G2GSR2R_2G.png")
            elif gsr_mode % 5 == 2:
                show_notice("G2GSR2R_S.png")
            elif gsr_mode % 5 == 3:
                show_notice("G2GSR2R_R.png")
            elif gsr_mode % 5 == 4:
                show_notice("G2GSR2R_2R.png")

        bpy.ops.switch.grab_scale_rotate_action('INVOKE_DEFAULT')

        return {'FINISHED'}


class GRAB_SCALE_ROTATE_OT_Switch_action(bpy.types.Operator):
    bl_idname = "switch.grab_scale_rotate_action"
    bl_label = "Modal Modifier Key Monitor"
    
    def modal(self, context, event):
        global gsr_mode

        typeandmode = bpy.context.active_object.type+bpy.context.active_object.mode

        if not event.ctrl and not event.shift and not event.alt:
            if bpy.context.mode == "OBJECT" or typeandmode in {
                "GPENCILEDIT_GPENCIL",
                "MESHSCULPT",
                "GREASEPENCILEDIT",
                "ARMATUREEDIT",
                "ARMATUREPOSE",
                "CURVEEDIT",
                "CURVESEDIT",
                "SURFACEEDIT",
                "METAEDIT",
                "LATTICEEDIT",
            }:
                if abs(gsr_mode) % 4 == 0:
                    show_notice("GSR_MIDDLE.png")
                    bpy.ops.transform.translate('INVOKE_DEFAULT')
                    return {'FINISHED'}
                elif abs(gsr_mode) % 4 == 1:
                    show_notice("GSR_MIDDLE.png")
                    bpy.ops.transform.resize('INVOKE_DEFAULT')
                    return {'FINISHED'}
                elif abs(gsr_mode) % 4 == 2:
                    show_notice("GSR_MIDDLE.png")
                    bpy.ops.transform.rotate('INVOKE_DEFAULT')
                    return {'FINISHED'}
                elif abs(gsr_mode) % 4 == 3:
                    bpy.ops.transform.trackball('INVOKE_DEFAULT')
                    return {'FINISHED'}

            elif typeandmode == "MESHEDIT":
                if abs(gsr_mode) % 5 == 0:
                    show_notice("GSR_MIDDLE.png")
                    bpy.ops.transform.translate('INVOKE_DEFAULT')
                    return {'FINISHED'}
                    
                elif abs(gsr_mode) % 5 == 1:
                    if context.tool_settings.mesh_select_mode[0]:
                        bpy.ops.transform.vert_slide('INVOKE_DEFAULT')
                        return {'FINISHED'}
                    elif context.tool_settings.mesh_select_mode[1] or context.tool_settings.mesh_select_mode[2]:
                        bm = bmesh.from_edit_mesh(bpy.context.edit_object.data)

                        bm.verts.ensure_lookup_table()
                        bm.edges.ensure_lookup_table()

                        selected_verts = [v for v in bm.verts if v.select]

                        for v in selected_verts:
                            selected_links = [e for e in v.link_edges if e.select]
                            if len(selected_links) > 2:
                                try:
                                    bpy.ops.transform.vert_slide('INVOKE_DEFAULT')
                                except RuntimeError:
                                    bpy.ops.transform.edge_slide('INVOKE_DEFAULT')
                                return {'FINISHED'}
                        
                        # 如果没有任何点满足条件
                        bpy.ops.transform.edge_slide('INVOKE_DEFAULT')
                        return {'FINISHED'}

                elif abs(gsr_mode) % 5 == 2:
                    show_notice("GSR_MIDDLE.png")
                    bpy.ops.transform.resize('INVOKE_DEFAULT')
                    return {'FINISHED'}
                elif abs(gsr_mode) % 5 == 3:
                    show_notice("GSR_MIDDLE.png")
                    bpy.ops.transform.rotate('INVOKE_DEFAULT')
                    return {'FINISHED'}
                elif abs(gsr_mode) % 5 == 4:
                    bpy.ops.transform.trackball('INVOKE_DEFAULT')
                    return {'FINISHED'}
                        
        elif event.type == 'WHEELUPMOUSE':
                    gsr_mode -= 1
                    bpy.ops.switch.grab_scale_rotate()
                    return {'FINISHED'}
        
        elif event.type == 'WHEELDOWNMOUSE':
                    gsr_mode += 1
                    bpy.ops.switch.grab_scale_rotate()

                    return {'FINISHED'}

        elif event.type in {'ESC','RIGHTMOUSE'}:
            return {'CANCELLED'}

        return {'RUNNING_MODAL'}
    
    def invoke(self, context, event):
        context.window_manager.modal_handler_add(self)
        return {'RUNNING_MODAL'}
