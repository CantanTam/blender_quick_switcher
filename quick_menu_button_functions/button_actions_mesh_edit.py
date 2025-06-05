import bpy
import bmesh

# “选择”菜单
class BUTTON_ACTION_OT_mesh_select_nth(bpy.types.Operator):
    bl_idname = "button.action_mesh_select_nth"
    bl_label = "间隔式弃选"
    bl_options = {'REGISTER', 'UNDO'}

    skip: bpy.props.IntProperty(
        name="",
        description="重复次序中跳过的元素数量",
        default=1,
        min=1,
        soft_max=100, 
    )

    nth: bpy.props.IntProperty(
        name="",
        description="重复次序中选择的元素数量",
        default=1,
        min=1,
        soft_max=100, 
    )

    offset: bpy.props.IntProperty(
        name="",
        description="从起始点偏移",
        default=0,
        soft_min=-100,
        soft_max=100, 
    )

    def invoke(self, context, event):
        return self.execute(context)

    def draw(self, context):
        layout = self.layout
        split = layout.row().split(factor=0.4)
        
        col_left = split.column()
        col_left.alignment = 'RIGHT'
        col_left.label(text="弃选项")
        col_left.label(text="选中项")
        col_left.label(text="偏移量")
        
        col_right = split.column()
        col_right.prop(self, "skip")
        col_right.prop(self, "nth")
        col_right.prop(self, "offset")

    def execute(self, context):
        bpy.ops.mesh.select_nth(skip=self.skip, nth=self.nth, offset=self.offset)
        return {'FINISHED'}

class BUTTON_ACTION_OT_mesh_edges_select_sharp(bpy.types.Operator):
    bl_idname = "button.action_mesh_edges_select_sharp"
    bl_label = "选择锐边"
    bl_options = {'REGISTER', 'UNDO'}

    sharpness: bpy.props.FloatProperty(
        name="",
        default=0.523599,
        min=0.000174533,
        max=3.14159,
        soft_min=0.0174533,
        soft_max=3.14159,
        subtype='ANGLE',
    )

    def invoke(self, context, event):
        return self.execute(context)

    def draw(self, context):
        layout = self.layout
        split = layout.row().split(factor=0.4)
        
        col_left = split.column()
        col_left.alignment = 'RIGHT'
        col_left.label(text="锐度")
        
        col_right = split.column()
        col_right.prop(self, "sharpness")

    def execute(self, context):
        bpy.ops.mesh.edges_select_sharp(sharpness=self.sharpness)
        return {'FINISHED'}

class BUTTON_ACTION_OT_mesh_select_by_trait(bpy.types.Operator):
    bl_idname = "popup.mesh_select_by_trait"
    bl_label = "按特征全选"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        return {'FINISHED'}

    def invoke(self, context, event):
        return context.window_manager.invoke_popup(self, width=100)

    def draw(self, context):
        layout = self.layout
        row = layout.row()
        col = row.column(align=True)
        col.label(text="按特征全选", icon='PRESET')
        col.operator("mesh.select_non_manifold", text="非流形", icon="RADIOBUT_OFF")
        col.operator("mesh.select_loose", text="松散几何元素", icon="RADIOBUT_OFF")
        col.operator("mesh.select_interior_faces", text="内侧面", icon="RADIOBUT_OFF")
        col.operator("mesh.select_face_by_sides", text="按侧选面", icon="RADIOBUT_OFF")

class BUTTON_ACTION_OT_mesh_call_select_by_trait(bpy.types.Operator):
    bl_idname = "button.action_mesh_call_select_by_trait"
    bl_label = "按特征全选"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.ops.popup.mesh_select_by_trait('INVOKE_DEFAULT')
        return {'FINISHED'}

class BUTTON_ACTION_OT_mesh_select_loops(bpy.types.Operator):
    bl_idname = "popup.mesh_select_loops"
    bl_label = "选择循环"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        return {'FINISHED'}

    def invoke(self, context, event):
        return context.window_manager.invoke_popup(self, width=100)

    def draw(self, context):
        layout = self.layout
        row = layout.row()
        col = row.column(align=True)
        col.label(text="选择循环", icon='PRESET')
        col.operator("mesh.loop_multi_select", text="循环边", icon="RADIOBUT_OFF").ring=False
        col.operator("mesh.loop_multi_select", text="并排边", icon="RADIOBUT_OFF").ring=True
        col.separator()
        col.operator("mesh.loop_to_region", text="选择循环线内侧区域", icon="RADIOBUT_OFF")
        col.operator("mesh.region_to_loop", text="选择区域轮廓线", icon="RADIOBUT_OFF")
        col.separator()
        col.operator("ed.undo", text="撤销", icon="LOOP_BACK")
        col.operator("ed.redo", text="重做", icon="LOOP_FORWARDS")

class BUTTON_ACTION_OT_call_mesh_select_loops(bpy.types.Operator):
    bl_idname = "button.action_call_mesh_select_loops"
    bl_label = "选择循环"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.ops.popup.mesh_select_loops('INVOKE_DEFAULT')
        return {'FINISHED'}

class BUTTON_ACTION_OT_mesh_select_axis(bpy.types.Operator):
    bl_idname = "button.action_mesh_select_axis"
    bl_label = "活动项的同侧"
    bl_options = {'REGISTER', 'UNDO'}

    orientation: bpy.props.EnumProperty(
        name="",
        description="轴朝向",
        items=[
            ('GLOBAL', "全局",    "", 'ORIENTATION_GLOBAL',   0),
            ('LOCAL',  "局部",     "", 'ORIENTATION_LOCAL', 1),
            ('NORMAL', "法向",    "", 'ORIENTATION_NORMAL',   2),
            ('GIMBAL', "万向",    "", 'ORIENTATION_GIMBAL',    3),
            ('VIEW',   "视图",      "", 'ORIENTATION_VIEW',      4),
            ('CURSOR', "游标",    "", 'ORIENTATION_CURSOR',        5),
            ('PARENT', "父级",    "", 'ORIENTATION_PARENT',     6),
        ],
        default='LOCAL',
    )

    sign: bpy.props.EnumProperty(
        name="",
        description="选择的一侧",
        items=[
            ('POS',   "正轴向",   ""),
            ('NEG',   "负轴向",   ""),
            ('ALIGN', "对齐轴",   ""),
        ],
        default='POS',
    )

    axis: bpy.props.EnumProperty(
        name="",
        description="选择各点用来比较的轴向",
        items=[
            ('X', "X", ""),
            ('Y', "Y", ""),
            ('Z', "Z", ""),
        ],
        default='X',
    )

    threshold: bpy.props.FloatProperty(
        name="",
        description="",
        default=0,
        min=0,
        max=50.0,
        soft_max=10.0,
        precision=3,
    )

    def invoke(self, context, event):
        return self.execute(context)

    def draw(self, context):
        layout = self.layout
        split = layout.row().split(factor=0.4)
        
        col_left = split.column()
        col_left.alignment = 'RIGHT'
        col_left.label(text="轴向模式")
        col_left.label(text="轴向记号")
        col_left.label(text="轴向")
        col_left.label(text="阈值")

        col_right = split.column()
        col_right.prop(self, "orientation")
        col_right.prop(self, "sign")
        col_right.prop(self, "axis")
        col_right.prop(self, "threshold")

    def execute(self, context):
        bpy.ops.mesh.select_axis(orientation=self.orientation, sign=self.sign, axis=self.axis, threshold=self.threshold)
        return {'FINISHED'}

