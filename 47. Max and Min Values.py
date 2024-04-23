def maxMin(dictnary):
    maxVal = max(dictnary.values())
    minVal = min(dictnary.values())

    return maxVal,minVal

dic1 = {'a':2,'b':4,'c':12,'d':8}
a,b = maxMin(dic1)
print("Max Value: ",a)
print("Min Value: ",b)
