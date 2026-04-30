from collections import deque
def solution(cacheSize, cities):
    cache = deque([])
    res = 0
    for c in cities:
        c = c.lower()
        if c in cache:
            cache.remove(c)
            res += 1
        else:
            if len(cache) == cacheSize != 0:
                cache.pop()
            res += 5
        if len(cache) != cacheSize:
            cache.appendleft(c)
    return res