def generate_dict(n):
    dictnary = {}
    for x in range(1,n+1):
        dictnary[x] = x*x

    return dictnary

print(generate_dict(15))
