class Robot:
    def __init__(self, name: str) -> None:
        self.name = name


    def _get_command(self, command) -> list[str]:
        return command.split(' ', 1)