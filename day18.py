import random
import datetime
random.randint(1,6)

print(random.randint(1,6))
print(datetime.date.today())
goal = datetime.date(2026, 6, 12)
day = datetime.date.today()
result = goal-day

print(result.days)