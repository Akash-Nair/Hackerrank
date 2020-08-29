# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import permutations
x,y = input().split()
perm = list(permutations(x,int(y)))
perm.sort()
for i in perm:
    print(''.join(i))
