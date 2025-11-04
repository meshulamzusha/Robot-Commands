import sys
from classes.movable_mixin import MovableMixin
from classes.speakable_mixin import SpeakableMixin


class DeliveryRobot(MovableMixin, SpeakableMixin):
    def __init__(self, name: str) -> None:
        super().__init__(name)


    def robot_action(self, complete_command: list[str]):
            command = complete_command[0]

            if len(complete_command) > 1:
                parm = complete_command[1]

            match command:
                case 'SAY':
                    try:
                        super().speak(parm)
                    except AttributeError:
                        print(f'unsupported command {command}')
                case 'MOVE':
                    new_position = parm.split()

                    try:
                        x = int(new_position[0])
                        y = int(new_position[1])
                    except (ValueError, IndexError):
                        print('For moving enter your command like this MOVE <x> <Y>')
                    else:
                        try:
                            super().move(x, y)
                        except AttributeError:
                            print(f'unsupported command {command}')
                case 'WHERE':
                    try:
                        super().print_position()
                    except AttributeError:
                        print(f'unsupported command {command}')
                case 'EXIT':
                    sys.exit()
                case _:
                    print(f'command not found')


