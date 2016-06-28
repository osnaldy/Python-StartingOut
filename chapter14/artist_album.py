import Tkinter

class Artist():

    #GUI
    def __init__(self):

        self.main_window = Tkinter.Tk()
        self.main_window.title('Artists and Albums')

        self.output_label = Tkinter.Label(self.main_window, text = 'Ready')
        self.output_label.pack()

        self.entry_box = Tkinter.Entry(self.main_window)
        self.entry_box.pack()

        self.list_box = Tkinter.Listbox(self.main_window)
        self.list_box.pack()

        self.show_all = Tkinter.Button(self.main_window, text = 'Show All', command = self.Show_all)
        self.show_all.pack()

        self.show_one = Tkinter.Button(self.main_window, text = 'Show One', command = self.Show_one)
        self.show_one.pack()

        self.add_one = Tkinter.Button(self.main_window, text = 'Add One', command = self.Add_one)
        self.add_one.pack()

        #Dictionary
        self.albums = {}

        self.albums["Romeo Santos"] = "Formula Vol. 1"
        self.albums["Ricardo Arjona"] = "Cuando Se Apaga la Luz"
        self.albums["Alexander Pires"] = "Cuando Acaba el Placer"

        Tkinter.mainloop()

    #Functions
    def Show_all(self):

        self.list_box.delete(0, "end")

        for self.artist in self.albums:
            self.list_box.insert("end", self.artist)

    def Show_one(self):

        self.artist = self.list_box.get('active')
        self.album = self.albums[self.artist]
        self.msg = self.artist + ' : ' + self.album
        self.output_label['text'] = self.msg

    def Add_one(self):

        self.info = self.entry_box.get()
        self.split_info = self.info.split(',')
        self.artist = self.split_info[0]
        self.album = self.split_info[1]
        self.albums[self.artist] = self.album
        self.Show_all()
        self.entry_box.delete(0, "end")

gui = Artist()