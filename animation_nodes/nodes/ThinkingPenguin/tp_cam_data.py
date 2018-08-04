import bpy
from ... base_types import AnimationNode
from ... data_structures.tp_data_struct import CamDataStructure

class TP_CameraDataNode(bpy.types.Node, AnimationNode):
    bl_idname = "an_TP_Camera_Data_Node"
    bl_label = "TP Camera Data"
    bl_width_default = 180

    def create(self):
        self.newInput("Object", "Tracking Object", "tracking_object")
        self.newInput("Object", "Focus Object", "focus_object", hide = True)
        self.newInput("Boolean", "Use track object as focus", "lock_track_focus")
        self.newInput("Boolean", "Manual Focus", "manual_focus", value = False, hide = True)
        self.newInput("Float", "Focus", "focus", minValue = 0, hide = True)
        self.newInput("Float", "Shift Focus", "shift_focus")
        self.newInput("Float", "Z-Roll", "roll")
        self.newInput("Interpolation", "Tracking Interpolation", "tracking_interpolation", hide = True)
        self.newInput("Interpolation", "Focus Interpolation", "focus_interpolation", hide = True)
        self.newInput("Camera Settings", "Camera Settings", "camera_settings", hide = True)
        self.newOutput("Camera Data", "Camera Data", "camera_data")
        



    def execute(self, tracking_object, focus_object, lock_track_focus, manual_focus, focus, shift_focus,
        roll, tracking_interpolation, focus_interpolation, camera_settings):
        return CamDataStructure(tracking_object, focus_object, lock_track_focus, manual_focus, focus, shift_focus,
            roll, tracking_interpolation, focus_interpolation, camera_settings)
        