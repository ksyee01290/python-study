def add(a,b):
    return a+b

add = lambda a, b: a+b

print(add(3,5))

students = [("철수", 90), ("영희", 85), ("민수", 95)]

students.sort(key=lambda x: x[0])

print(students)

"""
x[0] 은 이름(문자열)이니까 알파벳 순으로 정렬된 거예요 — 민수(M), 영희(Y), 철수(C) 순서.
x[2] 는 튜플에 인덱스 2가 없어서 에러난 거예요. 각 튜플이 ("철수", 90) 이렇게 2개뿐이니까 0, 1만 있어요 😊
"""
