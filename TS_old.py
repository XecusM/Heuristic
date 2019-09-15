'I think this is the main concept but you assume that you will always begin from (a) how you can get the minimum travel distance assuming that I have sales man in every country and I want to tell from one of them to make the job with minimum distance. after this step you need to check github-ts.py for generalization'
distances = {
    
    
    
    
edges = [
    ('a', 'b', 43),
    ('a', 'c', 31),
    ('a', 'd', 131),
    ('a', 'e', 55),
    ('b', 'c', 23),
    ('b', 'd', 76),
    ('b', 'e', 29),
    ('c', 'd', 60),
    ('c', 'e', 45),
    ('e', 'd', 69)
]


def traverse(graph, src, path=[], path_cost=0, level=1, visited=set()):
    """Explore a graph structure. Graph in this code is a list of tuples"""

    inf = 99999999

    best_path = path
    min_cost = inf


    visited.add(src)

    for dst in graph[src].keys():

        if dst in visited:
            continue

       
        new_path = path + [dst]
        new_path_cost = path_cost + graph[src][dst]

        

        child_path, child_cost = traverse(graph, dst, new_path, new_path_cost, level+1, visited)

        if child_cost < min_cost:
            min_cost = child_cost
            best_path = child_path

    visited.remove(src)

    if min_cost == inf:
        return (path, path_cost)
    else:
        return (best_path, min_cost)


def insert_dummy(graph):
    """Insert dummy edges from a new edge 'dummy' to every other node."""
    nodes = graph.keys()
    dummy_entry = {node: 0 for node in nodes}
    graph["dummy"] = dummy_entry


def make_graph(edges):
    """Construct a graph based on a list of edges."""

    graph = {}

    for src, dst, cost in edges:

        

        if src not in graph:    # Add dst as a child of src
            graph[src] = {}

        graph[src][dst] = cost 

        
        if dst not in graph:    # Add src as a child of dst
            graph[dst] = {}

        graph[dst][src] = cost  # Now we have all possible combination of nodes
        

    return graph


def main():
    graph = make_graph(edges)
    insert_dummy(graph)
    path, cost = traverse(graph, "dummy")
    print("Best path is %s (cost = %d)" % (path, cost))


if __name__ == '__main__':
    main()

    
    
       
  -------------------------------------------------------------------------------------  
    
    'a': {
        'b': 23,
        'c': 12,
        'd': 131,
        'e': 11
    },

    'b': {
        'a': 23,
        'c': 23,
        'd': 76,
        'e': 29


    },
    'c': {
        'a': 12,
        'b': 23,
        'd': 60,
        'e': 45


    },
    'd': {
        'a': 131,
        'b': 76,
        'c': 60,
        'e': 69

    },

    'e': {
        'a': 11,
        'b': 29,
        'c': 45,
        'd': 69

    }


}

totalDist = 0
minDist = 1000000
minNode = ""
currentNode = ""
cities = 5
visited = []


for key, value in distances.items():
        for key2, value2 in value.items():
            if value2 < minDist:
                minDist = value2
                minNode = key
                currentNode = key2
visited.append(minNode)
visited.append(currentNode)
totalDist = totalDist + minDist

print(visited)

while len(visited) < cities:
    minDist = 1000
    data = distances.get(currentNode, "")

    for key3, value3 in data.items():
        if key3 not in visited:
            if value3 < minDist:
                    minDist = value3
                    minNode = key3
                    currentNode = key3

    visited.append(currentNode)
    print(visited)
    totalDist = totalDist + minDist





print("The total distance that almost gave Hatooz an anurism was " + str(totalDist) + " lightyears")
