import bpy

# “变换”菜单
class VIEW3D_MT_common_function_transform_menu(bpy.types.Menu):
    bl_label = ""
    bl_idname = "view3d.mt_common_function_transform_menu"

    def draw(self, context):
        typeandmode = bpy.context.active_object.type+bpy.context.active_object.mode

        layout = self.layout
        
        if bpy.context.mode == "OBJECT":
            layout.operator("button.action_global_grab", text="移动")
            layout.operator("button.action_global_rotate", text="旋转")
            layout.operator("button.action_global_scale", text="缩放")
            layout.separator()
            layout.operator("button.action_transform_tosphere", text="球形化")
            layout.operator("button.action_transform_shear", text="切变")
            layout.operator("button.action_transform_bend", text="弯曲")
            layout.operator("button.action_transform_push_pull", text="推/拉")
            layout.separator()
            layout.operator("button.action_transform_translate_texturespace_true", text="移动纹理空间")
            layout.operator("button.action_transform_resize_texturespace_true", text="缩放纹理空间")
            layout.separator()
            layout.operator("transform.transform", text="对齐到变换坐标系").mode='ALIGN'
            layout.separator()
            layout.operator("object.randomize_transform", text="随机变换")
            layout.operator("object.align", text="对齐物体")
        elif typeandmode == "MESHEDIT":
            layout.operator("button.action_global_grab", text="移动")
            layout.operator("button.action_global_rotate", text="旋转")
            layout.operator("button.action_global_scale", text="缩放")
            layout.separator()
            layout.operator("button.action_transform_tosphere", text="球形化")
            layout.operator("button.action_transform_shear", text="切变")
            layout.operator("button.action_transform_bend", text="弯曲")
            layout.operator("button.action_transform_push_pull", text="推/拉")
            layout.operator("transform.vertex_warp", text="弯绕")
            layout.operator("transform.vertex_random", text="随机").offset=0.1
            layout.operator("transform.shrink_fatten", text="法向缩放")
            layout.operator("transform.skin_resize", text="重置蒙皮尺寸")
            layout.separator()
            layout.operator("button.action_transform_translate_texturespace_true", text="移动纹理空间")
            layout.operator("button.action_transform_resize_texturespace_true", text="缩放纹理空间")
        elif typeandmode in {"CURVEEDIT","SURFACEEDIT","METAEDIT","LATTICEEDIT"}:
            layout.operator("button.action_global_grab", text="移动")
            layout.operator("button.action_global_rotate", text="旋转")
            layout.operator("button.action_global_scale", text="缩放")
            layout.separator()
            layout.operator("button.action_transform_tosphere", text="球形化")
            layout.operator("button.action_transform_shear", text="切变")
            layout.operator("button.action_transform_bend", text="弯曲")
            layout.operator("button.action_transform_push_pull", text="推/拉")
            layout.operator("transform.vertex_warp", text="弯绕")
            layout.operator("transform.vertex_random", text="随机").offset=0.1
            if typeandmode == "CURVEEDIT":
                layout.operator("transform.transform", text="半径").mode='CURVE_SHRINKFATTEN'
            layout.separator()
            layout.operator("button.action_transform_translate_texturespace_true", text="移动纹理空间")
            layout.operator("button.action_transform_resize_texturespace_true", text="缩放纹理空间")
        elif typeandmode == "GPENCILEDIT_GPENCIL":
            layout.operator("button.action_global_grab", text="移动")
            layout.operator("button.action_global_rotate", text="旋转")
            layout.operator("button.action_global_scale", text="缩放")
            layout.separator()
            layout.operator("button.action_transform_bend", text="弯曲")
            layout.operator("button.action_transform_shear", text="切变")
            layout.operator("button.action_transform_tosphere", text="球形化")
            layout.operator("button.action_transform_push_pull", text="推/拉") # 官方菜单没有这个功能
            layout.operator("transform.transform", text="法向缩放").mode='GPENCIL_SHRINKFATTEN'
        elif typeandmode == "GREASEPENCILEDIT":
            layout.operator("button.action_global_grab", text="移动")
            layout.operator("button.action_global_rotate", text="旋转")
            layout.operator("button.action_global_scale", text="缩放")
            layout.separator()
            layout.operator("button.action_transform_tosphere", text="球形化")
            layout.operator("button.action_transform_shear", text="切变")
            layout.operator("button.action_transform_bend", text="弯曲")
            layout.operator("button.action_transform_push_pull", text="推/拉")
            layout.operator("transform.transform", text="半径").mode='CURVE_SHRINKFATTEN'     
        elif typeandmode in {"ARMATUREEDIT","ARMATUREPOSE"}:
            layout.operator("button.action_global_grab", text="移动")
            layout.operator("button.action_global_rotate", text="旋转")
            layout.operator("button.action_global_scale", text="缩放")
            layout.separator()
            layout.operator("button.action_transform_tosphere", text="球形化")
            layout.operator("button.action_transform_shear", text="切变")
            layout.operator("button.action_transform_bend", text="弯曲")
            layout.operator("button.action_transform_push_pull", text="推/拉")
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

