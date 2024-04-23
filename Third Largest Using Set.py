def third_largest(numbers):
    set1 = set(numbers)  #Removing duplicate elements 

    sorted_list = sorted(list(set1))

    if len(sorted_list) < 3:
        return false
    
    return sorted_list[-3]

    
ques1 = [3,45,23,24,4,23,24,99,12,7,84]
print(third_largest(ques1))
