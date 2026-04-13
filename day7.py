list = []
while True:
    
    print("1. 입력")
    print("2. 평균")
    print("3. 최곶점")

    num = int(input("메뉴를 선택해라"))

    if num == 1:
        add = int(input("점수 입력해라"))
        list.append(add)
        print("점수가 입력되었따 쯨")
    elif num == 2:
        result = sum(list)
        print(f"평균 :{result/ len(list)}")
        
    else:
        max_value = max(list)
        print("최고점은",max_value)
        break