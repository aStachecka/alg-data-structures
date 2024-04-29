#labolatorium 4
#implementacja algorytmow grafowych
#algorytm prima

def aPrima(graph):
    mst = [] #minimum spanning tree
    wierzcholki = list(graph.keys())
    v = set(wierzcholki[0]) #visited

    while len(v) < len(wierzcholki):
        edges = []

        for w in v:
            for neighbor, weight in graph[w].items():
                if neighbor not in v:
                    edges.append((weight, w, neighbor))

        edges.sort()
        weight, fr, to = edges[0]
        mst.append((fr, to, weight))
        v.add(to)

    return mst


graph = {
    'A': {'B': 2, 'D': 4},
    'B': {'A': 2, 'C': 3, 'D': 1},
    'C': {'B': 3, 'D': 5},
    'D': {'A': 4, 'B': 1, 'C': 5}
}

result = aPrima(graph)
print("Mst: ", result)