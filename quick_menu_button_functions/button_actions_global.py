# 这里只包含使用快捷键的功能：
import bpy
from ..show_switch_notice import show_notice

# 全局“视图”菜单功能
class BUTTON_ACTION_OT_global_view_selected(bpy.types.Operator):
    bl_idname = "button.action_global_view_selected"
    bl_label = "框选所选"
    bl_description = "快捷键 ."
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.ops.view3d.view_selected('INVOKE_DEFAULT')
        return {'FINISHED'}
    
class BUTTON_ACTION_OT_global_view_all(bpy.types.Operator):
    bl_idname = "button.action_global_view_all"
    bl_label = "框选全部"
    bl_description = "快捷键 Home"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.ops.view3d.view_all('INVOKE_DEFAULT')
        return {'FINISHED'}
    
class BUTTON_ACTION_OT_global_localview(bpy.types.Operator):
    bl_idname = "button.action_global_localview"
    bl_label = "切换局部视图"
    bl_description = "快捷键 /"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.ops.view3d.localview('INVOKE_DEFAULT')
        return {'FINISHED'}
    
class BUTTON_ACTION_OT_global_object_as_camera(bpy.types.Operator):
    bl_idname = "button.action_global_object_as_camera"
    bl_label = "设置活动物体为摄像机"
    bl_description = "快捷键 Ctrl Num_0"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.ops.view3d.object_as_camera('INVOKE_DEFAULT')
        return {'FINISHED'}
    
class BUTTON_ACTION_OT_global_view_center_camera(bpy.types.Operator):
    bl_idname = "button.action_global_view_center_camera"
    bl_label = "摄像机边界框"
    bl_description = "快捷键 Home"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.ops.view3d.view_center_camera('INVOKE_DEFAULT')
        return {'FINISHED'}
    
class BUTTON_ACTION_OT_global_view_viewpoint_menu(bpy.types.Operator):
    bl_idname = "button.action_global_view_viewpoint_menu"
    bl_label = "视图"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        return {'FINISHED'}

    def invoke(self, context, event):
        return context.window_manager.invoke_popup(self, width=80)

    def draw(self, context):
        layout = self.layout
        row = layout.row()
        col = row.column(align=True)
        col.label(text="视图", icon='PRESET')
        col.operator("view3d.view_camera", text="摄像机", icon="OUTLINER_DATA_CAMERA")
        col.separator()
        col.operator("view3d.view_axis", text="顶视图", icon="RADIOBUT_OFF").type='TOP'
        col.operator("view3d.view_axis", text="底视图", icon="RADIOBUT_OFF").type='BOTTOM'
        col.separator()
        col.operator("view3d.view_axis", text="前视图", icon="RADIOBUT_OFF").type='FRONT'
        col.operator("view3d.view_axis", text="后视图", icon="RADIOBUT_OFF").type='BACK'
        col.separator()
        col.operator("view3d.view_axis", text="右视图", icon="RADIOBUT_OFF").type='RIGHT'
        col.operator("view3d.view_axis", text="左视图", icon="RADIOBUT_OFF").type='LEFT'

# 唤出"视图“菜单类
class BUTTON_ACTION_OT_global_call_view_viewpoint_menu(bpy.types.Operator):
    bl_idname = "button.action_global_call_view_viewpoint_menu"
    bl_label = "视图"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.ops.button.action_global_view_viewpoint_menu('INVOKE_DEFAULT')
        return {'FINISHED'}

class BUTTON_ACTION_OT_global_view_navigation_menu(bpy.types.Operator):
    bl_idname = "button.action_global_view_navigation_menu"
    bl_label = "视图切换"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        return {'FINISHED'}

    def invoke(self, context, event):
        return context.window_manager.invoke_popup(self, width=100)

    def draw(self, context):
        layout = self.layout
        row = layout.row()
        col = row.column(align=True)
        col.label(text="视图切换", icon='PRESET')
        col.operator("view3d.view_orbit", text="视轨左滚", icon="RADIOBUT_OFF").type='ORBITLEFT'
        col.operator("view3d.view_orbit", text="视轨右滚", icon="RADIOBUT_OFF").type='ORBITRIGHT'
        col.operator("view3d.view_orbit", text="视轨上滚", icon="RADIOBUT_OFF").type='ORBITUP'
        col.operator("view3d.view_orbit", text="视轨下滚", icon="RADIOBUT_OFF").type='ORBITDOWN'
        op = col.operator("view3d.view_orbit", text="相对视轨", icon="RADIOBUT_OFF")
        op.angle=3.14159
        op.type='ORBITRIGHT'
        col.separator()
        col.operator("view3d.view_roll", text="左倾", icon="RADIOBUT_OFF").type='LEFT'
        col.operator("view3d.view_roll", text="右倾", icon="RADIOBUT_OFF").type='RIGHT'
        col.separator()
        col.operator("view3d.view_pan", text="左平移", icon="RADIOBUT_OFF").type='PANLEFT'
        col.operator("view3d.view_pan", text="右平移", icon="RADIOBUT_OFF").type='PANRIGHT'
        col.operator("view3d.view_pan", text="上平移", icon="RADIOBUT_OFF").type='PANUP'
        col.operator("view3d.view_pan", text="下平移", icon="RADIOBUT_OFF").type='PANDOWN'
        col.separator()
        col.operator("view3d.zoom", text="视图放大", icon="RADIOBUT_OFF").delta=1
        col.operator("view3d.zoom", text="视图缩小", icon="RADIOBUT_OFF").delta=-1
        col.operator("view3d.zoom_border", text="框选放大", icon="RADIOBUT_OFF")
        col.operator("view3d.dolly", text="滑动视图", icon="RADIOBUT_OFF")
        col.operator("view3d.zoom_camera_1_to_1", text="1:1缩放摄像机视图", icon="RADIOBUT_OFF")
        col.separator()
        col.operator("view3d.fly", text="飞行漫游模式", icon="RADIOBUT_OFF")
        col.operator("view3d.walk", text="行走漫游", icon="RADIOBUT_OFF")

# 唤出“视图切换”菜单类
class BUTTON_ACTION_OT_global_call_view_navigation_menu(bpy.types.Operator):
    bl_idname = "button.action_global_call_view_navigation_menu"
    bl_label = "视图切换"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.ops.button.action_global_view_navigation_menu('INVOKE_DEFAULT')
        return {'FINISHED'}
    
# 自定义“框选放大”操作类
class BUTTON_ACTION_OT_global_zoom_border(bpy.types.Operator):
    bl_idname = "button.action_global_zoom_border"
    bl_label = "框选放大"
    bl_description = "快捷键 Shift B"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        bpy.ops.view3d.zoom_border('INVOKE_DEFAULT')
        return {'FINISHED'}
    
class BUTTON_ACTION_OT_global_zoom_camera_1_to_1(bpy.types.Operator):
    bl_idname = "button.action_zoom_camera_1_to_1"
    bl_label = "1:1缩放摄像机视图"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        # 确保当前区域是 3D 视图并获取 RegionView3D 数据
        region_3d = getattr(context.space_data, "region_3d", None)
        if region_3d:
            return region_3d.view_perspective == 'CAMERA'
        return False
    
    def execute(self, context):
        bpy.ops.view3d.zoom_camera_1_to_1()
        return {'FINISHED'}

# 自定义“行走漫步”操作类
class BUTTON_ACTION_OT_global_walk(bpy.types.Operator):
    bl_idname = "button.action_global_walk"
    bl_label = "行走漫步"
    bl_description = "快捷键 Shift `"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        bpy.ops.view3d.view_lock_clear()
        bpy.ops.view3d.walk('INVOKE_DEFAULT')
        return {'FINISHED'}
    
class BUTTON_ACTION_OT_global_fly(bpy.types.Operator):
    bl_idname = "button.action_global_fly"
    bl_label = "飞行漫游模式"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        bpy.ops.view3d.view_lock_clear()
        bpy.ops.view3d.fly('INVOKE_DEFAULT')
        return {'FINISHED'}
    
class BUTTON_ACTION_OT_global_view_align_selected_menu(bpy.types.Operator):
    bl_idname = "button.action_view_align_selected_menu"
    bl_label = "视图对齐活动项"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        return {'FINISHED'}

    def invoke(self, context, event):
        return context.window_manager.invoke_popup(self, width=100)

    def draw(self, context):
        layout = self.layout
        row = layout.row()
        col = row.column(align=True)
        col.label(text="视图对齐活动项", icon='PRESET')
        op = col.operator("view3d.view_axis", text="顶视图", icon="RADIOBUT_OFF")
        op.type = 'TOP'
        op.align_active=True
        op = col.operator("view3d.view_axis", text="底视图", icon="RADIOBUT_OFF")
        op.type = 'BOTTOM'
        op.align_active=True
        col.separator()
        op = col.operator("view3d.view_axis", text="前视图", icon="RADIOBUT_OFF")
        op.type = 'FRONT'
        op.align_active=True
        op = col.operator("view3d.view_axis", text="后视图", icon="RADIOBUT_OFF")
        op.type = 'BACK'
        op.align_active=True
        col.separator()
        op = col.operator("view3d.view_axis", text="左视图", icon="RADIOBUT_OFF")
        op.type = 'RIGHT'
        op.align_active=True
        op = col.operator("view3d.view_axis", text="右视图", icon="RADIOBUT_OFF")
        op.type = 'LEFT'
        op.align_active=True

class BUTTON_ACTION_OT_global_call_view_align_selected_menu(bpy.types.Operator):
    bl_idname = "button.action_global_call_view_align_selected_menu"
    bl_label = "视图对齐活动项"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.ops.button.action_view_align_selected_menu('INVOKE_DEFAULT')
        return {'FINISHED'}

