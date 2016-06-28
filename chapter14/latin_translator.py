import Tkinter

class EnglishTranslator():

    def __init__(self):

        self.main_window = Tkinter.Tk()

        self.top_frame = Tkinter.Frame(self.main_window)
        self.middle_frame = Tkinter.Frame(self.main_window)
        self.bottom_frame = Tkinter.Frame(self.main_window)

        self.label1 = Tkinter.Label(self.top_frame,
                                    text = 'Sinister', padx = 10)
        self.button1 = Tkinter.Button(self.top_frame,
                                      text = 'Translate', padx = 10,
                                      command = self.translate1)

        self.result1 = Tkinter.StringVar()
        self.label11 = Tkinter.Label(self.top_frame, padx = 10, fg = 'blue',
                                     textvariable = self.result1)

        self.label1.pack(side = 'left')
        self.button1.pack(side = 'left')
        self.label11.pack(side = 'left')

        self.label2 = Tkinter.Label(self.middle_frame,
                                    text = 'dexter', padx = 10)
        self.button2 = Tkinter.Button(self.middle_frame,
                                      text = 'Translate', padx = 10,
                                      command = self.translate2)

        self.result2 = Tkinter.StringVar()
        self.label22 = Tkinter.Label(self.middle_frame, padx = 10, fg = 'red',
                                     textvariable = self.result2)

        self.label2.pack(side = 'left')
        self.button2.pack(side = 'left')
        self.label22.pack(side = 'left')

        self.label3 = Tkinter.Label(self.bottom_frame,
                                    text = 'medium', padx = 10)
        self.button3 = Tkinter.Button(self.bottom_frame,
                                      text = 'Translate', padx = 10,
                                      command = self.translate3)

        self.result3 = Tkinter.StringVar()
        self.label33 = Tkinter.Label(self.bottom_frame, padx = 10, fg = 'green',
                                     textvariable = self.result3)

        self.label3.pack(side = 'left')
        self.button3.pack(side = 'left')
        self.label33.pack(side = 'left')

        self.top_frame.pack()
        self.middle_frame.pack()
        self.bottom_frame.pack()

        Tkinter.mainloop()

    def translate1(self):

        self.translation = str('left')

        self.result1.set(self.translation)

    def translate2(self):

        self.translation = str('right')

        self.result2.set(self.translation)

    def translate3(self):

        self.translation = str('center')

        self.result3.set(self.translation)

my_gui = EnglishTranslator()