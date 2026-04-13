import os

def save(filename, content):
    with open(filename, "w", encoding="utf-8") as f:
        f.write(content)

def load(filename):
    with open(filename, "r", encoding="utf-8") as f:
        return f.read()


while True:
    try:
        print("1. 메모 쓰기(저장)")
        print("2. 메모 불러오기(읽기)")
        print("3. 메모 삭제")
        str = int(input("메뉴를 선택하시오:"))

        if str == 1:
            text = input("파일명:")
            text2 = input("메모작성:")
            save(text,text2)
        elif str == 2:
            text = input("불러올 파일명 입력:")
            print(load(text))
        elif str == 3:
            text = input("삭제할 파일명 입력:")
            os.remove(text)

        else :
            break
    except FileNotFoundError:
        print("파일이 없습니다.")