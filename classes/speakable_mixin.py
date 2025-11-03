from classes.robot import Robot


class SpeakableMixin(Robot):
    def __init__(self, name: str) -> None:
        super().__init__(name)


    def speak(self, msg) -> None:
        print(f'{msg}')