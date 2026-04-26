from dotenv import load_dotenv
import requests, json, os

load_dotenv()
api_key = os.getenv("API_KEY")
city = input("도시 이름 입력: ")

try:
    response = requests.get(f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric")
    if response.status_code == 200:
        data = response.json()

        print(json.dumps(data,indent=2))
        with open("weather.txt","w",encoding="utf-8") as f:
            f.write(f"{city} 현재 날씨\n")
            f.write(f"온도 : {data["main"]["temp"]}\n")
            f.write(f"날씨 : {data["weather"][0]["description"]}\n")
            f.write(f"지역 : {data["name"]}\n")
            f.write(f"습도 : {data["main"]["humidity"]}\n")
            f.write(f"체감온도 : {data["main"]["feels_like"]}\n")
        
    else:
        print("존재하지 않는 도시입니다.")

except Exception as e:
    print("인터넷 연결을 확인해주세요.")


