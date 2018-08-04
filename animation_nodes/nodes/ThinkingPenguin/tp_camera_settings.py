import bpy
from ... base_types import AnimationNode
from ... data_structures.tp_data_struct import CameraSettingsDataStructure

class TP_CameraSettingsNode(bpy.types.Node, AnimationNode):
    bl_idname = "an_TP_Camera_Settings_Node"
    bl_label = "TP Camera Setttings"
    bl_width_default = 180

    def create(self):
        self.newInput("Float", "Focal Length", "focal_length", minValue = 0, value = 35.0)
        self.newInput("Float", "Fstop", "fstop",minValue = 0)
        self.newInput("Float", "Sensor Size", "sensor_size", minValue = 0, value = 32.0)
        self.newInput("Float", "Clipping Start", "clipping_start", minValue = 0.1, value = 0.100, hide = True)
        self.newInput("Float", "Clipping End", "clipping_end", minValue = 0.1, value = 100.00, hide = True)

        self.newOutput("Camera Settings", "Camera Settings", "camera_settings")
        

    def execute(self, focal_length, fstop, sensor_size, clipping_start, clipping_end):
        return CameraSettingsDataStructure(focal_length, fstop, sensor_size, clipping_start, clipping_end)