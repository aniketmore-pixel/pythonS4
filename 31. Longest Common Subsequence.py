def long_com_subseq(list1,list2):
    if not list1 or not list2:
        return []

    if list1[0] == list2[0]:
        return [list1[0]] + long_com_subseq(list1[1:],list2[1:])
    else:
        subseq1 = long_com_subseq(list1[1:],list2)
        subseq2 = long_com_subseq(list1,list2[1:])
        
        if len(subseq1) > len(subseq2):
            return subseq1
        elif len(subseq1) < len(subseq2):
            return subseq2
        else:
            return subseq1


ques1 = [1,2,3,4,8,7]
ques2 = [1,3,4,9,8]
print(long_com_subseq(ques1,ques2))
