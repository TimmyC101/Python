import os

def writeData():
    data = "Hello World!"
    with open("test.txt",'a') as f:
        f.write(data)
        f.close()

def openFile():
    fileName = input("Please enter the file name with the type\n>>> ")
    with open(fileName,'r') as f:
        data = f.read()
        print(data)
        f.close()

if __name__ == "__main__":
    openFile()
