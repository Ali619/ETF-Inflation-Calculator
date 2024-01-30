import tkinter as tk
from tkinter_ui import window, etfs

def calculator():
    for k,v in etfs.items():
        if etfs[k]["etf_start"].get() and etfs[k]["etf_stop"].get(): 
            try:
                result = (int(etfs[k]["etf_start"].get()) - int(etfs[k]["etf_stop"].get())) / int(etfs[k]["etf_stop"].get()) * 100
                if 0.0 <= result < 7.0:
                    tk.Label(window, text=f"  {result:.2f} %  ", fg="green").grid(row=etfs[k]["row_number"], column=3)
                if 7.01 <= result < 15.0:
                    tk.Label(window, text=f"  {result:.2f} %  ", fg="orange").grid(row=etfs[k]["row_number"], column=3)
                if 15.01 <= result:
                    tk.Label(window, text=f"  {result:.2f} %  ", fg="red").grid(row=etfs[k]["row_number"], column=3)

            except Exception as e:
                print(e)
                pass

        elif not etfs[k]["etf_start"].get() or not etfs[k]["etf_stop"].get():
            tk.Label(window, text=f" "*20).grid(row=etfs[k]["row_number"], column=3)

calc_infl_button = tk.Button(window, text="اجرا", command=calculator, borderwidth=5, width=20, fg="red").grid(row=9, column=0, columnspan=2)
exit_button = tk.Button(window, text="خروج", command=exit, borderwidth=5, width=20, fg="red").grid(row=9, column=2, columnspan=3)
