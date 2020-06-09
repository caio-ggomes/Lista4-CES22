import tkinter as tk
from client import Client
from bank import Bank

class Application(tk.Frame):
    def __init__(self, master=None) -> None:
        super().__init__(master)
        self.master = master
        self.create_widgets()
        self.bank = Bank()
        self.mainClient = Client(self.bank)

    def create_client(self) -> None:
        Client(self.bank)

    def create_widgets(self) -> None:
        self.checkBalance = tk.Button(self.master)
        self.checkBalance["text"] = "Check Account Balance"
        self.checkBalance["command"] = self.getBalance
        self.checkBalance.grid(row = 0, column = 0)

        self.checkStatement = tk.Button(self.master)
        self.checkStatement["text"] = "Check Account Statement"
        self.checkStatement["command"] = self.getStatement
        self.checkStatement.grid(row = 0, column = 1)

        self.withdrawMoney = tk.Button(self.master)
        self.withdrawMoney["text"] = "Withdraw Money"
        self.withdrawMoneyEntry = tk.Entry(self.master)
        self.withdrawMoney["command"] = self.withdrawMoneyfunc
        labelWithdraw = tk.Label(self.master, text = "Amount (R$)")
        self.withdrawMoney.grid(row = 3, column = 0)
        self.withdrawMoneyEntry.grid(row = 3, column = 2)
        labelWithdraw.grid(row = 2, column = 2)

        self.depositMoney = tk.Button(self.master)
        self.depositMoney["text"] = "Deposit Money"
        self.depositMoneyEntry = tk.Entry(self.master)
        self.depositMoney["command"] = self.depositMoneyfunc
        labelDeposit = tk.Label(self.master, text = "Amount (R$)")
        self.depositMoney.grid(row = 5, column = 0)
        self.depositMoneyEntry.grid(row = 5, column = 2)
        labelDeposit.grid(row = 4, column = 2)

        self.transferFunds = tk.Button(self.master)
        self.transferFunds["text"] = "Transfer Funds"
        self.transferFundsAccount = tk.Entry(self.master)
        self.transferFundsValue = tk.Entry(self.master)
        self.transferFunds["command"] = self.transferFundsfunc
        labelTransferAccount = tk.Label(self.master, text = "Beneficiary Account")
        labelTransferValue = tk.Label(self.master, text = "Amount (R$)")
        self.transferFunds.grid(row = 7, column = 0)
        self.transferFundsAccount.grid(row = 7, column = 1)
        self.transferFundsValue.grid(row = 7, column = 2)
        labelTransferAccount.grid(row = 6, column = 1)
        labelTransferValue.grid(row = 6, column = 2)

        self.quit = tk.Button(self.master, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.quit.grid(row = 0, column = 2)

    def getBalance(self) -> None:
        self.mainClient.checkBalance()
    
    def getStatement(self) -> None:
        self.mainClient.checkStatement()
    
    def withdrawMoneyfunc(self) -> None:
        value = self.withdrawMoneyEntry.get()
        try:
            value = float(value)
        except: 
            raise Exception("Invalid input, value should be float type")
        self.mainClient.withdrawMoney(value)

    def depositMoneyfunc(self) -> None:
        value = self.depositMoneyEntry.get()
        try:
            value = float(value)
        except:
            raise Exception("Invalid input, value should be float type")
        self.mainClient.depositMoney(value)

    def transferFundsfunc(self) -> None:
        account = self.transferFundsAccount.get()
        value = self.transferFundsValue.get()
        try:
            account = int(account)
            try:
                value = float(value)
            except:
                raise Exception("Invalid input, value should be float type")
        except:
            raise Exception("Invalid input, account should be integer type")
        if account < 0:
            raise Exception("Invalid input, account should be a non negative integer")
        else:
            self.mainClient.transferFunds(account, value)


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Cashier")
    root.geometry("500x200")
    root.grid_columnconfigure((0, 1), weight=1)
    app = Application(master=root)
    app.create_client()
    app.mainloop()    
