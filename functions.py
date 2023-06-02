import os

def Load_Data(fname, obj):
    temp = []
    array = []

    ff = os.path.join(os.getcwd(), 'data') #cwd = current working directory
    fname = os.path.join(ff,fname)

    with open(fname, 'r') as file:
        for line in file:
            #print(line, end = "")
            temp.append(line.split())

    del temp[0]

    for x in temp:
        array.append(obj(*x))

    #for x in array:
    #   print(x.show_self())
    return array


def hello():
    print("helloe")