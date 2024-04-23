def removekey(dictnary,key):
    del dictnary[key]

dic1 = {'a':89,'b':24,'c':12}
print(dic1)

z = input("Enter the key to remove: ")
removekey(dic1,z)
print(dic1)
