from tkinter import *
root = Tk()
theLabel = Label(root, text="US Healthcare Cost Calculator", bg='green')
paramLabel=Label(root, text="Select Option", bg='blue')

theLabel.pack(fill=X)
paramLabel.pack(side=LEFT, fill=Y)

topFrame = Frame(root)
bottomFrame = Frame(root)
topFrame.pack()
bottomFrame.pack(side=BOTTOM)

button1 = Button(bottomFrame, text='Calculate', fg="red", bg="black")
button1.pack(side = BOTTOM)
entry_1 = Entry(root)
entry_1.pack()


root.mainloop()