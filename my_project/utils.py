import datetime

def inputs():
    numbers = []
    while True:
        num = input("수입력 (끝내려면 'q'입력):")
        if num == "q":
            break
        numbers.append(int(num))
    return numbers

def brith():
    birth = datetime.date(int(input("년:")), int(input("월:")), int(input("일:")))
    day = datetime.date.today()
    result = day.year - birth.year
    return result

def manu():
    print("1. 더하기")
    print("2. 빼  기")
    print("3. 나누기")
    print("4. 곱하기")
    
    return