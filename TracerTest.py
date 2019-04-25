
from tkinter import *
import tkinter as tk

root = tk.Tk()

def callback(*args):
    print('var1 changed')

var1=tk.StringVar()
var1.set("Why hello thur!")
print(var1)
var1.trace('w',callback)
var1.set("o rly?")

    
