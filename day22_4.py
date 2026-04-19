class Menu:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    
    def discount(self, percent):
        sale = self.price * (1 - percent /100)
        print(f"{self.name} 할인가: {sale}원")

coffee = Menu("아메리카노", 4000)
coffee.discount(15)