# 自定义“锁定/解锁视图至活动物体”按钮类
class BUTTON_ACTION_OT_global_lock_to_active_or_lock_clear(bpy.types.Operator):
    bl_idname = "button.action_global_lock_to_active_or_lock_clear"
    bl_label = "锁定/解锁视图"
    bl_description = "锁定视图至活动物体/消除视图锁定"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        if bpy.context.space_data.lock_object is None:
            bpy.ops.view3d.view_lock_to_active()
            show_notice("ACTIVE_LOCK.png")
        else:
            bpy.ops.view3d.view_lock_clear()
            show_notice("ACTIVE_UNLOCK.png")
        return {'FINISHED'}
    
class BUTTON_ACTION_OT_global_camera_to_view(bpy.types.Operator):
    bl_idname = "button.action_global_camera_to_view"
    bl_label = "活动摄像机对齐当前视角"
    bl_description = "Ctrl Alt Num_0"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        # 确保当前区域是 3D 视图并获取 RegionView3D 数据
        region_3d = getattr(context.space_data, "region_3d", None)
        if region_3d:
            # 如果视图透视类型正好是 CAMERA，则返回 False，使按钮灰显不可用
            return region_3d.view_perspective != 'CAMERA'  # :contentReference[oaicite:0]{index=0}
        return False

    def execute(self, context):
        bpy.ops.view3d.camera_to_view('INVOKE_DEFAULT')
        return {'FINISHED'}
    
class BUTTON_ACTION_OT_global_camera_to_view_selected(bpy.types.Operator):
    bl_idname = "button.action_global_camera_to_view_selected"
    bl_label = "活动摄像机对齐选中的物体"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        region_3d = getattr(context.space_data, "region_3d", None)
        if region_3d.view_perspective != 'CAMERA':
            bpy.ops.view3d.camera_to_view_selected()
            bpy.ops.view3d.view_camera('INVOKE_DEFAULT')
        elif region_3d.view_perspective == 'CAMERA':
            bpy.ops.view3d.view_camera('INVOKE_DEFAULT')
            bpy.ops.view3d.camera_to_view_selected()
            bpy.ops.view3d.view_camera('INVOKE_DEFAULT')
        return {'FINISHED'}

class BUTTON_ACTION_OT_global_call_view_align_menu(bpy.types.Operator):
    bl_idname = "button.action_global_call_view_align_menu"
    bl_label = "对齐视图"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.ops.wm.call_menu(name="VIEW3D_MT_view_align")
        return {'FINISHED'}
    
# 弹出“对齐视图”——游标居中并查看全部
class BUTTON_ACTION_OT_global_view_all_center_true(bpy.types.Operator):
    bl_idname = "button.action_global_view_all_center_true"
    bl_label = "游标居中并查看全部"
    bl_description = "快捷键 Shift C"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.ops.view3d.view_lock_clear()
        bpy.ops.view3d.snap_cursor_to_center()
        bpy.ops.view3d.view_all('INVOKE_DEFAULT')
        return {'FINISHED'}
    
class BUTTON_ACTION_OT_global_view_center_cursor(bpy.types.Operator):
    bl_idname = "button.action_global_view_center_cursor"
    bl_label = "视图中心对齐游标"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.ops.view3d.view_lock_clear()
        bpy.ops.view3d.view_center_cursor('INVOKE_DEFAULT')
        return {'FINISHED'}

class VIEW3D_MT_view_regions_menu(bpy.types.Menu):
    bl_idname = "button.action_global_view_regions_menu"
    bl_label = "视图框"
    bl_options = {'SEARCH_ON_KEY_PRESS'}

    def draw(self, context):
        layout = self.layout
        layout.operator("button.action_global_clip_border", text="裁剪框")
        layout.operator("button.action_global_render_border", text="渲染框")
        layout.separator()
        layout.operator("view3d.clear_render_border", text="清除渲染框")

# 弹出“视图框”菜单
class BUTTON_ACTION_OT_global_call_view_regions_menu(bpy.types.Operator):
    bl_idname = "button.action_global_call_view_regions_menu"
    bl_label = "视图框"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.ops.wm.call_menu(name="button.action_global_view_regions_menu")
        return {'FINISHED'}

# 自定义“裁剪框”操作类
class BUTTON_ACTION_OT_global_clip_border(bpy.types.Operator):
    bl_idname = "button.action_global_clip_border"
    bl_label = "裁剪框"
    bl_description = "快捷键 Alt B"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        bpy.ops.view3d.clip_border('INVOKE_DEFAULT')
        return {'FINISHED'}
    
# 自定义“渲染框”操作类
class BUTTON_ACTION_OT_global_render_border(bpy.types.Operator):
    bl_idname = "button.action_global_render_border"
    bl_label = "渲染框"
    bl_description = "快捷键 Ctrl B"
    bl_options = {'REGISTER', 'UNDO'}
    
    @staticmethod
    def render_border_active(context):
        for area in context.window.screen.areas:
            if area.type == 'VIEW_3D':
                return area.spaces.active.use_render_border
        return False

    def execute(self, context):
        if self.render_border_active(context):
            bpy.ops.view3d.clear_render_border()
        else:
            bpy.ops.view3d.render_border('INVOKE_DEFAULT')
        return {'FINISHED'}
    
class BUTTON_ACTION_OT_global_render_opengl(bpy.types.Operator):
    bl_idname = "button.action_global_render_opengl"
    bl_label = "视图渲染图像"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        bpy.ops.render.opengl('INVOKE_DEFAULT')
        return {'FINISHED'}
    
class BUTTON_ACTION_OT_global_render_opengl_animation(bpy.types.Operator):
    bl_idname = "button.action_global_render_opengl_animation"
    bl_label = "视图渲染动画"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        bpy.ops.render.opengl('INVOKE_DEFAULT', animation=True)
        return {'FINISHED'}
    
class BUTTON_ACTION_OT_global_render_opengl_keyframe(bpy.types.Operator):
    bl_idname = "button.action_global_render_opengl_keyframe"
    bl_label = "视图渲染关键帧"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        bpy.ops.render.opengl('INVOKE_DEFAULT', animation=True, render_keyed_only=True)
        return {'FINISHED'}

# 自定义“区域”菜单
class BUTTON_ACTION_OT_global_area_menu(bpy.types.Operator):
    bl_idname = "button.action_global_area_menu"
    bl_label = "区域"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        bpy.ops.wm.call_menu(name="INFO_MT_area")
        return {'FINISHED'}
    
# 自定义“区域”——切换全屏模式
class BUTTON_ACTION_OT_global_screen_screen_full_area(bpy.types.Operator):
    bl_idname = "button.action_global_screen_screen_full_area"
    bl_label = "切换全屏模式"
    bl_description = "快捷键 Ctrl Alt 空格"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        bpy.ops.screen.screen_full_area(use_hide_panels=True)
        return {'FINISHED'}
    












# “选择”菜单——全选
class BUTTON_ACTION_OT_global_select_all(bpy.types.Operator):
    bl_idname = "button.action_global_select_all"
    bl_label = "全选"
    bl_description = "快捷键 A"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        if bpy.context.mode in {"SCULPT_GPENCIL","SCULPT_GREASE_PENCIL"} and (
            not bpy.context.scene.tool_settings.use_gpencil_select_mask_point and
            not bpy.context.scene.tool_settings.use_gpencil_select_mask_stroke and
            not bpy.context.scene.tool_settings.use_gpencil_select_mask_segment):
            return False
        return True

    def execute(self, context):
        typeandmode = bpy.context.active_object.type+bpy.context.active_object.mode

        if bpy.context.mode == "OBJECT":
            bpy.ops.object.select_all(action='SELECT')
        elif typeandmode == "MESHEDIT":
            bpy.ops.mesh.select_all(action='SELECT')    
        elif typeandmode in {"MESHVERTEX_PAINT","MESHWEIGHT_PAINT","MESHTEXTURE_PAINT"}:
            bpy.ops.paint.face_select_all(action='SELECT')
        elif typeandmode in {"CURVEEDIT", "SURFACEEDIT"}:
            bpy.ops.curve.select_all(action='SELECT')
        elif typeandmode == "METAEDIT":
            bpy.ops.mball.select_all(action='SELECT')
        elif typeandmode ==  "FONTEDIT":
            bpy.ops.font.select_all()
        elif typeandmode == "LATTICEEDIT":
            bpy.ops.lattice.select_all(action='SELECT')
        elif typeandmode in {"GPENCILEDIT_GPENCIL","GPENCILVERTEX_GPENCIL","GPENCILSCULPT_GPENCIL"}:
            bpy.ops.gpencil.select_all(action='SELECT') # 4.2 版本
        elif typeandmode in { "GREASEPENCILEDIT","GREASEPENCILVERTEX_GREASE_PENCIL","GREASEPENCILSCULPT_GREASE_PENCIL"}:
            bpy.ops.grease_pencil.select_all(action='SELECT') # 4.3 版本
        elif typeandmode == "ARMATUREEDIT":
            bpy.ops.armature.select_all(action='SELECT')
        elif typeandmode == "ARMATUREPOSE":
            bpy.ops.pose.select_all(action='SELECT')
        else:
            return {'CANCELLED'}
        return {'FINISHED'}

