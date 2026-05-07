import csv

scores = []

with open("csv/students.csv", "r", encoding="utf-8") as f:
    reader = csv.reader(f)
    next(reader)

    for row in reader:
        scores.append(int(row[2]))
avg = sum(scores)/len(scores)
max_score = max(scores)
min_score = min(scores)

with open("report.txt","w",encoding="utf-8") as f:
    f.write("=== 성적 보고서 ===\n")
    f.write(f"평균:{avg}점\n")
    f.write(f"최고점: {max_score}점\n")
    f.write(f"최저점: {min_score}점\n")



#     for row in reader:
#         scores.append(int(row[2]))
# print(f"평균:{sum(scores)/len(scores):.0f}")
# print(f"최고점:{max(scores)}")
# print(f"최저점:{min(scores)}")