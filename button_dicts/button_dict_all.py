from ..button_dicts.button_dict_global import button_press_global
from ..button_dicts.button_dict_object import button_press_object
from ..button_dicts.button_dict_mesh_edit import button_press_mesh_edit
from ..button_dicts.button_dict_mesh_sculpt import button_press_mesh_sculpt
from ..button_dicts.button_dict_mesh_vertex import button_press_mesh_vertex
from ..button_dicts.button_dict_mesh_weight import button_press_mesh_weight
from ..button_dicts.button_dict_gpencil_edit import button_press_gpencil_edit
from ..button_dicts.button_dict_gpencil_weight import button_press_gpencil_weight
from ..button_dicts.button_dict_gpencil_vertex import button_press_gpencil_vertex

from ..button_dicts.button_dict_greasepencil_edit import button_press_greasepencil_edit
from ..button_dicts.button_dict_greasepencil_weight import button_press_greasepencil_weight
from ..button_dicts.button_dict_greasepencil_vertex import button_press_greasepencil_vertex
from ..button_dicts.button_dict_armature_edit import button_press_armature_edit
from ..button_dicts.button_dict_armature_pose import button_press_armature_pose
from ..button_dicts.button_dict_curve_edit import button_press_curve_edit
from ..button_dicts.button_dict_lattice_edit import button_press_lattice_edit
from ..button_dicts.button_dict_font_edit import button_press_font_edit

button_press_function = (
    button_press_global 
    | button_press_object
    | button_press_mesh_edit
    | button_press_mesh_sculpt
    | button_press_mesh_vertex
    | button_press_mesh_weight
    | button_press_gpencil_edit
    | button_press_gpencil_weight
    | button_press_gpencil_vertex
    | button_press_greasepencil_edit
    | button_press_greasepencil_weight
    | button_press_greasepencil_vertex
    | button_press_armature_edit
    | button_press_armature_pose
    | button_press_curve_edit
    | button_press_lattice_edit
    | button_press_font_edit
)