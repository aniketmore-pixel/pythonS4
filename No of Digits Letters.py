def digLet(str):
    letCount = 0
    digCount = 0

    for char in str:
        if char.isdigit():
            digCount += 1
        elif char.isalpha():
            letCount += 1

    return digCount,letCount

a = input("Enter a string: ")
print("The number of digits & letters are: ", digLet(a))
