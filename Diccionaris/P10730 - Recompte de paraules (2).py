from yogi import tokens


def dict_recompte() -> dict[str, int]:
    recompte = {}
    for word in tokens(str):
        word = word.lower()
        if word not in recompte:
            recompte[word] = 1
        else:
            recompte[word] += 1
    return recompte


def print_ordenat(recompte: dict[str, int]) -> None:
    # ordenem primer en funció de les ocurrències i en cas d'empat de les words
    for word, ocurrencies in sorted(recompte.items(), key = lambda x: (x[1], x[0])):
        print(ocurrencies, word)


def main() -> None:
    print_ordenat(dict_recompte())


if __name__ == "__main__":
    main()