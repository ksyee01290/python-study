import csv

scores = []

with open("world_population.csv", "r", encoding="utf-8") as f:
    reader = csv.reader(f)
    header = next(reader)

    for row in reader:
        if row[2] == "South Korea":
            scores.append(row)
    for year, population in zip(header[5:13], scores[0][5:13]):
        print(year, population)
    
    print(type(scores))
    print(scores)