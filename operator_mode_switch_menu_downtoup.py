import bpy

# 菜单选择模式切换编辑方式
class MODE_MENU_OT_Switch(bpy.types.Operator):
    bl_idname = "mode.menu_switch"
    bl_label = "选择编辑模式菜单"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        # 防止在场景无物体对象的情况下运行报错
        if not bpy.context.active_object:
            return {'CANCELLED'}
        
        else:
            # Blender 4.2 及以下蜡笔的 mode 名称：
            if context.active_object.type == 'GPENCIL':
                def gpencil_menu(self, context):
                    layout = self.layout
                    layout.operator("object.mode_set", text="物体模式", icon='OBJECT_DATAMODE').mode = 'OBJECT'
                    layout.operator("object.mode_set", text="编辑模式",icon='EDITMODE_HLT').mode = 'EDIT_GPENCIL'
                    layout.operator("object.mode_set", text="雕刻模式", icon='SCULPTMODE_HLT').mode = 'SCULPT_GPENCIL'
                    layout.operator("object.mode_set", text="绘制模式",icon='GREASEPENCIL').mode = 'PAINT_GPENCIL'
                    layout.operator("object.mode_set", text="权重绘制", icon='WPAINT_HLT').mode = 'WEIGHT_GPENCIL'
                    layout.operator("object.mode_set", text="顶点绘制",icon='VPAINT_HLT').mode = 'VERTEX_GPENCIL'
                    
                context.window_manager.popup_menu(gpencil_menu, title="切换蜡笔模式")

            # Blender 4.3 及以上蜡笔的 mode 名称：
            elif context.active_object.type == 'GREASEPENCIL':
                def greasepencil_menu(self, context):
                    layout = self.layout
                    layout.operator("object.mode_set", text="物体模式", icon='OBJECT_DATAMODE').mode = 'OBJECT'
                    layout.operator("object.mode_set", text="编辑模式",icon='EDITMODE_HLT').mode = 'EDIT'
                    layout.operator("object.mode_set", text="雕刻模式", icon='SCULPTMODE_HLT').mode = 'SCULPT_GREASE_PENCIL'
                    layout.operator("object.mode_set", text="绘制模式",icon='GREASEPENCIL').mode = 'PAINT_GREASE_PENCIL'
                    layout.operator("object.mode_set", text="权重绘制", icon='WPAINT_HLT').mode = 'WEIGHT_GREASE_PENCIL'
                    layout.operator("object.mode_set", text="顶点绘制",icon='VPAINT_HLT').mode = 'VERTEX_GREASE_PENCIL'
                    
                context.window_manager.popup_menu(greasepencil_menu, title="切换蜡笔模式")
            
            elif context.active_object.type == 'MESH':
                def mesh_menu(self, context):
                    layout = self.layout
                    layout.operator("object.mode_set", text="物体模式", icon='OBJECT_DATAMODE').mode = 'OBJECT'
                    layout.operator("object.mode_set", text="编辑模式",icon='EDITMODE_HLT').mode = 'EDIT'
                    layout.operator("object.mode_set", text="雕刻模式", icon='SCULPTMODE_HLT').mode = 'SCULPT'
                    layout.operator("object.mode_set", text="顶点绘制",icon='VPAINT_HLT').mode = 'VERTEX_PAINT'
                    layout.operator("object.mode_set", text="权重绘制", icon='WPAINT_HLT').mode = 'WEIGHT_PAINT'
                    layout.operator("object.mode_set", text="纹理绘制",icon='TPAINT_HLT').mode = 'TEXTURE_PAINT'
                    
                context.window_manager.popup_menu(mesh_menu, title="切换物体模式")

            elif context.active_object.type == 'ARMATURE':
                def armature_menu(self, context):
                    layout = self.layout
                    layout.operator("object.mode_set", text="物体模式", icon='OBJECT_DATAMODE').mode = 'OBJECT'
                    layout.operator("object.mode_set", text="编辑模式",icon='EDITMODE_HLT').mode = 'EDIT'
                    layout.operator("object.mode_set", text="姿态模式", icon='POSE_HLT').mode = 'POSE'
                    
                context.window_manager.popup_menu(armature_menu, title="切换骨架模式")

            elif bpy.context.active_object.type in {'CURVE','SURFACE','META','FONT'}:
                bpy.ops.object.editmode_toggle()
                
            else:
                return {'CANCELLED'}
        
        return {'FINISHED'}
