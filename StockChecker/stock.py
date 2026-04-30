import tkinter as tk
import yfinance as yf
import matplotlib.pyplot as plt

stocks = {
    "삼성전자" : "005930.KS",
    "앤비디아" : "NVDA",
    "애플" : "AAPL",
    "하이닉스" : "000660.KS",
    "아메리칸익스프레스" : "AXP"
}

def search():
    result.delete(1.0, tk.END)
    result.insert(tk.END, "조회 중...\n")
    window.update()

    name = entry.get()
    code = stocks[name]
    
    stock= yf.Ticker(code)
    info = stock.info
    price = int(info["currentPrice"])
    marketCap = info["marketCap"]
    twoweekhigh = int(info["fiftyTwoWeekHigh"])
    twoweeklow = int(info["fiftyTwoWeekLow"])
    regularmcp = int(info["regularMarketChangePercent"])
    
    result.insert(tk.END, f"현재가: {price:,}원\n")
    result.insert(tk.END, f"시가총액: {marketCap:,}원\n")
    result.insert(tk.END, f"52주 최고가: {twoweekhigh:,}원\n")
    result.insert(tk.END, f"52주 최저가: {twoweeklow:,}원\n")
    result.insert(tk.END, f"등락률: {regularmcp:,}원\n")

def show_graph():
    plt.figure(figsize=(12, 6))
    name = entry.get()
    code = stocks[name]
    stock = yf.Ticker(code)
    history = stock.history(period="1mo")

    plt.rcParams['font.family'] = 'Malgun Gothic'
    plt.xticks(rotation=45)
    plt.gca().yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f"{int(x):,}"))
    plt.plot(history["Close"])
    plt.title(name)
    plt.show()

window = tk.Tk()
window.title("StockChecker")

result = tk.Text(window, height=10, width=40)
result.pack()

label = tk.Label(window, text="종목 입력")
label.pack()

entry = tk.Entry(window)
entry.bind("<Return>", lambda event: search())
entry.pack()

button = tk.Button(window, text="조회", command=search)
button.pack()

graph_button = tk.Button(window, text="그래프", command=show_graph)
graph_button.pack()

window.mainloop()