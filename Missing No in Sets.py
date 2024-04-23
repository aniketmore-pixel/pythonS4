def missing(setx,sety):
    miss1 = sety - setx
    miss2 = setx - sety

    return miss1,miss2

    
set1 = {1,3,7}
set2 = {2,3,7}

a,b = missing(set1,set2)
print("Missing in set 1:", a)
print("Missing in set 2:", b)
