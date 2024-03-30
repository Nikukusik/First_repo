def caching_fibonacci():
    cache = {}
    def fibonacci(num):
        if num <= 0:
            return 0
        elif num == 1:
            return 1
        elif num in cache:
            return cache[num]
        cache[num] = fibonacci(num-1) + fibonacci(num-2)
        return cache[num]
    return fibonacci

cache_fib = caching_fibonacci()
res = cache_fib(3)
print(res)
