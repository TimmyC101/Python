mySentence = 'I love the color '
color_list = ['red','blue','pink','teal','black']

def fxn(var1,var2):
    lst = []
    for x in range(0,len(var2),1):
        msg = var1+var2[x]
        lst.append(msg)
    return lst

print(fxn(mySentence,color_list))

