from tkinter import *

tk = Tk()

canvas = Canvas(tk, width = 400, height = 400)

canvas.pack()

canvas.create_text(150, 100, text = "테스트 문자열 입니다.", font = ("나눔고딕코딩", 20), fill = "blue")

tk.mainloop()