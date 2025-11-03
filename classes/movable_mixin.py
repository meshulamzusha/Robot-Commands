from classes.robot import Robot


class MovableMixin(Robot):
    def __init__(self, name: str, x: int = 0, y: int = 0) -> None:
        super().__init__(name)
        self.x = x
        self.y = y


    def move(self, x: int, y: int) -> None:
        self.x = x
        self.y = y


    def print_position(self) -> None:
        print(f'{self.name} is at x: {self.x} y: {self.y}')