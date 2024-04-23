def remdup(dictnary):
    unique_dic = {}
    for key,val in dictnary.items():
        if val not in unique_dic.values():
            unique_dic[key] = val

    return unique_dic


dic = {'a':4,'b':5,'c':1,'d':5,'e':7,'f':1}
print(remdup(dic))
