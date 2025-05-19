import bpy
from . import preference

switcher_panel = "panelone"
switcher_mode = "_mode1"
switcher_column = "_col1"
switcher_button = "_button1"
switcher_action = ""

class PANEL_OT_set_panels(bpy.types.Operator):
    bl_idname = "panel.set_panels"
    bl_label = "设置panel"
    
    panel: bpy.props.StringProperty(
        name="极速菜单",
        default="panelone"
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

    mode: bpy.props.StringProperty(
        name="按钮",
        default="_mode1"
    ) 

    def execute(self, context):
        #global switcher_column
        #global switcher_button
        typeandmode = bpy.context.active_object.type+bpy.context.active_object.mode
        if bpy.context.active_object.mode == "OBJECT":
            self.mode = "_mode1"
        elif typeandmode == "MESHEDIT":
            self.mode = "_mode2"
        elif typeandmode == "MESHSCULPT":
            self.mode = "_mode3"
        elif typeandmode == "MESHVERTEX_PAINT":
            self.mode = "_mode4"
        elif typeandmode == "MESHWEIGHT_PAINT":
            self.mode = "_mode5"
        elif typeandmode == "MESHTEXTURE_PAINT":
            self.mode = "_mode6"
        elif typeandmode == "GPENCILEDIT_GPENCIL":
            self.mode = "_mode7"
        elif typeandmode == "GPENCILSCULPT_GPENCIL":
            self.mode = "_mode8"
        elif typeandmode == "GPENCILPAINT_GPENCIL":
            self.mode = "_mode9"
        elif typeandmode == "GPENCILWEIGHT_GPENCIL":
            self.mode = "_mode10"
        elif typeandmode == "GPENCILVERTEX_GPENCIL":
            self.mode = "_mode11"
        elif typeandmode == "GREASEPENCILEDIT":
            self.mode = "_mode12"
        elif typeandmode == "GREASEPENCILSCULPT_GREASE_PENCIL":
            self.mode = "_mode13"
        elif typeandmode == "GREASEPENCILPAINT_GREASE_PENCIL":
            self.mode = "_mode14"
        elif typeandmode == "GREASEPENCILWEIGHT_GREASE_PENCIL":
            self.mode = "_mode15"
        elif typeandmode == "GREASEPENCILVERTEX_GREASE_PENCIL":
            self.mode = "_mode16"
        elif typeandmode == "ARMATUREEDIT":
            self.mode = "_mode17"
        elif typeandmode == "ARMATUREPOSE":
            self.mode = "_mode18"
        elif typeandmode == "CURVEEDIT":
            self.mode = "_mode19"
        elif typeandmode == "SURFACEEDIT":
            self.mode = "_mode20"
        elif typeandmode == "METAEDIT":
            self.mode = "_mode21"
        elif typeandmode == "FONTEDIT":
            self.mode = "_mode22"
        elif typeandmode == "LATTICEEDIT":
            self.mode = "_mode23"

        switcher_mode = self.mode
        switcher_column = self.column
        switcher_button = self.button
        prefs = bpy.context.preferences.addons[__package__].preferences
        attr_name = f"{switcher_panel}{switcher_mode}{switcher_column}{switcher_button}"
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
        typeandmode =  bpy.context.active_object.type+" "+bpy.context.active_object.mode+" mode"
        layout = self.layout
        layout.label(text="OBJECT mode" if bpy.context.active_object.mode == "OBJECT" else typeandmode)
        # 创建三列布局并设置宽度比例 (col1最宽)
        row = layout.row()
        col0 = row.column(align=True)
        col1 = row.column(align=True)  # col1占2份宽度
        col2 = row.column(align=True)  # col2占1份宽度 
        col3 = row.column(align=True)  # col3占1份宽度
        col4 = row.column(align=True)  # col4占1份宽度
        col5 = row.column(align=True)  # col5占1份宽度
        col6 = row.column(align=True)  # col6占1份宽度
        col7 = row.column(align=True)  # col7占1份宽度
        col8 = row.column(align=True)  # col8占1份宽度

        col0.scale_x = 1.1  # col1 占较大比例
        # 扩展更多列设置
        for i in range(1, 11):
            col = getattr(self, f'col{i}', None)
            if col:
                col.scale_x = 1.0


        # 一列标题和分隔符
        col0.label(text="选择超级菜单", icon='PRESET')
        col0.operator("panel.set_panels", text="超级菜单1", icon='COLLECTION_COLOR_01' if switcher_panel == "panelone" else "COLLECTION_NEW").panel = "panelone"
        col0.operator("panel.set_panels", text="超级菜单2", icon='COLLECTION_COLOR_02' if switcher_panel == "paneltwo" else "COLLECTION_NEW").panel = "paneltwo"
        col0.operator("panel.set_panels", text="超级菜单3", icon='COLLECTION_COLOR_03' if switcher_panel == "panelthree" else "COLLECTION_NEW").panel = "panelthree"
        col0.operator("panel.set_panels", text="超级菜单4", icon='COLLECTION_COLOR_04' if switcher_panel == "panelfour" else "COLLECTION_NEW").panel = "panelfour"
        col0.operator("panel.set_panels", text="超级菜单5", icon='COLLECTION_COLOR_05' if switcher_panel == "panelfive" else "COLLECTION_NEW").panel = "panelfive"

        # 一列标题和分隔符
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

classes = (
    CALL_OT_add_to_switcher_menu,
    PANEL_OT_set_panels,
    BUTTON_OT_set_buttons,
)

def register():
    for cls in classes:
        bpy.utils.register_class(cls)

def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)
