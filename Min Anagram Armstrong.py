#Minimum of three numbers
def minimum(x,y,z):
    return min(x,y,z)

a = int(input("Enter 1st no: "))
b = int(input("Enter 2nd no: "))
c = int(input("Enter 3rd no: "))

print(minimum(a,b,c))


#Anagram check
def anagram(x,y):
    x.lower().replace(" ","")
    sortedx = sorted(x)

    y.lower().replace(" ","")
    sortedy = sorted(y)

    return sortedx == sortedy

w = input("Enter 1st string: ")
v = input("Enter 2nd string: ")

if anagram(w,v):
    print("These strings are Anagram.")
else:
    print("These strings are not Aragram.")


#Armstrong
def armstrong(num):
    sum = 0

    for j in num:
        sum += int(j) ** len(num)

    return sum == int(num)

h = input("Enter a no: ")

if armstrong(h):
    print(f"{h} is an Armstrong no.")
else:
    print(f"{h} is not an Armstrong no.")



