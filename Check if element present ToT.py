def find_ele(value,tuple_of_tuples):
    for tup in tuple_of_tuples:
        if value in tup:
            return True
    return False

ques1 = (('Red', 'White', 'Blue'), ('Green', 'Pink', 'Purple'), ('Orange', 'Yellow', 'Lime'))
tofind = input();
print(find_ele(tofind,ques1))
