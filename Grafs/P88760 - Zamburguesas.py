from yogi import read, tokens
from dataclasses import dataclass
from math import sqrt
from collections import deque
from typing import TypeAlias


@dataclass
class Rock:
    x: float
    y: float
    radius: float


def can_jump(ori: Rock, dest: Rock, d) -> bool:
    return sqrt((ori.x-dest.x)**2 + (ori.y-dest.y)**2) - ori.radius - dest.radius <= d


def min_jumps(n, d, rocks: list[Rock]) -> int:
    '''returns the minimum jumps in order to go from the first rock to
    the last one (-1 if not possible). Uses BFS'''

    if len(rocks) == 1:
        return 0

    jumps_to_arrive = [-1 for _ in range(n)] # el primer cop que es modifiqui sera valor minim (propietat BFS)
    jumps_to_arrive[0] = 0
    pending: deque[tuple[int, Rock]] = deque() # (idx_rock, rock)
    pending.append((0, rocks[0]))


    while pending:
        idx_rock, current = pending.popleft()

        if can_jump(current, rocks[-1], d):
            return jumps_to_arrive[idx_rock] + 1

        for i, rock in enumerate(rocks):
            if jumps_to_arrive[i] == -1 and can_jump(current, rock, d): # si ja l'havíem visitat (jumps != -1) no ens interessa
                jumps_to_arrive[i] = jumps_to_arrive[idx_rock] + 1
                pending.append((i, rock))

    return -1


def main():
    for n in tokens(int):
        d = read(float)
        rocks = [Rock(read(float), read(float), read(float)) for _ in range(n)]
        jumps = min_jumps(n, d, rocks)
        if jumps == -1:
            print("Xof!")
        else:
            print(jumps)

if __name__ == "__main__":
    main()
