conbeni = {"포카칩":3,"김밥":2,"콜라":20}
def manu_buy():
    print(conbeni.keys())
    name = input("주문할 메뉴 입력:")
    count = int(input("수량 입력:"))

    if name in conbeni:
        conbeni[name] += count
        print(conbeni[name])
    else:
        print("메뉴를 잘못 입력")

    return

def manu_sel():
    print(conbeni.keys())
    name = input("판매할 메뉴 입력 :")
    if name in conbeni:    
        print(conbeni[name])
        count = int(input("수량 입력 :"))
        if conbeni[name] > count:       
            conbeni[name] -= count
            print(conbeni[name])
        else:
            print("재고가 없음")
    else:
        print("메뉴를 잘못 입력했슴")
    return

def manu_search():
    print(conbeni.items())
    return


while True:
    print("편의점 재고 관리프로그램")
    print("1. 상품 주문")
    print("2. 상품 판매")
    print("3. 재고 검색")
    print("4. 종료")

    num = int(input("메뉴를 입력해주세요:"))

    if num == 1:
        manu_buy()
    
    if num == 2:
        manu_sel()
    
    if num == 3:
        manu_search()

    if num == 4:
        print("종료합니다")
        break