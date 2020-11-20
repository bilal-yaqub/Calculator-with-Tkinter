from tkinter import *

window = Tk()
window.title("Calculator")    

resultBox = Entry(window, width=50, borderwidth = 10)
resultBox.grid(row="0", columnspan=4)

clearButton = Button(window, text = "Clear")
clearButton.grid(row=1, column=1, columnspan=3)

eqButton = Button(window, text = "=")
eqButton.grid(row=1, column=4)

Button9 = Button(window, text = "9")
Button9.grid(row=2, column=1)

Button8 = Button(window, text = "8")
Button8.grid(row=2, column=2)

Button7 = Button(window, text = "7")
Button7.grid(row=2, column=3)

plusButton = Button(window, text = "+")
plusButton.grid(row=2, column=4)

Button6 = Button(window, text = "6")
Button6.grid(row=3, column=1)

Button5 = Button(window, text = "5")
Button5.grid(row=3, column=2)

Button4 = Button(window, text = "4")
Button4.grid(row=3, column=2)

minusButton = Button(window, text = "-")
minusButton.grid(row=3, column=4)

Button3 = Button(window, text = "3")
Button3.grid(row=4, column=1)

Button2 = Button(window, text = "2")
Button2.grid(row=4, column=2)

Button1 = Button(window, text = "1")
Button1.grid(row=4, column=3)

multButton = Button(window, text = "x")
multButton.grid(row=4, column=4)

Button0 = Button(window, text = "0")
Button0.grid(row=5, columnspan=3)

divButton = Button(window, text = "÷")
divButton.grid(row=5, column=4)
window.mainloop()
