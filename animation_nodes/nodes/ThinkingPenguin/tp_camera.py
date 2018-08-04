import bpy
from .tp_functions import TPFunctions
from ...data_structures.tp_data_struct import CameraSettingsDataStructure

class TPCamera(TPFunctions):
    
    def camera_focus(self, camera, focus):
        bpy.data.cameras[camera.data.name].dof_distance = focus

    def all_cam_settings(self, camera, global_camera_settings):
        bpy.data.cameras[camera.data.name].cycles.aperture_type = "FSTOP"
        bpy.data.cameras[camera.data.name].lens = global_camera_settings.focal_length 
        bpy.data.cameras[camera.data.name].cycles.aperture_fstop = global_camera_settings.fstop
        bpy.data.cameras[camera.data.name].sensor_width = global_camera_settings.sensor_size
        bpy.data.cameras[camera.data.name].clip_start = global_camera_settings.clipping_start
        bpy.data.cameras[camera.data.name].clip_end = global_camera_settings.clipping_end


    def camera_setting_list(self, global_camera_settings, camera_data_list):
        default_camera_settings = CameraSettingsDataStructure(35.0, 0.0, 32.0, 0.1, 100.0)
        if not global_camera_settings:
            global_camera_settings = default_camera_settings


        test_list = []
        for i in camera_data_list:
            if i.other_camera_settings:
                test_list.append(i.other_camera_settings)

        if len(test_list) == 0:
            return
        else:
            del test_list


        cs_list = []
        for i in range(len(camera_data_list)):
            if camera_data_list[i].other_camera_settings:
                cs_list.append(camera_data_list[i].other_camera_settings)
            else: cs_list.append(global_camera_settings)
        return cs_list

    def animated_camera_settings(self, camera, spline_data_list, camera_data_list, global_camera_settings, delay, tween_delay, time):
        cs_list = self.camera_setting_list(global_camera_settings, camera_data_list)
        default_camera_settings = CameraSettingsDataStructure(35.0, 0.0, 32.0, 0.1, 100.0)
        if not cs_list:
            if global_camera_settings:
                return global_camera_settings
            else:return default_camera_settings

        static_switching = self.camera_setting_static_switching(cs_list, camera_data_list, delay, time)
        animated_switching = self.camera_settings_tweening(cs_list, spline_data_list, camera_data_list, tween_delay, time)
        end_value = cs_list[-1]
       
        final_camera_settings = self.switcher(animated_switching, static_switching, end_value)

        return final_camera_settings

    def camera_setting_static_switching(self,cs_list, camera_data_list, delay, time):
        static_switching = cs_list[0]
        for i in range(len(camera_data_list)):
            if(delay[i] <= time):
                static_switching = cs_list[i]
        return static_switching

    def camera_settings_tweening(self, cs_list, spline_data_list, camera_data_list, delay, time):
        animated_settings = CameraSettingsDataStructure(35.0, 0.0, 32.0, 0.1, 100.0)

        for i in range(len(cs_list)):
            if i == 0:
                continue
            animated_lens, animating = self.animate_r_bool(cs_list[i-1].focal_length,cs_list[i].focal_length,
                spline_data_list[i-1].transition, camera_data_list[i-1].focus_interpolation, delay[i-1], time )

            animated_fstop, animating = self.animate_r_bool(cs_list[i-1].fstop, cs_list[i].fstop,
                spline_data_list[i-1].transition, camera_data_list[i-1].focus_interpolation, delay[i-1], time )

            animated_sensor_size, animating = self.animate_r_bool(cs_list[i-1].sensor_size, cs_list[i].sensor_size,
                spline_data_list[i-1].transition, camera_data_list[i-1].focus_interpolation, delay[i-1], time )

            animated_clipping_start, animating = self.animate_r_bool(cs_list[i-1].clipping_start, cs_list[i].clipping_start,
                spline_data_list[i-1].transition, camera_data_list[i-1].focus_interpolation, delay[i-1], time )
            
            animated_clipping_end, animating = self.animate_r_bool(cs_list[i-1].clipping_end, cs_list[i].clipping_end,
                spline_data_list[i-1].transition, camera_data_list[i-1].focus_interpolation, delay[i-1], time )

            animated_settings.focal_length = animated_lens
            animated_settings.fstop = animated_fstop
            animated_settings.sensor_size = animated_sensor_size
            animated_settings.clipping_start = animated_clipping_start
            animated_settings.clpping_end = animated_clipping_end

            if animating is True:
                return animated_settings
           
            

            



        

    

    
