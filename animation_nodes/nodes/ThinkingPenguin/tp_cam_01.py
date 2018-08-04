import bpy
from bpy.props import *
from ... base_types import AnimationNode
from .tp_spline_mode import TPSplineMode
from .tp_functions import TPFunctions
from mathutils import Vector



modeItems = [
    ("SIMPLE", "Simple", "Minimum mode", "", 0),
    ("SPLINE_DATA", "Spline Data", "Use spline data", "", 1)
]

class TPCam01Node(bpy.types.Node, AnimationNode, TPSplineMode):
    bl_idname = "an_TP_Cam_0.1_Node"
    bl_label = "TP Cam 0.1"
    bl_width_default = 200

    mode = EnumProperty(name = "Mode", default = "SPLINE_DATA", items = modeItems,
        update = AnimationNode.refresh)

    def create(self):
        self.newInput("Object", "Camera", "camera")
        self.newInput("Boolean", "Make Scene Camera", "make_scene_camera", value = False)
        self.newInput("Boolean", "Show Limits", "limits", value = False)
        
        if self.mode == "SIMPLE":
            self.newInput("Object", "Referece Camera", "ref_camera")
            self.newInput("Smoothness", "Smoothness", "smoothness")

        elif self.mode == "SPLINE_DATA":
            self.newInput("Spline Data", "Spline Data", "spline_data")
            self.newInput("Spline Data List", "Spline Data List", "spline_data_list")
            self.newInput("Camera Data", "Camera Data", "camera_data")
            self.newInput("Camera Data List", "Camera Data List", "camera_data_list")

        self.newInput("Overshoot", "Overshoot", "overshoot")
        self.newInput("Noise", "Noise", "noise")
        self.newInput("Camera Settings", "Global Camera Settings", "global_cam_settings")
        self.newInput("Float", "Time", "time")

        self.newOutput("Generic", "debug", "debug", hide = True)


    def draw(self, layout):
        layout.prop(self, "mode", text = "Mode")

    def getExecutionFunctionName(self):
        if self.mode == "SIMPLE":
            return "execute_simple"
        elif self.mode == "SPLINE_DATA":
            return "execute_Spline_Data"

    
    def execute_Spline_Data(self, camera, make_scene_camera, limits, spline_data, spline_data_list, camera_data, camera_data_list,
        overshoot, noise, global_cam_settings, time):  

        if camera:
            if make_scene_camera is True:
                bpy.context.scene.camera = camera   
            if limits is True:
                bpy.data.cameras[camera.data.name].show_limits = True 
            else: bpy.data.cameras[camera.data.name].show_limits = False 
     
        #validation
        spline_data_list = self.valid_list(spline_data_list)
        camera_data_list = self.valid_list(camera_data_list)

        if spline_data_list:
            spline_data = None

            for i in range(len(spline_data_list)):
                if camera_data_list:
                    camera_data = None
                    
                    if len(camera_data_list) > len(spline_data_list):
                        camera_data_list.pop()

                    cd_last_index = len(camera_data_list) - 1
                    if i <= cd_last_index:
                        continue
                    else: camera_data_list.append(camera_data_list[cd_last_index])



        if spline_data:
            self.animate_camera_on_path(spline_data, time, camera, camera_data, overshoot, noise)
        
        if camera_data:
            self.track_object(camera, camera_data, noise)
            self.camera_settings(camera, camera_data)
            
        self.global_camera_settings(camera, global_cam_settings)

        self.list_mode_aniamtions(spline_data_list, camera_data_list, global_cam_settings, camera, time, overshoot, noise)

        debug = ""
       
        return debug

        
    def execute_simple(self, camera, make_scene_camera, limits, ref_camera, smoothness, 
        overshoot, noise, global_cam_settings, time):
        if camera:
            if make_scene_camera is True:
                bpy.context.scene.camera = camera   
            if limits is True:
                bpy.data.cameras[camera.data.name].show_limits = True 
            else: bpy.data.cameras[camera.data.name].show_limits = False

        self.global_camera_settings(camera, global_cam_settings)

        debug = ""
        return debug