# “选择”菜单——反选
class BUTTON_ACTION_OT_global_select_invert(bpy.types.Operator):
    bl_idname = "button.action_global_select_invert"
    bl_label = "反选"
    bl_description = "快捷键 Ctrl I"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        typeandmode = bpy.context.active_object.type+bpy.context.active_object.mode

        if bpy.context.mode == "OBJECT":
            bpy.ops.object.select_all(action='INVERT')
        elif typeandmode == "MESHEDIT":
            bpy.ops.mesh.select_all(action='INVERT')    
        elif typeandmode in {"MESHVERTEX_PAINT","MESHWEIGHT_PAINT","MESHTEXTURE_PAINT"}:
            bpy.ops.paint.face_select_all(action='INVERT')
        elif typeandmode in {"CURVEEDIT", "SURFACEEDIT"}:
            bpy.ops.curve.select_all(action='INVERT')
        elif typeandmode == "METAEDIT":
            bpy.ops.mball.select_all(action='INVERT')
        elif typeandmode == "LATTICEEDIT":
            bpy.ops.lattice.select_all(action='INVERT')
        elif typeandmode in {"GPENCILEDIT_GPENCIL","GPENCILVERTEX_GPENCIL","GPENCILSCULPT_GPENCIL"}:
            bpy.ops.gpencil.select_all(action='INVERT') # 4.2 版本
        elif typeandmode in { "GREASEPENCILEDIT","GREASEPENCILVERTEX_GREASE_PENCIL","GREASEPENCILSCULPT_GREASE_PENCIL"}:
            bpy.ops.grease_pencil.select_all(action='INVERT') # 4.3 版本
        elif typeandmode == "ARMATUREEDIT":
            bpy.ops.armature.select_all(action='INVERT')
        elif typeandmode == "ARMATUREPOSE":
            bpy.ops.pose.select_all(action='INVERT')
        else:
            return {'CANCELLED'}
        return {'FINISHED'}

# “选择”菜单——刷选
class BUTTON_ACTION_OT_global_select_circle(bpy.types.Operator):
    bl_idname = "button.action_global_select_circle"
    bl_label = "刷选"
    bl_description = "快捷键 C"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        typeandmode = bpy.context.active_object.type+bpy.context.active_object.mode

        if bpy.context.mode == 'OBJECT':
            bpy.ops.view3d.select_circle('INVOKE_DEFAULT')
        elif typeandmode in {
            "CURVEEDIT", 
            "SURFACEEDIT",
            "METAEDIT",
            "LATTICEEDIT",
            "MESHEDIT",
            "MESHVERTEX_PAINT",
            "MESHWEIGHT_PAINT",
            "MESHTEXTURE_PAINT",
            "GREASEPENCILEDIT",
            "GREASEPENCILSCULPT_GREASE_PENCIL",
            "GREASEPENCILVERTEX_GREASE_PENCIL",
            "ARMATUREEDIT",
            "ARMATUREPOSE",
            }:
            bpy.ops.view3d.select_circle('INVOKE_DEFAULT')
        elif typeandmode in {
            "GPENCILEDIT_GPENCIL",
            "GPENCILVERTEX_GPENCIL",
            "GPENCILSCULPT_GPENCIL",
            }:
            bpy.ops.gpencil.select_circle('INVOKE_DEFAULT') # 4.2 版本
        else:
            return {'CANCELLED'}
        return {'FINISHED'}

# “选择”菜单——选择镜像
class BUTTON_ACTION_OT_global_select_select_mirror(bpy.types.Operator):
    bl_idname = "button.action_global_select_select_mirror"
    bl_label = "选择镜像"
    bl_options = {'REGISTER', 'UNDO'}

    axis: bpy.props.EnumProperty(
        name="镜像轴",
        items=[
            ('X', "X轴", ""),
            ('Y', "Y轴", ""),
            ('Z', "Z轴", ""),
        ],
        default='X',
    )
    
    extend: bpy.props.BoolProperty(
        name="扩展",
        default=False,
        description="扩展选择，而不是先取消选择",
    )

    # 针对骨骼的选项
    only_active: bpy.props.BoolProperty(
        name="仅激活",
        default=False,
        description="仅操作活动的骨骼",
    )

    def invoke(self, context, event):
        return self.execute(context)

    def draw(self, context):
        typeandmode = bpy.context.active_object.type + bpy.context.active_object.mode

        layout = self.layout
        split = layout.row().split(factor=0.4)
        
        # 左侧列 - 标签
        col_left = split.column()
        col_left.alignment = 'RIGHT'
        if typeandmode in {"MESHEDIT","LATTICEEDIT"}:
            col_left.label(text="轴向")
        
        # 右侧列 - 垂直排列的单选按钮
        col_right = split.column()
        if typeandmode in {"MESHEDIT","LATTICEEDIT"}:
            col_right.prop(self, "axis", expand=True)
        if typeandmode in {"ARMATUREEDIT","ARMATUREPOSE"}:
            col_right.prop(self, "only_active")
        col_right.prop(self, "extend")

    def execute(self, context):
        typeandmode = bpy.context.active_object.type + bpy.context.active_object.mode

        if bpy.context.mode == 'OBJECT':
            bpy.ops.object.select_mirror(extend=self.extend)
        elif typeandmode == "LATTICEEDIT":
            bpy.ops.lattice.select_mirror(axis={self.axis}, extend=self.extend)
        elif typeandmode == "MESHEDIT":
            # 在编辑模式下直接将轴参数传给操作符
            bpy.ops.mesh.select_mirror(axis={self.axis}, extend=self.extend)
        elif typeandmode == "ARMATUREEDIT":
            bpy.ops.armature.select_mirror(only_active=self.only_active, extend=self.extend)
        elif typeandmode == "ARMATUREPOSE":
            bpy.ops.pose.select_mirror(only_active=self.only_active, extend=self.extend)
        else:
            return {'CANCELLED'}
        return {'FINISHED'}

# “选择”菜单——随机选择
class BUTTON_ACTION_OT_global_select_select_random(bpy.types.Operator):
    bl_idname = "button.action_global_select_select_random"
    bl_label = "随机选择"
    bl_options = {'REGISTER', 'UNDO'}

    ratio: bpy.props.FloatProperty(
        name="",
        description="用于随机选择的部分",
        default=0.5, 
        min=0.0,  
        max=1.0, 
        subtype='FACTOR',      
        precision=3,          
        #update=lambda self, context: self.execute(context)  
    )

    seed: bpy.props.IntProperty(
        name="",
        description="随机数生成器的种值",
        default=0,
        min=0,
        soft_max=255, 
        #update=lambda self, context: self.execute(context)  
    )

    action: bpy.props.EnumProperty(
        name="动作",
        items=[
            ('SELECT', "选择", "全选"),
            ('DESELECT', "弃选", "弃选全部元素"),
        ],
        default='SELECT',
        #update=lambda self, context: self.execute(context) 
    )

    unselect_ends: bpy.props.BoolProperty(
        name="不选中末端",
        description="不选择笔画的起点和末点",
        default=False,
        #update=lambda self, context: self.execute(context)
    )
    
    def invoke(self, context, event):
        return self.execute(context)

    def draw(self, context):
        typeandmode = bpy.context.active_object.type + bpy.context.active_object.mode

        layout = self.layout
        split = layout.row().split(factor=0.4)
        
        col_left = split.column()
        col_left.alignment = 'RIGHT'
        col_left.label(text="比率")
        col_left.label(text="随机种")
        col_left.label(text="动作")
        
        col_right = split.column()
        col_right.prop(self, "ratio")
        col_right.prop(self, "seed")
        col_right.prop(self, "action", expand=True)
        if typeandmode in {"GPENCILEDIT_GPENCIL","GPENCILSCULPT_GPENCIL","GPENCILVERTEX_GPENCIL"}:
            col_right.prop(self, "unselect_ends")

    def execute(self, context):
        typeandmode = bpy.context.active_object.type + bpy.context.active_object.mode

        if bpy.context.mode == 'OBJECT':
            bpy.ops.object.select_random(ratio=self.ratio, seed=self.seed, action=self.action)
        elif typeandmode == "MESHEDIT":
            bpy.ops.mesh.select_random(ratio=self.ratio, seed=self.seed, action=self.action)
        elif typeandmode in {"CURVEEDIT","SURFACEEDIT"}:
            bpy.ops.curve.select_random(ratio=self.ratio, seed=self.seed, action=self.action)
        elif typeandmode == "METAEDIT":
            bpy.ops.mball.select_random_metaelems(ratio=self.ratio, seed=self.seed, action=self.action)
        elif typeandmode == "GPENCILEDIT_GPENCIL":
            bpy.ops.gpencil.select_random(ratio=self.ratio, seed=self.seed, action=self.action, unselect_ends=self.unselect_ends)
        elif typeandmode in {"GPENCILSCULPT_GPENCIL","GPENCILVERTEX_GPENCIL"} and\
            bpy.context.scene.tool_settings.use_gpencil_select_mask_point or\
            bpy.context.scene.tool_settings.use_gpencil_select_mask_stroke or\
            bpy.context.scene.tool_settings.use_gpencil_select_mask_segment:
            bpy.ops.gpencil.select_random(ratio=self.ratio, seed=self.seed, action=self.action, unselect_ends=self.unselect_ends)
        elif typeandmode == "GREASEPENCILEDIT":
            bpy.ops.grease_pencil.select_random(ratio=self.ratio, seed=self.seed, action=self.action)
        elif typeandmode in {"GREASEPENCILSCULPT_GREASE_PENCIL","GREASEPENCILVERTEX_GREASE_PENCIL"} and\
            bpy.context.scene.tool_settings.use_gpencil_select_mask_point or\
            bpy.context.scene.tool_settings.use_gpencil_select_mask_stroke or\
            bpy.context.scene.tool_settings.use_gpencil_select_mask_segment:
            bpy.ops.grease_pencil.select_random(ratio=self.ratio, seed=self.seed, action=self.action)
        elif typeandmode == "LATTICEEDIT":
            bpy.ops.lattice.select_random(ratio=self.ratio, seed=self.seed, action=self.action)
        else:
            return {'CANCELLED'}
        return {'FINISHED'}

