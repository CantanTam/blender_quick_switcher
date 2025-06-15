import bpy

class ACTION_OT_font_select_all(bpy.types.Operator):
    bl_idname = "action.font_select_all"
    bl_label = "全选"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.ops.font.select_all()
        return {'FINISHED'}
    
class ACTION_OT_font_select_multi_menu(bpy.types.Operator):
    bl_idname = "action.font_select_multi_menu"
    bl_label = "选择文字"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        return {'FINISHED'}

    def invoke(self, context, event):
        return context.window_manager.invoke_popup(self, width=100)

    def draw(self, context):
        layout = self.layout
        row = layout.row()
        col = row.column(align=True)
        col.label(text="选择文字", icon='WORDWRAP_ON')
        col.operator("font.move_select", text="光标至文本头", icon="RADIOBUT_OFF").type = 'TEXT_BEGIN'
        col.operator("font.move_select", text="光标至文本末", icon="RADIOBUT_OFF").type = 'TEXT_END'
        col.separator()
        col.operator("font.move_select", text="光标前十行", icon="RADIOBUT_OFF").type = 'PREVIOUS_PAGE'
        col.operator("font.move_select", text="光标后十行", icon="RADIOBUT_OFF").type = 'NEXT_PAGE'
        col.separator()
        col.operator("font.move_select", text="光标至行首", icon="RADIOBUT_OFF").type = 'LINE_BEGIN'
        col.operator("font.move_select", text="光标至行末", icon="RADIOBUT_OFF").type = 'LINE_END'
        col.separator()
        col.operator("font.move_select", text="选择上一行", icon="RADIOBUT_OFF").type = 'PREVIOUS_LINE'
        col.operator("font.move_select", text="选择下一行", icon="RADIOBUT_OFF").type = 'NEXT_LINE'
        col.separator()
        col.operator("font.move_select", text="前一个单词", icon="RADIOBUT_OFF").type = 'PREVIOUS_WORD'
        col.operator("font.move_select", text="后一个单词", icon="RADIOBUT_OFF").type = 'NEXT_WORD'
        col.separator()
        col.operator("font.move_select", text="前一个字符", icon="RADIOBUT_OFF").type = 'PREVIOUS_CHARACTER'
        col.operator("font.move_select", text="后一个字符", icon="RADIOBUT_OFF").type = 'NEXT_CHARACTER'


class ACTION_OT_font_select_multi(bpy.types.Operator):
    bl_idname = "action.font_select_multi"
    bl_label = "选择文字"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.ops.action.font_select_multi_menu('INVOKE_DEFAULT')
        return {'FINISHED'}

class ACTION_OT_font_select_text_begin(bpy.types.Operator):
    bl_idname = "action.font_select_text_begin"
    bl_label = "光标至文本头"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.ops.font.move_select(type='TEXT_BEGIN')
        return {'FINISHED'}

class ACTION_OT_font_select_text_end(bpy.types.Operator):
    bl_idname = "action.font_select_text_end"
    bl_label = "光标至文本末"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.ops.font.move_select(type='TEXT_END')
        return {'FINISHED'}

class ACTION_OT_font_select_previous_page(bpy.types.Operator):
    bl_idname = "action.font_select_previous_page"
    bl_label = "光标前十行"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.ops.font.move_select(type='PREVIOUS_PAGE')
        return {'FINISHED'}

class ACTION_OT_font_select_next_page(bpy.types.Operator):
    bl_idname = "action.font_select_next_page"
    bl_label = "光标后十行"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.ops.font.move_select(type='NEXT_PAGE')
        return {'FINISHED'}

class ACTION_OT_font_select_line_begin(bpy.types.Operator):
    bl_idname = "action.font_select_line_begin"
    bl_label = "光标至行首"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.ops.font.move_select(type='LINE_BEGIN')
        return {'FINISHED'}

class ACTION_OT_font_select_line_end(bpy.types.Operator):
    bl_idname = "action.font_select_line_end"
    bl_label = "光标至行末"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.ops.font.move_select(type='LINE_END')
        return {'FINISHED'}

