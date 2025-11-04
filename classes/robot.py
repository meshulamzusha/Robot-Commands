from abc import ABC, abstractmethod


class Robot(ABC):
    def __init__(self, name: str) -> None:
        self.name = name


    def _get_command(self, command) -> None:
        self.robot_action(command.split(' ', 1))
    

    @abstractmethod
    def robot_action(self, complete_command: list[str]) -> None:
        pass