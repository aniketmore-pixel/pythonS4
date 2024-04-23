def palindrome(list1):

    return list1 == list1[::-1]


ques1 = [1,2,3,4,3,2,1]
ques2 = [2,4,5,7]
print(palindrome(ques1))
print(palindrome(ques2))
