# rcj_soccer_player controller - ROBOT B3

###### REQUIRED in order to import files from B1 controller
import sys
from pathlib import Path
sys.path.append(str(Path('.').absolute().parent))
# You can now import scripts that you put into the folder with your
# robot B1 controller
from rcj_soccer_player_b1 import rcj_soccer_robot, utils
######

# Feel free to import built-in libraries
import math


class MyRobot(rcj_soccer_robot.RCJSoccerRobot):
    def run(self):
        while self.robot.step(rcj_soccer_robot.TIME_STEP) != -1:
            if self.is_new_data():
                data = self.get_new_data()
                left_speed = 0
                right_speed = 0
                # Get the position of our robot
                robot_pos = data[self.name]
                # Get the position of the ball
                ball_pos = data['ball']
                # Get angle between the robot and the ball
                # and between the robot and the north
                ball_angle, robot_angle = self.get_angles(ball_pos, robot_pos)
                ball_to = utils.get_direction(ball_angle)
                # print(robot_angle)
                # print(ball_pos['y'])
                if robot_angle < 5 and robot_angle > 4:
                    # print('lol')
                    if ball_to == 0:
                        left_speed = -10
                        right_speed = -10
                    else:
                        if ball_pos['x'] > robot_pos['x']+.05:
                            fwd = 1
                        else:
                            fwd = -1
                        if ball_pos['y'] > robot_pos['y']:
                            left_speed = 7*fwd
                            right_speed = 10*fwd
                        else:
                            left_speed = 10*fwd
                            right_speed = 7*fwd
                else:
                    if robot_angle > 4.5:
                        direction = -1
                    else:
                        direction = 1
                    # print(direction)
                    left_speed = 4*direction
                    right_speed = -4*direction

                # Set the speed to motors
                self.left_motor.setVelocity(left_speed)
                self.right_motor.setVelocity(right_speed)


my_robot = MyRobot()
my_robot.run()
