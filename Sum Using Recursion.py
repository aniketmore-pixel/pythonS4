#Write a Python program to get the sum of a non-negative integer using recursion.

def sum(a):
    if a<10:
        return a
    
    strno = str(a)
    str_first_digit = strno[0]
    first_digit = int(str_first_digit)
    strRest = strno[1:]

    if strRest != "":
        rest = int(strRest)
        return first_digit + sum(rest)

    return 0

b = int(input("Enter a non-negative no.: "))
print(sum(b))

    
