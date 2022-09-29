from ttkwidgets import ScrolledListbox
import tkinter as tk

# goto particular line https://stackoverflow.com/questions/64892716/is-it-possible-with-listbox-on-start-go-to-a-particular-line

window = tk.Tk()
listbox = ScrolledListbox(window, height=5)

for i in range(999999):
    listbox.listbox.insert('end', 'item {} has mnay lasdfklinabjsdfgoh'.format(i))

listbox.pack(fill='both', expand=True)
window.mainloop()