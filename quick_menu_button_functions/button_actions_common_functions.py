import bpy

# “变换”菜单
class VIEW3D_MT_common_function_transform_menu(bpy.types.Menu):
    bl_label = ""
    bl_idname = "view3d.mt_common_function_transform_menu"

    def draw(self, context):
        typeandmode = bpy.context.active_object.type+bpy.context.active_object.mode

        layout = self.layout
        
        if bpy.context.mode == "OBJECT":
            layout.operator("transform.translate", text="移动")
            layout.operator("transform.rotate", text="旋转")
            layout.operator("transform.resize", text="缩放")
            layout.separator()
            layout.operator("transform.tosphere", text="球形化")
            layout.operator("transform.shear", text="切变")
            layout.operator("transform.bend", text="弯曲")
            layout.operator("transform.push_pull", text="推/拉")
            layout.separator()
            layout.operator("transform.translate", text="移动纹理空间").texture_space=True
            layout.operator("transform.resize", text="缩放纹理空间").texture_space=True
            layout.separator()
            layout.operator("transform.transform", text="对齐到变换坐标系").mode='ALIGN'
            layout.separator()
            layout.operator("object.randomize_transform", text="随机变换")
            layout.operator("object.align", text="对齐物体")
        elif typeandmode == "MESHEDIT":
            layout.operator("transform.translate", text="移动")
            layout.operator("transform.rotate", text="旋转")
            layout.operator("transform.resize", text="缩放")
            layout.separator()
            layout.operator("transform.tosphere", text="球形化")
            layout.operator("transform.shear", text="切变")
            layout.operator("transform.bend", text="弯曲")
            layout.operator("transform.push_pull", text="推/拉")
            layout.operator("transform.vertex_warp", text="弯绕")
            layout.operator("transform.vertex_random", text="随机").offset=0.1
            layout.operator("transform.shrink_fatten", text="法向缩放")
            layout.operator("transform.skin_resize", text="重置蒙皮尺寸")
            layout.separator()
            layout.operator("transform.translate", text="移动纹理空间").texture_space=True
            layout.operator("transform.resize", text="缩放纹理空间").texture_space=True
        elif typeandmode in {"CURVEEDIT","SURFACEEDIT","METAEDIT","LATTICEEDIT"}:
            layout.operator("transform.translate", text="移动")
            layout.operator("transform.rotate", text="旋转")
            layout.operator("transform.resize", text="缩放")
            layout.separator()
            layout.operator("transform.tosphere", text="球形化")
            layout.operator("transform.shear", text="切变")
            layout.operator("transform.bend", text="弯曲")
            layout.operator("transform.push_pull", text="推/拉")
            layout.operator("transform.vertex_warp", text="弯绕")
            layout.operator("transform.vertex_random", text="随机").offset=0.1
            if typeandmode == "CURVEEDIT":
                layout.operator("transform.transform", text="半径").mode='CURVE_SHRINKFATTEN'
            layout.separator()
            layout.operator("transform.translate", text="移动纹理空间").texture_space=True
            layout.operator("transform.resize", text="缩放纹理空间").texture_space=True
        elif typeandmode == "GPENCILEDIT_GPENCIL":
            layout.operator("transform.translate", text="移动")
            layout.operator("transform.rotate", text="旋转")
            layout.operator("transform.resize", text="缩放")
            layout.separator()
            layout.operator("transform.bend", text="弯曲")
            layout.operator("transform.shear", text="切变")
            layout.operator("transform.tosphere", text="球形化")
            layout.operator("transform.transform", text="法向缩放").mode='GPENCIL_SHRINKFATTEN'
        elif typeandmode == "GREASEPENCILEDIT":
            layout.operator("transform.translate", text="移动")
            layout.operator("transform.rotate", text="旋转")
            layout.operator("transform.resize", text="缩放")
            layout.separator()
            layout.operator("transform.tosphere", text="球形化")
            layout.operator("transform.shear", text="切变")
            layout.operator("transform.bend", text="弯曲")
            layout.operator("transform.push_pull", text="推/拉")
            layout.operator("transform.transform", text="半径").mode='CURVE_SHRINKFATTEN'     
        elif typeandmode in {"ARMATUREEDIT","ARMATUREPOSE"}:
            layout.operator("transform.translate", text="移动")
            layout.operator("transform.rotate", text="旋转")
            layout.operator("transform.resize", text="缩放")
            layout.separator()
            layout.operator("transform.tosphere", text="球形化")
            layout.operator("transform.shear", text="切变")
            layout.operator("transform.bend", text="弯曲")
            layout.operator("transform.push_pull", text="推/拉")
            if typeandmode == "ARMATUREEDIT":
                layout.operator("transform.vertex_warp", text="弯绕")
                layout.operator("transform.vertex_random", text="随机").offset=0.1
                layout.separator()
                layout.operator("armature.align", text="对齐骨骼")

class BUTTON_ACTION_OT_call_common_function_transform_menu(bpy.types.Operator):
    bl_idname = "button.action_call_common_function_transform_menu"
    bl_label = "变换(菜单)"
    bl_description = "物体/网格模式共用的变换菜单"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.ops.wm.call_menu(name="view3d.mt_common_function_transform_menu")
        return {'FINISHED'}
