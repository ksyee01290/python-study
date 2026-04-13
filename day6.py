

print("-"*30)
list = []
while True:
    
    print("1. 추가")
    print("2. 삭제")
    print("3. 조회")

    num = int(input("메뉴를 선택해라"))

    if num == 1:
        add = int(input("리스트 추가해주십쇼"))
        list.append(add)
        print("추가되었습니다.")
    elif num == 2:
        add = int(input("삭제할부분 입력해주십쇼"))
        del list[add]
        print("삭제되었습니다.")
    else:
        print(list)