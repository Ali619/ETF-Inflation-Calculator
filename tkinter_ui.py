import tkinter as tk

window = tk.Tk()
window.title("حباب سنج")

start_label = tk.Label(window, text="قیمت پایانی").grid(row=0, column=1)
stop_label = tk.Label(window, text="ابطال NAV").grid(row=0, column=2)
result_infl_column = tk.Label(window, text="میزان حباب (%)").grid(row=0, column=3)

tala_label = tk.Label(window, text="طلا:")
tala_label.grid(row=1, column=0)
tala_entry_start = tk.Entry(window)
tala_entry_start.grid(row=1, column=1)
tala_entry_stop = tk.Entry(window)
tala_entry_stop.grid(row=1, column=2)

ayar_label = tk.Label(window, text="عیار:")
ayar_label.grid(row=2, column=0)
ayar_enrty_start = tk.Entry(window)
ayar_enrty_start.grid(row=2, column=1)
ayar_enrty_stop = tk.Entry(window)
ayar_enrty_stop.grid(row=2, column=2)

zar_label = tk.Label(window, text="زر:")
zar_label.grid(row=3, column=0)
zar_entry_start = tk.Entry(window)
zar_entry_start.grid(row=3, column=1)
zar_entry_stop = tk.Entry(window)
zar_entry_stop.grid(row=3, column=2)

mesghal_label = tk.Label(window, text="مثقال:")
mesghal_label.grid(row=4, column=0)
mesghal_entry_start = tk.Entry(window)
mesghal_entry_start.grid(row=4, column=1)
mesghal_entry_stop = tk.Entry(window)
mesghal_entry_stop.grid(row=4, column=2)

alton_label = tk.Label(window, text="آلتون:")
alton_label.grid(row=5, column=0)
alton_entry_start = tk.Entry(window)
alton_entry_start.grid(row=5, column=1)
alton_entry_stop = tk.Entry(window)
alton_entry_stop.grid(row=5, column=2)

javaher_label = tk.Label(window, text="جواهر:")
javaher_label.grid(row=6, column=0)
javaher_entry_start = tk.Entry(window)
javaher_entry_start.grid(row=6, column=1)
javaher_entry_stop = tk.Entry(window)
javaher_entry_stop.grid(row=6, column=2)

ganj_label = tk.Label(window, text="گنج:")
ganj_label.grid(row=7, column=0)
ganj_entry_start = tk.Entry(window)
ganj_entry_start.grid(row=7, column=1)
ganj_entry_stop = tk.Entry(window)
ganj_entry_stop.grid(row=7, column=2)

tabesh_label = tk.Label(window, text="تابش:")
tabesh_label.grid(row=8, column=0)
tabesh_entry_start = tk.Entry(window)
tabesh_entry_start.grid(row=8, column=1)
tabesh_entry_stop = tk.Entry(window)
tabesh_entry_stop.grid(row=8, column=2)

etfs = {
    "tala": {
        "row_number": 1,
        "etf_start": tala_entry_start,
        "etf_stop": tala_entry_stop,
        "etf_label": tala_label
    },

    "ayar": {
        "row_number": 2,
        "etf_start": ayar_enrty_start,
        "etf_stop": ayar_enrty_stop,
        "etf_label": ayar_label
    },

    "zar": {
        "row_number": 3,
        "etf_start": zar_entry_start,
        "etf_stop": zar_entry_stop,
        "etf_label": zar_label
    },

    "mesghal": {
        "row_number": 4,
        "etf_start": mesghal_entry_start,
        "etf_stop": mesghal_entry_stop,
        "etf_label": mesghal_label
    },

    "alton": {
        "row_number": 5,
        "etf_start": alton_entry_start,
        "etf_stop": alton_entry_stop,
        "etf_label": alton_label
    },

    "javaher": {
        "row_number": 6,
        "etf_start": javaher_entry_start,
        "etf_stop": javaher_entry_stop,
        "etf_label": javaher_label
    },

    "ganj": {
        "row_number": 7,
        "etf_start": ganj_entry_start,
        "etf_stop": ganj_entry_stop,
        "etf_label": ganj_label
    },

    "tabesh": {
        "row_number": 8,
        "etf_start": tabesh_entry_start,
        "etf_stop": tabesh_entry_stop,
        "etf_label": tabesh_label
    }
}
