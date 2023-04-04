import sys
from collections import deque

n, k = map(int, sys.stdin.readline().split())
de = deque()
answer = []

# n명의 사람들
for i in range(n):
    de.append(i+1)
    
while de:
    for i in range(k-1):
        de.append(de.popleft())
    answer.append(de.popleft())
    
print("<", end='')
print(", ".join(map(str, answer)), end='')
print(">")
