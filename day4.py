'''반복문 하는날'''
for i in range(1,101):
    print(i)
print("*"*30)

add = 0
for i in range(2,10):
    for j in range(1,10):
        add = i * j
        print(i,"*",j,"=" ,add)
    print("*"*30)

for i in range(5):
    print("*")

print("-"*30)

for i in range(5):
    for j in range(i+1):
        star = "*"
        print(star, end="")
    print()

print("-"*30)

for i in range(5):
    for j in range(5-i):
        star = "*"
        print(star, end="")
    print()

print("-"*30)