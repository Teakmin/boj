#재귀는 반복적인 학습이 필요

N, e, start = map(int,input().split())
graph = [[] for _ in range(N + 1)]
for i in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
for x in graph:
    x.sort()

def dfs(graph, visited, now):
    visited[now] = True
    print(now, end=' ')
    for next in graph[now]:
        if not visited[next]:
            dfs(graph, visited, next)

dfs_visited = [False] * (v + 1)
dfs_visited[start] = True
dfs(graph, visited, start)