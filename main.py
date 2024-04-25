from collections import deque
from heapq import heappush, heappop 

def shortest_shortest_path(graph, source):
    """
    Find shortest path weights and number of edges for each node from the source.

    Params: 
      graph.....a graph represented as a dict where each key is a vertex
                and the value is a set of (vertex, weight) tuples
      source....the source node

    Returns:
      a dict where each key is a vertex and the value is a tuple of
      (shortest path weight, shortest path number of edges).
    """
    # Initialize visited with source with distance 0 and edge count 0
    visited = {source: (0, 0)}
    queue = deque([source])

    while queue:
        current = queue.popleft()

        current_dist, current_edges = visited[current]

        for neighbor, weight in graph[current]:
            new_dist = current_dist + weight
            new_edges = current_edges + 1

            if neighbor not in visited or new_dist < visited[neighbor][0]:
                visited[neighbor] = (new_dist, new_edges)
                queue.append(neighbor)
            elif new_dist == visited[neighbor][0] and new_edges < visited[neighbor][1]:
                visited[neighbor] = (new_dist, new_edges)

    return visited

def bfs_path(graph, source):
    """
    Finds the parent of each vertex in the shortest path tree using BFS.

    Returns:
      a dict where each key is a vertex and the value is the parent of 
      that vertex in the shortest path tree.
    """
    visited = {source: None}
    queue = deque([source])

    while queue:
        node = queue.popleft()

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited[neighbor] = node
                queue.append(neighbor)

    return visited


def get_sample_graph():
   return {'s': {'a', 'b'},
          'a': {'b'},
          'b': {'c'},
          'c': {'a', 'd'},
          'd': {}
          }



def get_path(parents, destination):
    """
    Constructs the shortest path from the source to a given destination node.

    Params:
      parents......a dictionary mapping each node to its parent in the shortest path tree.
      destination..the destination node for which the path is required.

    Returns:
      A string representing the shortest path to the destination node.
    """
    path = []
    while destination is not None and parents[destination] is not None:
        path.append(destination)
        destination = parents[destination]

    return ''.join(reversed(path))


