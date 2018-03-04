from tkinter import *
import subprocess as sp
from tkMessageBox import *
#changesss

class Window:
    def __init__(self, master):
        self.master = master
        master.title("US Healthcare Treatment Cost Calculator")
        master.geometry("800x450")
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

        self.pulmButton = Button(master, text='Pulmonary Treatment', command=self.runCalc("0"),highlightbackground='black' )
        self.pulmButton.grid(row=1, column=0, sticky=W)
        self.cardsButton = Button(master, text='Cardiac Treatment', command=self.runCalc("1"),highlightbackground='black')
        self.cardsButton.grid(row=2, column=0, sticky=W)
        self.neuroButton = Button(master, text='Neurological Treatment', command=self.runCalc("2"),highlightbackground='black')
        self.neuroButton.grid(row=3, column=0, sticky=W)
        self.giButton = Button(master, text='GI Treatment', command=self.runCalc("3"),highlightbackground='black')
        self.giButton.grid(row=4, column=0, sticky=W)
        self.renalButton = Button(master, text='Renal Treatment', command=self.runCalc("4"),highlightbackground='black')
        self.renalButton.grid(row=5, column=0, sticky=W)
        self.traumaButton = Button(master, text='Trauma Treatment', command=self.runCalc("5"),highlightbackground='black')
        self.traumaButton.grid(row=6, column=0, sticky=W)
        self.orthoButton = Button(master, text='Orthopedic Treatment', command=self.runCalc("6"),highlightbackground='black')
        self.orthoButton.grid(row=7, column=0, sticky=W)
        self.otherButton = Button(master, text='Other ', command=self.runCalc("7"),highlightbackground='black')
        self.otherButton.grid(row=88, column=0, sticky=W)

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
        self.close_button.grid(row=2, column=2, sticky=S + W)

    def change_color(self):
        self.input_color = self.text_input.get()
        self.master.config(background=self.input_color)
        self.label.config(background=self.input_color)
        self.text_input.config(bd='0')
        self.print_text.config(highlightbackground=self.input_color)
        self.draw_line_button.config(highlightbackground=self.input_color)
        self.close_button.config(highlightbackground=self.input_color)
        if (self.input_color == 'black'):
            self.label.config(fg='white')
        else:
            self.label.config(fg='black')

    def draw_line(self, line_x1, line_y1, line_x2, line_y2, line_width):
        self.x1 = line_x1
        self.y1 = line_y1
        self.x2 = line_x2
        self.y2 = line_y2
        self.width = line_width
        self.canvas.create_line(self.x1, self.y1, self.x2, self.y2, fill="black", width=self.width)

    def runCalc(self, diagnosis):
        results = sp.Popen(["python", "CalcCosts.py", diagnosis])


root = Tk()
Window_var = Window(root)
root.mainloop()