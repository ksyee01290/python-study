class Animal:
    """ Dog 자식"""
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name}이 먹어요")

class Dog(Animal):
    """Animal 엄마"""
    def dark(self):
        print(f"{self.name}이 짖어요")

dog = Dog("흑구")
dog.eat()
dog.dark()