from htmlparser import HtmlParser
import tkinter as tk
parser = HtmlParser("https://bank.gov.ua/")
parser.NbuParse('div', 'index-page')
kurs = parser.Result['3']
hrn = 0
res = 0
def convert():
    hrn = float(s_entry.get())
    result = hrn / kurs
    res = f'{result:.2f}'
    text = tk.Label(root, text=f'{hrn} грн = {res} $', font=('Times New Roman', 14))
    text.grid(column=0, row=3)
root = tk.Tk()
root.title("Currency converter")
root.geometry("600x300+500+400")
root.resizable(False, False)
sign_label = tk.Label(root, text="Введіть суму (грн): ", font=("Arial", 14), padx=50)
sign_label.grid(column=0, row=1, sticky="w")
s_entry = tk.Entry(root, font=("Arial", 12), width=20)
s_entry.grid(column=1, row=1, sticky="w")
signup_button = tk.Button(root, text="OK", font=("Arial", 10), width=6, command=convert)
signup_button.grid(column=3, row=1)
root.mainloop()