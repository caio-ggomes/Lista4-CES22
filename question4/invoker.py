class Invoker:
    def __init__(self) -> None:
        self.command = None
    def setCommand(self, command) -> None:
        self.command = command
    def executeCommand(self, client, bank) -> None:
        self.command.execute(client, bank)