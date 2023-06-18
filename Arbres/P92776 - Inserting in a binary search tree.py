from yogi import tokens, read
from typing import Optional, TypeAlias

Bintree: TypeAlias = Optional[list[int, 'Bintree', 'Bintree']]

def print_pre(bt: Bintree) -> None:
    '''prints a binary tree bt in preorder'''
    if bt is not None:
        print(bt[0])
        print_pre(bt[1])
        print_pre(bt[2])


def insert(x: int, bt: Bintree) -> None:
    '''inserts element x recursively into the BST bt'''
    if x < bt[0]:
        if bt[1] is not None:
            insert(x, bt[1])
        else:
            bt[1]: Bintree = [x, None, None]

    elif x > bt[0]:
        if bt[2] is not None:
            insert(x, bt[2])
        else:
            bt[2]: Bintree = [x, None, None]


def create_search_bintree() -> Bintree:
    x = read(int)
    bt: Bintree = [x, None, None]
    for x in tokens(int):
        insert(x, bt)
    
    return bt


def main():
    print_pre(create_search_bintree())

main()