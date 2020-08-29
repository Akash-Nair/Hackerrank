# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations
x,y = input().split()
x = [i for i in x]
x.sort()
for j in range(1,int(y)+1):
    comb = list(combinations(x,j))
    for i in comb:
        print(''.join(i))
