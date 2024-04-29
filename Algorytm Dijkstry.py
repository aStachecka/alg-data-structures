#lab 4
#implementacja algorytmow grafowych
#algorytm dijkstry

import heapq

def AlgDijkstry(graph, start):
    dst = {v: float('inf') for v in graph}
    pred = {v: None for v in graph}
    dst[start] = 0

    pq = [(0, start)]

    while pq:
        currentDst, currentVrt = heapq.heappop(pq)
        if currentDst != dst[currentVrt]:
            continue

        for neighbor, weight in graph[currentVrt].items():
            newDst = dst[currentVrt] + weight
            if newDst < dst[neighbor]:
                dst[neighbor] = newDst
                pred[neighbor] = currentVrt
                heapq.heappush(pq, (newDst, neighbor))

    return dst, pred

graph = {
    'A': {'B': 2, 'C': 4},
    'B': {'A': 2, 'C': 1, 'D': 7},
    'C': {'A': 4, 'B': 1, 'D': 3},
    'D': {'B': 7, 'C': 3}
}

dist, pred = AlgDijkstry(graph, 'A')

print("Odległości od wierzchołka A:")
print(dist)
print("\nPoprzednicy:")
print(pred)