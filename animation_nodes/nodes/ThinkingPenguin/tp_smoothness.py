import bpy
from ... base_types import AnimationNode
from ... data_structures.tp_data_struct import SmoothnessDataStructure

class TP_SmoothnessNode(bpy.types.Node, AnimationNode):
    bl_idname = "an_TP_Smoothness_Node"
    bl_label = "TP Smoothness"
    bl_width_default = 180

    def create(self):
        self.newInput("Float", "Smoothness", "smoothness_amount")
        self.newOutput("Smoothness", "Smoothness", "smoothness")
        

    def execute(self, smoothness_amount):
        return SmoothnessDataStructure(smoothness_amount)
        