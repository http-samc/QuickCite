from citer import cite
from tkinter import *

class gui:
    """
    GUI for Citer
    """

    def __init__(self):

        #Creating Main Window
        self.win = Tk()
        self.win.title("Citer - by Samarth Chitgopekar")

        #Adding URL Label
        self.url_label = Label(self.win, font=("Times 12"), text="URL: ")
        self.url_label.grid(row=0, column=0)

        #Adding URL Entry 
        self.url_input = Entry(self.win, font=("Times 12"))
        self.url_input.grid(row=0, column=1)

        #Adding Start Button
        self.start = Button(self.win,text='Start', command = self.start,width=30, font=("Times 12"),)
        self.start.grid(row=1,column=0, columnspan=2)

        #Starting GUI
        self.win.mainloop()
    
    def start(self):
        
        #Creating citation
        citation = cite(self.url_input.get())

        #Creating citation popout window
        self.popout = Toplevel(self.win)
        self.popout.title("Citation")

        #Creating Entry (for easy copying of citation)
        self.citation = Text(self.popout, font=("Times 12"), width=107)

        #Inserting MLA citation
        self.citation.insert("1.0", citation.mla())
        
        #Putting citation on grid
        self.citation.grid(row=0,column=0)

gui()