# “网格”菜单
class BUTTON_ACTION_OT_meshedit_transform_shrink_fatten(bpy.types.Operator):
    bl_idname = "button.action_meshedit_transform_shrink_fatten"
    bl_label = "法向缩放"
    bl_description = "快捷键 Alt S"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.ops.transform.shrink_fatten('INVOKE_DEFAULT')
        return {'FINISHED'}

class BUTTON_ACTION_OT_meshedit_transform_skin_resize(bpy.types.Operator):
    bl_idname = "button.action_meshedit_transform_skin_resize"
    bl_label = "重置蒙皮尺寸"
    bl_description = "快捷键 Ctrl A"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.ops.transform.skin_resize('INVOKE_DEFAULT')
        return {'FINISHED'}

class BUTTON_ACTION_OT_meshedit_edit_mesh_extrude_menu(bpy.types.Operator):
    bl_idname = "button.action_meshedit_edit_mesh_extrude_menu"
    bl_label = "挤出"
    bl_description = "快捷键 Alt E"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.ops.wm.call_menu(name="VIEW3D_MT_edit_mesh_extrude")
        return {'FINISHED'}
    
class BUTTON_ACTION_OT_meshedit_edit_mesh_merge_menu(bpy.types.Operator):
    bl_idname = "button.action_meshedit_edit_mesh_merge_menu"
    bl_label = "合并"
    bl_description = "快捷键 M"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.ops.wm.call_menu(name="VIEW3D_MT_edit_mesh_merge")
        return {'FINISHED'}

class BUTTON_ACTION_OT_meshedit_edit_mesh_split_menu(bpy.types.Operator):
    bl_idname = "button.action_meshedit_edit_mesh_split_menu"
    bl_label = "拆分"
    bl_description = "快捷键 Alt M"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.ops.wm.call_menu(name="VIEW3D_MT_edit_mesh_split")
        return {'FINISHED'}
    
class BUTTON_ACTION_OT_meshedit_edit_mesh_split_menu(bpy.types.Operator):
    bl_idname = "button.action_meshedit_edit_mesh_split_menu"
    bl_label = "拆分"
    bl_description = "快捷键 Alt M"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.ops.wm.call_menu(name="VIEW3D_MT_edit_mesh_split")
        return {'FINISHED'}
    
class BUTTON_ACTION_OT_meshedit_mesh_separate(bpy.types.Operator):
    bl_idname = "button.action_meshedit_mesh_separate"
    bl_label = "分离"
    bl_description = "快捷键 P"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.ops.mesh.separate('INVOKE_DEFAULT')
        return {'FINISHED'} 

class BUTTON_ACTION_OT_meshedit_mesh_bisect(bpy.types.Operator):
    bl_idname = "button.action_meshedit_mesh_bisect"
    bl_label = "切分"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.ops.mesh.bisect('INVOKE_DEFAULT')
        return {'FINISHED'} 
    
class BUTTON_ACTION_OT_meshedit_mesh_knife_project(bpy.types.Operator):
    bl_idname = "button.action_meshedit_mesh_knife_project"
    bl_label = "投影切割"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.ops.mesh.knife_project()
        return {'FINISHED'} 

class BUTTON_ACTION_OT_meshedit_mesh_knife_tool(bpy.types.Operator):
    bl_idname = "button.action_meshedit_mesh_knife_tool"
    bl_label = "裁刀拓扑工具"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.ops.mesh.knife_tool('INVOKE_DEFAULT')
        return {'FINISHED'} 

class BUTTON_ACTION_OT_meshedit_mesh_convex_hull(bpy.types.Operator):
    bl_idname = "button.action_meshedit_mesh_convex_hull"
    bl_label = "凸壳"
    bl_options = {'REGISTER', 'UNDO'}

    delete_unused: bpy.props.BoolProperty(
        name="删除未使用项",
        description="",
        default=True
    )

    use_existing_faces: bpy.props.BoolProperty(
        name="使用已有的面",
        description="",
        default=True
    )

    make_holes: bpy.props.BoolProperty(
        name="生成空洞",
        description="",
        default=False
    )

    join_triangles: bpy.props.BoolProperty(
        name="合并三角面",
        description="",
        default=True
    )

    face_threshold: bpy.props.FloatProperty(
        name="",
        description="Face angle limit in radians",
        default=0.698132,
        min=0.0,
        max=3.14159,
        subtype='ANGLE'
    )

    shape_threshold: bpy.props.FloatProperty(
        name="",
        description="",
        default=0.698132,
        min=0.0,
        max=3.14159,
        subtype='ANGLE'
    )

    uvs: bpy.props.BoolProperty(
        name="比较UV",
        description="",
        default=False
    )

    vcols: bpy.props.BoolProperty(
        name="比较顶点色",
        description="",
        default=False
    )

    seam: bpy.props.BoolProperty(
        name="比较缝合边",
        description="",
        default=False
    )

    sharp: bpy.props.BoolProperty(
        name="比较锐边",
        description="",
        default=False
    )

    materials: bpy.props.BoolProperty(
        name="比较材质",
        description="",
        default=False
    )

    def invoke(self, context, event):
        return self.execute(context)

    def draw(self, context):
        layout = self.layout
        split = layout.row().split(factor=0.4)
        
        col_left = split.column()
        col_left.alignment = 'RIGHT'
        col_left.label(text="")
        col_left.label(text="")
        col_left.label(text="")
        col_left.label(text="")
        col_left.label(text="面夹角最大值")
        col_left.label(text="最大形状角度")
        col_left.label(text="")
        col_left.label(text="")
        col_left.label(text="")
        col_left.label(text="")
        col_left.label(text="")

        col_right = split.column()
        col_right.prop(self, "delete_unused")
        col_right.prop(self, "use_existing_faces")
        col_right.prop(self, "make_holes")
        col_right.prop(self, "join_triangles")
        col_right.prop(self, "face_threshold")
        col_right.prop(self, "shape_threshold")
        col_right.prop(self, "uvs")
        col_right.prop(self, "vcols")
        col_right.prop(self, "seam")
        col_right.prop(self, "sharp")
        col_right.prop(self, "materials")

    def execute(self, context):
        bpy.ops.mesh.convex_hull(
            delete_unused=self.delete_unused,
            use_existing_faces=self.use_existing_faces,
            make_holes=self.make_holes,
            join_triangles=self.join_triangles,
            face_threshold=self.face_threshold,
            shape_threshold=self.shape_threshold,
            uvs=self.uvs,
            vcols=self.vcols,
            seam=self.seam,
            sharp=self.sharp,
            materials=self.materials,)
        return {'FINISHED'} 
    
