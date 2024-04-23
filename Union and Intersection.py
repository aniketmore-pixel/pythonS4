def unionInt(list1,list2):
    union = list(set(list1) | set(list2))

    intersect = list(set(list1) & set(list2))

    return union,intersect


l1 = [3,4,5,6,6,7]
l2 = [2,4,5,6,8]

union,intersection = unionInt(l1,l2)
print("Union is: ", union)
print("Intersection is: ", intersection)

