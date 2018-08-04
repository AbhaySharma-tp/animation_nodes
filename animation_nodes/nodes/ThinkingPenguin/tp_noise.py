import bpy
from ... base_types import AnimationNode
from ... data_structures.tp_data_struct import NoiseDataStructure

class TP_NoiseNode(bpy.types.Node, AnimationNode):
    bl_idname = "an_TP_Noise_Node"
    bl_label = "TP Noise"
    bl_width_default = 180

    def create(self):
        self.newInput("Vector", "Location Noise", "loc_noise")
        self.newInput("Vector", "Track Noise", "track_noise")
        self.newInput("Float", "Roll Noise", "roll_noise")
        self.newOutput("Noise", "Noise", "noise")
        

    def execute(self, loc_noise, track_noise, roll_noise):
        return NoiseDataStructure(loc_noise, track_noise, roll_noise)