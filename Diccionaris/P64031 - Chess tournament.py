from yogi import read, tokens

def results_tournament(players: dict[str, list[int]]) -> dict[str, list[int]]:
    # [wins, draws, defeats]

    for name1 in tokens(str):
        name2 = read(str)
        result = read(str)

        if result == "1-0":
            players[name1][0] += 1 # wins
            players[name2][2] += 1 # loses

        elif result == "0-1":
            players[name1][2] += 1 # loses
            players[name2][0] += 1 # wins

        else:
            players[name1][1] += 1 # draw
            players[name2][1] += 1 # draw

    return players


def main() -> None:
    n = read(int)
    players: dict[str, list[int]] = {read(str): [0, 0, 0] for _ in range(n)}
    players = results_tournament(players)

    for name in sorted(players):
        print(name, *players[name])


if __name__ == "__main__":
    main()