class BUTTON_ACTION_OT_meshedit_mesh_symmetrize(bpy.types.Operator):
    bl_idname = "button.action_meshedit_mesh_symmetrize"
    bl_label = "对称"
    bl_options = {'REGISTER', 'UNDO'}

    direction: bpy.props.EnumProperty(
        name="",
        items=[
            ('NEGATIVE_X', "-X 到 +X", ""),
            ('POSITIVE_X', "+X 到 -X", ""),
            ('NEGATIVE_Y', "-Y 到 +Y", ""),
            ('POSITIVE_Y', "+Y 到 -Y", ""),
            ('NEGATIVE_Z', "-Z 到 +Z", ""),
            ('POSITIVE_Z', "+Z 到 -Z", ""),
        ],
        default='NEGATIVE_X'
    )

    threshold: bpy.props.FloatProperty(
        name="",
        default=0.000,
        min=0.0,
        max=10.0,
        soft_max=0.1,
        precision=3,
    )

    def invoke(self, context, event):
        return self.execute(context)

    def draw(self, context):
        layout = self.layout
        split = layout.row().split(factor=0.4)

        col_left = split.column()
        col_left.alignment = 'RIGHT'
        col_left.label(text="方向")
        col_left.label(text="阈值")

        col_right = split.column()
        col_right.prop(self, "direction")
        col_right.prop(self, "threshold")

    def execute(self, context):
        bpy.ops.mesh.symmetrize(direction=self.direction, threshold=self.threshold)
        return {'FINISHED'} 

class BUTTON_ACTION_OT_meshedit_mesh_symmetry_snap(bpy.types.Operator):
    bl_idname = "button.action_meshedit_mesh_symmetry_snap"
    bl_label = "吸附到对称结构"
    bl_options = {'REGISTER', 'UNDO'}

    direction: bpy.props.EnumProperty(
        name="",
        items=[
            ('NEGATIVE_X', "-X 到 +X", ""),
            ('POSITIVE_X', "+X 到 -X", ""),
            ('NEGATIVE_Y', "-Y 到 +Y", ""),
            ('POSITIVE_Y', "+Y 到 -Y", ""),
            ('NEGATIVE_Z', "-Z 到 +Z", ""),
            ('POSITIVE_Z', "+Z 到 -Z", "")
        ],
        default='NEGATIVE_X'
    )

    threshold: bpy.props.FloatProperty(
        name="",
        default=0.05,
        min=0.0,
        max=10.0,
        soft_max=1,
        subtype="DISTANCE",
    )

    factor: bpy.props.FloatProperty(
        name="",
        default=0.5,
        min=0.0,
        max=1.0
    )

    use_center: bpy.props.BoolProperty(
        name="中心",
        default=True
    )

    def invoke(self, context, event):
        return self.execute(context)

    def draw(self, context):
        layout = self.layout
        split = layout.row().split(factor=0.4)

        col_left = split.column()
        col_left.alignment = 'RIGHT'
        col_left.label(text="方向")
        col_left.label(text="阈值")
        col_left.label(text="系数")
        col_left.label(text="")

        col_right = split.column()
        col_right.prop(self, "direction")
        col_right.prop(self, "threshold")
        col_right.prop(self, "factor")
        col_right.prop(self, "use_center")
        
    def execute(self, context):
        bpy.ops.mesh.symmetry_snap(
            direction=self.direction,
            threshold=self.threshold, 
            factor=self.factor,
            use_center=self.use_center,)
        return {'FINISHED'} 
    
class BUTTON_ACTION_OT_meshedit_edit_mesh_normals_menu(bpy.types.Operator):
    bl_idname = "button.action_meshedit_edit_mesh_normals_menu"
    bl_label = "法向"
    bl_description = "快捷键 Alt N"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.ops.wm.call_menu(name="VIEW3D_MT_edit_mesh_normals")
        return {'FINISHED'}

class BUTTON_ACTION_OT_meshedit_flip_normals(bpy.types.Operator):
    bl_idname = "button.action_meshedit_flip_normals"
    bl_label = "翻转法向"
    bl_options = {'REGISTER', 'UNDO'}

    only_clnors: bpy.props.BoolProperty(
        name="仅自定义法向",
        default=False,
    )

    def invoke(self, context, event):
        return self.execute(context)

    def draw(self, context):
        layout = self.layout
        split = layout.row().split(factor=0.4)

        col_left = split.column()
        col_left.alignment = 'RIGHT'
        col_left.label(text="")

        col_right = split.column()
        col_right.prop(self, "only_clnors")

    def execute(self, context):
        bpy.ops.mesh.flip_normals(only_clnors=self.only_clnors)
        return {'FINISHED'}

class BUTTON_ACTION_OT_meshedit_normals_make_consistent(bpy.types.Operator):
    bl_idname = "button.action_meshedit_normals_make_consistent"
    bl_label = "重新计算法线"
    bl_options = {'REGISTER', 'UNDO'}

    inside: bpy.props.EnumProperty(
        name="",
        items=[
            ('OUT', "外向", ""),
            ('IN', "内向", ""),
        ],
        default='OUT',
    )
    
    def invoke(self, context, event):
        return self.execute(context)

    def draw(self, context):
        layout = self.layout
        split = layout.row().split(factor=0.4)

        col_left = split.column()
        col_left.alignment = 'RIGHT'
        col_left.label(text="法线方向")

        col_right = split.column()
        col_right.prop(self, "inside", text="abc", expand=True)

    def execute(self, context):
        bpy.ops.mesh.normals_make_consistent(inside=False if self.inside == 'OUT' else True)
        return {'FINISHED'}
    
class BUTTON_ACTION_OT_meshedit_set_normals_from_faces(bpy.types.Operator):
    bl_idname = "button.action_meshedit_set_normals_from_faces"
    bl_label = "从面设置法向"
    bl_options = {'REGISTER', 'UNDO'}

    keep_sharp: bpy.props.BoolProperty(
        name="保持锐边",
        default=False,
    )

    def invoke(self, context, event):
        return self.execute(context)

    def draw(self, context):
        layout = self.layout
        split = layout.row().split(factor=0.4)

        col_left = split.column()
        col_left.alignment = 'RIGHT'
        col_left.label(text="")

        col_right = split.column()
        col_right.prop(self, "keep_sharp")

    def execute(self, context):
        bpy.ops.mesh.set_normals_from_faces(keep_sharp=self.keep_sharp)
        return {'FINISHED'}

class BUTTON_ACTION_OT_meshedit_transform_rotate_normal(bpy.types.Operator):
    bl_idname = "button.action_meshedit_transform_rotate_normal"
    bl_label = "旋转法向"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.ops.transform.rotate_normal('INVOKE_DEFAULT')
        return {'FINISHED'}

