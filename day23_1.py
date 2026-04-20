class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, money):
        self.balance = self.balance + money
        print(f"입금된 잔액은 {self.balance}원 입니다")

    def withdraw(self, money):
        self.balance = self.balance - money
        print(f"출금된 잔액은 {self.balance}원 입니다")

    def balance_search(self):
        print(f"{self.name}의 잔액은{self.balance}원 입니다.")

account = BankAccount("철수", 10000)
account.deposit(5000)
account.withdraw(3000)
account.balance_search()