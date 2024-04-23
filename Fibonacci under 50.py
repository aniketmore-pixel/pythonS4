def fibonacci(limit):
    fib_sequence = [0,1]

    while True:
        next_no = fib_sequence[-1] + fib_sequence[-2]

        if next_no > limit:
            break

        fib_sequence.append(next_no)

    return fib_sequence

print(fibonacci(50))
