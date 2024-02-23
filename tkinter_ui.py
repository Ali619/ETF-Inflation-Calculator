import tkinter as tk
from etfs import etfs

class Create_Label():
    def __init__(self, window: tk.Tk, text: str, row: int, column: int):
        self.text = text
        self.window = window
        self.row = row
        self.column = column
        self.label = tk.Label(self.window, text=self.text)
        self.label.grid(row=self.row, column=self.column)

class Create_Entry():
    def __init__(self, window: tk.Tk, row: int, column: int):
        self.window = window
        self.row = row
        self.column = column
        self.entry = tk.Entry(self.window)
        self.entry.grid(row=self.row, column=self.column)
    
window = tk.Tk()
window.title("حباب سنج")
etf_name_label = Create_Label(window=window, text="نام صندوق", row=0, column=00)
last_price_label = Create_Label(window=window, text="قیمت پایانی", row=0, column=1)
nav_price_label = Create_Label(window=window, text="ابطال NAV قیمت", row=0, column=2)
result_label = Create_Label(window=window, text="میزان حباب (%)", row=0, column=3)            

i = 1
for k, v in etfs.items():
    Create_Label(window=window, text=etfs[k]["name"], row=i, column=0)
    etfs[k]["entry"].append((Create_Entry(window, row=i, column=1)).entry)
    etfs[k]["entry"].append((Create_Entry(window, row=i, column=2)).entry)
    etfs[k]["row_number"] = i
    i += 1