class TPFocus():

    def evaluate_focus(self, vec1, vec2):
        focus = (vec2 - vec1).length
        return focus
    
    def focus_list(self, camera, camera_data_list, delay, time):
        if not camera:
            return
        focus_list = []

        for i in range(len(camera_data_list)):

            if camera_data_list[i].fake_autofocus is True:
                camera_data_list[i].shift_focus -= self.fake_autofocus_m(camera_data_list[i], delay[i], time)

            if camera_data_list[i].manual_focus is True:
                focus_list.append(camera_data_list[i].focus + camera_data_list[i].shift_focus)
            elif camera_data_list[i].lock_track_focus is True:
                if camera_data_list[i].tracking_object:
                    focus_list.append(self.evaluate_focus(camera_data_list[i].tracking_object.location, camera.location) + camera_data_list[i].shift_focus)
            elif camera_data_list[i].focus_object:
                focus_list.append(self.evaluate_focus(camera_data_list[i].focus_object.location, camera.location) + camera_data_list[i].shift_focus)
                
            else: focus_list.append(camera_data_list[i].focus)
 
        return focus_list

    def focus_on_path(self, focus_list, delay, time):
        focus = 0.0
        for i in range(len(focus_list)):
            if(delay[i] <= time):
                    focus = focus_list[i]
        return focus

    def tween_focus(self, spline_data_list, camera_data_list, focus_list, delay, time):
        for i in range(len(camera_data_list)):
            if i == 0:
                continue

            animated_focus, animating = self.animate_r_bool(focus_list[i-1], focus_list[i],
                 spline_data_list[i-1].transition, camera_data_list[i-1].focus_interpolation, delay[i-1], time)

            if animating is True:
                return animated_focus

    def fake_autofocus_m(self, camera_data, delay, time):
        if camera_data.fa_duration == 0 : camera_data.fa_duration = 0.0001
        if camera_data.fa_delay == 0 : camera_data.fa_delay == 0.0001
        start = time - (camera_data.fa_delay + delay)

        pull_back = self.animate(0.0, camera_data.fa_pull_back, camera_data.fa_duration/2, 
            camera_data.fa_interpolation, camera_data.fa_delay + delay, time)

        original_focus = self.animate(pull_back, 0.0, camera_data.fa_duration/2, camera_data.fa_interpolation, 
            (delay + camera_data.fa_delay + (camera_data.fa_duration/2)), time)

        if (start >= 0 and start <= (camera_data.fa_duration/2)):
            return pull_back
        else: return original_focus



        

    
        
