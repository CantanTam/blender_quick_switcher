import bpy
from .show_switch_notice import show_notice

class SELECT_MODE_OT_right_to_left(bpy.types.Operator):
    bl_idname = "select.mode_right_to_left"
    bl_label = "切换选择模式(左←右)"
    bl_description = "面→线→点方向快速切换"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self,context):
        typeandmode = bpy.context.active_object.type+bpy.context.active_object.mode
        # 防止在场景无物体对象的情况下运行报错
        if not bpy.context.active_object:
            return {'CANCELLED'}
        
        elif typeandmode == "MESHEDIT":
            select_mode = context.tool_settings.mesh_select_mode
            if select_mode[2]:  # 面模式 -> 边模式
                context.tool_settings.mesh_select_mode = (False, True, False)
                show_notice("MESHEDIT_EDGE.png")
            elif select_mode[1]:  # 边模式 -> 顶点模式
                context.tool_settings.mesh_select_mode = (True, False, False)
                show_notice("MESHEDIT_VERTEX.png")
            else:  # 顶点模式 -> 面模式
                context.tool_settings.mesh_select_mode = (False, False, True)
                show_notice("MESHEDIT_FACE.png")

        elif typeandmode in {"MESHVERTEX_PAINT","MESHWEIGHT_PAINT"}:
            if bpy.context.active_object.data.use_paint_mask:
                bpy.context.active_object.data.use_paint_mask = False
                bpy.context.active_object.data.use_paint_mask_vertex = False
                show_notice("MESHVERTEX_NONE.png")
            elif bpy.context.active_object.data.use_paint_mask == False and \
                bpy.context.active_object.data.use_paint_mask_vertex == False:
                bpy.context.active_object.data.use_paint_mask_vertex = True
                show_notice("MESHVERTEX_VERTEX.png")
            elif bpy.context.active_object.data.use_paint_mask_vertex == True:
                bpy.context.active_object.data.use_paint_mask = True
                show_notice("MESHVERTEX_FACE.png")

        elif typeandmode == "MESHTEXTURE_PAINT":
            bpy.context.active_object.data.use_paint_mask = not bpy.context.active_object.data.use_paint_mask
            if bpy.context.active_object.data.use_paint_mask == True:
                show_notice("MESHTEXTURE_FACE.png")
            else:
                show_notice("MESHTEXTURE_NONE.png")

        elif typeandmode == "GPENCILEDIT_GPENCIL":
            if bpy.context.active_object.data.use_curve_edit:
                if bpy.context.scene.tool_settings.gpencil_selectmode_edit == 'POINT':
                    bpy.context.scene.tool_settings.gpencil_selectmode_edit = 'STROKE'
                    show_notice("GREASE_STROKE_CURVEON.png")
                else:
                    bpy.context.scene.tool_settings.gpencil_selectmode_edit = 'POINT'
                    show_notice("GREASE_POINT_CURVEON.png")
            else:
                if bpy.context.scene.tool_settings.gpencil_selectmode_edit == 'POINT':
                    bpy.context.scene.tool_settings.gpencil_selectmode_edit = 'SEGMENT'
                    show_notice("GREASE_BETWEEN.png")
                elif bpy.context.scene.tool_settings.gpencil_selectmode_edit == 'SEGMENT':
                    bpy.context.scene.tool_settings.gpencil_selectmode_edit = 'STROKE'
                    show_notice("GREASE_STROKE.png")
                else:
                    bpy.context.scene.tool_settings.gpencil_selectmode_edit = 'POINT'
                    show_notice("GREASE_POINT.png")

        elif typeandmode == "GREASEPENCILEDIT":
            if bpy.context.scene.tool_settings.gpencil_selectmode_edit == 'POINT':
                bpy.context.scene.tool_settings.gpencil_selectmode_edit = 'SEGMENT'
                show_notice("GREASE_BETWEEN.png")
            elif bpy.context.scene.tool_settings.gpencil_selectmode_edit == 'SEGMENT':
                bpy.context.scene.tool_settings.gpencil_selectmode_edit = 'STROKE'
                show_notice("GREASE_STROKE.png")
            else:
                bpy.context.scene.tool_settings.gpencil_selectmode_edit = 'POINT'
                show_notice("GREASE_POINT.png")   

        elif typeandmode in {"GPENCILVERTEX_GPENCIL","GREASEPENCILVERTEX_GREASE_PENCIL"}:
            if bpy.context.scene.tool_settings.use_gpencil_vertex_select_mask_segment:
                bpy.context.scene.tool_settings.use_gpencil_vertex_select_mask_stroke = True
                show_notice("GREASE_STROKE.png")
            elif bpy.context.scene.tool_settings.use_gpencil_vertex_select_mask_stroke:
                bpy.context.scene.tool_settings.use_gpencil_vertex_select_mask_point = True
                show_notice("GREASE_POINT.png")
            elif bpy.context.scene.tool_settings.use_gpencil_vertex_select_mask_point:
                bpy.context.scene.tool_settings.use_gpencil_vertex_select_mask_point = False
                show_notice("GREASE_NONE.png")
            else:
                bpy.context.scene.tool_settings.use_gpencil_vertex_select_mask_segment = True
                show_notice("GREASE_BETWEEN.png")

        elif typeandmode in {"GPENCILSCULPT_GPENCIL","GREASEPENCILSCULPT_GREASE_PENCIL"}:
            if bpy.context.scene.tool_settings.use_gpencil_select_mask_segment:
                bpy.context.scene.tool_settings.use_gpencil_select_mask_stroke = True
                show_notice("GREASE_STROKE.png")
            elif bpy.context.scene.tool_settings.use_gpencil_select_mask_stroke:
                bpy.context.scene.tool_settings.use_gpencil_select_mask_point = True
                show_notice("GREASE_POINT.png")
            elif bpy.context.scene.tool_settings.use_gpencil_select_mask_point:
                bpy.context.scene.tool_settings.use_gpencil_select_mask_point = False
                show_notice("GREASE_NONE.png")
            else:
                bpy.context.scene.tool_settings.use_gpencil_select_mask_segment = True
                show_notice("GREASE_BETWEEN.png")

        elif typeandmode in {"CURVESEDIT","CURVESSCULPT_CURVES"}:
            if bpy.context.active_object.data.selection_domain == 'POINT':
                bpy.ops.curves.set_selection_domain(domain='CURVE')
                show_notice("CURVES_CURVE.png")
            else:
                bpy.ops.curves.set_selection_domain(domain='POINT')
                show_notice("CURVES_POINT.png")

        return {'FINISHED'}

