# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import groupby
s = [int(i) for i in input()]
group = []
for j,g in groupby(s):
    group.append(tuple(g))
ans = []
for i in group:
    ans.append((len(i),i[0]))
print(*ans)
