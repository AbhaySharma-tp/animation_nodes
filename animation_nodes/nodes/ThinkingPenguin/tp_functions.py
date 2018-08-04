import bpy
from mathutils import Vector
from .. spline.evaluate_spline import EvaluateSplineNode
from .. spline.spline_evaluation_base import SplineEvaluationBase

class TPFunctions(SplineEvaluationBase):
    
    def animate(self,startvalue, endvalue, duration, interpolation, delay, time):
        if(duration == 0): duration = 0.00001 #to avoid devide by zero error
        time = time - delay
        diff = endvalue - startvalue 
        result = 0.0
        animating = False
        if(time >= 0 and time <= duration):
            animating = True
            influence = (time / duration)
            influence = interpolation(influence)
            result = startvalue + (diff * influence)
  
        #return result, animating
        return result

    def animate_r_bool(self,startvalue, endvalue, duration, interpolation, delay, time):
        if(duration == 0): duration = 0.00001 #to avoid devide by zero error
        time = time - delay
        diff = endvalue - startvalue 
        result = 0.0
        animating = False
        if(time >= 0 and time <= duration):
            animating = True
            influence = (time / duration)
            influence = interpolation(influence)
            result = startvalue + (diff * influence)
  
        return result, animating


    def execute_pos(self, spline, parameter):
        parameter = min(max(parameter, 0), 1)
        if spline.isEvaluable():
            if self.parameterType == "UNIFORM":
                spline.ensureUniformConverter(self.resolution)
                parameter = spline.toUniformParameter(parameter)
            return spline.evaluate(parameter)
        else:
            return Vector((0, 0, 0))

    def execute_rot(self, spline, parameter):
        parameter = min(max(parameter, 0), 1)
        if spline.isEvaluable():
            if self.parameterType == "UNIFORM":
                spline.ensureUniformConverter(self.resolution)
                parameter = spline.toUniformParameter(parameter)
            return spline.evaluateTangent(parameter)
        else:
            return Vector((0, 0, 0))

    def switcher(self, first_value, second_value, end_value):
        if first_value:
            value = first_value
        else:
            value = second_value
        if value:
            f_value = value
        else:
            f_value = end_value
        return f_value

    def switcher_b(self, first_value, second_value):
        if first_value:
            value = first_value
        else:
            value = second_value

        return value

    def valid_list(self,anylist):
        out_list = [i for i in anylist if i]
        if len(out_list) == 0:
            return
        else: return out_list






