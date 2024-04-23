def gcd(x,y):
    min_no = min(x,y)

    for i in range (min_no,0,-1):
        if x%i==0 and y%i==0:
            return i

def fibonacci(limit):
    fib_sequence = [0,1]
    next_no = 0
    
    while next_no<=limit:
        next_no = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_no)

    return fib_sequence

def factorial(a):
    fact = 1;

    for i in range(1,a+1):
        fact = fact * i

    return fact

print(gcd(3,5))
print(fibonacci(10))
print(factorial(6))
    
