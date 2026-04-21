import csv

scores = []

with open("csv/students.csv", "r", encoding="utf-8") as f:
    reader = csv.reader(f)
    next(reader)

    for row in reader:
        scores.append(row)

scores.sort(key=lambda x: int(x[2]), reverse=True)

for row in scores:
    print(row)



#     for row in reader:
#         scores.append(int(row[2]))
# print(f"평균:{sum(scores)/len(scores):.0f}")
# print(f"최고점:{max(scores)}")
# print(f"최저점:{min(scores)}")