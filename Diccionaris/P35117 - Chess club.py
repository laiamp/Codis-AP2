from yogi import read, tokens

def player_opponents(color: str, name: str, players: dict[str, list[list[str]]]) -> list[str]:
    '''returns a sorted list of opponents given a player and his/her color'''
    if color == "white": 
        return sorted(players[name][0])
    return sorted(players[name][1])


def read_data(matches: int) -> dict[str, list[list[str]]]:
    # [black opponents, white opponents]
    players: dict[str, list[list[str]]] = {}
    for _ in range(matches): 
        white, black = read(str), read(str)

        if white not in players:
            players[white] = [[black], []]
        else:
            players[white][0].append(black)
        
        if black not in players:
           players[black] = [[], [white]]
        else:
            players[black][1].append(white)

    return players


def queries(players) -> None:
     for s in tokens(str):
        if s == "?":
            color = "black"
            name = read(str)
        else:
            color = "white"
            name, s = s, read(str)

        opponents: list[str] = player_opponents(color, name, players)

        print(f'{name} has played {color} against:')
        for opponent in opponents:
            print(opponent)
        print()
 

def main() -> None:
    matches = read(int)
    players: dict[str, list[list[str]]] = read_data(matches)
    queries(players)

    
if __name__ == "__main__": 
    main()