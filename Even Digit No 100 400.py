def evenDig(num):
    strNo = str(num)

    for dig in strNo:
        if int(dig)%2!=0:
            return False

    return True

def find_even_no():
    for no in range(100,401):
        if evenDig(no):
            print(no)

find_even_no()
