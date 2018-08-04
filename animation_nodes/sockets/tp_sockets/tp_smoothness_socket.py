import bpy
from ... base_types import AnimationNodeSocket
from ... data_structures.tp_data_struct import SmoothnessDataStructure

class TP_SmoothnessSocket(bpy.types.NodeSocket, AnimationNodeSocket):
    bl_idname = "an_TP_SmoothnessSocket"
    bl_label = "TP Smoothness Socket"
    dataType = "Smoothness"
    allowedInputTypes = ["Smoothness"]
    drawColor = (0.721,0.701,0.913, 1)
    storable = True
    comparable = False

    @classmethod
    def getDefaultValue(cls):
        return None

    @classmethod
    def correctValue(cls, value):
        if isinstance(value, SmoothnessDataStructure):
            return value, 0
        return cls.getDefaultValue(), 2