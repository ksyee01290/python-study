def add(numbers):
    result = numbers[0]
    for i in numbers[1:]:
        result += i
    return result

def sub(numbers): 
    result = numbers[0]
    for i in numbers[1:]:
        result -= i
    return result

def div(numbers):
    result = numbers[0]
    for i in numbers[1:]:
        result /= i
    return result

def mul(numbers):
    result = numbers[0]
    for i in numbers[1:]:
        result *= i
    return result

def inputs():
    numbers = []
    while True:
        num = input("수입력 (끝내려면 'q'입력):")
        if num == "q":
            break
        numbers.append(int(num))
    return numbers

def manu():
    print("1. 더하기")
    print("2. 빼  기")
    print("3. 나누기")
    print("4. 곱하기")
    
    return

while True:
    manu()
    name = int(input("메뉴를 골라라"))
    if name == 1:
        num = inputs()
        print(add(num))
    
    elif name == 2:
        num = inputs()
        print(sub(num))

    elif name == 3:
        num = inputs()
        print(div(num))

    elif name == 4:
        num = inputs()
        print(mul(num))
    else:
        break