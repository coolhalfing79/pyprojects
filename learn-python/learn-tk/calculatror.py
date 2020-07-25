from tkinter import *


root = Tk()
root.title('calculator')

# create a label widget
e = Entry(root, width=35, borderwidth=5)
e.grid(row=0, column=0, columnspan=3)

def button_add():
	pass

def button_click():
	pass

# define buttons
button1 = Button(root, text='1', padx=40, pady=40, command=lambda: button_click(1))
button2 = Button(root, text='2', padx=40, pady=40, command=lambda: button_click(2))
button3 = Button(root, text='3', padx=40, pady=40, command=lambda: button_click(3))
button4 = Button(root, text='4', padx=40, pady=40, command=lambda: button_click(4))
button5 = Button(root, text='5', padx=40, pady=40, command=lambda: button_click(5))
button6 = Button(root, text='6', padx=40, pady=40, command=lambda: button_click(6))
button7 = Button(root, text='7', padx=40, pady=40, command=lambda: button_click(7))
button8 = Button(root, text='8', padx=40, pady=40, command=lambda: button_click(8))
button9 = Button(root, text='9', padx=40, pady=40, command=lambda: button_click(9))
button0 = Button(root, text='0', padx=40, pady=40, command=lambda: button_click(0))

button_add = Button(root, text='+', padx=39, pady=40, command=lambda: button_click())
button_eqs = Button(root, text='=', padx=39, pady=91, command=lambda: button_click())
button_cls = Button(root, text='cls', padx=85, pady=40, command=lambda: button_click())

# put button on screen
button1.grid(row=3, column=0)
button2.grid(row=3, column=1)
button3.grid(row=3, column=2)

button4.grid(row=2, column=0)
button5.grid(row=2, column=1)
button6.grid(row=2, column=2)

button7.grid(row=1, column=0)
button8.grid(row=1, column=1)
button9.grid(row=1, column=2)

button0.grid(row=4, column=0)

button_add.grid(row=4, column=1)
button_cls.grid(row=5, column=0, columnspan=2)
button_eqs.grid(row=4, column=2, rowspan=2)

root.mainloop()
