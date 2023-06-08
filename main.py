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

    bank.list_accounts()


if __name__ == "__main__":
    main()
