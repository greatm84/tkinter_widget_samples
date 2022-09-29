from ttkwidgets import ScrolledListbox
import tkinter as tk

# goto particular line https://stackoverflow.com/questions/64892716/is-it-possible-with-listbox-on-start-go-to-a-particular-line

window = tk.Tk()
listbox = ScrolledListbox(window, height=5)

app_log_path = './temp/applog.txt'

with open(app_log_path, 'r', encoding="UTF-8") as f:
    i = 0
    for line in f:
        listbox.listbox.insert('end', '{} : {}'.format(i, line))
        i = i + 1

listbox.pack(fill='both', expand=True)
window.mainloop()
