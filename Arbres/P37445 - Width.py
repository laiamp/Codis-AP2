from typing import TypeAlias, Optional
from yogi import read
from collections import deque


Bintree: TypeAlias = Optional[tuple[int, 'Bintree', 'Bintree']]

def read_pre() -> Bintree:
    '''read a binary tree given in preorder and returns it'''
    x = read(int)
    if x == -1: 
        return None
    return (x, read_pre(), read_pre())


def width_it(bt: Bintree) -> int:
    '''retorna l'amplada del binary tree bt calculada iterativament
    visitant l'arbre per nivells'''

    if bt is None:
        return 0
    
    pending: deque = deque() # (bt, level)
    # nodes del mateix nivell estan seguits
    width = 0
    max_width = 0
    pre_level = 0
    pending.append((bt, 0))

    while pending:
        subtree, level = pending.popleft()

        if pre_level != level: # hem canviat de nivell
            max_width = max(width, max_width)
            pre_level = level
            width = 1 # amplada del nou nivell
        
        else: #seguim al mateix nivell
            width += 1
        
        if subtree[1] is not None: # left children
            pending.append((subtree[1], level + 1))

        if subtree[2] is not None: # right children
            pending.append((subtree[2], level + 1))
    
    return max(max_width, width) # no haviem comprovat l'ultim nivell


def width_rec(bt: Bintree, level = 0) -> int:
    '''retorna l'amplada de bt calculada recursivament'''
    if bt is None:
        return 0
    
    level_width: list[int] = []
    update_level_width(bt, level, level_width)

    return max(level_width)


def update_level_width(bt, level: int, level_width: list[int]) -> None:
    '''updates level_width
    note: we can not visit a level without visiting the previous level'''
    if bt is None:
        return
      
    if level < len(level_width): # ja havíem estat en aquest nivell
        level_width[level] += 1
    else:
        level_width.append(1)

    
    if bt[1] is not None:
        update_level_width(bt[1], level + 1, level_width)

    if bt[2] is not None:
        update_level_width(bt[2], level + 1, level_width)


def main(): 
    m = read(int)
    
    for _ in range(m):
        bt = read_pre()
        print(width_it(bt))
        #print(width_rec(bt))

main()
