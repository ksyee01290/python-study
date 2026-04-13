print("짝수의합")
add = 0
for i in range(1,101):
    if i%2 == 0:
        add = add + i
print(add)

print("-"*30)

print("숫자 맞추기 게임")

import random

rnd = random.randint(1,100)

while True:
    num = int(input("숫자를 입력하시오: "))
    if num < rnd:
        print("up!")
    elif num > rnd:
        print("down!")
    else:
        print("정답")
        break

print("-"*30)

while True:
    
    print("1.무엇일까")
    print("2. 선택해봐")
    print("3. 종료")
    
    num = int(input("메뉴를 선택해주세요"))
    
    if num == 1:
        print("아무것도 없지롱")
    elif num == 2:
        print("잘못선택했어")
    else:
        print("잘가라")
        break