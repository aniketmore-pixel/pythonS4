def list_list(list_of_tuples):
    listolist = [list(j) for j in list_of_tuples]
    return listolist

input1 = [(1, 2), (2, 3), (3, 4)]
input2 = [(1, 2), (2, 3, 5), (3, 4), (2, 3, 4, 2)]

print(list_list(input1))
print(list_list(input2))
