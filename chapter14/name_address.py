import Tkinter

class ShowAddress():

    def __init__(self):

        self.main_window = Tkinter.Tk()

        self.top_frame = Tkinter.Frame(self.main_window)
        self.bottom_frame = Tkinter.Frame(self.main_window)

        self.hold_label = Tkinter.StringVar()
        self.my_label = Tkinter.Label(self.top_frame,
                                      textvariable = self.hold_label)

        self.my_label.pack(side = 'top')

        self.showinfo_button = Tkinter.Button(self.bottom_frame,
                                              text = 'Show Info',
                                              command = self.shows)
        self.quit_button = Tkinter.Button(self.bottom_frame,
                                          text = 'Quit',
                                          command = self.main_window.destroy)
        self.showinfo_button.pack(side = 'left', padx = 10)
        self.quit_button.pack(side = 'left')

        self.top_frame.pack()
        self.bottom_frame.pack()

        Tkinter.mainloop()

    def shows(self):

        self.name = str('Neo Prez \n 21 West Broadway \n New York, NY 1022')

        self.hold_label.set(self.name)

my_gui = ShowAddress()
