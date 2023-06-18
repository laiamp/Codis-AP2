from yogi import read
from typing import TypeAlias, Optional

Bintree: TypeAlias = Optional[tuple[int, 'Bintree', 'Bintree']]

def read_pre() -> Bintree:
    '''llegeix un arbre binari donat en preordre'''
    x = read(int)
    if x == -1:
        return None
    return (x, read_pre(), read_pre())


def height(bt: Bintree) -> int:
    '''retorna l'alçada d'un arbre binari donat'''
    if bt is None:
        return 0
    return max(height(bt[1]), height(bt[2])) + 1


def main():
    m = read(int)
    for _ in range(m):
        bt = read_pre()
        print(height(bt))


if __name__ == "__main__":
    main()