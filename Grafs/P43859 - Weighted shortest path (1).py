from yogi import tokens, read
import heapq

def min_cost(x: int, y: int, n: int, nbors: list[list[tuple[int,int]]]) -> int:
    '''retorna el minim cost per anar de x a y utilitzant Dijkstra'''
    dist: list[int] = [-1 for _ in range(n)]
    dist[x] = 0
    used: list[bool] = [False for _ in range(n)]
    pending: list = [] # dist, node
    heapq.heappush(pending, (0, x))

    while pending:

        current = heapq.heappop(pending)[1]

        if used[current]:
            continue

        used[current] = True # ja hem trobat la dist minima per anar a current

        if current == y:
            return dist[y]

        for v, w in nbors[current]:
            if not used[v] and (dist[v] == -1 or dist[v] > dist[current] + w):
                dist[v] = dist[current] + w
                heapq.heappush(pending, (dist[v], v))

    return dist[y]


def main() -> None:
    for n in tokens(int):
        m = read(int)
        nbors: list[list[tuple[int, int]]] = [[] for _ in range(n)]

        for _ in range(m):
            nbors[read(int)].append((read(int), read(int)))

        x, y = read(int), read(int)
        cost = min_cost(x, y, n, nbors)
        
        if cost == -1:
            print(f'no path from {x} to {y}')
        else:
            print(int(cost))

main()
