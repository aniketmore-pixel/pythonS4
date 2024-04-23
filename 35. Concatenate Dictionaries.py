dict1 = {'a':4, 'b':6}
dict2 = {'c':12, 'z':1}
dict3 = {'w':16, 'v':14}

dict1cpy = dict1.copy()
dict1cpy.update(dict2)
dict1cpy.update(dict3)

print(dict1cpy)
