def keyexists(key,dictnary):
    if key in dictnary:
        print(f"The {key} key exists in this Dictionary.")
    else:
        print(f"The {key} key doesn't exist in this Dictionary.")

dic1 = {'a':3, 'b':4, 'd':12, 'e':16}
key = input("Enter a key: ")
keyexists(key, dic1)