class BUTTON_ACTION_OT_meshedit_point_normals(bpy.types.Operator):
    bl_idname = "button.action_meshedit_point_normals"
    bl_label = "法向指向目标体"
    bl_description = "快捷键 Alt L"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.ops.mesh.point_normals('INVOKE_DEFAULT')
        return {'FINISHED'}

class BUTTON_ACTION_OT_meshedit_merge_normals(bpy.types.Operator):
    bl_idname = "button.action_meshedit_merge_normals"
    bl_label = "合并法向"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.ops.mesh.merge_normals()
        return {'FINISHED'}

class BUTTON_ACTION_OT_meshedit_split_normals(bpy.types.Operator):
    bl_idname = "button.action_meshedit_split_normals"
    bl_label = "拆分法向"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.ops.mesh.split_normals()
        return {'FINISHED'}

class BUTTON_ACTION_OT_meshedit_edit_mesh_normals_average(bpy.types.Operator):
    bl_idname = "button.action_meshedit_edit_mesh_normals_average"
    bl_label = "平均法向"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.ops.wm.call_menu(name="VIEW3D_MT_edit_mesh_normals_average")
        return {'FINISHED'}

class BUTTON_ACTION_OT_meshedit_edit_mesh_shading(bpy.types.Operator):
    bl_idname = "button.action_meshedit_edit_mesh_shading"
    bl_label = "着色方式"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.ops.wm.call_menu(name="VIEW3D_MT_edit_mesh_shading")
        return {'FINISHED'}

class BUTTON_ACTION_OT_meshedit_edit_mesh_weights(bpy.types.Operator):
    bl_idname = "button.action_meshedit_edit_mesh_weights"
    bl_label = "权重"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.ops.wm.call_menu(name="VIEW3D_MT_edit_mesh_weights")
        return {'FINISHED'}
    
class BUTTON_ACTION_OT_meshedit_attribute_set(bpy.types.Operator):
    bl_idname = "button.action_meshedit_attribute_set"
    bl_label = "设置属性"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.ops.mesh.attribute_set('INVOKE_DEFAULT')
        return {'FINISHED'}

class BUTTON_ACTION_OT_meshedit_sort_elements(bpy.types.Operator):
    bl_idname = "button.action_meshedit_sort_elements"
    bl_label = "网格元素排序"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.ops.mesh.sort_elements('INVOKE_DEFAULT')
        return {'FINISHED'}

class BUTTON_ACTION_OT_meshedit_edit_mesh_clean(bpy.types.Operator):
    bl_idname = "button.action_meshedit_edit_mesh_clean"
    bl_label = "清理"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.ops.wm.call_menu(name="VIEW3D_MT_edit_mesh_clean")
        return {'FINISHED'}

# “顶点”菜单
class BUTTON_ACTION_OT_meshedit_extrude_vertices_move(bpy.types.Operator):
    bl_idname = "button.action_meshedit_extrude_vertices_move"
    bl_label = "挤出顶点"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.ops.mesh.extrude_vertices_move('INVOKE_DEFAULT')
        return {'FINISHED'}

class BUTTON_ACTION_OT_meshedit_bevel_vertices(bpy.types.Operator):
    bl_idname = "button.action_meshedit_bevel_vertices"
    bl_label = "点倒角"
    bl_description = "快捷键 Ctrl Shift B"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.ops.mesh.bevel('INVOKE_DEFAULT',affect='VERTICES')
        return {'FINISHED'}
    
class BUTTON_ACTION_OT_meshedit_bevel_edges(bpy.types.Operator):
    bl_idname = "button.action_meshedit_bevel_edges"
    bl_label = "边倒角"
    bl_description = "快捷键 Ctrl B"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.ops.mesh.bevel('INVOKE_DEFAULT',affect='EDGES')
        return {'FINISHED'}

class BUTTON_ACTION_OT_meshedit_edge_face_add(bpy.types.Operator):
    bl_idname = "button.action_meshedit_edge_face_add"
    bl_label = "从顶点创建边/面"
    bl_description = "快捷键 F"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.ops.mesh.edge_face_add()
        return {'FINISHED'}
    
class BUTTON_ACTION_OT_meshedit_vert_connect_path(bpy.types.Operator):
    bl_idname = "button.action_meshedit_vert_connect_path"
    bl_label = "连接顶点路径"
    bl_description = "快捷键 J"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.ops.mesh.vert_connect_path()
        return {'FINISHED'}
    
class BUTTON_ACTION_OT_meshedit_vert_connect(bpy.types.Operator):
    bl_idname = "button.action_meshedit_vert_connect"
    bl_label = "连接顶点对"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.ops.mesh.vert_connect()
        return {'FINISHED'}
    
class BUTTON_ACTION_OT_meshedit_rip_move(bpy.types.Operator):
    bl_idname = "button.action_meshedit_rip_move"
    bl_label = "断离顶点"
    bl_description = "快捷键 V"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        obj = context.edit_object
        if not obj or obj.type != 'MESH':
            return False

        bm = bmesh.from_edit_mesh(bpy.context.edit_object.data)
        bm.verts.ensure_lookup_table()
        bm.edges.ensure_lookup_table()

        selected_verts = [v for v in bm.verts if v.select]
        if len(selected_verts) != 1:
            return False

        v = selected_verts[0]
        if len(v.link_edges) < 3:
            return False

        return True

    def execute(self, context):
        bpy.ops.mesh.rip_move('INVOKE_DEFAULT')
        return {'FINISHED'}
    
class BUTTON_ACTION_OT_meshedit_rip_move_fill(bpy.types.Operator):
    bl_idname = "button.action_meshedit_rip_move_fill"
    bl_label = "断离顶点并填充"
    bl_description = "快捷键 Alt V"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        obj = context.edit_object
        if not obj or obj.type != 'MESH':
            return False

        bm = bmesh.from_edit_mesh(bpy.context.edit_object.data)
        bm.verts.ensure_lookup_table()
        bm.edges.ensure_lookup_table()

        selected_verts = [v for v in bm.verts if v.select]
        if len(selected_verts) != 1:
            return False

        v = selected_verts[0]
        if len(v.link_edges) < 3:
            return False

        return True

    def execute(self, context):
        bpy.ops.mesh.rip_move('INVOKE_DEFAULT', MESH_OT_rip={"use_fill":True})
        return {'FINISHED'}
    
class BUTTON_ACTION_OT_meshedit_rip_edge_move(bpy.types.Operator):
    bl_idname = "button.action_meshedit_rip_edge_move"
    bl_label = "断离顶点并延长"
    bl_description = "快捷键 Alt D"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.ops.mesh.rip_edge_move('INVOKE_DEFAULT')
        return {'FINISHED'}
    
class BUTTON_ACTION_OT_meshedit_transform_vert_slide(bpy.types.Operator):
    bl_idname = "button.action_meshedit_transform_vert_slide"
    bl_label = "滑移顶点"
    bl_description = "快捷键 Shift V"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.ops.transform.vert_slide('INVOKE_DEFAULT')
        return {'FINISHED'}
    
