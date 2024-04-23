def removedup(list1):
    seen = {}
    result = []

    for ele in list1:
        if ele not in seen:
            result.append(ele)
            seen[ele] = True

    return result

ques1 = [4,3,2,1,2,7,8]
print(removedup(ques1))
            
