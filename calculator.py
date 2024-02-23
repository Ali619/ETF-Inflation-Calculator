import tkinter as tk
from tkinter_ui import window
from etfs import etfs

def calculator():
    for k,v in etfs.items(): 
            try:
                last_price, nav_price = int(etfs[k]["entry"][0].get()), int(etfs[k]["entry"][1].get())
                result = (int(last_price) - int(nav_price)) / int(nav_price) * 100
                if result <= 0:
                    tk.Label(window, text=f"  {result:.2f} %  ", fg="blue").grid(row=etfs[k]["row_number"], column=3)
                if 0.0 <= result < 7.0:
                    tk.Label(window, text=f"  {result:.2f} %  ", fg="green").grid(row=etfs[k]["row_number"], column=3)
                if 7.01 <= result < 15.0:
                    tk.Label(window, text=f"  {result:.2f} %  ", fg="orange").grid(row=etfs[k]["row_number"], column=3)
                if 15.01 <= result:
                    tk.Label(window, text=f"  {result:.2f} %  ", fg="red").grid(row=etfs[k]["row_number"], column=3)
            except Exception as e:
                tk.Label(window, text=f" "*20).grid(row=etfs[k]["row_number"], column=3)
                print(e)
                pass
        
calc_infl_button = tk.Button(window, text="اجرا", command=lambda: calculator(), borderwidth=5, width=20, fg="red").grid(row=len(etfs)+1, column=0, columnspan=2)