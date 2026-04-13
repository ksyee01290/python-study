import util
import requests

print(util.add(1,2))
response = requests.get("https://www.naver.com")
print(response.status_code)