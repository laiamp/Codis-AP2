from yogi import read, tokens
from typing import TypeAlias, Optional

Bintree: TypeAlias = Optional[tuple[int, 'Bintree', 'Bintree']]


def read_pre() -> Bintree:
    '''reads a binary tree given in preorder'''
    x = read(int)
    if x == -1:
        return None
    return (x, read_pre(), read_pre())


def search(bt: Bintree, target: int) -> int:
    '''given a BST, returns 0 if the target is not found,
    and 1 if it is found'''

    if bt is None: 
        return 0

    if bt[0] == target:
        return 1
    
    elif bt[0] > target:
        return search(bt[1], target)
    
    else:
        return search(bt[2], target)
    
    
def main() -> None:
    _ = read(int)
    bt = read_pre()
    for x in tokens(int):
        print(x, search(bt, x))

main()