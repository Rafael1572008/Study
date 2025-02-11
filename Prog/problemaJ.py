def treatment(n, edgers):
    graph = {}

    for i in range(1, n+1):
        graph[i] = []


    for edger in edgers:
        node_a, node_b = edger
        
        graph[node_a].append(node_b)
        graph[node_b].append(node_a)
    return graph

def connected_components_count(graph):
    visited = set()
    count = 0

    for node in graph:
        if node in visited:
            continue

        queue = [node]

        while queue:
            current_node = queue.pop()

            if current_node in visited:
                continue
            visited.add(current_node)

            for neighbor in graph[current_node]:
                if neighbor not in visited:
                    queue.append(neighbor)
        
        count += 1
    return count

graph = []

n, m = map(int, input().split())
for i in range(m):
    graph.append(list(map(int, input().split())))

resp =  connected_components_count(treatment(n, graph))

print(resp)
