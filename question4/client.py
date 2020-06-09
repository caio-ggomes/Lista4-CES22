from invoker import *
from commands import CheckBalance, CheckStatement, TransferFunds, DepositMoney, WithdrawMoney


class Client:
    def __init__(self, bank) -> None:
        self.bank = bank
        self.account = None
        self.balance = None
        self.statement = []
        bank.createAccount(self)
        self.invoker = Invoker()
    
    # Methods which are only executable by Bank

    def setAccount(self, newAccount) -> None:
        self.account = newAccount
    
    def setBalance(self, newBalance) -> None:
        self.balance = newBalance
    
    def getAccount(self) -> int:
        return self.account
    
    def getBalance(self) -> float:
        return self.balance

    def getStatement(self):
        return self.statement
    
    def insertOperation(self, command) -> None:
        self.statement.append(command)

    # Methods that client attempt to execute,
    # waiting for Bank response

    def checkBalance(self) -> None:
        command = CheckBalance()
        self.invoker.setCommand(command)
        self.invoker.executeCommand(self, self.bank)

    def checkStatement(self) -> None:
        command = CheckStatement()
        self.invoker.setCommand(command)
        self.invoker.executeCommand(self, self.bank)
        
    def transferFunds(self, otherAccount: int, value: float) -> None:
        command = TransferFunds(otherAccount, value)
        self.invoker.setCommand(command)
        self.invoker.executeCommand(self, self.bank)
        
    def withdrawMoney(self, value: float) -> None:
        command = WithdrawMoney(value)
        self.invoker.setCommand(command)
        self.invoker.executeCommand(self, self.bank)
        
    def depositMoney(self, value: float) -> None:
        command = DepositMoney(value)
        self.invoker.setCommand(command)
        self.invoker.executeCommand(self, self.bank)
