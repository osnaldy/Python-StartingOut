import Tkinter

class AverageExam():

    def __init__(self):

        self.main_window = Tkinter.Tk()

        self.frame_1 = Tkinter.Frame(self.main_window)
        self.frame_2 = Tkinter.Frame(self.main_window)
        self.frame_3 = Tkinter.Frame(self.main_window)
        self.frame_4 = Tkinter.Frame(self.main_window)
        self.frame_5 = Tkinter.Frame(self.main_window)

        self.label_1 = Tkinter.Label(self.frame_1,
                                     text = 'Enter the score for test #1:')
        self.entry_1 = Tkinter.Entry(self.frame_1,
                                     width = 10)

        self.label_1.pack(side = 'left')
        self.entry_1.pack(side = 'left')

        self.label_2 = Tkinter.Label(self.frame_2,
                                     text = 'Enter the score for test #2:')
        self.entry_2 = Tkinter.Entry(self.frame_2,
                                     width = 10)

        self.label_2.pack(side = 'left')
        self.entry_2.pack(side = 'left')

        self.label_3 = Tkinter.Label(self.frame_3,
                                     text = 'Enter the score for test #3:')
        self.entry_3 = Tkinter.Entry(self.frame_3,
                                     width = 10)

        self.label_3.pack(side = 'left')
        self.entry_3.pack(side = 'left')

        self.result_label = Tkinter.Label(self.frame_4,
                                          text = 'Average:')
        self.avg = Tkinter.StringVar()
        self.avg_label = Tkinter.Label(self.frame_4,
                                       textvariable = self.avg)
        self.result_label.pack(side = 'left')
        self.avg_label.pack(side = 'left')

        self.calc_button = Tkinter.Button(self.frame_5,
                                          text = 'Average',
                                          command = self.calc_avg)
        self.quit_button = Tkinter.Button(self.frame_5,
                                          text = 'Quit',
                                          command = self.main_window.destroy)

        self.calc_button.pack(side = 'left', padx = 10)
        self.quit_button.pack(side = 'left')

        self.frame_1.pack()
        self.frame_2.pack()
        self.frame_3.pack()
        self.frame_4.pack()
        self.frame_5.pack()

        Tkinter.mainloop()

    def calc_avg(self):

        self.test1 = float(self.entry_1.get())
        self.test2 = float(self.entry_2.get())
        self.test3 = float(self.entry_3.get())

        self.average = (self.test1 + self.test2 + self.test3) / 3
        self.avg.set(round(self.average))

gui = AverageExam()