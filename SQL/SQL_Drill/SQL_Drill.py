import sqlite3
import os

##    Write a script that creates a database and adds new data to it
##
##    Database must have 2 fields: an auto increment primary integer field and a string field
##    Read from the supplied list of file names at the bottom of page and
##        determine only the files from the list with a .txt extension
##    Add those qualifying file names within your database
##    Legibly print the qualifying text files to the console


conn = sqlite3.connect('Drill.db')
with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_name( \
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        col_1 TEXT)")
    conn.commit()
conn.close()

fileDir = 'C:\\Users\\Tim\\Documents\\GitHub\\Python\\SQL\\SQL_Drill'
fileList = os.listdir(fileDir)
txtList = []
for names in fileList:
    if names.endswith(".txt"):
        txtList.append(names)

conn = sqlite3.connect('Drill.db')
with conn:
    cur = conn.cursor()
    for i in range(len(txtList)):
        fileName = txtList[i]
        cur.execute("INSERT INTO tbl_name(col_1) VALUES (?)", \
            (fileName,))
        conn.commit()
conn.close()

for i in range(len(txtList)):
    fileName = txtList[i]
    fullPath = os.path.join(fileDir,fileName)
    print("File " + str(i+1))
    print("File Path>>> " + fullPath)
    print("Last Mod>>> " + str(os.path.getmtime(fullPath)))
    print("\n")


##    print(dir(sqlite3))
##    print(help(sqlite3))
