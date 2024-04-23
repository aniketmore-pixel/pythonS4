def kthsmallest(list1,k):
    
    listx = sorted(list1)

    return listx[k-1]

ques1 = [3,4,2,1,5,7,9]
k = int(input("Enter the value of k: "))
print(kthsmallest(ques1,k)) 
