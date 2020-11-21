from tkinter import *

window = Tk()
window.title("Calculator")  

def clickButton(number):
	return


# Created a entry box to output the result of the calculatioon 
resultBox = Entry(window, width=50, borderwidth = 6)
resultBox.grid(row=0, column=0, padx = 60, columnspan=4)

# List of Buttons in order
clearButton = Button(window, text = "Clear", padx=160, pady=15, command = lambda: clickButton(2))			# Set padding to 160 to over 3 columns
eqButton = Button(window, text = "=", padx=50, pady=15, command = lambda : clickButton())

Button9 = Button(window, text = "9", padx=50, pady=15, command = lambda: clickButton(9))
Button8 = Button(window, text = "8", padx=50, pady=15, command = lambda: clickButton(8))
Button7 = Button(window, text = "7", padx=50, pady=15, command = lambda: clickButton(7))
plusButton = Button(window, text = "+", padx=50, pady=15, command = lambda: clickButton())

Button6 = Button(window, text = "6", padx=50, pady=15, command = lambda: clickButton(6))
Button5 = Button(window, text = "5", padx=50, pady=15, command = lambda: clickButton(5))
Button4 = Button(window, text = "4", padx=50, pady=15, command = lambda: clickButton(4))
minusButton = Button(window, text = "-", padx=50, pady=15, command = lambda: clickButton())

Button3 = Button(window, text = "3", padx=50, pady=15, command = lambda: clickButton(3))
Button2 = Button(window, text = "2", padx=50, pady=15, command = lambda: clickButton(2))
Button1 = Button(window, text = "1", padx=50, pady=15, command = lambda: clickButton(1))
multButton = Button(window, text = "x", padx=50, pady=15, command = lambda: clickButton())

Button0 = Button(window, text = "0", padx=170, pady=15, command = lambda: clickButton(0))				# Set padding to 170 to over 3 columns greater than "Clear" as that was a word
divButton = Button(window, text = "÷", padx=50, pady=15, command = lambda: clickButton())

# Lists of Grids
clearButton.grid(row=1, column=0, columnspan=3)			# Set columnspan to 3 to cover 3 rows and make it allign
eqButton.grid(row=1, column=3)

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

Button0.grid(row=5,column=0, columnspan=3)			# Set columnspan to 3 to cover 3 rows and make it allign
divButton.grid(row=5, column=3)

window.mainloop()
