import bpy
from ... base_types import AnimationNodeSocket
from ... data_structures.tp_data_struct import OvershootDataStructure

class TP_OvershootSocket(bpy.types.NodeSocket, AnimationNodeSocket):
    bl_idname = "an_TP_OvershootSocket"
    bl_label = "TP Overshoot Socket"
    dataType = "Overshoot"
    allowedInputTypes = ["Overshoot"]
    drawColor = (0.992,0.882,0.415, 1)
    storable = True
    comparable = False

    @classmethod
    def getDefaultValue(cls):
        return None

    @classmethod
    def correctValue(cls, value):
        if isinstance(value, OvershootDataStructure):
            return value, 0
        return cls.getDefaultValue(), 2