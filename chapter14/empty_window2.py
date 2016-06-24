import Tkinter

class GUI():

    def __init__(self):
        self.main_window = Tkinter.Tk()

        self.label = Tkinter.Label(self.main_window, text='Hello People')
        self.label.pack()
        Tkinter.mainloop()

my_Gui = GUI()

