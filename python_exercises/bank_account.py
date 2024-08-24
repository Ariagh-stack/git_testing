from random import randrange
from typing import List


class BankAccount:
    """
    Bank Account Management
    """

    all_account_numbers: List[int] = []
    last_account_number = 999

    def __init__(self, name) -> None:
        BankAccount.last_account_number += 1
        an = BankAccount.last_account_number
        self.account_number: int = an
        BankAccount.all_account_numbers.append(an)
        self.name = name
        self.balance: float = 0

    def display(self) -> None:
        """
        Show Account Balance
        :return:
        """
        print("_" * 40)
        print(f"hi, {self.name}\nYour current balance is: {self.balance}")
        print("_" * 40)

    def deposit(self) -> None:
        """
        Increase Account Balance
        :return:
        """
        amount = float(input("Please Enter amount to deposit: "))
        self.balance += amount
        self.display()

    def withdraw(self) -> None:
        """
        Withdraw from bank Account
        :return:
        """
        amount = float(input("Please Enter amount to withdraw: "))
        if amount > self.balance:
            print("Insufficient Balance!")
        else:
            self.balance -= amount
        self.display()


def main():
    acc1 = BankAccount("Aria Ghodrati")
    acc1.display()
    print(f"Your account number : {acc1.account_number}")

    while True:
        choice = int(input("Enter 1 to see your current balance\nEnter 2 to deposit\n"
                           "Enter 3 to withdraw\nEnter 4 to exit\n\t\tYour choice: "))

        if choice == 1:
            acc1.display()
        elif choice == 2:
            acc1.deposit()
        elif choice == 3:
            acc1.withdraw()
        elif choice == 4:
            print()
            print("Thanks for your precious time!")
            break
        else:
            print("Invalid Input!!\nPlease Enter a valid number for your choice")
            print("_" * 40)


if __name__ == "__main__":
    main()







