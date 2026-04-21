class PasswordManager:
    def __init__(self):
        self.passwords = {}
        self.load_passwords()

    def save_password(self):
        site = input("사이트명 입력:")
        password = input("비밀번호 입력:")
        self.passwords[site] = password
        print(f"{site}에 저장되었습니다.")

    def search_password(self):
        site = input("사이트명 입력:")
        if site in self.passwords:
            print(self.passwords[site])

    def delete_password(self):
        site = input("사이트명 입력:")
        if site in self.passwords:
            del self.passwords[site]

    def exit_program(self):
        with open("text/passwords.txt","w", encoding="utf-8") as f:
            for key, value in self.passwords.items():
                f.write(f"{key},{value}\n")   

    def load_passwords(self):
        try:
            with open("text/passwords.txt", "r", encoding="utf-8") as f:
                for line in f:
                    data = line.strip().split(",")
                    self.passwords[data[0]] = data[1]
        except FileNotFoundError:
            pass

pm = PasswordManager()

while True:
    print("메뉴 출력")
    print("1. 저장")
    print("2. 조회")
    print("3. 삭제")
    print("4. 종료")

    num = int(input("메뉴 입력:"))

    if num == 1:
        pm.save_password()
    elif num == 2:
        pm.search_password()
    elif num == 3:
        pm.delete_password()             
    elif num == 4:
        pm.exit_program()
        break
