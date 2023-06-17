from yogi import read
from typing import TypeAlias, Optional

Bintree: TypeAlias = Optional[tuple[str, 'Bintree', 'Bintree']]

def read_pre() -> Bintree:
    s = read(str)
    if s == '-1':
        return None
    
    return (s, read_pre(), read_pre())


def print_bt(bt: Bintree, depth = 1) -> None:
    # right, node, left
    # tinc en compte la profunditat per imprimir els espais
    if bt is not None:
        if bt[2] is not None:
            print_bt(bt[2], depth + 1)
        
        print(" "*(10*depth - len(bt[0]) - 1), bt[0])

        if bt[1] is not None:
            print_bt(bt[1], depth + 1)


def main() -> None:
    bt: Bintree = read_pre()
    print_bt(bt)

main()