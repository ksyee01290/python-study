def is_even(x):
    return x%2 ==0

numbers =[1,2,3,4,5,6]
result = list(filter(is_even, numbers))
print(result)

"""
# DB에서 가져온 가격에 부가세 10% 붙이기
prices = [10000, 25000, 8000, 15000]
result = list(map(lambda x: x * 1.1, prices))


# 회원 중 활성 유저만 뽑기
users = [
    {"name": "철수", "active": True},
    {"name": "영희", "active": False},
    {"name": "민수", "active": True}
]
result = list(filter(lambda x: x["active"], users))

# 리스트 컴프리헨션
result = [x * 1.1 for x in prices]
result = [x for x in users if x["active"]]

"""