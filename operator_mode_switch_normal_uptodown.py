import bpy
from .show_switch_notice import show_notice

class MODE_NORMAL_UPDOWN_OT_Switch(bpy.types.Operator):
    bl_idname = "mode.normal_up_to_down"
    bl_label = "上下方向切换编辑模式"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        # 防止在场景无物体对象的情况下运行报错
        if not bpy.context.active_object:
            return {'CANCELLED'}
        
        else:
            if context.active_object.type in {'GPENCIL','GREASEPENCIL'}:
                # 4.2或以下版本字典
                greasepencil_mode_360 ={
                    "OBJECT":"EDIT_GPENCIL",
                    "EDIT_GPENCIL":"SCULPT_GPENCIL",
                    "SCULPT_GPENCIL":"PAINT_GPENCIL",
                    "PAINT_GPENCIL":"WEIGHT_GPENCIL",
                    "WEIGHT_GPENCIL":"VERTEX_GPENCIL",
                    "VERTEX_GPENCIL":"OBJECT"
                }

                # 4.3或以上版本字典
                greasepencil_mode_400 ={
                    "OBJECT":"EDIT",
                    "EDIT_GREASE_PENCIL":"SCULPT_GREASE_PENCIL",
                    "SCULPT_GREASE_PENCIL":"PAINT_GREASE_PENCIL",
                    "PAINT_GREASE_PENCIL":"WEIGHT_GREASE_PENCIL",
                    "WEIGHT_GREASE_PENCIL":"VERTEX_GREASE_PENCIL",
                    "VERTEX_GREASE_PENCIL":"OBJECT"
                }

                if bpy.app.version < (4,3,0):
                    greasepencil_mode = greasepencil_mode_360
                else:
                    greasepencil_mode = greasepencil_mode_400

                current_mode = context.mode

                if current_mode in greasepencil_mode:
                    new_mode = greasepencil_mode[current_mode]
                    bpy.ops.object.mode_set(mode=new_mode)
        
            elif bpy.context.active_object.type == 'ARMATURE':
                if context.mode == 'OBJECT':
                    bpy.ops.object.mode_set(mode='EDIT')
                elif context.mode == 'EDIT_ARMATURE':
                    bpy.ops.object.mode_set(mode='POSE')
                else:
                    bpy.ops.object.mode_set(mode='OBJECT')

            elif bpy.context.active_object.type == 'CURVES':
                if context.mode == 'OBJECT':
                    bpy.ops.object.mode_set(mode='EDIT')
                elif context.mode == 'EDIT_CURVES':
                    bpy.ops.object.mode_set(mode='SCULPT_CURVES')
                else:
                    bpy.ops.object.mode_set(mode='OBJECT')

            elif bpy.context.active_object.type == 'MESH':
                mesh_mode ={
                    "OBJECT":"EDIT",
                    "EDIT_MESH":"SCULPT",
                    "SCULPT":"VERTEX_PAINT",
                    "PAINT_VERTEX":"WEIGHT_PAINT",
                    "PAINT_WEIGHT":"TEXTURE_PAINT",
                    "PAINT_TEXTURE":"OBJECT"
                }
                
                current_mesh_mode = context.mode

                if current_mesh_mode in mesh_mode:
                    new_mesh_mode = mesh_mode[current_mesh_mode]
                    bpy.ops.object.mode_set(mode=new_mesh_mode)

            elif bpy.context.active_object.type in {'CURVE','SURFACE','META','FONT','LATTICE'}:
                bpy.ops.object.editmode_toggle()

            else:
                return {'CANCELLED'}
            
            image_name = bpy.context.active_object.type+bpy.context.active_object.mode+".png"
            show_notice(image_name)
        
        return {'FINISHED'}
