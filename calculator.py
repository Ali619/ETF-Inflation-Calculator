import tkinter as tk
import sys
from persiantools.jdatetime import JalaliDate
from tkinter_ui import window
from etfs import etfs
from tabulate import tabulate

def calculator():
    final_result = {'last_price': [], 'nav_price': [], 'bubble (%)': [], 'name': []}
    color_ranges = {
        (None, 0): "blue",
        (0, 7): "green",
        (7, 15): "orange",
        (15, None): "red"
    }
    
    for k, v in etfs.items():
        try:
            last_price, nav_price = int(v["entry"][0].get()), int(v["entry"][1].get())
            result = (last_price - nav_price) / nav_price * 100

            color = next(color for (min_val, max_val), color in color_ranges.items() 
                        if (min_val is None or result > min_val) and (max_val is None or result <= max_val))
            
            tk.Label(window, text=f"  {result:.2f} %  ", fg=color).grid(row=v["row_number"], column=3)
            final_result['name'].append(str(v['name']))
            final_result['last_price'].append(str(last_price))
            final_result['nav_price'].append(str(nav_price))
            final_result['bubble (%)'].append(str(result))
        except Exception as e:
            tk.Label(window, text=" "*20).grid(row=v["row_number"], column=3)
            print(e)
            pass
    return final_result

def save_as_text():
    result = calculator()
    with open(f"{JalaliDate.today()}.txt", 'w', encoding='utf-8') as f:
        f.write(tabulate(result, headers = 'keys', tablefmt = 'psql', numalign="center", stralign="center"))

calc_infl_button = tk.Button(window, text="اجرا", command=lambda: calculator(), borderwidth=5, width=25, fg="green").grid(row=len(etfs)+1, column=0, columnspan=2)
save_as_text_button = tk.Button(window, text="ذخیره کردن اطلاعات", command=lambda: save_as_text(), borderwidth=5, width=15, fg="blue").grid(row=len(etfs)+1, column=2, columnspan=1)
exit_button = tk.Button(window, text="خروج", command=lambda: sys.exit(), borderwidth=5, width=10, fg="red").grid(row=len(etfs)+1, column=3, columnspan=1)