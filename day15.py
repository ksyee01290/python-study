def total(*args):
    result = 0
    for i in args:
        result += i
    return result

print(total(10,20,30,40,50))
"""
리스트 [] → 수정 가능 (추가, 삭제, 변경)
튜플 () → 수정 불가 (한번 만들면 고정)

"""