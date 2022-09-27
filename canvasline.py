# Import the required libraries
from tkinter import *

# Create an instance of tkinter frame or window
win = Tk()

# Set the size of the tkinter window
# win.geometry("700x350")

# Create a canvas widget
canvas = Canvas(win, width=700, height=300)
canvas.pack()

x = 100
width = 400
# Add a line in canvas widget
canvas.create_line(x, 200, x + width, 200, fill="green", width=30)
test_text = "테스트 문자열 입니다."
text_len = len(test_text)
text_size = 20
text_width = text_len * text_size
canvas.create_text(x + text_width / 2, 200, text=test_text, font=("나눔고딕코딩", text_size), fill="blue")

win.mainloop()
