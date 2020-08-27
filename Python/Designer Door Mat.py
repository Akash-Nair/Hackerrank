# Enter your code here. Read input from STDIN. Print output to STDOUT
import math

m,n = [int(i) for i in input().split()]

limit = math.ceil(m/2)
for row in range(1,limit):
    print(('.|.'*(2*row-1)).center(n,'-'))

print('WELCOME'.center(n,'-'))

for row in range(limit-1,0,-1):
    print(('.|.'*(2*row-1)).center(n,'-'))

