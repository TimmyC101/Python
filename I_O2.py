import os

fname = 'test.txt'
fdir = 'C:\\Users\\Tim\\Documents\\GitHub\\Python\\'
print(open(os.path.join(fdir,fname),'r').read())



