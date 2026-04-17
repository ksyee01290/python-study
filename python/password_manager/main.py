def save_password():
    site = input("사이트명 입력:")
    password = input("비밀번호 입력:")
    passwords[site] = password
    print(f"{site}에 저장되었습니다.")

def search_password():
    site = input("사이트명 입력:")
    print(passwords[site])

def delete_password():
    site = input("사이트명 입력:")
    del passwords[site]

def exit_program():
    with open("text/passwords.txt","w", encoding="utf-8") as f:
        for key, value in passwords.items():
            f.write(f"{key},{value}\n")   

def load_passwords():
    try:
        with open("text/passwords.txt", "r", encoding="utf-8") as f:
            for line in f:
                data = line.strip().split(",")
                passwords[data[0]] = data[1]
    except Exception as e:
        print("에러발생:", e)

passwords = {}
load_passwords()

while True:
    print("메뉴 출력")
    print("1. 저장")
    print("2. 조회")
    print("3. 삭제")
    print("4. 종료")

    num = int(input("메뉴 입력:"))

    if num == 1:
        save_password()
    elif num == 2:
        search_password()
    elif num == 3:
        delete_password()             
    elif num == 4:
        exit_program()
        break
