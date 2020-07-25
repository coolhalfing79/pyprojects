from tkinter import *


root = Tk()

def myClick():
	myLabel = Label(root, text=e.get())
	myLabel.pack()
# create a label widget
e = Entry(root, width=50, bg='black', fg='white', borderwidth=50)
e.pack()
e.insert(0, 'enter your name:')

myButton = Button(root, text='don not click',
		padx=50, pady=50, command=myClick, fg='blue', bg='#000000')
myButton.pack()
root.mainloop()
