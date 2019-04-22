##    Drill - check a specific folder on the hard drive,
##    verify whether the files in with ".txt" file extension and if they do,
##    print those file names and their corresponding modified time-stamps to the console.
##
##    Use os.listdir() to iterate through all files within directory
##    Use os.path.join() to concatenate file directory to file name to form absolute path
##    Use os.path.getmtime() to find latest edit date for each file
##    print each ".txt" file and corresponding getmtime to the console
##
##    Create a new directory and create 10 files within this folder.
##    These can be anything but must contain at least 2 ".txt" documents

import os

fDir = 'C:\\Users\\Tim\\Documents\\GitHub\\Python\\Drill1\\'
fileList = os.listdir(fDir)
txtList = []
for names in fileList:
    if names.endswith(".txt"):
        txtList.append(names)
for i in range(len(txtList)):
    fName = txtList[i]
    fullPath = os.path.join(fDir,fName)
    print("File " + str(i+1))
    print("File Path>>> " + fullPath)
    print("Last Mod>>> " + str(os.path.getmtime(fullPath)))
    print("\n")



