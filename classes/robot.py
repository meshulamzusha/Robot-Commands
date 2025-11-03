class Robot:
    def __init__(self, name: str) -> None:
        self.name = name


    def _get_command(self) -> list[str]:
        command = input(f'Give a command to {self.name}')
        return command.split(' ', 1)