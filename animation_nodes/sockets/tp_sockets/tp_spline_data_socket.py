import bpy
from ... base_types import AnimationNodeSocket, PythonListSocket
from ... data_structures.tp_data_struct import SplineDataStructure

class TP_SplineDataSocket(bpy.types.NodeSocket, AnimationNodeSocket):
    bl_idname = "an_TP_SplineDataSocket"
    bl_label = "TP Spline Data Socket"
    dataType = "Spline Data"
    allowedInputTypes = ["Spline Data"]
    drawColor = (0.313,0.847,0.843, 1)
    storable = True
    comparable = False

    @classmethod
    def getDefaultValue(cls):
        return None

    @classmethod
    def correctValue(cls, value):
        if isinstance(value, SplineDataStructure):
            return value, 0
        return cls.getDefaultValue(), 2


class TP_SplineDataListSocket(bpy.types.NodeSocket, PythonListSocket):
    bl_idname = "an_TP_SplineDataListSocket"
    bl_label = "TP Spline Data List Socket"
    dataType = "Spline Data List"
    allowedInputTypes = ["Spline Data List"]
    baseDataType = "Spline Data"
    baseType = TP_SplineDataSocket
    drawColor = (0.313,0.847,0.843, 0.5)
    storable = True
    comparable = False

    @classmethod
    def getDefaultValue(cls):
        return "value[:]"

    @classmethod
    def correctValue(cls, value):
        if isinstance(value, list):
            if all(isinstance(element, SplineDataStructure) for element in value):
                return value, 0
        return cls.getDefaultValue(), 2