class ACTION_OT_font_select_previous_line(bpy.types.Operator):
    bl_idname = "action.font_select_previous_line"
    bl_label = "选择上一行"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.ops.font.move_select(type='PREVIOUS_LINE')
        return {'FINISHED'}

class ACTION_OT_font_select_next_line(bpy.types.Operator):
    bl_idname = "action.font_select_next_line"
    bl_label = "选择下一行"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.ops.font.move_select(type='NEXT_LINE')
        return {'FINISHED'}

class ACTION_OT_font_select_previous_word(bpy.types.Operator):
    bl_idname = "action.font_select_previous_word"
    bl_label = "前一个单词"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.ops.font.move_select(type='PREVIOUS_WORD')
        return {'FINISHED'}

class ACTION_OT_font_select_next_word(bpy.types.Operator):
    bl_idname = "action.font_select_next_word"
    bl_label = "后一个单词"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.ops.font.move_select(type='NEXT_WORD')
        return {'FINISHED'}

class ACTION_OT_font_text_cut(bpy.types.Operator):
    bl_idname = "action.font_text_cut"
    bl_label = "剪切"
    bl_description = "快捷键 Ctrl X"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.ops.font.text_cut()
        return {'FINISHED'}

class ACTION_OT_font_text_copy(bpy.types.Operator):
    bl_idname = "action.font_text_copy"
    bl_label = "复制"
    bl_description = "快捷键 Ctrl C"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.ops.font.text_copy()
        return {'FINISHED'}

class ACTION_OT_font_text_paste(bpy.types.Operator):
    bl_idname = "action.font_text_paste"
    bl_label = "粘贴文本"
    bl_description = "快捷键 Ctrl V"
    bl_options = {'REGISTER', 'UNDO'}

    selection: bpy.props.BoolProperty(
        default=False,
    )

    def invoke(self, context, event):
        return self.execute(context)

    def draw(self, context):
        layout = self.layout
        split = layout.row().split(factor=0.4)
        
        col_left = split.column()
        col_left.alignment = 'RIGHT'
        col_right = split.column()

        col_left.label(text="")
        col_right.prop(self, "selection", text="选中项(Linux有效)")

    def execute(self, context):
        bpy.ops.font.text_paste(selection=self.selection)
        return {'FINISHED'}

class ACTION_OT_font_text_paste_from_file(bpy.types.Operator):
    bl_idname = "action.font_text_paste_from_file"
    bl_label = "粘贴文件"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.ops.font.text_paste_from_file('INVOKE_DEFAULT')
        return {'FINISHED'}

class ACTION_OT_font_case_set(bpy.types.Operator):
    bl_idname = "action.font_case_set"
    bl_label = "切换大小写"
    bl_options = {'REGISTER', 'UNDO'}

    case: bpy.props.EnumProperty(
        name="大小写",
        items=[
            ('UPPER', "大写", ""),
            ('LOWER', "小写", ""),
        ],
        default='LOWER'
    )

    def invoke(self, context, event):
        return self.execute(context)

    def draw(self, context):
        layout = self.layout
        split = layout.row().split(factor=0.4)
        
        col_left = split.column()
        col_left.alignment = 'RIGHT'
        col_right = split.column()

        col_left.label(text="大小写")
        col_right.prop(self, "case", text="abc", expand=True)

    def execute(self, context):
        bpy.ops.font.case_set(case=self.case)
        return {'FINISHED'}

class ACTION_OT_font_edit_font_chars_menu(bpy.types.Operator):
    bl_idname = "action.font_edit_font_chars_menu"
    bl_label = "特殊字符"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.ops.wm.call_menu(name="VIEW3D_MT_edit_font_chars")
        return {'FINISHED'}

class ACTION_OT_font_style_toggle_bold(bpy.types.Operator):
    bl_idname = "action.font_style_toggle_bold"
    bl_label = "字体样式"
    bl_options = {'REGISTER', 'UNDO'}

    style: bpy.props.EnumProperty(
        items=[
            ('BOLD',        "粗体",   "", 'BOLD',      0),
            ('ITALIC',      "斜体",   "", 'ITALIC',    1),
            ('UNDERLINE',   "下划线",  "", 'UNDERLINE', 2),
            ('SMALL_CAPS', "小型大写", "", 'SMALL_CAPS', 3),
        ],
        default='BOLD',
    )

    def invoke(self, context, event):
        return self.execute(context)

    def draw(self, context):
        layout = self.layout
        split = layout.row().split(factor=0.4)
        
        col_left = split.column()
        col_left.alignment = 'RIGHT'
        col_right = split.column()

        col_left.label(text="样式")
        col_right.prop(self, "style", text="abc", expand=True)

    def execute(self, context):
        bpy.ops.font.style_toggle(style=self.style)
        return {'FINISHED'}

