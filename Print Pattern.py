def trianglepattern(a):
    for j in range(1,a+1):
        for k in range(1,j+1):
            print("* ", end="")
        print("")

a = int(input("Enter a number: "))
trianglepattern(a)
