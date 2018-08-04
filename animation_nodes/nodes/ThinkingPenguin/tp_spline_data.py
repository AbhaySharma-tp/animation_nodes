import bpy
from bpy.props import *
from ... base_types import AnimationNode
from ... data_structures.tp_data_struct import SplineDataStructure

class TP_SplineDataNode(bpy.types.Node, AnimationNode):
    bl_idname = "an_TP_Spline_Data_Node"
    bl_label = "TP SPline Data"
    bl_width_default = 160


    def create(self):
        self.newInput("Spline", "Spline", "spline")
        self.newInput("Float", "Duration", "duration")
        self.newInput("Float", "Transition Duration", "transition")
        self.newInput("Interpolation", "Interpolation", "interpolation", hide = True)
        self.newInput("Interpolation", "Transition Interpolation", "trans_interpolation", hide = True)
        
        self.newOutput("Spline Data", "Spline Data", "spline_data")

        

    def execute(self, spline, duration, transition, interpolation, trans_interpolation):
        return SplineDataStructure(spline, duration, transition, interpolation, trans_interpolation)

        