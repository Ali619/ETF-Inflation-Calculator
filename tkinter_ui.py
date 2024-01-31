import tkinter as tk

class Create_Label():
    def __init__(self, window, text, row, column):
        self.text = text
        self.window = window
        self.row = row
        self.column = column
        self.label = tk.Label(self.window, text=self.text)
        self.label.grid(row=self.row, column=self.column)

class Create_Entry():
    def __init__(self, fa_name: str, en_name: str, window: tk.Tk):
        self.fa_name = fa_name
        self.en_name = en_name
        self.window = window
        self.entry = tk.Entry(self.window)
    
window = tk.Tk()
label = Create_Label(window=window, text="label", row=0, column=0)
window.mainloop()