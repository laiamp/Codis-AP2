from yogi import read, tokens


def read_data(n: int, m: int) -> list[set[int]]:
    '''retorna una llista on l'i-essim element es un set amb els
    amics de la persona i'''

    amistats: list[set[int]] = [set() for _ in range(n)]
    for _ in range(m):
        a = read(int)
        b = read(int)
        amistats[a].add(b)
        amistats[b].add(a)

    return amistats


def total_amistats(id: int, amistats: list[set[int]]) -> int:
    '''retorna el total d'amics de id tenint en compte que els amics
    dels seus amics son els seus amics'''

    total = set()
    for amic in amistats[id]:
        total.add(amic)
        for amic_d_amic in amistats[amic]:
            total.add(amic_d_amic)

    if len(total) == 0: 
        return 0
    else: 
        return len(total) - 1 # -1 perquè no es compta a ell mateix


def main() -> None:
    n, m = read(int), read(int)
    amistats: list[set[int]] = read_data(n, m)
    for id in tokens(int):
        print(total_amistats(id, amistats))

    
if __name__ == "__main__":
    main()