from classes.delivery_robot import DeliveryRobot
from classes.guard_robot import GuardRobot


if __name__ == '__main__':

    commands = [
        'SAY ready',
        'MOVE 3 2',
        'WHERE',
        'SAY done',
        'EXIT'
    ]

    delivery_robot = DeliveryRobot('bob')
    guard_robot = GuardRobot('jin')

    for command in commands:
        delivery_robot._get_command(command)
        guard_robot._get_command(command)

