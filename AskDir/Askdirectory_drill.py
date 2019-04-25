####    DRILL
####    Create a GUI with a 'Browse' button and a text widget
####    When the button is clicked, it allows the user to select a directory from their PC
####    Script should then show the selected path in the text field
####    Use the askdirectory() method from tkinter
####    Link a function to the button widget

from tkinter import *
import tkinter as tk
from tkinter import filedialog

class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        self.master = master
        self.master.title("File Search")
        self.master.configure(bg="lightgray")

##      GUI Config
        self.btn1_browse = tk.Button(self.master, width=12, height=1, text='Browse...', command=lambda: fileDir(self))
        self.btn1_browse.grid(row=0, column=0, padx=(10,0), pady=(30,30), sticky=W)
        self.txt_dir = StringVar()
        self.txt_entry1 = tk.Entry(self.master, width=40, textvariable=self.txt_dir)
        self.txt_entry1.grid(row=0, column=1, padx=(15,10), pady=(30,30))

def fileDir(self):
    self.txt_dir.set(filedialog.askdirectory(title='Select a folder'))    

if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
