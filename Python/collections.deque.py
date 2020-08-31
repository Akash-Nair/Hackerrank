# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import deque
q = deque()
n = int(input())
for i in range(n):
    s = input().split()
    if s[0] == 'append':
        q.append(s[1])
    elif s[0] == 'appendleft':
        q.appendleft(s[1])
    elif s[0] == 'pop':
        q.pop()
    elif s[0] == 'popleft':
        q.popleft()
print(' '.join(q))
