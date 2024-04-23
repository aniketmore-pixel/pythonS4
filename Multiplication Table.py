def table(a):
    for j in range(1,11):
        res = a*j
        print(f"{a}*{j} = {res}")

table(int(input("Enter a number: ")))
