def generate_dict(n):
    dictnary = {}
    for x in range(1,n+1):
        dictnary[x] = x*x

    return dictnary

y = int(input("Enter a number: "))
print(generate_dict(y))
