def convert_case(stl):
    result = ""
    for char in stl:
        if char.isupper():   
            result += char.lower()
        elif char.islower():
            result += char.upper()
    return result

def noblock(stl):
    result = stl.replace(" ", "")
    return result

def strchange(stl):
    result = ""
    for char in stl:
        result = char +result
    return result

def strcount(stl):
    result = len(stl)
    return result

def inputs():
    stl = input("글자를 입력하시오 : ")
    return stl

def manu():
    print("1. 대소문자 변환")
    print("2. 공백 제거")
    print("3. 문자열 뒤집기")
    print("4. 글자 수 세기")
    print("5. 종료")
    return

while True:
    manu()
    name = int(input("메뉴를 골라라"))
    if name == 1:
        text = inputs()
        print(convert_case(text))
    
    elif name == 2:
        text = inputs()
        print(noblock(text))

    elif name == 3:
        text = inputs()
        print(strchange(text))

    elif name == 4:
        text = inputs()
        print(strcount(text))
    else:
        break