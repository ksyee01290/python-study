class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def login(self):
        print(f"{self.email}로 로그인")
        
class Customer(User):
    def buy(self, item):
        print(f"{self.name}이 {item} 구매")

class Seller(User):
    def sell(self, item):
        print(f"{self.name}이 {item} 판매")

customer = Customer("철수", "cs@gmail.com")
seller =Seller("맹구","yh@gmail.com")

customer.login()
seller.login()

customer.buy("신발")
seller.sell("신발")

# 모든 머머가 다 하는 건가?