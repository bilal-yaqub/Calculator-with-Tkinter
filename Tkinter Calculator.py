from tkinter import *

window = Tk()
window.title("Calculator")    

resultBox = Entry(window, width=50, borderwidth = 10)
resultBox.grid(row=0, column=0, padx = 20, pady = 10, columnspan=4)

# List of Buttons
# Set padding to 140 to over 3 rows
clearButton = Button(window, text = "Clear", padx=140, pady=15)
eqButton = Button(window, text = "=", padx=40, pady=15)
Button9 = Button(window, text = "9", padx=40, pady=15)
Button8 = Button(window, text = "8", padx=40, pady=15)
Button7 = Button(window, text = "7", padx=40, pady=15)
plusButton = Button(window, text = "+", padx=40, pady=15)
Button6 = Button(window, text = "6", padx=40, pady=15)
Button5 = Button(window, text = "5", padx=40, pady=15)
Button4 = Button(window, text = "4", padx=40, pady=15)
minusButton = Button(window, text = "-", padx=40, pady=15)
Button3 = Button(window, text = "3", padx=40, pady=15)
Button2 = Button(window, text = "2", padx=40, pady=15)
Button1 = Button(window, text = "1", padx=40, pady=15)
multButton = Button(window, text = "x", padx=40, pady=15)
# Set padding to 140 to over 3 rows
Button0 = Button(window, text = "0", padx=140, pady=15)
divButton = Button(window, text = "÷", padx=50, pady=15)

# Lists of Grids
# Set columnspan to 3 to cover 3 rows and make it allign
clearButton.grid(row=1, column=0, columnspan=3, sticky = NE)
eqButton.grid(row=1, column=4)
Button9.grid(row=2, column=0)
Button8.grid(row=2, column=1)
Button7.grid(row=2, column=2)
plusButton.grid(row=2, column=3)
Button6.grid(row=3, column=0)
Button5.grid(row=3, column=1)
Button4.grid(row=3, column=2)
minusButton.grid(row=3, column=3)
Button3.grid(row=4, column=0)
Button2.grid(row=4, column=1)
Button1.grid(row=4, column=2)
multButton.grid(row=4, column=3)
# Set columnspan to 3 to cover 3 rows and make it allign
Button0.grid(row=5,column=0, columnspan=3, sticky = NE)
divButton.grid(row=5, column=4)

window.mainloop()
