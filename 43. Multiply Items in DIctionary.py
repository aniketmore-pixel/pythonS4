def multiplyvals(dictnary):
    product = 1
    for val in dictnary.values():
        product = product * val

    return product

dic1 = {'a':4,'b':5,'c':2}
print(multiplyvals(dic1))
