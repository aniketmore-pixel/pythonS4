def dictnary(obj):
    dict1 = vars(obj)
    return dict1

class book:
    def __init__(self,name,price):
        self.name = name
        self.price = price

a = book("The Wise Man's Fear", 300)
print(dictnary(a))
