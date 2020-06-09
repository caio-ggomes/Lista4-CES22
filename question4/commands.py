from abc import ABC, abstractmethod


class Command(ABC):
    @abstractmethod
    def execute(self, client, bank) -> None:
        pass


class CheckBalance(Command):
    def execute(self, client, bank) -> None:
        bank.checkBalance(self, client)


class CheckStatement(Command):
    def execute(self, client, bank) -> None:
        bank.checkStatement(self, client)


class TransferFunds(Command):
    def __init__(self, beneficiaryAccount: int, value: float) -> None:
        self.beneficiaryAccount = beneficiaryAccount
        self.value = value
    
    def getBeneficiaryAccount(self) -> int:
        return self.beneficiaryAccount
    
    def getValue(self) -> float:
        return self.value

    def execute(self, client, bank) -> None:
        bank.transferFunds(self, client)


class WithdrawMoney(Command):
    def __init__(self, value: float) -> None:
        self.value = value
    
    def getValue(self) -> float:
        return self.value

    def execute(self, client, bank) -> None:
        bank.withdrawMoney(self, client)


class DepositMoney(Command):
    def __init__(self, value: float) -> None:
        self.value = value

    def getValue(self) -> float:
        return self.value

    def execute(self, client, bank) -> None:
        bank.depositMoney(self, client)