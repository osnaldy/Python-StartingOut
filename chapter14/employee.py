import Tkinter
import pickle

class Employees():

    FILE = open('Employee.dat', 'a')

    def __init__(self):

        self.main_window = Tkinter.Tk()

        self.employee_label = Tkinter.Label(self.main_window, text = "Employee's Name:")
        self.employee_label.grid(row = 0)

        self.employee_entry = Tkinter.Entry(self.main_window)
        self.employee_entry.grid(row = 0, column = 3)

        self.id_number_label = Tkinter.Label(self.main_window, text = "Employee's ID_Number:")
        self.id_number_label.grid(row = 1)

        self.id_number_entry = Tkinter.Entry(self.main_window)
        self.id_number_entry.grid(row =1 , column = 3)

        self.department_label = Tkinter.Label(self.main_window, text = "Employee's Department:")
        self.department_label.grid(row =2)

        self.department_entry = Tkinter.Entry(self.main_window)
        self.department_entry.grid(row =2 , column = 3)

        self.job_title_label = Tkinter.Label(self.main_window, text = "Employee's Job Title:")
        self.job_title_label.grid(row =3)

        self.job_title_entry = Tkinter.Entry(self.main_window)
        self.job_title_entry.grid(row =3 , column = 3)

        self.enter_button = Tkinter.Button(self.main_window, text = 'Enter Information',
                                           command = self.add_employee)
        self.enter_button.grid(row = 5)

        self.exit_button = Tkinter.Button(self.main_window, text = 'Exit Program',
                                          command = self.main_window.destroy)
        self.exit_button.grid(row = 5, column = 3)

        self.look_button = Tkinter.Button(self.main_window, text = "Look Up Employee",
                                          command = self.look_up)
        self.look_button.grid(row = 7, column = 2)

        self.employee = {}

        Tkinter.mainloop()

    def add_employee(self):

        self.employee["Name"] = self.employee_entry.get()
        self.employee["ID_Number"] = self.id_number_entry.get()
        self.employee["Department"] = self.department_entry.get()
        self.employee["Job_Title"] = self.job_title_entry.get()

        pickle.dump(self.employee, self.FILE)

        self.employee_entry.delete(0, "end")
        self.id_number_entry.delete(0, "end")
        self.department_entry.delete(0, "end")
        self.job_title_entry.delete(0, "end")

    def look_up(self):

        self.new_window = Tkinter.Tk()

        self.label_1 = Tkinter.Button(self.new_window, text = 'Employee Name')
        self.label_1.grid(row = 0)

        Tkinter.mainloop()

gui = Employees()