import bpy

# "选择"菜单——按类型全选
class BUTTON_ACTION_OT_object_select_select_by_type_menu(bpy.types.Operator):
    bl_label = ""
    bl_idname = "button.action_object_select_select_by_type_menu"

    def execute(self, context):
        def draw(self, context):
            layout = self.layout
            
            layout.operator("object.select_by_type", text="网格", icon="OUTLINER_OB_MESH").type='MESH'
            layout.operator("object.select_by_type", text="曲线", icon="OUTLINER_OB_CURVE").type='CURVE'
            layout.operator("object.select_by_type", text="表面", icon="OUTLINER_OB_SURFACE").type='SURFACE'
            layout.operator("object.select_by_type", text="元球", icon="OUTLINER_OB_META").type='META'
            layout.operator("object.select_by_type", text="文本", icon="OUTLINER_OB_FONT").type='FONT'
            layout.operator("object.select_by_type", text="毛发曲线", icon="OUTLINER_OB_CURVES").type='CURVES'
            layout.operator("object.select_by_type", text="点云", icon="OUTLINER_OB_POINTCLOUD").type='POINTCLOUD'
            layout.operator("object.select_by_type", text="体积", icon="OUTLINER_OB_VOLUME").type='VOLUME'
            if bpy.app.version >= (4,3,0):
                layout.operator("object.select_by_type", text="蜡笔", icon="OUTLINER_OB_GREASEPENCIL").type='GPENCIL'
                layout.operator("object.select_by_type", text="蜡笔V3版", icon="OUTLINER_OB_GREASEPENCIL").type='GREASEPENCIL'
            else:
                layout.operator("object.select_by_type", text="蜡笔", icon="OUTLINER_OB_GREASEPENCIL").type='GPENCIL'
            layout.separator()
            layout.operator("object.select_by_type", text="骨骼", icon="OUTLINER_OB_ARMATURE").type='ARMATURE'
            layout.operator("object.select_by_type", text="晶格", icon="OUTLINER_OB_LATTICE").type='LATTICE'
            layout.separator()
            layout.operator("object.select_by_type", text="空物体", icon="OUTLINER_OB_EMPTY").type='EMPTY'
            layout.separator()
            layout.operator("object.select_by_type", text="灯光", icon="OUTLINER_OB_LIGHT").type='LIGHT'
            layout.operator("object.select_by_type", text="光照探头", icon="OUTLINER_OB_LIGHTPROBE").type='LIGHT_PROBE'
            layout.separator()
            layout.operator("object.select_by_type", text="摄像机", icon="OUTLINER_OB_CAMERA").type='CAMERA'
            layout.separator()
            layout.operator("object.select_by_type", text="扬声器", icon="OUTLINER_OB_SPEAKER").type='SPEAKER'
        context.window_manager.popup_menu(draw, title="按类型全选")
        return {'FINISHED'}



classes = (
    BUTTON_ACTION_OT_object_select_select_by_type_menu,

)

def register():
    for cls in classes:
        bpy.utils.register_class(cls)

def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)