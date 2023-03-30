import sys
from collections import deque
n = int(sys.stdin.readline())
queue = deque()

for _ in range(1, n+1):
    queue.append(_)
                
while len(queue) > 1:
    queue.popleft()
    queue.append(queue.popleft())
    
print(queue[0])