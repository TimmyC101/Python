####    DRILL
####    Create a GUI called "Check files" with the following:
####    Browse Button followed by an input field with a fair amount of upper padding
####    Browse Button followed by an input field
####    "Check for files" button (SW pos) and a "Close Program" button on the same row with SE pos

from tkinter import *
import tkinter as tk

class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        self.master = master
##      Placeholder if we want to modify window
##      self.master.minsize(x,y)
##      self.master.maxsize(x,y)
        self.master.title("Check files")
        self.master.configure(bg="lightgray")

##      GUI Config
        self.btn1_browse = tk.Button(self.master, width=12, height=1, text='Browse...')
        self.btn1_browse.grid(row=0, column=0, padx=(10,0), pady=(30,0), sticky=W)
        self.btn2_browse = tk.Button(self.master, width=12, height=1, text='Browse...')
        self.btn2_browse.grid(row=1, column=0, padx=(10,0), pady=(5,0), sticky=W)
        self.btn3_check = tk.Button(self.master, width=12, height=2, text='Check for Files...')
        self.btn3_check.grid(row=2, column=0, padx=(10,0), pady=(5,10), sticky=W)
        self.btn4_close = tk.Button(self.master, width=12, height=2, text='Close Program')
        self.btn4_close.grid(row=2, column=1, padx=(0,10), pady=(5,10), sticky=E)

        self.txt_entry1 = tk.Entry(self.master, width=40, text='')
        self.txt_entry1.grid(row=0, column=1, padx=(15,10), pady=(30,0), sticky=N)
        self.txt_entry2 = tk.Entry(self.master, width=40, text='')
        self.txt_entry2.grid(row=1, column=1, padx=(15,10), pady=(5,0), sticky=N)
        
if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
