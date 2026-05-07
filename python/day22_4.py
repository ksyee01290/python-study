class Menu:
    """카페 메뉴 할인"""
    def __init__(self, name, price):
        self.name = name
        self.price = price
    
    def discount(self, percent):
        sale = self.price * (1 - percent /100)
        print(f"{self.name} 할인가: {sale}원")

class Employee:
    def __init__(self, name, department, salary):
        self.name = name
        self.department = department
        self.salary = salary

    def increase(self, percent):
        sal = self.salary * (1 + percent/100)
        print(f"{self.name}님의 연봉은 {sal}만원 으로 인상되셧습니다")

class coupang:
    def __init__(self, name, num):
        self.name = name
        self.num = num
    
    def add_stock(self, amount):
        self.num = self.num + amount
        print(f"{self.num}개 추가되었습니다.")

    def remove_stock(self, amount):
        self.num = self.num - amount
        print(f"{self.num}개 사라짐")
        
item = coupang("신발", 100)
item.add_stock(50)
item.remove_stock(30)


# humen = Employee("근원","개발부서",3000)
# humen.increase(12)
# coffee = Menu("아메리카노", 4000)
# coffee.discount(15)