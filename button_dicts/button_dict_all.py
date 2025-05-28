from ..button_dicts.button_dict_global import button_press_global
from ..button_dicts.button_dict_object import button_press_object
from ..button_dicts.button_dict_mesh_edit import button_press_mesh_edit
from ..button_dicts.button_dict_armature_edit import button_press_armature_edit

button_press_function = (
    button_press_global 
    | button_press_object
    | button_press_mesh_edit
    | button_press_armature_edit
)