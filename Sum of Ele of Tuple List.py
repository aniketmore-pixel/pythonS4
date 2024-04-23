def sumele(list_of_tuples):
    anslist = [sum(j) for j in list_of_tuples]
    return anslist

ques1 = [(1, 2), (2, 3), (3, 4)]

ques2 = [(1,2,6),(2,3,-6),(3,4),(2,2,2,2)]

print(sumele(ques1))
print(sumele(ques2))
