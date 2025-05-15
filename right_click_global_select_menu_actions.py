import bpy

def draw_add_to_switcher_global_select(self, context):
    show_switcher = bpy.context.preferences.addons[__package__].preferences.to_show_to_switcher
    if not show_switcher:
        return
    
    op = getattr(context, "operator", None) or getattr(context, "button_operator", None)
    # 检查右键对象是否为视图操作
    if op and op.bl_rna.identifier in {
        "OBJECT_OT_select_all",
        "CURVE_OT_select_all",
        "MBALL_OT_select_all",
        "FONT_OT_select_all",
        "LATTICE_OT_select_all",
        "MESH_OT_select_all",
        "GPENCIL_OT_select_all",    #4.2 版本或以下
        "GREASE_PENCIL_OT_select_all", #4.3 版本或以上
        "ARMATURE_OT_select_all",
        "POSE_OT_select_all",
        }:
        layout = self.layout
        layout.separator()
        layout.operator("call.add_to_switcher_menu", text="\"全选\"添加到Switcher", icon='EVENT_A').action = 'button.action_global_select_all'
        layout.operator("call.add_to_switcher_menu", text="\"反选\"添加到Switcher", icon='PLUS').action = 'button.action_global_select_invert'
        layout.operator("call.add_to_switcher_menu", text="添加分隔符到Switcher", icon='REMOVE').action = 'SEPARATOR'

    elif op and op.bl_rna.identifier == "VIEW3D_OT_select_circle":
        layout = self.layout
        layout.separator()
        layout.operator("call.add_to_switcher_menu", text="\"刷选\"添加到Switcher", icon='EVENT_C').action = 'button.action_global_select_circle'
        layout.operator("call.add_to_switcher_menu", text="添加分隔符到Switcher", icon='REMOVE').action = 'SEPARATOR'

    elif op and op.bl_rna.identifier == "OBJECT_OT_select_by_type":
        layout = self.layout
        layout.separator()
        layout.operator("call.add_to_switcher_menu", text="\"按类型全选(菜单)\"添加到Switcher", icon='PRESET').action = 'button.action_call_select_select_by_type_menu'
        layout.operator("call.add_to_switcher_menu", text="添加分隔符到Switcher", icon='REMOVE').action = 'SEPARATOR'

    elif op and op.bl_rna.identifier == "OBJECT_OT_select_camera":
        layout = self.layout
        layout.separator()
        layout.operator("call.add_to_switcher_menu", text="\"选择活动摄像机\"添加到Switcher", icon='OUTLINER_OB_CAMERA').action = 'object.select_camera'
        layout.operator("call.add_to_switcher_menu", text="添加分隔符到Switcher", icon='REMOVE').action = 'SEPARATOR'

    elif op and op.bl_rna.identifier in {
        "OBJECT_OT_select_mirror",
        "LATTICE_OT_select_mirror",
        "MESH_OT_select_mirror",
        "ARMATURE_OT_select_mirror",
        "POSE_OT_select_mirror",
        }:
        layout = self.layout
        layout.separator()
        layout.operator("call.add_to_switcher_menu", text="\"选择镜像\"添加到Switcher", icon='MOD_MIRROR').action = 'button.action_select_select_mirror'
        layout.operator("call.add_to_switcher_menu", text="添加分隔符到Switcher", icon='REMOVE').action = 'SEPARATOR'

    elif op and op.bl_rna.identifier in {
        "OBJECT_OT_select_random",
        "MESH_OT_select_random",
        "CURVE_OT_select_random",
        "MBALL_OT_select_random_metaelems",
        "GPENCIL_OT_select_random",
        "GREASE_PENCIL_OT_select_random",
        "LATTICE_OT_select_random",
        }:
        layout = self.layout
        layout.separator()
        layout.operator("call.add_to_switcher_menu", text="\"随机选择\"添加到Switcher", icon='RADIOBUT_OFF').action = 'button.action_select_select_random'
        layout.operator("call.add_to_switcher_menu", text="添加分隔符到Switcher", icon='REMOVE').action = 'SEPARATOR'


def register():
    bpy.types.UI_MT_button_context_menu.append(draw_add_to_switcher_global_select)


def unregister():
    bpy.types.UI_MT_button_context_menu.remove(draw_add_to_switcher_global_select)
