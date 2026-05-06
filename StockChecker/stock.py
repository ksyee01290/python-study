import tkinter as tk
import yfinance as yf
import matplotlib as mpl
import mplfinance as mpf
import matplotlib.pyplot as plt
from datetime import datetime

mpl.rcParams['font.family'] = 'Malgun Gothic'

stocks = {
    "삼성전자" : ("005930.KS","Samsung"),
    "앤비디아" : ("NVDA","NVIDIA"),
    "애플" : ("AAPL","APPLE"),
    "하이닉스" : ("000660.KS","SK"),
    "아메리칸익스프레스" : ("AXP","AMEX"),
}

EXCHANGE_RATE = 1350

def search():
    result.delete(1.0, tk.END)
    result.insert(tk.END, "조회 중...\n")
    window.update()

    name = entry.get()

    if name not in stocks:
        result.delete(1.0, tk.END)
        result.insert(tk.END, f"'{name}'은 목록에 없는 종목입니다.")
        return
    
    code = stocks[name][0]
    stock= yf.Ticker(code)
    info = stock.info

    currency = info.get("currency")

    raw_price = info.get("currentPrice", 0)
    marketCap = info.get("marketCap", 0)
    twoweekhigh = info.get("fiftyTwoWeekHigh", 0)
    twoweeklow = info.get("fiftyTwoWeekLow", 0)
    regularmcp = info.get("regularMarketChangePercent", 0)
    
    if currency == "USD":
        price = int(raw_price * EXCHANGE_RATE)
        m_cap = int(marketCap * EXCHANGE_RATE)
        high = int(twoweekhigh * EXCHANGE_RATE)
        low = int(twoweeklow * EXCHANGE_RATE)
        unit_info = f"적용 환율: {EXCHANGE_RATE}원 (달러 기준)"
    else:
        price = int(raw_price)
        m_cap = marketCap
        high = int(twoweekhigh)
        low = int(twoweeklow)
        unit_info = "기준 화폐: 원화(KRW)"

    result.delete(1.0, tk.END)
    result.insert(tk.END, f"[{name} 정보] - {unit_info}\n")
    result.insert(tk.END, f"현재가: {price:,}원\n")

    if currency == "USD":
        result.insert(tk.END, f"현지 가격: ${raw_price:,.2f}\n")
    
    result.insert(tk.END, f"시가총액: {m_cap:,}원\n")
    result.insert(tk.END, f"52주 최고가: {high:,}원\n")
    result.insert(tk.END, f"52주 최저가: {low:,}원\n")
    result.insert(tk.END, f"등락률: {regularmcp:.2f}%\n")

# def show_graph():
#     plt.figure(figsize=(12, 6))
#     name = entry.get()
#     code = stocks[name]
#     stock = yf.Ticker(code)
#     history = stock.history(period="1mo")

#     plt.rcParams['font.family'] = 'Malgun Gothic'
#     plt.xticks(rotation=45)
#     plt.gca().yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f"{int(x):,}"))
#     plt.plot(history["Close"])
#     plt.title(name)
#     plt.show()

def show_graph():
    name = entry.get()
    code = stocks[name][0]
    eng_name = stocks[name][1]
    stock = yf.Ticker(code)
    history = stock.history(period="6mo")

    mpf.plot(history, type='candle', style='yahoo', title=eng_name, figsize=(12,6),
            show_nontrading=True, datetime_format='%m/%d')
    
def compare_stocks():
    raw_input = entry.get() 
    split_list = raw_input.split(',')

    names = []
    for n in split_list:
        clean_name = n.strip()
        names.append(clean_name)
    
    plt.figure(figsize=(12, 6))
    
    for name in names:
        if name in stocks:
            code = stocks[name][0]
            stock_data = yf.Ticker(code)
            history = stock_data.history(period="3mo")["Close"]
            
            yields = (history / history.iloc[0] - 1) * 100
            plt.plot(yields, label=name)
            
    plt.title("종목 비교 (수익률 %)")
    plt.legend()
    plt.grid(True)
    plt.show()
    
    def save_stock(now, name, price, marketCap):
        with open("stock.txt","a",encoding="utf-8") as f:
            f.write(f"=== {now}===\n")
            f.write(f"회사이름 : {name}\n")
            f.write(f"현재가: {price}\n")
            f.write(f"시가총액:{marketCap}\n")
            
now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

window = tk.Tk()
window.title("StockChecker")

result = tk.Text(window, height=15, width=60)
result.pack()

label = tk.Label(window, text="종목 입력")
label.pack()

entry = tk.Entry(window)
entry.bind("<Return>", lambda event: search())
entry.pack()

button_frame = tk.Frame(window)
button_frame.pack(pady=10)

btn_width = 15

button = tk.Button(button_frame, text="조회", command=search, width=btn_width)
button.grid(row=0, column=0, padx=5)

graph_button = tk.Button(button_frame, text="그래프", command=show_graph, width=btn_width)
graph_button.grid(row=0, column=1, padx=5)

compare_button = tk.Button(button_frame, text="종목 비교", command=compare_stocks, width=btn_width)
compare_button.grid(row=0, column=2, padx=5)

button_frame = tk.Button(button_frame, text="저장", command=save_stock, width=btn_width)
button_frame.grid(row=0, column=0, padx=5)


window.mainloop()