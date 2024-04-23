def sumcalc(dictnary):
    total = 0
    for val in dictnary.values():
        total += val

    return total

dic1 = {'a':5, 'b':4, 'c':1, 'd':24, 'e':2}
print(sumcalc(dic1))
