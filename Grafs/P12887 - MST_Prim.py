from yogi import read, tokens
from heapq import heappush, heappop

def mst_prim(n: int, adj: list[list[tuple[int,int]]]):
    '''returns the weight of the MST using Prim's algorithm.
    Idea: in each iteration we want to add the edge with the minimum weight from
    the edges of visited nodes'''

    visited = [False for _ in range(n)]
    visited[0] = True
    edges_mst = 0
    weight_mst = 0

    cuap: list[tuple[int, int]] = [] # edges from visited nodes

    for v, w in adj[0]: # starting node is irrelevant (in this case 0)
        heappush(cuap, (w, v))

    while edges_mst < n-1: # tree property
        w, u = heappop(cuap)

        if not visited[u]:
            weight_mst += w
            visited[u] = True
            edges_mst += 1

            for v, w in adj[u]:
                heappush(cuap, (w, v))

    return weight_mst


def main() -> None:
    for n in tokens(int):
        m = read(int)
        adj: list[list[tuple[int, int]]] = [[] for _ in range(n)]
        for _ in range(m):
            u, v, w = read(int) - 1, read(int) - 1, read(int)
            adj[u].append((v, w))
            adj[v].append((u, w))

        print(mst_prim(n, adj))

main()
