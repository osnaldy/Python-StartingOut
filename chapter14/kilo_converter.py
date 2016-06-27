import Tkinter
import tkMessageBox

class Kilo_Converter():

    def __init__(self):

        self.main_window = Tkinter.Tk()
        self.top_frame = Tkinter.Frame(self.main_window)
        self.bottom_frame = Tkinter.Frame(self.main_window)

        self.my_label = Tkinter.Label(self.top_frame,
                                      text = 'Enter a distance in kilometers:')
        self.kilo_entry = Tkinter.Entry(self.top_frame,
                                        width = 10)
        self.my_label.pack(side = 'left')
        self.kilo_entry.pack(side = 'left')

        self.convert_button = Tkinter.Button(self.bottom_frame,
                                             text = 'Convert',
                                             command = self.converts)
        self.quit_button = Tkinter.Button(self.bottom_frame,
                                          text = 'Quit',
                                          command = self.main_window.destroy)
        self.convert_button.pack(side = 'left', padx = 5)
        self.quit_button.pack(side = 'left')

        self.top_frame.pack()
        self.bottom_frame.pack()
        Tkinter.mainloop()

    def converts(self):

        kilo = float(self.kilo_entry.get())

        miles = kilo * 0.6214

        tkMessageBox.showinfo('Results',
                              str(kilo) + ' Kilometers is equals to ' +
                              str(miles) + ' Miles')
convert = Kilo_Converter()