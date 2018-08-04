import bpy
from ... base_types import AnimationNodeSocket
from ... data_structures.tp_data_struct import CameraSettingsDataStructure

class TP_CameraSettingsSocket(bpy.types.NodeSocket, AnimationNodeSocket):
    bl_idname = "an_TP_Camera_Settins_Socket"
    bl_label = "TP Camera Settings Socket"
    dataType = "Camera Settings"
    allowedInputTypes = ["Camera Settings"]
    drawColor = (0.839,0.235,0.301, 1)
    storable = True
    comparable = False

    @classmethod
    def getDefaultValue(cls):
        return None

    @classmethod
    def correctValue(cls, value):
        if isinstance(value, CameraSettingsDataStructure):
            return value, 0
        return cls.getDefaultValue(), 2