# “选择”菜单——加选/减选
class VIEW3D_MT_global_select_more_or_less_menu(bpy.types.Operator):
    bl_label = ""
    bl_idname = "popup.global_more_or_less_menu"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        return {'FINISHED'}

    def invoke(self, context, event):
        return context.window_manager.invoke_popup(self, width=100)

    def draw(self, context):
        typeandmode = bpy.context.active_object.type+bpy.context.active_object.mode

        layout = self.layout
        row = layout.row()
        col = row.column(align=True)
        col.label(text="加选/减选", icon='FORCE_CHARGE')

        if bpy.context.mode == "OBJECT":
            col.operator("object.select_more", text="扩展选区", icon="ADD")
            col.operator("object.select_less", text="缩减选区", icon="REMOVE")
        elif typeandmode == "CURVEEDIT":
            col.operator("curve.select_more", text="扩展选择", icon="ADD")
            col.operator("curve.select_less", text="缩减选择", icon="REMOVE")
            col.separator()
            col.operator("curve.select_next", text="选择下一项", icon="FRAME_NEXT")
            col.operator("curve.select_previous", text="选择上一项", icon="FRAME_PREV")
        elif typeandmode == "SURFACEEDIT":
            col.operator("curve.select_more", text="扩展选择", icon="ADD")
            col.operator("curve.select_less", text="缩减选择", icon="REMOVE")
        elif typeandmode == "MESHEDIT":
            col.operator("mesh.select_more", text="扩展选区", icon="ADD")
            col.operator("mesh.select_less", text="缩减选区", icon="REMOVE")
            col.separator()
            col.operator("mesh.select_next_item", text="下一个活动元素", icon="FRAME_NEXT")
            col.operator("mesh.select_prev_item", text="上一个活动元素", icon="FRAME_PREV")

        elif typeandmode in {"MESHVERTEX_PAINT","MESHWEIGHT_PAINT","MESHTEXTURE_PAINT"}:
            col.operator("paint.face_select_more", text="扩展选择", icon="ADD")
            col.operator("paint.face_select_less", text="缩减选择", icon="REMOVE")

        elif typeandmode == "ARMATUREEDIT":
            col.operator("armature.select_more", text="扩展选区", icon="ADD")
            col.operator("armature.select_less", text="缩减选区", icon="REMOVE")
        elif typeandmode == "LATTICEEDIT":
            col.operator("lattice.select_more", text="扩展选区", icon="ADD")
            col.operator("lattice.select_less", text="缩减选区", icon="REMOVE")

        elif typeandmode == "GPENCILEDIT_GPENCIL":
            col.operator("gpencil.select_more", text="扩展选区", icon="ADD")
            col.operator("gpencil.select_less", text="缩减选区", icon="REMOVE")

        elif typeandmode in {"GPENCILSCULPT_GPENCIL","GPENCILVERTEX_GPENCIL"}:
            col.operator("gpencil.select_more", text="扩展选区", icon="ADD")
            col.operator("gpencil.select_less", text="缩减选区", icon="REMOVE")

        elif typeandmode == "GREASEPENCILEDIT":
            col.operator("grease_pencil.select_more", text="扩展选区", icon="ADD")
            col.operator("grease_pencil.select_less", text="缩减选区", icon="REMOVE")

        elif typeandmode in {"GREASEPENCILSCULPT_GREASE_PENCIL","GREASEPENCILVERTEX_GREASE_PENCIL"}:
            col.operator("grease_pencil.select_more", text="扩展选区", icon="ADD")
            col.operator("grease_pencil.select_less", text="缩减选区", icon="REMOVE")

        col.separator()
        col.operator("ed.undo", text="撤销", icon="LOOP_BACK")
        col.operator("ed.redo", text="重做", icon="LOOP_FORWARDS")

class BUTTON_ACTION_OT_call_global_select_more_or_less_menu(bpy.types.Operator):
    bl_idname = "button.action_call_global_select_more_or_less_menu"
    bl_label = "加选/减选"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.ops.popup.global_more_or_less_menu('INVOKE_DEFAULT')
        return {'FINISHED'}

# “选择”菜单——父级/子级
class BUTTON_ACTION_OT_global_select_select_parent_or_child(bpy.types.Operator):
    bl_idname = "button.action_global_select_select_parent_or_child"
    bl_label = "父级/子级/扩展父级/扩展子级"
    bl_description = "父级/子级/扩展父级/扩展子级功能集合"
    bl_options = {'REGISTER', 'UNDO'}

    direction: bpy.props.EnumProperty(
        name="选择动作", 
        items=[
            ('PARENT', "父级", ""),
            ('CHILD', "子级", ""), 
        ],
        default='PARENT',
    )

    extend: bpy.props.BoolProperty(
        name="扩展",            
        description="", 
        default=False,
    ) 

    def invoke(self, context, event):
        return self.execute(context)

    def draw(self, context):
        layout = self.layout
        split = layout.row().split(factor=0.4)
        
        col_left = split.column()
        col_left.alignment = 'RIGHT'
        col_left.label(text="方向")
        
        col_right = split.column()
        col_right.prop(self, "direction", expand=True)
        col_right.prop(self, "extend")

    def execute(self, context):
        typeandmode = bpy.context.active_object.type+bpy.context.active_object.mode

        if bpy.context.mode == 'OBJECT':
            bpy.ops.object.select_hierarchy(direction=self.direction, extend=self.extend)
        elif typeandmode == "ARMATUREEDIT":
            bpy.ops.armature.select_hierarchy(direction=self.direction, extend=self.extend)
        elif typeandmode == "ARMATUREPOSE":
            bpy.ops.pose.select_hierarchy(direction=self.direction, extend=self.extend)
        else:
            return {'CANCELLED'}
        return {'FINISHED'}
    
# "选择"菜单——按组选择
class BUTTON_ACTION_OT_global_select_select_grouped(bpy.types.Operator):
    bl_idname = "button.action_select_select_grouped"
    bl_label = "按组选择"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):        
        if bpy.context.mode == "OBJECT":
            bpy.ops.object.select_grouped('INVOKE_DEFAULT')
        elif bpy.context.mode in {
            "EDIT_GPENCIL",
            "SCULPT_GPENCIL",
            "VERTEX_GPENCIL"}:
            bpy.ops.gpencil.select_grouped('INVOKE_DEFAULT')
        elif bpy.context.mode == "POSE":
            bpy.ops.pose.select_grouped('INVOKE_DEFAULT')
        return {'FINISHED'}

# “选择”菜单——选择相连
class BUTTON_ACTION_OT_global_select_select_linked(bpy.types.Operator):
    bl_idname = "button.action_global_select_select_linked"
    bl_label = "选择相连"
    bl_description = "选择相连元素/关联项"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):        
        typeandmode = bpy.context.active_object.type + bpy.context.active_object.mode
        
        if bpy.context.mode == "OBJECT":
            bpy.ops.object.select_linked('INVOKE_DEFAULT')

        elif typeandmode == "GREASEPENCILEDIT":
            bpy.ops.grease_pencil.select_linked('INVOKE_DEFAULT')

        elif typeandmode == "GREASEPENCILSCULPT_GREASE_PENCIL":
            bpy.ops.grease_pencil.select_linked('INVOKE_DEFAULT')

        elif typeandmode == "GREASEPENCILVERTEX_GREASE_PENCIL":
            bpy.ops.grease_pencil.select_linked('INVOKE_DEFAULT')

        elif typeandmode == "GPENCILEDIT_GPENCIL":
            bpy.ops.gpencil.select_linked('INVOKE_DEFAULT')

        elif typeandmode == "GPENCILSCULPT_GPENCIL":
            if bpy.context.scene.tool_settings.use_gpencil_select_mask_point or\
                bpy.context.scene.tool_settings.use_gpencil_select_mask_stroke or\
                bpy.context.scene.tool_settings.use_gpencil_select_mask_segment:
                bpy.ops.gpencil.select_linked('INVOKE_DEFAULT')

        elif typeandmode == "GPENCILVERTEX_GPENCIL":
            if bpy.context.scene.tool_settings.use_gpencil_vertex_select_mask_point or\
                bpy.context.scene.tool_settings.use_gpencil_vertex_select_mask_stroke or\
                bpy.context.scene.tool_settings.use_gpencil_vertex_select_mask_segment:
                bpy.ops.gpencil.select_linked('INVOKE_DEFAULT')

        elif typeandmode in {"CURVEEDIT", "SURFACEEDIT"}:
            bpy.ops.curve.select_linked('INVOKE_DEFAULT')

        elif typeandmode == "MESHEDIT":
            bpy.ops.popup.mesh_select_linked_menu('INVOKE_DEFAULT')

        elif typeandmode in {
            "MESHVERTEX_PAINT",
            "MESHWEIGHT_PAINT",
            "MESHTEXTURE_PAINT"}:
            if bpy.context.active_object.data.use_paint_mask:
                bpy.ops.paint.face_select_linked()
            elif bpy.context.active_object.data.use_paint_mask_vertex:
                bpy.ops.paint.vert_select_linked()

        elif typeandmode == "ARMATUREPOSE":
            bpy.ops.pose.select_linked('INVOKE_DEFAULT')

        return {'FINISHED'}

