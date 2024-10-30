from collections import defaultdict

def dfs(graph, node, visited, result):
    visited.add(node)
    result.append(node)
    
    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited, result)

V, E = map(int, input().split())
graph = defaultdict(list)

for _ in range(E):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

start_node = int(input())
visited = set()
result = []

dfs(graph, start_node, visited, result)

print(" ".join(map(str, result)))
