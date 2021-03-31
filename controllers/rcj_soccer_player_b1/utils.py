def get_direction(ball_angle: float) -> int:
    """Get direction to navigate robot to face the ball

    Args:
        ball_angle (float): Angle between the ball and the robot

    Returns:
        int: 0 = forward, -1 = right, 1 = left
    """
    if ball_angle >= 345 or ball_angle <= 15:
        return 0
    return -1 if ball_angle < 180 else 1


def get_direction_front(ball_pos: dict, robot_pos: dict):
    """Get direction to navigate robot to face the ball

    Args:
        ball_angle (float): Angle between the ball and the robot

    Returns:
        int: 0 = forward, -1 = right, 1 = left
    """
    return -1 if ball_pos['y'] < robot_pos['y'] else 1


def face(ball_angle: float):
    if ball_angle > 180:
        ball_angle -= 180
        return ((11 * ball_angle) / 180) * 1
    return ((11 * ball_angle) / 180) * -1


def moveTo(self, x, y, robot_pos: dict):
    To = {
        'x': x,
        'y': y
    }
    angle, _ = self.get_angles(To, robot_pos)
    dir = get_direction(angle)
    dir *= 5
    if x+.01 > robot_pos['x'] and x-.01 < robot_pos['x'] and y+.01 > robot_pos['y'] and y-.01 < robot_pos['y']:
        return 0, 0, 1
    else:
        if dir != 0:
            return dir, -dir, 0
        else:
            return - 10, -10, 0


def face(self, x, y, robot_pos: dict):
    To = {
        'x': x,
        'y': y
    }
    angle, _ = self.get_angles(To, robot_pos)
    dir = get_direction(angle)
    return dir, -dir
