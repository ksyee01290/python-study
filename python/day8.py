dic = {'name': 'pey', 'phone':'010-7433-8469', 'birth':'1118'}

print(dic['name'])

dic.keys()
print(list(dic.keys()))
print(dic.items())

dics = {}
while True:
    print("전화번호부")
    print("1. 추가")
    print("2. 검색")
    print("3. 수정")
    print("4. 삭제")

    num = int(input("메뉴를 선택해라"))

    if num == 1:
        add = input("이름 입력(key입력) :")
        adds = input("전화번호 입력(value입력) :")
        dics[add] = adds
        print("추가 완료 쯨")

        print("-"*30)
    elif num == 2:
        print("-"*30)

        print(dics.keys())
        print("전체 메뉴중 고르시오")

        print("-"*30)

        num2 = input("검색할 key를 입력 :")
        print(dics.get(num2))

        print("-"*30)

    elif num == 3:
        print("수정할 메뉴를 고르시오")
        print(dics.keys())

        name = input("삭제할 이름 입력:")
        if name not in dics:
            print(f"'{name}'를 찾을수 없습니다.")
        print(f"현재 번호:{dics[name]}")
        new_phone = input("새 번호 입력:").strip()
        dics[name] = new_phone
        print("'{name}' 수정완료")


    elif num == 4:
        print("삭제할 메뉴를 고르시오")
        print(dics.keys())

        names = input("삭제할 이름 입력:")
        if names not in dics:
            print(f"'{names}'를 찾을수 없습니다.")
        del dics[names]
        print("삭제완료")

        
    else:

        break