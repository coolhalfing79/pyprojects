from tkinter import *


root = Tk()

def myClick():
	myLabel = Label(root, text='why?')
	myLabel.pack()
# create a label widget
myButton = Button(root, text='don not click',
		padx=50, pady=50, command=myClick, fg='blue', bg='#000000')
myButton.pack()
root.mainloop()
