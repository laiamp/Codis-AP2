from yogi import read
from typing import TypeAlias, Optional

Bintree: TypeAlias = tuple[int, 'Bintree', 'Bintree'] | None


def read_pre() -> Bintree:
    x = read(int)
    if x == -1:
        return None

    return (x, read_pre(), read_pre())


def print_post(bt: Bintree) -> None:
    if bt is not None:
        print_post(bt[1])
        print_post(bt[2])
        print("", bt[0], end = "")


def print_ino(bt: Bintree) -> None:
    if bt is not None:
        print_ino(bt[1])
        print("", bt[0], end ="")
        print_ino(bt[2])


def main() -> None:
    bt = read_pre()
    print("pos:", end="")
    print_post(bt)
    print("")

    print("ino:", end="")
    print_ino(bt)
    print("")


if __name__  == "__main__":
    main()
