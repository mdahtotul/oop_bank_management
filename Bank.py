from User import TrxHistory


class Bank:
    def __init__(self, name, address) -> None:
        self.name = name
        self.address = address
        self.accounts = []
        self.total_balance = 0
        self.total_loan = 0
        self.is_loan_available = True

    def add_account(self, user):
        self.accounts.append(user)
        self.total_balance += user.balance
        self.total_loan += user.loan
        obj = TrxHistory("own", user.balance, "Deposit")
        user.transaction_history.append(obj)

    def remove_account(self, user):
        self.accounts.remove(user)
        self.total_balance -= user.balance
        self.total_loan -= user.loan

    def deposit(self, user, amount):
        res = False
        if amount > 0:
            user.balance += amount
            self.total_balance += amount
            res = True
        else:
            print("Invalid amount")

        return res

    def withdraw(self, user, amount):
        res = False
        if user.balance >= amount:
            if self.total_balance >= amount:
                user.balance -= amount
                self.total_balance -= amount
                res = True
            else:
                print("Bank is bankrupt")
        else:
            print("Insufficient balance")

        return res

    def get_total_balance(self):
        return self.total_balance

    def get_total_loan(self):
        return self.total_loan

    def list_accounts(self):
        for account in self.accounts:
            print(
                f"Name: {account.name} \nEmail: {account.email} \nBalance: {account.balance} \nLoan:{account.loan} \nRole: {account.role}"
            )
            print("--------------------------------------------------\n")
