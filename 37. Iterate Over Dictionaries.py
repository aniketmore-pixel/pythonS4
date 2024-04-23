def iterate(dictnary):
    for key,value in dictnary.items():
        print(f"Key:{key},Value:{value}")

    for key in dictnary.keys():
        print(f"Key:{key}")

    for value in dictnary.values():
        print(f"Value:{value}")


dict1 = {'a':5,'b':3,'c':12,'d':7,'e':16}
iterate(dict1)
