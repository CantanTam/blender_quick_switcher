import bpy
from . import preference

def draw_add_to_switcher(self, context):
    show_switcher = bpy.context.preferences.addons[__package__].preferences.to_show_to_switcher
    if not show_switcher:
        return
    
    op = getattr(context, "operator", None) or getattr(context, "button_operator", None)
    # 检查右键对象是否为 Transform → Translate (Move)
    if op and op.bl_rna.identifier == "TRANSFORM_OT_translate":
        layout = self.layout
        layout.separator()
        layout.operator("call.add_to_switcher_menu", text="\"移动\"添加到Switcher", icon='EVENT_G').action = 'button.action_global_grab'
        layout.operator("call.add_to_switcher_menu", text="添加分隔符到Switcher", icon='REMOVE').action = 'SEPARATOR'
    elif op and op.bl_rna.identifier == "TRANSFORM_OT_resize":
        layout = self.layout
        layout.separator()
        layout.operator("call.add_to_switcher_menu", text="\"缩放\"添加到Switcher", icon='EVENT_S').action = 'button.action_global_scale'
        layout.operator("call.add_to_switcher_menu", text="添加分隔符到Switcher", icon='REMOVE').action = 'SEPARATOR'
    elif op and op.bl_rna.identifier == "TRANSFORM_OT_rotate":
        layout = self.layout
        layout.separator()
        layout.operator("call.add_to_switcher_menu", text="\"旋转\"添加到Switcher", icon='EVENT_R').action = 'button.action_global_rotate'
        layout.operator("call.add_to_switcher_menu", text="添加分隔符到Switcher", icon='REMOVE').action = 'SEPARATOR'
    elif op and op.bl_rna.identifier in {
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
    elif op and op.bl_rna.identifier in {
        "OBJECT_OT_duplicate_move",
        "CURVE_OT_duplicate_move",
        "MBALL_OT_duplicate_move",
        "GPENCIL_OT_duplicate_move", # 4.2 edition
        "GREASE_PENCIL_OT_duplicate_move", # 4.3 edition
        "MESH_OT_duplicate_move",
        "ARMATURE_OT_duplicate_move",
        }:
        layout = self.layout
        layout.separator()
        layout.operator("call.add_to_switcher_menu", text="\"复制\"添加到Switcher", icon='DUPLICATE').action = 'button.action_global_duplicate_move'
        layout.operator("call.add_to_switcher_menu", text="添加分隔符到Switcher", icon='REMOVE').action = 'SEPARATOR'
    elif op and op.bl_rna.identifier in {
        "VIEW3D_OT_copybuffer",
        "GPENCIL_OT_copy", # 4.2 edition
        "GREASE_PENCIL_OT_copy", # 4.3 edition
        "POSE_OT_copy",
        }:
        layout = self.layout
        layout.separator()
        layout.operator("call.add_to_switcher_menu", text="\"复制\"添加到Switcher", icon='COPYDOWN').action = 'button.action_global_copy'
        layout.operator("call.add_to_switcher_menu", text="添加分隔符到Switcher", icon='REMOVE').action = 'SEPARATOR'
    elif op and op.bl_rna.identifier in {
        "VIEW3D_OT_pastebuffer",
        "GPENCIL_OT_paste", # 4.2 edition
        "GREASE_PENCIL_OT_paste", # 4.3 edition
        "POSE_OT_paste",
        }:
        layout = self.layout
        layout.separator()
        layout.operator("call.add_to_switcher_menu", text="\"粘贴\"添加到Switcher", icon='PASTEDOWN').action = 'button.action_global_paste'
        layout.operator("call.add_to_switcher_menu", text="添加分隔符到Switcher", icon='REMOVE').action = 'SEPARATOR'
    elif op and op.bl_rna.identifier in {
        "OBJECT_OT_delete",
        "MBALL_OT_delete_metaelems",
        }:
        layout = self.layout
        layout.separator()
        layout.operator("call.add_to_switcher_menu", text="\"删除\"添加到Switcher", icon='EVENT_X').action = 'button.action_global_call_delete_menu'
        layout.operator("call.add_to_switcher_menu", text="添加分隔符到Switcher", icon='REMOVE').action = 'SEPARATOR'


#不能使用 draw_add_to_switcher 的添加到 Switcher 方法：
def add_menu_to_switcher(self, context):
    show_switcher = bpy.context.preferences.addons[__package__].preferences.to_show_to_switcher
    if not show_switcher:
        return
    self.layout.separator()
    self.layout.operator("call.add_to_switcher_menu", text="\"添加(菜单)\"添加到Switcher", icon='PLUS').action = 'button.action_global_add'
    self.layout.operator("call.add_to_switcher_menu", text="添加分隔符到Switcher", icon='REMOVE').action = 'SEPARATOR'

def delete_menu_to_switcher(self, context):
    show_switcher = bpy.context.preferences.addons[__package__].preferences.to_show_to_switcher
    if not show_switcher:
        return
    self.layout.separator()
    self.layout.operator("call.add_to_switcher_menu", text="\"删除(菜单)\"添加到Switcher", icon='EVENT_X').action = 'button.action_global_call_delete_menu'
    self.layout.operator("call.add_to_switcher_menu", text="添加分隔符到Switcher", icon='REMOVE').action = 'SEPARATOR'



switcher_panel = "panel1"
#switcher_column = "_col1"
#switcher_button = "_button1"
switcher_action = ""

class PANEL_OT_set_panels(bpy.types.Operator):
    bl_idname = "panel.set_panels"
    bl_label = "设置panel"
    
    panel: bpy.props.StringProperty(
        name="极速菜单",
        default="panel1"
    )

    def execute(self, context):
        global switcher_panel
        switcher_panel = self.panel
        self.report({'INFO'}, f"已切换到面板: {switcher_panel}")
        return {'FINISHED'}
    

class BUTTON_OT_set_buttons(bpy.types.Operator):
    bl_idname = "button.set_buttons"
    bl_label = "设置按钮位置"
    
    column: bpy.props.StringProperty(
        name="列",
        default="_col1"
    )

    button: bpy.props.StringProperty(
        name="按钮",
        default="_button1"
    )

    def execute(self, context):
        #global switcher_column
        #global switcher_button
        switcher_column = self.column
        switcher_button = self.button
        prefs = bpy.context.preferences.addons[__package__].preferences
        attr_name = f"{switcher_panel}{switcher_column}{switcher_button}"
        setattr(prefs, attr_name, switcher_action)
        # 完整保存流程
        try:
            # 1. 触发属性更新回调
            preference.update_preferences(prefs, context)
            
            # 2. 保存当前设置到内存
            prefs.save_to_file()
            
            # 3. 确保写入文件
            settings = {}
            for prop in prefs.bl_rna.properties:
                if not prop.is_readonly:
                    settings[prop.identifier] = getattr(prefs, prop.identifier)
            preference.save_settings(settings)
            
            self.report({'INFO'}, f"已保存按钮动作: {attr_name}={switcher_action}")
        except Exception as e:
            self.report({'ERROR'}, f"保存设置失败: {str(e)}")
            import traceback
            traceback.print_exc()
        return {'FINISHED'}

class CALL_OT_add_to_switcher_menu(bpy.types.Operator):
    bl_idname = "call.add_to_switcher_menu"
    bl_label = "添加到Switcher"

    action: bpy.props.StringProperty(
        name="动作",
        description="要执行的动作名称",
        default=""
    )

    def execute(self, context):
        return {'FINISHED'}

    def invoke(self, context, event):
        global switcher_action
        switcher_action = self.action  # 先设置动作
        # 显示弹出菜单
        return context.window_manager.invoke_popup(self, width=800)

    def draw(self, context):
        layout = self.layout

        # 创建三列布局并设置宽度比例 (col1最宽)
        row = layout.row()
        panel = row.column(align=True)
        col1 = row.column(align=True)  # col1占2份宽度
        col2 = row.column(align=True)  # col2占1份宽度 
        col3 = row.column(align=True)  # col3占1份宽度
        col4 = row.column(align=True)  # col4占1份宽度
        col5 = row.column(align=True)  # col5占1份宽度
        col6 = row.column(align=True)  # col6占1份宽度
        col7 = row.column(align=True)  # col7占1份宽度
        col8 = row.column(align=True)  # col8占1份宽度
        col9 = row.column(align=True)  # col9占1份宽度
        col10 = row.column(align=True) # col10占1份宽度

        panel.scale_x = 1.3  # col1 占较大比例
        # 扩展更多列设置
        for i in range(1, 11):
            col = getattr(self, f'col{i}', None)
            if col:
                col.scale_x = 1.0


        # 第一列标题和分隔符
        panel.label(text="选择超级菜单", icon='PRESET')
        for i in range(1, 11):
            panel.operator("panel.set_panels", text=f"超级菜单{i}", icon='TOPBAR').panel = f'panel{i}'

        # 第一列标题和分隔符
        col1.label(text="col1", icon='RADIOBUT_OFF')
        for i in range(1, 11):
            op = col1.operator("button.set_buttons", text="")
            op.column = '_col1'
            op.button = f'_button{i}'

        col2.label(text="col2", icon='RADIOBUT_OFF')
        for i in range(1, 11):
            op = col2.operator("button.set_buttons", text="")
            op.column = '_col2'
            op.button = f'_button{i}'

        col3.label(text="col3", icon='RADIOBUT_OFF')
        for i in range(1, 11):
            op = col3.operator("button.set_buttons", text="")
            op.column = '_col3'
            op.button = f'_button{i}'

        col4.label(text="col4", icon='RADIOBUT_OFF')
        for i in range(1, 11):
            op = col4.operator("button.set_buttons", text="")
            op.column = '_col4'
            op.button = f'_button{i}'

        col5.label(text="col5", icon='RADIOBUT_OFF')
        for i in range(1, 11):
            op = col5.operator("button.set_buttons", text="")
            op.column = '_col5'
            op.button = f'_button{i}'

        col6.label(text="col6", icon='RADIOBUT_OFF')
        for i in range(1, 11):
            op = col6.operator("button.set_buttons", text="")
            op.column = '_col6'
            op.button = f'_button{i}'

        col7.label(text="col7", icon='RADIOBUT_OFF')
        for i in range(1, 11):
            op = col7.operator("button.set_buttons", text="")
            op.column = '_col7'
            op.button = f'_button{i}'

        col8.label(text="col8", icon='RADIOBUT_OFF')
        for i in range(1, 11):
            op = col8.operator("button.set_buttons", text="")
            op.column = '_col8'
            op.button = f'_button{i}'

        col9.label(text="col9", icon='RADIOBUT_OFF')
        for i in range(1, 11):
            op = col9.operator("button.set_buttons", text="")
            op.column = '_col9'
            op.button = f'_button{i}'

        col10.label(text="col10", icon='RADIOBUT_OFF')
        for i in range(1, 11):
            op = col10.operator("button.set_buttons", text="")
            op.column = '_col10'
            op.button = f'_button{i}'
            
classes = (
    CALL_OT_add_to_switcher_menu,
    PANEL_OT_set_panels,
    BUTTON_OT_set_buttons,
)

def register():
    for cls in classes:
        bpy.utils.register_class(cls)
    bpy.types.UI_MT_button_context_menu.append(draw_add_to_switcher)
    #“添加”菜单
    bpy.types.VIEW3D_MT_add.append(add_menu_to_switcher)
    bpy.types.VIEW3D_MT_mesh_add.append(add_menu_to_switcher)
    bpy.types.VIEW3D_MT_curve_add.append(add_menu_to_switcher)
    bpy.types.VIEW3D_MT_surface_add.append(add_menu_to_switcher)
    bpy.types.VIEW3D_MT_metaball_add.append(add_menu_to_switcher)
    bpy.types.TOPBAR_MT_edit_armature_add.append(add_menu_to_switcher)

    #“删除”菜单
    bpy.types.VIEW3D_MT_edit_mesh_delete.append(delete_menu_to_switcher)
    if bpy.app.version <= (4, 2, 0):
        bpy.types.VIEW3D_MT_edit_gpencil_delete.append(delete_menu_to_switcher)    
    elif bpy.app.version >= (4, 3, 0):
        bpy.types.VIEW3D_MT_edit_greasepencil_delete.append(delete_menu_to_switcher)
    bpy.types.VIEW3D_MT_edit_armature_delete.append(delete_menu_to_switcher)
    bpy.types.VIEW3D_MT_edit_curve_delete.append(delete_menu_to_switcher)
    


def unregister():
    #“删除”菜单
    bpy.types.VIEW3D_MT_edit_mesh_delete.remove(delete_menu_to_switcher)
    bpy.types.VIEW3D_MT_edit_armature_delete.remove(delete_menu_to_switcher)
    bpy.types.VIEW3D_MT_edit_curve_delete.remove(delete_menu_to_switcher)
    if bpy.app.version <= (4, 2, 0):
        bpy.types.VIEW3D_MT_edit_gpencil_delete.remove(delete_menu_to_switcher)
    elif bpy.app.version >= (4, 3, 0):
        bpy.types.VIEW3D_MT_edit_greasepencil_delete.remove(delete_menu_to_switcher)

    #“添加”菜单
    bpy.types.TOPBAR_MT_edit_armature_add.remove(add_menu_to_switcher)
    bpy.types.VIEW3D_MT_metaball_add.remove(add_menu_to_switcher)
    bpy.types.VIEW3D_MT_surface_add.remove(add_menu_to_switcher)
    bpy.types.VIEW3D_MT_curve_add.remove(add_menu_to_switcher)
    bpy.types.VIEW3D_MT_mesh_add.remove(add_menu_to_switcher)
    bpy.types.VIEW3D_MT_add.remove(add_menu_to_switcher)

    bpy.types.UI_MT_button_context_menu.remove(draw_add_to_switcher)
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)
