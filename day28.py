import yfinance as yf
from datetime import datetime

stocks = {
    "삼성전자" : "005930.KS",
    "앤비디아" : "NVDA",
    "애플" : "AAPL",
    "하이닉스" : "000660.KS",
    "아메리칸익스프레스" : "AXP"
}
 
name = input("종목 입력: ")
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
    
    with open("stock.txt","a",encoding="utf-8") as f:
        f.write(f"=== {now} ===\n")
        f.write(f"현재가 : {price_krw:,}원 (${price:,})\n")
        f.write(f"회사이름 : {info["longName"]}\n")
        f.write(f"시가총액 : {marketCap_krw:,}원 (${marketCap:,})\n")

else:
    with open("stock.txt","a",encoding="utf-8") as f:
        f.write(f"=== {now} ===\n")
        f.write(f"현재가 : {price:,}원\n")  
        f.write(f"회사이름 : {info["longName"]}\n")
        f.write(f"시가총액 : {info["marketCap"]:,}\n")
# print(json.dumps(stock.info,indent=2))
# print(stock.info)