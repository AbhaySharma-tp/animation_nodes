import bpy
from ... base_types import AnimationNodeSocket, PythonListSocket
from ... data_structures.tp_data_struct import CamDataStructure

class TP_CamdDataDataSocket(bpy.types.NodeSocket, AnimationNodeSocket):
    bl_idname = "an_TP_CamDataSocket"
    bl_label = "TP Cam Data Socket"
    dataType = "Camera Data"
    allowedInputTypes = ["Camera Data"]
    drawColor = (0.8,1.0,0.796, 1)
    storable = True
    comparable = False

    @classmethod
    def getDefaultValue(cls):
        return None

    @classmethod
    def correctValue(cls, value):
        if isinstance(value, CamDataStructure):
            return value, 0
        return cls.getDefaultValue(), 2


class TP_CamDataListSocket(bpy.types.NodeSocket, PythonListSocket):
    bl_idname = "an_TP_CamDataListSocket"
    bl_label = "TP Cam Data List Socket"
    dataType = "Camera Data List"
    allowedInputTypes = ["Camera Data List"]
    baseDataType = "Camera Data"
    drawColor = (0.8,1.0,0.796, 0.5)
    storable = True
    comparable = False

    @classmethod
    def getDefaultValue(cls):
        return "value[:]"

    @classmethod
    def correctValue(cls, value):
        if isinstance(value, list):
            if all(isinstance(element, CamDataStructure) for element in value):
                return value, 0
        return cls.getDefaultValue(), 2


