from mathutils import Vector, Euler

class TPTrack():
    def track_object_locations(self, spline_data_list, camera_data_list, delay, time):
        location = Vector((0,0,0))

        if camera_data_list:
            for i in range(len(camera_data_list)):
                if camera_data_list[i].tracking_object is None:
                    camera_data_list[i].tracking_object = camera_data_list[i-1].tracking_object
                    if camera_data_list[i].tracking_object is None:
                        return

                if(delay[i] <= time):
                    location = camera_data_list[i].tracking_object.location
            
        return location


    def tween_track_locations(self, spline_data_list, camera, camera_data_list, delay, time):
        
        for i in range(len(spline_data_list)):
            if camera_data_list[i].tracking_object is None:
                camera_data_list[i].tracking_object = camera_data_list[i-1].tracking_object
                if camera_data_list[i].tracking_object is None:
                    return

            test = Vector((5,5,5))
            if(i==0):
                continue
            
            track_location, animating = self.animate_r_bool(camera_data_list[i-1].tracking_object.location, camera_data_list[i].tracking_object.location,
                 spline_data_list[i-1].transition, camera_data_list[i-1].tracking_interpolation, delay[i-1], time)

            if animating is True:
                return track_location


    def roll_list(self, camera_data_list):
        r_list = []
        for i in camera_data_list:
            r_list.append(i.roll)
        return r_list
    
    def roll_on_path(self, camera_data_list, delay, time):
        roll = 0.0
        r_list = self.roll_list(camera_data_list)
        for i in range(len(r_list)):
            if (delay[i] <= time):
                roll = r_list[i]
        return roll

    def roll_tween(self,spline_data_list, camera_data_list, delay, time):
        r_list = self.roll_list(camera_data_list)
        for i in range(len(camera_data_list)):
            if i==0:
                continue
            animated_roll, animating = self.animate_r_bool(r_list[i-1], r_list[i],
                 spline_data_list[i-1].transition, camera_data_list[i-1].focus_interpolation, delay[i-1], time)

            if animating is True:
                return animated_roll

