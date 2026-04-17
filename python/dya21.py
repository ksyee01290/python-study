
passwords = {}
with open("text/passwords.txt", "r", encoding="utf-8") as f:
    for line in f:
        data = line.strip().split(",")
        passwords[data[0]] = data[1]

while True:
    print("메뉴 출력")
    print("1. 저장")
    print("2. 조회")
    print("3. 삭제")
    print("4. 종료")

    num = int(input("메뉴 입력:"))

    if num == 1:
        sight = input("사이트명 입력:")
        password = input("비밀번호 입력:")
        passwords[sight] = password
        print(passwords[sight]+"에 저장되었습니다.")

    elif num == 2:
        sight = input("사이트명 입력:")
        print(passwords[sight])


    elif num == 3:
        key = input("사이트명 입력:")
        del passwords[key]
                
    elif num == 4:
        with open("text/passwords.txt","w", encoding="utf-8") as f:
            for key, value in passwords.items():
                f.write(f"{key},{value}\n")      
        break
