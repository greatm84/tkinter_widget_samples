# https://pythonguides.com/python-tkinter-scrollbar/

from tkinter import *

ws = Tk()
ws.title('PythonGuides')
ws.config(bg='#5F734C')

frame = Frame(
    ws,
    bg='#A8B9BF'
    )

text_box = Text(
    ws,
    height=13,
    width=32,
    font=(12)
)

text_box.grid(row=0, column=0)
text_box.config(bg='#D9D8D7')

sb = Scrollbar(
    ws,
    orient=VERTICAL
    )

sb.grid(row=0, column=1, sticky=NS)

text_box.config(yscrollcommand=sb.set)
sb.config(command=text_box.yview)


ws.mainloop()