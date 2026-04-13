def greet(name, msg="hello"):
    print(msg + name)

def add(a,b=3):
    return a+b

def gugudan(dan, start=2, end=9):
    for i in range(start, end+1):
        print(dan * i)

def temp(celsius, unit =""):
    print(celsius, unit)

def print_list(items, sep =", "):
    print(items, sep)
