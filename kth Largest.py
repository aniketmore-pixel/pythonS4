def kthlargest(list1,k):
    
    listx = sorted(list1)

    return listx[-k]

ques1 = [3,4,2,1,5,7,9]
k = int(input("Enter the value of k: "))
print(kthlargest(ques1,k)) 
