from collections import deque

def breadth_first_search(graph, start_node):
    visited = []
    queue = deque([start_node])
    visited_set = set([start_node])  

    while queue:
        current_node = queue.popleft()
        visited.append(current_node)
        for neighbor in graph[current_node]:
            if neighbor not in visited_set:
                queue.append(neighbor)
                visited_set.add(neighbor)

    return visited

def parse_input():
    num_vertices = int(input())
    
    graph = {i: [] for i in range(1, num_vertices + 1)}

    for _ in range(num_vertices - 1):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u) 

    start_node = int(input())  

    return graph, start_node

def main():
    graph, start_node = parse_input()
    bfs_result = breadth_first_search(graph, start_node)
    print(" ".join(map(str, bfs_result)))

if __name__ == "__main__":
    main()
