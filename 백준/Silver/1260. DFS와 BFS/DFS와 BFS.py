import sys
def dfs(idx):
    global visited
    visited[idx] = True
    print(idx, end=' ')
    for next in range(1, n+1):
        if not visited[next] and graph[idx][next]:
            dfs(next)
    
def bfs():
    global q, visited
    while q:
        cur = q.pop(0)
        visited[cur] = True
        print(cur, end=' ')
        for next in range(1, n+1):
            if not visited[next] and graph[cur][next]:
                visited[next] = True
                q.append(next)
                
# 입력
input = sys.stdin.readline
n, m, v = map(int, input().split())

graph = [[False] * (n+1) for _ in range(n+1)]
visited = [False] * (n+1)

for i in range(m):
    a, b = map(int, input().split())
    graph[a][b] = True
    graph[b][a] = True

# dfs
dfs(v)
print()


# bfs
visited = [False] * (n+1)
q = [v]
bfs()
    