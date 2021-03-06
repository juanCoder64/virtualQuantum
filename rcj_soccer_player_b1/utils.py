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
