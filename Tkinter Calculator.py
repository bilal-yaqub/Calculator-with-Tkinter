from tkinter import *

window = Tk()
window.title("Calculator")    

resultBox = Entry(window, width=50, borderwidth = 10)
resultBox.grid(row="0", columnspan=4)

# List of buttons
# Tried setting padx = "150" to make it occupy 3 rows as colspa wast working
clearButton = Button(window, text = "Clear", padx=150, pady=50)
clearButton.grid(row=1, column=1,)

eqButton = Button(window, text = "=", padx=50, pady=50)
eqButton.grid(row=1, column=4)

Button9 = Button(window, text = "9", padx=50, pady=50)
Button9.grid(row=2, column=1)

Button8 = Button(window, text = "8", padx=50, pady=50)
Button8.grid(row=2, column=2)

Button7 = Button(window, text = "7", padx=50, pady=50)
Button7.grid(row=2, column=3)

plusButton = Button(window, text = "+", padx=50, pady=50)
plusButton.grid(row=2, column=4)

Button6 = Button(window, text = "6", padx=50, pady=50)
Button6.grid(row=3, column=1)

Button5 = Button(window, text = "5", padx=50, pady=50)
Button5.grid(row=3, column=2)

Button4 = Button(window, text = "4", padx=50, pady=50)
Button4.grid(row=3, column=3)

minusButton = Button(window, text = "-", padx=50, pady=50)
minusButton.grid(row=3, column=4)

Button3 = Button(window, text = "3", padx=50, pady=50)
Button3.grid(row=4, column=1)

Button2 = Button(window, text = "2", padx=50, pady=50)
Button2.grid(row=4, column=2)

Button1 = Button(window, text = "1", padx=50, pady=50)
Button1.grid(row=4, column=3)

multButton = Button(window, text = "x", padx=50, pady=50)
multButton.grid(row=4, column=4)

# Tried setting padx = "150" to make it occupy 3 rows as colspa wast working
Button0 = Button(window, text = "0", padx=150, pady=50)
Button0.grid(row=5, columnspan=3)

divButton = Button(window, text = "÷", padx=50, pady=50)
divButton.grid(row=5, column=4)


window.mainloop()
