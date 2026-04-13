


pocket = ['paper', 'cellphone', 'money']
card = True

if 'mone' in pocket:
    print("택시타라")

else:
    if card:
        print("택시타")
    
    else:
        print("걸어가")


grade = "A"
match grade:
    case "A":
        print("탁월하군")
    case "B":
        print("좋군")
    case "C":
        print("별로군")
    case _:
        print("잘못적었군")

grade = "s"
match grade:
    case "A" | "B" | "C":
        print("잘했군")
    case _:
        print("불합격이군")


''' 성적등급 계산기'''

score = int(input("점수를 입력하시오: "))

match score:
    case score if score >= 90:
        print("A 등급")
    case score if score >= 70:
        print("B 등급")
    case score if score >= 50:
        print("C 등급")
    case _:
        print("F 등급")

''' 홀짝 판별기'''
number = int(input("숫자를 입력해주세요 :"))

if number % 2:
    print("홀수")
else:
    print("짝수")