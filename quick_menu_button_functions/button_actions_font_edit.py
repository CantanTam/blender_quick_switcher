import bpy

class ACTION_OT_font_select_all(bpy.types.Operator):
    bl_idname = "action.font_select_all"
    bl_label = "全选"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.ops.font.select_all()
        return {'FINISHED'}
    
class ACTION_OT_font_select_multi(bpy.types.Operator):
    bl_idname = "action.font_select_multi"
    bl_label = "选择文字"
    bl_options = {'REGISTER', 'UNDO'}

    type: bpy.props.EnumProperty(
        items=[
            ('TEXT_BEGIN',          "光标至文本头", ""),
            ('TEXT_END',            "光标至文本末", ""),
            ('PREVIOUS_PAGE',       "光标前十行", ""),
            ('NEXT_PAGE',           "光标后十行", ""),
            ('LINE_BEGIN',          "光标至行首", ""),
            ('LINE_END',            "光标至行末", ""),
            ('PREVIOUS_LINE',       "选择上一行", ""),
            ('NEXT_LINE',           "选择下一行", ""),
            ('PREVIOUS_WORD',       "前一个单词", ""),
            ('NEXT_WORD',           "后一个单词", ""),
            ('PREVIOUS_CHARACTER',  "前一个字符", ""),
            ('NEXT_CHARACTER',      "后一个字符", ""),
        ],
        default='LINE_BEGIN'
    )

    def invoke(self, context, event):
        return self.execute(context)

    def draw(self, context):
        layout = self.layout
        split = layout.row().split(factor=0.4)
        
        col_left = split.column()
        col_left.alignment = 'RIGHT'
        col_right = split.column()

        col_left.label(text="选择模式")
        col_right.prop(self, "type", text="abc", expand=True)

    def execute(self, context):
        bpy.ops.font.move_select(type=self.type)
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

classes = (
    ACTION_OT_font_select_all,
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

)    

def register():
    for cls in classes:
        bpy.utils.register_class(cls)

def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)