import bpy
import bmesh
from . show_switch_notice import show_notice

gsr_mode: int = 0

def is_object_selected(context):
    obj = context.active_object
    if not obj:
        return False

    # Object 模式
    if context.mode == "OBJECT":
        return obj.select_get()

    # Mesh Edit 模式
    if obj.type == 'MESH' and context.mode == "EDIT_MESH":
        bm = bmesh.from_edit_mesh(obj.data)
        return (
            any(e.select for e in bm.verts) or
            any(e.select for e in bm.edges) or
            any(e.select for e in bm.faces)
        )

    # Armature Edit 模式
    elif obj.type == 'ARMATURE' and context.mode == "EDIT_ARMATURE":
        return any(
            b.select_head or b.select_tail or b.select
            for b in obj.data.edit_bones
        )

    # ★★★Armature Pose 模式
    elif obj.type == 'ARMATURE' and context.mode == "POSE":
        return any(bone.bone.select for bone in obj.pose.bones)

    # ★★★Curve Edit 模式
    elif obj.type == 'CURVE' and context.mode == "EDIT_CURVE":
        return any(
            (
                # Bézier 点：控制点或任一柄被选中
                p.select_control_point or p.select_left_handle or p.select_right_handle
                if spl.type == 'BEZIER'
                # NURBS/Poly 点：常规 select 属性
                else p.select
            )
            for spl in obj.data.splines
            for p in (spl.bezier_points if spl.type == 'BEZIER' else spl.points)
        )

    # ★★★
    elif obj.type == 'SURFACE' and context.mode == "EDIT_SURFACE":
        return any(p.select for spl in obj.data.splines for p in spl.points )

    # ★★★Lattice Edit 模式
    elif obj.type == 'LATTICE' and context.mode == "EDIT_LATTICE":
        return any(p.select for p in obj.data.points)

    # ★★★Metaball Edit 模式
    elif obj.type == 'META' and context.mode == "EDIT_METABALL":
        return any(e.select for e in obj.data.elements)

    # Grease Pencil Edit 模式（兼容 4.2 和 4.3）
    elif obj.type == 'GPENCIL' and context.mode == "EDIT_GPENCIL":
        try:
            return any(
                p.select
                for l in obj.data.layers
                for f in l.frames
                for s in f.strokes
                for p in s.points
            )
        except AttributeError:
            return False
        
    elif obj.type == 'GREASEPENCIL' and context.mode == "EDIT_GREASE_PENCIL":
        try:
            return any(
                p.select
                for l in obj.data.layers
                for f in l.frames
                if f.drawing  # 确保 drawing 存在
                for s in f.drawing.strokes
                for p in s.points
            )
        except AttributeError:
            return False

    return False

class GRAB_SCALE_ROTATE_OT_Switch(bpy.types.Operator):
    bl_idname = "switch.grab_scale_rotate"
    bl_label = "切换移动/缩放/旋转"
    bl_description = "面→线→点方向快速切换"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self,context):
        global gsr_mode

        if not is_object_selected(context):
            self.report({'WARNING'}, "没有选中任何内容")
            return {'CANCELLED'}
        
        typeandmode = bpy.context.active_object.type+bpy.context.active_object.mode

        if bpy.context.mode == "OBJECT" or typeandmode in {
            "GPENCILEDIT_GPENCIL",
            "GREASEPENCILEDIT",
            "ARMATUREEDIT",
            "ARMATUREPOSE",
            "CURVEEDIT",
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
                "GREASEPENCILEDIT",
                "ARMATUREEDIT",
                "ARMATUREPOSE",
                "CURVEEDIT",
                "SURFACEEDIT",
                "METAEDIT",
                "LATTICEEDIT",
            }:
                if abs(gsr_mode) % 4 == 0:
                    show_notice("star01.png")
                    bpy.ops.transform.translate('INVOKE_DEFAULT')
                    return {'FINISHED'}
                elif abs(gsr_mode) % 4 == 1:
                    show_notice("star02.png")
                    bpy.ops.transform.resize('INVOKE_DEFAULT')
                    return {'FINISHED'}
                elif abs(gsr_mode) % 4 == 2:
                    show_notice("star03.png")
                    bpy.ops.transform.rotate('INVOKE_DEFAULT')
                    return {'FINISHED'}
                elif abs(gsr_mode) % 4 == 3:
                    show_notice("star04.png") 
                    bpy.ops.transform.trackball('INVOKE_DEFAULT')
                    return {'FINISHED'}

            elif typeandmode == "MESHEDIT":
                if abs(gsr_mode) % 5 == 0:
                    show_notice("star01.png")
                    bpy.ops.transform.translate('INVOKE_DEFAULT')
                    return {'FINISHED'}
                    
                elif abs(gsr_mode) % 5 == 1:
                    if context.tool_settings.mesh_select_mode[0]:
                        show_notice("star01.png")
                        bpy.ops.transform.vert_slide('INVOKE_DEFAULT')
                        return {'FINISHED'}
                    elif context.tool_settings.mesh_select_mode[1] or context.tool_settings.mesh_select_mode[2]:
                        # 只要有一个选中点的连接选中边数量超过3，就滑移顶点
                        bm = bmesh.from_edit_mesh(bpy.context.edit_object.data)

                        bm.verts.ensure_lookup_table()
                        bm.edges.ensure_lookup_table()

                        selected_verts = [v for v in bm.verts if v.select]

                        for v in selected_verts:
                            selected_links = [e for e in v.link_edges if e.select]
                            if len(selected_links) > 2:
                                try:
                                    # 强制切换模式 + 执行 vert_slide
                                    show_notice("star01.png")
                                    #bpy.ops.mesh.select_mode(type='VERT')
                                    bpy.ops.transform.vert_slide('INVOKE_DEFAULT')
                                except RuntimeError:
                                    self.report({'WARNING'}, "VERT slide failed, fallback to EDGE slide")
                                    bpy.ops.transform.edge_slide('INVOKE_DEFAULT')
                                return {'FINISHED'}
                        
                        # 如果没有任何点满足条件
                        show_notice("star01.png")
                        bpy.ops.transform.edge_slide('INVOKE_DEFAULT')
                        return {'FINISHED'}

                elif abs(gsr_mode) % 5 == 2:
                    show_notice("star02.png")
                    bpy.ops.transform.resize('INVOKE_DEFAULT')
                    return {'FINISHED'}
                elif abs(gsr_mode) % 5 == 3:
                    show_notice("star03.png")
                    bpy.ops.transform.rotate('INVOKE_DEFAULT')
                    return {'FINISHED'}
                elif abs(gsr_mode) % 5 == 4:
                    show_notice("star04.png") 
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
            self.report({'INFO'}, "Cancelled")
            return {'CANCELLED'}

        return {'RUNNING_MODAL'}
    
    def invoke(self, context, event):
        context.window_manager.modal_handler_add(self)
        self.report({'INFO'}, "Modifier key monitor started (ESC to stop)")
        return {'RUNNING_MODAL'}
