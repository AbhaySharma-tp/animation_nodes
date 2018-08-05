import bpy
from mathutils import Vector, Euler
import math
from .tp_modes_abstract import TP_Abstract
from .tp_functions import TPFunctions
from .tp_focus import TPFocus
from .tp_track import TPTrack
from .tp_cam_location import TPCamLocation
from .tp_camera import TPCamera

class TPSplineMode(TP_Abstract, TPCamera, TPCamLocation, TPTrack, TPFocus, TPFunctions):

    def animate_camera_on_path(self, spline_data, time, camera, camera_data, overshoot, noise):
        if camera is None or spline_data is None:
            return

        parameter = self.animate(0,1,spline_data.duration, spline_data.interpolation, 0, time)
        camera.location = self.execute_pos(spline_data.spline, parameter)
        if time >= spline_data.duration:
            camera.location = self.execute_pos(spline_data.spline, 1)
            if overshoot:
                if spline_data.duration == 0:
                    spline_data.duration = 0.001
                start_vector = self.execute_pos(spline_data.spline, 0)
                end_vector = self.execute_pos(spline_data.spline, 1)
                os = self.overshoot(overshoot, time, 0, spline_data.duration, start_vector, end_vector) 
                camera.location += os

        if noise:
            camera.location += noise.location_noise
        

    def track_object(self, camera, camera_data, noise):
        if camera_data.tracking_object and camera:
            n = Vector((0.0,0.0,0.0))
            roll_noise = 0.0
            location = camera_data.tracking_object.location
            if noise:
                n = noise.track_noise
                roll_noise = noise.roll_noise

            rotation = Euler((0,0,0))
            vec_difference = (location+n) - camera.location
            rotation = vec_difference.to_track_quat('-Z', 'Y').to_euler()
            camera.rotation_euler = rotation
            camera.rotation_euler.rotate_axis('Z', math.radians(camera_data.roll+roll_noise))
                

    def camera_settings(self, camera, camera_data, time):
        if camera:
            focus = 0.0
            if camera_data.fake_autofocus is True:
                camera_data.shift_focus -= self.fake_autofocus_m(camera_data, 0, time)

            if camera_data.manual_focus is True:
                    focus = camera_data.focus + camera_data.shift_focus
            elif camera_data.lock_track_focus is True:
                if camera_data.tracking_object:
                    focus = self.evaluate_focus(camera_data.tracking_object.location, camera.location) + camera_data.shift_focus
            elif camera_data.focus_object:
                focus = self.evaluate_focus(camera_data.focus_object.location, camera.location) + camera_data.shift_focus
                    
            else: focus = camera_data.focus + camera_data.shift_focus

            self.camera_focus(camera, focus)


    def list_mode_aniamtions(self, spline_data_list, camera_data_list, global_camera_settings, camera, time, overshoot, noise):
        if spline_data_list is None or camera_data_list is None:
            return
        delay = self.delay_list(spline_data_list)
        tween_delay = self.tween_delay_list(spline_data_list)

        #camera location
        path_location = self.animate_camera_on_path_pos_list(spline_data_list, camera, camera_data_list, delay, time)
        tween_location = self.tweening_pos(spline_data_list, camera, camera_data_list, tween_delay, time)
        end_spline = spline_data_list[len(spline_data_list) - 1]
        end_value = self.execute_pos(end_spline.spline, 1)
        location = self.switcher(path_location, tween_location, end_value)
        camera.location = location

        if overshoot:
            os = self.overshoot_repeat(overshoot, time, delay, spline_data_list)
            camera.location += os
        
        if noise:
            camera.location += noise.location_noise
            
        #camera rotation
        track_location_on_path = self.track_object_locations(spline_data_list, camera_data_list, delay, time)
        tween_track_location = self.tween_track_locations(spline_data_list, camera, camera_data_list, tween_delay, time)
        end_track_location = Vector((0,0,0))
        try:
            end_track_location = camera_data_list[-1].tracking_object.location
        except: passs
        else: end_track_location

        final_track_location = self.switcher(tween_track_location, track_location_on_path, end_track_location)
        vec_diff = final_track_location - camera.location
        if noise:
            n = Vector((1.0,1.0,0.0))
            final_noise = Vector((noise.track_noise[0]*n[0],noise.track_noise[1]*n[1],noise.track_noise[2]*n[2]))
            vec_diff += final_noise
        
        camera.rotation_euler = vec_diff.to_track_quat('-Z', 'Y').to_euler() 

        roll_path = self.roll_on_path(camera_data_list, delay, time)
        tween_roll = self.roll_tween(spline_data_list, camera_data_list,tween_delay, time)
        final_roll = self.switcher(tween_roll, roll_path, 0.0)
        camera.rotation_euler.rotate_axis('Z', math.radians(final_roll))

        #camera focus
        focus_list = self.focus_list(camera, camera_data_list, delay, time)
        focus_on_path = self.focus_on_path(focus_list, delay, time)        
        tween_focus = self.tween_focus(spline_data_list, camera_data_list, focus_list, tween_delay, time)
        end_focus = focus_list[-1]
        final_focus = self.switcher(tween_focus, focus_on_path, end_focus)
        self.camera_focus(camera, final_focus)
        
        #other camera settings
        cam_list_settings = self.animated_camera_settings(camera, spline_data_list, camera_data_list, global_camera_settings, delay, tween_delay, time)
        self.all_cam_settings(camera, cam_list_settings)    

        return cam_list_settings


    def delay_list(self, spline_data_list):
        delay = []
        temp = 0.0
        for i in range(len(spline_data_list)):
            if i==0:
                delay.append(temp)
            else:
                temp = temp + spline_data_list[i-1].duration + spline_data_list[i-1].transition
                delay.append(temp)

        return delay

    def tween_delay_list(self, spline_data_list):
        delay = []
        temp = 0.0
        for i in range(len(spline_data_list)):
            if i==0:
                temp = spline_data_list[i].duration
                delay.append(temp)
            else:
                temp = temp + spline_data_list[i].duration + spline_data_list[i-1].transition
                delay.append(temp)

        return delay

