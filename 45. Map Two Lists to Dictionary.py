def mapp(list1,list2):
    dictnary = dict(zip(list1,list2))

    return dictnary

lst1 = ['Car','Bike','Truck']
lst2 = ['Lamborghini','Kawasaki','TATA']
print(mapp(lst1,lst2))
