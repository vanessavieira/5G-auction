from collections import deque


def dijkstra(graph, initial):
    visited = {initial: 0}
    path = {}
    nodes_id = []

    for i in range(len(graph.nodes)):
        nodes_id.append(graph.nodes[i].id)

    while nodes_id:
        min_node = None
        for node in nodes_id:
            if node in visited:
                if min_node is None:
                    min_node = node
                elif visited[node] < visited[min_node]:
                    min_node = node
        if min_node is None:
            break

        nodes_id.remove(min_node)
        current_weight = visited[min_node]

        for edge in graph.edge_list[min_node]:
            try:
                weight = current_weight + graph.distances[(min_node, edge)]
            except:
                continue
            if edge not in visited or weight < visited[edge]:
                visited[edge] = weight
                path[edge] = min_node

    return visited, path


def shortest_path(graph, origin, destination):
    visited, paths = dijkstra(graph, origin)
    full_path = deque()
    _destination = paths[destination]

    while _destination != origin:
        full_path.appendleft(_destination)
        _destination = paths[_destination]

    full_path.appendleft(origin)
    full_path.append(destination)

    for i in range(len(full_path)):
        for j in range(len(graph.nodes)):
            if graph.nodes[j].id == full_path[i]:
                full_path[i] = graph.nodes[j]

    # return visited[destination],
    return list(full_path)