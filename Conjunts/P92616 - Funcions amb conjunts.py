
def average(s: set[float]) -> float:
    return sum(s)/len(s)


def different_elements(l1: list[int], l2: list[int]) -> int:
    '''donades dues llistes, retorna el nombre d'elements diferents 
    que contenen entre les dues'''
    return len(set(l1)|set(l2)) # | és la unió de dos conjunts


def has_duplicates(L: list[int]) -> bool:
    return len(set(L)) != len(L)
    

def extraneous(l1: list[str], l2: list[str]) -> str:
    '''retorna l'element de l2 que no hi és a l1'''
    for x in set(l2) - set(l1): # no hi ha més de 1 extraneous element
        return x


def extraneous_maybe(l1: list[str], l2: list[str]) -> str | None:
    return extraneous(l1, l2)


def different_words(s: str) -> int:
    return len(set(s.lower().split()))

