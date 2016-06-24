import Tkinter

class GUI():

    def __init__(self):
        self.main_window = Tkinter.Tk()

        self.top_frame = Tkinter.Frame(self.main_window)
        self.bottom_frame = Tkinter.Frame(self.main_window)

        self.label1 = Tkinter.Label(self.top_frame, text = 'Dog')
        self.label2 = Tkinter.Label(self.top_frame, text = 'Cat')
        self.label3 = Tkinter.Label(self.top_frame, text = 'Cow')

        self.label1.pack(side = 'top')
        self.label2.pack(side = 'top')
        self.label3.pack(side = 'top')

        self.label4 = Tkinter.Label(self.bottom_frame, text = 'Sheep')
        self.label5 = Tkinter.Label(self.bottom_frame, text = 'Chicken')
        self.label6 = Tkinter.Label(self.bottom_frame, text = 'Rooster')

        self.label4.pack(side = 'left')
        self.label5.pack(side = 'left')
        self.label6.pack(side = 'left')

        self.top_frame.pack()
        self.bottom_frame.pack()

        Tkinter.mainloop()

my_Gui = GUI()