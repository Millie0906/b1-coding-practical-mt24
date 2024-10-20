# defining a PD feedback controller
class Controller:
    def __init__(self, Kp, Kd):
        """
        Initialize the PD controller with given proportional and derivative gains.
        Set the previous error to 0
        """
        self.Kp = Kp
        self.Kd = Kd
        self.prev_error = 0

    def compute(self, error):
        """
        Compute the control action based on the current error.
        error: The current error (reference - output)
        return: Control action
        """
        derivative = error - self.prev_error
        control_action = self.Kp * error + self.Kd * derivative
        self.prev_error = error
        return control_action
    
    def reset(self):
        # Reset the previous error to zero
        self.prev_error = 0



