strng = input("Enter a string: ")

lst = []

for num in strng:
    if num.isdigit():
        lst.append(int(num))

print(lst)

fx1 = lambda a,string : a>len(string)

nums = []
for j in lst:
    if fx1(j,strng):
        nums.append(j)

print(sorted(nums))
        
    
