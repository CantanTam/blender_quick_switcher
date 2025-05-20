import bpy

class CALLOUT_QUICK_MENU_OT_one(bpy.types.Operator):
    bl_idname = "call.popup_menu_one"
    bl_label = "调用极速菜单1"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        typeandmode =  bpy.context.active_object.type+bpy.context.active_object.mode
        if bpy.context.mode == "OBJECT":    #mode1
            bpy.ops.wm.call_menu(name="popup.quick_menu_one_object")
        # MESH
        elif typeandmode == "MESHEDIT":     #mode2
            bpy.ops.wm.call_menu(name="popup.quick_menu_one_meshedit")
        elif typeandmode == "MESHSCULPT":   #mode3
            bpy.ops.wm.call_menu(name="popup.quick_menu_one_meshsculpt")
        elif typeandmode == "MESHVERTEX_PAINT": #mode4
            bpy.ops.wm.call_menu(name="popup.quick_menu_one_meshvertexpaint")
        elif typeandmode == "MESHWEIGHT_PAINT": #mode5
            bpy.ops.wm.call_menu(name="popup.quick_menu_one_meshweightpaint")
        elif typeandmode == "MESHTEXTURE_PAINT": #mode6
            bpy.ops.wm.call_menu(name="popup.quick_menu_one_meshtexture")
        # 4.2 或以下版本 GPENCIL
        elif typeandmode == "GPENCILEDIT_GPENCIL":  #mode7
            bpy.ops.wm.call_menu(name="popup.quick_menu_one_gpenciledit")
        elif typeandmode == "GPENCILSCULPT_GPENCIL":  #mode8
            bpy.ops.wm.call_menu(name="popup.quick_menu_one_gpencilsculpt")
        elif typeandmode == "GPENCILPAINT_GPENCIL":  #mode9
            bpy.ops.wm.call_menu(name="popup.quick_menu_one_gpencilpaint")
        elif typeandmode == "GPENCILWEIGHT_GPENCIL":  #mode10
            bpy.ops.wm.call_menu(name="popup.quick_menu_one_gpencilweight")
        elif typeandmode == "GPENCILVERTEX_GPENCIL":  #mode11
            bpy.ops.wm.call_menu(name="popup.quick_menu_one_gpencilvertex")
        # 4.3  或以上版本 GREASEPENCIL
        elif typeandmode == "GREASEPENCILEDIT":  #mode12
            bpy.ops.wm.call_menu(name="popup.quick_menu_one_greasepenciledit")
        elif typeandmode == "GREASEPENCILSCULPT_GREASE_PENCIL":  #mode13
            bpy.ops.wm.call_menu(name="popup.quick_menu_one_greasepencilsculpt")
        elif typeandmode == "GREASEPENCILPAINT_GREASE_PENCIL":  #mode14
            bpy.ops.wm.call_menu(name="popup.quick_menu_one_greasepencilpaint")
        elif typeandmode == "GREASEPENCILWEIGHT_GREASE_PENCIL":  #mode15
            bpy.ops.wm.call_menu(name="popup.quick_menu_one_greasepencilweight")
        elif typeandmode == "GREASEPENCILVERTEX_GREASE_PENCIL":  #mode16
            bpy.ops.wm.call_menu(name="popup.quick_menu_one_greasepencilvertex")
        # ARMATURE
        elif typeandmode == "ARMATUREEDIT":  #mode17
            bpy.ops.wm.call_menu(name="popup.quick_menu_one_armatureedit")
        elif typeandmode == "ARMATUREPOSE":  #mode18
            bpy.ops.wm.call_menu(name="popup.quick_menu_one_armaturepose")
        # CURVE/SURFACE/META/FONT/LATTICE
        elif typeandmode == "CURVEEDIT":  #mode19
            bpy.ops.wm.call_menu(name="popup.quick_menu_one_curveedit")
        elif typeandmode == "SURFACEEDIT":  #mode20
            bpy.ops.wm.call_menu(name="popup.quick_menu_one_surfaceedit")
        elif typeandmode == "METAEDIT":  #mode21
            bpy.ops.wm.call_menu(name="popup.quick_menu_one_metaedit")
        elif typeandmode == "FONTEDIT":  #mode22
            bpy.ops.wm.call_menu(name="popup.quick_menu_one_fontedit")
        elif typeandmode == "LATTICEEDIT":  #mode23
            bpy.ops.wm.call_menu(name="popup.quick_menu_one_latticeedit")

        return {'FINISHED'}
    
# 因为 operators.py 当中 限过了快捷键功能的运行方式是 exec(f'bpy.ops.{op}()') 
# ，无法在函数内部添加参数，而 bpy.ops.popup.quick_menu_one_object() 是无法调出自定义菜单的
# ，所以需要再构建一个函数，调用 bpy.ops.popup.quick_menu_one_object('INVOKE_DEFAULT')

class CALLOUT_QUICK_MENU_OT_two(bpy.types.Operator):
    bl_idname = "call.popup_menu_two"
    bl_label = "调用极速菜单2"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.ops.wm.call_menu(name="popup.quick_menu_one_meshedit")
        return {'FINISHED'}
    