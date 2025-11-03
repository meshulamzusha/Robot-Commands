import sys
from classes.speakable_mixin import SpeakableMixin


class GuardRobot(SpeakableMixin):
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
                    super().speak(parm)
                case 'MOVE':
                    if callable(self.move)
                case 'WHERE':
                    print(f'')
                case 'EXIT':
                    self.is_on = False
                    sys.exit()
                case _:
                    print(f'command not found')