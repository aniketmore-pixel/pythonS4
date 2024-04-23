def reverselist(list1,st_idx,ed_idx):
    list1[st_idx:ed_idx+1] = reversed(list1[st_idx:ed_idx+1])
    return list1

    
ques1 = [3,2,4,1,2,7,8,6]
start = 3
end = 6
print(reverselist(ques1,3,6))
