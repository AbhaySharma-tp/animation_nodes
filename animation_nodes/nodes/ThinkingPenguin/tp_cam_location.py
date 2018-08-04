
class TPCamLocation:
    
    def animate_camera_on_path_pos_list(self, spline_data_list, camera, camera_data_list, delay, time):
        if camera is None:
            return  

        for i in range(len(spline_data_list)):
            parameter, animating = self.animate_r_bool(0,1,spline_data_list[i].duration, spline_data_list[i].interpolation, delay[i], time)
            location = self.execute_pos(spline_data_list[i].spline, parameter)
            if animating is True:
                return location


    def tweening_pos(self, spline_data_list, camera, camera_data_list, delay, time):
        start_list, end_list = self.spline_start_end_vectors(spline_data_list)
        for i in range(len(spline_data_list)):
            if(i==0):
                continue
            
            loc, animating = self.animate_r_bool(end_list[i-1],start_list[i],spline_data_list[i-1].transition, 
                spline_data_list[i-1].transition_interpolation, delay[i-1], time) 
            if animating is True:
                return loc

    
    def spline_start_end_vectors(self, spline_data_list):
        start_list = []
        end_list = []
        for s in spline_data_list:
            start_list.append(self.execute_pos(s.spline, 0))
            end_list.append(self.execute_pos(s.spline, 1))
        return start_list, end_list
