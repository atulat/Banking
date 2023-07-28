class Account:
    def __init__(self, AccName, AccNumber, AccBalance):
        self.AccName = AccName
        self.AccNumber = AccNumber
        self.AccBalance = AccBalance

    def __str__(self):
        return f"Account Number: {self.AccNumber}, Account Name: {self.AccName}, Balance: {self.AccBalance}"

    def Deposit(self, Amount):
        self.AccBalance += Amount

    def Withdraw(self, Amount):
        self.AccBalance -= Amount

    def Display(self):
        print("Account Number :", self.AccNumber)
        print("Account Name : ", self.AccName)
        print("Balance :", self.AccBalance)

class SavingsAccount(Account):
    def __init__(self, AccName, AccNumber, AccBalance, SavIntRate):
        super().__init__(AccName, AccNumber, AccBalance)
        self.SavIntRate = SavIntRate

    def AddInterest(self):
        IntrestAmount = self.AccBalance * (self.SavIntRate / 100)
        self.AccBalance += IntrestAmount

class LoanAccount(Account):
    def __init__(self, AccName, AccNumber, AccBalance, LoanIntRate):
        super().__init__(AccName, AccNumber, AccBalance)
        self.LoanIntRate = LoanIntRate

    def AddInterest(self):
        IntrestAmount = self.AccBalance * (self.LoanIntRate / 100)
        self.AccBalance -= IntrestAmount


account = Account("Atul A T", 2014115073, 2400)
print(account)
