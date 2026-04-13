numbers =[i for i in range(10)]

print(numbers)

numbers2 =[i**2 for i in range(1,11)]

print(numbers2)

numbers3 =[i for i in range(10) if i%2 ==0]

print(numbers3)

numbers4 = ['apple', 'banana', 'cherry']

result =[i.upper() for i in numbers4 ]
print(result)

numbers5 = [i for i in range(10) if i>5]
print(numbers5)