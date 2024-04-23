import itertools

def permutations(list1):
    list_perm = itertools.permutations(list1)

    return list(list_perm)

ques1 = [1,2,3]
print(permutations(ques1))