class SELECT_MODE_OT_left_to_right(bpy.types.Operator):
    bl_idname = "select.mode_left_to_right"
    bl_label = "切换选择模式(左→右)"
    bl_description = "面→线→点方向快速切换"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self,context):
        typeandmode = bpy.context.active_object.type+bpy.context.active_object.mode
        # 防止在场景无物体对象的情况下运行报错
        if not bpy.context.active_object:
            return {'CANCELLED'}
        
        elif typeandmode == "MESHEDIT":
            select_mode = context.tool_settings.mesh_select_mode
            if select_mode[0]:  # 顶点模式 -> 边模式
                context.tool_settings.mesh_select_mode = (False, True, False)
                show_notice("MESHEDIT_EDGE.png")
            elif select_mode[1]:  # 边模式 -> 面模式
                context.tool_settings.mesh_select_mode = (False, False, True)
                show_notice("MESHEDIT_FACE.png")
            else:  # 面模式 -> 顶点模式
                context.tool_settings.mesh_select_mode = (True, False, False)
                show_notice("MESHEDIT_VERTEX.png")

        elif typeandmode in {"MESHVERTEX_PAINT","MESHWEIGHT_PAINT"}:
            if bpy.context.active_object.data.use_paint_mask:
                bpy.context.active_object.data.use_paint_mask = False
                bpy.context.active_object.data.use_paint_mask_vertex = True
                show_notice("MESHVERTEX_VERTEX.png")
            elif bpy.context.active_object.data.use_paint_mask_vertex:
                bpy.context.active_object.data.use_paint_mask_vertex = False
                bpy.context.active_object.data.use_paint_mask = False
                show_notice("MESHVERTEX_NONE.png")
            elif bpy.context.active_object.data.use_paint_mask == False and \
                bpy.context.active_object.data.use_paint_mask_vertex == False:
                bpy.context.active_object.data.use_paint_mask = True
                show_notice("MESHVERTEX_FACE.png")

        elif typeandmode == "MESHTEXTURE_PAINT":
            bpy.context.active_object.data.use_paint_mask = not bpy.context.active_object.data.use_paint_mask
            if bpy.context.active_object.data.use_paint_mask == True:
                show_notice("MESHTEXTURE_FACE.png")
            else:
                show_notice("MESHTEXTURE_NONE.png")

        elif typeandmode == "GPENCILEDIT_GPENCIL":
            if bpy.context.active_object.data.use_curve_edit:
                if bpy.context.scene.tool_settings.gpencil_selectmode_edit == 'POINT':
                    bpy.context.scene.tool_settings.gpencil_selectmode_edit = 'STROKE'
                    show_notice("GREASE_STROKE_CURVEON.png")
                else:
                    bpy.context.scene.tool_settings.gpencil_selectmode_edit = 'POINT'
                    show_notice("GREASE_POINT_CURVEON.png")
            else:
                if bpy.context.scene.tool_settings.gpencil_selectmode_edit == 'POINT':
                    bpy.context.scene.tool_settings.gpencil_selectmode_edit = 'STROKE'
                    show_notice("GREASE_STROKE.png")
                elif bpy.context.scene.tool_settings.gpencil_selectmode_edit == 'STROKE':
                    bpy.context.scene.tool_settings.gpencil_selectmode_edit = 'SEGMENT'
                    show_notice("GREASE_BETWEEN.png")
                else:
                    bpy.context.scene.tool_settings.gpencil_selectmode_edit = 'POINT'
                    show_notice("GREASE_POINT.png")

        elif typeandmode == "GREASEPENCILEDIT":
            if bpy.context.scene.tool_settings.gpencil_selectmode_edit == 'POINT':
                bpy.context.scene.tool_settings.gpencil_selectmode_edit = 'STROKE'
                show_notice("GREASE_STROKE.png")
            elif bpy.context.scene.tool_settings.gpencil_selectmode_edit == 'STROKE':
                bpy.context.scene.tool_settings.gpencil_selectmode_edit = 'SEGMENT'
                show_notice("GREASE_BETWEEN.png")
            else:
                bpy.context.scene.tool_settings.gpencil_selectmode_edit = 'POINT'
                show_notice("GREASE_POINT.png")   

        elif typeandmode in {"GPENCILVERTEX_GPENCIL","GREASEPENCILVERTEX_GREASE_PENCIL"}:
            if bpy.context.scene.tool_settings.use_gpencil_vertex_select_mask_point:
                bpy.context.scene.tool_settings.use_gpencil_vertex_select_mask_stroke = True
                show_notice("GREASE_STROKE.png")
            elif bpy.context.scene.tool_settings.use_gpencil_vertex_select_mask_stroke:
                bpy.context.scene.tool_settings.use_gpencil_vertex_select_mask_segment = True
                show_notice("GREASE_BETWEEN.png")
            elif bpy.context.scene.tool_settings.use_gpencil_vertex_select_mask_segment:
                bpy.context.scene.tool_settings.use_gpencil_vertex_select_mask_segment = False
                show_notice("GREASE_NONE.png")
            else:
                bpy.context.scene.tool_settings.use_gpencil_vertex_select_mask_point = True
                show_notice("GREASE_POINT.png")

        elif typeandmode in {"GPENCILSCULPT_GPENCIL","GREASEPENCILSCULPT_GREASE_PENCIL"}:
            if bpy.context.scene.tool_settings.use_gpencil_select_mask_point:
                bpy.context.scene.tool_settings.use_gpencil_select_mask_stroke = True
                show_notice("GREASE_STROKE.png")
            elif bpy.context.scene.tool_settings.use_gpencil_select_mask_stroke:
                bpy.context.scene.tool_settings.use_gpencil_select_mask_segment = True
                show_notice("GREASE_BETWEEN.png")
            elif bpy.context.scene.tool_settings.use_gpencil_select_mask_segment:
                bpy.context.scene.tool_settings.use_gpencil_select_mask_segment = False
                show_notice("GREASE_NONE.png")
            else:
                bpy.context.scene.tool_settings.use_gpencil_select_mask_point = True
                show_notice("GREASE_POINT.png")

        elif typeandmode in {"CURVESEDIT","CURVESSCULPT_CURVES"}:
            if bpy.context.active_object.data.selection_domain == 'POINT':
                bpy.ops.curves.set_selection_domain(domain='CURVE')
                show_notice("CURVES_CURVE.png")
            else:
                bpy.ops.curves.set_selection_domain(domain='POINT')
                show_notice("CURVES_POINT.png")

        return {'FINISHED'}