#Sample Wrong Code
t = int(input())
for i in range(t):
    n, l, r = map(int, input().split())
    arr = list(map(int, input().split()))
    arr.sort()
    ans = 0
    ind = 0
    for i in range(l - 1, r):
        ans += arr[ind]
        ind += 1
    print(ans)