class ACTION_OT_font_style_toggle_italic(bpy.types.Operator):
    bl_idname = "action.font_style_toggle_italic"
    bl_label = "字体样式"
    bl_options = {'REGISTER', 'UNDO'}

    style: bpy.props.EnumProperty(
        items=[
            ('BOLD',        "粗体",   "", 'BOLD',      0),
            ('ITALIC',      "斜体",   "", 'ITALIC',    1),
            ('UNDERLINE',   "下划线",  "", 'UNDERLINE', 2),
            ('SMALL_CAPS', "小型大写", "", 'SMALL_CAPS', 3),
        ],
        default='ITALIC',
    )

    def invoke(self, context, event):
        return self.execute(context)

    def draw(self, context):
        layout = self.layout
        split = layout.row().split(factor=0.4)
        
        col_left = split.column()
        col_left.alignment = 'RIGHT'
        col_right = split.column()

        col_left.label(text="样式")
        col_right.prop(self, "style", text="abc", expand=True)

    def execute(self, context):
        bpy.ops.font.style_toggle(style=self.style)
        return {'FINISHED'}

class ACTION_OT_font_style_toggle_underline(bpy.types.Operator):
    bl_idname = "action.font_style_toggle_underline"
    bl_label = "字体样式"
    bl_options = {'REGISTER', 'UNDO'}

    style: bpy.props.EnumProperty(
        items=[
            ('BOLD',        "粗体",   "", 'BOLD',      0),
            ('ITALIC',      "斜体",   "", 'ITALIC',    1),
            ('UNDERLINE',   "下划线",  "", 'UNDERLINE', 2),
            ('SMALL_CAPS', "小型大写", "", 'SMALL_CAPS', 3),
        ],
        default='UNDERLINE',
    )

    def invoke(self, context, event):
        return self.execute(context)

    def draw(self, context):
        layout = self.layout
        split = layout.row().split(factor=0.4)
        
        col_left = split.column()
        col_left.alignment = 'RIGHT'
        col_right = split.column()

        col_left.label(text="样式")
        col_right.prop(self, "style", text="abc", expand=True)

    def execute(self, context):
        bpy.ops.font.style_toggle(style=self.style)
        return {'FINISHED'}
    
class ACTION_OT_font_style_toggle_smallcaps(bpy.types.Operator):
    bl_idname = "action.font_style_toggle_smallcaps"
    bl_label = "字体样式"
    bl_options = {'REGISTER', 'UNDO'}

    style: bpy.props.EnumProperty(
        items=[
            ('BOLD',        "粗体",   "", 'BOLD',      0),
            ('ITALIC',      "斜体",   "", 'ITALIC',    1),
            ('UNDERLINE',   "下划线",  "", 'UNDERLINE', 2),
            ('SMALL_CAPS', "小型大写", "", 'SMALL_CAPS', 3),
        ],
        default='SMALL_CAPS',
    )

    def invoke(self, context, event):
        return self.execute(context)

    def draw(self, context):
        layout = self.layout
        split = layout.row().split(factor=0.4)
        
        col_left = split.column()
        col_left.alignment = 'RIGHT'
        col_right = split.column()

        col_left.label(text="样式")
        col_right.prop(self, "style", text="abc", expand=True)

    def execute(self, context):
        bpy.ops.font.style_toggle(style=self.style)
        return {'FINISHED'}

