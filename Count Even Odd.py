def evenodd(nums):
    evenct = 0
    oddct = 0
    for i in nums:
        if i%2==0:
            evenct += 1
        else:
            oddct += 1
            
    return evenct,oddct
    
numbers = (1,2,3,4,5,6,7,8,9)
print("Number of even and odd digits:",evenodd(numbers))
