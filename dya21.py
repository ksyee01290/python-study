
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
        with open("passwords.txt", "a", encoding="utf-8") as f:
            f.write(f"{sight},{password}\n")

    elif num == 2:
        sight = input("사이트명 입력:")
        with open("passwords.txt", "r", encoding="utf-8") as f:
            for line in f:
                data = line.strip().split(",")
                if data[0] == sight:
                    print(data[1])

    elif num == 3:
        sight = input("사이트명 입력:")
        lines = []

        with open("passwords.txt", "r", encoding="utf-8") as f:
            for line in f:
                data = line.strip().split(",")
                if data[0] != sight:
                    lines.append(line)

        with open("passwords.txt", "w", encoding="utf-8") as f:
            f.writelines(lines)
                
    elif num == 4:
        break
