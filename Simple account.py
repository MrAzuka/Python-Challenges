import datetime
import pytz


class Account:
    """ Simple account class with balance """
    @staticmethod
    def _current_time():
        utc_time = datetime.datetime.utcnow()
        return pytz.utc.localize(utc_time)

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.transactionList = []
        print("Account created for {}.".format(self.name))

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.showBalance()
            self.transactionList.append((Account._current_time(), amount))

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            self.transactionList.append((Account._current_time(), -amount))
        else:
            print("Invalid Transaction.")
        self.showBalance()

    def showBalance(self):
        print("Balance is {}".format(self.balance))

    def transactions(self):
        for date, amount in self.transactionList:
            if amount > 0:
                tranType = "Deposited"
            else:
                tranType = "Withdrawn"
                amount *= -1
            print("{:4} {} on {} (localtime was {}".format(amount, tranType, date, date.astimezone()))


if __name__ == "__main__":
    oliseh = Account("Olisemelie", 0)
    oliseh.showBalance()

    oliseh.deposit(5000)
    # oliseh.showBalance()
    oliseh.withdraw(3000)
    # oliseh.showBalance()

    oliseh.deposit(3000)
    oliseh.withdraw(1000000)
    oliseh.transactions()
    print(oliseh.__dict__)