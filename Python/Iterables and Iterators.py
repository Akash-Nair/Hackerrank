from itertools import combinations
n = int(input())
s = input().split()
k = int(input())

comb = list(combinations(s,k))
cnt = 0
for i in comb:
    if 'a' in i:
        cnt+=1

print(round(cnt/len(comb),12))
