def increasing(list1):
    seq=0
    maxseq=0
    
    for i in range(0,len(list1)):
        if i==0:
            seq += 1
            maxseq = max(seq,maxseq)
            
        elif list1[i] > list1[i-1]:
            seq += 1
            maxseq = max(seq,maxseq)

        else:
            maxseq = max(seq,maxseq)
            seq = 1
            
    return maxseq


ques1 = [3,4,2,1,9,8,4,5,6,7,1,2,3,4,5]
print(increasing(ques1))
