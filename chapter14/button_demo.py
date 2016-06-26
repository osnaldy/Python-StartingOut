import Tkinter
import tkMessageBox

class GUI():

    def __init__(self):
        self.main_window = Tkinter.Tk()

        self.my_button = Tkinter.Button(self.main_window,
                                        text = 'Click Me!',
                                        command = self.do_something)

        self.my_button.pack()

        Tkinter.mainloop()

    def do_something(self):

        tkMessageBox.showinfo('Response', 'Thanks for clicking')

my_Gui = GUI()