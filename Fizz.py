def fizzbuzz():
    for i in range(1,51):
        if (i%3==0) and (i%5==0):
            print("FizzBuzz")
            continue
        if i%3==0:
            print("Fizz")
        if i%5==0:
            print("Buzz")
        
    return


fizzbuzz()
