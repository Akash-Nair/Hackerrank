# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations_with_replacement
x,y = input().split()
x = [i for i in x]
x.sort()
comb = list(combinations_with_replacement(x,int(y)))
for i in comb:
    print(''.join(i))
