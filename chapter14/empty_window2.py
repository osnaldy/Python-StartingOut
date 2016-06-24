import Tkinter

class GUI():

    def __init__(self):
        self.main_window = Tkinter.Tk()

        self.label1 = Tkinter.Label(self.main_window, text='Hello People!!')
        self.label2 = Tkinter.Label(self.main_window, text= 'This is GUI')
        self.label1.pack(side= 'left')
        self.label2.pack(side = 'left')
        Tkinter.mainloop()

my_Gui = GUI()

