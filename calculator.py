import tkinter as tk
from tkinter_ui import window
from buttons import buttons
from tabulate import tabulate

def calculator():
    final_result = {'name': [], 'last_price': [], 'nav_price': [], 'bubble': []}
    for k,v in buttons.items(): 
            try:
                last_price, nav_price = int(buttons[k]["entry"][0].get()), int(buttons[k]["entry"][1].get())
                result = (int(last_price) - int(nav_price)) / int(nav_price) * 100
                if result <= 0:
                    tk.Label(window, text=f"  {result:.2f} %  ", fg="blue").grid(row=buttons[k]["row_number"], column=3)
                if 0.0 <= result < 7.0:
                    tk.Label(window, text=f"  {result:.2f} %  ", fg="green").grid(row=buttons[k]["row_number"], column=3)
                if 7.01 <= result < 15.0:
                    tk.Label(window, text=f"  {result:.2f} %  ", fg="orange").grid(row=buttons[k]["row_number"], column=3)
                if 15.01 <= result:
                    tk.Label(window, text=f"  {result:.2f} %  ", fg="red").grid(row=buttons[k]["row_number"], column=3)
                final_result['name'].append(str(buttons[k]['name']))
                final_result['last_price'].append(str(last_price))
                final_result['nav_price'].append(str(nav_price))
                final_result['bubble'].append(str(result))
            except Exception as e:
                tk.Label(window, text=f" "*20).grid(row=buttons[k]["row_number"], column=3)
                print(e)
                pass
    return final_result

def save_as_text():
    result = calculator()
    print(result)
    with open("test.txt", 'w', encoding='utf-8') as f:
        f.write(tabulate(result, headers = 'keys', tablefmt = 'psql'))

calc_infl_button = tk.Button(window, text="اجرا", command=lambda: calculator(), borderwidth=5, width=25, fg="red").grid(row=len(buttons)+1, column=0, columnspan=2)
save_as_text_button = tk.Button(window, text="ذخیره کردن اطلاعات", command=lambda: save_as_text(), borderwidth=5, width=15, fg="red").grid(row=len(buttons)+1, column=2)
exit_button = tk.Button(window, text="خروج", command=lambda: exit(), borderwidth=5, width=15, fg="red").grid(row=len(buttons)+1, column=3)