class BUTTON_ACTION_OT_meshedit_vertices_smooth(bpy.types.Operator):
    bl_idname = "button.action_meshedit_vertices_smooth"
    bl_label = "平滑顶点"
    bl_options = {'REGISTER', 'UNDO'}

    factor: bpy.props.FloatProperty(
        name="",
        default=0.0,
        min=-10.0,
        max=10.0,
        soft_min=1,
        soft_max=1,
        subtype="FACTOR",
        precision=3,
    )

    repeat: bpy.props.IntProperty(
        name="",
        default=1,
        min=1,
        max=1000,
        soft_max=100,
    )

    xaxis: bpy.props.BoolProperty(
        name="X 轴",
        description="Smooth along the X axis",
        default=True
    )

    yaxis: bpy.props.BoolProperty(
        name="Y 轴",
        description="Smooth along the Y axis",
        default=True
    )

    zaxis: bpy.props.BoolProperty(
        name="Z 轴",
        description="Smooth along the Z axis",
        default=True
    )

    def invoke(self, context, event):
        return self.execute(context)

    def draw(self, context):
        layout = self.layout
        split = layout.row().split(factor=0.4)

        col_left = split.column()
        col_left.alignment = 'RIGHT'
        col_left.label(text="平滑")
        col_left.label(text="重复")
        col_left.label(text="")
        col_left.label(text="")
        col_left.label(text="")

        col_right = split.column()
        col_right.prop(self, "factor")
        col_right.prop(self, "repeat")
        col_right.prop(self, "xaxis")
        col_right.prop(self, "yaxis")
        col_right.prop(self, "zaxis")


    def execute(self, context):
        bpy.ops.mesh.vertices_smooth(
        factor=self.factor,
        repeat=self.repeat,
        xaxis=self.xaxis,
        yaxis=self.yaxis,
        zaxis=self.zaxis,
        )
        return {'FINISHED'}
    
class BUTTON_ACTION_OT_meshedit_vertices_smooth_laplacian(bpy.types.Operator):
    bl_idname = "button.action_meshedit_vertices_smooth_laplacian"
    bl_label = "拉普拉斯平滑顶点"
    bl_options = {'REGISTER', 'UNDO'}

    repeat: bpy.props.IntProperty(
        name="",
        default=1,
        min=1,
        max=1000,
        soft_max=200,
    )

    lambda_factor: bpy.props.FloatProperty(
        name="",
        default=1.0,
        min=0,
        max=1000.0,
        precision=3
    )

    lambda_border: bpy.props.FloatProperty(
        name="",
        default=5e-5,
        min=0,
        max=1000.0,
        precision=3
    )

    use_x: bpy.props.BoolProperty(
        name="X 轴向平滑",
        default=True
    )

    use_y: bpy.props.BoolProperty(
        name="Y 轴向平滑",
        default=True
    )

    use_z: bpy.props.BoolProperty(
        name="Z 轴向平滑",
        default=True
    )

    preserve_volume: bpy.props.BoolProperty(
        name="维持体积",
        default=True
    )

    def invoke(self, context, event):
        return self.execute(context)

    def draw(self, context):
        layout = self.layout
        split = layout.row().split(factor=0.5)

        col_left = split.column()
        col_left.alignment = 'RIGHT'
        col_left.label(text="网格光滑次数")
        col_left.label(text="Lambda 系数")
        col_left.label(text="边界内的Lambda 系数")
        col_left.label(text="")
        col_left.label(text="")
        col_left.label(text="")
        col_left.label(text="")

        col_right = split.column()
        col_right.prop(self, "repeat")
        col_right.prop(self, "lambda_factor")
        col_right.prop(self, "lambda_border")
        col_right.prop(self, "use_x")
        col_right.prop(self, "use_y")
        col_right.prop(self, "use_z")
        col_right.prop(self, "preserve_volume")

    def execute(self, context):
        bpy.ops.mesh.vertices_smooth_laplacian(
            repeat=self.repeat,
            lambda_factor=self.lambda_factor,
            lambda_border=self.lambda_border,
            use_x=self.use_x,
            use_y=self.use_y,
            use_z=self.use_z,
            preserve_volume=self.preserve_volume
        )
        return {'FINISHED'}
    
class BUTTON_ACTION_OT_meshedit_transform_vert_crease(bpy.types.Operator):
    bl_idname = "button.action_meshedit_transform_vert_crease"
    bl_label = "顶点折痕"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.ops.transform.vert_crease('INVOKE_DEFAULT')
        return {'FINISHED'}
    
def shape_key_items(self, context):
    items = []
    obj = context.object

    if obj and obj.type == 'MESH' and obj.data.shape_keys:
        for i, key in enumerate(obj.data.shape_keys.key_blocks):
            items.append((
                key.name,     # name（返回值）
                key.name,     # label（显示值，保持英文原样）
                "",           # description
                'SHAPEKEY_DATA',  # 图标
                i             # index
            ))
    else:
        items.append(("", "None", "No shape keys available", 'ERROR', 0))

    return items
    
class BUTTON_ACTION_OT_meshedit_blend_from_shape(bpy.types.Operator):
    bl_idname = "button.action_meshedit_blend_from_shape"
    bl_label = "从形状混合"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):        
        if not context.active_object.data.shape_keys or len(context.active_object.data.shape_keys.key_blocks) == 0:
            return False

        bm = bmesh.from_edit_mesh(context.active_object.data)
        if not any(v.select for v in bm.verts) and not any(e.select for e in bm.edges) and not any(f.select for f in bm.faces):
            return False

        return True

    shape: bpy.props.EnumProperty(
        name="",
        items=shape_key_items,
    )

    blend: bpy.props.FloatProperty(
        name="",
        default=1.0,
        min=-1000.0,
        soft_min=-2,
        max=1000.0,
        soft_max=2,
        precision=3,
    )

    add: bpy.props.BoolProperty(
        name="相加",
        default=True
    )

    def invoke(self, context, event):
        return self.execute(context)

    def draw(self, context):
        layout = self.layout
        split = layout.row().split(factor=0.4)

        col_left = split.column()
        col_left.alignment = 'RIGHT'
        col_left.label(text="形状")
        col_left.label(text="混合")
        col_left.label(text="")

        col_right = split.column()
        col_right.prop(self, "shape")
        col_right.prop(self, "blend")
        col_right.prop(self, "add")

    def execute(self, context):
        bpy.ops.mesh.blend_from_shape(shape=self.shape, blend=self.blend, add=self.add)
        return {'FINISHED'}
    
class BUTTON_ACTION_OT_meshedit_shape_propagate_to_all(bpy.types.Operator):
    bl_idname = "button.action_meshedit_shape_propagate_to_all"
    bl_label = "传递到形状"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):        
        if not context.active_object.data.shape_keys or len(context.active_object.data.shape_keys.key_blocks) == 0:
            return False

        bm = bmesh.from_edit_mesh(context.active_object.data)
        if not any(v.select for v in bm.verts) and not any(e.select for e in bm.edges) and not any(f.select for f in bm.faces):
            return False

        return True

    def execute(self, context):
        bpy.ops.mesh.shape_propagate_to_all()
        return {'FINISHED'}
    