class VIEW3D_MT_mesh_select_linked_menu(bpy.types.Operator):
    bl_label = "选择相连元素"
    bl_idname = "popup.mesh_select_linked_menu"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        return {'FINISHED'}

    def invoke(self, context, event):
        return context.window_manager.invoke_popup(self, width=100)

    def draw(self, context):
        layout = self.layout
        row = layout.row()
        col = row.column(align=True)
        col.label(text="选择相连元素", icon='LINK_BLEND')
        col.operator("mesh.select_linked", text="关联项", icon="RADIOBUT_OFF")
        col.operator("mesh.shortest_path_select", text="最短路径", icon="RADIOBUT_OFF")
        col.operator("mesh.faces_select_linked_flat", text="相连的平展面", icon="RADIOBUT_OFF")
        col.separator()
        col.operator("ed.undo", text="撤销", icon="LOOP_BACK")
        col.operator("ed.redo", text="重做", icon="LOOP_FORWARDS")

# “选择”菜单——按名称
class BUTTON_ACTION_OT_global_select_select_pattern(bpy.types.Operator):
    bl_idname = "button.action_object_select_pattern"
    bl_label = "按名称选择"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.ops.object.select_pattern('INVOKE_DEFAULT')
        return {'FINISHED'}

# "选择"菜单——选择相似
class BUTTON_ACTION_OT_global_select_select_similar(bpy.types.Operator):
    bl_idname = "button.action_global_select_select_similar"
    bl_label = "选择相似"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):    
        typeandmode = bpy.context.active_object.type+bpy.context.active_object.mode    
        if typeandmode in {"CURVEEDIT","SURFACEEDIT"}:
            bpy.ops.curve.select_similar('INVOKE_DEFAULT')
        elif typeandmode == "MESHEDIT":
            bpy.ops.wm.call_menu(name="VIEW3D_MT_edit_mesh_select_similar")
        elif typeandmode == "METAEDIT":
            bpy.ops.mball.select_similar('INVOKE_DEFAULT')

        elif typeandmode == "GREASEPENCILEDIT":
            bpy.ops.wm.call_menu(name="button.action_global_select_select_similar_menu")

        elif typeandmode == "GREASEPENCILSCULPT_GREASE_PENCIL":
            if bpy.context.scene.tool_settings.use_gpencil_select_mask_point or\
                bpy.context.scene.tool_settings.use_gpencil_select_mask_stroke or\
                bpy.context.scene.tool_settings.use_gpencil_select_mask_segment:
                bpy.ops.wm.call_menu(name="button.action_global_select_select_similar_menu")
        
        elif typeandmode == "GREASEPENCILVERTEX_GREASE_PENCIL":
            if bpy.context.scene.tool_settings.use_gpencil_vertex_select_mask_point or\
                bpy.context.scene.tool_settings.use_gpencil_vertex_select_mask_stroke or\
                bpy.context.scene.tool_settings.use_gpencil_vertex_select_mask_segment:
                bpy.ops.wm.call_menu(name="button.action_global_select_select_similar_menu")

        return {'FINISHED'}

class VIEW3D_MT_global_select_select_similar_menu(bpy.types.Menu):
    bl_idname = "button.action_global_select_select_similar_menu"
    bl_label = "选择相似元素"
    bl_options = {'SEARCH_ON_KEY_PRESS'}

    def draw(self, context):
        layout = self.layout
        layout.operator("grease_pencil.select_similar", text="层").mode='LAYER'
        layout.operator("grease_pencil.select_similar", text="材质").mode='MATERIAL'
        layout.operator("grease_pencil.select_similar", text="顶点颜色").mode='VERTEX_COLOR'
        layout.operator("grease_pencil.select_similar", text="半径").mode='RADIUS'
        layout.operator("grease_pencil.select_similar", text="不透明度").mode='OPACITY'

