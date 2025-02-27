#only works for undirected graphs

def detect_cycle_undirected(graph):
    visited = set()

    def dfs(vertex, parent=None):
        visited.add(vertex)

        for neighbor, _ in graph.graph[vertex]:
            if neighbor in visited and neighbor != parent:
                return True

            if neighbor not in visited:
                if dfs(neighbor, vertex):
                    return True

        return False

    for vertex in graph.graph:
        if vertex not in visited:
            if dfs(vertex):
                return True

    return False

def find_cycle_path_undirected(graph):
    visited = set()
    parent = {}

    def dfs(vertex, prev=None):
        visited.add(vertex)
        parent[vertex] = prev

        for neighbor, _ in graph.graph[vertex]:
            if neighbor == prev:
                continue

            if neighbor in visited:
                cycle = []
                current = vertex
                while current != neighbor:
                    cycle.append(current)
                    current = parent[current]
                cycle.append(neighbor)
                cycle.append(vertex)
                return cycle

            path = dfs(neighbor, vertex)
            if path:
                return path

        return None

    for vertex in graph.graph:
        if vertex not in visited:
            cycle = dfs(vertex)
            if cycle:
                return cycle

    return None
