# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict
d = defaultdict(list)

n,m = [int(i) for i in input().split()]

for i in range(1,n+1):
    d[input()].append(i)

for j in range(m):
    x = d[input()]
    if x:
        print(*x)
    else:
        print(-1)