# “选择”菜单——未归组顶点
class BUTTON_ACTION_OT_global_select_select_ungrouped(bpy.types.Operator):
    bl_idname = "button.action_global_selectt_select_ungrouped"
    bl_label = "选择未归组项"
    bl_options = {'REGISTER', 'UNDO'}

    def lattice_has_grouped_points(self, obj):
        # 对 Lattice 的每个点检查是否有归组
        for i, point in enumerate(obj.data.points):
            for vg in obj.vertex_groups:
                try:
                    weight = vg.weight(i)
                    if weight > 0.0:
                        return True
                except RuntimeError:
                    continue
        return False

    extend: bpy.props.BoolProperty(
        name="扩展",            
        description="", 
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
        col_right.prop(self, "extend")  

    def execute(self, context):
        typeandmode = bpy.context.active_object.type+bpy.context.active_object.mode

        if typeandmode in {"MESHVERTEX_PAINT","MESHWEIGHT_PAINT"} and bpy.context.active_object.data.use_paint_mask_vertex:
            if not bpy.context.active_object.vertex_groups:
                self.report({'ERROR'}, "物体未包含权重/顶点组")
                return {'CANCELLED'}

            if not any(v.groups for v in bpy.context.active_object.data.vertices):
                self.report({'ERROR'}, "物体未包含权重/顶点组")
                return {'CANCELLED'}
            bpy.ops.paint.vert_select_ungrouped(extend=self.extend)

        elif typeandmode == "LATTICEEDIT":
            if not bpy.context.active_object.vertex_groups:
                self.report({'ERROR'}, "该 Lattice 没有顶点组")
                return {'CANCELLED'}
            if not self.lattice_has_grouped_points(bpy.context.active_object):
                self.report({'ERROR'}, "该 Lattice 没有归组的点")
                return {'CANCELLED'}

            bpy.ops.lattice.select_ungrouped(extend=self.extend)

        else:
            self.report({'ERROR'}, "不支持的物体类型或模式")
            return {'CANCELLED'}
        
        return {'FINISHED'}

# “选择”菜单——选择首点
class BUTTON_ACTION_OT_global_gpencil_select_select_first(bpy.types.Operator):
    bl_idname = "button.action_global_gpencil_select_select_first"
    bl_label = "选中首点"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        if bpy.context.mode == "SCULPT_GPENCIL" and (
            not bpy.context.scene.tool_settings.use_gpencil_select_mask_point and
            not bpy.context.scene.tool_settings.use_gpencil_select_mask_stroke and
            not bpy.context.scene.tool_settings.use_gpencil_select_mask_segment):
            return False
        elif bpy.context.mode == "VERTEX_GPENCIL" and (
            not bpy.context.scene.tool_settings.use_gpencil_vertex_select_mask_point and
            not bpy.context.scene.tool_settings.use_gpencil_vertex_select_mask_stroke and
            not bpy.context.scene.tool_settings.use_gpencil_vertex_select_mask_segment):
            return False
        return True

    only_selected_strokes: bpy.props.BoolProperty(
        name="仅选中笔画",            
        description="只选择笔画的起始点", 
        default=False,
    ) 

    extend: bpy.props.BoolProperty(
        name="扩展",            
        description="扩展选择，而不是取消选择", 
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
        col_left.label(text="")
        
        col_right = split.column()
        col_right.prop(self, "only_selected_strokes")
        col_right.prop(self, "extend")  

    def execute(self, context):
        bpy.ops.gpencil.select_first(only_selected_strokes=self.only_selected_strokes, extend=self.extend)
        return {'FINISHED'}

# “选择”菜单——选择末点
class BUTTON_ACTION_OT_global_gpencil_select_select_last(bpy.types.Operator):
    bl_idname = "button.action_global_gpencil_select_select_last"
    bl_label = "选中末点"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        if bpy.context.mode == "SCULPT_GPENCIL" and (
            not bpy.context.scene.tool_settings.use_gpencil_select_mask_point and
            not bpy.context.scene.tool_settings.use_gpencil_select_mask_stroke and
            not bpy.context.scene.tool_settings.use_gpencil_select_mask_segment):
            return False
        elif bpy.context.mode == "VERTEX_GPENCIL" and (
            not bpy.context.scene.tool_settings.use_gpencil_vertex_select_mask_point and
            not bpy.context.scene.tool_settings.use_gpencil_vertex_select_mask_stroke and
            not bpy.context.scene.tool_settings.use_gpencil_vertex_select_mask_segment):
            return False
        return True
    
    only_selected_strokes: bpy.props.BoolProperty(
        name="仅选中笔画",            
        description="只选择笔画的起始点", 
        default=False,
    ) 

    extend: bpy.props.BoolProperty(
        name="扩展",            
        description="扩展选择，而不是取消选择", 
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
        col_left.label(text="")
        
        col_right = split.column()
        col_right.prop(self, "only_selected_strokes")
        col_right.prop(self, "extend")  

    def execute(self, context):
        bpy.ops.gpencil.select_last(only_selected_strokes=self.only_selected_strokes, extend=self.extend)
        return {'FINISHED'}

# “选择”菜单——起始点
class BUTTON_ACTION_OT_global_greasepencil_select_select_first(bpy.types.Operator):
    bl_idname = "button.action_global_greasepencil_select_select_first"
    bl_label = "选择端点"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        if bpy.context.mode == "SCULPT_GREASE_PENCIL" and (
            not bpy.context.scene.tool_settings.use_gpencil_select_mask_point and
            not bpy.context.scene.tool_settings.use_gpencil_select_mask_stroke and
            not bpy.context.scene.tool_settings.use_gpencil_select_mask_segment):
            return False
        elif bpy.context.mode == "VERTEX_GREASE_PENCIL" and (
            not bpy.context.scene.tool_settings.use_gpencil_vertex_select_mask_point and
            not bpy.context.scene.tool_settings.use_gpencil_vertex_select_mask_stroke and
            not bpy.context.scene.tool_settings.use_gpencil_vertex_select_mask_segment):
            return False
        elif bpy.context.mode == "EDIT_GREASE_PENCIL" and bpy.context.scene.tool_settings.gpencil_selectmode_edit == 'STROKE':
            return False
        return True

    amount_start: bpy.props.IntProperty(
        name="",
        description="从起始端选择的点的数量",
        default=1,
        min=0,
    )

    amount_end: bpy.props.IntProperty(
        name="",
        description="从末端选择的点的数量",
        default=0,
        min=0,
    )

    def invoke(self, context, event):
        return self.execute(context)

    def draw(self, context):
        layout = self.layout
        split = layout.row().split(factor=0.4)
        
        col_left = split.column()
        col_left.alignment = 'RIGHT'
        col_left.label(text="起始数量")
        col_left.label(text="末端数量")
        
        col_right = split.column()
        col_right.prop(self, "amount_start")
        col_right.prop(self, "amount_end")  

    def execute(self, context):
        bpy.ops.grease_pencil.select_ends(amount_start=self.amount_start, amount_end=self.amount_end)
        return {'FINISHED'}

# “选择”菜单——结束点
class BUTTON_ACTION_OT_global_greasepencil_select_select_last(bpy.types.Operator):
    bl_idname = "button.action_global_greasepencil_select_select_last"
    bl_label = "选择端点"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        if bpy.context.mode == "SCULPT_GREASE_PENCIL" and (
            not bpy.context.scene.tool_settings.use_gpencil_select_mask_point and
            not bpy.context.scene.tool_settings.use_gpencil_select_mask_stroke and
            not bpy.context.scene.tool_settings.use_gpencil_select_mask_segment):
            return False
        elif bpy.context.mode == "VERTEX_GREASE_PENCIL" and (
            not bpy.context.scene.tool_settings.use_gpencil_vertex_select_mask_point and
            not bpy.context.scene.tool_settings.use_gpencil_vertex_select_mask_stroke and
            not bpy.context.scene.tool_settings.use_gpencil_vertex_select_mask_segment):
            return False
        elif bpy.context.mode == "EDIT_GREASE_PENCIL" and bpy.context.scene.tool_settings.gpencil_selectmode_edit == 'STROKE':
            return False
        return True

    amount_start: bpy.props.IntProperty(
        name="",
        description="从起始端选择的点的数量",
        default=0,
        min=0,
    )

    amount_end: bpy.props.IntProperty(
        name="",
        description="从末端选择的点的数量",
        default=1,
        min=0,
    )

    def invoke(self, context, event):
        return self.execute(context)

    def draw(self, context):
        layout = self.layout
        split = layout.row().split(factor=0.4)
        
        col_left = split.column()
        col_left.alignment = 'RIGHT'
        col_left.label(text="起始数量")
        col_left.label(text="末端数量")
        
        col_right = split.column()
        col_right.prop(self, "amount_start")
        col_right.prop(self, "amount_end")  

    def execute(self, context):
        bpy.ops.grease_pencil.select_ends(amount_start=self.amount_start, amount_end=self.amount_end)
        return {'FINISHED'}

# “选择”菜单——选择菜单
class BUTTON_ACTION_OT_global_select_select_alternate(bpy.types.Operator):
    bl_idname = "button.action_global_select_select_alternate"
    bl_label = "选择交替"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        if bpy.context.mode in {"SCULPT_GREASE_PENCIL","SCULPT_GPENCIL"} and (
            not bpy.context.scene.tool_settings.use_gpencil_select_mask_point and
            not bpy.context.scene.tool_settings.use_gpencil_select_mask_stroke and
            not bpy.context.scene.tool_settings.use_gpencil_select_mask_segment):
            return False
        
        elif bpy.context.mode == "EDIT_GREASE_PENCIL" and bpy.context.scene.tool_settings.gpencil_selectmode_edit == 'STROKE':
            return False
        
        elif bpy.context.mode == "VERTEX_GPENCIL" and (
            not bpy.context.scene.tool_settings.use_gpencil_vertex_select_mask_point and
            not bpy.context.scene.tool_settings.use_gpencil_vertex_select_mask_stroke and
            not bpy.context.scene.tool_settings.use_gpencil_vertex_select_mask_segment):
            return False
        
        return True

    unselect_ends: bpy.props.BoolProperty(
        name="不选中末端",            
        description="不选择笔画的起点和末点", 
        default=False,
    ) 

    deselect_ends: bpy.props.BoolProperty(
        name="取消选择末端",            
        description="选择/取消选择笔画的起点和末点", 
        default=False,
    ) 

    def invoke(self, context, event):
        return self.execute(context)

    def draw(self, context):
        typeandmode = bpy.context.active_object.type+bpy.context.active_object.mode

        layout = self.layout
        split = layout.row().split(factor=0.4)
        
        col_left = split.column()
        col_left.alignment = 'RIGHT'
        if typeandmode in {"GPENCILEDIT_GPENCIL","GPENCILSCULPT_GPENCIL","GPENCILVERTEX_GPENCIL"}:
            col_left.label(text="")
        elif typeandmode in {"GREASEPENCILEDIT","GREASEPENCILSCULPT_GREASE_PENCIL","GREASEPENCILVERTEX_GREASE_PENCIL"}:
            col_left.label(text="")
        
        col_right = split.column()
        if typeandmode in {"GPENCILEDIT_GPENCIL","GPENCILSCULPT_GPENCIL","GPENCILVERTEX_GPENCIL"}:
            col_right.prop(self, "unselect_ends")
        elif typeandmode in {"GREASEPENCILEDIT","GREASEPENCILSCULPT_GREASE_PENCIL","GREASEPENCILVERTEX_GREASE_PENCIL"}:
            col_right.prop(self, "deselect_ends")  

    def execute(self, context):
        typeandmode = bpy.context.active_object.type+bpy.context.active_object.mode

        if typeandmode in {"GPENCILEDIT_GPENCIL","GPENCILSCULPT_GPENCIL","GPENCILVERTEX_GPENCIL"}:
            bpy.ops.gpencil.select_alternate(unselect_ends = self.unselect_ends)
        elif typeandmode in {"GREASEPENCILEDIT","GREASEPENCILSCULPT_GREASE_PENCIL","GREASEPENCILVERTEX_GREASE_PENCIL"}:
            bpy.ops.grease_pencil.select_alternate(deselect_ends = self.deselect_ends)
        return {'FINISHED'}


























# 全局“移动”功能
class BUTTON_ACTION_OT_grab(bpy.types.Operator):
    bl_idname = "button.action_global_grab"
    bl_label = "移动"
    bl_description = "快捷键 G"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.ops.transform.translate('INVOKE_DEFAULT')
        return {'FINISHED'}
    
# 全局“缩放”功能
class BUTTON_ACTION_OT_scale(bpy.types.Operator):
    bl_idname = "button.action_global_scale"
    bl_label = "缩放"
    bl_description = "快捷键 S"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.ops.transform.resize('INVOKE_DEFAULT')
        return {'FINISHED'}

# 全局“旋转”功能    
class BUTTON_ACTION_OT_rotate(bpy.types.Operator):
    bl_idname = "button.action_global_rotate"
    bl_label = "旋转(R)"
    bl_description = "快捷键 R"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.ops.transform.rotate('INVOKE_DEFAULT')
        return {'FINISHED'}
    

# 全局“添加”菜单功能
class BUTTON_ACTION_OT_global_add(bpy.types.Operator):
    bl_idname = "button.action_global_add"
    bl_label = "添加"
    bl_description = "快捷键 Shift A"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        typeandmode = bpy.context.active_object.type+bpy.context.active_object.mode

        if bpy.context.mode == 'OBJECT':
            bpy.ops.wm.call_menu(name="VIEW3D_MT_add")
        if typeandmode == "CURVEEDIT":
            bpy.ops.wm.call_menu(name="VIEW3D_MT_curve_add")
        if typeandmode == 'SURFACEEDIT':
            bpy.ops.wm.call_menu(name="VIEW3D_MT_surface_add")
        if typeandmode == 'METAEDIT':
            bpy.ops.wm.call_menu(name="VIEW3D_MT_metaball_add")
        if typeandmode == 'MESHEDIT':
            bpy.ops.wm.call_menu(name="VIEW3D_MT_mesh_add")
        if typeandmode == 'ARMATUREEDIT':
            bpy.ops.wm.call_menu(name="TOPBAR_MT_edit_armature_add")
        return {'FINISHED'}

# 全局“复制 Shift D”按钮功能
class BUTTON_ACTION_OT_global_duplicate_move(bpy.types.Operator):
    bl_idname = "button.action_global_duplicate_move"
    bl_label = "复制"
    bl_description = "快捷键 Shift D"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        typeandmode = bpy.context.active_object.type+bpy.context.active_object.mode
        if bpy.context.mode == "OBJECT":
            bpy.ops.object.duplicate_move('INVOKE_DEFAULT')
        elif typeandmode in {"CURVEEDIT","SURFACEEDIT"}:
            bpy.ops.curve.duplicate_move('INVOKE_DEFAULT')
        elif typeandmode == "METAEDIT":
            bpy.ops.mball.duplicate_move('INVOKE_DEFAULT')
        elif typeandmode == "GPENCILEDIT_GPENCIL":
            bpy.ops.gpencil.duplicate_move('INVOKE_DEFAULT')
        elif typeandmode == "GREASEPENCILEDIT":
            bpy.ops.grease_pencil.duplicate_move('INVOKE_DEFAULT')
        elif typeandmode == "MESHEDIT":
            bpy.ops.mesh.duplicate_move('INVOKE_DEFAULT')
        elif typeandmode == "ARMATUREEDIT":
            bpy.ops.armature.duplicate_move('INVOKE_DEFAULT')
        return {'FINISHED'}
    
# 物体模式/蜡笔/骨架姿态“复制 Ctrl C”按钮功能
class BUTTON_ACTION_OT_global_copy(bpy.types.Operator):
    bl_idname = "button.action_global_copy"
    bl_label = "复制"
    bl_description = "快捷键 Ctrl C"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        typeandmode = bpy.context.active_object.type+bpy.context.active_object.mode
        if bpy.context.mode == "OBJECT":
            bpy.ops.view3d.copybuffer()
        elif typeandmode == "ARMATUREPOSE":
            bpy.ops.pose.copy()
        elif typeandmode == "GPENCILEDIT_GPENCIL":
            bpy.ops.gpencil.copy()
        elif typeandmode == "GREASEPENCILEDIT":
            bpy.ops.grease_pencil.copy()
        return {'FINISHED'}
    
# 物体模式/蜡笔/骨架姿态“复制 Ctrl V”按钮功能
class BUTTON_ACTION_OT_global_paste(bpy.types.Operator):
    bl_idname = "button.action_global_paste"
    bl_label = "粘贴"
    bl_description = "快捷键 Ctrl V"
    bl_options = {'REGISTER', 'UNDO'}

    autoselect: bpy.props.BoolProperty( # 粘贴“物体”用
        name="选择",
        default=True,
        description="扩展选择，而不是先取消选择",
        update=lambda self, context: self.execute(context) #if bpy.context.mode == 'EDIT_MESH' else None
    )

    active_collection: bpy.props.BoolProperty(  # 粘贴“物体”用
        name="活动集合",
        default=True,
        description="扩展选择，而不是先取消选择",
        update=lambda self, context: self.execute(context) #if bpy.context.mode == 'EDIT_MESH' else None
    )

    type: bpy.props.EnumProperty(   # 4.2 版本粘贴蜡笔用
        name="类型",
        items=[
            ('ACTIVE', "粘贴到活动项", ""),
            ('LAYER', "按层粘贴", ""),
        ],
        default='ACTIVE',
        update=lambda self, context: self.execute(context) #if bpy.context.mode == 'EDIT_MESH' else None
    )

    paste_back: bpy.props.BoolProperty(  # 4.2 4.3 两个版本共用粘贴蜡笔用
        name="粘贴到最后",
        default=False,
        description="将画笔粘贴到所有画笔之后",
        update=lambda self, context: self.execute(context) #if bpy.context.mode == 'EDIT_MESH' else None
    )

    keep_world_transform: bpy.props.BoolProperty(  # 4.3 版本粘贴蜡笔用
        name="保持世界变换",
        default=False,
        description="保持剪贴板中笔画的世界变换不变",
        update=lambda self, context: self.execute(context) #if bpy.context.mode == 'EDIT_MESH' else None
    )

    flipped: bpy.props.BoolProperty( # 粘贴“物体”用
        name="没X轴翻转",
        default=False,
        description="将存储的翻转姿态粘贴到当前姿态",
        update=lambda self, context: self.execute(context) 
    )

    selected_mask: bpy.props.BoolProperty( # 粘贴“物体”用
        name="只考虑所选部分",
        default=False,
        description="只将存储的姿态粘贴到当前姿态中的所选骨骼上",
        update=lambda self, context: self.execute(context) 
    )

    def invoke(self, context, event):
        return self.execute(context)
    
    def draw(self, context):
        typeandmode = bpy.context.active_object.type + bpy.context.active_object.mode

        layout = self.layout
        split = layout.row().split(factor=0.4)
        
        # 左侧列 - 标签
        col_left = split.column()
        col_left.alignment = 'RIGHT'
        if bpy.context.mode == "OBJECT":
            col_left.label(text="")
            col_left.label(text="")
        elif typeandmode == "GPENCILEDIT_GPENCIL":
            col_left.label(text="类型")
            col_left.label(text="") 
            col_left.label(text="")    
        elif typeandmode == "GREASEPENCILEDIT":
            col_left.label(text="") 
            col_left.label(text="")
        elif typeandmode == "ARMATUREPOSE":
            col_left.label(text="") 
            col_left.label(text="")
        
        # 右侧列 - 垂直排列的单选按钮
        col_right = split.column()
        if bpy.context.mode == "OBJECT":
            col_right.prop(self, "autoselect")
            col_right.prop(self, "active_collection")
        elif typeandmode == "GPENCILEDIT_GPENCIL":
            col_right.prop(self, "type", expand=True)
            col_right.prop(self, "paste_back")    
        elif typeandmode == "GREASEPENCILEDIT":
            col_right.prop(self, "paste_back") 
            col_right.prop(self, "keep_world_transform")
        elif typeandmode == "ARMATUREPOSE":
            col_right.prop(self, "flipped")
            col_right.prop(self, "selected_mask")

    def execute(self, context):
        typeandmode = bpy.context.active_object.type+bpy.context.active_object.mode
        if bpy.context.mode == "OBJECT":
            bpy.ops.view3d.pastebuffer(autoselect=self.autoselect, active_collection=self.active_collection)
        elif typeandmode == "GPENCILEDIT_GPENCIL":
            bpy.ops.gpencil.paste(type=self.type, paste_back=self.paste_back)
        elif typeandmode == "GREASEPENCILEDIT":
            bpy.ops.grease_pencil.paste(paste_back=self.paste_back, keep_world_transform=self.keep_world_transform)
        elif typeandmode == "ARMATUREPOSE":
            bpy.ops.pose.paste(flipped=self.flipped, selected_mask=self.selected_mask)
        return {'FINISHED'}

# 定义“删除”菜单
class VIEW3D_MT_global_delete_menu(bpy.types.Menu):
    bl_label = "删除"
    bl_idname = "view3d.mt_global_delete_menu"
    bl_options = {'SEARCH_ON_KEY_PRESS'}


    def draw(self, context):
        layout = self.layout

        typeandmode = bpy.context.active_object.type+bpy.context.active_object.mode

        if bpy.context.mode == "OBJECT":
            layout.operator("object.delete", text="删除", icon="QUESTION").use_global=False
        elif typeandmode == "MESHEDIT":
            layout.operator("mesh.dissolve_mode", text="融并删除" ,icon="CANCEL")
            layout.separator()
            layout.operator("mesh.delete", text="顶点").type='VERT'
            layout.operator("mesh.delete", text="边").type='EDGE'
            layout.operator("mesh.delete", text="面").type='FACE'
            layout.operator("mesh.delete", text="仅边和面").type='EDGE_FACE'
            layout.operator("mesh.delete", text="仅面").type='ONLY_FACE'
            layout.separator()
            layout.operator("mesh.dissolve_verts", text="融并顶点")
            layout.operator("mesh.dissolve_edges", text="融并边")
            layout.operator("mesh.dissolve_faces", text="融并面")
            layout.separator()
            layout.operator("mesh.dissolve_limited", text="有限融并")
            layout.separator()
            layout.operator("mesh.edge_collapse", text="塌陷边和面")
            layout.operator("mesh.delete_edgeloop", text="循环边")
        elif typeandmode == "METAEDIT":
            layout.operator("mball.delete_metaelems", text="删除", icon="QUESTION")
        elif typeandmode == "GPENCILEDIT_GPENCIL":
            layout.operator("gpencil.delete", text="点").type='POINTS'
            layout.operator("gpencil.delete", text="笔画").type='STROKES'
            layout.operator("gpencil.delete", text="帧").type='FRAME'
            layout.separator()
            layout.operator("gpencil.dissolve", text="消融").type='POINTS'
            layout.operator("gpencil.dissolve", text="融并期间").type='BETWEEN'
            layout.operator("gpencil.dissolve", text="融并未选中").type='UNSELECT'
            layout.separator()
            layout.operator("gpencil.delete", text="删除活动层的活动帧").type='FRAME'
            layout.operator("gpencil.active_frames_delete_all", text="删除全部层的活动帧")
        elif typeandmode == "GPENCILPAINT_GPENCIL":
            layout.operator("gpencil.delete", text="删除活动层的活动帧").type='FRAME'
            layout.operator("gpencil.active_frames_delete_all", text="删除全部层的活动帧")
        elif typeandmode == "GREASEPENCILEDIT":        
            layout.operator("grease_pencil.delete", text="删除")
            layout.separator()
            layout.operator("grease_pencil.dissolve", text="消融").type='POINTS'
            layout.operator("grease_pencil.dissolve", text="融并其间").type='BETWEEN'
            layout.operator("grease_pencil.dissolve", text="融并未选中").type='UNSELECT'
            layout.separator()
            layout.operator("grease_pencil.delete_frame", text="删除活动层的活动关键帧").type='ACTIVE_FRAME'
            layout.operator("grease_pencil.delete_frame", text="删除所有层的活动关键帧").type='ALL_FRAMES'
        elif typeandmode == "ARMATUREEDIT":
            layout.operator("armature.delete", text="骨骼")
            layout.separator()
            layout.operator("armature.dissolve", text="融并骨骼")
        elif typeandmode in {"CURVEEDIT","SURFACEEDIT"}:
            layout.operator("curve.delete", text="顶点").type='VERT'
            layout.operator("curve.delete", text="段数").type='SEGMENT'
            layout.separator()
            layout.operator("curve.dissolve_verts", text="融并顶点")

# 定义调用“删除”菜单操作
class BUTTON_ACTION_OT_call_global_delete_menu(bpy.types.Operator):
    bl_idname = "button.action_global_call_delete_menu"
    bl_label = "删除"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.ops.wm.call_menu(name="view3d.mt_global_delete_menu")
        return {'FINISHED'}

# 多种编辑模式“隐藏”/"隐藏未选项"
class BUTTON_ACTION_OT_global_hide_view_set(bpy.types.Operator):
    bl_idname = "button.action_global_hide_view_set"
    bl_label = "隐藏"
    bl_description = "快捷键 H"
    bl_options = {'REGISTER', 'UNDO'}

    unselected: bpy.props.BoolProperty(
        name="未选中项",
        default=False,
        description="隐藏未选中项而不是选择项",
        update=lambda self, context: self.execute(context) 
    )

    def invoke(self, context, event):
        return self.execute(context)

    def draw(self, context):

        layout = self.layout
        split = layout.row().split(factor=0.4)
        
        # 左侧列 - 标签
        col_left = split.column()
        col_left.alignment = 'RIGHT'
        col_left.label(text="")
        
        # 右侧列 - 垂直排列的单选按钮
        col_right = split.column()
        col_right.prop(self, "unselected")

    def execute(self, context):
        typeandmode = bpy.context.active_object.type+bpy.context.active_object.mode
        
        if bpy.context.mode == "OBJECT":
            bpy.ops.object.hide_view_set(unselected=self.unselected)
        if typeandmode in {"CURVEEDIT","SURFACEEDIT"}:
            bpy.ops.curve.hide(unselected=self.unselected)
        if typeandmode == "METAEDIT":
            bpy.ops.mball.hide_metaelems(unselected=self.unselected)
        if typeandmode == "MESHEDIT":
            bpy.ops.mesh.hide(unselected=self.unselected)
        if typeandmode in {"GPENCILEDIT_GPENCIL","GPENCILPAINT_GPENCIL"}:
            bpy.ops.gpencil.hide(unselected=self.unselected)
        if typeandmode in {"GREASEPENCILEDIT","GREASEPENCILPAINT_GREASE_PENCIL"}:
            bpy.ops.grease_pencil.layer_hide(unselected=self.unselected)
        if typeandmode == "ARMATUREEDIT":
            bpy.ops.armature.hide(unselected=self.unselected)
        if typeandmode == "ARMATUREPOSE":
            bpy.ops.pose.hide(unselected=self.unselected)
        return {'FINISHED'}
    
# 多种编辑模式"显示隐藏项"
class BUTTON_ACTION_OT_global_hide_view_clear(bpy.types.Operator):
    bl_idname = "button.action_global_hide_view_clear"
    bl_label = "显示隐藏项"
    bl_description = "快捷键 Alt H"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        typeandmode = bpy.context.active_object.type+bpy.context.active_object.mode
        
        if bpy.context.mode == "OBJECT":
            bpy.ops.object.hide_view_clear()
        if typeandmode in {"CURVEEDIT","SURFACEEDIT"}:
            bpy.ops.curve.reveal()
        if typeandmode == "METAEDIT":
            bpy.ops.mball.reveal_metaelems()
        if typeandmode == "MESHEDIT":
            bpy.ops.mesh.reveal()
        if typeandmode in {"GPENCILEDIT_GPENCIL","GPENCILPAINT_GPENCIL"}:
            bpy.ops.gpencil.reveal()
        if typeandmode in {"GREASEPENCILEDIT","GREASEPENCILPAINT_GREASE_PENCIL"}:
            bpy.ops.grease_pencil.layer_reveal()
        if typeandmode == "ARMATUREEDIT":
            bpy.ops.armature.reveal()
        if typeandmode == "ARMATUREPOSE":
            bpy.ops.pose.reveal()
        return {'FINISHED'}
    
# 物体模式/骨骼姿态模式——“应用 Ctrl A”操作
class BUTTON_ACTION_OT_global_apply(bpy.types.Operator):
    bl_idname = "button.action_global_apply"
    bl_label = "应用"
    bl_description = "快捷键 Ctrl A"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        typeandmode = bpy.context.active_object.type+bpy.context.active_object.mode
        
        if bpy.context.mode == "OBJECT":
            bpy.ops.wm.call_menu(name="VIEW3D_MT_object_apply")
        elif typeandmode == "ARMATUREPOSE":
            bpy.ops.wm.call_menu(name="VIEW3D_MT_pose_apply")
        return {'FINISHED'}
    
# 物体模式/网格模式/骨骼姿态模式——“交互镜像 Ctrl M”操作
class BUTTON_ACTION_OT_global_transform_mirror(bpy.types.Operator):
    bl_idname = "button.action_global_transform_mirror"
    bl_label = "交互镜像"
    bl_description = "快捷键 Ctrl M"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.ops.transform.mirror('INVOKE_DEFAULT')    
        return {'FINISHED'}

# 物体模式/骨骼姿态“清空变换(菜单)”操作
class BUTTON_ACTION_OT_global_object_pose_clear(bpy.types.Operator):
    bl_idname = "button.action_global_object_pose_clear"
    bl_label = "清空变换"
    bl_description = "物体模式/骨骼姿态模式“清空变换”菜单"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        typeandmode = bpy.context.active_object.type+bpy.context.active_object.mode
        
        if bpy.context.mode == "OBJECT":
            bpy.ops.wm.call_menu(name="VIEW3D_MT_object_clear")
        elif typeandmode == "ARMATUREPOSE":
            bpy.ops.wm.call_menu(name="VIEW3D_MT_pose_transform")
        return {'FINISHED'}


classes = (
    # "视图"菜单
    BUTTON_ACTION_OT_global_view_align_selected_menu,
    BUTTON_ACTION_OT_global_call_view_align_selected_menu,
    BUTTON_ACTION_OT_global_view_selected,
    BUTTON_ACTION_OT_global_view_all,
    BUTTON_ACTION_OT_global_localview,
    BUTTON_ACTION_OT_global_object_as_camera,
    BUTTON_ACTION_OT_global_view_center_camera,
    BUTTON_ACTION_OT_global_view_viewpoint_menu,
    BUTTON_ACTION_OT_global_call_view_viewpoint_menu,
    BUTTON_ACTION_OT_global_view_navigation_menu,
    BUTTON_ACTION_OT_global_call_view_navigation_menu,
    BUTTON_ACTION_OT_global_zoom_border,
    BUTTON_ACTION_OT_global_zoom_camera_1_to_1,
    BUTTON_ACTION_OT_global_walk,
    BUTTON_ACTION_OT_global_fly,
    BUTTON_ACTION_OT_global_camera_to_view,
    BUTTON_ACTION_OT_global_camera_to_view_selected,
    BUTTON_ACTION_OT_global_call_view_align_menu,
    VIEW3D_MT_view_regions_menu,
    BUTTON_ACTION_OT_global_call_view_regions_menu,
    BUTTON_ACTION_OT_global_clip_border,
    BUTTON_ACTION_OT_global_render_border,
    BUTTON_ACTION_OT_global_lock_to_active_or_lock_clear,
    BUTTON_ACTION_OT_global_view_all_center_true,
    BUTTON_ACTION_OT_global_view_center_cursor,
    BUTTON_ACTION_OT_global_render_opengl,
    BUTTON_ACTION_OT_global_render_opengl_animation,
    BUTTON_ACTION_OT_global_render_opengl_keyframe,
    BUTTON_ACTION_OT_global_area_menu,
    BUTTON_ACTION_OT_global_screen_screen_full_area,

    #“选择”菜单
    BUTTON_ACTION_OT_global_select_all,
    BUTTON_ACTION_OT_global_select_invert,
    BUTTON_ACTION_OT_global_select_circle,
    BUTTON_ACTION_OT_global_select_select_mirror,
    BUTTON_ACTION_OT_global_select_select_random,
    VIEW3D_MT_global_select_more_or_less_menu,
    BUTTON_ACTION_OT_call_global_select_more_or_less_menu,
    BUTTON_ACTION_OT_global_select_select_parent_or_child,
    BUTTON_ACTION_OT_global_select_select_grouped,
    VIEW3D_MT_mesh_select_linked_menu,
    BUTTON_ACTION_OT_global_select_select_linked,
    BUTTON_ACTION_OT_global_select_select_pattern,
    BUTTON_ACTION_OT_global_select_select_similar,
    VIEW3D_MT_global_select_select_similar_menu,
    BUTTON_ACTION_OT_global_select_select_ungrouped,
    BUTTON_ACTION_OT_global_gpencil_select_select_first,
    BUTTON_ACTION_OT_global_gpencil_select_select_last,
    BUTTON_ACTION_OT_global_greasepencil_select_select_first,
    BUTTON_ACTION_OT_global_greasepencil_select_select_last,
    BUTTON_ACTION_OT_global_select_select_alternate,



    BUTTON_ACTION_OT_grab,
    BUTTON_ACTION_OT_scale,
    BUTTON_ACTION_OT_rotate,
    BUTTON_ACTION_OT_global_duplicate_move,
    BUTTON_ACTION_OT_global_add,
    BUTTON_ACTION_OT_global_copy,
    BUTTON_ACTION_OT_global_paste,
    BUTTON_ACTION_OT_call_global_delete_menu,
    VIEW3D_MT_global_delete_menu,
    BUTTON_ACTION_OT_global_hide_view_set,
    BUTTON_ACTION_OT_global_hide_view_clear,
    BUTTON_ACTION_OT_global_apply,
    BUTTON_ACTION_OT_global_transform_mirror,
    BUTTON_ACTION_OT_global_object_pose_clear,
)

def register():
    for cls in classes:
        bpy.utils.register_class(cls)

def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)




