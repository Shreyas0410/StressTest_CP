#Sample Input Generator
import random

MAX_T = 10**4
MAX_N = 10**5  
MAX_VAL = 10**9 

t = 1  
print(t)
for _ in range(t):
    n = random.randint(1, 100000)  
    l = random.randint(1, n)
    r = random.randint(l, n)
    print(n, l, r)
    arr = [random.randint(1, 10000) for _ in range(n)]
    print(*arr)
