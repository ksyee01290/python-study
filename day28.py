import yfinance as yf
from datetime import datetime
import time

def save_stock(now, name, price, marketCap):
    with open("stock.txt","a",encoding="utf-8") as f:
        f.write(f"=== {now}===\n")
        f.write(f"회사이름 : {name}\n")
        f.write(f"현재가: {price}\n")
        f.write(f"시가총액:{marketCap}\n")

stocks = {
    "삼성전자" : "005930.KS",
    "앤비디아" : "NVDA",
    "애플" : "AAPL",
    "하이닉스" : "000660.KS",
    "아메리칸익스프레스" : "AXP"
}
try:
    name = input("종목 입력: ")
    start = time.time()
    code = stocks[name]
    stock= yf.Ticker(code)

    info = stock.info
    currency = info["currency"]
    price = int(info["currentPrice"])
    marketCap = info["marketCap"]

    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    if currency == "USD":
        price_krw = price * 1380
        marketCap_krw = marketCap * 1380
        price_str = f"{price_krw:,}원 (${price:,})"
        marketCap_str = f"{marketCap_krw:,}원 (${marketCap:,})"

    else:
        price_str = f"{price:,}원"
        marketCap_str = f"{marketCap:,}원"

    save_stock(now, info["longName"],price_str,marketCap_str)

    # print(json.dumps(stock.info,indent=2))
    # print(stock.info)
except KeyError:
    print("오류")
except Exception as e:
    print("데이터를 가져올수없음")

end = time.time()
print(f"실행시간 : {end - start:.2f}초")