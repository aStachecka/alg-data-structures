#lab 4
#implementacja algorytmow grafowych
#algorytm Flodya-Warshalla

INF = float('inf')

def AlgorytmFloydaWarshalla(graph):
    d = [row[:] for row in graph]
    p = [[-1 if graph[i][j] == 0 or graph[i][j] == INF else i for j in range(len(graph))] for i in range(len(graph))]

    for u in range(len(graph)):

        for v in range(len(graph)):

            for w in range(len(graph)):

                if u != v and v != w and u != w:
                    l = d[v][u] + d[u][w]

                    if l < d[v][w]:
                        d[v][w] = l
                        p[v][w] = p[u][w]

    return d, p


graph = [
    [0, 3, INF, 7],
    [8, 0, 2, INF],
    [5, INF, 0, 1],
    [2, INF, INF, 0]
]

result = AlgorytmFloydaWarshalla(graph)

print("d:")
for row in result[0]:
    print(row)
print("p:")
for row in result[1]:
    print(row)