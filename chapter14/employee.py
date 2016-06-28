import Tkinter
import pickle

class Employees():

    def __init__(self):
        self.main_window = Tkinter.Tk()

        self.main_window.title('Employees')
        #Employee Frame
        self.employee_frame = Tkinter.Frame(self.main_window, pady = 20)
        #Id_Number Frame
        self.id_number_frame = Tkinter.Frame(self.main_window, pady = 20)
        #Employee's Department Frame
        self.department_frame = Tkinter.Frame(self.main_window, pady = 20)
        #Employee's Job title Frame
        self.job_title_frame = Tkinter.Frame(self.main_window, pady = 20)
        #Buttons Frame
        self.button_frame = Tkinter.Frame(self.main_window, pady = 20)

        self.employee_label = Tkinter.Label(self.employee_frame, text = "Employee's Name:")
        self.employee_label.pack(side = 'left')

        self.employee_entry = Tkinter.Entry(self.employee_frame, width = 20)
        self.employee_entry.pack(side = 'right')

        self.id_number_label = Tkinter.Label(self.id_number_frame, text = "Employee's ID_Number:")
        self.id_number_label.pack(side = 'left')

        self.id_number_entry = Tkinter.Entry(self.id_number_frame, width = 20)
        self.id_number_entry.pack(side = 'right')

        self.department_label = Tkinter.Label(self.department_frame, text = "Employee's Department:")
        self.department_label.pack(side = 'left')

        self.department_entry = Tkinter.Entry(self.department_frame, width = 20)
        self.department_entry.pack(side = 'left')

        self.job_title_label = Tkinter.Label(self.job_title_frame, text = "Employee's Job Title:")
        self.job_title_label.pack(side = 'left')

        self.job_title_entry = Tkinter.Entry(self.job_title_frame, width = 20)
        self.job_title_entry.pack(side = 'left')

        self.enter_button = Tkinter.Button(self.button_frame, text = 'Enter Information')
        self.enter_button.pack(side = 'left', padx = 20)

        self.exit_button = Tkinter.Button(self.button_frame, text = 'Exit Program',
                                          command = self.main_window.destroy)
        self.exit_button.pack(side = 'left')

        self.employee_frame.pack()
        self.id_number_frame.pack()
        self.department_frame.pack()
        self.job_title_frame.pack()
        self.button_frame.pack()
        Tkinter.mainloop()

gui = Employees()