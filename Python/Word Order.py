from collections import OrderedDict
d = OrderedDict()
n = int(input())
for i in range(n):
    s = input()
    if s in d:
        d[s] += 1
    else:
        d[s] = 1

print(len(d))
ans = []
for i in d:
    ans.append(d[i])
print(' '.join([str(i) for i in ans]))
