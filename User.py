from Bank import Bank


class User:
    def __init__(self, name, email, password, balance) -> None:
        self.name = name
        self.email = email
        self.__password = password
        self.role = "User"
        self.balance = balance
        self.transactionHistory = []
        self.loan = 0

    def create_account(self, bank):
        bank.add_account(self)
