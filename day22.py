class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self, food, amount):
        print(f"{self.name}{self.age}이{food}를 {amount}g 먹었다")

dog1 = Dog("흑구",32)
dog1.info("사료", 100)
