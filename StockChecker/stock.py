import tkinter as tk
import yfinance as yf

def search():
    name = entry.get()
    code = stocks[name]
    stock= yf.Ticker(code)
    result.insert(tk.END, stock)

stocks = {
    "삼성전자" : "005930.KS",
    "앤비디아" : "NVDA",
    "애플" : "AAPL",
    "하이닉스" : "000660.KS",
    "아메리칸익스프레스" : "AXP"
}



window = tk.Tk()
window.title("StockChecker")

result = tk.Text(window, height=10, width=40)
result.pack()

label = tk.Label(window, text="종목 입력")
label.pack()

entry = tk.Entry(window)
entry.pack()

button = tk.Button(window, text="조회", command=search)
button.pack()

window.mainloop()