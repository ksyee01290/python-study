with open("students.csv", "r", encoding="utf-8") as f:
    result = 0
    scores = []
    for line in f:
        data = line.strip().split(",")
        if data[0] == "이름":
            continue
        scores.append(int(data[2]))

    for i in scores:
        result +=i
    
    result = result/len(scores)
    print(result)