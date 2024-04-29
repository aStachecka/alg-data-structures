#lab 4
#implementacja algorytmow grafowych
#algorytm A*

import heapq

class AlgorytmA:
    def __init__(self, graph):
        self.graph = graph

    def astar(self, start, goal):
        open_list = [(0, start)]
        visited = set()
        gScores = {node: float('inf') for node in self.graph}
        gScores[start] = 0
        fScores = {node: float('inf') for node in self.graph}
        fScores[start] = self.heuristic(start, goal)
        came_from = {}

        while open_list:
            currentScore, currentNode = heapq.heappop(open_list)

            if currentNode == goal:
                path = self.reconstructPath(start, goal, came_from)
                return path

            visited.add(currentNode)

            for neighbor, cost in self.graph[currentNode].items():
                if neighbor in visited:
                    continue

                ttGScore = gScores[currentNode] + cost

                if ttGScore < gScores[neighbor]:
                    gScores[neighbor] = ttGScore
                    fScores[neighbor] = ttGScore + self.heuristic(neighbor, goal)
                    heapq.heappush(open_list, (fScores[neighbor], neighbor))
                    came_from[neighbor] = currentNode

        return None

    def heuristic(self, node, goal):
        x1, y1 = node
        x2, y2 = goal
        return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

    def reconstructPath(self, start, goal, came_from):
        path = [goal]
        current = goal
        while current != start:
            current = came_from[current]
            path.insert(0, current)
        return path

graph = {
    (0, 0): {(1, 0): 1, (0, 1): 1},
    (1, 0): {(0, 0): 1, (1, 1): 1, (2, 0): 1},
    (0, 1): {(0, 0): 1, (1, 1): 1},
    (1, 1): {(0, 1): 1, (1, 0): 1, (2, 1): 1},
    (2, 0): {(1, 0): 1, (2, 1): 1},
    (2, 1): {(1, 1): 1, (2, 0): 1}
}
startPoint = (0, 0)
goalPoint = (2, 1)

algorytm = AlgorytmA(graph)
path = algorytm.astar(startPoint, goalPoint)

if path:
    print(f"Sciezka od {startPoint} do {goalPoint}: {path}")
else:
    print("Nie znaleziono sciezki.")