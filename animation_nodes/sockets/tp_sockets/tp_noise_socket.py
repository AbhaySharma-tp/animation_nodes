import bpy
from ... base_types import AnimationNodeSocket
from ... data_structures.tp_data_struct import NoiseDataStructure

class TP_NoiseSocket(bpy.types.NodeSocket, AnimationNodeSocket):
    bl_idname = "an_TP_NoiseSocket"
    bl_label = "TP Noise Socket"
    dataType = "Noise"
    allowedInputTypes = ["Noise"]
    drawColor = (0.270,0.431,0.749, 1)
    storable = True
    comparable = False

    @classmethod
    def getDefaultValue(cls):
        return None

    @classmethod
    def correctValue(cls, value):
        if isinstance(value, NoiseDataStructure):
            return value, 0
        return cls.getDefaultValue(), 2