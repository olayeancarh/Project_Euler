def fibonacci(limit):
    fib_series = [1, 2]

    lastValue = 2

    while lastValue < limit+1:
        fib_series.append(fib_series[-1] + fib_series[-2])

        lastValue = fib_series[-1] + fib_series[-2]

    abc = sum([fib_series[values] for values in range(1, len(fib_series), 3)])

    print(abc)

fibonacci(4000000)
        