class BUTTON_ACTION_OT_meshedit_vertex_group_menu(bpy.types.Operator):
    bl_idname = "button.action_meshedit_vertex_group_menu"
    bl_label = "顶点组"
    bl_description = "快捷键 Ctrl G"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.ops.wm.call_menu(name="VIEW3D_MT_vertex_group")
        return {'FINISHED'}
    
class BUTTON_ACTION_OT_meshedit_hook_menu(bpy.types.Operator):
    bl_idname = "button.action_meshedit_hook_menu"
    bl_label = "钩挂"
    bl_description = "快捷键 Ctrl H"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.ops.wm.call_menu(name="VIEW3D_MT_hook")
        return {'FINISHED'}
    
class BUTTON_ACTION_OT_meshedit_vertex_parent_set(bpy.types.Operator):
    bl_idname = "button.action_meshedit_vertex_parent_set"
    bl_label = "创建父级顶点"
    bl_description = "快捷键 Ctrl P"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.ops.object.vertex_parent_set('INVOKE_DEFAULT')
        return {'FINISHED'}

# “边”菜单
class BUTTON_ACTION_OT_meshedit_extrude_edges_move(bpy.types.Operator):
    bl_idname = "button.action_meshedit_extrude_edges_move"
    bl_label = "挤出边线"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.ops.mesh.extrude_edges_move('INVOKE_DEFAULT')
        return {'FINISHED'}
    
class BUTTON_ACTION_OT_meshedit_bridge_edge_loops(bpy.types.Operator):
    bl_idname = "button.action_meshedit_bridge_edge_loops"
    bl_label = "桥接循环边"
    bl_options = {'REGISTER', 'UNDO'}

    type: bpy.props.EnumProperty(
        name="",
        items=[
            ('SINGLE', "开放循环", ""),
            ('CLOSED', "闭合循环", ""),
            ('PAIRS', "循环对", ""),
        ],
        default='SINGLE',
    )

    use_merge: bpy.props.BoolProperty(
        name="合并",
        default=False,
    )

    merge_factor: bpy.props.FloatProperty(
        name="",
        default=0.5,
        min=0.0,
        max=1.0,
        precision=3,
    )

    twist_offset: bpy.props.IntProperty(
        name="",
        default=0,
        min=-1000,
        max=1000,
    )

    number_cuts: bpy.props.IntProperty(
        name="",
        default=0,
        min=0,
        max=1000,
        soft_max=64,
    )

    interpolation: bpy.props.EnumProperty(
        name="",
        items=[
            ('LINEAR', "线性", ""),
            ('PATH', "混合路径", ""),
            ('SURFACE', "混合曲面", ""),
        ],
        default='PATH',
    )

    smoothness: bpy.props.FloatProperty(
        name="",
        default=1.0,
        min=0.0,
        max=1000.0,
        soft_max=2,
        precision=3,
    )

    profile_shape_factor: bpy.props.FloatProperty(
        name="",
        default=0.0,
        min=-1000.0,
        soft_min=-2,
        max=1000.0,
        soft_max=2,
        precision=3,
    )

    profile_shape: bpy.props.EnumProperty(
        name="",
        items=[
            ('SMOOTH', "平滑", "", 'SMOOTHCURVE', 0),
            ('SPHERE', "球状", "", 'SPHERECURVE', 1),
            ('ROOT', "根凸", "", 'ROOTCURVE', 2),
            ('INVERSE_SQUARE', "平方反比", "", 'INVERSESQUARECURVE', 3),
            ('SHARP', "锐利", "", 'SHARPCURVE', 4),
            ('LINEAR', "线性", "", 'LINCURVE', 5),
        ],
        default='SMOOTH',
    )
    
    def invoke(self, context, event):
        return self.execute(context)

    def draw(self, context):
        layout = self.layout
        split = layout.row().split(factor=0.4)

        col_left = split.column()
        col_left.alignment = 'RIGHT'
        col_left.label(text="连接多个循环")
        col_left.label(text="")
        col_left.label(text="合并系数")
        col_left.label(text="扭曲")
        col_left.label(text="切割次数")
        col_left.label(text="插值类型")
        col_left.label(text="平滑度")
        col_left.label(text="轮廓系数")
        col_left.label(text="轮廓形状")

        col_right = split.column()
        col_right.prop(self, "type")
        col_right.prop(self, "use_merge")
        col_right.prop(self, "merge_factor")
        col_right.prop(self, "twist_offset")
        col_right.prop(self, "number_cuts")
        col_right.prop(self, "interpolation")
        col_right.prop(self, "smoothness")
        col_right.prop(self, "profile_shape_factor")
        col_right.prop(self, "profile_shape")

    def execute(self, context):
        bpy.ops.mesh.bridge_edge_loops(
            type=self.type,
            use_merge=self.use_merge,
            merge_factor=self.merge_factor,
            twist_offset=self.twist_offset,
            number_cuts=self.number_cuts,
            interpolation=self.interpolation,
            smoothness=self.smoothness,
            profile_shape_factor=self.profile_shape_factor,
            profile_shape=self.profile_shape,
        )
        return {'FINISHED'}

class BUTTON_ACTION_OT_meshedit_subdivide_edgering(bpy.types.Operator):
    bl_idname = "button.action_meshedit_subdivide_edgering"
    bl_label = "细分并排边"
    bl_options = {'REGISTER', 'UNDO'}

    number_cuts: bpy.props.IntProperty(
        name="",
        default=10,
        min=0,
        max=1000,
        soft_max=64,
    )

    interpolation: bpy.props.EnumProperty(
        name="",
        items=[
            ('LINEAR', "线性", ""),
            ('PATH', "混合路径", ""),
            ('SURFACE', "混合曲面", ""),
        ],
        default='PATH',
    )

    smoothness: bpy.props.FloatProperty(
        name="",
        default=1.0,
        min=0.0,
        max=1000.0,
        soft_max=2,
        precision=3,
    )

    profile_shape_factor: bpy.props.FloatProperty(
        name="",
        default=0.0,
        min=-1000.0,
        soft_min=-2,
        max=1000.0,
        soft_max=2,
        precision=3,
    )

    profile_shape: bpy.props.EnumProperty(
        name="",
        items=[
            ('SMOOTH', "平滑", "", 'SMOOTHCURVE', 0),
            ('SPHERE', "球状", "", 'SPHERECURVE', 1),
            ('ROOT', "根凸", "", 'ROOTCURVE', 2),
            ('INVERSE_SQUARE', "平方反比", "", 'INVERSESQUARECURVE', 3),
            ('SHARP', "锐利", "", 'SHARPCURVE', 4),
            ('LINEAR', "线性", "", 'LINCURVE', 5),
        ],
        default='SMOOTH',
    )
    
    def invoke(self, context, event):
        return self.execute(context)

    def draw(self, context):
        layout = self.layout
        split = layout.row().split(factor=0.4)

        col_left = split.column()
        col_left.alignment = 'RIGHT'
        col_left.label(text="切割次数")
        col_left.label(text="插值类型")
        col_left.label(text="平滑度")
        col_left.label(text="轮廓系数")
        col_left.label(text="轮廓形状")

        col_right = split.column()
        col_right.prop(self, "number_cuts")
        col_right.prop(self, "interpolation")
        col_right.prop(self, "smoothness")
        col_right.prop(self, "profile_shape_factor")
        col_right.prop(self, "profile_shape")
    
    def execute(self, context):
        bpy.ops.mesh.subdivide_edgering(
            number_cuts=self.number_cuts,
            interpolation=self.interpolation,
            smoothness=self.smoothness,
            profile_shape_factor=self.profile_shape_factor,
            profile_shape=self.profile_shape,
        )
        return {'FINISHED'}