class VIEW3D_MT_font_change_spacing_menu(bpy.types.Operator):
    bl_idname = "popup.font_change_spacing_menu"
    bl_label = "调整字距"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        return {'FINISHED'}

    def invoke(self, context, event):
        return context.window_manager.invoke_popup(self, width=100)

    def draw(self, context):
        layout = self.layout
        row = layout.row()
        col = row.column(align=True)
        col.label(text="调整字距", icon='FILE_FONT')
        col.operator("font.change_spacing", text="调高字距", icon="ADD").delta=1
        col.operator("font.change_spacing", text="调低字距", icon="REMOVE").delta=-1
        col.separator()
        col.operator("font.change_spacing", text="调高字距(5倍)", icon="ADD").delta=5
        col.operator("font.change_spacing", text="调低字距(5倍)", icon="REMOVE").delta=-5
        col.separator()
        col.operator("ed.undo", text="撤销", icon="LOOP_BACK")
        col.operator("ed.redo", text="重做", icon="LOOP_FORWARDS")

class ACTION_OT_font_call_change_spacing_menu(bpy.types.Operator):
    bl_idname = "action.font_call_change_spacing_menu"
    bl_label = "调整字距"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.ops.popup.font_change_spacing_menu('INVOKE_DEFAULT')
        return {'FINISHED'}
    
class VIEW3D_MT_font_delete_menu(bpy.types.Operator):
    bl_idname = "popup.font_delete_menu"
    bl_label = "删除文本"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        return {'FINISHED'}

    def invoke(self, context, event):
        return context.window_manager.invoke_popup(self, width=100)

    def draw(self, context):
        layout = self.layout
        row = layout.row()
        col = row.column(align=True)
        col.label(text="删除文本")
        col.operator("font.delete", text="删除选中内容", icon="RADIOBUT_OFF").type = 'SELECTION'
        col.separator()
        col.operator("font.delete", text="删除前一字符", icon="RADIOBUT_OFF").type = 'PREVIOUS_CHARACTER'
        col.operator("font.delete", text="删除后一字符", icon="RADIOBUT_OFF").type = 'NEXT_CHARACTER'
        col.separator()
        col.operator("font.delete", text="删除前一单词", icon="RADIOBUT_OFF").type = 'PREVIOUS_WORD'
        col.operator("font.delete", text="删除后一单词", icon="RADIOBUT_OFF").type = 'NEXT_WORD'
        col.separator()
        col.operator("font.delete", text="选中或后一字符", icon="RADIOBUT_OFF").type = 'NEXT_OR_SELECTION'
        col.operator("font.delete", text="选中或前一字符", icon="RADIOBUT_OFF").type = 'PREVIOUS_OR_SELECTION'
        col.separator()
        col.operator("ed.undo", text="撤销", icon="LOOP_BACK")
        col.operator("ed.redo", text="重做", icon="LOOP_FORWARDS")

class ACTION_OT_font_delete(bpy.types.Operator):
    bl_idname = "action.font_delete"
    bl_label = "删除文本"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.ops.popup.font_delete_menu('INVOKE_DEFAULT')
        return {'FINISHED'}


classes = (
    ACTION_OT_font_select_all,
    ACTION_OT_font_select_multi_menu,
    ACTION_OT_font_select_multi,
    ACTION_OT_font_select_text_begin,
    ACTION_OT_font_select_text_end,
    ACTION_OT_font_select_previous_page,
    ACTION_OT_font_select_next_page,
    ACTION_OT_font_select_line_begin,
    ACTION_OT_font_select_line_end,
    ACTION_OT_font_select_previous_line,
    ACTION_OT_font_select_next_line,
    ACTION_OT_font_select_previous_word,
    ACTION_OT_font_select_next_word,

    ACTION_OT_font_text_cut,
    ACTION_OT_font_text_copy,
    ACTION_OT_font_text_paste,
    ACTION_OT_font_text_paste_from_file,
    ACTION_OT_font_case_set,
    ACTION_OT_font_edit_font_chars_menu,
    ACTION_OT_font_style_toggle_bold,
    ACTION_OT_font_style_toggle_italic,
    ACTION_OT_font_style_toggle_underline,
    ACTION_OT_font_style_toggle_smallcaps,
    VIEW3D_MT_font_change_spacing_menu,
    ACTION_OT_font_call_change_spacing_menu,
    VIEW3D_MT_font_delete_menu,
    ACTION_OT_font_delete,


)    

def register():
    for cls in classes:
        bpy.utils.register_class(cls)

def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)