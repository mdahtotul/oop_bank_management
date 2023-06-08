import datetime


class TrxHistory:
    def __init__(self, account, amount, type) -> None:
        self.account = account
        self.amount = amount
        self.type = type
        self.date = datetime.datetime.now()


class User:
    def __init__(self, name, email, password, balance) -> None:
        self.name = name
        self.email = email
        self.__password = password
        self.role = "User"
        self.balance = balance
        self.transaction_history = []
        self.loan = 0
        self.created_at = datetime.datetime.now()

    def create_account(self, bank):
        bank.add_account(self)

    def deposit_money(self, bank, amount):
        result = bank.deposit(self, amount)
        if result:
            obj = TrxHistory("own", amount, "Deposit")
            self.transaction_history.append(obj)

    def withdraw_money(self, bank, amount):
        result = bank.withdraw(self, amount)
        if result:
            obj = TrxHistory("own", amount, "Withdraw")
            self.transaction_history.append(obj)

    def transfer_money(self, user, amount, bank_balance):
        if self.balance >= amount:
            if bank_balance >= amount:
                self.balance -= amount
                user.balance += amount
                obj1 = TrxHistory(user.name, amount, "Fund Transfer")
                obj2 = TrxHistory(self.name, amount, "Fund Transfer")
                self.transaction_history.append(obj1)
                user.transaction_history.append(obj2)
            else:
                print("Bank is bankrupt")
        else:
            print("Insufficient balance")

    def get_transaction_history(self):
        if len(self.transaction_history) == 0:
            print("No transaction history found")
        else:
            print(f"\n\nTransaction history for {self.name}:\n")
            for item in self.transaction_history:
                time_format = item.date.strftime("%d-%b-%Y %H:%M:%S")
                print(
                    f"Transaction Type: {item.type}, Amount: {item.amount}, Account: {item.account}, Date: {time_format}"
                )

    def available_balance(self):
        return self.balance
