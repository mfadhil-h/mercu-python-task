def all_path(graph, start, end, path=None):
    if path is None:
        path = []
    path = path + [start]
    if start == end:
        return [path]
    if start not in graph:
        return []
    paths = []
    for node in graph[start]:
        if node not in path:
            new_paths = all_path(graph, node, end, path)
            for new_path in new_paths:
                paths.append(new_path)
    return paths


def shortest_path(graph, start, end, path=None):
    if path is None:
        path = []
    path = path + [start]
    if start == end:
        return path
    if start not in graph:
        return None
    shortest = None

    for node in graph[start]:
        if node not in path:
            new_path = shortest_path(graph, node, end, path)
            if new_path:
                if not shortest or len(new_path) < len(shortest):
                    shortest = new_path

    return shortest


def find_list_shortest_path(all_paths):
    list_shortest = []
    for path in all_paths:
        if len(path) == len(short_path):
            list_shortest.append(path)
    return list_shortest


def display_block(paths):
    for i in range(len(paths)):
        print('Path', i + 1, '=', paths[i])


def find_all_edges(graphs):
    list_edge = []
    for keys in graphs.keys():
        if graphs[keys]:
            for value in graphs[keys]:
                temp = keys + ' => ' + value,
                list_edge.append(temp)
    return list_edge


random_graph = {
    'A': ['C', 'D'],
    'B': ['C', 'E'],
    'C': ['A', 'B', 'D', 'E'],
    'D': ['C', 'E'],
    'E': ['C', 'B'],
    'F': []
}

list_all_path = all_path(random_graph, 'A', 'E')
print('\nAll Paths  : ')
display_block(list_all_path)

short_path = shortest_path(random_graph, 'A', 'E')
list_shortest_path = find_list_shortest_path(list_all_path)
print('\nShortest Path and Alternative : ')
display_block(list_shortest_path)

all_edges = find_all_edges(random_graph)
print('\nAll Edges : ')

display_block(all_edges)
