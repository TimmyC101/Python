####    DRILL
####    Create a GUI with 2 'Browse' buttons and a 2 text widgets
####    The 1st button selects a source directory
####    The 2nd button selects the destination directory
####    There also needs to be a button to execute a function that iterates thru the source
####        and pastes all ".txt" files from that source into the destination directory
####    Lastly, the script should record the file names that were moved and their
####        corresponding modified timestamps into a database and print out those text files
####        and modified time stamps to the console.
####    Use the following: listdir(), path.join(), getmtime(), shutil.move()
        

from tkinter import *
import tkinter as tk
from tkinter import filedialog
import os
import shutil
import sqlite3
import time

class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        self.master = master
        self.master.title("File Search")
        self.master.configure(bg="lightgray")

##      GUI Config
        #Create Buttons
        self.sourceButton = tk.Button(self.master, width=20, height=1, text='Select Source Folder', \
                                     command=lambda: fileSource(self))
        self.sourceButton.grid(row=0, column=0, padx=(20,0), pady=(30,30), sticky=W)
        self.destinationButton = tk.Button(self.master, width=20, height=1, text='Select Destination Folder', \
                                     command=lambda: fileDestination(self))
        self.destinationButton.grid(row=1, column=0, padx=(20,0), pady=(0,30), sticky=W)
        self.executeButton = tk.Button(self.master, width=20, height=1, text="Execute '.txt' File Transfer", \
                                     command=lambda: fileTransfer(self))
        self.executeButton.grid(row=2, column=1, padx=(20,20), pady=(0,30), sticky=E)
        
        #Instantiate file path variables as StringVar
        self.txt_source = StringVar()
        self.txt_destination = StringVar()

        #Create Entry Boxes for File Paths
        self.sourceEntry = tk.Entry(self.master, width=80, textvariable=self.txt_source)
        self.sourceEntry.grid(row=0, column=1, padx=(15,20), pady=(30,30))
        self.destinationEntry = tk.Entry(self.master, width=80, textvariable=self.txt_destination)
        self.destinationEntry.grid(row=1, column=1, padx=(15,20), pady=(0,30))

####    Define functions for writing the file path to the StringVar
#returns full path of source folder
def fileSource(self):
    self.txt_source.set(filedialog.askdirectory(title='Select a Source Folder'))
    
#returns full path of destination folder
def fileDestination(self):
    self.txt_destination.set(filedialog.askdirectory(title='Select a Destination Folder'))
    
#iterates thru source file, locates .txt files, and moves them to destination file.  Then, calls on updateDB
def fileTransfer(self):
    self.source = self.txt_source.get()
    self.target = self.txt_destination.get()
    self.fileList = os.listdir(self.source)
    for files in self.fileList:
        if files.endswith(".txt"):
            self.filePath = os.path.join(self.source,files)
            shutil.move(self.filePath,self.target)
    updateDB(self)
#updates database with relevant data
def updateDB(self):
    conn = sqlite3.connect('Drill.db')
    with conn:
        cur = conn.cursor()
        #create database if not exists
        cur.execute("CREATE TABLE IF NOT EXISTS tbl_fileMove( \
            ID INTEGER PRIMARY KEY AUTOINCREMENT, \
            col_fileName TEXT, \
            col_getmtime TEXT)")
        #look at files in destination directory.  For each, insert into table the file name (files) and getmtime
        #redefine fileList since the files were relocated
        self.fileList = os.listdir(self.target)
        for files in self.fileList:
            self.filePath = os.path.join(self.target,files)
            cur.execute("INSERT INTO tbl_fileMove(col_fileName,col_getmtime) VALUES (?,?)", \
            (files,str(time.ctime(os.path.getmtime(self.filePath))),))
            print(self.filePath)
            print(str(time.ctime(os.path.getmtime(self.filePath))))
        conn.commit()
    conn.close()
    

if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
