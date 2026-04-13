def check_age(age):
    if age<0:
        raise ValueError("음수다매")
    return age

try:
    check_age(-5)

except ValueError as e:
    print("에러발생:", e)

# ValueError → 값이 잘못됐을 때
# TypeError → 타입이 잘못됐을 때
# ZeroDivisionError → 0으로 나눌 때
# FileNotFoundError → 파일 없을 때
# IndexError → 리스트 범위 벗어날 때
# KeyError → 딕셔너리에 없는 키 접근할 때
# NameError → 없는 변수 쓸 때
# AttributeError → 없는 메서드/속성 쓸 때