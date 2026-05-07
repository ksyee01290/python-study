# test 계산기

def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def div(a,b):
    return a/b
def mul(a,b):
    return a*b
def text():
    a = int(input("수입력:"))
    b = int(input("수입력:"))
    return a,b

while True:
    
    print("1. 더하기")
    print("2. 빼기")
    print("3. 나누기")
    print("4. 곱하기")
    num = int(input("숫자 입력:"))

    if num == 1:
        a,b = text()
        print(add(a,b))
    elif num == 2:
        a,b = text()
        print(sub(a,b))
    elif num == 3:
        a,b = text()
        print(div(a,b))        
    elif num == 4:
        a,b = text()
        print(mul(a,b))
