from math import sin, pi, exp
from mathutils import Vector
from .tp_functions import TPFunctions

class TP_Abstract(TPFunctions):


    def overshoot(self, overshoot_obj, time, delay, duration, start, end):
        time = (time - delay)*0.1
        amplitude = ((end - start) / duration)*overshoot_obj.amplitude
        #w = (overshoot_obj.frequency*pi*2) + 0.0001
        w = overshoot_obj.frequency
        out = amplitude*sin(time*w)/exp(time*overshoot_obj.decay)
        return out

    def overshoot_b(self, overshoot_obj, spline_data, time, delay):
        if spline_data.duration == 0: return 0.0
        time = (time - delay)
        out = 0.0
        if time >= delay:
            spline_len = self.find_spline_length(spline_data.spline, 0,1)
            speed = (spline_len / spline_data.duration)
            out = speed * sin(time*overshoot_obj.frequency)/exp(time*overshoot_obj.decay) * (overshoot_obj.amplitude*spline_data.duration)
        return out


    def overshoot_repeat(self, overshoot_obj, time, delay, spline_data_list):
        os = Vector((0,0,0))
        start, end = self.spline_start_end_vectors(spline_data_list)
        for i in range(len(delay)):
            duration = spline_data_list[i-1].transition
            if duration == 0: duration = 0.001
            if i == 0:
                continue
            if time >= delay[i]:
                os = self.overshoot(overshoot_obj, time, delay[i], duration, start[i], end[i-1])
        return os


    def noise(self, location_noise, track_noise, focus_noise):
        pass


    def global_camera_settings(self, camera, global_cam_settings):
        if global_cam_settings:
            self.all_cam_settings(camera, global_cam_settings)





    