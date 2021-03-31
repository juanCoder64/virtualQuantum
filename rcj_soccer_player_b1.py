# rcj_soccer_player controller - ROBOT B1
# solo intenta ir al centro
import math

from rcj_soccer_robot import RCJSoccerRobot, TIME_STEP
import utils
import math
center = {
    "x": 0,
    "y": 0,
}


class MyRobot(RCJSoccerRobot):
    def run(self):
        ready = 0
        while self.robot.step(TIME_STEP) != -1:
            if self.is_new_data():
                data = self.get_new_data()
                robot_pos = data[self.name]
                # Get the position of the ball
                ball_pos = data['ball']
                left_speed, right_speed, ready = utils.moveTo(
                    self, 0.1, 0, robot_pos)
                if ready:
                    left_speed, right_speed = utils.face(self, 0, 0, robot_pos)
                    left_speed *= 5
                    right_speed *= 5

                self.left_motor.setVelocity(left_speed)
                self.right_motor.setVelocity(right_speed)


my_robot = MyRobot()
my_robot.run()
