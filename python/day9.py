sentence = input("문장 입력: ")
words = sentence.split()
count = {}

for ist in words:
    if ist in count:
        count[ist] += 1
    else:
        count[ist] = 1

print(count)