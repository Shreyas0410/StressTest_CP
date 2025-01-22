for _ in range(int(input())):
    n,l,r = map(int, input().split())
    a = list(map(int, input().split()))
    print(min(sum(sorted(a[:r])[:r-l+1]), sum(sorted(a[l-1:])[:r-l+1])))