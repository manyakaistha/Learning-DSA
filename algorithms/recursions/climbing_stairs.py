def climbStairs(n):
        cache = {}
        cache[1] = 1
        cache[2] = 2

        def climb(n):
            if n in cache:
                return cache[n]
            else:
                cache[n] = climb(n - 1) + climb(n - 2)
                return cache[n]

        return climb(n)
