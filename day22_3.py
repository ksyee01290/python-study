class Animal:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound
    def speak(self):
        print(f"{self.name}이 {self.sound} 하고 울어요")


class Dog(Animal):
    def fetch(self):
        print(f"{self.name}가 공을 가져와요")

class Cat(Animal):
    def purr(self):
        print(f"{self.name}가 그루릉")

dog = Dog("흑구","멍멍")
cat = Cat("모카","야옹")

dog.fetch()
cat.purr()

dog.speak()
cat.speak()