import bpy
from .. import ADDON_NAME

def draw_add_to_switcher_font(self, context):

    show_switcher = bpy.context.preferences.addons[ADDON_NAME].preferences.to_show_to_switcher
    if not show_switcher:
        return
    
    op = getattr(context, "operator", None) or getattr(context, "button_operator", None)

    if op and op.bl_rna.identifier == "FONT_OT_select_all":
        layout = self.layout
        layout.separator()
        layout.operator("call.add_to_switcher_menu", text="\"全选\"⟶Switcher", icon='RADIOBUT_OFF').action = 'action.font_select_all'

    elif op and op.bl_rna.identifier == "FONT_OT_move_select":
        layout = self.layout
        layout.separator()
        layout.operator("call.add_to_switcher_menu", text="\"光标至文本头\"⟶Switcher", icon='RADIOBUT_OFF').action = 'action.font_select_text_begin'
        layout.operator("call.add_to_switcher_menu", text="\"光标至文本末\"⟶Switcher", icon='RADIOBUT_OFF').action = 'action.font_select_text_end'
        layout.separator()
        layout.operator("call.add_to_switcher_menu", text="\"光标前十行\"⟶Switcher", icon='RADIOBUT_OFF').action = 'action.font_select_previous_page'
        layout.operator("call.add_to_switcher_menu", text="\"光标后十行\"⟶Switcher", icon='RADIOBUT_OFF').action = 'action.font_select_next_page'
        layout.separator()
        layout.operator("call.add_to_switcher_menu", text="\"光标至行首\"⟶Switcher", icon='RADIOBUT_OFF').action = 'action.font_select_line_begin'
        layout.operator("call.add_to_switcher_menu", text="\"光标至行末\"⟶Switcher", icon='RADIOBUT_OFF').action = 'action.font_select_line_end'
        layout.separator()
        layout.operator("call.add_to_switcher_menu", text="\"选择上一行\"⟶Switcher", icon='RADIOBUT_OFF').action = 'action.font_select_previous_line'
        layout.operator("call.add_to_switcher_menu", text="\"选择下一行\"⟶Switcher", icon='RADIOBUT_OFF').action = 'action.font_select_next_line'
        layout.separator()
        layout.operator("call.add_to_switcher_menu", text="\"前一个单词\"⟶Switcher", icon='RADIOBUT_OFF').action = 'action.font_select_previous_word'
        layout.operator("call.add_to_switcher_menu", text="\"后一个单词\"⟶Switcher", icon='RADIOBUT_OFF').action = 'action.font_select_next_word'

    elif op and op.bl_rna.identifier == "FONT_OT_text_cut":
        layout = self.layout
        layout.separator()
        layout.operator("call.add_to_switcher_menu", text="\"剪切\"⟶Switcher", icon='RADIOBUT_OFF').action = 'action.font_text_cut'

    elif op and op.bl_rna.identifier == "FONT_OT_text_copy":
        layout = self.layout
        layout.separator()
        layout.operator("call.add_to_switcher_menu", text="\"复制\"⟶Switcher", icon='COPYDOWN').action = 'action.font_text_copy'

    elif op and op.bl_rna.identifier == "FONT_OT_text_paste":
        layout = self.layout
        layout.separator()
        layout.operator("call.add_to_switcher_menu", text="\"粘贴\"⟶Switcher", icon='PASTEDOWN').action = 'action.font_text_paste'

    elif op and op.bl_rna.identifier == "FONT_OT_text_paste_from_file":
        layout = self.layout
        layout.separator()
        layout.operator("call.add_to_switcher_menu", text="\"粘贴文件\"⟶Switcher", icon='PLUS').action = 'action.font_text_paste_from_file'

    elif op and op.bl_rna.identifier == "FONT_OT_case_set":
        layout = self.layout
        layout.separator()
        layout.operator("call.add_to_switcher_menu", text="\"切换大小写\"⟶Switcher", icon='OUTLINER_OB_FONT').action = 'action.font_case_set'
    
    elif op and op.bl_rna.identifier == "FONT_OT_style_toggle":
        layout = self.layout
        layout.separator()
        layout.operator("call.add_to_switcher_menu", text="\"粗体\"⟶Switcher", icon='BOLD').action = 'action.font_style_toggle_bold'
        layout.operator("call.add_to_switcher_menu", text="\"斜体\"⟶Switcher", icon='ITALIC').action = 'action.font_style_toggle_italic'
        layout.operator("call.add_to_switcher_menu", text="\"下划线\"⟶Switcher", icon='UNDERLINE').action = 'action.font_style_toggle_underline'
        layout.operator("call.add_to_switcher_menu", text="\"小型大写\"⟶Switcher", icon='SMALL_CAPS').action = 'action.font_style_toggle_smallcaps'





def fontedit_select_text_to_switcher(self, context):
    show_switcher = bpy.context.preferences.addons[ADDON_NAME].preferences.to_show_to_switcher
    if not show_switcher:
        return
    self.layout.separator()
    self.layout.operator("call.add_to_switcher_menu", text="\"选择文字\"⟶Switcher", icon='WORDWRAP_ON').action = 'action.font_select_multi'


def fontedit_font_chars_menu_to_switcher(self, context):
    show_switcher = bpy.context.preferences.addons[ADDON_NAME].preferences.to_show_to_switcher
    if not show_switcher:
        return
    self.layout.separator()
    self.layout.operator("call.add_to_switcher_menu", text="\"特殊字符\"⟶Switcher", icon='PRESET').action = 'action.font_edit_font_chars_menu'

def fontedit_change_spacing_menu_to_switcher(self, context):
    show_switcher = bpy.context.preferences.addons[ADDON_NAME].preferences.to_show_to_switcher
    if not show_switcher:
        return
    self.layout.separator()
    self.layout.operator("call.add_to_switcher_menu", text="\"调整字距\"⟶Switcher", icon='PRESET').action = 'action.font_call_change_spacing_menu'

def fontedit_delete_menu_to_switcher(self, context):
    show_switcher = bpy.context.preferences.addons[ADDON_NAME].preferences.to_show_to_switcher
    if not show_switcher:
        return
    self.layout.separator()
    self.layout.operator("call.add_to_switcher_menu", text="\"删除文本\"⟶Switcher", icon='PRESET').action = 'action.font_delete'


def register():
    bpy.types.UI_MT_button_context_menu.append(draw_add_to_switcher_font)
    bpy.types.VIEW3D_MT_select_edit_text.append(fontedit_select_text_to_switcher)
    bpy.types.VIEW3D_MT_edit_font_chars.append(fontedit_font_chars_menu_to_switcher)
    bpy.types.VIEW3D_MT_edit_font_kerning.append(fontedit_change_spacing_menu_to_switcher)
    bpy.types.VIEW3D_MT_edit_font_delete.append(fontedit_delete_menu_to_switcher)

def unregister():
    bpy.types.VIEW3D_MT_edit_font_delete.remove(fontedit_delete_menu_to_switcher)
    bpy.types.VIEW3D_MT_edit_font_kerning.remove(fontedit_change_spacing_menu_to_switcher)
    bpy.types.VIEW3D_MT_edit_font_chars.remove(fontedit_font_chars_menu_to_switcher)
    bpy.types.VIEW3D_MT_select_edit_text.remove(fontedit_select_text_to_switcher)
    bpy.types.UI_MT_button_context_menu.remove(draw_add_to_switcher_font)
