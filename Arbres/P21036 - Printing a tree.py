from yogi import read
from typing import TypeAlias, Optional

Bintree: TypeAlias = Optional[tuple[str, 'Bintree', 'Bintree']]

def read_pre() -> Bintree:
    '''llegim un arbre binari donat en preordre i el retornem'''
    s = read(str)
    if s == '-1':
        return None
    
    return (s, read_pre(), read_pre())


def print_bt(bt: Bintree, depth = 1) -> None:
    '''imprimim un arbre binari tenint en compte els espais. 
    Els espais depenen de la profunditat del node.
    Recorrem l'arbre en inordre (començant per la dreta)'''
    
    if bt is not None:
        if bt[2] is not None: # right
            print_bt(bt[2], depth + 1)
        
        print(" "*(10*depth - len(bt[0]) - 1), bt[0]) # node

        if bt[1] is not None: # left
            print_bt(bt[1], depth + 1)


def main() -> None:
    bt: Bintree = read_pre()
    print_bt(bt)


if __name__ == "__main__":
    main()
