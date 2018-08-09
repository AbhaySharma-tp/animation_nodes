from math import sin, pi, exp
from mathutils import Vector
from .tp_functions import TPFunctions

class TP_Abstract(TPFunctions):


    def overshoot(self, overshoot_obj, time, delay, duration, start, end):
        time = (time - delay)
        speed = (((end - start).length*.1) / duration)
        frequency = overshoot_obj.frequency
        out = speed * sin((time-duration)*frequency)/exp(time*overshoot_obj.decay)
        return out * overshoot_obj.amplitude

    def overshoot_b(self, overshoot_obj, spline_data, time, delay):
        if spline_data.duration == 0: return 0.0
        time = (time - delay)
        out = 0.0
        if time >= delay:
            spline_len = self.find_spline_length(spline_data.spline, 0,1)
            speed = (spline_len / spline_data.duration)
            duration = spline_data.duration
            out = speed * sin((time-duration)*overshoot_obj.frequency*speed)/exp(time*overshoot_obj.decay) 
        return out * overshoot_obj.amplitude * duration


    def overshoot_repeat(self, overshoot_obj, time, delay, spline_data_list):
        final_os = Vector((0.0,0.0,0.0))
        start, end = self.spline_start_end_vectors(spline_data_list)
        for i in range(len(delay)):
            duration = spline_data_list[i-1].transition
            if duration == 0: duration = 0.001
            if i == 0:
                continue
            if time >= delay[i]:
                os = self.overshoot(overshoot_obj, time, delay[i], duration, start[i], end[i-1])
                direction = end[i-1] - start[i]
                final_os = Vector((direction[0]*os,direction[1]*os,direction[2]*os))
        return final_os


    def noise(self, location_noise, track_noise, focus_noise):
        pass


    def global_camera_settings(self, camera, global_cam_settings):
        if global_cam_settings:
            self.all_cam_settings(camera, global_cam_settings)





    