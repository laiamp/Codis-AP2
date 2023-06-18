from yogi import read, tokens
from heapq import heappop, heappush

def mst_weight(adj: list[list[tuple[int, int]]]) -> int:
    '''returns the weight of the mst using Prim's algorithm'''

    n = len(adj)
    visited = [False for _ in range(n)]
    visited[0] = True
    num_edges = 0
    min_cost = 0
    cuap: list[tuple[int,int,int]] = [] # weight, node, parent
    
    for v, w in adj[0]:
        heappush(cuap, (w, v))

    while num_edges < n-1:
        cost, u = heappop(cuap)
        
        if not visited[u]:
            min_cost += cost
            num_edges += 1

            visited[u] = True

            for v, w in adj[u]:
                if not visited[v]:
                    heappush(cuap, (w, v))
                    
    return min_cost


def max_savings(adj: list[list[tuple[int, int]]]) -> int:
    n = len(adj)
    min_cost = mst_weight(adj)
    total = sum(edge[1] for u in range(n) for edge in adj[u]) // 2 # comptabilitzo cada edge 2 cops

    return total - min_cost


def main() -> None:
    for n in tokens(int):
        m = read(int)
        adj: list[list[tuple[int,int]]] = [[] for _  in range(n)]
        for _ in range(m):
            x, y, c =  read(int), read(int), read(int)
            adj[x].append((y, c))
            adj[y].append((x, c))

        print(max_savings(adj))

main()