class BUTTON_ACTION_OT_meshedit_unsubdivide(bpy.types.Operator):
    bl_idname = "button.action_meshedit_unsubdivide"
    bl_label = "反细分"
    bl_options = {'REGISTER', 'UNDO'}

    iterations: bpy.props.IntProperty(
        name="",
        min=1,
        max=1000,
        soft_max=100,
        default=2,
    )
    
    def invoke(self, context, event):
        return self.execute(context)

    def draw(self, context):
        layout = self.layout
        split = layout.row().split(factor=0.4)

        col_left = split.column()
        col_left.alignment = 'RIGHT'
        col_left.label(text="迭代")

        col_right = split.column()
        col_right.prop(self, "iterations")

    def execute(self, context):
        bpy.ops.mesh.unsubdivide(iterations=self.iterations)
        return {'FINISHED'}

class BUTTON_ACTION_OT_meshedit_edge_rotate(bpy.types.Operator):
    bl_idname = "button.action_meshedit_edge_rotate"
    bl_label = "顺/逆时针旋转边"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        obj = context.active_object
        if not obj or obj.type != 'MESH':
            return False

        if context.mode != 'EDIT_MESH':
            return False

        bm = bmesh.from_edit_mesh(obj.data)

        # 不管处于哪种选择模式，只要有选中的面，就直接 False
        if any(f.select for f in bm.faces):
            return False

        selected_edges = {e for e in bm.edges if e.select}
        if selected_edges:
            for face in bm.faces:
                # 如果这个面所有的边都被选中了，则构成了一个完整面
                if face.edges and face.edges.issubset(selected_edges):
                    return False  # 有一个完整面 -> 不允许旋转
            return True  # 所有面都没被完整选中 -> 允许旋转

        # 检查是否选中了两个点且刚好是一条边的两端
        selected_verts = [v for v in bm.verts if v.select]
        if len(selected_verts) == 2:
            v1, v2 = selected_verts
            for e in v1.link_edges:
                if e.other_vert(v1) == v2:
                    return True

        return False

    use_ccw: bpy.props.EnumProperty(
        name="",
        items=[
            ('FALSE', "顺时针", ""),
            ('TRUE', "逆时针", ""),
        ],
        default='FALSE',
    )
    
    def invoke(self, context, event):
        return self.execute(context)

    def draw(self, context):
        layout = self.layout
        split = layout.row().split(factor=0.4)

        col_left = split.column()
        col_left.alignment = 'RIGHT'
        col_left.label(text="旋转方向")

        col_right = split.column()
        col_right.prop(self, "use_ccw", text="abc", expand=True)

    def execute(self, context):
        bpy.ops.mesh.edge_rotate(use_ccw=False if self.use_ccw == 'FALSE' else True)
        return {'FINISHED'}

class BUTTON_ACTION_OT_meshedit_transform_edge_slide(bpy.types.Operator):
    bl_idname = "button.action_meshedit_transform_edge_slide"
    bl_label = "滑移边线"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.ops.transform.edge_slide('INVOKE_DEFAULT')
        return {'FINISHED'}

class BUTTON_ACTION_OT_meshedit_loopcut_slide(bpy.types.Operator):
    bl_idname = "button.action_meshedit_loopcut_slide"
    bl_label = "环切并滑移"
    bl_description = "快捷键 Ctrl R"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.ops.mesh.loopcut_slide('INVOKE_DEFAULT')
        return {'FINISHED'}
    
class BUTTON_ACTION_OT_meshedit_offset_edge_loops_slide(bpy.types.Operator):
    bl_idname = "button.action_meshedit_offset_edge_loops_slide"
    bl_label = "偏移边线并滑移"
    bl_description = "快捷键 Ctrl Shift R"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.ops.mesh.offset_edge_loops_slide('INVOKE_DEFAULT')
        return {'FINISHED'}
    
class BUTTON_ACTION_OT_meshedit_transform_edge_crease(bpy.types.Operator):
    bl_idname = "button.action_meshedit_transform_edge_crease"
    bl_label = "边线折痕"
    bl_description = "快捷键 Shift E"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.ops.transform.edge_crease('INVOKE_DEFAULT')
        return {'FINISHED'}

class BUTTON_ACTION_OT_meshedit_transform_edge_bevelweight(bpy.types.Operator):
    bl_idname = "button.action_meshedit_transform_edge_bevelweight"
    bl_label = "倒角边权重"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.ops.transform.edge_bevelweight('INVOKE_DEFAULT')
        return {'FINISHED'}

class BUTTON_ACTION_OT_meshedit_mesh_mark_seam_toggle(bpy.types.Operator):
    bl_idname = "button.action_meshedit_mesh_mark_seam_toggle"
    bl_label = "缝合边"
    bl_description = "标记缝合边/清除缝合边二合一"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bm = bmesh.from_edit_mesh(context.active_object.data)
        has_seam = any(e.select and e.seam for e in bm.edges)
        bpy.ops.mesh.mark_seam(clear=has_seam)
        return {'FINISHED'}

class BUTTON_ACTION_OT_meshedit_mesh_mark_sharp_toggle(bpy.types.Operator):
    bl_idname = "button.action_meshedit_mesh_mark_sharp_toggle"
    bl_label = "标记/清除锐边"
    bl_description = "标记缝合边/清除缝合边二合一"
    bl_options = {'REGISTER', 'UNDO'}

    use_verts: bpy.props.BoolProperty(
        name="",
        default=False,
    )

    def invoke(self, context, event):
        return self.execute(context)

    def draw(self, context):
        bm = bmesh.from_edit_mesh(context.active_object.data)
        has_sharp = any(e.select and not e.smooth for e in bm.edges)

        layout = self.layout
        split = layout.row().split(factor=0.6)

        col_left = split.column()
        col_left.alignment = 'RIGHT'
        col_left.label(text="标记锐边顶点" if has_sharp else "清除锐边顶点")

        col_right = split.column()
        col_right.prop(self, "use_verts")

    def execute(self, context):
        bm = bmesh.from_edit_mesh(context.active_object.data)
        has_sharp = any(e.select and not e.smooth for e in bm.edges)
        bpy.ops.mesh.mark_sharp(clear=has_sharp, use_verts=self.use_verts)
        return {'FINISHED'}

