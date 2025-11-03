import sys
from classes.movable_mixin import MovableMixin
from classes.speakable_mixin import SpeakableMixin


class DeliveryRobot(MovableMixin, SpeakableMixin):
    def __init__(self, name: str) -> None:
        super().__init__(name)
        self.is_on = True


    def action(self):
        while self.is_on:
            complete_command = super()._get_command(self)
            command = complete_command[0]
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
                    self.is_on = False
                    sys.exit()
                case _:
                    print(f'command not found')


