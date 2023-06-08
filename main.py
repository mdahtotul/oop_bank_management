from User import User
from Bank import Bank


def main():
    bank = Bank("Baper Bank", "Uganda")

    # adding user from bank
    user1 = User("Chan Mia", "chan@mia.com", "1234", 1000)
    bank.add_account(user1)

    user2 = User("Kala Manik", "kala@manik.com", "45678", 5000)
    bank.add_account(user2)

    # user can create account by themselves
    user3 = User("Kopa Samsu", "kopa@samsu.com", "adbdsc", 7000)
    user3.create_account(bank)

    # bank.list_accounts()
    print("#############################################\n")
    print(f"Total Balance: {bank.get_total_balance()}")
    # user can deposit money
    user1.deposit_money(bank, 1070)
    user1.deposit_money(bank, 4000)
    user1.withdraw_money(bank, 1000)
    user1.withdraw_money(bank, 2000)
    user1.deposit_money(bank, 3000)
    user1.transfer_money(user2, 1000, bank.total_balance)

    bank.provide_loan(user3, 14002, 10, 2)
    # bank.list_accounts()

    print("-------------- Transaction History --------------")
    # user1.get_transaction_history()
    # user2.get_transaction_history()


if __name__ == "__main__":
    main()
