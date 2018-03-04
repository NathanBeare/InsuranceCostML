from Tkinter import *
import subprocess as sp
import time
# from tkMessageBox import *
from functools import partial
from PIL import Image, ImageTk
#changesss

class Window:
    def __init__(self, master):

        self.master = master
        master.title("US Healthcare Treatment Cost Calculator")
        master.geometry("700x700")
        master.resizable(0, 0)
        master.config(background='black')

        master.columnconfigure(0, pad=3)
        master.columnconfigure(1, pad=3)
        master.columnconfigure(2, pad=3)

        master.rowconfigure(0, pad=3)
        master.rowconfigure(1, pad=3)
        master.rowconfigure(2, pad=3)

        # self.canvas = Canvas(master, width=400, height=200)
        # self.canvas.grid(row=1, column=2, sticky=E)

        self.label = Label(master, text="Pick a type of treatment:", background='black', fg='white')
        self.label.grid(row=0, column=0, sticky=W)

        # self.text_input = Entry(master, bd='0')
        # self.text_input.grid(row=0, column=1, sticky=W)

        # self.print_text = Button(master, text="Change Background Color", command=self.change_color,
        #                          highlightbackground='black')
        action_with_arg = partial((self.runCalc), 0, master)
        self.pulmButton = Button(master, text='Pulmonary Treatment', command=action_with_arg ,highlightbackground='black' )
        self.pulmButton.grid(row=1, column=0, sticky=W)

        action_with_arg = partial((self.runCalc), 1, master)
        self.cardsButton = Button(master, text='Cardiac Treatment', command=action_with_arg,highlightbackground='black')
        # self.cardsButton.grid(row=2, column=0, sticky=W)

        action_with_arg = partial((self.runCalc), 2, master)
        self.neuroButton = Button(master, text='Neurological Treatment', command=action_with_arg,highlightbackground='black')
        self.neuroButton.grid(row=3, column=0, sticky=W)

        action_with_arg = partial((self.runCalc), 3, master)
        self.giButton = Button(master, text='GI Treatment', command=action_with_arg,highlightbackground='black')
        self.giButton.grid(row=4, column=0, sticky=W)

        action_with_arg = partial((self.runCalc), 4, master)
        self.renalButton = Button(master, text='Renal Treatment', command=action_with_arg,highlightbackground='black')
        self.renalButton.grid(row=5, column=0, sticky=W)

        action_with_arg = partial((self.runCalc), 5, master)
        self.traumaButton = Button(master, text='Trauma Treatment', command =action_with_arg,highlightbackground='black')
        self.traumaButton.grid(row=6, column=0, sticky=W)

        action_with_arg = partial((self.runCalc), 6, master)
        self.orthoButton = Button(master, text='Orthopedic Treatment', command=action_with_arg,highlightbackground='black')
        self.orthoButton.grid(row=7, column=0, sticky=W)

        action_with_arg = partial((self.runCalc), 7, master)
        self.otherButton = Button(master, text='Other ', command=action_with_arg,highlightbackground='black')
        self.otherButton.grid(row=8, column=0, sticky=W)

        # self.print_text.grid(row=0, column=2, sticky=W)

        # self.x1_i = Entry(master, bd='0')
        # self.text_input.grid(row=1, column=0, padx=3, sticky=W)

        # self.y1_i = Entry(master, bd='0')
        # self.text_input.grid(row=1, column=0, padx=3, sticky=W)

        # self.draw_line_button = Button(master, text="Draw Line",
        #                                command=self.draw_line(self.x1_i, self.y1_i, 20, 30, 4),
        #                                highlightbackground='black')
        # self.draw_line_button.grid(row=1, column=0, padx=3, sticky=W)

        self.close_button = Button(master, text="Close", command=master.quit, highlightbackground='black')
        self.close_button.grid(row=30, column=2, sticky=S + W)

    def runCalc(self, diagnosis, master):
        # diagnosis = diagnosis
        sp.Popen(["python", "CalcCosts.py", str(diagnosis)])
        print "RESULTS OUTPUTTED TO CALC_OUTPUTS.txt"
        time.sleep(3)

        string1=""
        with open("calc_outputs.txt", "r") as fh:
            for line in fh:
                    results = line.split(',')
                    string1 = "National Cost : " + str(results[0])
                    string1 += "\nCheapest Cost Found in " + str(results[3]) + ": " + str(results[1])
                    string1 +=  "\nTotal Range in Disparity: " + str(results[1] + " - " + str(results[2]))
                    msg = Message(master, text=string1)
                    msg.config(bg='lightgreen', font =('times', 14))
                    msg.grid(row=10, column=2)
                    msg2= Message(master, text="Box Plot Saved as barChartResults.png in directory")
                    msg2.config(bg='lightgreen', font=('times', 14))
                    msg2.grid(row=10, column=20)
                    time.sleep(4)
                    # image = Image.open('barChartResults.png')
                    # display = ImageTk.PhotoImage(image)

                    # labelchart = Label(root, image=display)
                    # labelchart.grid(rows=0, column=0)



root = Tk()
Window_var = Window(root)



root.mainloop()