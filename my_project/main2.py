import calculator, utils
import datetime

# print(utils.brith())
birth = datetime.date(int(input("년:")), int(input("월:")), int(input("일:")))
day = datetime.date.today()
next_birthday = datetime.date(day.year, birth.month, birth.day)

if day > next_birthday:
    next_birthday = datetime.date(day.year+1, birth.month, birth.day)
    
else :
    next_birthday = datetime.date(day.year,birth.month,birth.day)

result = next_birthday - day
print(next_birthday)
print(result.days)