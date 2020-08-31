# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import namedtuple
n = int(input())
stud = namedtuple('stud',(input().strip().split()))
s = 0
for i in range(n):
    x = stud(*input().strip().split())
    s+=float(x.MARKS)
print(s/n)
