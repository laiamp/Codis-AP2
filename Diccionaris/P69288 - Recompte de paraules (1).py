from yogi import tokens

def print_ocurrencies(ocurrencies: dict[str, int]) -> None:
    for paraula in sorted(ocurrencies.keys()):
        print(paraula, ocurrencies[paraula])


def main() -> None:
    ocurrencies: dict[str, int] = {}

    for paraula in tokens(str):
        paraula = paraula.lower()
        if paraula not in ocurrencies:
            ocurrencies[paraula] = 1
        else:
            ocurrencies[paraula] += 1   

    print_ocurrencies(ocurrencies)   

if __name__ == "__main__":
    main()