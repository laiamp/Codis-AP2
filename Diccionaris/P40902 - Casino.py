from yogi import tokens, read

def inside(nom: str, jugadors: dict[str, tuple[bool, int]]) -> bool:
    return jugadors[nom][0]

def casino() -> None:
    jugadors: dict[str, tuple[bool, int]] = {} # jugador: (esta al casino, guanys)
    for nom in tokens(str):
        accio = read(str)

        if nom not in jugadors: # primera aparicio del jugador
            jugadors[nom] = (False, 0)

        if accio == "enters":
            if inside(nom, jugadors): 
                print(nom, "is already in the casino")
            jugadors[nom] = (True, jugadors[nom][1])

        elif accio == "leaves":
            if not inside(nom, jugadors): 
                print(nom, "is not in the casino")
            else:
                print(nom, "has won", jugadors[nom][1])
                jugadors[nom] = (False, 0)

        else:
            amount = read(int)
            if not inside(nom, jugadors): 
                print(nom, "is not in the casino")
            else:
                jugadors[nom] = (jugadors[nom][0], jugadors[nom][1] + amount)

    print("----------")
    
    for nom in sorted(jugadors.keys()): # falten per marxar
        if inside(nom, jugadors): 
            print(nom, "is winning", jugadors[nom][1])


def main():
    casino()
        

if __name__ == "__main__":
    main()