class BUTTON_ACTION_OT_meshedit_mesh_set_sharpness_by_angle(bpy.types.Operator):
    bl_idname = "button.action_meshedit_mesh_set_sharpness_by_angle"
    bl_label = "按角度设置锐边"
    bl_options = {'REGISTER', 'UNDO'}

    angle: bpy.props.FloatProperty(
        name="",
        default=0.523599,  
        min=0.000174533,  
        soft_min=0.0174533, 
        max=3.14159,       
        subtype='ANGLE',  
        unit='ROTATION',
    )

    extend: bpy.props.BoolProperty(
        name="扩展",
        default=False,
    )

    def invoke(self, context, event):
        return self.execute(context)

    def draw(self, context):
        layout = self.layout
        split = layout.row().split(factor=0.4)

        col_left = split.column()
        col_left.alignment = 'RIGHT'
        col_left.label(text="角度")
        col_left.label(text="")

        col_right = split.column()
        col_right.prop(self, "angle")
        col_right.prop(self, "extend")

    def execute(self, context):
        bpy.ops.mesh.set_sharpness_by_angle(angle=self.angle, extend=self.extend)
        return {'FINISHED'}

class BUTTON_ACTION_OT_meshedit_mesh_mark_freestyle_edge_clear_false(bpy.types.Operator):
    bl_idname = "button.action_meshedit_mesh_mark_freestyle_edge_clear_false"
    bl_label = "标记Freestyle边"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.ops.mesh.mark_freestyle_edge(clear=False)
        return {'FINISHED'}

class BUTTON_ACTION_OT_meshedit_mesh_mark_freestyle_edge_clear_true(bpy.types.Operator):
    bl_idname = "button.action_meshedit_mesh_mark_freestyle_edge_clear_true"
    bl_label = "清除Freestyle边"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.ops.mesh.mark_freestyle_edge(clear=True)
        return {'FINISHED'}





classes = (
    BUTTON_ACTION_OT_mesh_select_nth,
    BUTTON_ACTION_OT_mesh_edges_select_sharp,
    BUTTON_ACTION_OT_mesh_select_by_trait,
    BUTTON_ACTION_OT_mesh_call_select_by_trait,
    BUTTON_ACTION_OT_mesh_select_loops,
    BUTTON_ACTION_OT_call_mesh_select_loops,
    BUTTON_ACTION_OT_mesh_select_axis,

    BUTTON_ACTION_OT_meshedit_transform_shrink_fatten,
    BUTTON_ACTION_OT_meshedit_transform_skin_resize,

    BUTTON_ACTION_OT_meshedit_edit_mesh_extrude_menu,
    BUTTON_ACTION_OT_meshedit_edit_mesh_merge_menu,
    BUTTON_ACTION_OT_meshedit_edit_mesh_split_menu,
    BUTTON_ACTION_OT_meshedit_mesh_separate,
    BUTTON_ACTION_OT_meshedit_mesh_bisect,
    BUTTON_ACTION_OT_meshedit_mesh_knife_project,
    BUTTON_ACTION_OT_meshedit_mesh_knife_tool,
    BUTTON_ACTION_OT_meshedit_mesh_convex_hull,
    BUTTON_ACTION_OT_meshedit_mesh_symmetrize,
    BUTTON_ACTION_OT_meshedit_mesh_symmetry_snap,

    BUTTON_ACTION_OT_meshedit_edit_mesh_normals_menu,
    BUTTON_ACTION_OT_meshedit_flip_normals,
    BUTTON_ACTION_OT_meshedit_normals_make_consistent,
    BUTTON_ACTION_OT_meshedit_set_normals_from_faces,
    BUTTON_ACTION_OT_meshedit_transform_rotate_normal,
    BUTTON_ACTION_OT_meshedit_point_normals,
    BUTTON_ACTION_OT_meshedit_merge_normals,
    BUTTON_ACTION_OT_meshedit_split_normals,
    BUTTON_ACTION_OT_meshedit_edit_mesh_normals_average,

    BUTTON_ACTION_OT_meshedit_edit_mesh_shading,
    BUTTON_ACTION_OT_meshedit_edit_mesh_weights,
    BUTTON_ACTION_OT_meshedit_attribute_set,
    BUTTON_ACTION_OT_meshedit_sort_elements,
    BUTTON_ACTION_OT_meshedit_edit_mesh_clean,

    BUTTON_ACTION_OT_meshedit_extrude_vertices_move,
    BUTTON_ACTION_OT_meshedit_bevel_vertices,
    BUTTON_ACTION_OT_meshedit_bevel_edges,
    BUTTON_ACTION_OT_meshedit_edge_face_add,
    BUTTON_ACTION_OT_meshedit_vert_connect_path,
    BUTTON_ACTION_OT_meshedit_vert_connect,
    BUTTON_ACTION_OT_meshedit_rip_move,
    BUTTON_ACTION_OT_meshedit_rip_move_fill,
    BUTTON_ACTION_OT_meshedit_rip_edge_move,
    BUTTON_ACTION_OT_meshedit_transform_vert_slide,
    BUTTON_ACTION_OT_meshedit_vertices_smooth,
    BUTTON_ACTION_OT_meshedit_vertices_smooth_laplacian,
    BUTTON_ACTION_OT_meshedit_transform_vert_crease,
    BUTTON_ACTION_OT_meshedit_blend_from_shape,
    BUTTON_ACTION_OT_meshedit_shape_propagate_to_all,
    BUTTON_ACTION_OT_meshedit_vertex_group_menu,
    BUTTON_ACTION_OT_meshedit_hook_menu,
    BUTTON_ACTION_OT_meshedit_vertex_parent_set,
    BUTTON_ACTION_OT_meshedit_extrude_edges_move,
    BUTTON_ACTION_OT_meshedit_bridge_edge_loops,

    BUTTON_ACTION_OT_meshedit_subdivide_edgering,
    BUTTON_ACTION_OT_meshedit_unsubdivide,
    BUTTON_ACTION_OT_meshedit_edge_rotate,
    BUTTON_ACTION_OT_meshedit_transform_edge_slide,
    BUTTON_ACTION_OT_meshedit_loopcut_slide,
    BUTTON_ACTION_OT_meshedit_offset_edge_loops_slide,
    BUTTON_ACTION_OT_meshedit_transform_edge_crease,
    BUTTON_ACTION_OT_meshedit_transform_edge_bevelweight,
    BUTTON_ACTION_OT_meshedit_mesh_mark_seam_toggle,
    BUTTON_ACTION_OT_meshedit_mesh_mark_sharp_toggle,
    BUTTON_ACTION_OT_meshedit_mesh_set_sharpness_by_angle,
    BUTTON_ACTION_OT_meshedit_mesh_mark_freestyle_edge_clear_false,
    BUTTON_ACTION_OT_meshedit_mesh_mark_freestyle_edge_clear_true,

)

def register():
    for cls in classes:
        bpy.utils.register_class(cls)

def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)