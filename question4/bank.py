# Function to check wheter some account is registered in the bank
def exist(bank, account: int) -> bool:
    if account < len(bank.getClients()) and account >= 0:
        return True
    else:
        return False


class Bank:
    def __init__(self) -> None:
        self.clients = []
    
    def getClients(self):
        return self.clients
    
    def createAccount(self, client) -> None:
        client.setAccount(len(self.clients))
        client.setBalance(0.0)
        self.clients.append(client)
    
    def transferFunds(self, command, client) -> None:
        otherAccount = command.getBeneficiaryAccount()
        value = command.getValue()
        if not exist(self, otherAccount):
            raise Exception("Beneficiary account does not exist")
        elif otherAccount == client.getAccount():
            raise Exception("Can't transfer to your own account")
        elif value > client.getBalance():
            raise Exception("Insuficient funds to make this transaction")
        elif value <= 0:
            raise Exception("Transfer value has to be a positive float")
        else:
            client.setBalance(client.getBalance() - value)
            self.clients[otherAccount].setBalance(self.clients[otherAccount].getBalance() + value)
        client.insertOperation(command)
        print("\nR${0:.2f} were transfered from your account to account {1}".format(value, otherAccount))    
        print("Current Balance : R${:.2f}".format(client.getBalance()))
     
    def withdrawMoney(self, command, client) -> None:
        value = command.getValue()
        if value > client.getBalance():
            raise Exception("Insuficient funds")
        elif value <= 0:
            raise Exception("Request should be a positive value")
        else:
            client.setBalance(client.getBalance() - value)
        client.insertOperation(command)
        print("\nR${:.2f}  were withdrawn from your account".format(value))
        print("Current Balance : R${:.2f}".format(client.getBalance()))
    
    def depositMoney(self, command, client) -> None:
        value = command.getValue()
        if value <= 0:
            raise Exception("Deposit must be a positive value")
        client.setBalance(client.getBalance() + value)
        client.insertOperation(command)
        print("\nR${:.2f} were deposited in your account".format(value))
        print("Current Balance : R${:.2f}".format(client.getBalance()))
    
    def checkBalance(self, command, client) -> None:
        print("\nCurrent Balance : R${:.2f}".format(client.getBalance()))
    
    def checkStatement(self, command, client) -> None:
        print("\n----------------------STATEMENT-----------------------")
        for operation in client.getStatement():
            if operation.__class__.__name__ == "DepositMoney":
                print("Money Deposited, Value = R${:.2f}".format(operation.getValue()))
            elif operation.__class__.__name__ == "WithdrawMoney":
                print("Money Withdrawn, Value = R${:.2f}".format(operation.getValue()))
            elif operation.__class__.__name__ == "TransferFunds":
                print("Transaction, Beneficiary Account: {0}, Value = R${1:.2f}".format(operation.getBeneficiaryAccount(), operation.getValue()))
            else:
                raise Exception("Exists at least one registered operation that shouldn't be part of the client's statement")
        
        print("\nCurrent Balance : R${:.2f}".format(client.getBalance()))
        print("------------------------------------------------------")