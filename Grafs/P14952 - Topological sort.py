'''
topological sort can also be performed using dfs
'''

from yogi import read, tokens
from heapq import heappush, heappop


def topological_sort(n, adj, indegree) -> list[int]:
    '''returns a list of the nodes in topological order.
    The algorithm is based on the number of edges that are incident
    in each node'''

    toposort: list[int] = []
    
    cuap: list[int] = [] # nodes with indegree == 0
    for u in range(n):
        if indegree[u] == 0:
            heappush(cuap, u)
    
    while cuap:
        u = heappop(cuap)

        toposort.append(u)
        for v in adj[u]:
            indegree[v] -= 1
            if indegree[v] == 0:
                heappush(cuap, v)

    return toposort


def main() -> None:
    for n in tokens(int):
        m = read(int)
        indegree: list[int] = [0 for _ in range(n)]
        adj: list[list[int]] = [[] for _ in range(n)]

        for _ in range(m):
            u = read(int)
            v = read(int)
            adj[u].append(v)
            indegree[v] += 1

        print(*topological_sort(n, adj, indegree))

main()