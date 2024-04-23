def fnre(list1):
    freq = {}
    for ele in list1:
        if ele in freq:
            freq[ele] += 1
        else:
            freq[ele] = 1

    for ele in freq:
        if freq[ele] == 1:
            return ele

    return None


ques1 = [1,2,3,4,5,1,2,3]
print(fnre(ques1))
