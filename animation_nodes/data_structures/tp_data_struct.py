import bpy

class SplineDataStructure:

    def __init__(self, spline, duration, transition, interpolation, transition_interpolation):
        self.spline = spline
        self.duration = duration
        self.transition = transition
        self.interpolation = interpolation
        self.transition_interpolation = transition_interpolation


class CamDataStructure:
    def __init__(self, tracking_object, focus_object, lock_track_focus, manual_focus, focus,
        shift_focus, roll, tracking_interpolation, focus_interpolation, other_camera_settings,
        fake_autofocus, fa_pull_back, fa_duration, fa_delay, fa_interpolation):
        self.tracking_object = tracking_object
        self.focus_object = focus_object
        self.lock_track_focus = lock_track_focus
        self.manual_focus = manual_focus
        self.focus = focus
        self.shift_focus = shift_focus
        self.roll = roll
        self.tracking_interpolation = tracking_interpolation
        self.focus_interpolation = focus_interpolation
        self.other_camera_settings = other_camera_settings
        self.fake_autofocus = fake_autofocus
        self.fa_pull_back = fa_pull_back
        self.fa_duration = fa_duration
        self.fa_delay = fa_delay
        self.fa_interpolation = fa_interpolation


class TargetsDataStructure:
    def __init__(self, target_object, stay, transition):
        self.target_object = target_object
        self.stay = stay
        self.transition = transition

class SmoothnessDataStructure:
    def __init__(self, smoothness):
        self.smoothness = smoothness

class OvershootDataStructure:
    def __init__(self, amplitude, frequency, decay):
        self.amplitude = amplitude
        self.frequency = frequency
        self.decay = decay


class NoiseDataStructure:
    def __init__(self, location_noise, track_noise, roll_noise):
        self.location_noise = location_noise
        self.track_noise = track_noise
        self.roll_noise = roll_noise

class TrackFollowDataStructure:
    def __init__(self, delay, delay_interpolation):
        self.delay = delay
        self.delay_interpolation = delay_interpolation

class CameraSettingsDataStructure:
    def __init__(self, focal_length, fstop, sensor_size, clipping_start, clipping_end):
        self.focal_length = focal_length
        self.fstop = fstop
        self.sensor_size = sensor_size
        self.clipping_start = clipping_start
        self.clipping_end = clipping_end
        
