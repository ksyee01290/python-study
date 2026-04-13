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