import bpy
from ... base_types import AnimationNode
from ... data_structures.tp_data_struct import OvershootDataStructure

class TP_OvershootNode(bpy.types.Node, AnimationNode):
    bl_idname = "an_TP_Overshoot_Node"
    bl_label = "TP Overshoot"
    bl_width_default = 180

    def create(self):
        self.newInput("Float", "Amplitute", "amplitude", value = 1.0)
        self.newInput("Float", "Frequency", "frequency", value = 1.0)
        self.newInput("Float", "Decay", "decay", value = .1, minValue = 0.001, maxValue = 1)

        self.newOutput("Overshoot", "Overshoot", "overshoot")
        

    def execute(self, amplitude, frequency, decay):
        return OvershootDataStructure(amplitude, frequency, decay)
