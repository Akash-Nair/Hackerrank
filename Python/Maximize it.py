# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import product
k,m = [int(i) for i in input().split()]
s = 0

x = []
for i in range(k):
    x.append([int(i) for i in input().split()][1:])

z = list(map(lambda x: sum(i**2 for i in x)%m,product(*x)))
print(max(z))
