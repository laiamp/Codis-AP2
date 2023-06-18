from yogi import read


def dfs_topo(u: int, adj: list[list[int]], visited: list[bool], stack: list[int]) -> None:
    visited[u] = True

    for v in adj[u]:
        if not visited[v]:
            dfs_topo(v, adj, visited, stack)

    stack.append(u)


def toposort(n: int, adj: list[list[int]]) -> list:
    stack: list[int] = []
    visited = [False for _ in range(n)]
    for u in range(n):
        if not visited[u]:
            dfs_topo(u, adj, visited, stack)

    return stack[::-1]


def reverse_graph(adj: list[list[int]]) -> list[list[int]]:
    '''returns an adjacency list from the graph described by adj
    but with the edges reversed'''
    adj_rev: list[list[int]] = [[] for _ in range(len(adj))]
    for u in range(len(adj)):
        for v in adj[u]:
            adj_rev[v].append(u)
    return adj_rev


def dfs_cc(u, adj_rev, visited) -> None:
    visited[u] = True
    for v in adj_rev[u]:
        if not visited[v]:
            dfs_cc(v, adj_rev, visited)


def connected_components(adj) -> int:
    '''returns the number of connected components of the
    graph described by adj'''

    n = len(adj)
    post = toposort(n, adj) # nodes ordenats topologicament
    adj_rev: list[list[int]] = reverse_graph(adj)

    visited = [False for _ in range(n)]


    # si tenim un cc de mida n, un cop es processi el primer element de post d'aquesta cc tindrem els n seguents a visited marcats
    cc = 0
    for u in post:
        if not visited[u]:
            dfs_cc(u, adj_rev, visited) # es crida un cop per cada cc (una crida ja marca tots els nodes de la cc)
            cc += 1

    return cc


def main() -> None:
    t = read(int)

    for i in range(1, t+1):
        n, m = read(int), read(int)
        adj: list[list[int]] = [[] for _ in range(n)]

        for _ in range(m):
            a, b = read(int), read(int)
            adj[a].append(b)

        print(f'Graph #{i} has {connected_components(adj)} strongly connected component(s).')


if __name__ == "__main__":
    main()
