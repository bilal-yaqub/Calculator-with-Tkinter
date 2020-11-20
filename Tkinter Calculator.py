from tkinter import *

window = Tk()
window.title("Calculator")    

resultBox = Entry(window, width=50, borderwidth = 10)
resultBox.grid(row="0", columnspan=3)
resultBox.insert(0, "Answer")

window.mainloop()
