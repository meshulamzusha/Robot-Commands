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
                    x = int(new_position[0])
                    y = int(new_position[1])
                    super().move(x, y)
                case 'WHERE':
                    super().print_position()
                case 'EXIT':
                    self.is_on = False
                    sys.exit()
                case _:
                    print(f'command not found')


