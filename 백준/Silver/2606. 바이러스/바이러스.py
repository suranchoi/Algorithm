import sys
# 값 입력
n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
v = 1

# graph 정보 입력
graph = [[False] * (n+1) for _ in range(n+1)]
visited = [False] * (n+1)
for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a][b] = True
    graph[b][a] = True
  
# bfs  
def bfs():
    while q:
        cur = q.pop(0)
        visited[cur] = True
        for next in range(1, n+1):
            if not visited[next] and graph[cur][next]:
                visited[next] = True
                q.append(next)
    return sum(visited) - 1
    
q = [v]
print(bfs())
