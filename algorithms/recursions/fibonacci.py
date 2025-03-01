def fibonacci(n): #n time complexity
    cache = {}
    cache[0] = 0
    cache[1] = 1

    def fib(n):
        if n in cache:
            return cache[n]
        else:
            cache[n] = fib(n - 1) + fib(n - 2)
            return cache[n]

    return fib(n)

def unoptimised_fibonacci(n): #2^n time complexity
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]

    fib = unoptimised_fibonacci(n - 1)
    fib.append(fib[-1] + fib[-2])
    return fib
