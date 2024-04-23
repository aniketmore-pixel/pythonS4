def sortDict(dictnary):
    asc = dict(sorted(dictnary.items(), key=lambda item:item[1]))

    dsc = dict(sorted(dictnary.items(), key=lambda item:item[1], reverse=True))

    return asc, dsc


my_nums = {'a':2,'b':4,'c':1,'d':8,'e':5}
x,y = sortDict(my_nums)
print("Ascending Order: ", x)
print("Descending Order: ", y)
