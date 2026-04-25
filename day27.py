import requests
import json

city = input("도시 이름 입력: ")

try:
    response = requests.get(f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid=f31f56b24ff5ce60edf1fedf749ee5b8&units=metric")
    if response.status_code == 200:
        data = response.json()

        print(json.dumps(data,indent=2))

        print(f"{city} 현재 날씨")
        print(f"온도 : {data["main"]["temp"]}")
        print(f"날씨 : {data["weather"][0]["description"]}")
        print(f"지역 : {data["name"]}")
        
    else:
        print("존재하지 않는 도시입니다.")

except Exception as e:
    print("인터넷 연결을 확인해주세요.")


