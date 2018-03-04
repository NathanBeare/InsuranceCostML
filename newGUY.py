from Tkinter import *
from tkMessageBox import *
import subprocess as sp

def runCalc(diagnosis):
    results = sp.Popen(["python", "CalcCosts.py", diagnosis])
    # print results
# def callback():
#     if askyesno('Verify', 'Really quit?'):
#         showwarning('Yes', 'Not yet implemented')
#     else:
#         showinfo('No', 'Quit has been cancelled')
root = Tk()
leftFrame = Frame(root)
leftGrame.pack()
pulmButton = Button(leftFrame, text='Pulmonary Treatment', command=runCalc("0"))
cardsButton = Button(leftFrame,text='Cardiac Treatment', command=runCalc("1"))
neuroButton = Button(leftFrame,text='Neurological Treatment', command=runCalc("2"))
giButton = Button(leftFrame, text='GI Treatment', command=runCalc("3"))
renalButton = Button(leftFrame, text='Renal Treatment', command=runCalc("4"))
traumaButton = Button(leftFrame,text='Trauma Treatment', command=runCalc("5"))
orthoButton = Button(leftFrame,text='Orthopedic Treatment', command=runCalc("6"))
otherButton = Button(leftFrame,text='Other ', command=runCalc("7"))

pulmButton.pack(side=LEFT)
cardsButton.pack(side=LEFT)

# Button(text='Answer', command=answer).pack(fill=X)
mainloop()