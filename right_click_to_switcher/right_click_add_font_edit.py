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
        layout.operator("call.add_to_switcher_menu", text="\"选择文字\"⟶Switcher", icon='WORDWRAP_ON').action = 'action.font_select_multi'

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





def register():
    bpy.types.UI_MT_button_context_menu.append(draw_add_to_switcher_font)

def unregister():
    bpy.types.UI_MT_button_context_menu.remove(draw_add_to_switcher_font)
