import random

# Maximum constraints
MAX_T = 10**4  # Max number of test cases
MAX_N = 10**5  # Max size of the array
MAX_VAL = 10**9  # Max value of elements in the array

# Generate random test cases
t = 1  # Adjust the range for smaller or larger tests
print(t)
for _ in range(t):
    # Generate n, l, r
    n = random.randint(1, 100000)  # Smaller range to ensure quick testing; use MAX_N for stress tests
    l = random.randint(1, n)
    r = random.randint(l, n)  # Ensure r >= l
    print(n, l, r)
    
    # Generate the array
    arr = [random.randint(1, 10000) for _ in range(n)]
    print(*arr)
