def info(**kwargs):
    for i in kwargs:
        print(i, kwargs[i])

info(name="철수", age=20, city="서울")
"""
*args → 값만 넘길 때 → 튜플
**kwargs → 이름+값 넘길 때 → 딕셔너리
 """