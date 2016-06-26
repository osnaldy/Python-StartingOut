import Tkinter
import tkMessageBox

class GUI():

    def __init__(self):

        self.main_window = Tkinter.Tk()
        self.my_button = Tkinter.Button(self.main_window,
                                        text = 'Click Me!',
                                        command = self.do_something)
        self.quit_button = Tkinter.Button(self.main_window,
                                          text = 'Quit',
                                          command = self.main_window.destroy)
        self.my_button.pack()
        self.quit_button.pack()

        Tkinter.mainloop()

    def do_something(self):
        tkMessageBox.showinfo('Response', 'Thanks For Clicking')

my_gui = GUI()