# 变换——球形化
class BUTTON_ACTION_OT_transform_tosphere(bpy.types.Operator):
    bl_idname = "button.action_transform_tosphere"
    bl_label = "球形化"
    bl_description = "快捷键 Shift Alt S"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.ops.transform.tosphere('INVOKE_DEFAULT')
        return {'FINISHED'}
    
# 变换——切变
class BUTTON_ACTION_OT_transform_shear(bpy.types.Operator):
    bl_idname = "button.action_transform_shear"
    bl_label = "切变"
    bl_description = "快捷键 Ctrl Shift Alt S"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.ops.transform.shear('INVOKE_DEFAULT')
        return {'FINISHED'}
    
# 变换——弯曲
class BUTTON_ACTION_OT_transform_bend(bpy.types.Operator):
    bl_idname = "button.action_transform_bend"
    bl_label = "弯曲"
    bl_description = "快捷键 Shift W"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.ops.transform.bend('INVOKE_DEFAULT')
        return {'FINISHED'}
    
# 变换——推/位
class BUTTON_ACTION_OT_transform_push_pull(bpy.types.Operator):
    bl_idname = "button.action_transform_push_pull"
    bl_label = "推/拉"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.ops.transform.push_pull('INVOKE_DEFAULT')
        return {'FINISHED'}
    
# 变换——移动纹理空间
class BUTTON_ACTION_OT_transform_translate_texturespace_true(bpy.types.Operator):
    bl_idname = "button.action_transform_translate_texturespace_true"
    bl_label = "移动纹理空间"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.ops.transform.translate('INVOKE_DEFAULT', texture_space=True)
        return {'FINISHED'}
    
# 变换——缩放纹理空间
class BUTTON_ACTION_OT_transform_resize_texturespace_true(bpy.types.Operator):
    bl_idname = "button.action_transform_resize_texturespace_true"
    bl_label = "缩放纹理空间"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.ops.transform.resize('INVOKE_DEFAULT', texture_space=True)
        return {'FINISHED'}
    
# 变换——随机
class BUTTON_ACTION_OT_transform_vertex_random(bpy.types.Operator):
    bl_idname = "button.action_transform_vertex_random"
    bl_label = "随机"
    bl_description = "多种编辑模式下共用的“随机”"
    bl_options = {'REGISTER', 'UNDO'}

    offset : bpy.props.FloatProperty(
        name="",
        default=0.1,
        min=-10,
        max=10,
        precision=2,
        subtype='DISTANCE',
        update=lambda self, context: self.execute(context)  # 如果需要在修改时自动执行
    )

    uniform : bpy.props.FloatProperty(
        name="",
        default=0.0,
        min=0.0,
        max=1.0,
        precision=3,
        subtype='FACTOR',
        update=lambda self, context: self.execute(context)  # 如果需要在修改时自动执行
    )

    normal : bpy.props.FloatProperty(
        name="",
        default=0.0,
        min=0.0,
        max=1.0,
        precision=3,
        subtype='FACTOR',
        update=lambda self, context: self.execute(context)  # 如果需要在修改时自动执行
    )

    seed: bpy.props.IntProperty(
        name="",
        default=0,
        min=0,
        max=10000,
        update=lambda self, context: self.execute(context)  # 如果需要在修改时自动执行
    )

    def invoke(self, context, event):
        return self.execute(context)
    
    def draw(self, context):
        layout = self.layout
        split = layout.row().split(factor=0.4)
        
        # 左侧列 - 标签
        col_left = split.column()
        col_left.alignment = 'RIGHT'
        col_left.label(text="(数)量")
        col_left.label(text="均衡")
        col_left.label(text="法向")
        col_left.label(text="随机种")

        # 右侧列 - 垂直排列的单选按钮
        col_right = split.column()
        col_right.prop(self, "offset")
        col_right.prop(self, "uniform")
        col_right.prop(self, "normal")
        col_right.prop(self, "seed")

    def execute(self, context):
        bpy.ops.transform.vertex_random(offset=self.offset, uniform=self.uniform, normal=self.normal, seed=self.seed, wait_for_input=True)
        return {'FINISHED'}
    
