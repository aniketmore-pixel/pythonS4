def typeTriangle(x,y,z):
    if x==y==z:
        print("Equilateral Triangle.")
    elif x==y or y==z or x==z:
        print("Isoceles Triangle.")
    else:
        print("Scalene Triangle.")


typeTriangle(3,4,4)
typeTriangle(6,6,6)
typeTriangle(1,2,3)
